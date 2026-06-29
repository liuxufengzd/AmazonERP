"""
Catalog Items API wrapper.

Wraps the ``catalog-items-api`` swagger client to fetch product details
by ASIN: title, brand, identifiers, images, and sales ranks.

NOTE: Several swagger-codegen container models have empty ``swagger_types``,
causing the SDK deserializer to silently drop their contents.  We bypass this
by requesting the raw HTTP response (``_preload_content=False``) and parsing
the JSON ourselves.
"""

from __future__ import annotations

import logging

from core.api_loader import load_json_response, make_api_client
from core.config import CATALOG_LOCALE, MARKETPLACE_ID

logger = logging.getLogger(__name__)

_INCLUDED_DATA = [
    "summaries",
    "identifiers",
    "images",
    "salesRanks",
]


def get_catalog_item(asin: str) -> dict:
    """
    Return catalog details for an ASIN as a plain dict.

    Keys available:
      ``asin``        — ASIN string
      ``summaries``   — list of per-marketplace summary dicts
      ``images``      — list of per-marketplace image dicts
      ``identifiers`` — list of per-marketplace identifier dicts
      ``sales_ranks`` — list of per-marketplace rank dicts
    """
    client = make_api_client("catalog-items-api")
    from swagger_client.api.catalog_api import CatalogApi  # type: ignore

    api = CatalogApi(client)
    logger.debug("Fetching catalog for ASIN %s (locale %s)", asin, CATALOG_LOCALE)

    raw = api.get_catalog_item(
        asin=asin,
        marketplace_ids=[MARKETPLACE_ID],
        included_data=_INCLUDED_DATA,
        locale=CATALOG_LOCALE,
        _preload_content=False,
    )
    data: dict = load_json_response(raw)
    return {
        "asin": data.get("asin"),
        "summaries": data.get("summaries") or [],
        "images": data.get("images") or [],
        "identifiers": data.get("identifiers") or [],
        "sales_ranks": data.get("salesRanks") or [],
    }
