from collections import OrderedDict
from unittest import TestCase

from repositories.redis import FibonacciNumbersRepo


class FibonacciNumbersRepoTestCase(TestCase):
    def test_convert_response_with_simple_response(self):
        self.assertEqual(
            FibonacciNumbersRepo._convert_response([(1, 1)]),
            OrderedDict([(1, 1)])
        )

    def test_convert_response_inversion(self):
        self.assertEqual(
            FibonacciNumbersRepo._convert_response([(2, 1)]),
            OrderedDict([(1, 2)])
        )

    def test_convert_response_sorting(self):
        self.assertEqual(
            FibonacciNumbersRepo._convert_response([(2, 2), (1, 1)]),
            OrderedDict([(1, 1), (2, 2)])
        )

    def test_convert_response_type_conversion(self):
        self.assertEqual(
            FibonacciNumbersRepo._convert_response([('2', '2'), ('1', '1')]),
            OrderedDict([(1, 1), (2, 2)])
        )
