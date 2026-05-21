# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParaGroupUpdate:

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
        'values': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'values': 'values'
    }

    def __init__(self, name=None, description=None, values=None):
        r"""ParaGroupUpdate

        The model defined in huaweicloud sdk

        :param name: **参数解释**：  参数组名称。  **约束限制**：  不涉及。  **取值范围**：  在1到64个字符之间，区分大小写，可包含字母、数字、中划线、下划线或句点，不能包含其他特殊字符。。  **默认取值**：  不涉及。
        :type name: str
        :param description: **参数解释**：  参数组描述。  **约束限制**：  不涉及。  **取值范围**：  不能超过256位，且不能包含回车和特殊字符 ! &lt; \&quot; &#x3D; &#39; &gt; &amp;。  **默认取值**：  不涉及。
        :type description: str
        :param values: **参数解释**：  修改的值。  **约束限制**：  不涉及  **取值范围**：  长度为1-64的a-z、A-Z、0-9、.、_ 和 -的字符。  **默认取值**：  不涉及。
        :type values: dict(str, str)
        """
        
        

        self._name = None
        self._description = None
        self._values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.values = values

    @property
    def name(self):
        r"""Gets the name of this ParaGroupUpdate.

        **参数解释**：  参数组名称。  **约束限制**：  不涉及。  **取值范围**：  在1到64个字符之间，区分大小写，可包含字母、数字、中划线、下划线或句点，不能包含其他特殊字符。。  **默认取值**：  不涉及。

        :return: The name of this ParaGroupUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ParaGroupUpdate.

        **参数解释**：  参数组名称。  **约束限制**：  不涉及。  **取值范围**：  在1到64个字符之间，区分大小写，可包含字母、数字、中划线、下划线或句点，不能包含其他特殊字符。。  **默认取值**：  不涉及。

        :param name: The name of this ParaGroupUpdate.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ParaGroupUpdate.

        **参数解释**：  参数组描述。  **约束限制**：  不涉及。  **取值范围**：  不能超过256位，且不能包含回车和特殊字符 ! < \" = ' > &。  **默认取值**：  不涉及。

        :return: The description of this ParaGroupUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ParaGroupUpdate.

        **参数解释**：  参数组描述。  **约束限制**：  不涉及。  **取值范围**：  不能超过256位，且不能包含回车和特殊字符 ! < \" = ' > &。  **默认取值**：  不涉及。

        :param description: The description of this ParaGroupUpdate.
        :type description: str
        """
        self._description = description

    @property
    def values(self):
        r"""Gets the values of this ParaGroupUpdate.

        **参数解释**：  修改的值。  **约束限制**：  不涉及  **取值范围**：  长度为1-64的a-z、A-Z、0-9、.、_ 和 -的字符。  **默认取值**：  不涉及。

        :return: The values of this ParaGroupUpdate.
        :rtype: dict(str, str)
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this ParaGroupUpdate.

        **参数解释**：  修改的值。  **约束限制**：  不涉及  **取值范围**：  长度为1-64的a-z、A-Z、0-9、.、_ 和 -的字符。  **默认取值**：  不涉及。

        :param values: The values of this ParaGroupUpdate.
        :type values: dict(str, str)
        """
        self._values = values

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
        if not isinstance(other, ParaGroupUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
