#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
redis_session_backemd.tests
~~~~~~~~~~~~~~~~~~~~~~~~~~

Unittests for redis_session_backend

:copyright: (c) 2011 by Alexandr Lispython (alex@obout.ru).
:license: BSD, see LICENSE for more details.
"""
import unittest

class RedisSessionTestCase(unittest.TestCase):

    def test_create(self):
        self.assertTrue(True)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RedisSessionTestCase))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest="suite")
