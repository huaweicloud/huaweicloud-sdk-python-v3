# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttrsObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'capacity': 'str',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'capacity': 'capacity',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, capacity=None, name=None, value=None):
        r"""AttrsObject

        The model defined in huaweicloud sdk

        :param capacity: 缓存容量（G Byte）。
        :type capacity: str
        :param name: 额外信息名，取值范围如下： - sharding_num：该规格实例支持的分片数。 - proxy_num：该规格Proxy实例支持的Proxy节点数量。如果不是Proxy实例，该参数为0。 - db_number：该规格实例的DB数量。 - max_memory：实际可使用的最大内存。 - max_connections：该规格支持的最大连接数。 - max_clients：该规格支持的最大客户端数，一般等于最大连接数。 - max_bandwidth：该规格支持的最大带宽。 - max_in_bandwidth：该规格支持的最大接入带宽，一般等于最大带宽。 
        :type name: str
        :param value: 额外信息值。
        :type value: str
        """
        
        

        self._capacity = None
        self._name = None
        self._value = None
        self.discriminator = None

        if capacity is not None:
            self.capacity = capacity
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def capacity(self):
        r"""Gets the capacity of this AttrsObject.

        缓存容量（G Byte）。

        :return: The capacity of this AttrsObject.
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this AttrsObject.

        缓存容量（G Byte）。

        :param capacity: The capacity of this AttrsObject.
        :type capacity: str
        """
        self._capacity = capacity

    @property
    def name(self):
        r"""Gets the name of this AttrsObject.

        额外信息名，取值范围如下： - sharding_num：该规格实例支持的分片数。 - proxy_num：该规格Proxy实例支持的Proxy节点数量。如果不是Proxy实例，该参数为0。 - db_number：该规格实例的DB数量。 - max_memory：实际可使用的最大内存。 - max_connections：该规格支持的最大连接数。 - max_clients：该规格支持的最大客户端数，一般等于最大连接数。 - max_bandwidth：该规格支持的最大带宽。 - max_in_bandwidth：该规格支持的最大接入带宽，一般等于最大带宽。 

        :return: The name of this AttrsObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AttrsObject.

        额外信息名，取值范围如下： - sharding_num：该规格实例支持的分片数。 - proxy_num：该规格Proxy实例支持的Proxy节点数量。如果不是Proxy实例，该参数为0。 - db_number：该规格实例的DB数量。 - max_memory：实际可使用的最大内存。 - max_connections：该规格支持的最大连接数。 - max_clients：该规格支持的最大客户端数，一般等于最大连接数。 - max_bandwidth：该规格支持的最大带宽。 - max_in_bandwidth：该规格支持的最大接入带宽，一般等于最大带宽。 

        :param name: The name of this AttrsObject.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this AttrsObject.

        额外信息值。

        :return: The value of this AttrsObject.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this AttrsObject.

        额外信息值。

        :param value: The value of this AttrsObject.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, AttrsObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
