# Load in our dependencies
from unittest import TestCase

# http://werkzeug.pocoo.org/docs/0.11/exceptions/#werkzeug.exceptions.BadRequest
from werkzeug.exceptions import BadRequest

from planet_rest_api.models.asset import Asset


# TODO: Test leading dash
# TODO: Test leading underscore
# TODO: Test short name
# TODO: Test long name
# TODO: Test valid type/invalid type
# TODO: Test matching class/non-matching class

# Define our tests
class ModelAssetTestCase(TestCase):
    def test_validate_name_valid(self):
        # An asset with an alphanumerica, underscore,and dashed name
        asset = Asset(name='abcd1234-_', type=Asset.TYPE_SATELLITE,
                      klass=Asset.CLASS_SATELLITE_DOVE)

        # has no validation errors
        asset.validate()

    def test_validate_name_invalid_bad_chars(self):
        # An asset with bad characters in its name
        asset = Asset(name='abcd1234!', type=Asset.TYPE_SATELLITE,
                      klass=Asset.CLASS_SATELLITE_DOVE)

        # has a validation error
        with self.assertRaisesRegexp(BadRequest, 'Name contains non-alphanumeric'):
            asset.validate()

    def test_validate_name_invalid_short(self):
        # An asset with a short name
        asset = Asset(name='abc', type=Asset.TYPE_SATELLITE,
                      klass=Asset.CLASS_SATELLITE_DOVE)

        # has a validation error
        with self.assertRaisesRegexp(BadRequest, 'Name is too short'):
            asset.validate()

    def test_validate_name_invalid_long(self):
        # An asset with a long name
        asset = Asset(name='a' * 65, type=Asset.TYPE_SATELLITE,
                      klass=Asset.CLASS_SATELLITE_DOVE)

        # has a validation error
        with self.assertRaisesRegexp(BadRequest, 'Name is too long'):
            asset.validate()

    def test_validate_name_invalid_leading_dash(self):
        # An asset with a leading dash in its name name
        asset = Asset(name='-abcdef', type=Asset.TYPE_SATELLITE,
                      klass=Asset.CLASS_SATELLITE_DOVE)

        # has a validation error
        with self.assertRaisesRegexp(BadRequest, 'Name begins with a dash or underscore'):
            asset.validate()

    def test_validate_name_invalid_leading_underscore(self):
        # An asset with a leading underscore in its name name
        asset = Asset(name='_abcdef', type=Asset.TYPE_SATELLITE,
                      klass=Asset.CLASS_SATELLITE_DOVE)

        # has a validation error
        with self.assertRaisesRegexp(BadRequest, 'Name begins with a dash or underscore'):
            asset.validate()
