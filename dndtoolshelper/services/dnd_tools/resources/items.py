from dndtoolshelper.services.dnd_tools.util import DNDToolsAPIResource


class DNDToolsItems(DNDToolsAPIResource):
    def list(self):
        return self._api.request('GET', 'items.json')
