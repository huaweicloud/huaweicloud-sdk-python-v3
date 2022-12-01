# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'values': 'list[ConfigurationParameterUnit]',
        'unit': 'str',
        'type': 'str',
        'readonly': 'bool',
        'value_range': 'str',
        'restart_required': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'values': 'values',
        'unit': 'unit',
        'type': 'type',
        'readonly': 'readonly',
        'value_range': 'value_range',
        'restart_required': 'restart_required',
        'description': 'description'
    }

    def __init__(self, name=None, values=None, unit=None, type=None, readonly=None, value_range=None, restart_required=None, description=None):
        """ConfigurationParameter

        The model defined in huaweicloud sdk

        :param name: 参数名称。
        :type name: str
        :param values: 参数值。
        :type values: list[:class:`huaweicloudsdkdws.v2.ConfigurationParameterUnit`]
        :param unit: 参数单位。
        :type unit: str
        :param type: 参数类型，包括boolean、string、integer、float、list。
        :type type: str
        :param readonly: 是否只读。
        :type readonly: bool
        :param value_range: 参数值范围。
        :type value_range: str
        :param restart_required: 是否需要重启。
        :type restart_required: bool
        :param description: 参数描述。
        :type description: str
        """
        
        

        self._name = None
        self._values = None
        self._unit = None
        self._type = None
        self._readonly = None
        self._value_range = None
        self._restart_required = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.values = values
        self.unit = unit
        self.type = type
        self.readonly = readonly
        self.value_range = value_range
        self.restart_required = restart_required
        self.description = description

    @property
    def name(self):
        """Gets the name of this ConfigurationParameter.

        参数名称。

        :return: The name of this ConfigurationParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigurationParameter.

        参数名称。

        :param name: The name of this ConfigurationParameter.
        :type name: str
        """
        self._name = name

    @property
    def values(self):
        """Gets the values of this ConfigurationParameter.

        参数值。

        :return: The values of this ConfigurationParameter.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ConfigurationParameterUnit`]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ConfigurationParameter.

        参数值。

        :param values: The values of this ConfigurationParameter.
        :type values: list[:class:`huaweicloudsdkdws.v2.ConfigurationParameterUnit`]
        """
        self._values = values

    @property
    def unit(self):
        """Gets the unit of this ConfigurationParameter.

        参数单位。

        :return: The unit of this ConfigurationParameter.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ConfigurationParameter.

        参数单位。

        :param unit: The unit of this ConfigurationParameter.
        :type unit: str
        """
        self._unit = unit

    @property
    def type(self):
        """Gets the type of this ConfigurationParameter.

        参数类型，包括boolean、string、integer、float、list。

        :return: The type of this ConfigurationParameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConfigurationParameter.

        参数类型，包括boolean、string、integer、float、list。

        :param type: The type of this ConfigurationParameter.
        :type type: str
        """
        self._type = type

    @property
    def readonly(self):
        """Gets the readonly of this ConfigurationParameter.

        是否只读。

        :return: The readonly of this ConfigurationParameter.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """Sets the readonly of this ConfigurationParameter.

        是否只读。

        :param readonly: The readonly of this ConfigurationParameter.
        :type readonly: bool
        """
        self._readonly = readonly

    @property
    def value_range(self):
        """Gets the value_range of this ConfigurationParameter.

        参数值范围。

        :return: The value_range of this ConfigurationParameter.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        """Sets the value_range of this ConfigurationParameter.

        参数值范围。

        :param value_range: The value_range of this ConfigurationParameter.
        :type value_range: str
        """
        self._value_range = value_range

    @property
    def restart_required(self):
        """Gets the restart_required of this ConfigurationParameter.

        是否需要重启。

        :return: The restart_required of this ConfigurationParameter.
        :rtype: bool
        """
        return self._restart_required

    @restart_required.setter
    def restart_required(self, restart_required):
        """Sets the restart_required of this ConfigurationParameter.

        是否需要重启。

        :param restart_required: The restart_required of this ConfigurationParameter.
        :type restart_required: bool
        """
        self._restart_required = restart_required

    @property
    def description(self):
        """Gets the description of this ConfigurationParameter.

        参数描述。

        :return: The description of this ConfigurationParameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConfigurationParameter.

        参数描述。

        :param description: The description of this ConfigurationParameter.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ConfigurationParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
