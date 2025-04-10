# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleTaskExecuteHistory:

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
        'task_id': 'str',
        'task_type': 'ScheduleTaskTypeEnum',
        'status': 'ScheduleTaskStatus',
        'scheduled_type': 'ScheduledTypeEnum',
        'total_count': 'int',
        'success_count': 'int',
        'failed_count': 'int',
        'excuting_count': 'int',
        'time_zone': 'str',
        'begin_time': 'datetime',
        'end_time': 'datetime',
        'create_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'task_id': 'task_id',
        'task_type': 'task_type',
        'status': 'status',
        'scheduled_type': 'scheduled_type',
        'total_count': 'total_count',
        'success_count': 'success_count',
        'failed_count': 'failed_count',
        'excuting_count': 'excuting_count',
        'time_zone': 'time_zone',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, task_id=None, task_type=None, status=None, scheduled_type=None, total_count=None, success_count=None, failed_count=None, excuting_count=None, time_zone=None, begin_time=None, end_time=None, create_time=None):
        r"""ScheduleTaskExecuteHistory

        The model defined in huaweicloud sdk

        :param id: 定时任务执行记录主键id。
        :type id: str
        :param task_id: 定时任务主键id。
        :type task_id: str
        :param task_type: 
        :type task_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        :param status: 
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskStatus`
        :param scheduled_type: 
        :type scheduled_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduledTypeEnum`
        :param total_count: 总子任务数。
        :type total_count: int
        :param success_count: 成功的子任务数。
        :type success_count: int
        :param failed_count: 失败的子任务数。
        :type failed_count: int
        :param excuting_count: 正在执行的子任务数。
        :type excuting_count: int
        :param time_zone: 时区。
        :type time_zone: str
        :param begin_time: 任务开始时间。
        :type begin_time: datetime
        :param end_time: 任务结束时间。
        :type end_time: datetime
        :param create_time: 创建时间。
        :type create_time: datetime
        """
        
        

        self._id = None
        self._task_id = None
        self._task_type = None
        self._status = None
        self._scheduled_type = None
        self._total_count = None
        self._success_count = None
        self._failed_count = None
        self._excuting_count = None
        self._time_zone = None
        self._begin_time = None
        self._end_time = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_id is not None:
            self.task_id = task_id
        if task_type is not None:
            self.task_type = task_type
        if status is not None:
            self.status = status
        if scheduled_type is not None:
            self.scheduled_type = scheduled_type
        if total_count is not None:
            self.total_count = total_count
        if success_count is not None:
            self.success_count = success_count
        if failed_count is not None:
            self.failed_count = failed_count
        if excuting_count is not None:
            self.excuting_count = excuting_count
        if time_zone is not None:
            self.time_zone = time_zone
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this ScheduleTaskExecuteHistory.

        定时任务执行记录主键id。

        :return: The id of this ScheduleTaskExecuteHistory.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScheduleTaskExecuteHistory.

        定时任务执行记录主键id。

        :param id: The id of this ScheduleTaskExecuteHistory.
        :type id: str
        """
        self._id = id

    @property
    def task_id(self):
        r"""Gets the task_id of this ScheduleTaskExecuteHistory.

        定时任务主键id。

        :return: The task_id of this ScheduleTaskExecuteHistory.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ScheduleTaskExecuteHistory.

        定时任务主键id。

        :param task_id: The task_id of this ScheduleTaskExecuteHistory.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_type(self):
        r"""Gets the task_type of this ScheduleTaskExecuteHistory.

        :return: The task_type of this ScheduleTaskExecuteHistory.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ScheduleTaskExecuteHistory.

        :param task_type: The task_type of this ScheduleTaskExecuteHistory.
        :type task_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        """
        self._task_type = task_type

    @property
    def status(self):
        r"""Gets the status of this ScheduleTaskExecuteHistory.

        :return: The status of this ScheduleTaskExecuteHistory.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScheduleTaskExecuteHistory.

        :param status: The status of this ScheduleTaskExecuteHistory.
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskStatus`
        """
        self._status = status

    @property
    def scheduled_type(self):
        r"""Gets the scheduled_type of this ScheduleTaskExecuteHistory.

        :return: The scheduled_type of this ScheduleTaskExecuteHistory.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduledTypeEnum`
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        r"""Sets the scheduled_type of this ScheduleTaskExecuteHistory.

        :param scheduled_type: The scheduled_type of this ScheduleTaskExecuteHistory.
        :type scheduled_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduledTypeEnum`
        """
        self._scheduled_type = scheduled_type

    @property
    def total_count(self):
        r"""Gets the total_count of this ScheduleTaskExecuteHistory.

        总子任务数。

        :return: The total_count of this ScheduleTaskExecuteHistory.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ScheduleTaskExecuteHistory.

        总子任务数。

        :param total_count: The total_count of this ScheduleTaskExecuteHistory.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def success_count(self):
        r"""Gets the success_count of this ScheduleTaskExecuteHistory.

        成功的子任务数。

        :return: The success_count of this ScheduleTaskExecuteHistory.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this ScheduleTaskExecuteHistory.

        成功的子任务数。

        :param success_count: The success_count of this ScheduleTaskExecuteHistory.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def failed_count(self):
        r"""Gets the failed_count of this ScheduleTaskExecuteHistory.

        失败的子任务数。

        :return: The failed_count of this ScheduleTaskExecuteHistory.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        r"""Sets the failed_count of this ScheduleTaskExecuteHistory.

        失败的子任务数。

        :param failed_count: The failed_count of this ScheduleTaskExecuteHistory.
        :type failed_count: int
        """
        self._failed_count = failed_count

    @property
    def excuting_count(self):
        r"""Gets the excuting_count of this ScheduleTaskExecuteHistory.

        正在执行的子任务数。

        :return: The excuting_count of this ScheduleTaskExecuteHistory.
        :rtype: int
        """
        return self._excuting_count

    @excuting_count.setter
    def excuting_count(self, excuting_count):
        r"""Sets the excuting_count of this ScheduleTaskExecuteHistory.

        正在执行的子任务数。

        :param excuting_count: The excuting_count of this ScheduleTaskExecuteHistory.
        :type excuting_count: int
        """
        self._excuting_count = excuting_count

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ScheduleTaskExecuteHistory.

        时区。

        :return: The time_zone of this ScheduleTaskExecuteHistory.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ScheduleTaskExecuteHistory.

        时区。

        :param time_zone: The time_zone of this ScheduleTaskExecuteHistory.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ScheduleTaskExecuteHistory.

        任务开始时间。

        :return: The begin_time of this ScheduleTaskExecuteHistory.
        :rtype: datetime
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ScheduleTaskExecuteHistory.

        任务开始时间。

        :param begin_time: The begin_time of this ScheduleTaskExecuteHistory.
        :type begin_time: datetime
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ScheduleTaskExecuteHistory.

        任务结束时间。

        :return: The end_time of this ScheduleTaskExecuteHistory.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ScheduleTaskExecuteHistory.

        任务结束时间。

        :param end_time: The end_time of this ScheduleTaskExecuteHistory.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def create_time(self):
        r"""Gets the create_time of this ScheduleTaskExecuteHistory.

        创建时间。

        :return: The create_time of this ScheduleTaskExecuteHistory.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ScheduleTaskExecuteHistory.

        创建时间。

        :param create_time: The create_time of this ScheduleTaskExecuteHistory.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, ScheduleTaskExecuteHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
