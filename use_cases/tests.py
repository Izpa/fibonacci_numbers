"""Tests for all in usecases package."""
from unittest import TestCase
from unittest.mock import MagicMock

from use_cases.fibonacci_numbers import GetFibonacciSequenceRequest, \
    GetFibonacciSequenceUseCase



class RepoMock:
    """Mock repo for test."""

    def __init__(self):
        """Set numbers dict."""
        self._numbers = {str(i): None for i in range(100)}

    def numbers_list(self, start: int, end: int):
        """
        Return sequence of fibonacci numbers.

        :param start: start order of numbers sequence
        :param end: end order of numbers sequence
        :return: list of fibonacci numbers
        """
        return [self._numbers[str(i)] for i in range(start, end + 1)]

    def add_numbers(self, **numbers):
        """
        Add new numbers to repo.

        :param numbers: key - order of fibonacci number,
        value - fibonacci number
        :return:
        """
        self._numbers.update(numbers)


class GetFibonacciSequenceUseCaseTestCase(TestCase):
    """Tests for GetFibonacciSequenceUseCase class."""

    use_case_class = GetFibonacciSequenceUseCase

    def setUp(self):
        """Run before all tests."""
        repo = RepoMock()
        self.use_case = self.use_case_class(repo)

    def test_calculate_fibonacci_number_with_zero_fibonacci_number(self):
        """
        Run calculate_fibonacci_number() with 0 as order.

        Expect 0.
        """
        self.assertEqual(0, self.use_case_class._calculate_fibonacci_number(0))

    def test_calculate_fibonacci_number_with_first_fibonacci_number(self):
        """
        Run calculate_fibonacci_number() with 1 as order.

        Expect 1.
        """
        self.assertEqual(1, self.use_case_class._calculate_fibonacci_number(1))

    def test_calculate_fibonacci_number_with_second_fibonacci_number(self):
        """
        Run calculate_fibonacci_number() with 2 as order.

        Expect 1.
        """
        self.assertEqual(1, self.use_case_class._calculate_fibonacci_number(2))

    def test_calculate_fibonacci_number_with_third_fibonacci_number(self):
        """
        Run calculate_fibonacci_number() with 3 as order.

        Expect 2.
        """
        self.assertEqual(2, self.use_case_class._calculate_fibonacci_number(3))

    def test_calculate_fibonacci_number_with_hight_fibonacci_number(self):
        """
        Run calculate_fibonacci_number() with hight order.

        Expect correct fibonacci number.
        """
        self.assertEqual(
            10946, self.use_case_class._calculate_fibonacci_number(21))

    def test_calculate_fibonacci_number_with_negative_order(self):
        """
        Run calculate_fibonacci_number() with incorrect order type.

        Expect raising ValueError exception.
        """
        with self.assertRaises(ValueError) as e:
            self.use_case_class._calculate_fibonacci_number(-1)
        self.assertEqual(str(e.exception), 'order must be positive')

    def test_calculate_fibonacci_number_with_incorrect_order_type(self):
        """
        Run calculate_fibonacci_number() with incorrect order type.

        Expect raising TypeError exception.
        """
        with self.assertRaises(TypeError) as e:
            self.use_case_class._calculate_fibonacci_number('x')
        self.assertEqual(str(e.exception), 'order must be integer')

    def test_calculate_fibonacci_number_without_arguments(self):
        """
        Run calculate_fibonacci_number() without arguments.

        Expect raising TypeError exception.
        """
        with self.assertRaises(TypeError) as e:
            self.use_case_class._calculate_fibonacci_number()
        self.assertEqual(
            str(e.exception),
            '_calculate_fibonacci_number() missing 1 required positional '
            "argument: 'order'")

    def test_get_fibonacci_sequence_with_simple_sequence(self):
        """
        Run get_fibonacci_sequence() in start of fibonacci sequence.

        Expect list with fibonacci numbers sequence.
        """
        self.assertEqual(
            [0, 1, 1, 2],
            self.use_case._get_fibonacci_sequence(0, 3))

    def test_get_fibonacci_sequence_with_hight_sequence(self):
        """
        Run get_fibonacci_sequence() with hight start and end.

        Expect list with fibonacci numbers sequence.
        """
        self.assertEqual(
            [2584, 4181, 6765, 10946],
            self.use_case._get_fibonacci_sequence(18, 21))

    def test_get_fibonacci_sequence_with_incorrect_start_type(self):
        """
        Run get_fibonacci_sequence() with incorrect type of start.

        Expect raising TypeError exception.
        """
        with self.assertRaises(TypeError) as e:
            self.use_case._get_fibonacci_sequence('x', 1)
        self.assertEqual(str(e.exception), 'start must be integer')

    def test_get_fibonacci_sequence_with_incorrect_end_type(self):
        """
        Run get_fibonacci_sequence() with incorrect type of end.

        Expect raising TypeError exception.
        """
        with self.assertRaises(TypeError) as e:
            self.use_case._get_fibonacci_sequence(1, 'x')
        self.assertEqual(str(e.exception), 'end must be integer')

    def test_get_fibonacci_sequence_with_negative_start(self):
        """
        Run get_fibonacci_sequence() with negative start.

        Expect raising ValueError exception.
        """
        with self.assertRaises(ValueError) as e:
            self.use_case._get_fibonacci_sequence(-1, 1)
        self.assertEqual(str(e.exception), 'start must be positive')

    def test_get_fibonacci_sequence_with_negative_end(self):
        """
        Run get_fibonacci_sequence() with negative end.

        Expect raising ValueError exception.
        """
        with self.assertRaises(ValueError) as e:
            self.use_case._get_fibonacci_sequence(1, -1)
        self.assertEqual(str(e.exception), 'end must be positive')

    def test_get_fibonacci_sequence_with_start_greater_to_end(self):
        """
        Run get_fibonacci_sequence() with start greater to end.

        Expect raising ValueError exception.
        """
        with self.assertRaises(ValueError) as e:
            self.use_case._get_fibonacci_sequence(2, 1)
        self.assertEqual(str(e.exception), 'end must be greater than or '
                                           'equal to start')

    def test_get_fibonacci_sequence_with_empty_arguments(self):
        """
        Run get_fibonacci_sequence() without arguments.

        Expect raising TypeError exception.
        """
        with self.assertRaises(TypeError) as e:
            self.use_case._get_fibonacci_sequence()
        self.assertEqual(
            str(e.exception),
            '_get_fibonacci_sequence() missing 2 required positional '
            "arguments: 'start' and 'end'")

    def test_get_fibonacci_sequence_with_one_argument(self):
        """
        Run get_fibonacci_sequence() with one argument.

        Expect raising TypeError exception.
        """
        with self.assertRaises(TypeError) as e:
            self.use_case._get_fibonacci_sequence(1)
        self.assertEqual(
            str(e.exception),
            '_get_fibonacci_sequence() missing 1 required positional '
            "argument: 'end'")

    def test_fibonacci_sequence_add_into_repo(self):
        """
        Run _get_fibonacci_sequence with clear repo.

        Except adding calculated numbers into repo.
        """
        numbers = {str(i): None for i in range(100)}
        self.assertEqual(self.use_case.repo._numbers,
                         numbers)
        self.use_case._get_fibonacci_sequence(18, 21)
        numbers.update({
            '18': 2584,
            '19': 4181,
            '20': 6765,
            '21': 10946
        })
        self.assertEqual(self.use_case.repo._numbers,
                         numbers)

    def test_exist_fibonacci_sequence_get_from_repo_without_calculating(self):
        """
        Run _get_fibonacci_sequence with fibonacci sequence, exist in repo.

        Except response without running calculate_fibonacci_number method.
        """
        self.use_case.repo._numbers.update({
            '18': 2584,
            '19': 4181,
            '20': 6765,
            '21': 10946
        })
        self.use_case._calculate_fibonacci_number = MagicMock()
        self.use_case._get_fibonacci_sequence(18, 21)
        self.assertEqual(
            len(self.use_case._calculate_fibonacci_number.mock_calls), 0)

    def test_execute_request_handles_bad_request(self):
        """
        Execute usecase with incorrect request object.

        Expect response failure response object with error message.
        """
        request = GetFibonacciSequenceRequest()

        response = self.use_case.execute(request)

        self.assertFalse(bool(response))
        self.assertEqual(
            response.value,
            {'message': 'start: is required\nend: is required',
             'type': 'PARAMETERS_ERROR'})

    def test_execute_with_correct_request(self):
        """
        Execute usecase with correct request object.

        Expect response object with correct fibonacci sequence.
        """
        request = GetFibonacciSequenceRequest(18, 21)
        response = self.use_case.execute(request)

        self.assertTrue(bool(response))
        self.assertListEqual(response.value,
                             [2584, 4181, 6765, 10946])


