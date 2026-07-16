# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOpsEvaluationTaskResultRequestBodyCorrection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reason': 'str',
        'score': 'str'
    }

    attribute_map = {
        'reason': 'reason',
        'score': 'score'
    }

    def __init__(self, reason=None, score=None):
        r"""UpdateOpsEvaluationTaskResultRequestBodyCorrection

        The model defined in huaweicloud sdk

        :param reason: **参数解释：** 校正评估结果的具体原因说明。 **约束限制：** 长度为1到 2000个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type reason: str
        :param score: **参数解释：** 校正后的新评估分数。 **约束限制：** 固定长度为3个字符。 **取值范围：** 0到1之间的数字字符串，保留1位小数（如 \&quot;1.0\&quot;, \&quot;0.5\&quot;）。 **默认取值：** 不涉及。 
        :type score: str
        """
        
        

        self._reason = None
        self._score = None
        self.discriminator = None

        self.reason = reason
        self.score = score

    @property
    def reason(self):
        r"""Gets the reason of this UpdateOpsEvaluationTaskResultRequestBodyCorrection.

        **参数解释：** 校正评估结果的具体原因说明。 **约束限制：** 长度为1到 2000个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The reason of this UpdateOpsEvaluationTaskResultRequestBodyCorrection.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this UpdateOpsEvaluationTaskResultRequestBodyCorrection.

        **参数解释：** 校正评估结果的具体原因说明。 **约束限制：** 长度为1到 2000个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param reason: The reason of this UpdateOpsEvaluationTaskResultRequestBodyCorrection.
        :type reason: str
        """
        self._reason = reason

    @property
    def score(self):
        r"""Gets the score of this UpdateOpsEvaluationTaskResultRequestBodyCorrection.

        **参数解释：** 校正后的新评估分数。 **约束限制：** 固定长度为3个字符。 **取值范围：** 0到1之间的数字字符串，保留1位小数（如 \"1.0\", \"0.5\"）。 **默认取值：** 不涉及。 

        :return: The score of this UpdateOpsEvaluationTaskResultRequestBodyCorrection.
        :rtype: str
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this UpdateOpsEvaluationTaskResultRequestBodyCorrection.

        **参数解释：** 校正后的新评估分数。 **约束限制：** 固定长度为3个字符。 **取值范围：** 0到1之间的数字字符串，保留1位小数（如 \"1.0\", \"0.5\"）。 **默认取值：** 不涉及。 

        :param score: The score of this UpdateOpsEvaluationTaskResultRequestBodyCorrection.
        :type score: str
        """
        self._score = score

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
        if not isinstance(other, UpdateOpsEvaluationTaskResultRequestBodyCorrection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
