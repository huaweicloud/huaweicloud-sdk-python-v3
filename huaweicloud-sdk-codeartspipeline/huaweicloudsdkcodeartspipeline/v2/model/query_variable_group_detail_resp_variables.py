# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryVariableGroupDetailRespVariables:

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
        'sequence': 'int',
        'type': 'str',
        'value': 'str',
        'is_secret': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'sequence': 'sequence',
        'type': 'type',
        'value': 'value',
        'is_secret': 'is_secret',
        'description': 'description'
    }

    def __init__(self, name=None, sequence=None, type=None, value=None, is_secret=None, description=None):
        r"""QueryVariableGroupDetailRespVariables

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 参数名称。 **取值范围**： 不涉及。 
        :type name: str
        :param sequence: **参数解释**： 参数序号。 **取值范围**： 不涉及。 
        :type sequence: int
        :param type: **参数解释**： 参数类型。 **取值范围**： 不涉及。 
        :type type: str
        :param value: **参数解释**： 参数默认值。 **取值范围**： 不涉及。 
        :type value: str
        :param is_secret: **参数解释**： 是否私密。 **取值范围**： - true：是私密参数。 - false：不是私密参数。 
        :type is_secret: bool
        :param description: **参数解释**： 描述。 **取值范围**： 不涉及。 
        :type description: str
        """
        
        

        self._name = None
        self._sequence = None
        self._type = None
        self._value = None
        self._is_secret = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if sequence is not None:
            self.sequence = sequence
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if is_secret is not None:
            self.is_secret = is_secret
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this QueryVariableGroupDetailRespVariables.

        **参数解释**： 参数名称。 **取值范围**： 不涉及。 

        :return: The name of this QueryVariableGroupDetailRespVariables.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QueryVariableGroupDetailRespVariables.

        **参数解释**： 参数名称。 **取值范围**： 不涉及。 

        :param name: The name of this QueryVariableGroupDetailRespVariables.
        :type name: str
        """
        self._name = name

    @property
    def sequence(self):
        r"""Gets the sequence of this QueryVariableGroupDetailRespVariables.

        **参数解释**： 参数序号。 **取值范围**： 不涉及。 

        :return: The sequence of this QueryVariableGroupDetailRespVariables.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this QueryVariableGroupDetailRespVariables.

        **参数解释**： 参数序号。 **取值范围**： 不涉及。 

        :param sequence: The sequence of this QueryVariableGroupDetailRespVariables.
        :type sequence: int
        """
        self._sequence = sequence

    @property
    def type(self):
        r"""Gets the type of this QueryVariableGroupDetailRespVariables.

        **参数解释**： 参数类型。 **取值范围**： 不涉及。 

        :return: The type of this QueryVariableGroupDetailRespVariables.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this QueryVariableGroupDetailRespVariables.

        **参数解释**： 参数类型。 **取值范围**： 不涉及。 

        :param type: The type of this QueryVariableGroupDetailRespVariables.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this QueryVariableGroupDetailRespVariables.

        **参数解释**： 参数默认值。 **取值范围**： 不涉及。 

        :return: The value of this QueryVariableGroupDetailRespVariables.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this QueryVariableGroupDetailRespVariables.

        **参数解释**： 参数默认值。 **取值范围**： 不涉及。 

        :param value: The value of this QueryVariableGroupDetailRespVariables.
        :type value: str
        """
        self._value = value

    @property
    def is_secret(self):
        r"""Gets the is_secret of this QueryVariableGroupDetailRespVariables.

        **参数解释**： 是否私密。 **取值范围**： - true：是私密参数。 - false：不是私密参数。 

        :return: The is_secret of this QueryVariableGroupDetailRespVariables.
        :rtype: bool
        """
        return self._is_secret

    @is_secret.setter
    def is_secret(self, is_secret):
        r"""Sets the is_secret of this QueryVariableGroupDetailRespVariables.

        **参数解释**： 是否私密。 **取值范围**： - true：是私密参数。 - false：不是私密参数。 

        :param is_secret: The is_secret of this QueryVariableGroupDetailRespVariables.
        :type is_secret: bool
        """
        self._is_secret = is_secret

    @property
    def description(self):
        r"""Gets the description of this QueryVariableGroupDetailRespVariables.

        **参数解释**： 描述。 **取值范围**： 不涉及。 

        :return: The description of this QueryVariableGroupDetailRespVariables.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this QueryVariableGroupDetailRespVariables.

        **参数解释**： 描述。 **取值范围**： 不涉及。 

        :param description: The description of this QueryVariableGroupDetailRespVariables.
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
        if not isinstance(other, QueryVariableGroupDetailRespVariables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
