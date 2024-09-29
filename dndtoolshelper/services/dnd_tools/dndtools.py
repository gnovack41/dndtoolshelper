from dndtoolshelper.services.dnd_tools.resources import DNDToolsItems
from dndtoolshelper.services.dnd_tools.util import DNDToolsAPIClient


class DNDToolsAPI:
    def __init__(self):
        self._api = api = DNDToolsAPIClient()

        self.items = DNDToolsItems(api)


dndtools_api = DNDToolsAPI()
