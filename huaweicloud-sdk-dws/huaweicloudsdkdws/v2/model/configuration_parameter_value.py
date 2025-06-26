# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationParameterValue:

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
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, type=None, name=None, value=None):
        r"""ConfigurationParameterValue

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 参数类型。 **取值范围**： cn、dn。
        :type type: str
        :param name: **参数解释**： 参数名称。 **取值范围**： 不涉及。
        :type name: str
        :param value: **参数解释**： 参数值。 **取值范围**： 不涉及。
        :type value: str
        """
        
        

        self._type = None
        self._name = None
        self._value = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.value = value

    @property
    def type(self):
        r"""Gets the type of this ConfigurationParameterValue.

        **参数解释**： 参数类型。 **取值范围**： cn、dn。

        :return: The type of this ConfigurationParameterValue.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConfigurationParameterValue.

        **参数解释**： 参数类型。 **取值范围**： cn、dn。

        :param type: The type of this ConfigurationParameterValue.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ConfigurationParameterValue.

        **参数解释**： 参数名称。 **取值范围**： 不涉及。

        :return: The name of this ConfigurationParameterValue.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConfigurationParameterValue.

        **参数解释**： 参数名称。 **取值范围**： 不涉及。

        :param name: The name of this ConfigurationParameterValue.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this ConfigurationParameterValue.

        **参数解释**： 参数值。 **取值范围**： 不涉及。

        :return: The value of this ConfigurationParameterValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ConfigurationParameterValue.

        **参数解释**： 参数值。 **取值范围**： 不涉及。

        :param value: The value of this ConfigurationParameterValue.
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
        if not isinstance(other, ConfigurationParameterValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
