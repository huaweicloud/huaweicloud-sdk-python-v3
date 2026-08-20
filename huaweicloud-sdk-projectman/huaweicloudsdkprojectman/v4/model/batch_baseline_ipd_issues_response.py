# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchBaselineIpdIssuesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'list[BatchBaselineIssueResponseResult]',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'result': 'result',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, result=None, status=None, message=None):
        r"""BatchBaselineIpdIssuesResponse

        The model defined in huaweicloud sdk

        :param result: 批量基线工作项的结果列表。
        :type result: list[:class:`huaweicloudsdkprojectman.v4.BatchBaselineIssueResponseResult`]
        :param status: 返回状态。
        :type status: str
        :param message: 操作失败原因。
        :type message: str
        """
        
        super().__init__()

        self._result = None
        self._status = None
        self._message = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def result(self):
        r"""Gets the result of this BatchBaselineIpdIssuesResponse.

        批量基线工作项的结果列表。

        :return: The result of this BatchBaselineIpdIssuesResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.BatchBaselineIssueResponseResult`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this BatchBaselineIpdIssuesResponse.

        批量基线工作项的结果列表。

        :param result: The result of this BatchBaselineIpdIssuesResponse.
        :type result: list[:class:`huaweicloudsdkprojectman.v4.BatchBaselineIssueResponseResult`]
        """
        self._result = result

    @property
    def status(self):
        r"""Gets the status of this BatchBaselineIpdIssuesResponse.

        返回状态。

        :return: The status of this BatchBaselineIpdIssuesResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchBaselineIpdIssuesResponse.

        返回状态。

        :param status: The status of this BatchBaselineIpdIssuesResponse.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this BatchBaselineIpdIssuesResponse.

        操作失败原因。

        :return: The message of this BatchBaselineIpdIssuesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this BatchBaselineIpdIssuesResponse.

        操作失败原因。

        :param message: The message of this BatchBaselineIpdIssuesResponse.
        :type message: str
        """
        self._message = message

    def to_dict(self):
        import warnings
        warnings.warn("BatchBaselineIpdIssuesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchBaselineIpdIssuesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
