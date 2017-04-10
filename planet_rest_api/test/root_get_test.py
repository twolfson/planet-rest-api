# Load in our dependencies
from planet_rest_api.test import ApiTestCase


# Define our tests
class RootGetTestCase(ApiTestCase):
    def test_success(self):
        # A request to our root endpoint
        rv = self.get_response('/')

        # receives no errors
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.json, {'message': 'OK'})
