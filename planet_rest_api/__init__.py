# Load in our dependencies
from flask import Flask, jsonify

# Define our application
app = Flask(__name__)


# Define our assets class
# TODO: Relocate into models file
class Asset(object):
    # Define a store for all assets
    asset_map = {}

    def __init__(self, name):
        self.name = name

    def save(self):
        self.asset_map[self.name] = self

    def serialize(self):
        return {
            'name': self.name,
        }

    @classmethod
    def get_all(cls):
        return cls.asset_map.values()


# Bind our routes
@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'OK'})


@app.route('/assets', methods=['GET'])
def assets_get():
    return jsonify([
        asset.serialize()
        for asset in Asset.get_all()
    ])
