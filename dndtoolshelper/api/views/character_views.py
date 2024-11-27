from requests import HTTPError
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from dndtoolshelper.api.logic.character_logic import get_character_from_dndbeyond
from dndtoolshelper.api.models import Character
from dndtoolshelper.api.serializers import CharacterSerializer
from dndtoolshelper.api.serializers.character_serializers import CharacterImportSerializer, CharacterSyncItemSerializer
from dndtoolshelper.services.dndbeyond import dndbeyond_api


class CharacterViewSet(ModelViewSet):
    queryset = Character.objects.all()

    serializer_class = CharacterSerializer

    @action(detail=False, methods=['POST'])
    def dndbeyond_import(self, request):
        serializer = CharacterImportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dndbeyond_id: str = serializer.validated_data['character_dndbeyond_id']
        from requests import HTTPError
        try:
            character = get_character_from_dndbeyond(dndbeyond_id)
        except HTTPError as e:
            if e.response.status_code in [400, 404]:
                raise serializers.ValidationError({'missing_character': ['Character not found']})

            raise

        update = False
        if existing_character := Character.objects.filter(dndbeyond_id=dndbeyond_id).first():
            character.id = existing_character.id
            update = True

        character.save(
            update_fields=[
                'updated_at',
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
            ],
            force_update=update,
        )

        return Response(CharacterSerializer(character).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def sync_items(self, request):
        serializer = CharacterSyncItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            dndbeyond_api.characters.add_item(
                character_id=serializer.validated_data['character_dndbeyond_id'],
                items=[{
                    'item_id': item['dndbeyond_id'],
                    'quantity': item['quantity'],
                } for item in serializer.validated_data['items']],
            )
        except HTTPError as e:
            if e.response.status_code in [400, 404]:
                raise serializers.ValidationError({'invalid_entities': ['Character or item not found']})

            raise

        return Response(status=status.HTTP_204_NO_CONTENT)
