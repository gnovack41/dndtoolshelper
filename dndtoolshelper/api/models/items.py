from django.db import models

from dndtoolshelper.api.models.base_model import BaseModel
from dndtoolshelper.utils.models import unique_together_constraint


class Item(BaseModel):
    class Rarity(models.TextChoices):
        COMMON = 'common', 'Common'
        UNCOMMON = 'uncommon', 'Uncommon'
        RARE = 'rare', 'Rare'
        VERY_RARE = 'very_rare', 'Very Rare'
        LEGENDARY = 'legendary', 'Legendary'
        ARTIFACT = 'artifact', 'Artifact'

    name = models.CharField()
    source = models.CharField()
    rarity = models.CharField(choices=Rarity.choices, null=True)

    class Meta(BaseModel.Meta):
        constraints = [unique_together_constraint('name', 'source')]
