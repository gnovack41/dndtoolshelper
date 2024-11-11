from dndtoolshelper.services.dndbeyond.resources import DNDBeyondItems
from dndtoolshelper.services.dndbeyond.util import DNDBeyondAPIClient


class DNDBeyondAPI:
    def __init__(self, token: str | None = None):
        self._api = api = DNDBeyondAPIClient(token)

        self.items = DNDBeyondItems(api)


dndbeyond_api = DNDBeyondAPI()
