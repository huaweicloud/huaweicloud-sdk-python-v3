# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugOpsEvaluatorRequestBodyGevalConfigRubric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'score': 'float',
        'reference_outcome': 'str'
    }

    attribute_map = {
        'score': 'score',
        'reference_outcome': 'reference_outcome'
    }

    def __init__(self, score=None, reference_outcome=None):
        r"""DebugOpsEvaluatorRequestBodyGevalConfigRubric

        The model defined in huaweicloud sdk

        :param score: **参数解释：** 该档位对应的评估得分。 **约束限制：** 必须为0~1之间的数值，且不能与其他档位的score重复。 **取值范围：** 0~1（闭区间）。 **默认取值：** 不涉及。 
        :type score: float
        :param reference_outcome: **参数解释：** 该分数档位对应的参考输出描述，作为大模型评分的锚点文本。 **约束限制：** 必填；去除首尾空格后长度需在1~200字符之间，不能为空或纯空白。 **取值范围：** 1~200字符。 **默认取值：** 不涉及。 
        :type reference_outcome: str
        """
        
        

        self._score = None
        self._reference_outcome = None
        self.discriminator = None

        self.score = score
        self.reference_outcome = reference_outcome

    @property
    def score(self):
        r"""Gets the score of this DebugOpsEvaluatorRequestBodyGevalConfigRubric.

        **参数解释：** 该档位对应的评估得分。 **约束限制：** 必须为0~1之间的数值，且不能与其他档位的score重复。 **取值范围：** 0~1（闭区间）。 **默认取值：** 不涉及。 

        :return: The score of this DebugOpsEvaluatorRequestBodyGevalConfigRubric.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this DebugOpsEvaluatorRequestBodyGevalConfigRubric.

        **参数解释：** 该档位对应的评估得分。 **约束限制：** 必须为0~1之间的数值，且不能与其他档位的score重复。 **取值范围：** 0~1（闭区间）。 **默认取值：** 不涉及。 

        :param score: The score of this DebugOpsEvaluatorRequestBodyGevalConfigRubric.
        :type score: float
        """
        self._score = score

    @property
    def reference_outcome(self):
        r"""Gets the reference_outcome of this DebugOpsEvaluatorRequestBodyGevalConfigRubric.

        **参数解释：** 该分数档位对应的参考输出描述，作为大模型评分的锚点文本。 **约束限制：** 必填；去除首尾空格后长度需在1~200字符之间，不能为空或纯空白。 **取值范围：** 1~200字符。 **默认取值：** 不涉及。 

        :return: The reference_outcome of this DebugOpsEvaluatorRequestBodyGevalConfigRubric.
        :rtype: str
        """
        return self._reference_outcome

    @reference_outcome.setter
    def reference_outcome(self, reference_outcome):
        r"""Sets the reference_outcome of this DebugOpsEvaluatorRequestBodyGevalConfigRubric.

        **参数解释：** 该分数档位对应的参考输出描述，作为大模型评分的锚点文本。 **约束限制：** 必填；去除首尾空格后长度需在1~200字符之间，不能为空或纯空白。 **取值范围：** 1~200字符。 **默认取值：** 不涉及。 

        :param reference_outcome: The reference_outcome of this DebugOpsEvaluatorRequestBodyGevalConfigRubric.
        :type reference_outcome: str
        """
        self._reference_outcome = reference_outcome

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
        if not isinstance(other, DebugOpsEvaluatorRequestBodyGevalConfigRubric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
