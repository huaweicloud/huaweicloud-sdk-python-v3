import json

from huaweicloudsdkcore.exceptions.exceptions import SdkError, ServerResponseException, ClientRequestException
from huaweicloudsdkcore.exceptions.exception_handler import ExceptionHandler


class CceExceptionHandler(ExceptionHandler):
    def handle_exception(self, request, response):
        if response.status_code < 400:
            return

        sdk_error = SdkError(request_id=response.headers.get("X-Request-Id"))

        data = json.loads(response.content)
        sdk_error.error_code = data.get("error_code")
        sdk_error.error_msg = data.get("error_msg", "")
        message = data.get("message")
        if message and sdk_error.error_msg != message:
            sdk_error.error_msg += ", " + message

        raise ClientRequestException(response.status_code, sdk_error) if response.status_code < 500 \
            else ServerResponseException(response.status_code, sdk_error)
