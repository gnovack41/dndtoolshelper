from django.db import models

from dndtoolshelper.api.models.base_model import BaseModel


class RefreshToken(BaseModel):
    refresh_token = models.CharField()
    expires_at = models.DateField()
