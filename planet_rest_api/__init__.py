# Load in our dependencies
from flask import Flask, jsonify, request
from flask_json_multidict import get_json_multidict

from planet_rest_api.models.asset import Asset


# Define our application
app = Flask(__name__)


# Install Multidict wrapper for JSON
# https://github.com/underdogio/flask-json-multidict/tree/1.0.0
# DEV: This is to get easy `400` errors with consistent format to urlencoded bodies
def resolve_request_body():
    """Before every request, resolve `request.body` from either `request.form` or `request.get_json()`"""
    request.body = request.form
    if request.headers['content-type'] == 'application/json':
        request.body = get_json_multidict(request)
app.before_request(resolve_request_body) # noqa


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


@app.route('/assets', methods=['POST'])
def assets_name_post():
    # Generate our asset
    # DEV: We are using `flask-json-multidict` which will raise a `BadRequestKeyError` on a missing parameter
    asset = Asset(
        name=request.body['name'],
        type=request.body['type'],
        klass=request.body['class'],
    )

    # Save and reply with our asset
    asset.save()
    return jsonify(asset.serialize())


@app.route('/assets/<name>', methods=['GET'])
def assets_name_get(name):
    asset = Asset.get_or_404(name)
    return jsonify(asset.serialize())


# Define our generic error handler
@app.errorhandler(400)
def invalid_request(error):
    # TODO: Add better messaging about which key is missing based on `BadRequestKeyError`
    return jsonify({'message': 'Invalid request'}), 400


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({'message': 'Resource not found'}), 404
