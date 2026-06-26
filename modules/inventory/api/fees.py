"""
Product Fees API wrapper.

Fetches FBA fee estimates for an ASIN given a listing price.
Uses ``product-fees-api`` swagger client.
"""

from __future__ import annotations

import logging

from core.api_loader import make_api_client
from core.config import MARKETPLACE_ID

logger = logging.getLogger(__name__)


def get_fees_estimate(asin: str, price: float, currency: str = "JPY") -> dict:
    """
    Return estimated FBA fees for an ASIN at the given listing price.

    Returns a dict with keys:
      ``total_fees``           — total estimated fee amount
      ``currency``             — currency code
      ``fee_breakdown``        — list of {type, amount} individual fee components
      ``referral_fee``         — referral fee amount
      ``fulfillment_fee``      — FBA fulfillment fee amount
    """
    client = make_api_client("product-fees-api")
    from swagger_client.api.fees_api import FeesApi  # type: ignore
    from swagger_client.models.get_my_fees_estimate_request import (  # pyright: ignore[reportMissingImports]
        GetMyFeesEstimateRequest,
    )
    from swagger_client.models.fees_estimate_request import FeesEstimateRequest  # type: ignore
    from swagger_client.models.price_to_estimate_fees import PriceToEstimateFees  # type: ignore
    from swagger_client.models.money_type import MoneyType  # type: ignore

    listing_price = MoneyType(currency_code=currency, amount=price)
    price_to_estimate = PriceToEstimateFees(listing_price=listing_price)
    fees_request = FeesEstimateRequest(
        marketplace_id=MARKETPLACE_ID,
        is_amazon_fulfilled=True,
        price_to_estimate_fees=price_to_estimate,
        identifier=f"fees-{asin}",
    )
    body = GetMyFeesEstimateRequest(fees_estimate_request=fees_request)

    api = FeesApi(client)
    logger.debug("Fetching fees estimate for ASIN %s at %s %s", asin, price, currency)
    resp = api.get_my_fees_estimate_for_asin(body=body, asin=asin)

    payload = getattr(resp, "payload", None)
    result = getattr(payload, "fees_estimate_result", None) if payload else None
    estimate = getattr(result, "fees_estimate", None) if result else None

    if not estimate:
        return {}

    total_fees_obj = getattr(estimate, "total_fees_estimate", None)
    total_amount = getattr(total_fees_obj, "amount", None) if total_fees_obj else None
    fee_currency = (
        getattr(total_fees_obj, "currency_code", currency)
        if total_fees_obj
        else currency
    )

    # Parse individual fee components
    fee_detail_list = getattr(estimate, "fee_detail_list", []) or []
    breakdown: list[dict] = []
    referral_fee: float | None = None
    fulfillment_fee: float | None = None

    for fee in fee_detail_list:
        fee_type = getattr(fee, "fee_type", None)
        amount_obj = getattr(fee, "final_fee", None)
        amount = float(getattr(amount_obj, "amount", 0) or 0) if amount_obj else 0.0
        breakdown.append({"type": fee_type, "amount": amount})
        t = (fee_type or "").lower()
        if "referral" in t:
            referral_fee = amount
        elif "fulfillment" in t or "fba" in t or "pick" in t:
            fulfillment_fee = (fulfillment_fee or 0) + amount

    return {
        "total_fees": float(total_amount) if total_amount is not None else None,
        "currency": fee_currency,
        "fee_breakdown": breakdown,
        "referral_fee": referral_fee,
        "fulfillment_fee": fulfillment_fee,
    }
