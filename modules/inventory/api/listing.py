"""
Listings Items API wrapper.

Wraps the ``listings-items-api`` swagger client to fetch listing details
for a given seller SKU: summaries, offers, fulfillment availability, and issues.

NOTE: ``ItemSummaries`` and ``ItemOffers`` container models have empty
``swagger_types`` in the generated SDK, causing the deserializer to silently
drop all data.  We bypass this by requesting the raw HTTP response
(``_preload_content=False``) and parsing the JSON ourselves.
"""

from __future__ import annotations

import json
import logging

from core.api_loader import make_api_client
from core.config import MARKETPLACE_ID

logger = logging.getLogger(__name__)

_INCLUDED_DATA = [
    "summaries",
    "offers",
    "fulfillmentAvailability",
    "issues",
]


def get_listing_item(seller_id: str, sku: str) -> dict:
    """
    Return the listings-items record for a SKU as a plain dict.

    Keys available:
      ``sku``                      — seller SKU
      ``summaries``                — list of per-marketplace summary dicts
      ``offers``                   — list of per-marketplace offer dicts
      ``fulfillment_availability`` — list of fulfillment channel dicts
      ``issues``                   — list of issue dicts
    """
    client = make_api_client("listings-items-api")
    from swagger_client.api.listings_api import ListingsApi  # type: ignore

    api = ListingsApi(client)
    logger.debug("Fetching listing for SKU %s (seller %s)", sku, seller_id)

    # _preload_content=False → returns raw urllib3 HTTPResponse, bypassing
    # the broken model deserializer.
    raw = api.get_listings_item(
        seller_id=seller_id,
        sku=sku,
        marketplace_ids=[MARKETPLACE_ID],
        included_data=_INCLUDED_DATA,
        _preload_content=False,
    )
    data: dict = json.loads(raw.data)
    return {
        "sku": data.get("sku"),
        "summaries": data.get("summaries") or [],
        "offers": data.get("offers") or [],
        "fulfillment_availability": data.get("fulfillmentAvailability") or [],
        "issues": data.get("issues") or [],
    }
