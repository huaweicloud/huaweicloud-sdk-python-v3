# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugOpsEvaluatorRequestBodyGevalConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'criteria': 'str',
        'evaluation_steps': 'list[str]',
        'rubric': 'list[DebugOpsEvaluatorRequestBodyGevalConfigRubric]',
        'model_config': 'EvaluationOpsLLMConfig'
    }

    attribute_map = {
        'criteria': 'criteria',
        'evaluation_steps': 'evaluation_steps',
        'rubric': 'rubric',
        'model_config': 'model_config'
    }

    def __init__(self, criteria=None, evaluation_steps=None, rubric=None, model_config=None):
        r"""DebugOpsEvaluatorRequestBodyGevalConfig

        The model defined in huaweicloud sdk

        :param criteria: **参数解释：** 评估标准，描述大模型对输出进行评分的依据。 **约束限制：** 必填；去除首尾空格后长度不能超过20000字符；必须至少包含一个 {{variable}} 格式的模板变量，模板变量会在评估时被 test_case 中的值替换。 **取值范围：** 1~20000字符，且必须包含至少一个 {{变量名}} 占位符。 **默认取值：** 不涉及。 
        :type criteria: str
        :param evaluation_steps: **参数解释：** 评估步骤，指导大模型按步骤进行评估打分，可省略。 **约束限制：** 可选；数量不能超过10个；每个步骤去除首尾空格后长度需在1~200字符之间，不能为空。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type evaluation_steps: list[str]
        :param rubric: **参数解释：** 评分细则，定义各分数档位对应的参考输出描述，供大模型打分时作为锚点，可省略。 **约束限制：** 可选；数量不能超过10个；score必须在0~1之间且不能重复；reference_outcome去除首尾空格后长度需在1~200字符之间，不能为空。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type rubric: list[:class:`huaweicloudsdkagentarts.v1.DebugOpsEvaluatorRequestBodyGevalConfigRubric`]
        :param model_config: 
        :type model_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsLLMConfig`
        """
        
        

        self._criteria = None
        self._evaluation_steps = None
        self._rubric = None
        self._model_config = None
        self.discriminator = None

        self.criteria = criteria
        if evaluation_steps is not None:
            self.evaluation_steps = evaluation_steps
        if rubric is not None:
            self.rubric = rubric
        self.model_config = model_config

    @property
    def criteria(self):
        r"""Gets the criteria of this DebugOpsEvaluatorRequestBodyGevalConfig.

        **参数解释：** 评估标准，描述大模型对输出进行评分的依据。 **约束限制：** 必填；去除首尾空格后长度不能超过20000字符；必须至少包含一个 {{variable}} 格式的模板变量，模板变量会在评估时被 test_case 中的值替换。 **取值范围：** 1~20000字符，且必须包含至少一个 {{变量名}} 占位符。 **默认取值：** 不涉及。 

        :return: The criteria of this DebugOpsEvaluatorRequestBodyGevalConfig.
        :rtype: str
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        r"""Sets the criteria of this DebugOpsEvaluatorRequestBodyGevalConfig.

        **参数解释：** 评估标准，描述大模型对输出进行评分的依据。 **约束限制：** 必填；去除首尾空格后长度不能超过20000字符；必须至少包含一个 {{variable}} 格式的模板变量，模板变量会在评估时被 test_case 中的值替换。 **取值范围：** 1~20000字符，且必须包含至少一个 {{变量名}} 占位符。 **默认取值：** 不涉及。 

        :param criteria: The criteria of this DebugOpsEvaluatorRequestBodyGevalConfig.
        :type criteria: str
        """
        self._criteria = criteria

    @property
    def evaluation_steps(self):
        r"""Gets the evaluation_steps of this DebugOpsEvaluatorRequestBodyGevalConfig.

        **参数解释：** 评估步骤，指导大模型按步骤进行评估打分，可省略。 **约束限制：** 可选；数量不能超过10个；每个步骤去除首尾空格后长度需在1~200字符之间，不能为空。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The evaluation_steps of this DebugOpsEvaluatorRequestBodyGevalConfig.
        :rtype: list[str]
        """
        return self._evaluation_steps

    @evaluation_steps.setter
    def evaluation_steps(self, evaluation_steps):
        r"""Sets the evaluation_steps of this DebugOpsEvaluatorRequestBodyGevalConfig.

        **参数解释：** 评估步骤，指导大模型按步骤进行评估打分，可省略。 **约束限制：** 可选；数量不能超过10个；每个步骤去除首尾空格后长度需在1~200字符之间，不能为空。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param evaluation_steps: The evaluation_steps of this DebugOpsEvaluatorRequestBodyGevalConfig.
        :type evaluation_steps: list[str]
        """
        self._evaluation_steps = evaluation_steps

    @property
    def rubric(self):
        r"""Gets the rubric of this DebugOpsEvaluatorRequestBodyGevalConfig.

        **参数解释：** 评分细则，定义各分数档位对应的参考输出描述，供大模型打分时作为锚点，可省略。 **约束限制：** 可选；数量不能超过10个；score必须在0~1之间且不能重复；reference_outcome去除首尾空格后长度需在1~200字符之间，不能为空。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The rubric of this DebugOpsEvaluatorRequestBodyGevalConfig.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.DebugOpsEvaluatorRequestBodyGevalConfigRubric`]
        """
        return self._rubric

    @rubric.setter
    def rubric(self, rubric):
        r"""Sets the rubric of this DebugOpsEvaluatorRequestBodyGevalConfig.

        **参数解释：** 评分细则，定义各分数档位对应的参考输出描述，供大模型打分时作为锚点，可省略。 **约束限制：** 可选；数量不能超过10个；score必须在0~1之间且不能重复；reference_outcome去除首尾空格后长度需在1~200字符之间，不能为空。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param rubric: The rubric of this DebugOpsEvaluatorRequestBodyGevalConfig.
        :type rubric: list[:class:`huaweicloudsdkagentarts.v1.DebugOpsEvaluatorRequestBodyGevalConfigRubric`]
        """
        self._rubric = rubric

    @property
    def model_config(self):
        r"""Gets the model_config of this DebugOpsEvaluatorRequestBodyGevalConfig.

        :return: The model_config of this DebugOpsEvaluatorRequestBodyGevalConfig.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsLLMConfig`
        """
        return self._model_config

    @model_config.setter
    def model_config(self, model_config):
        r"""Sets the model_config of this DebugOpsEvaluatorRequestBodyGevalConfig.

        :param model_config: The model_config of this DebugOpsEvaluatorRequestBodyGevalConfig.
        :type model_config: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsLLMConfig`
        """
        self._model_config = model_config

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
        if not isinstance(other, DebugOpsEvaluatorRequestBodyGevalConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
