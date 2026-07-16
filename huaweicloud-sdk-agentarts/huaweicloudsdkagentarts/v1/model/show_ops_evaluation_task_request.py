# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluationTaskRequest:

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
        'name': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'name': 'name'
    }

    def __init__(self, task_id=None, name=None):
        r"""ShowOpsEvaluationTaskRequest

        The model defined in huaweicloud sdk

        :param task_id: **参数解释：** 评估任务的唯一标识符（ID）。该参数嵌入在API路径中，用于定位需要操作的具体任务实例。 **约束限制：** 长度为0到100个字符的字符串。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type task_id: str
        :param name: **参数解释：** 评估任务的名称。作为查询参数使用时，可根据任务名称进行精确或过滤匹配。 **约束限制：** 长度为0到120个字符的字符串。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        """
        
        

        self._task_id = None
        self._name = None
        self.discriminator = None

        self.task_id = task_id
        if name is not None:
            self.name = name

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowOpsEvaluationTaskRequest.

        **参数解释：** 评估任务的唯一标识符（ID）。该参数嵌入在API路径中，用于定位需要操作的具体任务实例。 **约束限制：** 长度为0到100个字符的字符串。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The task_id of this ShowOpsEvaluationTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowOpsEvaluationTaskRequest.

        **参数解释：** 评估任务的唯一标识符（ID）。该参数嵌入在API路径中，用于定位需要操作的具体任务实例。 **约束限制：** 长度为0到100个字符的字符串。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param task_id: The task_id of this ShowOpsEvaluationTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def name(self):
        r"""Gets the name of this ShowOpsEvaluationTaskRequest.

        **参数解释：** 评估任务的名称。作为查询参数使用时，可根据任务名称进行精确或过滤匹配。 **约束限制：** 长度为0到120个字符的字符串。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this ShowOpsEvaluationTaskRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowOpsEvaluationTaskRequest.

        **参数解释：** 评估任务的名称。作为查询参数使用时，可根据任务名称进行精确或过滤匹配。 **约束限制：** 长度为0到120个字符的字符串。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this ShowOpsEvaluationTaskRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ShowOpsEvaluationTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
