from celery.app import shared_task

from dndtoolshelper.api.serializers import ItemSerializer
from dndtoolshelper.services.dnd_tools import dndtools_api


@shared_task
def sync_dndtools_items():
    items = dndtools_api.items.list()['item']
    valid_items = [item for item in items if {'name', 'source', 'rarity'} <= set(item.keys())]

    for item in valid_items:
        serializer = ItemSerializer(data=item)
        serializer.is_valid(raise_exception=True)
        serializer.save()