class GetFibonacciSequenceRequestObjectTestCase(TestCase):
    """Tests for GetFibonacciSequenceRequest class."""

    request = GetFibonacciSequenceRequest

    def test_correct_creation(self):
        """
        Create request object with corrects.

        Expect valid request object.
        """
        request = self.request(1, 2)

        self.assertEqual(bool(request), True)
        self.assertEqual(request.start, 1)
        self.assertEqual(request.end, 2)

    def test_creation_with_incorrect_start_type(self):
        """
        Create request object with incorrect type of start.

        Expect invalid request object with error on start parameter.
        """
        request = self.request('x', 1)

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'start')
        self.assertEqual(request.errors[0]['message'],
                         'must be integer')

    def test_creation_with_incorrect_end_type(self):
        """
        Create request object with incorrect type of end.

        Expect invalid request object with error on end parameter.
        """
        request = self.request(1, 'x')

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'end')
        self.assertEqual(request.errors[0]['message'],
                         'must be integer')

    def test_creation_with_negative_start(self):
        """
        Create request object with negative start.

        Expect invalid request object with error on start parameter.
        """
        request = self.request(-1, 1)

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'start')
        self.assertEqual(request.errors[0]['message'],
                         'must be positive')

    def test_creation_with_negative_end(self):
        """
        Create request object with negative end.

        Expect invalid request object with error on end parameter.
        """
        request = self.request(1, -1)

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'end')
        self.assertEqual(request.errors[0]['message'],
                         'must be positive')

    def test_creation_with_start_greater_to_end(self):
        """
        Create request object with start greater to end.

        Expect invalid request object with error on end parameter.
        """
        request = self.request(2, 1)

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'end')
        self.assertEqual(request.errors[0]['message'],
                         'must be greater than or equal to start')

    def test_creation_with_empty_arguments(self):
        """
        Create request object without arguments.

        Expect invalid request object with error on start parameter.
        """
        request = self.request()

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'start')
        self.assertEqual(request.errors[0]['message'], 'is required')

    def test_creation_with_one_argument(self):
        """
        Create request object with one argument.

        Expect invalid request object with error on end parameter.
        """
        request = self.request(1)

        self.assertTrue(request.has_errors())
        self.assertFalse(request)
        self.assertEqual(request.errors[0]['parameter'], 'end')
        self.assertEqual(request.errors[0]['message'], 'is required')
