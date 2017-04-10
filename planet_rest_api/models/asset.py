# Load in our dependencies
import re

from flask import abort


# Define our Asset class
class Asset(object):
    # Define our constants
    TYPE_SATELLITE = 'satellite'
    TYPE_ANTENNA = 'antenna'
    VALID_TYPES = [TYPE_SATELLITE, TYPE_ANTENNA]

    CLASS_SATELLITE_DOVE = 'dove'
    CLASS_SATELLITE_RAPIDEYE = 'rapideye'
    CLASS_ANTENNA_DISH = 'dish'
    CLASS_ANTENNA_YAGI = 'yagi'
    VALID_CLASSES = {
        TYPE_SATELLITE: [CLASS_SATELLITE_DOVE, CLASS_SATELLITE_RAPIDEYE],
        TYPE_ANTENNA: [CLASS_ANTENNA_DISH, CLASS_ANTENNA_YAGI],
    }

    # Define a store for all assets
    _asset_map = {}

    # Define our methods
    def __init__(self, name, type, klass):
        # Save our model information
        self.name = name
        self.type = type
        self.klass = klass

        # Mark our asset as new
        self.is_new = True

    @classmethod
    def _reset(cls):
        cls._asset_map = {}

    @classmethod
    def get_all(cls):
        return cls._asset_map.values()

    @classmethod
    def get(self, name):
        return self._asset_map.get(name)

    @classmethod
    def get_or_404(self, name):
        if name not in self._asset_map:
            abort(404)
        else:
            return self._asset_map[name]

    def save(self):
        # Run validation
        self.validate()

        # If our asset is new
        if self.is_new is True:
            # Assert it isn't overwriting an asset
            if self.name in self._asset_map:
                abort(400)

            # Save it
            self._asset_map[self.name] = self

        # Otherwise, do nothing -- it's already in our db
        self.is_new = False

    def validate(self):
        # Validate our asset name
        # DEV: We could use a custom error here and add a custom handler
        #   but for this exercise, a Flask error should work
        # DEV: We assert length first to avoid errors with `self.name[0]`
        if len(self.name) < 4:
            abort(400, 'Name is too short (under 4 characters)')
        if len(self.name) > 64:
            abort(400, 'Name is too long (over 64 characters)')
        if re.search(r'[^A-Za-z0-9\-_]', self.name):
            abort(400, 'Name contains non-alphanumeric, dash, or underscore characters')
        if self.name[0] in ['-', '_']:
            abort(400, 'Name begins with a dash or underscore')

    def serialize(self):
        return {
            'name': self.name,
            'type': self.type,
            'class': self.klass,
        }
