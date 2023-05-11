# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'summary': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'summary': 'summary',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, summary=None, error_code=None, error_msg=None):
        """RunSummaryResponse

        The model defined in huaweicloud sdk

        :param summary: 根据文本请求体，返回摘要结果。调用失败时无此字段。
        :type summary: str
        :param error_code: 调用失败时的错误码，具体请参见错误码。调用成功时无此字段。
        :type error_code: str
        :param error_msg: 调用失败时的错误信息。调用成功时无此字段。
        :type error_msg: str
        """
        
        super(RunSummaryResponse, self).__init__()

        self._summary = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if summary is not None:
            self.summary = summary
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def summary(self):
        """Gets the summary of this RunSummaryResponse.

        根据文本请求体，返回摘要结果。调用失败时无此字段。

        :return: The summary of this RunSummaryResponse.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this RunSummaryResponse.

        根据文本请求体，返回摘要结果。调用失败时无此字段。

        :param summary: The summary of this RunSummaryResponse.
        :type summary: str
        """
        self._summary = summary

    @property
    def error_code(self):
        """Gets the error_code of this RunSummaryResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :return: The error_code of this RunSummaryResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this RunSummaryResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :param error_code: The error_code of this RunSummaryResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this RunSummaryResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :return: The error_msg of this RunSummaryResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this RunSummaryResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :param error_msg: The error_msg of this RunSummaryResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, RunSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
