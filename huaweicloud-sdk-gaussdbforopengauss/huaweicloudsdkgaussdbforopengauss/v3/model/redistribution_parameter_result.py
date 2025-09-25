# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedistributionParameterResult:

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
        'value_range': 'str',
        'type': 'object',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'restart_required': 'restart_required',
        'value_range': 'value_range',
        'type': 'type',
        'description': 'description'
    }

    def __init__(self, name=None, value=None, restart_required=None, value_range=None, type=None, description=None):
        r"""RedistributionParameterResult

        The model defined in huaweicloud sdk

        :param name: **参数解释**: 参数名称。 **取值范围**: 不涉及。
        :type name: str
        :param value: **参数解释**: 参数值。 **取值范围**: 不涉及。
        :type value: str
        :param restart_required: **参数解释**: 修改参数是否需要重启。 **取值范围**: - true：需要重启。 - false：不需要重启。
        :type restart_required: bool
        :param value_range: **参数解释**: 参数取值范围。 **取值范围**: 不涉及。
        :type value_range: str
        :param type: **参数解释**: 参数类型。 **取值范围**: - integer：整数。 - boolean：布尔类型。 - string：字符串类型。
        :type type: object
        :param description: **参数解释**: 参数描述。 **取值范围**: 不涉及。
        :type description: str
        """
        
        

        self._name = None
        self._value = None
        self._restart_required = None
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
        if value_range is not None:
            self.value_range = value_range
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this RedistributionParameterResult.

        **参数解释**: 参数名称。 **取值范围**: 不涉及。

        :return: The name of this RedistributionParameterResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RedistributionParameterResult.

        **参数解释**: 参数名称。 **取值范围**: 不涉及。

        :param name: The name of this RedistributionParameterResult.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this RedistributionParameterResult.

        **参数解释**: 参数值。 **取值范围**: 不涉及。

        :return: The value of this RedistributionParameterResult.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this RedistributionParameterResult.

        **参数解释**: 参数值。 **取值范围**: 不涉及。

        :param value: The value of this RedistributionParameterResult.
        :type value: str
        """
        self._value = value

    @property
    def restart_required(self):
        r"""Gets the restart_required of this RedistributionParameterResult.

        **参数解释**: 修改参数是否需要重启。 **取值范围**: - true：需要重启。 - false：不需要重启。

        :return: The restart_required of this RedistributionParameterResult.
        :rtype: bool
        """
        return self._restart_required

    @restart_required.setter
    def restart_required(self, restart_required):
        r"""Sets the restart_required of this RedistributionParameterResult.

        **参数解释**: 修改参数是否需要重启。 **取值范围**: - true：需要重启。 - false：不需要重启。

        :param restart_required: The restart_required of this RedistributionParameterResult.
        :type restart_required: bool
        """
        self._restart_required = restart_required

    @property
    def value_range(self):
        r"""Gets the value_range of this RedistributionParameterResult.

        **参数解释**: 参数取值范围。 **取值范围**: 不涉及。

        :return: The value_range of this RedistributionParameterResult.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        r"""Sets the value_range of this RedistributionParameterResult.

        **参数解释**: 参数取值范围。 **取值范围**: 不涉及。

        :param value_range: The value_range of this RedistributionParameterResult.
        :type value_range: str
        """
        self._value_range = value_range

    @property
    def type(self):
        r"""Gets the type of this RedistributionParameterResult.

        **参数解释**: 参数类型。 **取值范围**: - integer：整数。 - boolean：布尔类型。 - string：字符串类型。

        :return: The type of this RedistributionParameterResult.
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RedistributionParameterResult.

        **参数解释**: 参数类型。 **取值范围**: - integer：整数。 - boolean：布尔类型。 - string：字符串类型。

        :param type: The type of this RedistributionParameterResult.
        :type type: object
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this RedistributionParameterResult.

        **参数解释**: 参数描述。 **取值范围**: 不涉及。

        :return: The description of this RedistributionParameterResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RedistributionParameterResult.

        **参数解释**: 参数描述。 **取值范围**: 不涉及。

        :param description: The description of this RedistributionParameterResult.
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
        if not isinstance(other, RedistributionParameterResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
