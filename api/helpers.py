import uuid
from django.db import models


class StatusChoice(models.TextChoices):
    DRAFT = 'df', 'Draft'
    PUBLISH = 'pb', 'Publish'
