"""
Base application module.

Contain routing and some additional methods.
"""
import json

from flask import Flask, render_template, request, Response
from instance.settings import app_config
from repositories.redis import FibonacciNumbersRepo
from shared.use_case import ResponseFailure, ResponseSuccess
from use_cases.fibonacci_numbers import GetFibonacciSequenceRequest, \
    GetFibonacciSequenceUseCase

STATUS_CODES = {
    ResponseSuccess.SUCCESS: 200,
    ResponseFailure.RESOURCE_ERROR: 404,
    ResponseFailure.PARAMETERS_ERROR: 400,
    ResponseFailure.SYSTEM_ERROR: 500
}


def _create_request_from_request_args(request_args: dict):
    params = {
        'start': request_args.get('from'),
        'end': request_args.get('to')
    }
    return GetFibonacciSequenceRequest(**params)


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
        use_case_request = _create_request_from_request_args(request.args)
        repo = FibonacciNumbersRepo()
        use_case = GetFibonacciSequenceUseCase(repo)
        response = use_case.execute(use_case_request)
        return Response(json.dumps(response.value).strip('"'),
                        status=STATUS_CODES[response.type])

    return app
