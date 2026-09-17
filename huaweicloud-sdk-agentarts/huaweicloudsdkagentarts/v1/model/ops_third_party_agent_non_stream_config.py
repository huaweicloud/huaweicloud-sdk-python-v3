# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsThirdPartyAgentNonStreamConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'output_key': 'str'
    }

    attribute_map = {
        'output_key': 'output_key'
    }

    def __init__(self, output_key=None):
        r"""OpsThirdPartyAgentNonStreamConfig

        The model defined in huaweicloud sdk

        :param output_key: **参数解释：** 响应体中Agent输出内容的字段路径，支持多级路径（如data.choices[0].message.content）。 **约束限制：** 最大长度200字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type output_key: str
        """
        
        

        self._output_key = None
        self.discriminator = None

        self.output_key = output_key

    @property
    def output_key(self):
        r"""Gets the output_key of this OpsThirdPartyAgentNonStreamConfig.

        **参数解释：** 响应体中Agent输出内容的字段路径，支持多级路径（如data.choices[0].message.content）。 **约束限制：** 最大长度200字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The output_key of this OpsThirdPartyAgentNonStreamConfig.
        :rtype: str
        """
        return self._output_key

    @output_key.setter
    def output_key(self, output_key):
        r"""Sets the output_key of this OpsThirdPartyAgentNonStreamConfig.

        **参数解释：** 响应体中Agent输出内容的字段路径，支持多级路径（如data.choices[0].message.content）。 **约束限制：** 最大长度200字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param output_key: The output_key of this OpsThirdPartyAgentNonStreamConfig.
        :type output_key: str
        """
        self._output_key = output_key

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
        if not isinstance(other, OpsThirdPartyAgentNonStreamConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
