"""
FastAPI router for the Inventory module.

Endpoints
---------
  GET /api/inventory/           List all FBA inventory (overview, fast)
  GET /api/inventory/{sku}      Full SKU dashboard (product + sales)
"""

from __future__ import annotations

import logging
from typing import Any

from fastapi import APIRouter, HTTPException

from core.config import SELLER_ID
from modules.inventory.dashboard import (
    fetch_all_inventory_overview,
    fetch_sku_dashboard,
)

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/",
    summary="List all FBA inventory",
    response_description="Compact list of all active FBA SKUs with inventory quantities",
)
def list_inventory() -> list[dict[str, Any]]:
    """
    Fetch FBA inventory summaries for every active SKU.

    Returns a compact list with quantity breakdown (fulfillable, inbound,
    reserved, unfulfillable).  No catalog or sales API calls are made, so
    this endpoint is fast even with a large catalogue.
    """
    try:
        return fetch_all_inventory_overview()
    except Exception as exc:
        logger.exception("list_inventory failed")
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.get(
    "/{sku}",
    summary="Get full SKU dashboard",
    response_description="Complete dashboard including product, listing and sales",
)
def get_sku_dashboard(sku: str) -> dict[str, Any]:
    """
    Collect and return all available information for a single seller SKU.

    Calls (in order):
    1. FBA Inventory API
    2. Listings Items API
    3. Catalog Items API
    4. Sales API (1/7/30/90 day)
    5. Product Fees API
    6. Replenishment computation (days-of-supply, suggested order qty)
    """
    if not SELLER_ID:
        raise HTTPException(
            status_code=503,
            detail="SELLER_ID is not configured. Check your environment variables.",
        )
    try:
        return fetch_sku_dashboard(seller_id=SELLER_ID, sku=sku)
    except Exception as exc:
        logger.exception("get_sku_dashboard failed for SKU=%s", sku)
        raise HTTPException(status_code=500, detail=str(exc)) from exc
