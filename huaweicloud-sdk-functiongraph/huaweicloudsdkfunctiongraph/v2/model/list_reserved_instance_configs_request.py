# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReservedInstanceConfigsRequest:

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
        r"""ListReservedInstanceConfigsRequest

        The model defined in huaweicloud sdk

        :param function_urn: 函数的URN，详细解释见FunctionGraph函数模型的描述。
        :type function_urn: str
        :param marker: 本次查询起始位置，默认值0
        :type marker: str
        :param limit: 本次查询最大返回的数据条数，最大值500，默认值100
        :type limit: str
        """
        
        

        self._function_urn = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        if function_urn is not None:
            self.function_urn = function_urn
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def function_urn(self):
        r"""Gets the function_urn of this ListReservedInstanceConfigsRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :return: The function_urn of this ListReservedInstanceConfigsRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        r"""Sets the function_urn of this ListReservedInstanceConfigsRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :param function_urn: The function_urn of this ListReservedInstanceConfigsRequest.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def marker(self):
        r"""Gets the marker of this ListReservedInstanceConfigsRequest.

        本次查询起始位置，默认值0

        :return: The marker of this ListReservedInstanceConfigsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListReservedInstanceConfigsRequest.

        本次查询起始位置，默认值0

        :param marker: The marker of this ListReservedInstanceConfigsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListReservedInstanceConfigsRequest.

        本次查询最大返回的数据条数，最大值500，默认值100

        :return: The limit of this ListReservedInstanceConfigsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListReservedInstanceConfigsRequest.

        本次查询最大返回的数据条数，最大值500，默认值100

        :param limit: The limit of this ListReservedInstanceConfigsRequest.
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
        if not isinstance(other, ListReservedInstanceConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
