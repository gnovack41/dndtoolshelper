from django.db import models

from dndtoolshelper.api.models.base_model import BaseModel


class Source(BaseModel):
    id = models.IntegerField(primary_key=True)

    name = models.CharField()
    label = models.CharField()
