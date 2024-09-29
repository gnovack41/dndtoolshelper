from typing import Any

import requests
from django.conf import settings
from requests import Response
from requests.auth import HTTPBasicAuth

from dndtoolshelper.services.utils import HTTP_METHODS, JSON
from dndtoolshelper.utils.urls import url_join


# 5eTools Client
class DNDToolsAPIClient:
    def request(
        self,
        method: HTTP_METHODS,
        path: str,
    ) -> JSON:
        response: Response = requests.request(
            method=method,
            url=url_join(settings.DND_API_URL, path),
            headers={
                'User-Agent': 'Mozilla/5.0',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': '*/*',
                'Connection': 'keep-alive',
            }
        )

        response.raise_for_status()

        return response.json()


class DNDToolsAPIResource:
    """Base class for all DND API wrapper resources to inherit from"""

    def __init__(self, api: DNDToolsAPIClient):
        self._api = api
