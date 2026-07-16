# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsQuotaRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_type': 'str'
    }

    attribute_map = {
        'task_type': 'task_type'
    }

    def __init__(self, task_type=None):
        r"""ShowOpsQuotaRequest

        The model defined in huaweicloud sdk

        :param task_type: **参数解释：** 任务的类型分类标识。该参数用于在查询列表时进行过滤，以便区分并获取特定类别的任务（例如：评估任务、数据合成任务等）。 **约束限制：** 字符串长度为0-1,200。 **取值范围：** 0-1200字符。 **默认取值：** 不涉及。
        :type task_type: str
        """
        
        

        self._task_type = None
        self.discriminator = None

        if task_type is not None:
            self.task_type = task_type

    @property
    def task_type(self):
        r"""Gets the task_type of this ShowOpsQuotaRequest.

        **参数解释：** 任务的类型分类标识。该参数用于在查询列表时进行过滤，以便区分并获取特定类别的任务（例如：评估任务、数据合成任务等）。 **约束限制：** 字符串长度为0-1,200。 **取值范围：** 0-1200字符。 **默认取值：** 不涉及。

        :return: The task_type of this ShowOpsQuotaRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ShowOpsQuotaRequest.

        **参数解释：** 任务的类型分类标识。该参数用于在查询列表时进行过滤，以便区分并获取特定类别的任务（例如：评估任务、数据合成任务等）。 **约束限制：** 字符串长度为0-1,200。 **取值范围：** 0-1200字符。 **默认取值：** 不涉及。

        :param task_type: The task_type of this ShowOpsQuotaRequest.
        :type task_type: str
        """
        self._task_type = task_type

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
        if not isinstance(other, ShowOpsQuotaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
