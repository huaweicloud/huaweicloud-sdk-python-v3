# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetPropertyLastValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'property_name': 'str',
        'value': 'object',
        'timestamp': 'str'
    }

    attribute_map = {
        'property_name': 'property_name',
        'value': 'value',
        'timestamp': 'timestamp'
    }

    def __init__(self, property_name=None, value=None, timestamp=None):
        r"""AssetPropertyLastValue

        The model defined in huaweicloud sdk

        :param property_name: 资产属性名称
        :type property_name: str
        :param value: 资产属性值
        :type value: object
        :param timestamp: 资产属性值最后更新时间
        :type timestamp: str
        """
        
        

        self._property_name = None
        self._value = None
        self._timestamp = None
        self.discriminator = None

        if property_name is not None:
            self.property_name = property_name
        if value is not None:
            self.value = value
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def property_name(self):
        r"""Gets the property_name of this AssetPropertyLastValue.

        资产属性名称

        :return: The property_name of this AssetPropertyLastValue.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        r"""Sets the property_name of this AssetPropertyLastValue.

        资产属性名称

        :param property_name: The property_name of this AssetPropertyLastValue.
        :type property_name: str
        """
        self._property_name = property_name

    @property
    def value(self):
        r"""Gets the value of this AssetPropertyLastValue.

        资产属性值

        :return: The value of this AssetPropertyLastValue.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this AssetPropertyLastValue.

        资产属性值

        :param value: The value of this AssetPropertyLastValue.
        :type value: object
        """
        self._value = value

    @property
    def timestamp(self):
        r"""Gets the timestamp of this AssetPropertyLastValue.

        资产属性值最后更新时间

        :return: The timestamp of this AssetPropertyLastValue.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this AssetPropertyLastValue.

        资产属性值最后更新时间

        :param timestamp: The timestamp of this AssetPropertyLastValue.
        :type timestamp: str
        """
        self._timestamp = timestamp

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
        if not isinstance(other, AssetPropertyLastValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
