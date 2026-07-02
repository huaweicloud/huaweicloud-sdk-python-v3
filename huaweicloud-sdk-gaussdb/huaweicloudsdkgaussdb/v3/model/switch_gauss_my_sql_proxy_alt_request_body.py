# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchGaussMySqlProxyAltRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alt_enabled': 'str'
    }

    attribute_map = {
        'alt_enabled': 'alt_enabled'
    }

    def __init__(self, alt_enabled=None):
        r"""SwitchGaussMySqlProxyAltRequestBody

        The model defined in huaweicloud sdk

        :param alt_enabled: **参数解释**：  ALT开关状态。  **取值范围**： - on：开启。 - off：关闭。  **默认取值**： 不涉及。
        :type alt_enabled: str
        """
        
        

        self._alt_enabled = None
        self.discriminator = None

        self.alt_enabled = alt_enabled

    @property
    def alt_enabled(self):
        r"""Gets the alt_enabled of this SwitchGaussMySqlProxyAltRequestBody.

        **参数解释**：  ALT开关状态。  **取值范围**： - on：开启。 - off：关闭。  **默认取值**： 不涉及。

        :return: The alt_enabled of this SwitchGaussMySqlProxyAltRequestBody.
        :rtype: str
        """
        return self._alt_enabled

    @alt_enabled.setter
    def alt_enabled(self, alt_enabled):
        r"""Sets the alt_enabled of this SwitchGaussMySqlProxyAltRequestBody.

        **参数解释**：  ALT开关状态。  **取值范围**： - on：开启。 - off：关闭。  **默认取值**： 不涉及。

        :param alt_enabled: The alt_enabled of this SwitchGaussMySqlProxyAltRequestBody.
        :type alt_enabled: str
        """
        self._alt_enabled = alt_enabled

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
        if not isinstance(other, SwitchGaussMySqlProxyAltRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
