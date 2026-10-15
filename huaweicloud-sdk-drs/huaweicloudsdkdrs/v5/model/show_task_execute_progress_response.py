# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskExecuteProgressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'progress': 'str',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'status': 'status',
        'progress': 'progress',
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, status=None, progress=None, error_code=None, error_message=None):
        r"""ShowTaskExecuteProgressResponse

        The model defined in huaweicloud sdk

        :param status: 任务状态。
        :type status: str
        :param progress: 任务执行进度。
        :type progress: str
        :param error_code: 错误码。
        :type error_code: str
        :param error_message: 错误信息。
        :type error_message: str
        """
        
        super().__init__()

        self._status = None
        self._progress = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def status(self):
        r"""Gets the status of this ShowTaskExecuteProgressResponse.

        任务状态。

        :return: The status of this ShowTaskExecuteProgressResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTaskExecuteProgressResponse.

        任务状态。

        :param status: The status of this ShowTaskExecuteProgressResponse.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        r"""Gets the progress of this ShowTaskExecuteProgressResponse.

        任务执行进度。

        :return: The progress of this ShowTaskExecuteProgressResponse.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this ShowTaskExecuteProgressResponse.

        任务执行进度。

        :param progress: The progress of this ShowTaskExecuteProgressResponse.
        :type progress: str
        """
        self._progress = progress

    @property
    def error_code(self):
        r"""Gets the error_code of this ShowTaskExecuteProgressResponse.

        错误码。

        :return: The error_code of this ShowTaskExecuteProgressResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ShowTaskExecuteProgressResponse.

        错误码。

        :param error_code: The error_code of this ShowTaskExecuteProgressResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this ShowTaskExecuteProgressResponse.

        错误信息。

        :return: The error_message of this ShowTaskExecuteProgressResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ShowTaskExecuteProgressResponse.

        错误信息。

        :param error_message: The error_message of this ShowTaskExecuteProgressResponse.
        :type error_message: str
        """
        self._error_message = error_message

    def to_dict(self):
        import warnings
        warnings.warn("ShowTaskExecuteProgressResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowTaskExecuteProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
