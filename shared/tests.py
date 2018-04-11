"""Tests for all in shared package."""
from unittest import mock, TestCase

from shared.request_object import InvalidRequestObject, ValidRequestObject
from shared.response_object import ResponseFailure, ResponseSuccess
from shared.use_case import UseCase


class RequestObjectTestCase(TestCase):
    """Tests for RequestObject class."""

    def test_invalid_request_object_is_false(self):
        """
        Create invalid request object.

        Except false object.
        """
        request = InvalidRequestObject()

        self.assertFalse(bool(request))

    def test_invalid_request_object_accepts_errors(self):
        """Add errors to exist invalid request object."""
        request = InvalidRequestObject()
        request.add_error(parameter='aparam', message='wrong value')
        request.add_error(parameter='anotherparam', message='wrong type')

        self.assertTrue(request.has_errors())
        self.assertEqual(len(request.errors), 2)

    def test_valid_request_object_is_true(self):
        """
        Create valid request object.

        Except true object.
        """
        request = ValidRequestObject()
        self.assertTrue(bool(request))


class UseCaseTestCase(TestCase):
    """Tests for UseCase class."""

    def test_cannot_process_valid_requests(self):
        """
        Execute usecase with valid request object.

        Except returning failed response object with SYSTEM_ERROR type and
        exception message (because process_request() not implemented).
        """
        valid_request_object = mock.MagicMock()
        valid_request_object.__bool__.return_value = True

        use_case = UseCase()
        response = use_case.execute(valid_request_object)

        self.assertFalse(response)
        self.assertEqual(response.type, ResponseFailure.SYSTEM_ERROR)
        self.assertEqual(
            response.message,
            'NotImplementedError: process_request() not implemented by '
            'UseCase class')

    def test_can_process_invalid_requests_and_returns_response_failure(self):
        """
        Execute usecase with invalid request object.

        Except returning failed response object with PARAMETERS_ERROR type and
        param message.
        """
        invalid_request_object = InvalidRequestObject()
        invalid_request_object.add_error('some_param', 'some_message')

        use_case = UseCase()
        response = use_case.execute(invalid_request_object)

        self.assertFalse(response)
        self.assertEqual(response.type, ResponseFailure.PARAMETERS_ERROR)
        self.assertEqual(response.message, 'some_param: some_message')

    def test_can_manage_generic_exception_from_process_request(self):
        """
        Execute usecase with raisin exception in process_request.

        Except returning failed response object with SYSTEM_ERROR type and
        exception message.
        """
        use_case = UseCase()

        class TestException(Exception):
            pass

        use_case.process_request = mock.Mock()
        use_case.process_request.side_effect = TestException('some_message')
        response = use_case.execute(mock.Mock)

        self.assertFalse(response)
        self.assertEqual(response.type, ResponseFailure.SYSTEM_ERROR)
        self.assertEqual(response.message, 'TestException: some_message')


class ResponseObjectTestCase(TestCase):
    """Tests for ResponseObject class."""

    def setUp(self):
        """
        Set response value, type and message.

        Set before each test in this case.
        """
        self.response_value = {'key': ['value1', 'value2']}
        self.response_type = 'ResponseError'
        self.response_message = 'This is a response error'

    def test_response_success_is_true(self):
        """
        Create successed response object.

        Except true object.
        """
        self.assertTrue(bool(ResponseSuccess(self.response_value)))

    def test_response_failure_is_false(self):
        """
        Create failed response object.

        Except false object.
        """
        self.assertFalse(bool(ResponseFailure(self.response_type,
                                              self.response_message)))

    def test_response_success_contains_value(self):
        """
        Create successed response object with value.

        Except successed response object with correct value.
        """
        response = ResponseSuccess(self.response_value)

        self.assertEqual(response.value, self.response_value)

    def test_response_failure_has_type_and_message(self):
        """
        Create ResponseFailure object with response type and message.

        Except failed response with response type and message with correct
        values.
        """
        response = ResponseFailure(self.response_type, self.response_message)

        self.assertEqual(response.type, self.response_type)
        self.assertEqual(response.message, self.response_message)

    def test_response_failure_contains_value(self):
        """
        Create ResponseFailure object with response type and message.

        Except failed response with response value with type and message keys
        with correct values.
        """
        response = ResponseFailure(self.response_type, self.response_message)

        self.assertEqual(response.value, {'type': self.response_type,
                                          'message': self.response_message})

    def test_response_failure_initialization_with_exception(self):
        """
        Create ResponseFailure object with response type and exception.

        Except failed response with response type and message with correct
        values.
        """
        response = ResponseFailure(self.response_type,
                                   Exception('Just an error message'))

        self.assertFalse(bool(response))
        self.assertEqual(response.type, self.response_type)
        self.assertEqual(response.message, 'Exception: Just an error message')

    def test_response_failure_from_invalid_request_object(self):
        """
        Build ResponseFailure from invalid request object.

        Except failed response object.
        """
        response = ResponseFailure.build_from_invalid_request_object(
            InvalidRequestObject())

        self.assertFalse(bool(response))

    def test_response_failure_from_invalid_request_object_with_errors(self):
        """
        Build ResponseFailure from invalid request object.

        Except failed response object with PARAMETERS_ERROR type and request
        object's errors messages.
        """
        request_object = InvalidRequestObject()
        request_object.add_error('path', 'Is mandatory')
        request_object.add_error('path', "can't be blank")

        response = ResponseFailure.build_from_invalid_request_object(
            request_object)

        self.assertFalse(bool(response))
        self.assertEqual(response.type, ResponseFailure.PARAMETERS_ERROR)
        self.assertEqual(response.message,
                         "path: Is mandatory\npath: can't be blank")

    def test_response_failure_build_resource_error(self):
        """
        Build ResponseFailure with resource error and with message.

        Except failed response object with RESOURCE_ERROR type and message.
        """
        response = ResponseFailure.build_resource_error('test message')

        self.assertFalse(bool(response))
        self.assertEqual(response.type, ResponseFailure.RESOURCE_ERROR)
        self.assertEqual(response.message, 'test message')

    def test_response_failure_build_parameters_error(self):
        """
        Build ResponseFailure with parameters error and with message.

        Except failed response object with PARAMETERS_ERROR type and message.
        """
        response = ResponseFailure.build_parameters_error('test message')

        self.assertFalse(bool(response))
        self.assertEqual(response.type, ResponseFailure.PARAMETERS_ERROR)
        self.assertEqual(response.message, 'test message')

    def test_response_failure_build_system_error(self):
        """
        Build ResponseFailure with system error and with message.

        Except failed response object with SYSTEM_ERROR type and message.
        """
        response = ResponseFailure.build_system_error('test message')

        self.assertFalse(bool(response))
        self.assertEqual(response.type, ResponseFailure.SYSTEM_ERROR)
        self.assertEqual(response.message, 'test message')
