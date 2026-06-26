"""
Inventory dashboard orchestration.

Coordinates calls to the individual SP-API wrappers and assembles the
final dashboard dict consumed by the display layer.

No display logic lives here; no API implementation logic lives here.
"""

from __future__ import annotations

import logging

from core.config import MARKETPLACE_ID
from modules.inventory.api.catalog import get_catalog_item
from modules.inventory.api.fba import get_inventory_summaries
from modules.inventory.api.fees import get_fees_estimate
from modules.inventory.api.listing import get_listing_item
from modules.inventory.api.restock import fetch_restock_report
from modules.inventory.api.sales import (
    extract_daily_series,
    extract_sales_metrics,
    get_daily_sales,
    get_sales_metrics,
)
from modules.inventory.replenishment import compute_replenishment

logger = logging.getLogger(__name__)


# ──────────────────────────────────────────────────────────────────────────
# Internal helpers
# ──────────────────────────────────────────────────────────────────────────


def _inventory_section(sku: str) -> tuple[dict, str | None, str | None, str | None]:
    """
    Fetch FBA inventory for a SKU.
    Returns (inventory_dict, asin, fnsku, condition).
    """
    summaries = get_inventory_summaries(seller_sku=sku)
    if not summaries:
        logger.info("No inventory record found for SKU %s", sku)
        return {}, None, None, None

    s = summaries[0]
    d = getattr(s, "inventory_details", None)

    inventory = {
        "total_quantity": getattr(s, "total_quantity", None),
        "fulfillable_qty": getattr(d, "fulfillable_quantity", None) if d else None,
        "inbound_working_qty": getattr(d, "inbound_working_quantity", None) if d else None,
        "inbound_shipped_qty": getattr(d, "inbound_shipped_quantity", None) if d else None,
        "inbound_receiving_qty": getattr(d, "inbound_receiving_quantity", None) if d else None,
        "reserved_qty": getattr(d, "reserved_quantity", None) if d else None,
        "unfulfillable_qty": getattr(d, "unfulfillable_quantity", None) if d else None,
        "last_updated": str(getattr(s, "last_updated_time", "")),
    }
    return (
        inventory,
        getattr(s, "asin", None),
        getattr(s, "fn_sku", None),
        getattr(s, "condition", None),
    )


def _listing_section(seller_id: str, sku: str, fallback_asin: str | None) -> dict:
    """
    Fetch listing details and return a structured dict.
    get_listing_item() now returns a raw dict (bypassing broken swagger deserializer).
    """
    item: dict = get_listing_item(seller_id, sku)

    summaries_l: list = item.get("summaries") or []
    offers_l:    list = item.get("offers")     or []
    fa_l:        list = item.get("fulfillment_availability") or []
    issues_l:    list = item.get("issues")     or []
    first_s: dict = summaries_l[0] if summaries_l else {}

    def _parse_price(offer: dict) -> dict:
        # Listings API v2021-08-01: offer["price"] = {"currencyCode": "...", "amount": "..."}
        p = offer.get("price") or {}
        raw_amount = p.get("amount")
        try:
            amount = float(raw_amount) if raw_amount is not None else None
        except (TypeError, ValueError):
            amount = None
        return {
            "amount": amount,
            "currency": p.get("currencyCode"),
        }

    return {
        "item_name": first_s.get("itemName"),
        "condition": first_s.get("conditionType"),
        "status": first_s.get("status") or [],
        "created_date": first_s.get("createdDate"),
        "asin": first_s.get("asin") or fallback_asin,
        "offers": [
            {
                "listing_price": _parse_price(o),
                "points": o.get("points"),
                "fulfillment_channel": o.get("offerType"),
            }
            for o in offers_l
        ],
        "fulfillment_availability": [
            {
                "channel": fa.get("fulfillmentChannelCode"),
                "quantity": fa.get("quantity"),
                "lead_time": fa.get("fulfillmentLeadTime"),
            }
            for fa in fa_l
        ],
        "issues": [
            {
                "severity": i.get("severity"),
                "message": i.get("message"),
            }
            for i in issues_l
        ],
    }


