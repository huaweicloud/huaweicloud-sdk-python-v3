# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishOpsEvaluatorVersionRequest:

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
        'body': 'CreateOpsEvaluatorRequestBody'
    }

    attribute_map = {
        'evaluator_id': 'evaluator_id',
        'body': 'body'
    }

    def __init__(self, evaluator_id=None, body=None):
        r"""PublishOpsEvaluatorVersionRequest

        The model defined in huaweicloud sdk

        :param evaluator_id: **参数解释：** 评估器的唯一标识符（ID）。该参数用于在路径中指定需要发布新版本的特定评估器。 **约束限制：** 长度为1到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type evaluator_id: str
        :param body: Body of the PublishOpsEvaluatorVersionRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.CreateOpsEvaluatorRequestBody`
        """
        
        

        self._evaluator_id = None
        self._body = None
        self.discriminator = None

        self.evaluator_id = evaluator_id
        if body is not None:
            self.body = body

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this PublishOpsEvaluatorVersionRequest.

        **参数解释：** 评估器的唯一标识符（ID）。该参数用于在路径中指定需要发布新版本的特定评估器。 **约束限制：** 长度为1到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The evaluator_id of this PublishOpsEvaluatorVersionRequest.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this PublishOpsEvaluatorVersionRequest.

        **参数解释：** 评估器的唯一标识符（ID）。该参数用于在路径中指定需要发布新版本的特定评估器。 **约束限制：** 长度为1到100个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param evaluator_id: The evaluator_id of this PublishOpsEvaluatorVersionRequest.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def body(self):
        r"""Gets the body of this PublishOpsEvaluatorVersionRequest.

        :return: The body of this PublishOpsEvaluatorVersionRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateOpsEvaluatorRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this PublishOpsEvaluatorVersionRequest.

        :param body: The body of this PublishOpsEvaluatorVersionRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.CreateOpsEvaluatorRequestBody`
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
        if not isinstance(other, PublishOpsEvaluatorVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
