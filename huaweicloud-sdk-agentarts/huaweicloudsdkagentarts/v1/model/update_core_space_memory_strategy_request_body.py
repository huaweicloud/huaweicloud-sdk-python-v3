# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreSpaceMemoryStrategyRequestBody:

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
        'steps': 'list[CoreSpaceMemoryStrategyStepRequestBody]'
    }

    attribute_map = {
        'name': 'name',
        'steps': 'steps'
    }

    def __init__(self, name=None, steps=None):
        r"""UpdateCoreSpaceMemoryStrategyRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：**  策略名称，用于标识和区分不同的记忆策略。 **约束限制：**  仅支持字母、数字和中划线。 **取值范围：**  长度1-48字符。 **默认取值：** 不涉及。 
        :type name: str
        :param steps: **参数解释：** 更新已有步骤。 **约束限制：** 数组长度0-20个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type steps: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceMemoryStrategyStepRequestBody`]
        """
        
        

        self._name = None
        self._steps = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.steps = steps

    @property
    def name(self):
        r"""Gets the name of this UpdateCoreSpaceMemoryStrategyRequestBody.

        **参数解释：**  策略名称，用于标识和区分不同的记忆策略。 **约束限制：**  仅支持字母、数字和中划线。 **取值范围：**  长度1-48字符。 **默认取值：** 不涉及。 

        :return: The name of this UpdateCoreSpaceMemoryStrategyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateCoreSpaceMemoryStrategyRequestBody.

        **参数解释：**  策略名称，用于标识和区分不同的记忆策略。 **约束限制：**  仅支持字母、数字和中划线。 **取值范围：**  长度1-48字符。 **默认取值：** 不涉及。 

        :param name: The name of this UpdateCoreSpaceMemoryStrategyRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def steps(self):
        r"""Gets the steps of this UpdateCoreSpaceMemoryStrategyRequestBody.

        **参数解释：** 更新已有步骤。 **约束限制：** 数组长度0-20个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The steps of this UpdateCoreSpaceMemoryStrategyRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceMemoryStrategyStepRequestBody`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this UpdateCoreSpaceMemoryStrategyRequestBody.

        **参数解释：** 更新已有步骤。 **约束限制：** 数组长度0-20个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param steps: The steps of this UpdateCoreSpaceMemoryStrategyRequestBody.
        :type steps: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceMemoryStrategyStepRequestBody`]
        """
        self._steps = steps

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
        if not isinstance(other, UpdateCoreSpaceMemoryStrategyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
