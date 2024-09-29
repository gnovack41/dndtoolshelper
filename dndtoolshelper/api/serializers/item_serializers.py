from rest_framework import serializers

from dndtoolshelper.api.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'source', 'rarity']

    def to_internal_value(self, data):
        if item := Item.objects.filter(name=data.get('name'), source=data.get('source')).first():
            self.instance = item

        if data.get('rarity', '').replace(' ', '') not in Item.Rarity.values:
            data['rarity'] = None

        return super().to_internal_value(data)
