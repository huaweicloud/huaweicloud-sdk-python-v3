# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStructuredLogsWithTimeRangeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'list[object]'
    }

    attribute_map = {
        'result': 'result'
    }

    def __init__(self, result=None):
        """ListStructuredLogsWithTimeRangeResponse

        The model defined in huaweicloud sdk

        :param result: 查询结构化日志结果信息。 此处仅为示例，具体参数名称取决于查询的字段。
        :type result: list[object]
        """
        
        super(ListStructuredLogsWithTimeRangeResponse, self).__init__()

        self._result = None
        self.discriminator = None

        if result is not None:
            self.result = result

    @property
    def result(self):
        """Gets the result of this ListStructuredLogsWithTimeRangeResponse.

        查询结构化日志结果信息。 此处仅为示例，具体参数名称取决于查询的字段。

        :return: The result of this ListStructuredLogsWithTimeRangeResponse.
        :rtype: list[object]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ListStructuredLogsWithTimeRangeResponse.

        查询结构化日志结果信息。 此处仅为示例，具体参数名称取决于查询的字段。

        :param result: The result of this ListStructuredLogsWithTimeRangeResponse.
        :type result: list[object]
        """
        self._result = result

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
        if not isinstance(other, ListStructuredLogsWithTimeRangeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
