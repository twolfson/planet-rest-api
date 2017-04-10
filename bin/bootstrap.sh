#!/usr/bin/env bash
# Exit on first error
set -e

# Install our package
python setup.py develop

# Install dev dependencies
pip install -r requirements-dev.txt

