# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_type': 'list[int]',
        'turn_type': 'list[str]',
        'evaluator_content_type': 'list[str]',
        'evaluator_objective_type': 'list[str]'
    }

    attribute_map = {
        'evaluator_type': 'evaluator_type',
        'turn_type': 'turn_type',
        'evaluator_content_type': 'evaluator_content_type',
        'evaluator_objective_type': 'evaluator_objective_type'
    }

    def __init__(self, evaluator_type=None, turn_type=None, evaluator_content_type=None, evaluator_objective_type=None):
        r"""ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions

        The model defined in huaweicloud sdk

        :param evaluator_type: **参数解释：** 评估器类型筛选项。  **约束限制：** 至少包含 1 个选项，最多包含 3 个选项。  **取值范围：** - 1: 模型判定 - 2: 代码判定 - 3: 自适应判定  **默认取值：** 不涉及。 
        :type evaluator_type: list[int]
        :param turn_type: **参数解释：** 对话轮次类型筛选项。  **约束限制：** 至少包含 1 个选项，最多包含 2 个选项。  **取值范围：** - single: 单轮对话 - multi: 多轮对话  **默认取值：** 不涉及。 
        :type turn_type: list[str]
        :param evaluator_content_type: **参数解释：** 评估内容类型筛选项。  **约束限制：** 至少包含 1 个选项，最多包含 2 个选项。  **取值范围：** - text: 文本 - trajectory: 轨迹  **默认取值：** 不涉及。 
        :type evaluator_content_type: list[str]
        :param evaluator_objective_type: **参数解释：** 评估目标类型筛选项。  **约束限制：** 至少包含 1 个选项，最多包含 5 个选项。  **取值范围：** - TASK_COMPLETION: 评估任务是否完成 - OUTPUT_QUALITY: 评估输出内容的质量 - SECURITY: 评估内容安全性 - TOOL_INVOCATION: 评估工具调用的合理性 - TRAJECTORY_QUALITY: 评估 Agent 轨迹的质量  **默认取值：** 不涉及。 
        :type evaluator_objective_type: list[str]
        """
        
        

        self._evaluator_type = None
        self._turn_type = None
        self._evaluator_content_type = None
        self._evaluator_objective_type = None
        self.discriminator = None

        self.evaluator_type = evaluator_type
        self.turn_type = turn_type
        self.evaluator_content_type = evaluator_content_type
        self.evaluator_objective_type = evaluator_objective_type

    @property
    def evaluator_type(self):
        r"""Gets the evaluator_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.

        **参数解释：** 评估器类型筛选项。  **约束限制：** 至少包含 1 个选项，最多包含 3 个选项。  **取值范围：** - 1: 模型判定 - 2: 代码判定 - 3: 自适应判定  **默认取值：** 不涉及。 

        :return: The evaluator_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.
        :rtype: list[int]
        """
        return self._evaluator_type

    @evaluator_type.setter
    def evaluator_type(self, evaluator_type):
        r"""Sets the evaluator_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.

        **参数解释：** 评估器类型筛选项。  **约束限制：** 至少包含 1 个选项，最多包含 3 个选项。  **取值范围：** - 1: 模型判定 - 2: 代码判定 - 3: 自适应判定  **默认取值：** 不涉及。 

        :param evaluator_type: The evaluator_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.
        :type evaluator_type: list[int]
        """
        self._evaluator_type = evaluator_type

    @property
    def turn_type(self):
        r"""Gets the turn_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.

        **参数解释：** 对话轮次类型筛选项。  **约束限制：** 至少包含 1 个选项，最多包含 2 个选项。  **取值范围：** - single: 单轮对话 - multi: 多轮对话  **默认取值：** 不涉及。 

        :return: The turn_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.
        :rtype: list[str]
        """
        return self._turn_type

    @turn_type.setter
    def turn_type(self, turn_type):
        r"""Sets the turn_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.

        **参数解释：** 对话轮次类型筛选项。  **约束限制：** 至少包含 1 个选项，最多包含 2 个选项。  **取值范围：** - single: 单轮对话 - multi: 多轮对话  **默认取值：** 不涉及。 

        :param turn_type: The turn_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.
        :type turn_type: list[str]
        """
        self._turn_type = turn_type

    @property
    def evaluator_content_type(self):
        r"""Gets the evaluator_content_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.

        **参数解释：** 评估内容类型筛选项。  **约束限制：** 至少包含 1 个选项，最多包含 2 个选项。  **取值范围：** - text: 文本 - trajectory: 轨迹  **默认取值：** 不涉及。 

        :return: The evaluator_content_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.
        :rtype: list[str]
        """
        return self._evaluator_content_type

    @evaluator_content_type.setter
    def evaluator_content_type(self, evaluator_content_type):
        r"""Sets the evaluator_content_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.

        **参数解释：** 评估内容类型筛选项。  **约束限制：** 至少包含 1 个选项，最多包含 2 个选项。  **取值范围：** - text: 文本 - trajectory: 轨迹  **默认取值：** 不涉及。 

        :param evaluator_content_type: The evaluator_content_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.
        :type evaluator_content_type: list[str]
        """
        self._evaluator_content_type = evaluator_content_type

    @property
    def evaluator_objective_type(self):
        r"""Gets the evaluator_objective_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.

        **参数解释：** 评估目标类型筛选项。  **约束限制：** 至少包含 1 个选项，最多包含 5 个选项。  **取值范围：** - TASK_COMPLETION: 评估任务是否完成 - OUTPUT_QUALITY: 评估输出内容的质量 - SECURITY: 评估内容安全性 - TOOL_INVOCATION: 评估工具调用的合理性 - TRAJECTORY_QUALITY: 评估 Agent 轨迹的质量  **默认取值：** 不涉及。 

        :return: The evaluator_objective_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.
        :rtype: list[str]
        """
        return self._evaluator_objective_type

    @evaluator_objective_type.setter
    def evaluator_objective_type(self, evaluator_objective_type):
        r"""Sets the evaluator_objective_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.

        **参数解释：** 评估目标类型筛选项。  **约束限制：** 至少包含 1 个选项，最多包含 5 个选项。  **取值范围：** - TASK_COMPLETION: 评估任务是否完成 - OUTPUT_QUALITY: 评估输出内容的质量 - SECURITY: 评估内容安全性 - TOOL_INVOCATION: 评估工具调用的合理性 - TRAJECTORY_QUALITY: 评估 Agent 轨迹的质量  **默认取值：** 不涉及。 

        :param evaluator_objective_type: The evaluator_objective_type of this ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions.
        :type evaluator_objective_type: list[str]
        """
        self._evaluator_objective_type = evaluator_objective_type

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
        if not isinstance(other, ListOpsEvaluatorFilterOptionsResponseBodyFilterOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