def _catalog_section(asin: str) -> dict:
    """
    Fetch catalog/product details for an ASIN and return a structured dict.
    get_catalog_item() now returns a raw dict (bypassing broken swagger deserializer).
    """
    cat: dict = get_catalog_item(asin)

    # summaries is a list; pick the first entry
    summaries: list = cat.get("summaries") or []
    cs: dict = summaries[0] if summaries else {}

    # Images: list of per-marketplace blocks, each with an "images" list
    main_image: str | None = None
    for img_block in (cat.get("images") or []):
        for img in (img_block.get("images") or []):
            if img.get("variant") == "MAIN":
                main_image = img.get("link")
                break
        if main_image:
            break

    # Identifiers: list of per-marketplace blocks, each with an "identifiers" list
    ext_ids: dict = {}
    for id_block in (cat.get("identifiers") or []):
        for id_obj in (id_block.get("identifiers") or []):
            ext_ids[id_obj.get("identifierType", "?")] = id_obj.get("identifier")

    # Sales ranks: list of per-marketplace blocks
    # Each block may have "classificationRanks" and/or "displayGroupRanks"
    sales_ranks: list[dict] = []
    for rank_block in (cat.get("sales_ranks") or []):
        for r in (rank_block.get("classificationRanks") or []):
            sales_ranks.append({
                "title": r.get("title"),
                "rank": r.get("rank"),
                "link": r.get("link"),
            })
        for r in (rank_block.get("displayGroupRanks") or []):
            sales_ranks.append({
                "title": r.get("title"),
                "rank": r.get("rank"),
                "link": r.get("link"),
            })

    return {
        "asin": asin,
        "title": cs.get("itemName"),
        "brand": cs.get("brand"),
        "manufacturer": cs.get("manufacturer"),
        "model_number": cs.get("modelNumber"),
        "color": cs.get("color"),
        "size": cs.get("size"),
        "item_class": cs.get("itemClassification"),
        "identifiers": ext_ids,
        "main_image": main_image,
        "sales_ranks": sales_ranks,
    }


def _sales_section(sku: str, asin: str | None) -> dict:
    """
    Fetch aggregated (1/7/30/90-day) and 30-day daily sales metrics.
    Falls back to ASIN-level data when SKU returns zero.
    """
    agg_1d  = extract_sales_metrics(get_sales_metrics(sku=sku, days=1,  asin=asin))
    agg_7d  = extract_sales_metrics(get_sales_metrics(sku=sku, days=7,  asin=asin))
    agg_30d = extract_sales_metrics(get_sales_metrics(sku=sku, days=30, asin=asin))
    agg_90d = extract_sales_metrics(get_sales_metrics(sku=sku, days=90, asin=asin))

    daily_raw    = get_daily_sales(sku=sku, days=30, asin=asin)
    daily_series = extract_daily_series(daily_raw)

    return {
        "last_1_day":   agg_1d,
        "last_7_days":  agg_7d,
        "last_30_days": agg_30d,
        "last_90_days": agg_90d,
        "daily_series": daily_series,
    }


def _fees_section(asin: str, listing: dict) -> dict:
    """Fetch FBA fee estimate if a listing price is available."""
    offers = listing.get("offers") or []
    price_offer = next(
        (o for o in offers if o.get("listing_price", {}).get("amount") is not None),
        None,
    )
    if not price_offer:
        return {}

    price    = price_offer["listing_price"]["amount"]
    currency = price_offer["listing_price"].get("currency") or "JPY"

    try:
        return get_fees_estimate(asin=asin, price=float(price), currency=currency)
    except Exception:
        logger.exception("Fees estimate failed for ASIN %s", asin)
        return {}


def _restock_report_section(sku: str) -> dict:
    """Fetch and extract the restock report row for a specific SKU."""
    rows = fetch_restock_report()
    row = next(
        (r for r in rows if r.get("sku") == sku or r.get("seller-sku") == sku),
        None,
    )
    if not row:
        return {"note": "SKU not found in restock report"}

    return {
        "days_of_supply": row.get("days-of-supply") or row.get("Days of Supply"),
        "recommended_qty": row.get("recommended-replenishment-qty")
            or row.get("Recommended Replenishment Qty"),
        "reorder_date": row.get("reorder-date") or row.get("Reorder Date"),
        "alert": row.get("alert") or row.get("Alert"),
        "unit_sales_7d": row.get("unit-sales-7-day"),
        "unit_sales_30d": row.get("unit-sales-30-day"),
        "unit_sales_90d": row.get("unit-sales-90-day"),
    }


# ──────────────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────────────


