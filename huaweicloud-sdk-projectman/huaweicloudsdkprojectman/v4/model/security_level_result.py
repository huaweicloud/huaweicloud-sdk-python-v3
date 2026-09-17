# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityLevelResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'display_value': 'str',
        'value': 'str',
        'code': 'str',
        'sequence': 'float'
    }

    attribute_map = {
        'id': 'id',
        'display_value': 'display_value',
        'value': 'value',
        'code': 'code',
        'sequence': 'sequence'
    }

    def __init__(self, id=None, display_value=None, value=None, code=None, sequence=None):
        r"""SecurityLevelResult

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 密级字段ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type id: str
        :param display_value: **参数解释**： 密级字段名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type display_value: str
        :param value: **参数解释**： 用户自定义的密级字段的值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type value: str
        :param code: **参数解释**： 密级编码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type code: str
        :param sequence: **参数解释**： 密级排序值，越大级别越高。 **取值范围**： 不涉及。
        :type sequence: float
        """
        
        

        self._id = None
        self._display_value = None
        self._value = None
        self._code = None
        self._sequence = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_value is not None:
            self.display_value = display_value
        if value is not None:
            self.value = value
        if code is not None:
            self.code = code
        if sequence is not None:
            self.sequence = sequence

    @property
    def id(self):
        r"""Gets the id of this SecurityLevelResult.

        **参数解释**： 密级字段ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The id of this SecurityLevelResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SecurityLevelResult.

        **参数解释**： 密级字段ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param id: The id of this SecurityLevelResult.
        :type id: str
        """
        self._id = id

    @property
    def display_value(self):
        r"""Gets the display_value of this SecurityLevelResult.

        **参数解释**： 密级字段名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The display_value of this SecurityLevelResult.
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        r"""Sets the display_value of this SecurityLevelResult.

        **参数解释**： 密级字段名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param display_value: The display_value of this SecurityLevelResult.
        :type display_value: str
        """
        self._display_value = display_value

    @property
    def value(self):
        r"""Gets the value of this SecurityLevelResult.

        **参数解释**： 用户自定义的密级字段的值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The value of this SecurityLevelResult.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this SecurityLevelResult.

        **参数解释**： 用户自定义的密级字段的值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param value: The value of this SecurityLevelResult.
        :type value: str
        """
        self._value = value

    @property
    def code(self):
        r"""Gets the code of this SecurityLevelResult.

        **参数解释**： 密级编码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The code of this SecurityLevelResult.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this SecurityLevelResult.

        **参数解释**： 密级编码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param code: The code of this SecurityLevelResult.
        :type code: str
        """
        self._code = code

    @property
    def sequence(self):
        r"""Gets the sequence of this SecurityLevelResult.

        **参数解释**： 密级排序值，越大级别越高。 **取值范围**： 不涉及。

        :return: The sequence of this SecurityLevelResult.
        :rtype: float
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this SecurityLevelResult.

        **参数解释**： 密级排序值，越大级别越高。 **取值范围**： 不涉及。

        :param sequence: The sequence of this SecurityLevelResult.
        :type sequence: float
        """
        self._sequence = sequence

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
        if not isinstance(other, SecurityLevelResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
