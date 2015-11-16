# -*- coding: utf-8 -*-
from django.utils import timezone
from rest_framework.authentication import BaseAuthentication
from .models import AuthToken


class BaseTokenAuthentication(BaseAuthentication):
    token_header = None
    token_class = None

    def authenticate(self, request):
        now_ = timezone.now()
        key = request.META.get(self.token_header, None)
        if key is None:
            return None
        token = self.token_class \
                     .objects \
                     .filter(key=key, expired_at__lt=now_) \
                     .first()
        if len(token):
            return (token.user, token)
        else:
            return None


class AuthTokenAuthentication(BaseTokenAuthentication):
    token_header = 'HTTP_X_AUTH_TOKEN'
    token_class = AuthToken
