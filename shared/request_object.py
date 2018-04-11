"""Request objects."""


class InvalidRequestObject(object):
    """Class for invalid requests."""

    def __init__(self):
        """Set errors list."""
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self):
        return len(self.errors) > 0

    def __nonzero__(self):
        """Nonzero for bool."""
        return False

    __bool__ = __nonzero__


class ValidRequestObject(object):
    """Class for valid requests."""

    def __nonzero__(self):
        """Nonzero for bool."""
        return True

    __bool__ = __nonzero__
