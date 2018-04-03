from unittest import TestCase

from use_cases.fibonacci_numbers import calculate_fibonacci_number_by_order


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
