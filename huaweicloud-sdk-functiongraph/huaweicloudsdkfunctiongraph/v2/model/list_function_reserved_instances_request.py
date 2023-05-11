# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionReservedInstancesRequest:

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
        'urn': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'urn': 'urn'
    }

    def __init__(self, marker=None, limit=None, urn=None):
        """ListFunctionReservedInstancesRequest

        The model defined in huaweicloud sdk

        :param marker: 上一次查询到的最后的记录位置。
        :type marker: str
        :param limit: 每次查询获取的最大函数记录数量  最大值：400 如果不提供该值或者提供的值大于400或等于0，则使用默认值：400 如果该值小于0，则返回参数错误。
        :type limit: str
        :param urn: 查询指定函数版本预留实例数的函数urn。
        :type urn: str
        """
        
        

        self._marker = None
        self._limit = None
        self._urn = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if urn is not None:
            self.urn = urn

    @property
    def marker(self):
        """Gets the marker of this ListFunctionReservedInstancesRequest.

        上一次查询到的最后的记录位置。

        :return: The marker of this ListFunctionReservedInstancesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListFunctionReservedInstancesRequest.

        上一次查询到的最后的记录位置。

        :param marker: The marker of this ListFunctionReservedInstancesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListFunctionReservedInstancesRequest.

        每次查询获取的最大函数记录数量  最大值：400 如果不提供该值或者提供的值大于400或等于0，则使用默认值：400 如果该值小于0，则返回参数错误。

        :return: The limit of this ListFunctionReservedInstancesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFunctionReservedInstancesRequest.

        每次查询获取的最大函数记录数量  最大值：400 如果不提供该值或者提供的值大于400或等于0，则使用默认值：400 如果该值小于0，则返回参数错误。

        :param limit: The limit of this ListFunctionReservedInstancesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def urn(self):
        """Gets the urn of this ListFunctionReservedInstancesRequest.

        查询指定函数版本预留实例数的函数urn。

        :return: The urn of this ListFunctionReservedInstancesRequest.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this ListFunctionReservedInstancesRequest.

        查询指定函数版本预留实例数的函数urn。

        :param urn: The urn of this ListFunctionReservedInstancesRequest.
        :type urn: str
        """
        self._urn = urn

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
        if not isinstance(other, ListFunctionReservedInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
