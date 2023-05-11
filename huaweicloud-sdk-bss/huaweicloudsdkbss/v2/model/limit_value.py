# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LimitValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value1': 'str',
        'value2': 'str'
    }

    attribute_map = {
        'value1': 'value1',
        'value2': 'value2'
    }

    def __init__(self, value1=None, value2=None):
        """LimitValue

        The model defined in huaweicloud sdk

        :param value1: 属性值1。
        :type value1: str
        :param value2: 属性值2。
        :type value2: str
        """
        
        

        self._value1 = None
        self._value2 = None
        self.discriminator = None

        if value1 is not None:
            self.value1 = value1
        if value2 is not None:
            self.value2 = value2

    @property
    def value1(self):
        """Gets the value1 of this LimitValue.

        属性值1。

        :return: The value1 of this LimitValue.
        :rtype: str
        """
        return self._value1

    @value1.setter
    def value1(self, value1):
        """Sets the value1 of this LimitValue.

        属性值1。

        :param value1: The value1 of this LimitValue.
        :type value1: str
        """
        self._value1 = value1

    @property
    def value2(self):
        """Gets the value2 of this LimitValue.

        属性值2。

        :return: The value2 of this LimitValue.
        :rtype: str
        """
        return self._value2

    @value2.setter
    def value2(self, value2):
        """Sets the value2 of this LimitValue.

        属性值2。

        :param value2: The value2 of this LimitValue.
        :type value2: str
        """
        self._value2 = value2

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
        if not isinstance(other, LimitValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
