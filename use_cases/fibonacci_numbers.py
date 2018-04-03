from math import sqrt


def calculate_fibonacci_number_by_order(order: int):
    if not isinstance(order, int):
        raise TypeError('order must be integer')
    if order < 0:
        raise ValueError('order must be positive')

    # Binet's formula
    sqrt_five = sqrt(5)
    left = (1 + sqrt_five) / 2
    right = (1 - sqrt_five) / 2

    return round((pow(left, order) - pow(right, order)) / sqrt_five)


def calculate_fibonacci_sequence(start: int, end: int):
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

    first = calculate_fibonacci_number_by_order(start)
    second = calculate_fibonacci_number_by_order(start+1)
    for i in range(end+1-start):
        yield first
        first, second = second, first + second
