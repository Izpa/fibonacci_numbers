# Fibonacci numbers

Web-api, which generates sequence of fibonacci numbers

## Requirements
Python 3.6

Flask 0.12.2

## Download
https://gitlab.com/MarkovArtemP/fibonacci_numbers/repository/develop/archive.zip

or

```
git clone git@gitlab.com:MarkovArtemP/fibonacci_numbers.git
```

## Installation
In virtualenv run

```
pip install -r requirements.txt
```

Then you must set environment variable APP_SETTINGS (development, testing, staging or production), FLASK_APP (run.py)
and SECRET (random string)

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

Also you can use docker file in project root (you also must set environment variables for your container)

## Usage example

Request example

```

```

Response example

```

```

## Run unit tests

```
python -m unittest discover
```