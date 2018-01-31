# -*- coding: utf-8 -*-
"""Unit tests for the Master Controller.

- http://flask.pocoo.org/docs/0.12/testing/
"""
import unittest
import json

from master_controller.app import APP as app
from master_controller.app import STATES as states


class MasterControllerTests(unittest.TestCase):
    """Tests of the Master Controller"""

    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        """Executed after each test."""
        pass

    def test_get_state_successful(self):
        """Test of successfully returning the SDP state."""
        response = self.app.get('/state')
        self.assertEqual(response.mimetype,
                         'application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertTrue(data['state'] in states)
