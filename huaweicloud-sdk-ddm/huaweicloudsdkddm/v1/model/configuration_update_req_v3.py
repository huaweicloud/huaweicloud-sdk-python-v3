# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationUpdateReqV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'values': 'dict(str, str)',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'values': 'values',
        'name': 'name'
    }

    def __init__(self, description=None, values=None, name=None):
        r"""ConfigurationUpdateReqV3

        The model defined in huaweicloud sdk

        :param description: **参数解释**：  描述。  **约束限制**：  不涉及  **取值范围**：  0-256的不是!、&lt;、&gt;、&#x3D;、&amp;、\&quot; 或 &#39; 的字符。  **默认取值**：  不涉及。
        :type description: str
        :param values: **参数解释**：  修改的值。  **约束限制**：  不涉及  **取值范围**：  长度为1-64的a-z、A-Z、0-9、.、_ 和 -的字符。  **默认取值**：  不涉及。
        :type values: dict(str, str)
        :param name: **参数解释**：  参数的名称。  **约束限制**：  不涉及  **取值范围**：  长度为1-64的a-z、A-Z、0-9、.、_ 和 -的字符。  **默认取值**：  不涉及。
        :type name: str
        """
        
        

        self._description = None
        self._values = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.values = values
        if name is not None:
            self.name = name

    @property
    def description(self):
        r"""Gets the description of this ConfigurationUpdateReqV3.

        **参数解释**：  描述。  **约束限制**：  不涉及  **取值范围**：  0-256的不是!、<、>、=、&、\" 或 ' 的字符。  **默认取值**：  不涉及。

        :return: The description of this ConfigurationUpdateReqV3.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConfigurationUpdateReqV3.

        **参数解释**：  描述。  **约束限制**：  不涉及  **取值范围**：  0-256的不是!、<、>、=、&、\" 或 ' 的字符。  **默认取值**：  不涉及。

        :param description: The description of this ConfigurationUpdateReqV3.
        :type description: str
        """
        self._description = description

    @property
    def values(self):
        r"""Gets the values of this ConfigurationUpdateReqV3.

        **参数解释**：  修改的值。  **约束限制**：  不涉及  **取值范围**：  长度为1-64的a-z、A-Z、0-9、.、_ 和 -的字符。  **默认取值**：  不涉及。

        :return: The values of this ConfigurationUpdateReqV3.
        :rtype: dict(str, str)
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this ConfigurationUpdateReqV3.

        **参数解释**：  修改的值。  **约束限制**：  不涉及  **取值范围**：  长度为1-64的a-z、A-Z、0-9、.、_ 和 -的字符。  **默认取值**：  不涉及。

        :param values: The values of this ConfigurationUpdateReqV3.
        :type values: dict(str, str)
        """
        self._values = values

    @property
    def name(self):
        r"""Gets the name of this ConfigurationUpdateReqV3.

        **参数解释**：  参数的名称。  **约束限制**：  不涉及  **取值范围**：  长度为1-64的a-z、A-Z、0-9、.、_ 和 -的字符。  **默认取值**：  不涉及。

        :return: The name of this ConfigurationUpdateReqV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConfigurationUpdateReqV3.

        **参数解释**：  参数的名称。  **约束限制**：  不涉及  **取值范围**：  长度为1-64的a-z、A-Z、0-9、.、_ 和 -的字符。  **默认取值**：  不涉及。

        :param name: The name of this ConfigurationUpdateReqV3.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ConfigurationUpdateReqV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
