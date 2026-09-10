# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InvokeOpsFineGrainedEvaluationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scenario': 'str',
        'evaluator_version': 'str',
        'data': 'OpsFineGrainedEvaluationData',
        'stream': 'bool'
    }

    attribute_map = {
        'scenario': 'scenario',
        'evaluator_version': 'evaluator_version',
        'data': 'data',
        'stream': 'stream'
    }

    def __init__(self, scenario=None, evaluator_version=None, data=None, stream=None):
        r"""InvokeOpsFineGrainedEvaluationRequestBody

        The model defined in huaweicloud sdk

        :param scenario: **参数解释：** 评估场景，指定本次评估的数据来源和处理方式。 **约束限制：** 必须为枚举值之一。 **取值范围：** - dataset：评测集评估，直接传入输入输出数据进行评估。 - agent：智能体调用评估，传入输入调用智能体获取输出后进行评估。 - trace：Trace评估，传入TraceId从可观测子服务获取trace数据后进行评估。 **默认取值：** 不涉及。
        :type scenario: str
        :param evaluator_version: **参数解释：** 评估器的版本号，用于指定使用评估器的特定版本。 **约束限制：** 字符串类型，最大长度36。 **取值范围：** 系统内有效的评估器版本号。 **默认取值：** 评估器最新版本。
        :type evaluator_version: str
        :param data: 
        :type data: :class:`huaweicloudsdkagentarts.v1.OpsFineGrainedEvaluationData`
        :param stream: **参数解释：** 是否启用流式返回。启用后，评估结果通过SSE（Server-Sent Events）协议逐步推送，调用方可实时获取评估进度和结果。 **约束限制：** 不涉及。 **取值范围：** true（流式返回）、false（非流式返回，等待全部评估完成后一次性返回JSON结果）。 **默认取值：** true。
        :type stream: bool
        """
        
        

        self._scenario = None
        self._evaluator_version = None
        self._data = None
        self._stream = None
        self.discriminator = None

        self.scenario = scenario
        self.evaluator_version = evaluator_version
        self.data = data
        if stream is not None:
            self.stream = stream

    @property
    def scenario(self):
        r"""Gets the scenario of this InvokeOpsFineGrainedEvaluationRequestBody.

        **参数解释：** 评估场景，指定本次评估的数据来源和处理方式。 **约束限制：** 必须为枚举值之一。 **取值范围：** - dataset：评测集评估，直接传入输入输出数据进行评估。 - agent：智能体调用评估，传入输入调用智能体获取输出后进行评估。 - trace：Trace评估，传入TraceId从可观测子服务获取trace数据后进行评估。 **默认取值：** 不涉及。

        :return: The scenario of this InvokeOpsFineGrainedEvaluationRequestBody.
        :rtype: str
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        r"""Sets the scenario of this InvokeOpsFineGrainedEvaluationRequestBody.

        **参数解释：** 评估场景，指定本次评估的数据来源和处理方式。 **约束限制：** 必须为枚举值之一。 **取值范围：** - dataset：评测集评估，直接传入输入输出数据进行评估。 - agent：智能体调用评估，传入输入调用智能体获取输出后进行评估。 - trace：Trace评估，传入TraceId从可观测子服务获取trace数据后进行评估。 **默认取值：** 不涉及。

        :param scenario: The scenario of this InvokeOpsFineGrainedEvaluationRequestBody.
        :type scenario: str
        """
        self._scenario = scenario

    @property
    def evaluator_version(self):
        r"""Gets the evaluator_version of this InvokeOpsFineGrainedEvaluationRequestBody.

        **参数解释：** 评估器的版本号，用于指定使用评估器的特定版本。 **约束限制：** 字符串类型，最大长度36。 **取值范围：** 系统内有效的评估器版本号。 **默认取值：** 评估器最新版本。

        :return: The evaluator_version of this InvokeOpsFineGrainedEvaluationRequestBody.
        :rtype: str
        """
        return self._evaluator_version

    @evaluator_version.setter
    def evaluator_version(self, evaluator_version):
        r"""Sets the evaluator_version of this InvokeOpsFineGrainedEvaluationRequestBody.

        **参数解释：** 评估器的版本号，用于指定使用评估器的特定版本。 **约束限制：** 字符串类型，最大长度36。 **取值范围：** 系统内有效的评估器版本号。 **默认取值：** 评估器最新版本。

        :param evaluator_version: The evaluator_version of this InvokeOpsFineGrainedEvaluationRequestBody.
        :type evaluator_version: str
        """
        self._evaluator_version = evaluator_version

    @property
    def data(self):
        r"""Gets the data of this InvokeOpsFineGrainedEvaluationRequestBody.

        :return: The data of this InvokeOpsFineGrainedEvaluationRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsFineGrainedEvaluationData`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this InvokeOpsFineGrainedEvaluationRequestBody.

        :param data: The data of this InvokeOpsFineGrainedEvaluationRequestBody.
        :type data: :class:`huaweicloudsdkagentarts.v1.OpsFineGrainedEvaluationData`
        """
        self._data = data

    @property
    def stream(self):
        r"""Gets the stream of this InvokeOpsFineGrainedEvaluationRequestBody.

        **参数解释：** 是否启用流式返回。启用后，评估结果通过SSE（Server-Sent Events）协议逐步推送，调用方可实时获取评估进度和结果。 **约束限制：** 不涉及。 **取值范围：** true（流式返回）、false（非流式返回，等待全部评估完成后一次性返回JSON结果）。 **默认取值：** true。

        :return: The stream of this InvokeOpsFineGrainedEvaluationRequestBody.
        :rtype: bool
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this InvokeOpsFineGrainedEvaluationRequestBody.

        **参数解释：** 是否启用流式返回。启用后，评估结果通过SSE（Server-Sent Events）协议逐步推送，调用方可实时获取评估进度和结果。 **约束限制：** 不涉及。 **取值范围：** true（流式返回）、false（非流式返回，等待全部评估完成后一次性返回JSON结果）。 **默认取值：** true。

        :param stream: The stream of this InvokeOpsFineGrainedEvaluationRequestBody.
        :type stream: bool
        """
        self._stream = stream

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
        if not isinstance(other, InvokeOpsFineGrainedEvaluationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
