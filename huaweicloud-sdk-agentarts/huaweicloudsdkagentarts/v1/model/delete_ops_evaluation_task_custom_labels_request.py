# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteOpsEvaluationTaskCustomLabelsRequest:

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
        'label_id': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'label_id': 'label_id'
    }

    def __init__(self, task_id=None, label_id=None):
        r"""DeleteOpsEvaluationTaskCustomLabelsRequest

        The model defined in huaweicloud sdk

        :param task_id: **参数解释：** 用于标识评估任务的唯一ID。该参数在路径中指定，确保操作作用于正确的任务实例。 **约束限制：** 字符串长度为0-100。 **取值范围：** 0-100字符。 **默认取值：** 不涉及。
        :type task_id: str
        :param label_id: **参数解释：** 与评估任务关联的特定标签ID。用于在任务范围内精确筛选或定位某类标签数据。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 0-100字符。 **默认取值：** 不涉及。
        :type label_id: str
        """
        
        

        self._task_id = None
        self._label_id = None
        self.discriminator = None

        self.task_id = task_id
        self.label_id = label_id

    @property
    def task_id(self):
        r"""Gets the task_id of this DeleteOpsEvaluationTaskCustomLabelsRequest.

        **参数解释：** 用于标识评估任务的唯一ID。该参数在路径中指定，确保操作作用于正确的任务实例。 **约束限制：** 字符串长度为0-100。 **取值范围：** 0-100字符。 **默认取值：** 不涉及。

        :return: The task_id of this DeleteOpsEvaluationTaskCustomLabelsRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this DeleteOpsEvaluationTaskCustomLabelsRequest.

        **参数解释：** 用于标识评估任务的唯一ID。该参数在路径中指定，确保操作作用于正确的任务实例。 **约束限制：** 字符串长度为0-100。 **取值范围：** 0-100字符。 **默认取值：** 不涉及。

        :param task_id: The task_id of this DeleteOpsEvaluationTaskCustomLabelsRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def label_id(self):
        r"""Gets the label_id of this DeleteOpsEvaluationTaskCustomLabelsRequest.

        **参数解释：** 与评估任务关联的特定标签ID。用于在任务范围内精确筛选或定位某类标签数据。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 0-100字符。 **默认取值：** 不涉及。

        :return: The label_id of this DeleteOpsEvaluationTaskCustomLabelsRequest.
        :rtype: str
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        r"""Sets the label_id of this DeleteOpsEvaluationTaskCustomLabelsRequest.

        **参数解释：** 与评估任务关联的特定标签ID。用于在任务范围内精确筛选或定位某类标签数据。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 0-100字符。 **默认取值：** 不涉及。

        :param label_id: The label_id of this DeleteOpsEvaluationTaskCustomLabelsRequest.
        :type label_id: str
        """
        self._label_id = label_id

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
        if not isinstance(other, DeleteOpsEvaluationTaskCustomLabelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
