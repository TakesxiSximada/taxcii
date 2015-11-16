# -*- coding: utf-8 -*-
import uuid
from django.db.models import (
    CharField,
    ForeignKey,
    DateTimeField,
    )

from django.contrib.auth.models import AbstractUser
from .utils import (
    AuthKeyFactory,
    ExpireDatetimeFactory,
    )


class User(AbstractUser):
    code = CharField(max_length=0xFF, unique=True, db_index=True)


class AuthToken(Model):
    user = Foreignkey(User)
    key = CharField(max_length=0xFF, default=AuthKeyFactory(), unique=True, db_index=True)
    expired_at = DateTimeField(default=ExpireDatetimeFactory(days=3), blank=True, null=True)  # None is no expire
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
