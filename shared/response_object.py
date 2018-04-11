"""Response objects."""


class ResponseSuccess(object):
    """Class for successed responses."""

    SUCCESS = 'SUCCESS'

    def __init__(self, value=None):
        """Set type and value."""
        self.type = self.SUCCESS
        self.value = value

    def __nonzero__(self):
        """Nonzero for bool."""
        return True

    __bool__ = __nonzero__


class ResponseFailure(object):
    """Class for failed responses."""

    RESOURCE_ERROR = 'RESOURCE_ERROR'
    PARAMETERS_ERROR = 'PARAMETERS_ERROR'
    SYSTEM_ERROR = 'SYSTEM_ERROR'

    def __init__(self, type_, message):
        """
        Set type and message.

        :param type_: error type.
        :param message: error message.
        """
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return '{}: {}'.format(msg.__class__.__name__, '{}'.format(msg))
        return msg

    @property
    def value(self):
        return {'type': self.type, 'message': self.message}

    def __bool__(self):
        """Bool."""
        return False

    @classmethod
    def build_resource_error(cls, message=None):
        return cls(cls.RESOURCE_ERROR, message)

    @classmethod
    def build_system_error(cls, message=None):
        return cls(cls.SYSTEM_ERROR, message)

    @classmethod
    def build_parameters_error(cls, message=None):
        return cls(cls.PARAMETERS_ERROR, message)

    @classmethod
    def build_from_invalid_request_object(cls, invalid_request_object):
        message = '\n'.join(['{}: {}'.format(err['parameter'], err['message'])
                             for err in invalid_request_object.errors])
        return cls.build_parameters_error(message)
