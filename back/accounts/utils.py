# -*- coding: utf-8 -*-
import uuid
import hashlib
import datetime


class AuthKeyFactory(object):
    def __init__(self, hash_factory=None, uuid_factory=None):
        self._uuid_factory = uuid.uuid4 if uuid_factory is None else uuid_factory
        self._hash_factory = hashlib.sha256 if hash_factory is None else hash_factory

    def __call__(self):
        _uuid = self._uuid_factory().encode()
        _hash = self._hash_factory(_uuid.encode())
        return _hash.hexdigest()


class ExpireDatetimeFactory(object):
    def __init__(self, **kwds):
        self._kwds = kwds

    def __call__(self):
        return datetime.datetime.now() + datetime.timedelta(**self._kwds)
