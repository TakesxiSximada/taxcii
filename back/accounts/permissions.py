# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class AuthTokenPermission(BasePermission):
    def has_permission(self, request, view):
        token = request.auth
        if not token
