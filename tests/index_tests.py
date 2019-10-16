#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#python imports
import unittest
import xmlrpclib
import json

#app imports
from base import HubTests


class TestIndex(HubTests):
    """Tests for the index."""

    def setUp(self):
        super(TestIndex, self).setUp()

    def tearDown(self):
        super(TestIndex, self).tearDown()

    def test_foo(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
