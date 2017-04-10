#!/usr/bin/env bash
# Exit on first error
set -e

# Run our lint
if test "$SKIP_LINT" != "TRUE"; then
  flake8 planet_rest_api
fi

# Run our tests
nosetests --nocapture $*
