#!/usr/bin/env python
# -*- coding:  utf-8 -*-

"""
redis_session_backend
~~~~~~~~~~~~~~~~~~~~~

Sessions backend for django framework

:copyright: (c) 2011 by Alexandr Sokolovskiy (alex@obout.ru).
:license: BSD, see LICENSE for more details.
"""


from cPickle import loads, dumps

from django.contrib.sessions.backends.base import SessionBase, CreateError
from django.conf import settings

import redis

class SessionStore(SessionBase):
    """
    A redis-based session store.
     """
    def __init__(self, session_key=None):
        self.redis = redis.Redis(
            host=getattr(settings, "REDIS_HOST", 'localhost'),
            port=getattr(settings, "REDIS_PORT", 6379),
            db=getattr(settings, "REDIS_DB"))
        self._session_key = session_key

        ## self._session_key = self.session_key = session_key
        self.modified = None
        super(SessionStore, self).__init__(session_key)


    def load(self):
        session_data = self.redis.get(self._session_key)
        if session_data is not None:
            return loads(session_data)
        self.create()
        return {}

    def create(self):
        while True:
            self._session_key = self._get_new_session_key()
            try:
                self.save(must_create=True)
            except CreateError:
                # Would be raised if the key wasn't unique
                continue
            self.modified = True
            return

    def save(self, must_create=False):
        if must_create:
            # preserve=True -> SETNX
            result = self.redis.set(
                self._session_key, dumps(self._get_session(no_load=must_create)))
            if result == 0: # 0 == not created, 1 == created.
                raise CreateError
        else:
            self.redis.set(self._session_key, dumps(self._get_session(no_load=must_create)),)

    def exists(self, session_key):
        if self.redis.exists(session_key):
            return True
        return False

    def delete(self, session_key=None):
        if session_key is None:
            if self._session_key is None:
                return
            session_key = self._session_key
        self.redis.delete(session_key)

