"""Fibonacci number usecase, request and response classes."""


class UseCase:
    """
    Abstract class for business logic of application.

    Layer between domain and repo.
    """

    def execute(self, request):
        """
        Run usecase.

        :param request:
        :return: ResponseFailure or ResponseSuccess object
        """
        if not request:
            return ResponseFailure.build_from_invalid_request(
                request)
        try:
            return self.process_request(request)
        except Exception as exc:
            return ResponseFailure.build_system_error(
                '{}: {}'.format(exc.__class__.__name__, '{}'.format(exc)))

    def process_request(self, request):
        """Abstract method, must return ResponseSuccess object."""
        raise NotImplementedError(
            'process_request() not implemented by UseCase class')


class Request:
    """Request for usecase."""

    def __init__(self):
        """Set errors list."""
        self.errors = []

    def add_error(self, parameter, message):
        """
        Add error to errors list.

        :param parameter: error parameter.
        :param message: error message.
        :return:
        """
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self):
        """
        Check errors list.

        :return: bool
        """
        return len(self.errors) > 0

    def __bool__(self):
        """For quick error check."""
        return not self.has_errors()


class ResponseSuccess:
    """Class for successed responses from usecase."""

    SUCCESS = 'SUCCESS'

    def __init__(self, value=None):
        """Set type and value."""
        self.type = self.SUCCESS
        self.value = value

    def __bool__(self):
        """For quick error check."""
        return True


class ResponseFailure:
    """Class for failed responses from usecase."""

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
        """
        Convert type and message to dict.

        :return:
        """
        return {'type': self.type, 'message': self.message}

    def __bool__(self):
        """For quick error check."""
        return False

    @classmethod
    def build_resource_error(cls, message=None):
        """
        Create failed response object with RESOURCE_ERROR type.

        :param message:
        :return:
        """
        return cls(cls.RESOURCE_ERROR, message)

    @classmethod
    def build_system_error(cls, message=None):
        """
        Create failed response object with SYSTEM_ERROR type.

        :param message:
        :return:
        """
        return cls(cls.SYSTEM_ERROR, message)

    @classmethod
    def build_parameters_error(cls, message=None):
        """
        Create failed response object with PARAMETERS_ERROR type.

        :param message:
        :return:
        """
        return cls(cls.PARAMETERS_ERROR, message)

    @classmethod
    def build_from_invalid_request(cls, invalid_request):
        """
        Create failed response object with invalid_request message.

        :param invalid_request:
        :return:
        """
        message = '\n'.join(['{}: {}'.format(err['parameter'], err['message'])
                             for err in invalid_request.errors])
        return cls.build_parameters_error(message)
