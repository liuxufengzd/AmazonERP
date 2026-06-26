"""
Catalog Items API wrapper.

Wraps the ``catalog-items-api`` swagger client to fetch product details
by ASIN: title, brand, identifiers, images, and sales ranks.

NOTE: Several swagger-codegen container models (ItemSummaries, ItemImages,
ItemIdentifiers, ItemSalesRanks) have empty ``swagger_types``, causing the
SDK deserializer to silently drop their contents.  We bypass this by
requesting the raw HTTP response (``_preload_content=False``) and parsing
the JSON ourselves.
"""

from __future__ import annotations

import json
import logging

from core.api_loader import make_api_client
from core.config import MARKETPLACE_ID, TARGET_COUNTRY

logger = logging.getLogger(__name__)

_LOCALE_MAP: dict[str, str] = {
    "JP": "ja_JP",
    "US": "en_US",
    "AU": "en_AU",
    "SG": "en_SG",
    "DE": "de_DE",
    "UK": "en_GB",
}

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
    locale = _LOCALE_MAP.get(TARGET_COUNTRY, "en_US")
    logger.debug("Fetching catalog for ASIN %s (locale %s)", asin, locale)

    # _preload_content=False → returns raw urllib3 HTTPResponse, bypassing
    # the broken model deserializer.
    raw = api.get_catalog_item(
        asin=asin,
        marketplace_ids=[MARKETPLACE_ID],
        included_data=_INCLUDED_DATA,
        locale=locale,
        _preload_content=False,
    )
    data: dict = json.loads(raw.data)
    return {
        "asin": data.get("asin"),
        "summaries": data.get("summaries") or [],
        "images": data.get("images") or [],
        "identifiers": data.get("identifiers") or [],
        "sales_ranks": data.get("salesRanks") or [],
    }
