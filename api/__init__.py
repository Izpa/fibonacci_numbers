"""
Base application module.

Contain routing and some additional methods.
"""
import json

from flask import Flask, render_template, request, Response
from instance.settings import app_config
from repositories.redis import FibonacciNumbersRepo
from shared.response_object import ResponseFailure, ResponseSuccess
from use_cases.fibonacci_numbers import GetFibonacciSequenceUseCase
from use_cases.request_objects import GetFibonacciSequenceRequestObject

STATUS_CODES = {
    ResponseSuccess.SUCCESS: 200,
    ResponseFailure.RESOURCE_ERROR: 404,
    ResponseFailure.PARAMETERS_ERROR: 400,
    ResponseFailure.SYSTEM_ERROR: 500
}


def _create_request_object_from_request_args(request_args: dict):
    params = {
        'start': request_args.get('from'),
        'end': request_args.get('to')
    }
    return GetFibonacciSequenceRequestObject(**params)


def create_app(config_name):
    """
    Create flask application.

    :param config_name: application configuration name.
    :return: flask application.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('settings.py')

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/fibonachi/')
    def fibonacci():
        request_object = _create_request_object_from_request_args(request.args)
        repo = FibonacciNumbersRepo()
        use_case = GetFibonacciSequenceUseCase(repo)
        response = use_case.execute(request_object)
        return Response(json.dumps(response.value).strip('"'),
                        status=STATUS_CODES[response.type])

    return app
