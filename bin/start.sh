#!/usr/bin/env bash
# Exit on first error
set -e

# Start our server
# http://flask.pocoo.org/docs/0.12/quickstart/
export FLASK_APP=planet_rest_api
flask run
