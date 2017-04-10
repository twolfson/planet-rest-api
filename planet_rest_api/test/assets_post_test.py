# Load in our dependencies
import json

from mock import patch

from planet_rest_api.models.asset import Asset
from planet_rest_api.test import ApiTestCase


# Define our tests
class AssetsPostTestCase(ApiTestCase):
    @patch('planet_rest_api.models.asset.Asset.validate')
    def test_success(self, validate):
        # A valid request to `POST /assets`
        rv = self.post_response('/assets', data=json.dumps({
            'name': 'test-satellite',
            'type': 'satellite',
            'class': 'rapideye',
        }))

        # has no errors
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.json, {
            'name': 'test-satellite',
            'type': 'satellite',
            'class': 'rapideye',
        })

        # uses `validate` under the hood
        # DEV: This asserts we have a contract to our model unit test
        self.assertEqual(validate.call_count, 1)

        # creates our asset inside of our database
        asset = Asset.get('test-satellite')
        self.assertTrue(asset)
        self.assertEqual(asset.name, 'test-satellite')
        self.assertEqual(asset.type, 'satellite')
        self.assertEqual(asset.klass, 'rapideye')

    def test_invalid(self):
        # An invalid request to `POST /assets`
        rv = self.post_response('/assets', data=json.dumps({
            # Intentionally empty
        }))

        # receives an error
        self.assertEqual(rv.status_code, 400)
        self.assertEqual(rv.json, {'message': 'Invalid request'})

        # TODO: Assert db is empty
