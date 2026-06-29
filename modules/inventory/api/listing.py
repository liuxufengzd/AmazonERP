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

import logging

from core.api_loader import load_json_response, make_api_client
from core.config import MARKETPLACE_ID

logger = logging.getLogger(__name__)

_BUYABLE_STATUS = "BUYABLE"
_SEARCH_PAGE_SIZE = 20

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

    raw = api.get_listings_item(
        seller_id=seller_id,
        sku=sku,
        marketplace_ids=[MARKETPLACE_ID],
        included_data=_INCLUDED_DATA,
        _preload_content=False,
    )
    data: dict = load_json_response(raw)
    return {
        "sku": data.get("sku"),
        "summaries": data.get("summaries") or [],
        "offers": data.get("offers") or [],
        "fulfillment_availability": data.get("fulfillmentAvailability") or [],
        "issues": data.get("issues") or [],
    }


def _listing_is_buyable(item: dict) -> bool:
    """Return True when the listing can be purchased on the configured marketplace."""
    for summary in item.get("summaries") or []:
        if summary.get("marketplaceId") != MARKETPLACE_ID:
            continue
        if _BUYABLE_STATUS in (summary.get("status") or []):
            return True
    return False


def get_active_skus_from_list(seller_id: str, skus: list[str]) -> set[str]:
    """Return the subset of *skus* whose listings are still buyable on Amazon."""
    if not skus:
        return set()

    client = make_api_client("listings-items-api")
    from swagger_client.api.listings_api import ListingsApi  # type: ignore

    api = ListingsApi(client)
    active: set[str] = set()

    for offset in range(0, len(skus), _SEARCH_PAGE_SIZE):
        batch = skus[offset : offset + _SEARCH_PAGE_SIZE]
        page_token: str | None = None

        while True:
            kwargs: dict = {
                "identifiers": batch,
                "identifiers_type": "SKU",
                "included_data": ["summaries"],
                "with_status": [_BUYABLE_STATUS],
                "page_size": _SEARCH_PAGE_SIZE,
                "_preload_content": False,
            }
            if page_token:
                kwargs["page_token"] = page_token

            raw = api.search_listings_items(
                seller_id=seller_id,
                marketplace_ids=[MARKETPLACE_ID],
                **kwargs,
            )
            data: dict = load_json_response(raw)

            for item in data.get("items") or []:
                sku = item.get("sku")
                if sku and _listing_is_buyable(item):
                    active.add(sku)

            pagination = data.get("pagination") or {}
            page_token = pagination.get("nextToken")
            if not page_token:
                break

    logger.debug(
        "Listing status check: %d buyable of %d FBA SKUs",
        len(active),
        len(skus),
    )
    return active
