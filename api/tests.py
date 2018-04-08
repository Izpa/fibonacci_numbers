import unittest
from unittest.mock import MagicMock, patch

from api import _create_request_object_from_request_args
from run import app

numbers_list_mock = MagicMock(return_value=[None, None, None, None])
add_numbers_mock = MagicMock()


@patch('repositories.redis.FibonacciNumbersRepo.numbers_list',
       numbers_list_mock)
@patch('repositories.redis.FibonacciNumbersRepo.add_numbers',
       add_numbers_mock)
class IndexTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_with_all_correct_params(self):
        response = self.test_client.get(
            '/fibonachi/?from=18&to=21',
            content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,
                         b'[2584, 4181, 6765, 10946]')

    def test_without_params(self):
        response = self.test_client.get('/fibonachi/', content_type='html/text')
        self.assertEqual(response.status_code, 400)

    def test_from_param_is_required(self):
        response = self.test_client.get(
            '/fibonachi/?to=21',
            content_type='html/text')
        self.assertEqual(response.status_code, 400)

    def test_from_param_must_be_integer(self):
        response = self.test_client.get(
            '/fibonachi/?from=test&to=21',
            content_type='html/text')
        self.assertEqual(response.status_code, 400)

    def test_to_param_is_required(self):
        response = self.test_client.get(
            '/fibonachi/?from=18',
            content_type='html/text')
        self.assertEqual(response.status_code, 400)

    def test_to_param_must_be_integer(self):
        response = self.test_client.get(
            '/fibonachi/?from=18&to=test',
            content_type='html/text')
        self.assertEqual(response.status_code, 400)


class CreateRequestObjectFromRequestArgsTestCase(unittest.TestCase):
    def test_with_all_correct_params(self):
        request_object = _create_request_object_from_request_args(
            {'from': '18', 'to': '21'})
        self.assertEqual(bool(request_object), True)
        self.assertEqual(18, request_object.start)
        self.assertEqual(21, request_object.end)
