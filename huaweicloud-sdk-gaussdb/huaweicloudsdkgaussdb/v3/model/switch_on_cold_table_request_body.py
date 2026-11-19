# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchOnColdTableRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_on': 'bool'
    }

    attribute_map = {
        'switch_on': 'switch_on'
    }

    def __init__(self, switch_on=None):
        r"""SwitchOnColdTableRequestBody

        The model defined in huaweicloud sdk

        :param switch_on: **参数解释**：  冷热分离开关状态。  **约束限制**：  开启冷热数据分离功能后，暂不支持关闭。  **取值范围**：  true：开启。  **默认取值**：  不涉及。
        :type switch_on: bool
        """
        
        

        self._switch_on = None
        self.discriminator = None

        self.switch_on = switch_on

    @property
    def switch_on(self):
        r"""Gets the switch_on of this SwitchOnColdTableRequestBody.

        **参数解释**：  冷热分离开关状态。  **约束限制**：  开启冷热数据分离功能后，暂不支持关闭。  **取值范围**：  true：开启。  **默认取值**：  不涉及。

        :return: The switch_on of this SwitchOnColdTableRequestBody.
        :rtype: bool
        """
        return self._switch_on

    @switch_on.setter
    def switch_on(self, switch_on):
        r"""Sets the switch_on of this SwitchOnColdTableRequestBody.

        **参数解释**：  冷热分离开关状态。  **约束限制**：  开启冷热数据分离功能后，暂不支持关闭。  **取值范围**：  true：开启。  **默认取值**：  不涉及。

        :param switch_on: The switch_on of this SwitchOnColdTableRequestBody.
        :type switch_on: bool
        """
        self._switch_on = switch_on

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
        if not isinstance(other, SwitchOnColdTableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
