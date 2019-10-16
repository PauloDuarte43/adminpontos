#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#python imports
import unittest

from tasks import app


class TasksTests(unittest.TestCase):
    """Base testing for all tests."""

    # ------------------------------------------------------------
    #  Test set up and tear down
    # ------------------------------------------------------------
    def setUp(self):
        self.app = app.test_client()
        return

    def tearDown(self):
        return

    # ------------------------------------------------------------
    #  Common data
    # ------------------------------------------------------------

