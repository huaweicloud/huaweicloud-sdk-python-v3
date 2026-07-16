# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddOpsEvaluationTaskCustomLabelValuesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'body': 'BatchAddOpsEvaluationTaskCustomLabelValuesRequestBody'
    }

    attribute_map = {
        'task_id': 'task_id',
        'body': 'body'
    }

    def __init__(self, task_id=None, body=None):
        r"""BatchAddOpsEvaluationTaskCustomLabelValuesRequest

        The model defined in huaweicloud sdk

        :param task_id: **参数解释：** 评估任务的唯一标识符（ID）。该ID用于在API路径中精确定位需要操作的目标评估任务。 **约束限制：** 长度为0到100个字符的字符串。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type task_id: str
        :param body: Body of the BatchAddOpsEvaluationTaskCustomLabelValuesRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.BatchAddOpsEvaluationTaskCustomLabelValuesRequestBody`
        """
        
        

        self._task_id = None
        self._body = None
        self.discriminator = None

        self.task_id = task_id
        if body is not None:
            self.body = body

    @property
    def task_id(self):
        r"""Gets the task_id of this BatchAddOpsEvaluationTaskCustomLabelValuesRequest.

        **参数解释：** 评估任务的唯一标识符（ID）。该ID用于在API路径中精确定位需要操作的目标评估任务。 **约束限制：** 长度为0到100个字符的字符串。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The task_id of this BatchAddOpsEvaluationTaskCustomLabelValuesRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this BatchAddOpsEvaluationTaskCustomLabelValuesRequest.

        **参数解释：** 评估任务的唯一标识符（ID）。该ID用于在API路径中精确定位需要操作的目标评估任务。 **约束限制：** 长度为0到100个字符的字符串。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param task_id: The task_id of this BatchAddOpsEvaluationTaskCustomLabelValuesRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def body(self):
        r"""Gets the body of this BatchAddOpsEvaluationTaskCustomLabelValuesRequest.

        :return: The body of this BatchAddOpsEvaluationTaskCustomLabelValuesRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchAddOpsEvaluationTaskCustomLabelValuesRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchAddOpsEvaluationTaskCustomLabelValuesRequest.

        :param body: The body of this BatchAddOpsEvaluationTaskCustomLabelValuesRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.BatchAddOpsEvaluationTaskCustomLabelValuesRequestBody`
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
        if not isinstance(other, BatchAddOpsEvaluationTaskCustomLabelValuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
