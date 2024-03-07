# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledTasksRecords:

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
        'start_time': 'str',
        'task_type': 'str',
        'scheduled_type': 'str',
        'status': 'str',
        'success_num': 'int',
        'failed_num': 'int',
        'skip_num': 'int',
        'time_zone': 'str',
        'execute_task_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'start_time': 'start_time',
        'task_type': 'task_type',
        'scheduled_type': 'scheduled_type',
        'status': 'status',
        'success_num': 'success_num',
        'failed_num': 'failed_num',
        'skip_num': 'skip_num',
        'time_zone': 'time_zone',
        'execute_task_id': 'execute_task_id'
    }

    def __init__(self, id=None, start_time=None, task_type=None, scheduled_type=None, status=None, success_num=None, failed_num=None, skip_num=None, time_zone=None, execute_task_id=None):
        """ScheduledTasksRecords

        The model defined in huaweicloud sdk

        :param id: 任务执行记录id
        :type id: str
        :param start_time: 执行时间，格式为yyyy-MM-dd HH:mm:ss。
        :type start_time: str
        :param task_type: 任务类型。START：开机，STOP：关机，REBOOT：重启，HIBERNATE：休眠，REBUILD：重建系统盘。
        :type task_type: str
        :param scheduled_type: 执行周期类型。FIXED_TIME：指定时间，DAY：按天，WEEK：按周，MONTH：按月。
        :type scheduled_type: str
        :param status: 本次执行状态。
        :type status: str
        :param success_num: 成功桌面个数。
        :type success_num: int
        :param failed_num: 失败桌面个数。
        :type failed_num: int
        :param skip_num: 跳过桌面个数。
        :type skip_num: int
        :param time_zone: 时区
        :type time_zone: str
        :param execute_task_id: 执行定时任务的任务id，只有定时执行脚本返回。
        :type execute_task_id: str
        """
        
        

        self._id = None
        self._start_time = None
        self._task_type = None
        self._scheduled_type = None
        self._status = None
        self._success_num = None
        self._failed_num = None
        self._skip_num = None
        self._time_zone = None
        self._execute_task_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if start_time is not None:
            self.start_time = start_time
        if task_type is not None:
            self.task_type = task_type
        if scheduled_type is not None:
            self.scheduled_type = scheduled_type
        if status is not None:
            self.status = status
        if success_num is not None:
            self.success_num = success_num
        if failed_num is not None:
            self.failed_num = failed_num
        if skip_num is not None:
            self.skip_num = skip_num
        if time_zone is not None:
            self.time_zone = time_zone
        if execute_task_id is not None:
            self.execute_task_id = execute_task_id

    @property
    def id(self):
        """Gets the id of this ScheduledTasksRecords.

        任务执行记录id

        :return: The id of this ScheduledTasksRecords.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScheduledTasksRecords.

        任务执行记录id

        :param id: The id of this ScheduledTasksRecords.
        :type id: str
        """
        self._id = id

    @property
    def start_time(self):
        """Gets the start_time of this ScheduledTasksRecords.

        执行时间，格式为yyyy-MM-dd HH:mm:ss。

        :return: The start_time of this ScheduledTasksRecords.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScheduledTasksRecords.

        执行时间，格式为yyyy-MM-dd HH:mm:ss。

        :param start_time: The start_time of this ScheduledTasksRecords.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def task_type(self):
        """Gets the task_type of this ScheduledTasksRecords.

        任务类型。START：开机，STOP：关机，REBOOT：重启，HIBERNATE：休眠，REBUILD：重建系统盘。

        :return: The task_type of this ScheduledTasksRecords.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ScheduledTasksRecords.

        任务类型。START：开机，STOP：关机，REBOOT：重启，HIBERNATE：休眠，REBUILD：重建系统盘。

        :param task_type: The task_type of this ScheduledTasksRecords.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def scheduled_type(self):
        """Gets the scheduled_type of this ScheduledTasksRecords.

        执行周期类型。FIXED_TIME：指定时间，DAY：按天，WEEK：按周，MONTH：按月。

        :return: The scheduled_type of this ScheduledTasksRecords.
        :rtype: str
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        """Sets the scheduled_type of this ScheduledTasksRecords.

        执行周期类型。FIXED_TIME：指定时间，DAY：按天，WEEK：按周，MONTH：按月。

        :param scheduled_type: The scheduled_type of this ScheduledTasksRecords.
        :type scheduled_type: str
        """
        self._scheduled_type = scheduled_type

    @property
    def status(self):
        """Gets the status of this ScheduledTasksRecords.

        本次执行状态。

        :return: The status of this ScheduledTasksRecords.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScheduledTasksRecords.

        本次执行状态。

        :param status: The status of this ScheduledTasksRecords.
        :type status: str
        """
        self._status = status

    @property
    def success_num(self):
        """Gets the success_num of this ScheduledTasksRecords.

        成功桌面个数。

        :return: The success_num of this ScheduledTasksRecords.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        """Sets the success_num of this ScheduledTasksRecords.

        成功桌面个数。

        :param success_num: The success_num of this ScheduledTasksRecords.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def failed_num(self):
        """Gets the failed_num of this ScheduledTasksRecords.

        失败桌面个数。

        :return: The failed_num of this ScheduledTasksRecords.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        """Sets the failed_num of this ScheduledTasksRecords.

        失败桌面个数。

        :param failed_num: The failed_num of this ScheduledTasksRecords.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def skip_num(self):
        """Gets the skip_num of this ScheduledTasksRecords.

        跳过桌面个数。

        :return: The skip_num of this ScheduledTasksRecords.
        :rtype: int
        """
        return self._skip_num

    @skip_num.setter
    def skip_num(self, skip_num):
        """Sets the skip_num of this ScheduledTasksRecords.

        跳过桌面个数。

        :param skip_num: The skip_num of this ScheduledTasksRecords.
        :type skip_num: int
        """
        self._skip_num = skip_num

    @property
    def time_zone(self):
        """Gets the time_zone of this ScheduledTasksRecords.

        时区

        :return: The time_zone of this ScheduledTasksRecords.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ScheduledTasksRecords.

        时区

        :param time_zone: The time_zone of this ScheduledTasksRecords.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def execute_task_id(self):
        """Gets the execute_task_id of this ScheduledTasksRecords.

        执行定时任务的任务id，只有定时执行脚本返回。

        :return: The execute_task_id of this ScheduledTasksRecords.
        :rtype: str
        """
        return self._execute_task_id

    @execute_task_id.setter
    def execute_task_id(self, execute_task_id):
        """Sets the execute_task_id of this ScheduledTasksRecords.

        执行定时任务的任务id，只有定时执行脚本返回。

        :param execute_task_id: The execute_task_id of this ScheduledTasksRecords.
        :type execute_task_id: str
        """
        self._execute_task_id = execute_task_id

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
        if not isinstance(other, ScheduledTasksRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
