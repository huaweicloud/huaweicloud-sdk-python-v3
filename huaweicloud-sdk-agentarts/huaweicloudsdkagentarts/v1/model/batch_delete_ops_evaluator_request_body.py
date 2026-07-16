# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteOpsEvaluatorRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_ids': 'list[str]'
    }

    attribute_map = {
        'evaluator_ids': 'evaluator_ids'
    }

    def __init__(self, evaluator_ids=None):
        r"""BatchDeleteOpsEvaluatorRequestBody

        The model defined in huaweicloud sdk

        :param evaluator_ids: **参数解释：** 待批量删除的评估器唯一标识符列表。 **约束限制：** 数组长度0到10000。 **取值范围：** 每个ID为长度不超过 100 字符的字符串。 **默认取值：** 不涉及。 
        :type evaluator_ids: list[str]
        """
        
        

        self._evaluator_ids = None
        self.discriminator = None

        if evaluator_ids is not None:
            self.evaluator_ids = evaluator_ids

    @property
    def evaluator_ids(self):
        r"""Gets the evaluator_ids of this BatchDeleteOpsEvaluatorRequestBody.

        **参数解释：** 待批量删除的评估器唯一标识符列表。 **约束限制：** 数组长度0到10000。 **取值范围：** 每个ID为长度不超过 100 字符的字符串。 **默认取值：** 不涉及。 

        :return: The evaluator_ids of this BatchDeleteOpsEvaluatorRequestBody.
        :rtype: list[str]
        """
        return self._evaluator_ids

    @evaluator_ids.setter
    def evaluator_ids(self, evaluator_ids):
        r"""Sets the evaluator_ids of this BatchDeleteOpsEvaluatorRequestBody.

        **参数解释：** 待批量删除的评估器唯一标识符列表。 **约束限制：** 数组长度0到10000。 **取值范围：** 每个ID为长度不超过 100 字符的字符串。 **默认取值：** 不涉及。 

        :param evaluator_ids: The evaluator_ids of this BatchDeleteOpsEvaluatorRequestBody.
        :type evaluator_ids: list[str]
        """
        self._evaluator_ids = evaluator_ids

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
        if not isinstance(other, BatchDeleteOpsEvaluatorRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
