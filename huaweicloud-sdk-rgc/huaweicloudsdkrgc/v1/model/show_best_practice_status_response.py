# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBestPracticeStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_id': 'str',
        'status': 'str',
        'percentage_complete': 'int',
        'error_messages': 'list[str]'
    }

    attribute_map = {
        'operation_id': 'operation_id',
        'status': 'status',
        'percentage_complete': 'percentage_complete',
        'error_messages': 'error_messages'
    }

    def __init__(self, operation_id=None, status=None, percentage_complete=None, error_messages=None):
        r"""ShowBestPracticeStatusResponse

        The model defined in huaweicloud sdk

        :param operation_id: 操作Id
        :type operation_id: str
        :param status: 状态：进行中，成功，失败
        :type status: str
        :param percentage_complete: 检测进度
        :type percentage_complete: int
        :param error_messages: 错误消息
        :type error_messages: list[str]
        """
        
        super(ShowBestPracticeStatusResponse, self).__init__()

        self._operation_id = None
        self._status = None
        self._percentage_complete = None
        self._error_messages = None
        self.discriminator = None

        if operation_id is not None:
            self.operation_id = operation_id
        if status is not None:
            self.status = status
        if percentage_complete is not None:
            self.percentage_complete = percentage_complete
        if error_messages is not None:
            self.error_messages = error_messages

    @property
    def operation_id(self):
        r"""Gets the operation_id of this ShowBestPracticeStatusResponse.

        操作Id

        :return: The operation_id of this ShowBestPracticeStatusResponse.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        r"""Sets the operation_id of this ShowBestPracticeStatusResponse.

        操作Id

        :param operation_id: The operation_id of this ShowBestPracticeStatusResponse.
        :type operation_id: str
        """
        self._operation_id = operation_id

    @property
    def status(self):
        r"""Gets the status of this ShowBestPracticeStatusResponse.

        状态：进行中，成功，失败

        :return: The status of this ShowBestPracticeStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowBestPracticeStatusResponse.

        状态：进行中，成功，失败

        :param status: The status of this ShowBestPracticeStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def percentage_complete(self):
        r"""Gets the percentage_complete of this ShowBestPracticeStatusResponse.

        检测进度

        :return: The percentage_complete of this ShowBestPracticeStatusResponse.
        :rtype: int
        """
        return self._percentage_complete

    @percentage_complete.setter
    def percentage_complete(self, percentage_complete):
        r"""Sets the percentage_complete of this ShowBestPracticeStatusResponse.

        检测进度

        :param percentage_complete: The percentage_complete of this ShowBestPracticeStatusResponse.
        :type percentage_complete: int
        """
        self._percentage_complete = percentage_complete

    @property
    def error_messages(self):
        r"""Gets the error_messages of this ShowBestPracticeStatusResponse.

        错误消息

        :return: The error_messages of this ShowBestPracticeStatusResponse.
        :rtype: list[str]
        """
        return self._error_messages

    @error_messages.setter
    def error_messages(self, error_messages):
        r"""Sets the error_messages of this ShowBestPracticeStatusResponse.

        错误消息

        :param error_messages: The error_messages of this ShowBestPracticeStatusResponse.
        :type error_messages: list[str]
        """
        self._error_messages = error_messages

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowBestPracticeStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
