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

MARKETPLACE_ID: str = MARKETPLACE_IDS[REGION][TARGET_COUNTRY]
REGION_HOST: str = _REGION_HOST[REGION]

# ──────────────────────────────────────────────────────────────────────────
# Business logic defaults
# ──────────────────────────────────────────────────────────────────────────

RESTOCK_TARGET_DAYS: int = 60

# Sales API (rate limit: 0.5 req/s — see sales-api docs)
# ──────────────────────────────────────────────────────────────────────────

SALES_API_MIN_INTERVAL: float = float(os.getenv("SALES_API_MIN_INTERVAL", "2.1"))
SALES_API_MAX_RETRIES: int = int(os.getenv("SALES_API_MAX_RETRIES", "6"))
