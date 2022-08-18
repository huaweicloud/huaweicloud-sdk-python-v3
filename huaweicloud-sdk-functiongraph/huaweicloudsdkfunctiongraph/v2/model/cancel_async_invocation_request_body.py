# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelAsyncInvocationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'type': 'type'
    }

    def __init__(self, request_id=None, type=None):
        """CancelAsyncInvocationRequestBody

        The model defined in huaweicloud sdk

        :param request_id: 被停止的请求id
        :type request_id: str
        :param type: 停止的类型 支持recursive, force。 recursive: 停止正在调用的子函数。 force: 直接杀死runtime。
        :type type: str
        """
        
        

        self._request_id = None
        self._type = None
        self.discriminator = None

        self.request_id = request_id
        if type is not None:
            self.type = type

    @property
    def request_id(self):
        """Gets the request_id of this CancelAsyncInvocationRequestBody.

        被停止的请求id

        :return: The request_id of this CancelAsyncInvocationRequestBody.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CancelAsyncInvocationRequestBody.

        被停止的请求id

        :param request_id: The request_id of this CancelAsyncInvocationRequestBody.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def type(self):
        """Gets the type of this CancelAsyncInvocationRequestBody.

        停止的类型 支持recursive, force。 recursive: 停止正在调用的子函数。 force: 直接杀死runtime。

        :return: The type of this CancelAsyncInvocationRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CancelAsyncInvocationRequestBody.

        停止的类型 支持recursive, force。 recursive: 停止正在调用的子函数。 force: 直接杀死runtime。

        :param type: The type of this CancelAsyncInvocationRequestBody.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, CancelAsyncInvocationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
