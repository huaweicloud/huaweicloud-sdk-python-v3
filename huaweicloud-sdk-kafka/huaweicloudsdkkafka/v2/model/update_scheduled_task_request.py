# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScheduledTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'task_id': 'str',
        'execute_at': 'str',
        'status': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'task_id': 'task_id',
        'execute_at': 'execute_at',
        'status': 'status'
    }

    def __init__(self, instance_id=None, task_id=None, execute_at=None, status=None):
        r"""UpdateScheduledTaskRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type instance_id: str
        :param task_id: **参数解释**： 定时任务ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type task_id: str
        :param execute_at: **参数解释**： 修改定时任务的执行时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type execute_at: str
        :param status: **参数解释**： 修改定时任务状态。 **约束限制**： 不涉及。 **取值范围**： - CANCELLED：定时任务被取消。 - null：定时任务待执行。 **默认取值**： 不涉及。
        :type status: str
        """
        
        

        self._instance_id = None
        self._task_id = None
        self._execute_at = None
        self._status = None
        self.discriminator = None

        self.instance_id = instance_id
        self.task_id = task_id
        if execute_at is not None:
            self.execute_at = execute_at
        if status is not None:
            self.status = status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateScheduledTaskRequest.

        **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_id of this UpdateScheduledTaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateScheduledTaskRequest.

        **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param instance_id: The instance_id of this UpdateScheduledTaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def task_id(self):
        r"""Gets the task_id of this UpdateScheduledTaskRequest.

        **参数解释**： 定时任务ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The task_id of this UpdateScheduledTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this UpdateScheduledTaskRequest.

        **参数解释**： 定时任务ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param task_id: The task_id of this UpdateScheduledTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def execute_at(self):
        r"""Gets the execute_at of this UpdateScheduledTaskRequest.

        **参数解释**： 修改定时任务的执行时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The execute_at of this UpdateScheduledTaskRequest.
        :rtype: str
        """
        return self._execute_at

    @execute_at.setter
    def execute_at(self, execute_at):
        r"""Sets the execute_at of this UpdateScheduledTaskRequest.

        **参数解释**： 修改定时任务的执行时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param execute_at: The execute_at of this UpdateScheduledTaskRequest.
        :type execute_at: str
        """
        self._execute_at = execute_at

    @property
    def status(self):
        r"""Gets the status of this UpdateScheduledTaskRequest.

        **参数解释**： 修改定时任务状态。 **约束限制**： 不涉及。 **取值范围**： - CANCELLED：定时任务被取消。 - null：定时任务待执行。 **默认取值**： 不涉及。

        :return: The status of this UpdateScheduledTaskRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateScheduledTaskRequest.

        **参数解释**： 修改定时任务状态。 **约束限制**： 不涉及。 **取值范围**： - CANCELLED：定时任务被取消。 - null：定时任务待执行。 **默认取值**： 不涉及。

        :param status: The status of this UpdateScheduledTaskRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, UpdateScheduledTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
