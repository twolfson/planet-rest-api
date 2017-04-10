from unittest import TestCase
import planet_rest_api


class TestRunFunction(TestCase):
    def test_run_exists(self):
        self.assertEqual(planet_rest_api.foo, 'bar')
