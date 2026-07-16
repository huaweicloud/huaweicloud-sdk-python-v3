# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsAddItemRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'turns': 'list[OpsTurnInput]'
    }

    attribute_map = {
        'turns': 'turns'
    }

    def __init__(self, turns=None):
        r"""OpsAddItemRequest

        The model defined in huaweicloud sdk

        :param turns: **参数解释：** 构成该数据条目的交互轮次列表。对于单轮问答长度为1，多轮对话包含多个轮次。 **约束限制：** 包含1到10000个轮次项。 **取值范围：** 参考OpsTurnInput定义。 **默认取值：** 不涉及。 
        :type turns: list[:class:`huaweicloudsdkagentarts.v1.OpsTurnInput`]
        """
        
        

        self._turns = None
        self.discriminator = None

        self.turns = turns

    @property
    def turns(self):
        r"""Gets the turns of this OpsAddItemRequest.

        **参数解释：** 构成该数据条目的交互轮次列表。对于单轮问答长度为1，多轮对话包含多个轮次。 **约束限制：** 包含1到10000个轮次项。 **取值范围：** 参考OpsTurnInput定义。 **默认取值：** 不涉及。 

        :return: The turns of this OpsAddItemRequest.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTurnInput`]
        """
        return self._turns

    @turns.setter
    def turns(self, turns):
        r"""Sets the turns of this OpsAddItemRequest.

        **参数解释：** 构成该数据条目的交互轮次列表。对于单轮问答长度为1，多轮对话包含多个轮次。 **约束限制：** 包含1到10000个轮次项。 **取值范围：** 参考OpsTurnInput定义。 **默认取值：** 不涉及。 

        :param turns: The turns of this OpsAddItemRequest.
        :type turns: list[:class:`huaweicloudsdkagentarts.v1.OpsTurnInput`]
        """
        self._turns = turns

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
        if not isinstance(other, OpsAddItemRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
