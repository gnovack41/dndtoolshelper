from typing import TypedDict

from dndtoolshelper.services.dndbeyond.util import DNDBeyondAPIResource


class UploadedItem(TypedDict):
    item_id: str
    quantity: int


class DNDBeyondCharacters(DNDBeyondAPIResource):
    def get(self, character_id: str):
        return self._api.request('GET', f'character/{character_id}')

    def add_item(self, character_id: str, items: list[UploadedItem]):
        return self._api.request(
            'POST',
            f'inventory/item',
            json={
                'characterId': character_id,
                'equipment': [{
                    'entityId': item['item_id'],
                    'quantity': item['quantity'],
                    'entityTypeId': '112130694',
                } for item in items],
            },
        )
