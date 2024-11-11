from dndtoolshelper.services.dndbeyond.util import DNDBeyondAPIResource


class DNDBeyondCharacters(DNDBeyondAPIResource):
    def get(self, character_id: str):
        return self._api.request('GET', f'character/{character_id}')
