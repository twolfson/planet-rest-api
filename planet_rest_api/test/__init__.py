# Load in our dependencies
# Taken from https://gist.github.com/twolfson/13f5f5784f67fd49b245
import json
from unittest import TestCase

import planet_rest_api


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
        # http://flask.pocoo.org/docs/0.12/testing/
        planet_rest_api.app.config['TESTING'] = True
        self.app = planet_rest_api.app.test_client()

    def tearDown(self):
        del planet_rest_api.app.config['TESTING']

    # Helper methods
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
