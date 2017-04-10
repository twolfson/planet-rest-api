# Load in our dependencies
from unittest import TestCase

# http://werkzeug.pocoo.org/docs/0.11/exceptions/#werkzeug.exceptions.BadRequest
from werkzeug.exceptions import BadRequest

from planet_rest_api.models.asset import Asset


# Define our tests
class ModelAssetTestCase(TestCase):
    # Validate: Name
    def test_validate_name_valid(self):
        # An asset with an alphanumeric, underscore,and dashed name
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

    # Validate: Type
    def test_validate_type_valid(self):
        # An asset with a valid asset type
        asset = Asset(name='abcd1234', type='satellite',
                      klass=Asset.CLASS_SATELLITE_DOVE)

        # has no validation errors
        asset.validate()

    def test_validate_type_invalid(self):
        # An asset with an invalid asset type
        asset = Asset(name='abcd1234', type='not-a-satellite',
                      klass=Asset.CLASS_SATELLITE_DOVE)

        # has a validation error
        with self.assertRaisesRegexp(BadRequest, 'Invalid asset type'):
            asset.validate()

    # Validate: Class
    def test_validate_class_matching(self):
        # An asset with a matching asset class
        asset = Asset(name='abcd1234', type='satellite',
                      klass='dove')

        # has no validation errors
        asset.validate()

        # Sanity check for antenna
        asset = Asset(name='abcd1234', type='antenna',
                      klass='dish')
        asset.validate()

    def test_validate_class_non_matching(self):
        # An asset with a non-matching asset class
        asset = Asset(name='abcd1234', type='satellite',
                      klass='not-a-dove')

        # has a validation error
        with self.assertRaisesRegexp(BadRequest, 'Invalid asset class'):
            asset.validate()
