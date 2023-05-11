# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionAsyncInvokeConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'marker': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, function_urn=None, marker=None, limit=None):
        """ListFunctionAsyncInvokeConfigRequest

        The model defined in huaweicloud sdk

        :param function_urn: 函数的URN（Uniform Resource Name），唯一标识函数。
        :type function_urn: str
        :param marker: 上一次查询到的最后的记录位置。
        :type marker: str
        :param limit: 每页显示的条目数量。 - 如果不提供该值或者提供的值等于0，则使用默认值：10，最大值100，大于100取值100。 - 如果该值小于0，则返回参数错误。
        :type limit: str
        """
        
        

        self._function_urn = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.function_urn = function_urn
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def function_urn(self):
        """Gets the function_urn of this ListFunctionAsyncInvokeConfigRequest.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :return: The function_urn of this ListFunctionAsyncInvokeConfigRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this ListFunctionAsyncInvokeConfigRequest.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :param function_urn: The function_urn of this ListFunctionAsyncInvokeConfigRequest.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def marker(self):
        """Gets the marker of this ListFunctionAsyncInvokeConfigRequest.

        上一次查询到的最后的记录位置。

        :return: The marker of this ListFunctionAsyncInvokeConfigRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListFunctionAsyncInvokeConfigRequest.

        上一次查询到的最后的记录位置。

        :param marker: The marker of this ListFunctionAsyncInvokeConfigRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListFunctionAsyncInvokeConfigRequest.

        每页显示的条目数量。 - 如果不提供该值或者提供的值等于0，则使用默认值：10，最大值100，大于100取值100。 - 如果该值小于0，则返回参数错误。

        :return: The limit of this ListFunctionAsyncInvokeConfigRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFunctionAsyncInvokeConfigRequest.

        每页显示的条目数量。 - 如果不提供该值或者提供的值等于0，则使用默认值：10，最大值100，大于100取值100。 - 如果该值小于0，则返回参数错误。

        :param limit: The limit of this ListFunctionAsyncInvokeConfigRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListFunctionAsyncInvokeConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
