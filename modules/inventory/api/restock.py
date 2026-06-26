"""
FBA Restock Report API wrapper.

Orchestrates the full report pipeline:
  create_report → poll until done → download document → parse TSV rows.

Report type: ``GET_RESTOCK_INVENTORY_RECOMMENDATIONS_REPORT``
Key columns:  sku, fnsku, asin, days-of-supply,
              recommended-replenishment-qty, reorder-date, alert
"""

from __future__ import annotations

import csv
import gzip
import io
import logging
import time

import requests

from core.api_loader import make_api_client
from core.config import MARKETPLACE_ID

logger = logging.getLogger(__name__)

_REPORT_TYPE = "GET_RESTOCK_INVENTORY_RECOMMENDATIONS_REPORT"
_POLL_INTERVAL_SECONDS = 15
_TERMINAL_STATUSES = {"DONE", "FATAL", "CANCELLED"}


def _request_report() -> str:
    """Submit the restock report request and return the report ID."""
    client = make_api_client("reports-api")
    from swagger_client.api.reports_api import ReportsApi  # type: ignore
    from swagger_client.models.create_report_specification import (  # pyright: ignore[reportMissingImports]
        CreateReportSpecification,
    )

    spec = CreateReportSpecification(
        report_type=_REPORT_TYPE,
        marketplace_ids=[MARKETPLACE_ID],
    )
    result = ReportsApi(client).create_report(body=spec)
    logger.debug("Restock report requested: %s", result.report_id)
    return result.report_id


def _poll_until_done(report_id: str, max_wait: int = 300) -> object:
    """Poll the report status until it reaches a terminal state."""
    deadline = time.time() + max_wait
    while time.time() < deadline:
        client = make_api_client("reports-api")
        from swagger_client.api.reports_api import ReportsApi  # type: ignore

        report = ReportsApi(client).get_report(report_id=report_id)
        status = report.processing_status
        logger.info("Restock report [%s] status: %s", report_id, status)
        if status in _TERMINAL_STATUSES:
            return report
        time.sleep(_POLL_INTERVAL_SECONDS)

    raise TimeoutError(f"Restock report did not finish within {max_wait}s")


def _download_document(report_document_id: str) -> str:
    """Download and decompress (if GZIP) a report document; return raw text."""
    client = make_api_client("reports-api")
    from swagger_client.api.reports_api import ReportsApi  # type: ignore

    doc = ReportsApi(client).get_report_document(report_document_id=report_document_id)
    resp = requests.get(doc.url, timeout=60)
    resp.raise_for_status()

    if getattr(doc, "compression_algorithm", None) == "GZIP":
        return gzip.decompress(resp.content).decode("utf-8")
    return resp.text


def _parse_tsv(content: str) -> list[dict]:
    """Parse a tab-separated report body into a list of row dicts."""
    return list(csv.DictReader(io.StringIO(content), delimiter="\t"))


def fetch_restock_report() -> list[dict]:
    """
    Run the full restock report pipeline and return parsed rows.

    Each row is a dict keyed by the report's column names.
    Returns an empty list if the report does not complete successfully.
    """
    report_id = _request_report()
    report = _poll_until_done(report_id)

    if report.processing_status != "DONE":
        logger.warning("Restock report ended with status: %s", report.processing_status)
        return []

    content = _download_document(report.report_document_id)
    rows = _parse_tsv(content)
    logger.debug("Restock report parsed: %d rows", len(rows))
    return rows
