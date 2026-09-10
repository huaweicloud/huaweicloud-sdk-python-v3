# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsFineGrainedEvaluationData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'items': 'list[list[OpsFineGrainedEvalFieldKV]]',
        'evaluation_object_config': 'OpsFineGrainedEvaluationObjectConfig',
        'agent_output_variable': 'str',
        'trace_ids': 'list[str]'
    }

    attribute_map = {
        'items': 'items',
        'evaluation_object_config': 'evaluation_object_config',
        'agent_output_variable': 'agent_output_variable',
        'trace_ids': 'trace_ids'
    }

    def __init__(self, items=None, evaluation_object_config=None, agent_output_variable=None, trace_ids=None):
        r"""OpsFineGrainedEvaluationData

        The model defined in huaweicloud sdk

        :param items: **参数解释：** 待评估的数据条目列表，scenario&#x3D;dataset和scenario&#x3D;agent时必填。每条数据为键值对列表，字段名和字段数量由评估器Prompt模板决定。 - scenario&#x3D;dataset时，每条需包含评估器Prompt中引用的所有变量对应的字段（如input、actual_output等）。 - scenario&#x3D;agent时，每条需包含输入相关字段（如input），API将调用智能体获取actual_output后自动填充。 **约束限制：** 数组长度1到100。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type items: list[list[OpsFineGrainedEvalFieldKV]]
        :param evaluation_object_config: 
        :type evaluation_object_config: :class:`huaweicloudsdkagentarts.v1.OpsFineGrainedEvaluationObjectConfig`
        :param agent_output_variable: **参数解释：** 评估器中接收智能体输出的变量名，scenario&#x3D;agent时使用。API调用智能体获取输出后，将输出填入该变量名对应的字段中。若不传，默认为actual_output。 **约束限制：** 字符长度1到100。 **取值范围：** 评估器Prompt模板中定义的变量名。 **默认取值：** actual_output。
        :type agent_output_variable: str
        :param trace_ids: **参数解释：** 待评估的TraceId列表，API将根据TraceId从可观测子服务获取对应的trace数据后进行评估，scenario&#x3D;trace时必填。 **约束限制：** 数组长度1到100，每个元素字符长度1到100。TraceId必须在可观测子服务中存在，否则返回TRACE_NOT_FOUND错误。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type trace_ids: list[str]
        """
        
        

        self._items = None
        self._evaluation_object_config = None
        self._agent_output_variable = None
        self._trace_ids = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if evaluation_object_config is not None:
            self.evaluation_object_config = evaluation_object_config
        if agent_output_variable is not None:
            self.agent_output_variable = agent_output_variable
        if trace_ids is not None:
            self.trace_ids = trace_ids

    @property
    def items(self):
        r"""Gets the items of this OpsFineGrainedEvaluationData.

        **参数解释：** 待评估的数据条目列表，scenario=dataset和scenario=agent时必填。每条数据为键值对列表，字段名和字段数量由评估器Prompt模板决定。 - scenario=dataset时，每条需包含评估器Prompt中引用的所有变量对应的字段（如input、actual_output等）。 - scenario=agent时，每条需包含输入相关字段（如input），API将调用智能体获取actual_output后自动填充。 **约束限制：** 数组长度1到100。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The items of this OpsFineGrainedEvaluationData.
        :rtype: list[list[OpsFineGrainedEvalFieldKV]]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this OpsFineGrainedEvaluationData.

        **参数解释：** 待评估的数据条目列表，scenario=dataset和scenario=agent时必填。每条数据为键值对列表，字段名和字段数量由评估器Prompt模板决定。 - scenario=dataset时，每条需包含评估器Prompt中引用的所有变量对应的字段（如input、actual_output等）。 - scenario=agent时，每条需包含输入相关字段（如input），API将调用智能体获取actual_output后自动填充。 **约束限制：** 数组长度1到100。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param items: The items of this OpsFineGrainedEvaluationData.
        :type items: list[list[OpsFineGrainedEvalFieldKV]]
        """
        self._items = items

    @property
    def evaluation_object_config(self):
        r"""Gets the evaluation_object_config of this OpsFineGrainedEvaluationData.

        :return: The evaluation_object_config of this OpsFineGrainedEvaluationData.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsFineGrainedEvaluationObjectConfig`
        """
        return self._evaluation_object_config

    @evaluation_object_config.setter
    def evaluation_object_config(self, evaluation_object_config):
        r"""Sets the evaluation_object_config of this OpsFineGrainedEvaluationData.

        :param evaluation_object_config: The evaluation_object_config of this OpsFineGrainedEvaluationData.
        :type evaluation_object_config: :class:`huaweicloudsdkagentarts.v1.OpsFineGrainedEvaluationObjectConfig`
        """
        self._evaluation_object_config = evaluation_object_config

    @property
    def agent_output_variable(self):
        r"""Gets the agent_output_variable of this OpsFineGrainedEvaluationData.

        **参数解释：** 评估器中接收智能体输出的变量名，scenario=agent时使用。API调用智能体获取输出后，将输出填入该变量名对应的字段中。若不传，默认为actual_output。 **约束限制：** 字符长度1到100。 **取值范围：** 评估器Prompt模板中定义的变量名。 **默认取值：** actual_output。

        :return: The agent_output_variable of this OpsFineGrainedEvaluationData.
        :rtype: str
        """
        return self._agent_output_variable

    @agent_output_variable.setter
    def agent_output_variable(self, agent_output_variable):
        r"""Sets the agent_output_variable of this OpsFineGrainedEvaluationData.

        **参数解释：** 评估器中接收智能体输出的变量名，scenario=agent时使用。API调用智能体获取输出后，将输出填入该变量名对应的字段中。若不传，默认为actual_output。 **约束限制：** 字符长度1到100。 **取值范围：** 评估器Prompt模板中定义的变量名。 **默认取值：** actual_output。

        :param agent_output_variable: The agent_output_variable of this OpsFineGrainedEvaluationData.
        :type agent_output_variable: str
        """
        self._agent_output_variable = agent_output_variable

    @property
    def trace_ids(self):
        r"""Gets the trace_ids of this OpsFineGrainedEvaluationData.

        **参数解释：** 待评估的TraceId列表，API将根据TraceId从可观测子服务获取对应的trace数据后进行评估，scenario=trace时必填。 **约束限制：** 数组长度1到100，每个元素字符长度1到100。TraceId必须在可观测子服务中存在，否则返回TRACE_NOT_FOUND错误。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The trace_ids of this OpsFineGrainedEvaluationData.
        :rtype: list[str]
        """
        return self._trace_ids

    @trace_ids.setter
    def trace_ids(self, trace_ids):
        r"""Sets the trace_ids of this OpsFineGrainedEvaluationData.

        **参数解释：** 待评估的TraceId列表，API将根据TraceId从可观测子服务获取对应的trace数据后进行评估，scenario=trace时必填。 **约束限制：** 数组长度1到100，每个元素字符长度1到100。TraceId必须在可观测子服务中存在，否则返回TRACE_NOT_FOUND错误。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param trace_ids: The trace_ids of this OpsFineGrainedEvaluationData.
        :type trace_ids: list[str]
        """
        self._trace_ids = trace_ids

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
        if not isinstance(other, OpsFineGrainedEvaluationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
