# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchModifyReadAndWriteStrategyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'read_weight_list': 'list[dict(str, int)]'
    }

    attribute_map = {
        'read_weight_list': 'read_weight_list'
    }

    def __init__(self, read_weight_list=None):
        r"""BatchModifyReadAndWriteStrategyRequest

        The model defined in huaweicloud sdk

        :param read_weight_list: **参数解释**：  读写策略。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type read_weight_list: list[dict(str, int)]
        """
        
        

        self._read_weight_list = None
        self.discriminator = None

        if read_weight_list is not None:
            self.read_weight_list = read_weight_list

    @property
    def read_weight_list(self):
        r"""Gets the read_weight_list of this BatchModifyReadAndWriteStrategyRequest.

        **参数解释**：  读写策略。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The read_weight_list of this BatchModifyReadAndWriteStrategyRequest.
        :rtype: list[dict(str, int)]
        """
        return self._read_weight_list

    @read_weight_list.setter
    def read_weight_list(self, read_weight_list):
        r"""Sets the read_weight_list of this BatchModifyReadAndWriteStrategyRequest.

        **参数解释**：  读写策略。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param read_weight_list: The read_weight_list of this BatchModifyReadAndWriteStrategyRequest.
        :type read_weight_list: list[dict(str, int)]
        """
        self._read_weight_list = read_weight_list

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
        if not isinstance(other, BatchModifyReadAndWriteStrategyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
