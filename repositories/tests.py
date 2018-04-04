from collections import OrderedDict
from unittest import TestCase

from repositories.redis import FibonacciNumbersRepo


class FibonacciNumbersRepoTestCase(TestCase):
    def setUp(self):
        self.repo = FibonacciNumbersRepo()
    
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

    def test_list_ncorrect_start_type(self):
        with self.assertRaises(TypeError) as e:
            list(self.repo.list('x', 1))
        self.assertEqual(str(e.exception), 'start must be integer')

    def test_list_incorrect_end_type(self):
        with self.assertRaises(TypeError) as e:
            list(self.repo.list(1, 'x'))
        self.assertEqual(str(e.exception), 'end must be integer')

    def test_list_negative_start(self):
        with self.assertRaises(ValueError) as e:
            list(self.repo.list(-1, 1))
        self.assertEqual(str(e.exception), 'start must be positive')

    def test_list_negative_end(self):
        with self.assertRaises(ValueError) as e:
            list(self.repo.list(1, -1))
        self.assertEqual(str(e.exception), 'end must be positive')

    def test_list_start_greater_to_end(self):
        with self.assertRaises(ValueError) as e:
            list(self.repo.list(2, 1))
        self.assertEqual(str(e.exception), 'end must be greater than or '
                                           'equal to start')

    def test_list_empty_arguments(self):
        with self.assertRaises(TypeError) as e:
            list(self.repo.list())
        self.assertEqual(
            str(e.exception),
            "list() missing 2 required positional "
            "arguments: 'start' and 'end'")

    def test_list_one_argument(self):
        with self.assertRaises(TypeError) as e:
            list(self.repo.list(1))
        self.assertEqual(
            str(e.exception),
            "list() missing 1 required positional "
            "argument: 'end'")
