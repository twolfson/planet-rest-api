# Load in our dependencies
# Taken from https://gist.github.com/twolfson/13f5f5784f67fd49b245
import json
from unittest import TestCase

import planet_rest_api
Asset = planet_rest_api.Asset


# Define our fixtures
# DEV: In a database setup, these would be separate files
#   but this is a trivial project
FIXTURES = {
    'satellite1': {
        'name': 'Satellite 1',
        'type': Asset.TYPE_SATELLITE,
        'klass': Asset.CLASS_SATELLITE_DOVE,
    }
}


# Define our base test case
class ApiTestCase(TestCase):
    # API setup/teardown
    @classmethod
    def setUpClass(cls):
        """On inherited classes, run our `setUp` method"""
        # Inspired via http://stackoverflow.com/questions/1323455/python-unit-test-with-base-and-sub-class/17696807#17696807 # noqa
        if cls is not ApiTestCase and cls.setUp is not ApiTestCase.setUp:
            orig_setUp = cls.setUp

            def setUpOverride(self, *args, **kwargs):
                ApiTestCase.setUp(self)
                return orig_setUp(self, *args, **kwargs)
            cls.setUp = setUpOverride

    def setUp(self):
        # Create our test client
        # http://flask.pocoo.org/docs/0.12/testing/
        planet_rest_api.app.config['TESTING'] = True
        self.app = planet_rest_api.app.test_client()

        # Wipe out our fixtures
        planet_rest_api.assets = {}

    def tearDown(self):
        # Reset our config
        del planet_rest_api.app.config['TESTING']

    # HTTP helper methods
    def _load_response(self, method, pathname, parse_json=True, *args, **kwargs):
        # Make our request
        method_fn = getattr(self.app, method)
        rv = method_fn(pathname, *args, **kwargs)

        # Parse our JSON
        if parse_json:
            rv.json = json.loads(rv.data)

        # Return our result
        return rv

    def get_response(self, pathname, *args, **kwargs):
        return self._load_response('get', pathname, *args, **kwargs)

    # Define fixture helpers
    def install_fixtures(self, keys):
        # Resolve our fixtures
        # DEV: This will throw key errors when we can't find a fixture
        fixtures = [FIXTURES[key] for key in keys]

        # Install our fixtures
        for fixture in fixtures:
            asset = Asset(**fixture)
            asset.save()
