# Load in our dependencies
from flask import Flask, jsonify

from planet_rest_api.models.asset import Asset


# Define our application
app = Flask(__name__)


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
