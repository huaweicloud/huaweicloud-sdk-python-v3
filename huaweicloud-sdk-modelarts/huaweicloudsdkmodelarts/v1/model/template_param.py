# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateParam:

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
        'description': 'str',
        'value': 'str',
        'visible': 'str',
        'regex': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'value': 'value',
        'visible': 'visible',
        'regex': 'regex'
    }

    def __init__(self, name=None, description=None, value=None, visible=None, regex=None):
        r"""TemplateParam

        The model defined in huaweicloud sdk

        :param name: **参数解释**：参数名称。 **取值范围**：不涉及。
        :type name: str
        :param description: **参数解释**：参数描述。 **取值范围**：不涉及。
        :type description: str
        :param value: **参数解释**：参数取值。 **取值范围**：不涉及。
        :type value: str
        :param visible: **参数解释**：是否展示在console。 **取值范围**：- true   -false。
        :type visible: str
        :param regex: **参数解释**：正则校验。 **取值范围**：不涉及。
        :type regex: str
        """
        
        

        self._name = None
        self._description = None
        self._value = None
        self._visible = None
        self._regex = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if value is not None:
            self.value = value
        if visible is not None:
            self.visible = visible
        if regex is not None:
            self.regex = regex

    @property
    def name(self):
        r"""Gets the name of this TemplateParam.

        **参数解释**：参数名称。 **取值范围**：不涉及。

        :return: The name of this TemplateParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TemplateParam.

        **参数解释**：参数名称。 **取值范围**：不涉及。

        :param name: The name of this TemplateParam.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this TemplateParam.

        **参数解释**：参数描述。 **取值范围**：不涉及。

        :return: The description of this TemplateParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TemplateParam.

        **参数解释**：参数描述。 **取值范围**：不涉及。

        :param description: The description of this TemplateParam.
        :type description: str
        """
        self._description = description

    @property
    def value(self):
        r"""Gets the value of this TemplateParam.

        **参数解释**：参数取值。 **取值范围**：不涉及。

        :return: The value of this TemplateParam.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this TemplateParam.

        **参数解释**：参数取值。 **取值范围**：不涉及。

        :param value: The value of this TemplateParam.
        :type value: str
        """
        self._value = value

    @property
    def visible(self):
        r"""Gets the visible of this TemplateParam.

        **参数解释**：是否展示在console。 **取值范围**：- true   -false。

        :return: The visible of this TemplateParam.
        :rtype: str
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this TemplateParam.

        **参数解释**：是否展示在console。 **取值范围**：- true   -false。

        :param visible: The visible of this TemplateParam.
        :type visible: str
        """
        self._visible = visible

    @property
    def regex(self):
        r"""Gets the regex of this TemplateParam.

        **参数解释**：正则校验。 **取值范围**：不涉及。

        :return: The regex of this TemplateParam.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        r"""Sets the regex of this TemplateParam.

        **参数解释**：正则校验。 **取值范围**：不涉及。

        :param regex: The regex of this TemplateParam.
        :type regex: str
        """
        self._regex = regex

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
        if not isinstance(other, TemplateParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
