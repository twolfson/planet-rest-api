# Load in our dependencies
from flask import Flask, jsonify

# Define our application
app = Flask(__name__)


# Define our assets class
# TODO: Relocate into models file
class Asset(object):
    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            'name': self.name,
        }


# Define our assets
assets = [Asset('Dove')]


# Bind our routes
@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'OK'})


@app.route('/assets', methods=['GET'])
def assets_get():
    return jsonify([
        asset.serialize()
        for asset in assets
    ])
