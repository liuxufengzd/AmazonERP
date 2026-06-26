"""Thread-safe minimum-interval rate limiter for SP-API calls."""

from __future__ import annotations

import threading
import time


class RateLimiter:
    """Enforce at least ``min_interval`` seconds between consecutive calls."""

    def __init__(self, min_interval: float) -> None:
        self._min_interval = min_interval
        self._lock = threading.Lock()
        self._last_at = 0.0

    def wait(self) -> None:
        with self._lock:
            now = time.monotonic()
            delay = self._min_interval - (now - self._last_at)
            if delay > 0:
                time.sleep(delay)
            self._last_at = time.monotonic()
