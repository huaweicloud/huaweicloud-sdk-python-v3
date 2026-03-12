# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationParameterResult:

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
        'value': 'str',
        'restart_required': 'bool',
        'readonly': 'bool',
        'value_range': 'str',
        'type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'restart_required': 'restart_required',
        'readonly': 'readonly',
        'value_range': 'value_range',
        'type': 'type',
        'description': 'description'
    }

    def __init__(self, name=None, value=None, restart_required=None, readonly=None, value_range=None, type=None, description=None):
        r"""ConfigurationParameterResult

        The model defined in huaweicloud sdk

        :param name: 参数名称。
        :type name: str
        :param value: 参数值。
        :type value: str
        :param restart_required: 修改该参数是否需要重启实例。
        :type restart_required: bool
        :param readonly: **参数解释**: 该参数的value值是否为只读，无法直接修改。 **取值范围**: - true：该参数的value值只读，不允许用户直接修改。 - false：允许修改。
        :type readonly: bool
        :param value_range: 参数取值范围。
        :type value_range: str
        :param type: 参数类型，取值为“string”、“integer”、“boolean”、“list”或“float”之一。
        :type type: str
        :param description: 参数描述。
        :type description: str
        """
        
        

        self._name = None
        self._value = None
        self._restart_required = None
        self._readonly = None
        self._value_range = None
        self._type = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if restart_required is not None:
            self.restart_required = restart_required
        if readonly is not None:
            self.readonly = readonly
        if value_range is not None:
            self.value_range = value_range
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this ConfigurationParameterResult.

        参数名称。

        :return: The name of this ConfigurationParameterResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConfigurationParameterResult.

        参数名称。

        :param name: The name of this ConfigurationParameterResult.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this ConfigurationParameterResult.

        参数值。

        :return: The value of this ConfigurationParameterResult.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ConfigurationParameterResult.

        参数值。

        :param value: The value of this ConfigurationParameterResult.
        :type value: str
        """
        self._value = value

    @property
    def restart_required(self):
        r"""Gets the restart_required of this ConfigurationParameterResult.

        修改该参数是否需要重启实例。

        :return: The restart_required of this ConfigurationParameterResult.
        :rtype: bool
        """
        return self._restart_required

    @restart_required.setter
    def restart_required(self, restart_required):
        r"""Sets the restart_required of this ConfigurationParameterResult.

        修改该参数是否需要重启实例。

        :param restart_required: The restart_required of this ConfigurationParameterResult.
        :type restart_required: bool
        """
        self._restart_required = restart_required

    @property
    def readonly(self):
        r"""Gets the readonly of this ConfigurationParameterResult.

        **参数解释**: 该参数的value值是否为只读，无法直接修改。 **取值范围**: - true：该参数的value值只读，不允许用户直接修改。 - false：允许修改。

        :return: The readonly of this ConfigurationParameterResult.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        r"""Sets the readonly of this ConfigurationParameterResult.

        **参数解释**: 该参数的value值是否为只读，无法直接修改。 **取值范围**: - true：该参数的value值只读，不允许用户直接修改。 - false：允许修改。

        :param readonly: The readonly of this ConfigurationParameterResult.
        :type readonly: bool
        """
        self._readonly = readonly

    @property
    def value_range(self):
        r"""Gets the value_range of this ConfigurationParameterResult.

        参数取值范围。

        :return: The value_range of this ConfigurationParameterResult.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        r"""Sets the value_range of this ConfigurationParameterResult.

        参数取值范围。

        :param value_range: The value_range of this ConfigurationParameterResult.
        :type value_range: str
        """
        self._value_range = value_range

    @property
    def type(self):
        r"""Gets the type of this ConfigurationParameterResult.

        参数类型，取值为“string”、“integer”、“boolean”、“list”或“float”之一。

        :return: The type of this ConfigurationParameterResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConfigurationParameterResult.

        参数类型，取值为“string”、“integer”、“boolean”、“list”或“float”之一。

        :param type: The type of this ConfigurationParameterResult.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this ConfigurationParameterResult.

        参数描述。

        :return: The description of this ConfigurationParameterResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConfigurationParameterResult.

        参数描述。

        :param description: The description of this ConfigurationParameterResult.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigurationParameterResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
