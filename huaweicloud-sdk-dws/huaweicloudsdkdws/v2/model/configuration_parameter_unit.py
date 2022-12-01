# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationParameterUnit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'value': 'str',
        'default_value': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'default_value': 'default_value'
    }

    def __init__(self, type=None, value=None, default_value=None):
        """ConfigurationParameterUnit

        The model defined in huaweicloud sdk

        :param type: 参数类型，包括：cn、dn。
        :type type: str
        :param value: 参数值。
        :type value: str
        :param default_value: 参数默认值。
        :type default_value: str
        """
        
        

        self._type = None
        self._value = None
        self._default_value = None
        self.discriminator = None

        self.type = type
        self.value = value
        self.default_value = default_value

    @property
    def type(self):
        """Gets the type of this ConfigurationParameterUnit.

        参数类型，包括：cn、dn。

        :return: The type of this ConfigurationParameterUnit.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConfigurationParameterUnit.

        参数类型，包括：cn、dn。

        :param type: The type of this ConfigurationParameterUnit.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this ConfigurationParameterUnit.

        参数值。

        :return: The value of this ConfigurationParameterUnit.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConfigurationParameterUnit.

        参数值。

        :param value: The value of this ConfigurationParameterUnit.
        :type value: str
        """
        self._value = value

    @property
    def default_value(self):
        """Gets the default_value of this ConfigurationParameterUnit.

        参数默认值。

        :return: The default_value of this ConfigurationParameterUnit.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this ConfigurationParameterUnit.

        参数默认值。

        :param default_value: The default_value of this ConfigurationParameterUnit.
        :type default_value: str
        """
        self._default_value = default_value

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
        if not isinstance(other, ConfigurationParameterUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
