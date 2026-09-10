# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InvokeOpsFineGrainedEvaluationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_id': 'str',
        'body': 'InvokeOpsFineGrainedEvaluationRequestBody'
    }

    attribute_map = {
        'evaluator_id': 'evaluator_id',
        'body': 'body'
    }

    def __init__(self, evaluator_id=None, body=None):
        r"""InvokeOpsFineGrainedEvaluationRequest

        The model defined in huaweicloud sdk

        :param evaluator_id: **参数解释：** 评估器的唯一标识符，用于指定本次评估使用的评估器。 **约束限制：** 字符串类型，长度1到36字符，评估器必须已存在。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。
        :type evaluator_id: str
        :param body: Body of the InvokeOpsFineGrainedEvaluationRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.InvokeOpsFineGrainedEvaluationRequestBody`
        """
        
        

        self._evaluator_id = None
        self._body = None
        self.discriminator = None

        self.evaluator_id = evaluator_id
        if body is not None:
            self.body = body

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this InvokeOpsFineGrainedEvaluationRequest.

        **参数解释：** 评估器的唯一标识符，用于指定本次评估使用的评估器。 **约束限制：** 字符串类型，长度1到36字符，评估器必须已存在。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。

        :return: The evaluator_id of this InvokeOpsFineGrainedEvaluationRequest.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this InvokeOpsFineGrainedEvaluationRequest.

        **参数解释：** 评估器的唯一标识符，用于指定本次评估使用的评估器。 **约束限制：** 字符串类型，长度1到36字符，评估器必须已存在。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。

        :param evaluator_id: The evaluator_id of this InvokeOpsFineGrainedEvaluationRequest.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def body(self):
        r"""Gets the body of this InvokeOpsFineGrainedEvaluationRequest.

        :return: The body of this InvokeOpsFineGrainedEvaluationRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.InvokeOpsFineGrainedEvaluationRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this InvokeOpsFineGrainedEvaluationRequest.

        :param body: The body of this InvokeOpsFineGrainedEvaluationRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.InvokeOpsFineGrainedEvaluationRequestBody`
        """
        self._body = body

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
        if not isinstance(other, InvokeOpsFineGrainedEvaluationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
