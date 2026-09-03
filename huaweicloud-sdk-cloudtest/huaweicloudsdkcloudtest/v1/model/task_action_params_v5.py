# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskActionParamsV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_id': 'int',
        'environment_group_id': 'str',
        'plan_id': 'str',
        'task_ids': 'list[str]'
    }

    attribute_map = {
        'action_id': 'action_id',
        'environment_group_id': 'environment_group_id',
        'plan_id': 'plan_id',
        'task_ids': 'taskIds'
    }

    def __init__(self, action_id=None, environment_group_id=None, plan_id=None, task_ids=None):
        r"""TaskActionParamsV5

        The model defined in huaweicloud sdk

        :param action_id: 启停、调试动作（1为启动，0为停止，2为调试）
        :type action_id: int
        :param environment_group_id: 环境Id
        :type environment_group_id: str
        :param plan_id: 测试计划Id
        :type plan_id: str
        :param task_ids: 任务id列表信息
        :type task_ids: list[str]
        """
        
        

        self._action_id = None
        self._environment_group_id = None
        self._plan_id = None
        self._task_ids = None
        self.discriminator = None

        if action_id is not None:
            self.action_id = action_id
        if environment_group_id is not None:
            self.environment_group_id = environment_group_id
        if plan_id is not None:
            self.plan_id = plan_id
        if task_ids is not None:
            self.task_ids = task_ids

    @property
    def action_id(self):
        r"""Gets the action_id of this TaskActionParamsV5.

        启停、调试动作（1为启动，0为停止，2为调试）

        :return: The action_id of this TaskActionParamsV5.
        :rtype: int
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this TaskActionParamsV5.

        启停、调试动作（1为启动，0为停止，2为调试）

        :param action_id: The action_id of this TaskActionParamsV5.
        :type action_id: int
        """
        self._action_id = action_id

    @property
    def environment_group_id(self):
        r"""Gets the environment_group_id of this TaskActionParamsV5.

        环境Id

        :return: The environment_group_id of this TaskActionParamsV5.
        :rtype: str
        """
        return self._environment_group_id

    @environment_group_id.setter
    def environment_group_id(self, environment_group_id):
        r"""Sets the environment_group_id of this TaskActionParamsV5.

        环境Id

        :param environment_group_id: The environment_group_id of this TaskActionParamsV5.
        :type environment_group_id: str
        """
        self._environment_group_id = environment_group_id

    @property
    def plan_id(self):
        r"""Gets the plan_id of this TaskActionParamsV5.

        测试计划Id

        :return: The plan_id of this TaskActionParamsV5.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this TaskActionParamsV5.

        测试计划Id

        :param plan_id: The plan_id of this TaskActionParamsV5.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def task_ids(self):
        r"""Gets the task_ids of this TaskActionParamsV5.

        任务id列表信息

        :return: The task_ids of this TaskActionParamsV5.
        :rtype: list[str]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        r"""Sets the task_ids of this TaskActionParamsV5.

        任务id列表信息

        :param task_ids: The task_ids of this TaskActionParamsV5.
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
        if not isinstance(other, TaskActionParamsV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
