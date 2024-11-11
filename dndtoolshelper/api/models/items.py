from django.db import models

from dndtoolshelper.api.models.base_model import BaseModel


class Item(BaseModel):
    class Rarity(models.TextChoices):
        COMMON = 'common', 'Common'
        UNCOMMON = 'uncommon', 'Uncommon'
        RARE = 'rare', 'Rare'
        VERY_RARE = 'very_rare', 'Very Rare'
        LEGENDARY = 'legendary', 'Legendary'
        ARTIFACT = 'artifact', 'Artifact'
        VARIES = 'varies', 'Varies'

    name = models.CharField()
    source = models.ForeignKey('Source', null=True, default=None, on_delete=models.SET_NULL, related_name='items')
    rarity = models.CharField(choices=Rarity.choices, null=True)
    description = models.TextField(null=True, blank=True, default=None)
    image_url = models.URLField(null=True, blank=True, default=None)

    dndbeyond_id = models.IntegerField(null=True, default=None, unique=True)
