"""
FBA Inventory API wrapper.

Wraps the ``fba-inventory-api`` swagger client to fetch inventory summaries
with full detail breakdown (fulfillable, inbound, reserved, unfulfillable).

The swagger codegen emits ``InventorySummaries`` with empty ``swagger_types``,
so the API client returns the JSON array as raw dicts.  ``_deserialize_summary``
manually constructs the typed objects.
"""

from __future__ import annotations

import logging
from typing import Optional

from core.api_loader import activate_package, make_api_client
from core.config import MARKETPLACE_ID

logger = logging.getLogger(__name__)


def _deserialize_summary(raw: dict | object) -> object:
    """Convert a raw inventory dict into a typed ``InventorySummary`` object."""
    if not isinstance(raw, dict):
        return raw

    activate_package("fba-inventory-api")
    from swagger_client.models.inventory_summary import InventorySummary  # type: ignore
    from swagger_client.models.inventory_details import InventoryDetails  # type: ignore

    d_raw = raw.get("inventoryDetails") or {}
    details = (
        InventoryDetails(
            fulfillable_quantity=d_raw.get("fulfillableQuantity"),
            inbound_working_quantity=d_raw.get("inboundWorkingQuantity"),
            inbound_shipped_quantity=d_raw.get("inboundShippedQuantity"),
            inbound_receiving_quantity=d_raw.get("inboundReceivingQuantity"),
        )
        if d_raw
        else None
    )

    return InventorySummary(
        asin=raw.get("asin"),
        fn_sku=raw.get("fnSku"),
        seller_sku=raw.get("sellerSku"),
        condition=raw.get("condition"),
        inventory_details=details,
        total_quantity=raw.get("totalQuantity"),
        last_updated_time=raw.get("lastUpdatedTime"),
    )


def get_inventory_summaries(
    seller_sku: Optional[str] = None,
    seller_skus: Optional[list[str]] = None,
) -> list:
    """
    Fetch FBA inventory summaries with full detail breakdown.

    Pass ``seller_sku`` to filter to a single SKU, ``seller_skus`` for a batch,
    or neither to retrieve all active FBA SKUs.

    Returns a list of ``InventorySummary`` objects.
    """
    client = make_api_client("fba-inventory-api")
    from swagger_client.api.fba_inventory_api import FbaInventoryApi  # type: ignore

    api = FbaInventoryApi(client)
    kwargs: dict = {"details": True}
    if seller_sku:
        kwargs["seller_sku"] = seller_sku
    if seller_skus:
        kwargs["seller_skus"] = seller_skus

    all_summaries: list = []
    next_token: Optional[str] = None

    while True:
        if next_token:
            kwargs["next_token"] = next_token

        resp = api.get_inventory_summaries(
            granularity_type="Marketplace",
            granularity_id=MARKETPLACE_ID,
            marketplace_ids=[MARKETPLACE_ID],
            **kwargs,
        )
        payload = getattr(resp, "payload", None)
        raw_batch = (
            (getattr(payload, "inventory_summaries", []) or []) if payload else []
        )
        all_summaries.extend(_deserialize_summary(item) for item in raw_batch)

        pagination = getattr(resp, "pagination", None)
        next_token = getattr(pagination, "next_token", None) if pagination else None
        if not next_token:
            break

    logger.debug("Fetched %d inventory summaries", len(all_summaries))
    return all_summaries
