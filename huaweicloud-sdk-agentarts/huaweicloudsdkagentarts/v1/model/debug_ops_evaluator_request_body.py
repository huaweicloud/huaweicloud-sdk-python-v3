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
        'llm_config': 'EvaluationOpsLLMConfig',
        'evaluator_content_type': 'str',
        'evaluator_id': 'str',
        'evaluator_version': 'str',
        'geval_config': 'DebugOpsEvaluatorRequestBodyGevalConfig'
    }

    attribute_map = {
        'type': 'type',
        'turn_type': 'turn_type',
        'llm_config': 'llm_config',
        'evaluator_content_type': 'evaluator_content_type',
        'evaluator_id': 'evaluator_id',
        'evaluator_version': 'evaluator_version',
        'geval_config': 'geval_config'
    }

    def __init__(self, type=None, turn_type=None, llm_config=None, evaluator_content_type=None, evaluator_id=None, evaluator_version=None, geval_config=None):
        r"""DebugOpsEvaluatorRequestBody

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 评估器的调试类型。 **约束限制：** 长度为0到100个字符。 **取值范围：** - llm: 基于大语言模型的调试 - code: 基于代码脚本的调试 **默认取值：** 不涉及。 
        :type type: str
        :param turn_type: **参数解释：** 评估器的轮次类型。 **约束限制：** 长度为0到100个字符。 **取值范围：** - single: 单轮评估器 - multi: 多轮评估器 **默认取值：** 不涉及。 
        :type turn_type: str
        :param llm_config: 
        :type llm_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsLLMConfig`
        :param evaluator_content_type: **参数解释：** 评估器的内容类型。 **约束限制：** 不涉及。 **取值范围：** - text：文本 - trajectory：轨迹 **默认取值：** 不涉及。 
        :type evaluator_content_type: str
        :param evaluator_id: **参数解释：** 待调试评估器的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。不传时表示纯调试模式，不关联已保存的评估器；传值时调试完成后可直接关联该评估器。 
        :type evaluator_id: str
        :param evaluator_version: **参数解释：** 待调试评估器的版本号。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。不传时使用该评估器的最新版本；传值时调试指定的评估器版本。 
        :type evaluator_version: str
        :param geval_config: 
        :type geval_config: :class:`huaweicloudsdkagentarts.v1.DebugOpsEvaluatorRequestBodyGevalConfig`
        """
        
        

        self._type = None
        self._turn_type = None
        self._llm_config = None
        self._evaluator_content_type = None
        self._evaluator_id = None
        self._evaluator_version = None
        self._geval_config = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if turn_type is not None:
            self.turn_type = turn_type
        if llm_config is not None:
            self.llm_config = llm_config
        if evaluator_content_type is not None:
            self.evaluator_content_type = evaluator_content_type
        if evaluator_id is not None:
            self.evaluator_id = evaluator_id
        if evaluator_version is not None:
            self.evaluator_version = evaluator_version
        if geval_config is not None:
            self.geval_config = geval_config

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

    @property
    def evaluator_content_type(self):
        r"""Gets the evaluator_content_type of this DebugOpsEvaluatorRequestBody.

        **参数解释：** 评估器的内容类型。 **约束限制：** 不涉及。 **取值范围：** - text：文本 - trajectory：轨迹 **默认取值：** 不涉及。 

        :return: The evaluator_content_type of this DebugOpsEvaluatorRequestBody.
        :rtype: str
        """
        return self._evaluator_content_type

    @evaluator_content_type.setter
    def evaluator_content_type(self, evaluator_content_type):
        r"""Sets the evaluator_content_type of this DebugOpsEvaluatorRequestBody.

        **参数解释：** 评估器的内容类型。 **约束限制：** 不涉及。 **取值范围：** - text：文本 - trajectory：轨迹 **默认取值：** 不涉及。 

        :param evaluator_content_type: The evaluator_content_type of this DebugOpsEvaluatorRequestBody.
        :type evaluator_content_type: str
        """
        self._evaluator_content_type = evaluator_content_type

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this DebugOpsEvaluatorRequestBody.

        **参数解释：** 待调试评估器的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。不传时表示纯调试模式，不关联已保存的评估器；传值时调试完成后可直接关联该评估器。 

        :return: The evaluator_id of this DebugOpsEvaluatorRequestBody.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this DebugOpsEvaluatorRequestBody.

        **参数解释：** 待调试评估器的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。不传时表示纯调试模式，不关联已保存的评估器；传值时调试完成后可直接关联该评估器。 

        :param evaluator_id: The evaluator_id of this DebugOpsEvaluatorRequestBody.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def evaluator_version(self):
        r"""Gets the evaluator_version of this DebugOpsEvaluatorRequestBody.

        **参数解释：** 待调试评估器的版本号。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。不传时使用该评估器的最新版本；传值时调试指定的评估器版本。 

        :return: The evaluator_version of this DebugOpsEvaluatorRequestBody.
        :rtype: str
        """
        return self._evaluator_version

    @evaluator_version.setter
    def evaluator_version(self, evaluator_version):
        r"""Sets the evaluator_version of this DebugOpsEvaluatorRequestBody.

        **参数解释：** 待调试评估器的版本号。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。不传时使用该评估器的最新版本；传值时调试指定的评估器版本。 

        :param evaluator_version: The evaluator_version of this DebugOpsEvaluatorRequestBody.
        :type evaluator_version: str
        """
        self._evaluator_version = evaluator_version

    @property
    def geval_config(self):
        r"""Gets the geval_config of this DebugOpsEvaluatorRequestBody.

        :return: The geval_config of this DebugOpsEvaluatorRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.DebugOpsEvaluatorRequestBodyGevalConfig`
        """
        return self._geval_config

    @geval_config.setter
    def geval_config(self, geval_config):
        r"""Sets the geval_config of this DebugOpsEvaluatorRequestBody.

        :param geval_config: The geval_config of this DebugOpsEvaluatorRequestBody.
        :type geval_config: :class:`huaweicloudsdkagentarts.v1.DebugOpsEvaluatorRequestBodyGevalConfig`
        """
        self._geval_config = geval_config

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
