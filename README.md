# Fibonacci numbers

Web-api, which generates sequence of fibonacci numbers

## Requirements
Python 3.6

Flask 0.12.2

Redis 4.0.9

## Download
https://github.com/Izpa/fibonacci_numbers/archive/develop.zip

or

```
git clone git@github.com:Izpa/fibonacci_numbers.git
```

## Installation
In virtualenv run

```
pip install -r requirements.txt
```

Then you must set environment variable
APP_SETTINGS
(development, testing, staging or production, production is default),
FLASK_APP (run.py), SECRET (random string)
and REDIS_URL (redis server url, redis://localhost:6379/0 is default)

```
export APP_SETTINGS="development"
export FLASK_APP="run.py"
export SECRET="some_random_string"
export REDIS_URL="redis_url"
```

And then run the web-application

```
flask run
```

Now web-application running on http://127.0.0.1:5000/


```
gunicorn gunicorn_run:app
```

And get application by url http://127.0.0.1:8000/

Or you can use docker or docker-compose (redis included)

## Usage example

Simple frontend for testing available on root url

API request example

```
/fibonachi/?from=5&to=10
```

API response example

```
[5, 8, 13, 21, 34, 55]
```

## Run unit tests

```
python -m unittest discover
```