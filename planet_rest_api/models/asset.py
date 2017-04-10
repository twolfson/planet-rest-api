# Load in our dependencies
from flask import abort

# TODO: Disallow overwriting existing assets
# TODO: Unit test bad names and spy our create method uses validate


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

    @classmethod
    def _reset(cls):
        cls._asset_map = {}

    @classmethod
    def get_all(cls):
        return cls._asset_map.values()

    @classmethod
    def get_or_404(self, name):
        if name not in self._asset_map:
            abort(404)
        else:
            return self._asset_map[name]

    def save(self):
        # Run validation
        self.validate()

        # Save our model
        self._asset_map[self.name] = self

    def validate(self):
        # Validate our asset name
        pass

    def serialize(self):
        return {
            'name': self.name,
            'type': self.type,
            'class': self.klass,
        }