def fetch_sku_dashboard(
    seller_id: str,
    sku: str,
    include_restock_report: bool = False,
) -> dict:
    """
    Collect and return all information for a single SKU.

    Steps:
      1. FBA Inventory API          → asin, fnsku, qty breakdown
      2. Listings Items API         → price, status, issues
      3. Catalog Items API          → title, brand, image, identifiers, ranks
      4. Sales API (1/7/30/90 day)  → sales metrics + daily series
      5. Product Fees API           → FBA fee estimate
      6. Replenishment computation  → days-of-supply, suggested order qty
    """
    result: dict = {"sku": sku, "marketplace_id": MARKETPLACE_ID}

    # ── Step 1: FBA Inventory ──────────────────────────────────────────
    logger.info("[1/6] FBA Inventory for SKU: %s", sku)
    try:
        inventory, asin, fnsku, condition = _inventory_section(sku)
        result.update({"asin": asin, "fnsku": fnsku, "condition": condition, "inventory": inventory})
    except Exception:
        logger.exception("Inventory fetch failed for SKU %s", sku)
        result.update({"asin": None, "fnsku": None, "condition": None, "inventory": {}})

    # ── Step 2: Listing Details ────────────────────────────────────────
    logger.info("[2/6] Listing details for SKU: %s", sku)
    try:
        result["listing"] = _listing_section(seller_id, sku, result.get("asin"))
        if not result.get("asin") and result["listing"].get("asin"):
            result["asin"] = result["listing"]["asin"]
    except Exception:
        logger.exception("Listing fetch failed for SKU %s", sku)
        result["listing"] = {}

    asin = result.get("asin")

    # ── Step 3: Catalog Details ────────────────────────────────────────
    if asin:
        logger.info("[3/6] Catalog details for ASIN: %s", asin)
        try:
            result["product"] = _catalog_section(asin)
        except Exception:
            logger.exception("Catalog fetch failed for ASIN %s", asin)
            result["product"] = {"asin": asin}
    else:
        logger.info("[3/6] Skipping catalog — ASIN not available")
        result["product"] = {}

    # ── Step 4: Sales Metrics ──────────────────────────────────────────
    logger.info("[4/6] Sales metrics for SKU: %s", sku)
    try:
        result["sales"] = _sales_section(sku=sku, asin=asin)
    except Exception:
        logger.exception("Sales fetch failed for SKU %s", sku)
        result["sales"] = {}

    # ── Step 5: FBA Fees ───────────────────────────────────────────────
    if asin:
        logger.info("[5/6] FBA fees estimate for ASIN: %s", asin)
        try:
            result["fees"] = _fees_section(asin=asin, listing=result.get("listing", {}))
        except Exception:
            logger.exception("Fees fetch failed for ASIN %s", asin)
            result["fees"] = {}
    else:
        result["fees"] = {}

    # ── Step 6: Replenishment ──────────────────────────────────────────
    logger.info("[6/6] Computing replenishment for SKU: %s", sku)
    inv = result.get("inventory", {})
    fulfillable = inv.get("fulfillable_qty") or 0
    inbound = (
        (inv.get("inbound_working_qty") or 0)
        + (inv.get("inbound_shipped_qty") or 0)
        + (inv.get("inbound_receiving_qty") or 0)
    )
    sales_data = result.get("sales", {})
    unit_30d = (sales_data.get("last_30_days") or {}).get("unit_count") or 0
    unit_90d = (sales_data.get("last_90_days") or {}).get("unit_count") or 0

    result["replenishment_computed"] = compute_replenishment(
        fulfillable_qty=fulfillable,
        inbound_qty=inbound,
        unit_count_30d=unit_30d,
        unit_count_90d=unit_90d,
    )

    if include_restock_report:
        logger.info("Fetching FBA Restock report (may take 1–5 min) …")
        try:
            result["replenishment_report"] = _restock_report_section(sku)
        except Exception:
            logger.exception("Restock report fetch failed for SKU %s", sku)
            result["replenishment_report"] = {"error": "Restock report fetch failed"}
    else:
        result["replenishment_report"] = {
            "note": "Pass ?restock=true to fetch the official Amazon restock report"
        }

    return result


def fetch_all_inventory_overview() -> list[dict]:
    """
    Fetch inventory summaries for all active FBA SKUs (no catalog/sales calls).
    """
    logger.info("Fetching full FBA inventory …")
    summaries = get_inventory_summaries()

    rows = []
    for s in summaries:
        d = getattr(s, "inventory_details", None)
        rows.append(
            {
                "sku": getattr(s, "seller_sku", None),
                "asin": getattr(s, "asin", None),
                "fnsku": getattr(s, "fn_sku", None),
                "condition": getattr(s, "condition", None),
                "total_qty": getattr(s, "total_quantity", None),
                "fulfillable_qty": getattr(d, "fulfillable_quantity", None) if d else None,
                "inbound_working_qty": getattr(d, "inbound_working_quantity", None) if d else None,
                "inbound_shipped_qty": getattr(d, "inbound_shipped_quantity", None) if d else None,
                "inbound_receiving_qty": getattr(d, "inbound_receiving_quantity", None) if d else None,
                "reserved_qty": getattr(d, "reserved_quantity", None) if d else None,
                "unfulfillable_qty": getattr(d, "unfulfillable_quantity", None) if d else None,
            }
        )
    return rows
