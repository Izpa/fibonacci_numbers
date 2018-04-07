"""Request object classes."""
from shared.request_object import InvalidRequestObject, ValidRequestObject


class GetFibonacciSequenceRequestObject(ValidRequestObject):
    """Request object foe fibonacci sequence."""

    def __new__(cls, start: int = None, end: int = None):
        """Replace returned object."""
        invalid_request = InvalidRequestObject()
        instance = super().__new__(cls)

        if start is None:
            invalid_request.add_error('start', 'is required')
        elif not isinstance(start, int):
            invalid_request.add_error('start', 'must be integer')
        elif start < 0:
            invalid_request.add_error('start', 'must be positive')
        if end is None:
            invalid_request.add_error('end', 'is required')
        if not isinstance(end, int):
            invalid_request.add_error('end', 'must be integer')
        elif end < 0:
            invalid_request.add_error('end', 'must be positive')
        if not invalid_request.has_errors() and end < start:
            invalid_request.add_error('end',
                                      'must be greater than or equal to start')

        if invalid_request.has_errors():
            return invalid_request

        instance.start = start
        instance.end = end
        return instance
