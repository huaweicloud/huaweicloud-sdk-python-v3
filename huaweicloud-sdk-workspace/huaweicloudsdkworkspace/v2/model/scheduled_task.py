# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'task_name': 'str',
        'task_type': 'str',
        'scheduled_type': 'str',
        'life_cycle_type': 'str',
        'last_status': 'str',
        'next_execution_time': 'str',
        'enable': 'bool',
        'description': 'str',
        'priority': 'int',
        'time_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'scheduled_type': 'scheduled_type',
        'life_cycle_type': 'life_cycle_type',
        'last_status': 'last_status',
        'next_execution_time': 'next_execution_time',
        'enable': 'enable',
        'description': 'description',
        'priority': 'priority',
        'time_zone': 'time_zone'
    }

    def __init__(self, id=None, task_name=None, task_type=None, scheduled_type=None, life_cycle_type=None, last_status=None, next_execution_time=None, enable=None, description=None, priority=None, time_zone=None):
        """ScheduledTask

        The model defined in huaweicloud sdk

        :param id: 任务id。
        :type id: str
        :param task_name: 任务名称。
        :type task_name: str
        :param task_type: 任务类型。START：开机，STOP：关机，REBOOT：重启，HIBERNATE：休眠，REBUILD：重建系统盘，EXECUTE_SCRIPT：执行脚本。
        :type task_type: str
        :param scheduled_type: 执行周期。FIXED_TIME：指定时间，DAY：按天，WEEK：按周，MONTH：按月。
        :type scheduled_type: str
        :param life_cycle_type: 触发场景类型。
        :type life_cycle_type: str
        :param last_status: 最近一次执行状态。SUCCESS：成功，SKIP：跳过，FAIL：失败。
        :type last_status: str
        :param next_execution_time: 下一次执行时间。格式为yyyy-MM-dd HH:mm:ss。
        :type next_execution_time: str
        :param enable: 是否启用。
        :type enable: bool
        :param description: 描述。
        :type description: str
        :param priority: 优先级。触发式任务使用。
        :type priority: int
        :param time_zone: 时区
        :type time_zone: str
        """
        
        

        self._id = None
        self._task_name = None
        self._task_type = None
        self._scheduled_type = None
        self._life_cycle_type = None
        self._last_status = None
        self._next_execution_time = None
        self._enable = None
        self._description = None
        self._priority = None
        self._time_zone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if scheduled_type is not None:
            self.scheduled_type = scheduled_type
        if life_cycle_type is not None:
            self.life_cycle_type = life_cycle_type
        if last_status is not None:
            self.last_status = last_status
        if next_execution_time is not None:
            self.next_execution_time = next_execution_time
        if enable is not None:
            self.enable = enable
        if description is not None:
            self.description = description
        if priority is not None:
            self.priority = priority
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def id(self):
        """Gets the id of this ScheduledTask.

        任务id。

        :return: The id of this ScheduledTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScheduledTask.

        任务id。

        :param id: The id of this ScheduledTask.
        :type id: str
        """
        self._id = id

    @property
    def task_name(self):
        """Gets the task_name of this ScheduledTask.

        任务名称。

        :return: The task_name of this ScheduledTask.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this ScheduledTask.

        任务名称。

        :param task_name: The task_name of this ScheduledTask.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        """Gets the task_type of this ScheduledTask.

        任务类型。START：开机，STOP：关机，REBOOT：重启，HIBERNATE：休眠，REBUILD：重建系统盘，EXECUTE_SCRIPT：执行脚本。

        :return: The task_type of this ScheduledTask.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ScheduledTask.

        任务类型。START：开机，STOP：关机，REBOOT：重启，HIBERNATE：休眠，REBUILD：重建系统盘，EXECUTE_SCRIPT：执行脚本。

        :param task_type: The task_type of this ScheduledTask.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def scheduled_type(self):
        """Gets the scheduled_type of this ScheduledTask.

        执行周期。FIXED_TIME：指定时间，DAY：按天，WEEK：按周，MONTH：按月。

        :return: The scheduled_type of this ScheduledTask.
        :rtype: str
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        """Sets the scheduled_type of this ScheduledTask.

        执行周期。FIXED_TIME：指定时间，DAY：按天，WEEK：按周，MONTH：按月。

        :param scheduled_type: The scheduled_type of this ScheduledTask.
        :type scheduled_type: str
        """
        self._scheduled_type = scheduled_type

    @property
    def life_cycle_type(self):
        """Gets the life_cycle_type of this ScheduledTask.

        触发场景类型。

        :return: The life_cycle_type of this ScheduledTask.
        :rtype: str
        """
        return self._life_cycle_type

    @life_cycle_type.setter
    def life_cycle_type(self, life_cycle_type):
        """Sets the life_cycle_type of this ScheduledTask.

        触发场景类型。

        :param life_cycle_type: The life_cycle_type of this ScheduledTask.
        :type life_cycle_type: str
        """
        self._life_cycle_type = life_cycle_type

    @property
    def last_status(self):
        """Gets the last_status of this ScheduledTask.

        最近一次执行状态。SUCCESS：成功，SKIP：跳过，FAIL：失败。

        :return: The last_status of this ScheduledTask.
        :rtype: str
        """
        return self._last_status

    @last_status.setter
    def last_status(self, last_status):
        """Sets the last_status of this ScheduledTask.

        最近一次执行状态。SUCCESS：成功，SKIP：跳过，FAIL：失败。

        :param last_status: The last_status of this ScheduledTask.
        :type last_status: str
        """
        self._last_status = last_status

    @property
    def next_execution_time(self):
        """Gets the next_execution_time of this ScheduledTask.

        下一次执行时间。格式为yyyy-MM-dd HH:mm:ss。

        :return: The next_execution_time of this ScheduledTask.
        :rtype: str
        """
        return self._next_execution_time

    @next_execution_time.setter
    def next_execution_time(self, next_execution_time):
        """Sets the next_execution_time of this ScheduledTask.

        下一次执行时间。格式为yyyy-MM-dd HH:mm:ss。

        :param next_execution_time: The next_execution_time of this ScheduledTask.
        :type next_execution_time: str
        """
        self._next_execution_time = next_execution_time

    @property
    def enable(self):
        """Gets the enable of this ScheduledTask.

        是否启用。

        :return: The enable of this ScheduledTask.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this ScheduledTask.

        是否启用。

        :param enable: The enable of this ScheduledTask.
        :type enable: bool
        """
        self._enable = enable

    @property
    def description(self):
        """Gets the description of this ScheduledTask.

        描述。

        :return: The description of this ScheduledTask.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScheduledTask.

        描述。

        :param description: The description of this ScheduledTask.
        :type description: str
        """
        self._description = description

    @property
    def priority(self):
        """Gets the priority of this ScheduledTask.

        优先级。触发式任务使用。

        :return: The priority of this ScheduledTask.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ScheduledTask.

        优先级。触发式任务使用。

        :param priority: The priority of this ScheduledTask.
        :type priority: int
        """
        self._priority = priority

    @property
    def time_zone(self):
        """Gets the time_zone of this ScheduledTask.

        时区

        :return: The time_zone of this ScheduledTask.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ScheduledTask.

        时区

        :param time_zone: The time_zone of this ScheduledTask.
        :type time_zone: str
        """
        self._time_zone = time_zone

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScheduledTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
