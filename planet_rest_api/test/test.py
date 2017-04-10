from unittest import TestCase
from planet_rest_api import planet_rest_api


class TestRunFunction(TestCase):
    def test_run_exists(self):
        self.assertTrue(bool(planet_rest_api.run))
