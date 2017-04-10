# Load in our dependencies
from unittest import TestCase


# Define our tests
class ModelAssetTestCase(TestCase):
    def test_validate_name_ascii_valid(self):
        # An asset with an ASCII, underscore,and dashed name

        # has no validation errors
        pass

    def test_validate_name_ascii_invalid(self):
        # An asset with a non-ASCII name

        # has validation errors
        pass
