# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOpsDatasetItemRequestBody:

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
        r"""UpdateOpsDatasetItemRequestBody

        The model defined in huaweicloud sdk

        :param turns: **参数解释：** 待更新的多轮对话或业务数据内容。 **约束限制：** 必填参数；数组长度限制 1 到 10000。 **取值范围：** 符合 OpsTurnInput 结构的对象数组。 **默认取值：** 不涉及。 
        :type turns: list[:class:`huaweicloudsdkagentarts.v1.OpsTurnInput`]
        """
        
        

        self._turns = None
        self.discriminator = None

        self.turns = turns

    @property
    def turns(self):
        r"""Gets the turns of this UpdateOpsDatasetItemRequestBody.

        **参数解释：** 待更新的多轮对话或业务数据内容。 **约束限制：** 必填参数；数组长度限制 1 到 10000。 **取值范围：** 符合 OpsTurnInput 结构的对象数组。 **默认取值：** 不涉及。 

        :return: The turns of this UpdateOpsDatasetItemRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTurnInput`]
        """
        return self._turns

    @turns.setter
    def turns(self, turns):
        r"""Sets the turns of this UpdateOpsDatasetItemRequestBody.

        **参数解释：** 待更新的多轮对话或业务数据内容。 **约束限制：** 必填参数；数组长度限制 1 到 10000。 **取值范围：** 符合 OpsTurnInput 结构的对象数组。 **默认取值：** 不涉及。 

        :param turns: The turns of this UpdateOpsDatasetItemRequestBody.
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
        if not isinstance(other, UpdateOpsDatasetItemRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
