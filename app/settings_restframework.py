# -*- coding: utf-8 -*-
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'account.authentications.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGE_SIZE': 1000,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
}
