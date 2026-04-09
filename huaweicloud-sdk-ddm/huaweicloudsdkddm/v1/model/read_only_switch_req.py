# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReadOnlySwitchReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'readonly': 'bool'
    }

    attribute_map = {
        'readonly': 'readonly'
    }

    def __init__(self, readonly=None):
        r"""ReadOnlySwitchReq

        The model defined in huaweicloud sdk

        :param readonly: **参数解释**：  实例是否设置为只读。 - true：设置为只读。 - false：解除只读状态。  **约束限制**：  不涉及。  **取值范围**：  true或者false。  **默认取值**：  不涉及。
        :type readonly: bool
        """
        
        

        self._readonly = None
        self.discriminator = None

        self.readonly = readonly

    @property
    def readonly(self):
        r"""Gets the readonly of this ReadOnlySwitchReq.

        **参数解释**：  实例是否设置为只读。 - true：设置为只读。 - false：解除只读状态。  **约束限制**：  不涉及。  **取值范围**：  true或者false。  **默认取值**：  不涉及。

        :return: The readonly of this ReadOnlySwitchReq.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        r"""Sets the readonly of this ReadOnlySwitchReq.

        **参数解释**：  实例是否设置为只读。 - true：设置为只读。 - false：解除只读状态。  **约束限制**：  不涉及。  **取值范围**：  true或者false。  **默认取值**：  不涉及。

        :param readonly: The readonly of this ReadOnlySwitchReq.
        :type readonly: bool
        """
        self._readonly = readonly

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
        if not isinstance(other, ReadOnlySwitchReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
