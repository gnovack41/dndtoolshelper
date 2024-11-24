from rest_framework import serializers

from dndtoolshelper.api.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        read_only_fields = ['id']
        fields = read_only_fields + [
            'name',
            'avatar_url',
            'dnd_class',
            'race',
            'level',
            'strength_score',
            'dexterity_score',
            'constitution_score',
            'intelligence_score',
            'wisdom_score',
            'charisma_score',
        ]


class CharacterImportSerializer(serializers.Serializer):
    character_dndbeyond_id = serializers.CharField()
