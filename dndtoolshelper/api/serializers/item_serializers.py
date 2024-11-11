import re

from rest_framework import serializers

from dndtoolshelper.api.models import Item


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='dndbeyond_id', required=False, default=None)
    description = serializers.CharField(required=False, default=None)

    class Meta:
        model = Item
        fields = ['id', 'name', 'source', 'rarity', 'description', 'dndbeyond_id']

    def to_internal_value(self, data):
        if item := Item.objects.filter(name=data.get('name'), source=data.get('source'), dndbeyond_id__isnull=True).first():
            self.instance = item

        if not self.instance and 'id' in data and (item := Item.objects.filter(dndbeyond_id=data['id']).first()):
            self.instance = item

        if (data.get('rarity') or '').replace(' ', '').casefold() not in [rarity.casefold() for rarity in Item.Rarity.values]:
            data['rarity'] = None
        elif data['rarity'] is not None:
            data['rarity'] = data['rarity'].lower().replace(' ', '_')

        if data['description'] is not None:
            data['description'] = re.sub(r'<[^<]*>', '', data['description'])

        return super().to_internal_value(data)
