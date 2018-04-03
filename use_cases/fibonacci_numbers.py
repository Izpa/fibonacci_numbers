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
