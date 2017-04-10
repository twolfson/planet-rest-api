# planet-rest-api [![Build status](https://travis-ci.org/twolfson/planet-rest-api.svg?branch=master)](https://travis-ci.org/twolfson/planet-rest-api)

REST API coding challenge for Planet Labs

TODO: Test server manually

## Requirements
Before getting started, make sure the following tools are installed locally:

- Python 2.7
- [virutalenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

## Getting Started
To get a local copy of our repository running, run the following:

```bash
# Clone our repository
git clone git@github.com:twolfson/planet-rest-api.git
cd planet-rest-api

# Set up a virtual environment
mkvirtualenv planet-rest-api

# Install our dependencies
bin/bootstrap.sh

# Start our server
./start.sh

# On future iterations, we can use
workon planet-rest-api
./start.sh
```

## Documentation
### Testing
Tests can be run via:

```bash
# Runs `nosetests`
./test.sh
```

## Examples
_(Coming soon)_

## Contributing
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality. Test via `nosetests`.

## Unlicense
As of Apr 10 2017, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the [UNLICENSE][].

[UNLICENSE]: UNLICENSE
