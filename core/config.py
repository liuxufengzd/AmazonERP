"""
Shared configuration for the Amazon ERP project.

All values are loaded from environment variables (via .env).
Import from this module anywhere a configuration constant is needed.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# ──────────────────────────────────────────────────────────────────────────
# Credentials & region (from .env)
# ──────────────────────────────────────────────────────────────────────────

CLIENT_ID: str = os.getenv("CLIENT_ID", "")
CLIENT_SECRET: str = os.getenv("CLIENT_SECRET", "")
REFRESH_TOKEN: str = os.getenv("REFRESH_TOKEN", "")
REGION: str = os.getenv("REGION", "FE")
SELLER_ID: str = os.getenv("SELLER_ID", "")
TARGET_COUNTRY: str = os.getenv("TARGET_COUNTRY", "JP")

# Resolved absolute path to the auto-generated SP-API client packages
CLIENT_BASE_PATH: Path = Path(__file__).resolve().parent.parent / "clients"

# ──────────────────────────────────────────────────────────────────────────
# SP-API regional endpoints
# ──────────────────────────────────────────────────────────────────────────

_REGION_HOST: dict[str, str] = {
    "NA": "sellingpartnerapi-na.amazon.com",
    "EU": "sellingpartnerapi-eu.amazon.com",
    "FE": "sellingpartnerapi-fe.amazon.com",
}

# ──────────────────────────────────────────────────────────────────────────
# Marketplace IDs by region → country
# ──────────────────────────────────────────────────────────────────────────

MARKETPLACE_IDS: dict[str, dict[str, str]] = {
    "FE": {
        "JP": "A1VC38T7YXB528",
        "AU": "A39IBJ37TRP1C6",
        "SG": "A19VAU5U5O7RUS",
    },
    "NA": {
        "US": "ATVPDKIKX0DER",
        "CA": "A2EUQ1WTGCTBG2",
        "MX": "A1AM78C64UM0Y8",
    },
    "EU": {
        "DE": "A1PA6795UKMFR9",
        "UK": "A1F83G8C2ARO7P",
        "FR": "A13V1IB3VIYZZH",
        "JP": "A1VC38T7YXB528",
    },
}

# Per-country locale and timezone used by Catalog and Sales API calls.
MARKETPLACE_LOCALE: dict[str, str] = {
    "JP": "ja_JP",
    "US": "en_US",
    "AU": "en_AU",
    "SG": "en_SG",
    "DE": "de_DE",
    "UK": "en_GB",
}

MARKETPLACE_TIMEZONE: dict[str, str] = {
    "JP": "Asia/Tokyo",
    "US": "US/Eastern",
    "AU": "Australia/Sydney",
    "SG": "Asia/Singapore",
    "DE": "Europe/Berlin",
    "UK": "Europe/London",
}


def _resolve_region_host(region: str) -> str:
    host = _REGION_HOST.get(region)
    if host is None:
        valid = ", ".join(sorted(_REGION_HOST))
        raise ValueError(f"Invalid REGION={region!r}. Expected one of: {valid}")
    return host


def _resolve_marketplace_id(region: str, country: str) -> str:
    by_country = MARKETPLACE_IDS.get(region)
    if by_country is None:
        valid = ", ".join(sorted(MARKETPLACE_IDS))
        raise ValueError(f"Invalid REGION={region!r}. Expected one of: {valid}")
    marketplace_id = by_country.get(country)
    if marketplace_id is None:
        valid = ", ".join(sorted(by_country))
        raise ValueError(
            f"Invalid TARGET_COUNTRY={country!r} for REGION={region!r}. "
            f"Expected one of: {valid}"
        )
    return marketplace_id


MARKETPLACE_ID: str = _resolve_marketplace_id(REGION, TARGET_COUNTRY)
REGION_HOST: str = _resolve_region_host(REGION)
CATALOG_LOCALE: str = MARKETPLACE_LOCALE.get(TARGET_COUNTRY, "en_US")
SALES_TIMEZONE: str = MARKETPLACE_TIMEZONE.get(TARGET_COUNTRY, "UTC")

# ──────────────────────────────────────────────────────────────────────────
# Business logic defaults
# ──────────────────────────────────────────────────────────────────────────

RESTOCK_TARGET_DAYS: int = 60
