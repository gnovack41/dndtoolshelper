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

    class Origin(models.TextChoices):
        FiveETools = '5ETOOLS', '5eTools'
        DNDBEYOND = 'DNDBEYOND', 'DndBeyond'

    name = models.CharField()
    source = models.CharField(null=True, blank=True, default=None)
    rarity = models.CharField(choices=Rarity.choices, null=True)
    description = models.TextField(null=True, blank=True, default=None)

    dndbeyond_id = models.IntegerField(null=True, default=None)
