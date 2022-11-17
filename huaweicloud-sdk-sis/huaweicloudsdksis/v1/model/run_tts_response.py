# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunTtsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trace_id': 'str',
        'result': 'CustomResult'
    }

    attribute_map = {
        'trace_id': 'trace_id',
        'result': 'result'
    }

    def __init__(self, trace_id=None, result=None):
        """RunTtsResponse

        The model defined in huaweicloud sdk

        :param trace_id: 服务内部的令牌，可用于在日志中追溯具体流程。  在某些错误情况下可能没有此令牌字符串。
        :type trace_id: str
        :param result: 
        :type result: :class:`huaweicloudsdksis.v1.CustomResult`
        """
        
        super(RunTtsResponse, self).__init__()

        self._trace_id = None
        self._result = None
        self.discriminator = None

        if trace_id is not None:
            self.trace_id = trace_id
        if result is not None:
            self.result = result

    @property
    def trace_id(self):
        """Gets the trace_id of this RunTtsResponse.

        服务内部的令牌，可用于在日志中追溯具体流程。  在某些错误情况下可能没有此令牌字符串。

        :return: The trace_id of this RunTtsResponse.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this RunTtsResponse.

        服务内部的令牌，可用于在日志中追溯具体流程。  在某些错误情况下可能没有此令牌字符串。

        :param trace_id: The trace_id of this RunTtsResponse.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def result(self):
        """Gets the result of this RunTtsResponse.

        :return: The result of this RunTtsResponse.
        :rtype: :class:`huaweicloudsdksis.v1.CustomResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RunTtsResponse.

        :param result: The result of this RunTtsResponse.
        :type result: :class:`huaweicloudsdksis.v1.CustomResult`
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
        if not isinstance(other, RunTtsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
