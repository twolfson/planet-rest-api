# Load in our dependencies
from flask import Flask, jsonify

# Define our application
app = Flask(__name__)

# Bind our routes
@app.route('/')
def root():
    return jsonify({'message': 'OK'})

@app.route('/asset')
def asset_list():
    return jsonify([
    ])
