from unittest import TestCase

from use_cases.fibonacci_numbers import calculate_fibonacci_number_by_order, \
    calculate_fibonacci_sequence


class DefaultTestCase(TestCase):
    def test_calculate_fibonacci_number_by_order(self):
        # Zero fibonacci number
        self.assertEqual(0, calculate_fibonacci_number_by_order(0))

        # First fibonacci number
        self.assertEqual(1, calculate_fibonacci_number_by_order(1))

        # Second fibonacci number
        self.assertEqual(1, calculate_fibonacci_number_by_order(2))

        # Third fibonacci number
        self.assertEqual(2, calculate_fibonacci_number_by_order(3))

        # 21th fibonacci number
        self.assertEqual(10946, calculate_fibonacci_number_by_order(21))

        # Negative order
        with self.assertRaises(ValueError) as e:
            calculate_fibonacci_number_by_order(-1)
        self.assertEqual(str(e.exception), 'order must be positive')

        # Incorrect order type
        with self.assertRaises(TypeError) as e:
            calculate_fibonacci_number_by_order('x')
        self.assertEqual(str(e.exception), 'order must be integer')

        # Empty order
        with self.assertRaises(TypeError) as e:
            calculate_fibonacci_number_by_order()
        self.assertEqual(str(e.exception),
                         "calculate_fibonacci_number_by_order() missing 1 "
                         "required positional argument: 'order'")

    def test_calculate_fibonacci_sequence(self):
        # Fibonacci sequence from 0 to 0
        self.assertEqual([0], list(calculate_fibonacci_sequence(0, 0)))
        # Fibonacci sequence from 0 to 1
        self.assertEqual([0, 1], list(calculate_fibonacci_sequence(0, 1)))
        # Fibonacci sequence from 0 to 2
        self.assertEqual([0, 1, 1], list(calculate_fibonacci_sequence(0, 2)))
        # Fibonacci sequence from 0 to 3
        self.assertEqual([0, 1, 1, 2],
                         list(calculate_fibonacci_sequence(0, 3)))
        # Fibonacci sequence from 2 to 3
        self.assertEqual([1, 2], list(calculate_fibonacci_sequence(2, 3)))
        # Fibonacci sequence from 18 to 21
        self.assertEqual([2584, 4181, 6765, 10946],
                         list(calculate_fibonacci_sequence(18, 21)))
        # Incorrect start type
        with self.assertRaises(TypeError) as e:
            list(calculate_fibonacci_sequence('x', 1))
        self.assertEqual(str(e.exception), 'start must be integer')
        # Incorrect end type
        with self.assertRaises(TypeError) as e:
            list(calculate_fibonacci_sequence(1, 'x'))
        self.assertEqual(str(e.exception), 'end must be integer')
        # Negative start
        with self.assertRaises(ValueError) as e:
            list(calculate_fibonacci_sequence(-1, 1))
        self.assertEqual(str(e.exception), 'start must be positive')
        # Negative end
        with self.assertRaises(ValueError) as e:
            list(calculate_fibonacci_sequence(1, -1))
        self.assertEqual(str(e.exception), 'end must be positive')
        # Start greater than or equal to end
        with self.assertRaises(ValueError) as e:
            list(calculate_fibonacci_sequence(2, 1))
        self.assertEqual(str(e.exception), 'end must be greater than or '
                                           'equal to start')
        # Empty arguments
        with self.assertRaises(TypeError) as e:
            list(calculate_fibonacci_sequence())
        self.assertEqual(str(e.exception), "calculate_fibonacci_sequence() "
                                           "missing 2 required positional "
                                           "arguments: 'start' and 'end'")
        # One argument
        with self.assertRaises(TypeError) as e:
            list(calculate_fibonacci_sequence(1))
        self.assertEqual(str(e.exception), "calculate_fibonacci_sequence() "
                                           "missing 1 required positional "
                                           "argument: 'end'")
