# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVariableGroupReqVariables:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sequence': 'int',
        'name': 'str',
        'type': 'str',
        'value': 'str',
        'description': 'str',
        'is_secret': 'bool'
    }

    attribute_map = {
        'sequence': 'sequence',
        'name': 'name',
        'type': 'type',
        'value': 'value',
        'description': 'description',
        'is_secret': 'is_secret'
    }

    def __init__(self, sequence=None, name=None, type=None, value=None, description=None, is_secret=None):
        r"""CreateVariableGroupReqVariables

        The model defined in huaweicloud sdk

        :param sequence: **参数解释**： 参数序号。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type sequence: int
        :param name: **参数解释**： 参数名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type name: str
        :param type: **参数解释**： 参数类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type type: str
        :param value: **参数解释**： 参数默认值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type value: str
        :param description: **参数解释**： 参数描述。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type description: str
        :param is_secret: **参数解释**： 是否私密参数。 **约束限制**： 不涉及。 **取值范围**： - true：是私密参数。 - false：不是私密参数。 **默认取值**： 不涉及。 
        :type is_secret: bool
        """
        
        

        self._sequence = None
        self._name = None
        self._type = None
        self._value = None
        self._description = None
        self._is_secret = None
        self.discriminator = None

        if sequence is not None:
            self.sequence = sequence
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if description is not None:
            self.description = description
        if is_secret is not None:
            self.is_secret = is_secret

    @property
    def sequence(self):
        r"""Gets the sequence of this CreateVariableGroupReqVariables.

        **参数解释**： 参数序号。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The sequence of this CreateVariableGroupReqVariables.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this CreateVariableGroupReqVariables.

        **参数解释**： 参数序号。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param sequence: The sequence of this CreateVariableGroupReqVariables.
        :type sequence: int
        """
        self._sequence = sequence

    @property
    def name(self):
        r"""Gets the name of this CreateVariableGroupReqVariables.

        **参数解释**： 参数名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The name of this CreateVariableGroupReqVariables.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateVariableGroupReqVariables.

        **参数解释**： 参数名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param name: The name of this CreateVariableGroupReqVariables.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this CreateVariableGroupReqVariables.

        **参数解释**： 参数类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The type of this CreateVariableGroupReqVariables.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateVariableGroupReqVariables.

        **参数解释**： 参数类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param type: The type of this CreateVariableGroupReqVariables.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this CreateVariableGroupReqVariables.

        **参数解释**： 参数默认值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The value of this CreateVariableGroupReqVariables.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CreateVariableGroupReqVariables.

        **参数解释**： 参数默认值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param value: The value of this CreateVariableGroupReqVariables.
        :type value: str
        """
        self._value = value

    @property
    def description(self):
        r"""Gets the description of this CreateVariableGroupReqVariables.

        **参数解释**： 参数描述。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The description of this CreateVariableGroupReqVariables.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateVariableGroupReqVariables.

        **参数解释**： 参数描述。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param description: The description of this CreateVariableGroupReqVariables.
        :type description: str
        """
        self._description = description

    @property
    def is_secret(self):
        r"""Gets the is_secret of this CreateVariableGroupReqVariables.

        **参数解释**： 是否私密参数。 **约束限制**： 不涉及。 **取值范围**： - true：是私密参数。 - false：不是私密参数。 **默认取值**： 不涉及。 

        :return: The is_secret of this CreateVariableGroupReqVariables.
        :rtype: bool
        """
        return self._is_secret

    @is_secret.setter
    def is_secret(self, is_secret):
        r"""Sets the is_secret of this CreateVariableGroupReqVariables.

        **参数解释**： 是否私密参数。 **约束限制**： 不涉及。 **取值范围**： - true：是私密参数。 - false：不是私密参数。 **默认取值**： 不涉及。 

        :param is_secret: The is_secret of this CreateVariableGroupReqVariables.
        :type is_secret: bool
        """
        self._is_secret = is_secret

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
        if not isinstance(other, CreateVariableGroupReqVariables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
