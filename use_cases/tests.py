from unittest import TestCase

from use_cases.fibonacci_numbers import GetFibonacciSequenceUseCase


class CalculateFibonacciNumberByOrderTestCase(TestCase):
    def test_zero_fibonacci_number(self):
        self.assertEqual(
            0, GetFibonacciSequenceUseCase._calculate_fibonacci_number(0))

    def test_first_fibonacci_number(self):
        self.assertEqual(
            1, GetFibonacciSequenceUseCase._calculate_fibonacci_number(1))

    def test_second_fibonacci_number(self):
        self.assertEqual(
            1, GetFibonacciSequenceUseCase._calculate_fibonacci_number(2))

    def test_third_fibonacci_number(self):
        self.assertEqual(
            2, GetFibonacciSequenceUseCase._calculate_fibonacci_number(3))

    def test_hight_fibonacci_number(self):
        self.assertEqual(
            10946, GetFibonacciSequenceUseCase._calculate_fibonacci_number(21))

    def test_negative_order(self):
        with self.assertRaises(ValueError) as e:
            GetFibonacciSequenceUseCase._calculate_fibonacci_number(-1)
        self.assertEqual(str(e.exception), 'order must be positive')

    def test_negative_order_type(self):
        with self.assertRaises(TypeError) as e:
            GetFibonacciSequenceUseCase._calculate_fibonacci_number('x')
        self.assertEqual(str(e.exception), 'order must be integer')

    def test_incorrect_order_type(self):
        with self.assertRaises(TypeError) as e:
            GetFibonacciSequenceUseCase._calculate_fibonacci_number()
        self.assertEqual(
            str(e.exception),
            "_calculate_fibonacci_number() missing 1 required positional "
            "argument: 'order'")


class CalculateFibonacciSequenceTestCase(TestCase):
    def test_simple_sequence(self):
        self.assertEqual(
            [0, 1, 1, 2],
            list(GetFibonacciSequenceUseCase._calculate_fibonacci_sequence(
                0, 3)))
        
    def test_no_zero_started_sequence(self):
        self.assertEqual(
            [1, 2],
            list(
                GetFibonacciSequenceUseCase._calculate_fibonacci_sequence(
                    2, 3)))
        
    def test_hight_sequence(self):
        self.assertEqual(
            [2584, 4181, 6765, 10946],
            list(GetFibonacciSequenceUseCase._calculate_fibonacci_sequence(
                18, 21)))
    
    def test_incorrect_start_type(self):
        with self.assertRaises(TypeError) as e:
            list(GetFibonacciSequenceUseCase._calculate_fibonacci_sequence(
                'x', 1))
        self.assertEqual(str(e.exception), 'start must be integer')

    def test_incorrect_end_type(self):
        with self.assertRaises(TypeError) as e:
            list(GetFibonacciSequenceUseCase._calculate_fibonacci_sequence(
                1, 'x'))
        self.assertEqual(str(e.exception), 'end must be integer')

    def test_negative_start(self):
        with self.assertRaises(ValueError) as e:
            list(GetFibonacciSequenceUseCase._calculate_fibonacci_sequence(
                -1, 1))
        self.assertEqual(str(e.exception), 'start must be positive')

    def test_negative_end(self):
        with self.assertRaises(ValueError) as e:
            list(GetFibonacciSequenceUseCase._calculate_fibonacci_sequence(
                1, -1))
        self.assertEqual(str(e.exception), 'end must be positive')

    def test_start_greater_to_end(self):
        with self.assertRaises(ValueError) as e:
            list(GetFibonacciSequenceUseCase._calculate_fibonacci_sequence(
                2, 1))
        self.assertEqual(str(e.exception), 'end must be greater than or '
                                           'equal to start')

    def test_empty_arguments(self):
        with self.assertRaises(TypeError) as e:
            list(GetFibonacciSequenceUseCase._calculate_fibonacci_sequence())
        self.assertEqual(
            str(e.exception),
            "_calculate_fibonacci_sequence() missing 2 required positional "
            "arguments: 'start' and 'end'")

    def test_one_argument(self):
        with self.assertRaises(TypeError) as e:
            list(GetFibonacciSequenceUseCase._calculate_fibonacci_sequence(1))
        self.assertEqual(
            str(e.exception),
            "_calculate_fibonacci_sequence() missing 1 required positional "
            "argument: 'end'")
