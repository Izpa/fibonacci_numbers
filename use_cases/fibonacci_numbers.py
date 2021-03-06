"""Module for fibonacci sequence usecase class."""
from math import sqrt

from shared.use_case import Request, ResponseSuccess, UseCase


class GetFibonacciSequenceUseCase(UseCase):
    """Usecase class."""

    def __init__(self, repo):
        """Set repo."""
        self.repo = repo

    def process_request(self, request):
        """
        Need for usecase implementation.

        :param request: request object witn start and end orders numbers
        of requested fibonacci sequence.
        :return: response success object
        """
        start = request.start
        end = request.end
        numbers = self._get_fibonacci_sequence(start, end)
        return ResponseSuccess(numbers)

    @staticmethod
    def _calculate_fibonacci_number(order: int):
        """
        Calculate fibonacci number by order number.

        Use Binet's formula.

        :param order: order number of fibonacci number
        :return: fibonacci number
        """
        if not isinstance(order, int):
            raise TypeError('order must be integer')
        if order < 0:
            raise ValueError('order must be positive')

        # Binet's formula
        sqrt_five = sqrt(5)
        left = (1 + sqrt_five) / 2
        right = (1 - sqrt_five) / 2

        return round((pow(left, order) - pow(right, order)) / sqrt_five)

    def _get_fibonacci_sequence(self, start: int, end: int):
        """
        Get fibonacci sequence from repo or calculate.

        If number of requested sequence doesn't exist in repo, it calculate
        by previous numbers in sequence. If first two numbers of requested
        sequence don't exist, they calculate by _calculate_fibonacci_number.

        :param start: start order number of fibonacci sequence
        :param end: end order number of fibonacci sequence
        :return: list with fibonacci sequence
        """
        if not isinstance(start, int):
            raise TypeError('start must be integer')
        if not isinstance(end, int):
            raise TypeError('end must be integer')
        if start < 0:
            raise ValueError('start must be positive')
        if end < 0:
            raise ValueError('end must be positive')
        if end < start:
            raise ValueError('end must be greater than or equal to start')

        numbers = self.repo.numbers_list(start, end)
        numbers_for_save = {}

        none_indices = (
            index for index, number in enumerate(numbers) if number is None)
        for index in none_indices:
            if index < 2:
                numbers[index] = self._calculate_fibonacci_number(start+index)
            else:
                numbers[index] = numbers[index-1] + numbers[index-2]
            numbers_for_save[str(start+index)] = numbers[index]

        self.repo.add_numbers(**numbers_for_save)

        return numbers


class GetFibonacciSequenceRequest(Request):
    """Request object foe fibonacci sequence."""

    def __init__(self, start=None, end=None):
        """Check and set params and errors."""
        super().__init__()
        if start is None:
            self.add_error('start', 'is required')
        else:
            try:
                start = int(start)
                if start < 0:
                    self.add_error('start', 'must be positive')
            except ValueError:
                self.add_error('start', 'must be integer')
        if end is None:
            self.add_error('end', 'is required')
        else:
            try:
                end = int(end)
                if end < 0:
                    self.add_error('end', 'must be positive')
            except ValueError:
                self.add_error('end', 'must be integer')
        if not self.has_errors() and end < start:
            self.add_error('end', 'must be greater than or equal to start')

        self.start = start
        self.end = end
