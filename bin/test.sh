#!/usr/bin/env bash
# Exit on first error
set -e

# Run our lint
if test "$SKIP_LINT" != "TRUE"; then
  flake8 planet_rest_api
fi

# Enable globstar for finding all our `_test.py` files
shopt -s globstar

# Run our tests
nosetests --nocapture planet_rest_api/test/**/*_test.py $*

# Disable globstar
shopt -u globstar
