#!/usr/bin/env bash
# Exit on first error
set -e

# Install our dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
