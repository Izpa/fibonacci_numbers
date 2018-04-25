"""Redis repository for application."""
from instance.settings import FIBONACCI_NUMBERS_REDIS_KEY, redis_client


class FibonacciNumbersRepo:
    """
    Redis repo for fibonacci numbers.

    Key - order number of fibonacci number.
    Value - fibonacci number.
    """

    __client = redis_client
    __key = FIBONACCI_NUMBERS_REDIS_KEY

    def numbers_list(self, start: int, end: int):
        """
        Get list of fibonacci sequence from redis.

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

        response = self.__client.mget(range(start, end+1))
        return [i if i is None else int(i) for i in response]

    def add_numbers(self, **numbers):
        """
        Add fibonacci numbers to redis.

        :param numbers: dict of fibonacci numbers
        :return:
        """
        if len(numbers):
            if not all(isinstance(value, int) for value in numbers.values()):
                raise TypeError('All values must be integer')
            self.__client.mset(**numbers)
