# Define a store for all assets
asset_map = {}

# Define our Asset class
class Asset(object):
    def __init__(self, name):
        self.name = name

    def save(self):
        asset_map[self.name] = self

    def serialize(self):
        return {
            'name': self.name,
        }

    @classmethod
    def get_all(cls):
        return asset_map.values()
