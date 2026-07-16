# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugOpsEvaluatorRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'turn_type': 'str',
        'llm_config': 'EvaluationOpsLLMConfig'
    }

    attribute_map = {
        'type': 'type',
        'turn_type': 'turn_type',
        'llm_config': 'llm_config'
    }

    def __init__(self, type=None, turn_type=None, llm_config=None):
        r"""DebugOpsEvaluatorRequestBody

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 评估器的调试类型。 **约束限制：** 长度为0到100个字符。 **取值范围：** - llm: 基于大语言模型的调试 - code: 基于代码脚本的调试 **默认取值：** 不涉及。 
        :type type: str
        :param turn_type: **参数解释：** 评估器的轮次类型。 **约束限制：** 长度为0到100个字符。 **取值范围：** - single: 单轮评估器 - multi: 多轮评估器 **默认取值：** 不涉及。 
        :type turn_type: str
        :param llm_config: 
        :type llm_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsLLMConfig`
        """
        
        

        self._type = None
        self._turn_type = None
        self._llm_config = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if turn_type is not None:
            self.turn_type = turn_type
        if llm_config is not None:
            self.llm_config = llm_config

    @property
    def type(self):
        r"""Gets the type of this DebugOpsEvaluatorRequestBody.

        **参数解释：** 评估器的调试类型。 **约束限制：** 长度为0到100个字符。 **取值范围：** - llm: 基于大语言模型的调试 - code: 基于代码脚本的调试 **默认取值：** 不涉及。 

        :return: The type of this DebugOpsEvaluatorRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DebugOpsEvaluatorRequestBody.

        **参数解释：** 评估器的调试类型。 **约束限制：** 长度为0到100个字符。 **取值范围：** - llm: 基于大语言模型的调试 - code: 基于代码脚本的调试 **默认取值：** 不涉及。 

        :param type: The type of this DebugOpsEvaluatorRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def turn_type(self):
        r"""Gets the turn_type of this DebugOpsEvaluatorRequestBody.

        **参数解释：** 评估器的轮次类型。 **约束限制：** 长度为0到100个字符。 **取值范围：** - single: 单轮评估器 - multi: 多轮评估器 **默认取值：** 不涉及。 

        :return: The turn_type of this DebugOpsEvaluatorRequestBody.
        :rtype: str
        """
        return self._turn_type

    @turn_type.setter
    def turn_type(self, turn_type):
        r"""Sets the turn_type of this DebugOpsEvaluatorRequestBody.

        **参数解释：** 评估器的轮次类型。 **约束限制：** 长度为0到100个字符。 **取值范围：** - single: 单轮评估器 - multi: 多轮评估器 **默认取值：** 不涉及。 

        :param turn_type: The turn_type of this DebugOpsEvaluatorRequestBody.
        :type turn_type: str
        """
        self._turn_type = turn_type

    @property
    def llm_config(self):
        r"""Gets the llm_config of this DebugOpsEvaluatorRequestBody.

        :return: The llm_config of this DebugOpsEvaluatorRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsLLMConfig`
        """
        return self._llm_config

    @llm_config.setter
    def llm_config(self, llm_config):
        r"""Sets the llm_config of this DebugOpsEvaluatorRequestBody.

        :param llm_config: The llm_config of this DebugOpsEvaluatorRequestBody.
        :type llm_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsLLMConfig`
        """
        self._llm_config = llm_config

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
        if not isinstance(other, DebugOpsEvaluatorRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
