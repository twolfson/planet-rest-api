# Load in our dependencies
from unittest import TestCase
import planet_rest_api


# Define our tests
class RootGetTestCase(TestCase):
    def setUp(self):
        # http://flask.pocoo.org/docs/0.12/testing/
        planet_rest_api.app.config['TESTING'] = True
        self.app = planet_rest_api.app.test_client()

    def tearDown(self):
        del planet_rest_api.app.config['TESTING']

    def test_success(self):
        # A request to our root endpoint
        rv = self.app.get('/')

        # receives no errors
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.data, 'OK')
