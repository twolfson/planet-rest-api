# Load in our dependencies
from planet_rest_api.test import ApiTestCase


# Define our tests
class AssetsGetTestCase(ApiTestCase):
    def test_empty(self):
        # A request to an empty `GET /assets` endpoint
        rv = self.get_response('/assets')

        # receives no assets
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.json, [{'name': 'Dove'}])