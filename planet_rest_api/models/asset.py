# Define a store for all assets
asset_map = {}

# TODO: Disallow overwriting existing assets
# TODO: Unit test bad names and spy our create method uses validate


# Define our Asset class
class Asset(object):
    def __init__(self, name):
        # Save our model information
        self.name = name

    def save(self):
        # Run validation
        self.validate()

        # Save our model
        asset_map[self.name] = self

    def validate(self):
        # Validate our asset name
        pass

    def serialize(self):
        return {
            'name': self.name,
        }

    @classmethod
    def get_all(cls):
        return asset_map.values()
