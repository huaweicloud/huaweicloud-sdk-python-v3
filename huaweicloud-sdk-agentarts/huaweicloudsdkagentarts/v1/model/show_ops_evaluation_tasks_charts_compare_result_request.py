# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluationTasksChartsCompareResultRequest:

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
        'task_ids': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_ids': 'task_ids'
    }

    def __init__(self, task_id=None, task_ids=None):
        r"""ShowOpsEvaluationTasksChartsCompareResultRequest

        The model defined in huaweicloud sdk

        :param task_id: **参数解释：** 基线评估任务的唯一标识符（ID）。 **约束限制：** 字符长度在0到100之间。 **取值范围：** 长度为0到100个字符的字符串。 **默认取值：** 不涉及。
        :type task_id: str
        :param task_ids: **参数解释：** 基线评估任务的唯一标识符列表，多个任务间用逗号相隔。 **约束限制：** 字符串类型，最大长度1000字符。 **取值范围：** 字符串长度不超过1000。 **默认取值：** 不涉及。
        :type task_ids: str
        """
        
        

        self._task_id = None
        self._task_ids = None
        self.discriminator = None

        self.task_id = task_id
        self.task_ids = task_ids

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowOpsEvaluationTasksChartsCompareResultRequest.

        **参数解释：** 基线评估任务的唯一标识符（ID）。 **约束限制：** 字符长度在0到100之间。 **取值范围：** 长度为0到100个字符的字符串。 **默认取值：** 不涉及。

        :return: The task_id of this ShowOpsEvaluationTasksChartsCompareResultRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowOpsEvaluationTasksChartsCompareResultRequest.

        **参数解释：** 基线评估任务的唯一标识符（ID）。 **约束限制：** 字符长度在0到100之间。 **取值范围：** 长度为0到100个字符的字符串。 **默认取值：** 不涉及。

        :param task_id: The task_id of this ShowOpsEvaluationTasksChartsCompareResultRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_ids(self):
        r"""Gets the task_ids of this ShowOpsEvaluationTasksChartsCompareResultRequest.

        **参数解释：** 基线评估任务的唯一标识符列表，多个任务间用逗号相隔。 **约束限制：** 字符串类型，最大长度1000字符。 **取值范围：** 字符串长度不超过1000。 **默认取值：** 不涉及。

        :return: The task_ids of this ShowOpsEvaluationTasksChartsCompareResultRequest.
        :rtype: str
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        r"""Sets the task_ids of this ShowOpsEvaluationTasksChartsCompareResultRequest.

        **参数解释：** 基线评估任务的唯一标识符列表，多个任务间用逗号相隔。 **约束限制：** 字符串类型，最大长度1000字符。 **取值范围：** 字符串长度不超过1000。 **默认取值：** 不涉及。

        :param task_ids: The task_ids of this ShowOpsEvaluationTasksChartsCompareResultRequest.
        :type task_ids: str
        """
        self._task_ids = task_ids

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
        if not isinstance(other, ShowOpsEvaluationTasksChartsCompareResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
