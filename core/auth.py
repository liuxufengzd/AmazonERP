"""
LWA (Login with Amazon) authentication.

Manages access-token acquisition and caching.  The token is refreshed
automatically when it falls within 60 seconds of expiry.
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field

import requests

from core.config import CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN

logger = logging.getLogger(__name__)

_LWA_TOKEN_URL = "https://api.amazon.com/auth/o2/token"
_EXPIRY_BUFFER_SECONDS = 60


@dataclass
class _TokenCache:
    access_token: str | None = field(default=None)
    expires_at: float = field(default=0.0)

    def is_valid(self, now: float) -> bool:
        return (
            self.access_token is not None
            and now < self.expires_at - _EXPIRY_BUFFER_SECONDS
        )


_cache = _TokenCache()


def get_access_token() -> str:
    """Return a valid LWA access token, refreshing if near expiry."""
    now = time.time()
    if _cache.is_valid(now):
        return _cache.access_token

    logger.debug("Refreshing LWA access token")
    resp = requests.post(
        _LWA_TOKEN_URL,
        data={
            "grant_type": "refresh_token",
            "refresh_token": REFRESH_TOKEN,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
        timeout=15,
    )
    resp.raise_for_status()
    payload = resp.json()

    _cache.access_token = payload["access_token"]
    _cache.expires_at = now + payload.get("expires_in", 3600)
    return _cache.access_token
