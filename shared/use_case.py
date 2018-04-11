"""Module for abstract use case class."""
from shared.response_object import ResponseFailure


class UseCase(object):
    """
    Abstract class for business logic of application.

    Layer between domain and repo.
    """

    def execute(self, request_object):
        """
        Run use case.

        :param request_object:
        :return: ResponseFailure or ResponseSuccess object
        """
        if not request_object:
            return ResponseFailure.build_from_invalid_request_object(
                request_object)
        try:
            return self.process_request(request_object)
        except Exception as exc:
            return ResponseFailure.build_system_error(
                '{}: {}'.format(exc.__class__.__name__, '{}'.format(exc)))

    def process_request(self, request_object):
        """Abstract method, must return ResponseSuccess object."""
        raise NotImplementedError(
            'process_request() not implemented by UseCase class')
