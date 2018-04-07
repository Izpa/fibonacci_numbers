from unittest import TestCase

from repositories.redis import FibonacciNumbersRepo


class FibonacciNumbersRepoTestCase(TestCase):
    repo = FibonacciNumbersRepo()

    def test_numbers_list_incorrect_start_type(self):
        with self.assertRaises(TypeError) as e:
            self.repo.numbers_list('x', 1)
        self.assertEqual(str(e.exception), 'start must be integer')

    def test_numbers_list_incorrect_end_type(self):
        with self.assertRaises(TypeError) as e:
            self.repo.numbers_list(1, 'x')
        self.assertEqual(str(e.exception), 'end must be integer')

    def test_numbers_list_negative_start(self):
        with self.assertRaises(ValueError) as e:
            self.repo.numbers_list(-1, 1)
        self.assertEqual(str(e.exception), 'start must be positive')

    def test_numbers_list_negative_end(self):
        with self.assertRaises(ValueError) as e:
            self.repo.numbers_list(1, -1)
        self.assertEqual(str(e.exception), 'end must be positive')

    def test_numbers_list_start_greater_to_end(self):
        with self.assertRaises(ValueError) as e:
            self.repo.numbers_list(2, 1)
        self.assertEqual(str(e.exception), 'end must be greater than or '
                                           'equal to start')

    def test_numbers_list_empty_arguments(self):
        with self.assertRaises(TypeError) as e:
            self.repo.numbers_list()
        self.assertEqual(
            str(e.exception),
            'numbers_list() missing 2 required positional '
            "arguments: 'start' and 'end'")

    def test_numbers_list_one_argument(self):
        with self.assertRaises(TypeError) as e:
            self.repo.numbers_list(1)
        self.assertEqual(
            str(e.exception),
            'numbers_list() missing 1 required positional '
            "argument: 'end'")
