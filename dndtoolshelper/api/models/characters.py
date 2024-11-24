from django.db import models

from dndtoolshelper.api.models.base_model import BaseModel


class Character(BaseModel):
    dndbeyond_id = models.CharField(unique=True, null=True, blank=True)
    name = models.CharField()
    race = models.CharField()
    dnd_class = models.CharField()
    level = models.IntegerField()

    avatar_url = models.URLField(null=True, blank=True)

    strength_score = models.IntegerField()
    dexterity_score = models.IntegerField()
    constitution_score = models.IntegerField()
    intelligence_score = models.IntegerField()
    wisdom_score = models.IntegerField()
    charisma_score = models.IntegerField()
