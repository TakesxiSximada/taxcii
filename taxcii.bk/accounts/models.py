# -*- coding: utf-8 -*-
import uuid
from django.db.models import (
    UUIDField
    )

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    auth_key = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
