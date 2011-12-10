#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
redis_sesson_backend.debug
~~~~~~~~~~~~~~~~~~~~~~~~~~

Debugging tests for redis_session_backend

:copyright: (c) 2011 by Alexandr Lispython (alex@obout.ru).
:license: BSD, see LICENSE for more details.
"""

import logging
from .tests import *


logger = logging.getLogger("redis_session_backend")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()

formatter = logging.Formatter("%(levelname)s %(asctime)s %(module)s [%(lineno)d] %(process)d %(thread)d | %(message)s ")

handler.setFormatter(formatter)

logger.addHandler(handler)
