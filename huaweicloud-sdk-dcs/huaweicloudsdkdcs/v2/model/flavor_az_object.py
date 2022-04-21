# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorAzObject:

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
        'az_codes': 'list[str]'
    }

    attribute_map = {
        'capacity': 'capacity',
        'az_codes': 'az_codes'
    }

    def __init__(self, capacity=None, az_codes=None):
        """FlavorAzObject

        The model defined in huaweicloud sdk

        :param capacity: 缓存容量（G Byte）。
        :type capacity: str
        :param az_codes: 有资源的可用区编码。
        :type az_codes: list[str]
        """
        
        

        self._capacity = None
        self._az_codes = None
        self.discriminator = None

        if capacity is not None:
            self.capacity = capacity
        if az_codes is not None:
            self.az_codes = az_codes

    @property
    def capacity(self):
        """Gets the capacity of this FlavorAzObject.

        缓存容量（G Byte）。

        :return: The capacity of this FlavorAzObject.
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this FlavorAzObject.

        缓存容量（G Byte）。

        :param capacity: The capacity of this FlavorAzObject.
        :type capacity: str
        """
        self._capacity = capacity

    @property
    def az_codes(self):
        """Gets the az_codes of this FlavorAzObject.

        有资源的可用区编码。

        :return: The az_codes of this FlavorAzObject.
        :rtype: list[str]
        """
        return self._az_codes

    @az_codes.setter
    def az_codes(self, az_codes):
        """Sets the az_codes of this FlavorAzObject.

        有资源的可用区编码。

        :param az_codes: The az_codes of this FlavorAzObject.
        :type az_codes: list[str]
        """
        self._az_codes = az_codes

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
        if not isinstance(other, FlavorAzObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
