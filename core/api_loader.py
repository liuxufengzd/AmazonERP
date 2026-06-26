"""
Swagger client factory for Amazon SP-API.

Every SP-API client package under clients/ is named ``swagger_client``,
so they cannot coexist in sys.modules.  This module manages sys.path and
the module cache so each package can be activated on demand before import.

All SP-API calls in this project are synchronous and fully resolve before
the next package is activated, so there is no cross-package import conflict.
"""

from __future__ import annotations

import sys

from core.config import CLIENT_BASE_PATH, REGION_HOST
from core.auth import get_access_token


def activate_package(package_name: str) -> None:
    """
    Flush any cached ``swagger_client`` modules and insert the requested
    package at the front of ``sys.path`` so subsequent imports resolve to it.
    """
    pkg_path = str(CLIENT_BASE_PATH / package_name)

    for key in list(sys.modules.keys()):
        if key == "swagger_client" or key.startswith("swagger_client."):
            del sys.modules[key]

    sys.path = [p for p in sys.path if p != pkg_path]
    sys.path.insert(0, pkg_path)


def make_api_client(package_name: str):
    """
    Return a configured swagger ``ApiClient`` for the given client package
    with a fresh LWA access token injected into the default headers.
    """
    activate_package(package_name)

    from swagger_client.api_client import ApiClient  # type: ignore
    from swagger_client.configuration import Configuration  # type: ignore

    cfg = Configuration()
    cfg.host = f"https://{REGION_HOST}"

    client = ApiClient(configuration=cfg)
    client.set_default_header("x-amz-access-token", get_access_token())
    return client
