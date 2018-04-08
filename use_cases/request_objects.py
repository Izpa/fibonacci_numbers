"""Request object classes."""
from shared.request_object import InvalidRequestObject, ValidRequestObject


class GetFibonacciSequenceRequestObject(ValidRequestObject):
    """Request object foe fibonacci sequence."""

    def __new__(cls, start=None, end=None):
        """Replace returned object."""
        invalid_request = InvalidRequestObject()
        instance = super().__new__(cls)

        if start is None:
            invalid_request.add_error('start', 'is required')
        else:
            try:
                start = int(start)
                if start < 0:
                    invalid_request.add_error('start', 'must be positive')
            except ValueError:
                invalid_request.add_error('start', 'must be integer')
        if end is None:
            invalid_request.add_error('end', 'is required')
        else:
            try:
                end = int(end)
                if end < 0:
                    invalid_request.add_error('end', 'must be positive')
            except ValueError:
                invalid_request.add_error('end', 'must be integer')
        if not invalid_request.has_errors() and end < start:
            invalid_request.add_error('end',
                                      'must be greater than or equal to start')

        if invalid_request.has_errors():
            return invalid_request

        instance.start = start
        instance.end = end
        return instance
