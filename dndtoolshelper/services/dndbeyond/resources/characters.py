from dndtoolshelper.services.dndbeyond.util import DNDBeyondAPIResource


class DNDBeyondCharacters(DNDBeyondAPIResource):
    def get(self, character_id: str):
        return self._api.request('GET', f'character/{character_id}')

    def add_item(self, character_id: str, item_id: str, quantity: int):
        return self._api.request(
            'POST',
            f'inventory/item',
            json={
                'characterId': character_id,
                'equipment': [{
                    'entityId': item_id,
                    'quantity': quantity,
                    'entityTypeId': '112130694',
                }],
            },
        )
