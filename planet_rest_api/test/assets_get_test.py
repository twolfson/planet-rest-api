# Load in our dependencies
from planet_rest_api.test import ApiTestCase


# Define our tests
class AssetsGetTestCase(ApiTestCase):
    def test_empty(self):
        # A request to an empty `GET /assets` endpoint
        rv = self.get_response('/assets')

        # receives no assets
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.json, [])

    def test_non_empty(self):
        # A request to a non-empty `GET /assets` endpoint
        self.install_fixtures(['satellite1'])
        rv = self.get_response('/assets')

        # receives expected assets
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.json, [{
            'name': 'Satellite 1',
            'type': 'satellite',
            'class': 'dove'
        }])
