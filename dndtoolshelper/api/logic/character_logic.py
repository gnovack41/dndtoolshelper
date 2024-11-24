from typing import Any, TypedDict

from dndtoolshelper.api.models import Character
from dndtoolshelper.services.dndbeyond import dndbeyond_api


class ClassData(TypedDict):
    name: str
    level: int


def get_character_from_dndbeyond(character_id: str):
    character_data = dndbeyond_api.characters.get(character_id)['data']

    class_data = parse_character_classes(character_data['classes'])

    name = character_data['name']
    race_name = character_data['race']['fullName']
    class_name = '/'.join([c['name'] for c in class_data])
    level = sum(c['level'] for c in class_data)
    avatar_url = character_data['decorations']['avatarUrl']

    attributes_data = character_data['stats']
    strength_score = attributes_data[0]['value']
    dexterity_score = attributes_data[1]['value']
    constitution_score = attributes_data[2]['value']
    intelligence_score = attributes_data[3]['value']
    wisdom_score = attributes_data[4]['value']
    charisma_score = attributes_data[5]['value']

    return Character(
        dndbeyond_id=character_id,
        name=name,
        race=race_name,
        dnd_class=class_name,
        level=level,
        avatar_url=avatar_url,
        strength_score=strength_score,
        dexterity_score=dexterity_score,
        constitution_score=constitution_score,
        intelligence_score=intelligence_score,
        wisdom_score=wisdom_score,
        charisma_score=charisma_score,
    )


def parse_character_classes(classes_data: list[dict[str, Any]]) -> list[ClassData]:
    return [{'name': class_data['definition']['name'], 'level': class_data['level']} for class_data in classes_data]
