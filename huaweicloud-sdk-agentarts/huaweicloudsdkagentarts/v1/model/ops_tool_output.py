# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsToolOutput:

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
        'explanation': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'explanation': 'explanation'
    }

    def __init__(self, name=None, description=None, explanation=None):
        r"""OpsToolOutput

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 工具的名称。  **约束限制：** 不涉及。  **取值范围：** 长度在1-256个字符。  **默认取值：** 无。
        :type name: str
        :param description: **参数解释：** 工具的描述内容。  **约束限制：** 不涉及。  **取值范围：** 长度在1-10000个字符。  **默认取值：** 无。
        :type description: str
        :param explanation: **参数解释：** 优化的原因。  **取值范围：** 长度在0-4096个字符。
        :type explanation: str
        """
        
        

        self._name = None
        self._description = None
        self._explanation = None
        self.discriminator = None

        self.name = name
        self.description = description
        if explanation is not None:
            self.explanation = explanation

    @property
    def name(self):
        r"""Gets the name of this OpsToolOutput.

        **参数解释：** 工具的名称。  **约束限制：** 不涉及。  **取值范围：** 长度在1-256个字符。  **默认取值：** 无。

        :return: The name of this OpsToolOutput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OpsToolOutput.

        **参数解释：** 工具的名称。  **约束限制：** 不涉及。  **取值范围：** 长度在1-256个字符。  **默认取值：** 无。

        :param name: The name of this OpsToolOutput.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this OpsToolOutput.

        **参数解释：** 工具的描述内容。  **约束限制：** 不涉及。  **取值范围：** 长度在1-10000个字符。  **默认取值：** 无。

        :return: The description of this OpsToolOutput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OpsToolOutput.

        **参数解释：** 工具的描述内容。  **约束限制：** 不涉及。  **取值范围：** 长度在1-10000个字符。  **默认取值：** 无。

        :param description: The description of this OpsToolOutput.
        :type description: str
        """
        self._description = description

    @property
    def explanation(self):
        r"""Gets the explanation of this OpsToolOutput.

        **参数解释：** 优化的原因。  **取值范围：** 长度在0-4096个字符。

        :return: The explanation of this OpsToolOutput.
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        r"""Sets the explanation of this OpsToolOutput.

        **参数解释：** 优化的原因。  **取值范围：** 长度在0-4096个字符。

        :param explanation: The explanation of this OpsToolOutput.
        :type explanation: str
        """
        self._explanation = explanation

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
        if not isinstance(other, OpsToolOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
