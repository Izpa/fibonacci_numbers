from unittest import TestCase

from use_cases.fibonacci_numbers import GetFibonacciSequenceUseCase


class GetFibonacciSequenceUseCaseTestCase(TestCase):
    use_case = GetFibonacciSequenceUseCase

    def test_calculate_fibonacci_number_with_zero_fibonacci_number(self):
        self.assertEqual(0, self.use_case._calculate_fibonacci_number(0))

    def test_calculate_fibonacci_number_with_first_fibonacci_number(self):
        self.assertEqual(1, self.use_case._calculate_fibonacci_number(1))

    def test_calculate_fibonacci_number_with_second_fibonacci_number(self):
        self.assertEqual(1, self.use_case._calculate_fibonacci_number(2))

    def test_calculate_fibonacci_number_with_third_fibonacci_number(self):
        self.assertEqual(2, self.use_case._calculate_fibonacci_number(3))

    def test_calculate_fibonacci_number_with_hight_fibonacci_number(self):
        self.assertEqual(10946, self.use_case._calculate_fibonacci_number(21))

    def test_calculate_fibonacci_number_with_negative_order(self):
        with self.assertRaises(ValueError) as e:
            self.use_case._calculate_fibonacci_number(-1)
        self.assertEqual(str(e.exception), 'order must be positive')

    def test_calculate_fibonacci_number_with_negative_order_type(self):
        with self.assertRaises(TypeError) as e:
            self.use_case._calculate_fibonacci_number('x')
        self.assertEqual(str(e.exception), 'order must be integer')

    def test_calculate_fibonacci_number_with_incorrect_order_type(self):
        with self.assertRaises(TypeError) as e:
            self.use_case._calculate_fibonacci_number()
        self.assertEqual(
            str(e.exception),
            "_calculate_fibonacci_number() missing 1 required positional "
            "argument: 'order'")

    def test_calculate_fibonacci_sequence_with_simple_sequence(self):
        self.assertEqual(
            [0, 1, 1, 2],
            list(self.use_case._calculate_fibonacci_sequence(0, 3)))
        
    def test_calculate_fibonacci_sequence_with_no_zero_started_sequence(self):
        self.assertEqual(
            [1, 2],
            list(self.use_case._calculate_fibonacci_sequence(2, 3)))
        
    def test_calculate_fibonacci_sequence_with_hight_sequence(self):
        self.assertEqual(
            [2584, 4181, 6765, 10946],
            list(self.use_case._calculate_fibonacci_sequence(18, 21)))
    
    def test_calculate_fibonacci_sequence_with_incorrect_start_type(self):
        with self.assertRaises(TypeError) as e:
            list(self.use_case._calculate_fibonacci_sequence('x', 1))
        self.assertEqual(str(e.exception), 'start must be integer')

    def test_calculate_fibonacci_sequence_with_incorrect_end_type(self):
        with self.assertRaises(TypeError) as e:
            list(self.use_case._calculate_fibonacci_sequence(1, 'x'))
        self.assertEqual(str(e.exception), 'end must be integer')

    def test_calculate_fibonacci_sequence_with_negative_start(self):
        with self.assertRaises(ValueError) as e:
            list(self.use_case._calculate_fibonacci_sequence(-1, 1))
        self.assertEqual(str(e.exception), 'start must be positive')

    def test_calculate_fibonacci_sequence_with_negative_end(self):
        with self.assertRaises(ValueError) as e:
            list(self.use_case._calculate_fibonacci_sequence(1, -1))
        self.assertEqual(str(e.exception), 'end must be positive')

    def test_calculate_fibonacci_sequence_with_start_greater_to_end(self):
        with self.assertRaises(ValueError) as e:
            list(self.use_case._calculate_fibonacci_sequence(2, 1))
        self.assertEqual(str(e.exception), 'end must be greater than or '
                                           'equal to start')

    def test_calculate_fibonacci_sequence_with_empty_arguments(self):
        with self.assertRaises(TypeError) as e:
            list(self.use_case._calculate_fibonacci_sequence())
        self.assertEqual(
            str(e.exception),
            "_calculate_fibonacci_sequence() missing 2 required positional "
            "arguments: 'start' and 'end'")

    def test_calculate_fibonacci_sequence_with_one_argument(self):
        with self.assertRaises(TypeError) as e:
            list(self.use_case._calculate_fibonacci_sequence(1))
        self.assertEqual(
            str(e.exception),
            "_calculate_fibonacci_sequence() missing 1 required positional "
            "argument: 'end'")
