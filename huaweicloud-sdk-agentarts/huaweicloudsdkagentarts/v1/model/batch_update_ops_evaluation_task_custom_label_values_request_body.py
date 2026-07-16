# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateOpsEvaluationTaskCustomLabelValuesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'records': 'list[UpdateOpsEvaluationTaskCustomLabelValuesRequestBody]'
    }

    attribute_map = {
        'records': 'records'
    }

    def __init__(self, records=None):
        r"""BatchUpdateOpsEvaluationTaskCustomLabelValuesRequestBody

        The model defined in huaweicloud sdk

        :param records: **参数解释：** 待批量更新的评估任务自定义标签值记录列表。 **约束限制：** 数组长度为0到100。 **取值范围：** 参考UpdateOpsEvaluationTaskCustomLabelValuesRequestBody定义。 **默认取值：** 不涉及。 
        :type records: list[:class:`huaweicloudsdkagentarts.v1.UpdateOpsEvaluationTaskCustomLabelValuesRequestBody`]
        """
        
        

        self._records = None
        self.discriminator = None

        self.records = records

    @property
    def records(self):
        r"""Gets the records of this BatchUpdateOpsEvaluationTaskCustomLabelValuesRequestBody.

        **参数解释：** 待批量更新的评估任务自定义标签值记录列表。 **约束限制：** 数组长度为0到100。 **取值范围：** 参考UpdateOpsEvaluationTaskCustomLabelValuesRequestBody定义。 **默认取值：** 不涉及。 

        :return: The records of this BatchUpdateOpsEvaluationTaskCustomLabelValuesRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.UpdateOpsEvaluationTaskCustomLabelValuesRequestBody`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this BatchUpdateOpsEvaluationTaskCustomLabelValuesRequestBody.

        **参数解释：** 待批量更新的评估任务自定义标签值记录列表。 **约束限制：** 数组长度为0到100。 **取值范围：** 参考UpdateOpsEvaluationTaskCustomLabelValuesRequestBody定义。 **默认取值：** 不涉及。 

        :param records: The records of this BatchUpdateOpsEvaluationTaskCustomLabelValuesRequestBody.
        :type records: list[:class:`huaweicloudsdkagentarts.v1.UpdateOpsEvaluationTaskCustomLabelValuesRequestBody`]
        """
        self._records = records

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
        if not isinstance(other, BatchUpdateOpsEvaluationTaskCustomLabelValuesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
