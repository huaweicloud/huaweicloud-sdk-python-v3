# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreSpaceMemoryStrategyStepRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step_order': 'int',
        'instruction': 'str'
    }

    attribute_map = {
        'step_order': 'step_order',
        'instruction': 'instruction'
    }

    def __init__(self, step_order=None, instruction=None):
        r"""CoreSpaceMemoryStrategyStepRequestBody

        The model defined in huaweicloud sdk

        :param step_order: **参数解释：** 步骤执行顺序，从 1 开始。 **约束限制：** 不涉及。 **取值范围：** 1-20 **默认取值：** 不涉及。 
        :type step_order: int
        :param instruction: **参数解释：** 步骤指令（Prompt 模板）。 **约束限制：** 长度不超过50000字符。 **取值范围：** 长度0-50000字符。 **默认取值：** 不传使用默认模板。 
        :type instruction: str
        """
        
        

        self._step_order = None
        self._instruction = None
        self.discriminator = None

        self.step_order = step_order
        if instruction is not None:
            self.instruction = instruction

    @property
    def step_order(self):
        r"""Gets the step_order of this CoreSpaceMemoryStrategyStepRequestBody.

        **参数解释：** 步骤执行顺序，从 1 开始。 **约束限制：** 不涉及。 **取值范围：** 1-20 **默认取值：** 不涉及。 

        :return: The step_order of this CoreSpaceMemoryStrategyStepRequestBody.
        :rtype: int
        """
        return self._step_order

    @step_order.setter
    def step_order(self, step_order):
        r"""Sets the step_order of this CoreSpaceMemoryStrategyStepRequestBody.

        **参数解释：** 步骤执行顺序，从 1 开始。 **约束限制：** 不涉及。 **取值范围：** 1-20 **默认取值：** 不涉及。 

        :param step_order: The step_order of this CoreSpaceMemoryStrategyStepRequestBody.
        :type step_order: int
        """
        self._step_order = step_order

    @property
    def instruction(self):
        r"""Gets the instruction of this CoreSpaceMemoryStrategyStepRequestBody.

        **参数解释：** 步骤指令（Prompt 模板）。 **约束限制：** 长度不超过50000字符。 **取值范围：** 长度0-50000字符。 **默认取值：** 不传使用默认模板。 

        :return: The instruction of this CoreSpaceMemoryStrategyStepRequestBody.
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        r"""Sets the instruction of this CoreSpaceMemoryStrategyStepRequestBody.

        **参数解释：** 步骤指令（Prompt 模板）。 **约束限制：** 长度不超过50000字符。 **取值范围：** 长度0-50000字符。 **默认取值：** 不传使用默认模板。 

        :param instruction: The instruction of this CoreSpaceMemoryStrategyStepRequestBody.
        :type instruction: str
        """
        self._instruction = instruction

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
        if not isinstance(other, CoreSpaceMemoryStrategyStepRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
