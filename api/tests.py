"""Tests for all in api package."""
import unittest
from unittest.mock import MagicMock, patch

from api import _create_request_from_request_args
from run import app

numbers_list_mock = MagicMock(return_value=[None, None, None, None])
add_numbers_mock = MagicMock()


@patch('repositories.redis.FibonacciNumbersRepo.numbers_list',
       numbers_list_mock)
@patch('repositories.redis.FibonacciNumbersRepo.add_numbers',
       add_numbers_mock)
class FibonacciTestCase(unittest.TestCase):
    """Tests for fibonacci url."""

    def setUp(self):
        """Set client for url requests."""
        self.test_client = app.test_client(self)

    def test_with_all_correct_params(self):
        """
        Get url with correct parameters.

        Except response with 200 code and list with fibonacci sequence.
        """
        response = self.test_client.get(
            '/fibonachi/?from=18&to=21',
            content_type='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,
                         b'[2584, 4181, 6765, 10946]')

    def test_without_params(self):
        """
        Get url without parameters.

        Except response with 400 code.
        """
        response = self.test_client.get('/fibonachi/', content_type='html/text')
        self.assertEqual(response.status_code, 400)

    def test_from_param_is_required(self):
        """
        Get url with only from parameter.

        Except response with 400 code.
        """
        response = self.test_client.get(
            '/fibonachi/?to=21',
            content_type='html/text')
        self.assertEqual(response.status_code, 400)

    def test_from_param_must_be_integer(self):
        """
        Get url with incorrect from parameter type.

        Except response with 400 code.
        """
        response = self.test_client.get(
            '/fibonachi/?from=test&to=21',
            content_type='html/text')
        self.assertEqual(response.status_code, 400)

    def test_to_param_is_required(self):
        """
        Get url with only to parameter.

        Except response with 400 code.
        """
        response = self.test_client.get(
            '/fibonachi/?from=18',
            content_type='html/text')
        self.assertEqual(response.status_code, 400)

    def test_to_param_must_be_integer(self):
        """
        Get url with incorrect to parameter type.

        Except response with 400 code.
        """
        response = self.test_client.get(
            '/fibonachi/?from=18&to=test',
            content_type='html/text')
        self.assertEqual(response.status_code, 400)


class CreateRequestObjectFromRequestArgsTestCase(unittest.TestCase):
    """Tests for _create_request_from_request_args."""

    def test_with_correct_params(self):
        """
        Run with correct args.

        Except valid request object with correct start and end values.
        """
        request = _create_request_from_request_args(
            {'from': '18', 'to': '21'})
        self.assertTrue(bool(request))
        self.assertEqual(18, request.start)
        self.assertEqual(21, request.end)

    def test_with_incorrect_start_type(self):
        """
        Run with incorrect type of from parameter.

        Expect invalid request object with error on start parameter.
        """
        request = _create_request_from_request_args(
            {'from': 'x', 'to': '1'})

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'start')
        self.assertEqual(request.errors[0]['message'],
                         'must be integer')

    def test_with_incorrect_end_type(self):
        """
        Run with incorrect type of to parameter.

        Expect invalid request object with error on end parameter.
        """
        request = _create_request_from_request_args(
            {'from': '1', 'to': 'x'})

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'end')
        self.assertEqual(request.errors[0]['message'],
                         'must be integer')

    def test_with_negative_start(self):
        """
        Run with negative from parameter.

        Expect invalid request object with error on start parameter.
        """
        request = _create_request_from_request_args(
            {'from': '-1', 'to': '1'})

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'start')
        self.assertEqual(request.errors[0]['message'],
                         'must be positive')

    def test_with_negative_end(self):
        """
        Run with negative to parameter.

        Expect invalid request object with error on end parameter.
        """
        request = _create_request_from_request_args(
            {'from': '1', 'to': '-1'})

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'end')
        self.assertEqual(request.errors[0]['message'],
                         'must be positive')

    def test_with_start_greater_to_end(self):
        """
        Run with start greater to to parameter.

        Expect invalid request object with error on end parameter.
        """
        request = _create_request_from_request_args(
            {'from': '2', 'to': '1'})

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'end')
        self.assertEqual(request.errors[0]['message'],
                         'must be greater than or equal to start')

    def test_with_empty_arguments(self):
        """
        Run without arguments.

        Expect invalid request object with error on start parameter.
        """
        request = _create_request_from_request_args({})

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'start')
        self.assertEqual(request.errors[0]['message'], 'is required')

    def test_with_only_start(self):
        """
        Run with only from parameter.

        Expect invalid request object with error on end parameter.
        """
        request = _create_request_from_request_args(
            {'from': '1'})

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'end')
        self.assertEqual(request.errors[0]['message'], 'is required')

    def test_with_only_end(self):
        """
        Run with only to parameter.

        Expect invalid request object with error on end parameter.
        """
        request = _create_request_from_request_args(
            {'end': '1'})

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'start')
        self.assertEqual(request.errors[0]['message'], 'is required')
