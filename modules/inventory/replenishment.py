"""
Replenishment computation — pure business logic, no I/O.

Computes days-of-supply and a simple reorder recommendation from inventory
quantities and recent sales data.  Uses 30-day sales as the primary signal;
falls back to 90-day data (scaled to 30 days) when no 30-day sales exist.
"""

from __future__ import annotations

from core.config import RESTOCK_TARGET_DAYS


def compute_replenishment(
    fulfillable_qty: int,
    inbound_qty: int,
    unit_count_30d: int,
    unit_count_90d: int = 0,
    target_days: int = RESTOCK_TARGET_DAYS,
) -> dict:
    """
    Return replenishment metrics derived from current inventory and sales.

    ``days_of_supply``       = fulfillable_qty / avg_daily_sales
    ``suggested_order_qty``  = max(0, target_days * avg_daily − fulfillable − inbound)

    Both values are ``None`` when there are no recent sales.
    """
    if unit_count_30d > 0:
        avg_daily = unit_count_30d / 30.0
        source = "30d"
    elif unit_count_90d > 0:
        avg_daily = unit_count_90d / 90.0
        source = "90d"
    else:
        avg_daily = 0.0
        source = "none"

    days_of_supply: float | None
    days_of_supply_total: float | None
    suggested_order_qty: int | None

    if avg_daily > 0:
        days_of_supply = round(fulfillable_qty / avg_daily, 1)
        total_available = fulfillable_qty + inbound_qty
        days_of_supply_total = round(total_available / avg_daily, 1)
        needed = target_days * avg_daily
        suggested_order_qty = max(0, round(needed - total_available))
    else:
        days_of_supply = None
        days_of_supply_total = None
        suggested_order_qty = None

    status = _classify_status(
        days_of_supply=days_of_supply,
        days_of_supply_total=days_of_supply_total if avg_daily > 0 else None,
        inbound_qty=inbound_qty,
        suggested_order_qty=suggested_order_qty,
        avg_daily=avg_daily,
        target_days=target_days,
    )

    return {
        "avg_daily_sales": round(avg_daily, 2),
        "days_of_supply": days_of_supply,
        "days_of_supply_total": days_of_supply_total if avg_daily > 0 else None,
        "suggested_order_qty": suggested_order_qty,
        "target_days": target_days,
        "sales_source": source,
        "status": status,
        "note": "Computed from inventory + sales data",
    }


def _classify_status(
    *,
    days_of_supply: float | None,
    days_of_supply_total: float | None,
    inbound_qty: int,
    suggested_order_qty: int | None,
    avg_daily: float,
    target_days: int,
) -> str:
    if avg_daily <= 0 or days_of_supply is None:
        return "no_sales"
    if suggested_order_qty and suggested_order_qty > 0:
        return "needs_restock"
    if (
        days_of_supply < target_days
        and inbound_qty > 0
        and days_of_supply_total is not None
        and days_of_supply_total >= target_days
    ):
        return "covered_by_inbound"
    return "ok"
