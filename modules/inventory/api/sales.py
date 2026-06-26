"""
Sales API wrapper.

Wraps the ``sales-api`` swagger client to fetch aggregated order metrics
for a SKU (or ASIN) over configurable trailing-day windows, plus a
day-by-day breakdown used for the trend chart.

NOTE: ``OrderMetricsList`` has empty ``swagger_types`` in the generated SDK,
causing the deserializer to silently drop all payload data.  We bypass this
by requesting the raw HTTP response (``_preload_content=False``) and parsing
the JSON ourselves.

JSON field reference (from OrderMetricsInterval.attribute_map):
  interval          → "interval"
  unit_count        → "unitCount"
  order_item_count  → "orderItemCount"
  order_count       → "orderCount"
  average_unit_price→ "averageUnitPrice"  {currencyCode, amount}
  total_sales       → "totalSales"        {currencyCode, amount}
"""

from __future__ import annotations

import datetime
import json
import logging
import time

from core.api_loader import make_api_client
from core.config import (
    MARKETPLACE_ID,
    SALES_API_MAX_RETRIES,
    SALES_API_MIN_INTERVAL,
    TARGET_COUNTRY,
)
from core.rate_limit import RateLimiter

logger = logging.getLogger(__name__)

_SALES_LIMITER = RateLimiter(SALES_API_MIN_INTERVAL)

_TZ_MAP: dict[str, str] = {
    "JP": "Asia/Tokyo",
    "US": "US/Eastern",
    "AU": "Australia/Sydney",
    "SG": "Asia/Singapore",
    "DE": "Europe/Berlin",
    "UK": "Europe/London",
}
_GRANULARITY_TZ = _TZ_MAP.get(TARGET_COUNTRY, "UTC")


def _make_interval(days: int) -> str:
    """Return ISO-8601 interval string for the past ``days`` days in UTC."""
    end   = datetime.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    start = end - datetime.timedelta(days=days)
    return (
        f"{start.strftime('%Y-%m-%dT%H:%M:%SZ')}"
        f"--{end.strftime('%Y-%m-%dT%H:%M:%SZ')}"
    )


def _is_rate_limit_error(exc: Exception) -> bool:
    status = getattr(exc, "status", None)
    body = getattr(exc, "body", b"") or b""
    body_str = body.decode("utf-8", errors="replace").lower() if isinstance(body, bytes) else str(body).lower()
    return status == 429 or "quota" in body_str or "throttl" in body_str or "rate" in body_str


def _call_raw(
    granularity: str,
    interval: str,
    sku: str | None = None,
    asin: str | None = None,
) -> list[dict]:
    """
    Make a raw (non-deserialized) call to get_order_metrics and return the
    payload as a list of plain dicts.
    """
    client = make_api_client("sales-api")
    from swagger_client.api.sales_api import SalesApi  # type: ignore

    api = SalesApi(client)
    kwargs: dict = {}
    if sku:
        kwargs["sku"] = sku
    elif asin:
        kwargs["asin"] = asin

    logger.debug(
        "Sales API: granularity=%s interval=%s sku=%s asin=%s",
        granularity, interval, sku, asin,
    )

    last_exc: Exception | None = None
    for attempt in range(SALES_API_MAX_RETRIES):
        _SALES_LIMITER.wait()
        try:
            raw = api.get_order_metrics(
                marketplace_ids=[MARKETPLACE_ID],
                interval=interval,
                granularity=granularity,
                granularity_time_zone=_GRANULARITY_TZ,
                buyer_type="B2C",
                _preload_content=False,
                **kwargs,
            )
            data: dict = json.loads(raw.data)
            return data.get("payload") or []
        except Exception as exc:
            from swagger_client.rest import ApiException  # type: ignore

            if isinstance(exc, ApiException) and _is_rate_limit_error(exc):
                last_exc = exc
                if attempt < SALES_API_MAX_RETRIES - 1:
                    delay = min(60.0, 3.0 * (2 ** attempt))
                    logger.warning(
                        "Sales API rate limited for sku=%s asin=%s; retry in %.1fs (%d/%d)",
                        sku, asin, delay, attempt + 1, SALES_API_MAX_RETRIES,
                    )
                    time.sleep(delay)
                    continue
            raise

    if last_exc:
        raise last_exc
    return []


def _total_units(rows: list[dict]) -> int:
    return sum(int(r.get("unitCount") or 0) for r in rows)


def get_sales_metrics(sku: str, days: int = 30, asin: str | None = None) -> list[dict]:
    """
    Return a list of raw metric dicts for the past ``days`` days
    using ``granularity="Total"`` (one aggregate row).

    Falls back to ASIN-level data when the SKU returns zero units.
    """
    interval = _make_interval(days)
    rows = _call_raw("Total", interval, sku=sku)
    if asin and _total_units(rows) == 0:
        asin_rows = _call_raw("Total", interval, asin=asin)
        if _total_units(asin_rows) > 0:
            logger.debug("SKU %s has 0 units; using ASIN %s data (%d days)", sku, asin, days)
            return asin_rows
    return rows


def get_daily_sales(sku: str, days: int = 30, asin: str | None = None) -> list[dict]:
    """
    Return a list of raw metric dicts for the past ``days`` days
    using ``granularity="Day"`` (one row per calendar day).

    Falls back to ASIN-level data when the SKU returns zero units.
    """
    interval = _make_interval(days)
    rows = _call_raw("Day", interval, sku=sku)
    if asin and _total_units(rows) == 0:
        asin_rows = _call_raw("Day", interval, asin=asin)
        if _total_units(asin_rows) > 0:
            return asin_rows
    return rows


def extract_sales_metrics(rows: list[dict]) -> dict:
    """
    Aggregate a list of raw metric dicts into summary totals.

    Returns keys: ``unit_count``, ``order_count``,
    ``revenue_amount``, ``revenue_currency``.
    """
    if not rows:
        return {"unit_count": 0, "order_count": 0, "revenue_amount": None, "revenue_currency": None}

    total_units  = 0
    total_orders = 0
    total_rev    = 0.0
    currency: str | None = None

    for r in rows:
        total_units  += int(r.get("unitCount")  or 0)
        total_orders += int(r.get("orderCount") or 0)
        ts = r.get("totalSales") or {}
        raw_amt = ts.get("amount")
        if raw_amt is not None:
            try:
                total_rev += float(raw_amt)
            except (TypeError, ValueError):
                pass
            if currency is None:
                currency = ts.get("currencyCode")

    return {
        "unit_count":      total_units,
        "order_count":     total_orders,
        "revenue_amount":  round(total_rev, 2) if total_rev else None,
        "revenue_currency": currency,
    }


def extract_daily_series(daily_rows: list[dict]) -> list[dict]:
    """
    Convert daily raw metric dicts into a sorted ``[{date, units, revenue, orders}]`` list.

    ``date`` is an ISO-8601 date string (YYYY-MM-DD) extracted from the
    ``interval`` field (e.g. ``"2024-01-01T00:00:00Z--2024-01-02T00:00:00Z"``).
    """
    series = []
    for r in daily_rows:
        interval_str = r.get("interval") or ""
        date_part = interval_str.split("--")[0][:10] if interval_str else ""
        ts = r.get("totalSales") or {}
        raw_amt = ts.get("amount")
        try:
            rev = float(raw_amt) if raw_amt is not None else 0.0
        except (TypeError, ValueError):
            rev = 0.0
        series.append({
            "date":    date_part,
            "units":   int(r.get("unitCount")  or 0),
            "revenue": rev,
            "orders":  int(r.get("orderCount") or 0),
        })
    series.sort(key=lambda x: x["date"])
    return series
