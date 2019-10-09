import uuid
from django.db import models

# Create your models here.

class BasicGeneric(models.Model):
    alias = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_ip = models.GenericIPAddressField(null=True, blank=True, editable=False,)

