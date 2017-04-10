# Load in our dependencies
from planet_rest_api.test import ApiTestCase


# Define our tests
class AssetsNameGetTestCase(ApiTestCase):
    def test_success(self):
        # A request to a non-empty `GET /assets` endpoint
        self.install_fixtures(['satellite1'])
        rv = self.get_response('/assets/satellite1')

        # receives expected assets
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.json, {
            'name': 'satellite1',
            'type': 'satellite',
            'class': 'dove'
        })

    def test_non_existent(self):
        # A request to an empty `GET /assets` endpoint
        rv = self.get_response('/assets/satellite1')

        # receives no assets
        self.assertEqual(rv.status_code, 404)
        self.assertEqual(rv.json, {'message': 'Asset not found'})
