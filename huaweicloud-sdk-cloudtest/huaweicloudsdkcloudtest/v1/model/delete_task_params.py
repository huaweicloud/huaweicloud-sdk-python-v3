# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTaskParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plan_id': 'str',
        'task_ids': 'list[str]'
    }

    attribute_map = {
        'plan_id': 'planId',
        'task_ids': 'taskIds'
    }

    def __init__(self, plan_id=None, task_ids=None):
        r"""DeleteTaskParams

        The model defined in huaweicloud sdk

        :param plan_id: 测试计划id
        :type plan_id: str
        :param task_ids: 任务id列表信息
        :type task_ids: list[str]
        """
        
        

        self._plan_id = None
        self._task_ids = None
        self.discriminator = None

        if plan_id is not None:
            self.plan_id = plan_id
        if task_ids is not None:
            self.task_ids = task_ids

    @property
    def plan_id(self):
        r"""Gets the plan_id of this DeleteTaskParams.

        测试计划id

        :return: The plan_id of this DeleteTaskParams.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this DeleteTaskParams.

        测试计划id

        :param plan_id: The plan_id of this DeleteTaskParams.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def task_ids(self):
        r"""Gets the task_ids of this DeleteTaskParams.

        任务id列表信息

        :return: The task_ids of this DeleteTaskParams.
        :rtype: list[str]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        r"""Sets the task_ids of this DeleteTaskParams.

        任务id列表信息

        :param task_ids: The task_ids of this DeleteTaskParams.
        :type task_ids: list[str]
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
        if not isinstance(other, DeleteTaskParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
