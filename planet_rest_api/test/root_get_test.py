# Load in our dependencies
import json
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

    def _load_response(self, method, parse_json=True, *args, **kwargs):
        # Make our request
        method_fn = getattr(self.app, method)
        rv = method_fn(*args, **kwargs)

        # Parse our JSON
        if parse_json:
            rv.json = json.loads(rv.data)

        # Return our result
        return rv

    def get_response(self, *args, **kwargs):
        return self._load_response('get', *args, **kwargs)

    def test_success(self):
        # A request to our root endpoint
        rv = self.get_response('/')

        # receives no errors
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.json, {'message': 'OK'})
