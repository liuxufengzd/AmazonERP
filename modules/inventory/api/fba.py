"""
FBA Inventory API wrapper.

Wraps the ``fba-inventory-api`` swagger client to fetch inventory summaries
with full detail breakdown (fulfillable, inbound, reserved, unfulfillable).

The swagger codegen emits container models with empty ``swagger_types``,
so we request the raw HTTP response (``_preload_content=False``) and parse
the JSON ourselves — the same approach used by listing, catalog, and sales.
"""

from __future__ import annotations

import logging
from typing import Any

from core.api_loader import load_json_response, make_api_client
from core.config import MARKETPLACE_ID

logger = logging.getLogger(__name__)


def parse_inventory_summary(raw: dict[str, Any]) -> dict[str, Any]:
    """Normalize one FBA inventory summary API record into a flat dict."""
    details = raw.get("inventoryDetails") or {}
    reserved = details.get("reservedQuantity") or {}
    unfulfillable = details.get("unfulfillableQuantity") or {}

    return {
        "sku": raw.get("sellerSku"),
        "asin": raw.get("asin"),
        "fnsku": raw.get("fnSku"),
        "condition": raw.get("condition"),
        "total_qty": raw.get("totalQuantity"),
        "fulfillable_qty": details.get("fulfillableQuantity"),
        "inbound_working_qty": details.get("inboundWorkingQuantity"),
        "inbound_shipped_qty": details.get("inboundShippedQuantity"),
        "inbound_receiving_qty": details.get("inboundReceivingQuantity"),
        "reserved_qty": reserved.get("totalReservedQuantity"),
        "unfulfillable_qty": unfulfillable.get("totalUnfulfillableQuantity"),
        "last_updated": raw.get("lastUpdatedTime"),
    }


def get_inventory_summaries(
    seller_sku: str | None = None,
    seller_skus: list[str] | None = None,
) -> list[dict[str, Any]]:
    """
    Fetch FBA inventory summaries with full detail breakdown.

    Pass ``seller_sku`` to filter to a single SKU, ``seller_skus`` for a batch,
    or neither to retrieve all active FBA SKUs.
    """
    client = make_api_client("fba-inventory-api")
    from swagger_client.api.fba_inventory_api import FbaInventoryApi  # type: ignore

    api = FbaInventoryApi(client)
    kwargs: dict[str, Any] = {"details": True}
    if seller_sku:
        kwargs["seller_sku"] = seller_sku
    if seller_skus:
        kwargs["seller_skus"] = seller_skus

    all_summaries: list[dict[str, Any]] = []
    next_token: str | None = None

    while True:
        if next_token:
            kwargs["next_token"] = next_token
        else:
            kwargs.pop("next_token", None)

        raw = api.get_inventory_summaries(
            granularity_type="Marketplace",
            granularity_id=MARKETPLACE_ID,
            marketplace_ids=[MARKETPLACE_ID],
            _preload_content=False,
            **kwargs,
        )
        data: dict[str, Any] = load_json_response(raw)
        payload = data.get("payload") or {}
        raw_batch = payload.get("inventorySummaries") or []
        all_summaries.extend(parse_inventory_summary(item) for item in raw_batch)

        pagination = data.get("pagination") or {}
        next_token = pagination.get("nextToken")
        if not next_token:
            break

    logger.debug("Fetched %d inventory summaries", len(all_summaries))
    return all_summaries
