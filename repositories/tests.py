"""Tests for all in repositories package."""
from unittest import TestCase

from repositories.redis import FibonacciNumbersRepo


class FibonacciNumbersRepoTestCase(TestCase):
    """Tests for FibonacciNumbersRepo class."""

    repo = FibonacciNumbersRepo()

    def test_numbers_list_incorrect_start_type(self):
        """
        Run numbers_list with incorrect start type.

        Except raising TypeError.
        """
        with self.assertRaises(TypeError) as e:
            self.repo.numbers_list('x', 1)
        self.assertEqual(str(e.exception), 'start must be integer')

    def test_numbers_list_incorrect_end_type(self):
        """
        Run numbers_list with incorrect end type.

        Except raising TypeError.
        """
        with self.assertRaises(TypeError) as e:
            self.repo.numbers_list(1, 'x')
        self.assertEqual(str(e.exception), 'end must be integer')

    def test_numbers_list_negative_start(self):
        """
        Run numbers_list with negative start.

        Except raising ValueError.
        """
        with self.assertRaises(ValueError) as e:
            self.repo.numbers_list(-1, 1)
        self.assertEqual(str(e.exception), 'start must be positive')

    def test_numbers_list_negative_end(self):
        """
        Run numbers_list with negative end.

        Except raising ValueError.
        """
        with self.assertRaises(ValueError) as e:
            self.repo.numbers_list(1, -1)
        self.assertEqual(str(e.exception), 'end must be positive')

    def test_numbers_list_start_greater_to_end(self):
        """
        Run numbers_list with start greater then end.

        Except raising ValueError.
        """
        with self.assertRaises(ValueError) as e:
            self.repo.numbers_list(2, 1)
        self.assertEqual(str(e.exception), 'end must be greater than or '
                                           'equal to start')

    def test_numbers_list_empty_arguments(self):
        """
        Run numbers_list without arguments.

        Except raising TypeError.
        """
        with self.assertRaises(TypeError) as e:
            self.repo.numbers_list()
        self.assertEqual(
            str(e.exception),
            'numbers_list() missing 2 required positional '
            "arguments: 'start' and 'end'")

    def test_numbers_list_one_argument(self):
        """
        Run numbers_list with one argument.

        Except raising TypeError.
        """
        with self.assertRaises(TypeError) as e:
            self.repo.numbers_list(1)
        self.assertEqual(
            str(e.exception),
            'numbers_list() missing 1 required positional '
            "argument: 'end'")
