from typing import Any

import requests
from django.conf import settings
from requests import Response
from requests.auth import HTTPBasicAuth

from dndtoolshelper.services.utils import HTTP_METHODS, JSON
from dndtoolshelper.utils.urls import url_join


# 5eTools Client
class DNDBeyondAPIClient:
    def __init__(self, token: str | None = None):
        self.token = token

    def request(
        self,
        method: HTTP_METHODS,
        path: str,
        headers: dict[str, str] | None = None,
    ) -> JSON:
        response: Response = requests.request(
            method=method,
            url=url_join(settings.DND_BEYOND_URL, path),
            headers=(
                {'User-Agent': 'Mozilla/5.0'}
                | ({'Authorization': f'Bearer {self.token}'} if self.token else {})
                | (headers or {})
            ),
        )

        response.raise_for_status()

        return response.json()


class DNDBeyondAPIResource:
    """Base class for all DND API wrapper resources to inherit from"""

    def __init__(self, api: DNDBeyondAPIClient):
        self._api = api
