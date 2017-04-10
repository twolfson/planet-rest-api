# planet-rest-api [![Build status](https://travis-ci.org/twolfson/planet-rest-api.svg?branch=master)](https://travis-ci.org/twolfson/planet-rest-api)

REST API coding challenge for Planet Labs

TODO: Document endpoints

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
bin/start.sh
```

Our server should be running at <http://localhost:5000/>. For making requests, see our documentation.

**On future iterations, we can use:**

```bash
workon planet-rest-api
bin/start.sh
```

## Documentation
### Testing
Tests can be run via:

```bash
# Runs `nosetests`
bin/test.sh
```

## Contributing
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality. Test via `bin/test.sh`.

## Unlicense
As of Apr 10 2017, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the [UNLICENSE][].

[UNLICENSE]: UNLICENSE
