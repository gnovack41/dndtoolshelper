from dndtoolshelper.services.dndbeyond.util import DNDBeyondAPIResource


class DNDBeyondItems(DNDBeyondAPIResource):
    def list(self):
        return self._api.request('GET', 'game-data/items')
