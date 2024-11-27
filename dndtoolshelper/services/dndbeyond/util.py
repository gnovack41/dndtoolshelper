import logging
from typing import Any

import requests
from django.conf import settings
from requests import HTTPError, Response

from dndtoolshelper.dndbeyond.models import RefreshToken
from dndtoolshelper.services.utils import HTTP_METHODS, JSON
from dndtoolshelper.utils.urls import url_join

logger = logging.getLogger(__name__)


class DNDBeyondAPIClient:
    def __init__(self):
        self.token: str | None = None

    def request(
        self,
        method: HTTP_METHODS,
        path: str,
        headers: dict[str, str] | None = None,
        **kwargs,
    ) -> JSON:
        def make_request() -> dict[str, Any]:
            response: Response = requests.request(
                method=method,
                url=url_join(settings.DND_BEYOND_URL, path),
                headers=(
                    {'User-Agent': 'Mozilla/5.0'}
                    | ({'Authorization': f'Bearer {self.token}'} if self.token else {})
                    | (headers or {})
                ),
                **kwargs,
            )

            response.raise_for_status()

            return response.json()

        try:
            response = make_request()
        except HTTPError as e:
            if e.response.status_code in [401, 403]:
                self._update_access_token()
                response = make_request()
            else:
                raise

        return response

    def _update_access_token(self):
        logger.info('Updating access token')
        refresh_token = RefreshToken.objects.values_list('refresh_token', flat=True).get()

        response: Response = requests.request(
            method='POST',
            url='https://auth-service.dndbeyond.com/v1/cobalt-token',
            headers={
                'Cookie': f'CobaltSession={refresh_token}',
            }
        )

        response.raise_for_status()
        response_json = response.json()

        self.token = response_json['token']


class DNDBeyondAPIResource:
    """Base class for all DND API wrapper resources to inherit from"""

    def __init__(self, api: DNDBeyondAPIClient):
        self._api = api
