from django.db import models
import uuid
from datetime import datetime

# Create your models here.

class IdStamp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    timestamp = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.id

