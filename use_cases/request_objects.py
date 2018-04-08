"""Request object classes."""
from shared.request_object import InvalidRequestObject, ValidRequestObject


class GetFibonacciSequenceRequestObject(ValidRequestObject):
    """Request object foe fibonacci sequence."""

    @staticmethod
    def _validate_params(start=None, end=None):
        invalid_request = InvalidRequestObject()
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

        return invalid_request, start, end

    def __new__(cls, start=None, end=None):
        """Replace returned object."""
        instance = super().__new__(cls)

        invalid_request, start, end = cls._validate_params(start, end)
        if invalid_request.has_errors():
            return invalid_request
        instance.start = start
        instance.end = end
        return instance
