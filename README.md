# planet-rest-api [![Build status](https://travis-ci.org/twolfson/planet-rest-api.svg?branch=master)](https://travis-ci.org/twolfson/planet-rest-api)

REST API coding challenge for Planet Labs

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
### Resources
We have the following resource types:

#### Asset
Dictionary containing information about physical asset. It has the following structure:

- name `String` - Name of asset
    - This must be unique across all access
    - This may only contain alphanumeric ASCII characters, underscores, and dashes
    - This cannot start with an underscore or dash
    - This must be between 4 and 64 characters long
- type `String` - Type of asset
    - This must be either "satellite" or "antenna"
- class `String` - Class of asset, depends on `type`
    - For a "satellite" asset, this must be either "dove" or "rapideye"
    - For an "antenna" asset, this must be either "dish" or "yagi"

**Examples:**

```json
{
  "name": "dove1",
  "type": "satellite",
  "class": "dove"
}
```

```json
{
  "name": "yagi3",
  "type": "antenna",
  "class": "yagi3"
}
```

### API
We expose a REST API with JSON-based resources with the following endpoints:

#### GET /
Basic health check for our API

**Request body:**

None

**Response body:**

- message `String` - OK response from server

**Example:**

```bash
$ curl http://localhost:5000/
{
  "message": "OK"
}
```

#### GET /assets
List all existing assets

**Request body:**

None

**Response body:**

- asset[] `list`
    - asset `Asset` - JSON representation of asset

**Example:**

```bash
$ curl http://localhost:5000/assets
[
  {
    "name": "dove1",
    "type": "satellite",
    "class": "dove"
  }
]
```

#### POST /assets
Create a new asset

**Request body:**

Parameters should match `Asset` specification (e.g. `name`, `type`)

**Response body:**

Upon success, response will match serialized `Asset` result

**Example:**

```bash
$ curl -X POST http://localhost:5000/assets \
  -H 'Content-Type: application/json' \
  --data '{
    "name": "dove1",
    "type": "satellite",
    "class": "dove"
  }'
{
  "name": "dove1",
  "type": "satellite",
  "class": "dove"
}
```

#### GET /assets/:name
Retrieve an asset by its name

**Request body:**

None

**Response body:**

Upon success, response will be JSON representation of asset

**Example:**

```bash
$ curl http://localhost:5000/assets/dove1
{
  "class": "dove",
  "name": "dove1",
  "type": "satellite"
}
```

#### Error handlers
If an error is encountered, then we will reply with the following format:

**Response body:**

- message `String` - Explanation of error

**Notes:**

We will also send an HTTP status code matching the error (e.g. 400, 404, 500).

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
