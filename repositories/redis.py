from collections import OrderedDict

from instance.settings import redis_client, FIBONACCI_NUMBERS_REDIS_KEY


class FibonacciNumbersRepo:
    __client = redis_client
    __key = FIBONACCI_NUMBERS_REDIS_KEY

    @staticmethod
    def _convert_response(response: list):
        int_reverse_response = map(lambda x: (int(x[1]), int(x[0])), response)
        sorted_int_reverse_response = sorted(int_reverse_response,
                                             key=lambda x: x[0])
        return OrderedDict(sorted_int_reverse_response)

    def list(self, start: int, end: int):
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

        response = self.__client.zrangebyscore(self.__key,
                                               start,
                                               end,
                                               withscores=True)
        return self._convert_response(response)

    def add_numbers(self, **numbers):
        converted_numbers = {
            str(key): int(value) for key, value in numbers.items()}
        self.__client.zadd(self.__key, **converted_numbers)
