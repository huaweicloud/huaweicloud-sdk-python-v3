# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTuningRewardRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_name': 'str',
        'weight': 'float',
        'regex': 'str'
    }

    attribute_map = {
        'function_name': 'function_name',
        'weight': 'weight',
        'regex': 'regex'
    }

    def __init__(self, function_name=None, weight=None, regex=None):
        r"""OpsTuningRewardRule

        The model defined in huaweicloud sdk

        :param function_name: **参数解释：** 规则名称，对应具体的奖励计算逻辑。  **约束限制：** 不涉及  **取值范围：** 思维链式奖励think_format_reward，精准匹配奖励exact_match_reward，数值匹配奖励math_correctness_reward。  **默认取值：** 无
        :type function_name: str
        :param weight: **参数解释：** 权重，表示该规则在总奖励中的占比。  **约束限制：** 不涉及  **取值范围：** 0.0到1.0之间的浮点数。  **默认取值：** 无
        :type weight: float
        :param regex: **参数解释：** 正则表达式，用于匹配模型输出的特定格式。  **约束限制：** 不涉及  **取值范围：** 合法的正则表达式字符串。  **默认取值：** 无
        :type regex: str
        """
        
        

        self._function_name = None
        self._weight = None
        self._regex = None
        self.discriminator = None

        self.function_name = function_name
        self.weight = weight
        self.regex = regex

    @property
    def function_name(self):
        r"""Gets the function_name of this OpsTuningRewardRule.

        **参数解释：** 规则名称，对应具体的奖励计算逻辑。  **约束限制：** 不涉及  **取值范围：** 思维链式奖励think_format_reward，精准匹配奖励exact_match_reward，数值匹配奖励math_correctness_reward。  **默认取值：** 无

        :return: The function_name of this OpsTuningRewardRule.
        :rtype: str
        """
        return self._function_name

    @function_name.setter
    def function_name(self, function_name):
        r"""Sets the function_name of this OpsTuningRewardRule.

        **参数解释：** 规则名称，对应具体的奖励计算逻辑。  **约束限制：** 不涉及  **取值范围：** 思维链式奖励think_format_reward，精准匹配奖励exact_match_reward，数值匹配奖励math_correctness_reward。  **默认取值：** 无

        :param function_name: The function_name of this OpsTuningRewardRule.
        :type function_name: str
        """
        self._function_name = function_name

    @property
    def weight(self):
        r"""Gets the weight of this OpsTuningRewardRule.

        **参数解释：** 权重，表示该规则在总奖励中的占比。  **约束限制：** 不涉及  **取值范围：** 0.0到1.0之间的浮点数。  **默认取值：** 无

        :return: The weight of this OpsTuningRewardRule.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this OpsTuningRewardRule.

        **参数解释：** 权重，表示该规则在总奖励中的占比。  **约束限制：** 不涉及  **取值范围：** 0.0到1.0之间的浮点数。  **默认取值：** 无

        :param weight: The weight of this OpsTuningRewardRule.
        :type weight: float
        """
        self._weight = weight

    @property
    def regex(self):
        r"""Gets the regex of this OpsTuningRewardRule.

        **参数解释：** 正则表达式，用于匹配模型输出的特定格式。  **约束限制：** 不涉及  **取值范围：** 合法的正则表达式字符串。  **默认取值：** 无

        :return: The regex of this OpsTuningRewardRule.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        r"""Sets the regex of this OpsTuningRewardRule.

        **参数解释：** 正则表达式，用于匹配模型输出的特定格式。  **约束限制：** 不涉及  **取值范围：** 合法的正则表达式字符串。  **默认取值：** 无

        :param regex: The regex of this OpsTuningRewardRule.
        :type regex: str
        """
        self._regex = regex

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
        if not isinstance(other, OpsTuningRewardRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
