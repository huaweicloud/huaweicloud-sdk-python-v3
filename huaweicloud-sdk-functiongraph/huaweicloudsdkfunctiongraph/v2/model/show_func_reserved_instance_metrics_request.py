# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFuncReservedInstanceMetricsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'str',
        'func_urn': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'func_urn': 'func_urn'
    }

    def __init__(self, marker=None, limit=None, func_urn=None):
        """ShowFuncReservedInstanceMetricsRequest

        The model defined in huaweicloud sdk

        :param marker: 本次查询起始位置，默认值0
        :type marker: str
        :param limit: 本次查询最大返回的数据条数，最大值500，默认值100
        :type limit: str
        :param func_urn: 函数的URN，详细解释见FunctionGraph函数模型的描述。
        :type func_urn: str
        """
        
        

        self._marker = None
        self._limit = None
        self._func_urn = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        self.func_urn = func_urn

    @property
    def marker(self):
        """Gets the marker of this ShowFuncReservedInstanceMetricsRequest.

        本次查询起始位置，默认值0

        :return: The marker of this ShowFuncReservedInstanceMetricsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ShowFuncReservedInstanceMetricsRequest.

        本次查询起始位置，默认值0

        :param marker: The marker of this ShowFuncReservedInstanceMetricsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ShowFuncReservedInstanceMetricsRequest.

        本次查询最大返回的数据条数，最大值500，默认值100

        :return: The limit of this ShowFuncReservedInstanceMetricsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowFuncReservedInstanceMetricsRequest.

        本次查询最大返回的数据条数，最大值500，默认值100

        :param limit: The limit of this ShowFuncReservedInstanceMetricsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def func_urn(self):
        """Gets the func_urn of this ShowFuncReservedInstanceMetricsRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :return: The func_urn of this ShowFuncReservedInstanceMetricsRequest.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        """Sets the func_urn of this ShowFuncReservedInstanceMetricsRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :param func_urn: The func_urn of this ShowFuncReservedInstanceMetricsRequest.
        :type func_urn: str
        """
        self._func_urn = func_urn

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
        if not isinstance(other, ShowFuncReservedInstanceMetricsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
