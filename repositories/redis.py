from instance.settings import FIBONACCI_NUMBERS_REDIS_KEY, redis_client


class FibonacciNumbersRepo:
    __client = redis_client
    __key = FIBONACCI_NUMBERS_REDIS_KEY

    def numbers_list(self, start: int, end: int):
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
        return list(map(lambda x: x if x is None else int(x), response))

    def add_numbers(self, **numbers):
        if len(numbers):
            if not all(isinstance(value, int) for value in numbers.values()):
                raise TypeError('All values must be integer')
            self.__client.mset(**numbers)
