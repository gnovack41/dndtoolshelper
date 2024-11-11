import re

from rest_framework import serializers

from dndtoolshelper.api.models import Item


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='dndbeyond_id', required=False, default=None)
    description = serializers.CharField(required=False, default=None)
    avatarUrl = serializers.URLField(source='image_url', write_only=True, allow_null=True, default=None)

    source = serializers.CharField(source='source.name', read_only=True)

    class Meta:
        model = Item
        read_only_fields = ['source', 'image_url']
        fields = read_only_fields + ['id', 'name', 'rarity', 'description', 'dndbeyond_id', 'avatarUrl']

    def to_internal_value(self, data):
        if not self.instance and (item := Item.objects.filter(dndbeyond_id=data['id']).first()):
            self.instance = item

        if data['rarity'] is not None:
            data['rarity'] = data['rarity'].lower().replace(' ', '_')

        if data['rarity'] not in Item.Rarity.values:
            data['rarity'] = None

        if data['description'] is not None:
            data['description'] = re.sub(r'<[^<]*>', '', data['description'])

        return super().to_internal_value(data)

    def validate(self, data):
        return data
