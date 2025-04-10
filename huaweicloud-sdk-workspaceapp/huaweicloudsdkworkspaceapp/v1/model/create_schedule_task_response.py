# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateScheduleTaskResponse(SdkResponse):

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
        'last_status': 'ScheduleTaskStatus',
        'task_type': 'ScheduleTaskTypeEnum',
        'task_cron': 'str',
        'next_execution_time': 'str',
        'schedule_task_policy': 'ScheduleTaskPolicy',
        'scheduled_type': 'ScheduledTypeEnum',
        'day_interval': 'int',
        'week_list': 'str',
        'month_list': 'str',
        'date_list': 'str',
        'time_zone': 'str',
        'scheduled_date': 'str',
        'scheduled_time': 'str',
        'expire_time': 'datetime',
        'description': 'str',
        'is_enable': 'bool',
        'create_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'task_name': 'task_name',
        'last_status': 'last_status',
        'task_type': 'task_type',
        'task_cron': 'task_cron',
        'next_execution_time': 'next_execution_time',
        'schedule_task_policy': 'schedule_task_policy',
        'scheduled_type': 'scheduled_type',
        'day_interval': 'day_interval',
        'week_list': 'week_list',
        'month_list': 'month_list',
        'date_list': 'date_list',
        'time_zone': 'time_zone',
        'scheduled_date': 'scheduled_date',
        'scheduled_time': 'scheduled_time',
        'expire_time': 'expire_time',
        'description': 'description',
        'is_enable': 'is_enable',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, task_name=None, last_status=None, task_type=None, task_cron=None, next_execution_time=None, schedule_task_policy=None, scheduled_type=None, day_interval=None, week_list=None, month_list=None, date_list=None, time_zone=None, scheduled_date=None, scheduled_time=None, expire_time=None, description=None, is_enable=None, create_time=None, update_time=None):
        r"""CreateScheduleTaskResponse

        The model defined in huaweicloud sdk

        :param id: 定时任务主键id。
        :type id: str
        :param task_name: 任务名称。
        :type task_name: str
        :param last_status: 
        :type last_status: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskStatus`
        :param task_type: 
        :type task_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        :param task_cron: 定时任务表达式。
        :type task_cron: str
        :param next_execution_time: 下一次执行时间。
        :type next_execution_time: str
        :param schedule_task_policy: 
        :type schedule_task_policy: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskPolicy`
        :param scheduled_type: 
        :type scheduled_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduledTypeEnum`
        :param day_interval: 周期按天时：按x天间隔执行。
        :type day_interval: int
        :param week_list: 周期按周时：取值1~7，英文逗号分隔，如1,2,7。
        :type week_list: str
        :param month_list: 周期按月时：取值1~12，英文逗号分隔，如1,3,12。
        :type month_list: str
        :param date_list: 周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。
        :type date_list: str
        :param time_zone: 时区。
        :type time_zone: str
        :param scheduled_date: 周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。
        :type scheduled_date: str
        :param scheduled_time: 指定的执行时间点，格式为HH:mm:ss。
        :type scheduled_time: str
        :param expire_time: 到期时间。
        :type expire_time: datetime
        :param description: 任务描述。
        :type description: str
        :param is_enable: 是否是开启状态。
        :type is_enable: bool
        :param create_time: 创建时间。
        :type create_time: datetime
        :param update_time: 更新时间。
        :type update_time: datetime
        """
        
        super(CreateScheduleTaskResponse, self).__init__()

        self._id = None
        self._task_name = None
        self._last_status = None
        self._task_type = None
        self._task_cron = None
        self._next_execution_time = None
        self._schedule_task_policy = None
        self._scheduled_type = None
        self._day_interval = None
        self._week_list = None
        self._month_list = None
        self._date_list = None
        self._time_zone = None
        self._scheduled_date = None
        self._scheduled_time = None
        self._expire_time = None
        self._description = None
        self._is_enable = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_name is not None:
            self.task_name = task_name
        if last_status is not None:
            self.last_status = last_status
        if task_type is not None:
            self.task_type = task_type
        if task_cron is not None:
            self.task_cron = task_cron
        if next_execution_time is not None:
            self.next_execution_time = next_execution_time
        if schedule_task_policy is not None:
            self.schedule_task_policy = schedule_task_policy
        if scheduled_type is not None:
            self.scheduled_type = scheduled_type
        if day_interval is not None:
            self.day_interval = day_interval
        if week_list is not None:
            self.week_list = week_list
        if month_list is not None:
            self.month_list = month_list
        if date_list is not None:
            self.date_list = date_list
        if time_zone is not None:
            self.time_zone = time_zone
        if scheduled_date is not None:
            self.scheduled_date = scheduled_date
        if scheduled_time is not None:
            self.scheduled_time = scheduled_time
        if expire_time is not None:
            self.expire_time = expire_time
        if description is not None:
            self.description = description
        if is_enable is not None:
            self.is_enable = is_enable
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this CreateScheduleTaskResponse.

        定时任务主键id。

        :return: The id of this CreateScheduleTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateScheduleTaskResponse.

        定时任务主键id。

        :param id: The id of this CreateScheduleTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def task_name(self):
        r"""Gets the task_name of this CreateScheduleTaskResponse.

        任务名称。

        :return: The task_name of this CreateScheduleTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this CreateScheduleTaskResponse.

        任务名称。

        :param task_name: The task_name of this CreateScheduleTaskResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def last_status(self):
        r"""Gets the last_status of this CreateScheduleTaskResponse.

        :return: The last_status of this CreateScheduleTaskResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskStatus`
        """
        return self._last_status

    @last_status.setter
    def last_status(self, last_status):
        r"""Sets the last_status of this CreateScheduleTaskResponse.

        :param last_status: The last_status of this CreateScheduleTaskResponse.
        :type last_status: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskStatus`
        """
        self._last_status = last_status

    @property
    def task_type(self):
        r"""Gets the task_type of this CreateScheduleTaskResponse.

        :return: The task_type of this CreateScheduleTaskResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this CreateScheduleTaskResponse.

        :param task_type: The task_type of this CreateScheduleTaskResponse.
        :type task_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        """
        self._task_type = task_type

    @property
    def task_cron(self):
        r"""Gets the task_cron of this CreateScheduleTaskResponse.

        定时任务表达式。

        :return: The task_cron of this CreateScheduleTaskResponse.
        :rtype: str
        """
        return self._task_cron

    @task_cron.setter
    def task_cron(self, task_cron):
        r"""Sets the task_cron of this CreateScheduleTaskResponse.

        定时任务表达式。

        :param task_cron: The task_cron of this CreateScheduleTaskResponse.
        :type task_cron: str
        """
        self._task_cron = task_cron

    @property
    def next_execution_time(self):
        r"""Gets the next_execution_time of this CreateScheduleTaskResponse.

        下一次执行时间。

        :return: The next_execution_time of this CreateScheduleTaskResponse.
        :rtype: str
        """
        return self._next_execution_time

    @next_execution_time.setter
    def next_execution_time(self, next_execution_time):
        r"""Sets the next_execution_time of this CreateScheduleTaskResponse.

        下一次执行时间。

        :param next_execution_time: The next_execution_time of this CreateScheduleTaskResponse.
        :type next_execution_time: str
        """
        self._next_execution_time = next_execution_time

    @property
    def schedule_task_policy(self):
        r"""Gets the schedule_task_policy of this CreateScheduleTaskResponse.

        :return: The schedule_task_policy of this CreateScheduleTaskResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskPolicy`
        """
        return self._schedule_task_policy

    @schedule_task_policy.setter
    def schedule_task_policy(self, schedule_task_policy):
        r"""Sets the schedule_task_policy of this CreateScheduleTaskResponse.

        :param schedule_task_policy: The schedule_task_policy of this CreateScheduleTaskResponse.
        :type schedule_task_policy: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskPolicy`
        """
        self._schedule_task_policy = schedule_task_policy

    @property
    def scheduled_type(self):
        r"""Gets the scheduled_type of this CreateScheduleTaskResponse.

        :return: The scheduled_type of this CreateScheduleTaskResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduledTypeEnum`
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        r"""Sets the scheduled_type of this CreateScheduleTaskResponse.

        :param scheduled_type: The scheduled_type of this CreateScheduleTaskResponse.
        :type scheduled_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduledTypeEnum`
        """
        self._scheduled_type = scheduled_type

    @property
    def day_interval(self):
        r"""Gets the day_interval of this CreateScheduleTaskResponse.

        周期按天时：按x天间隔执行。

        :return: The day_interval of this CreateScheduleTaskResponse.
        :rtype: int
        """
        return self._day_interval

    @day_interval.setter
    def day_interval(self, day_interval):
        r"""Sets the day_interval of this CreateScheduleTaskResponse.

        周期按天时：按x天间隔执行。

        :param day_interval: The day_interval of this CreateScheduleTaskResponse.
        :type day_interval: int
        """
        self._day_interval = day_interval

    @property
    def week_list(self):
        r"""Gets the week_list of this CreateScheduleTaskResponse.

        周期按周时：取值1~7，英文逗号分隔，如1,2,7。

        :return: The week_list of this CreateScheduleTaskResponse.
        :rtype: str
        """
        return self._week_list

    @week_list.setter
    def week_list(self, week_list):
        r"""Sets the week_list of this CreateScheduleTaskResponse.

        周期按周时：取值1~7，英文逗号分隔，如1,2,7。

        :param week_list: The week_list of this CreateScheduleTaskResponse.
        :type week_list: str
        """
        self._week_list = week_list

    @property
    def month_list(self):
        r"""Gets the month_list of this CreateScheduleTaskResponse.

        周期按月时：取值1~12，英文逗号分隔，如1,3,12。

        :return: The month_list of this CreateScheduleTaskResponse.
        :rtype: str
        """
        return self._month_list

    @month_list.setter
    def month_list(self, month_list):
        r"""Sets the month_list of this CreateScheduleTaskResponse.

        周期按月时：取值1~12，英文逗号分隔，如1,3,12。

        :param month_list: The month_list of this CreateScheduleTaskResponse.
        :type month_list: str
        """
        self._month_list = month_list

    @property
    def date_list(self):
        r"""Gets the date_list of this CreateScheduleTaskResponse.

        周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。

        :return: The date_list of this CreateScheduleTaskResponse.
        :rtype: str
        """
        return self._date_list

    @date_list.setter
    def date_list(self, date_list):
        r"""Sets the date_list of this CreateScheduleTaskResponse.

        周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。

        :param date_list: The date_list of this CreateScheduleTaskResponse.
        :type date_list: str
        """
        self._date_list = date_list

    @property
    def time_zone(self):
        r"""Gets the time_zone of this CreateScheduleTaskResponse.

        时区。

        :return: The time_zone of this CreateScheduleTaskResponse.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this CreateScheduleTaskResponse.

        时区。

        :param time_zone: The time_zone of this CreateScheduleTaskResponse.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def scheduled_date(self):
        r"""Gets the scheduled_date of this CreateScheduleTaskResponse.

        周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。

        :return: The scheduled_date of this CreateScheduleTaskResponse.
        :rtype: str
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        r"""Sets the scheduled_date of this CreateScheduleTaskResponse.

        周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。

        :param scheduled_date: The scheduled_date of this CreateScheduleTaskResponse.
        :type scheduled_date: str
        """
        self._scheduled_date = scheduled_date

    @property
    def scheduled_time(self):
        r"""Gets the scheduled_time of this CreateScheduleTaskResponse.

        指定的执行时间点，格式为HH:mm:ss。

        :return: The scheduled_time of this CreateScheduleTaskResponse.
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        r"""Sets the scheduled_time of this CreateScheduleTaskResponse.

        指定的执行时间点，格式为HH:mm:ss。

        :param scheduled_time: The scheduled_time of this CreateScheduleTaskResponse.
        :type scheduled_time: str
        """
        self._scheduled_time = scheduled_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this CreateScheduleTaskResponse.

        到期时间。

        :return: The expire_time of this CreateScheduleTaskResponse.
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this CreateScheduleTaskResponse.

        到期时间。

        :param expire_time: The expire_time of this CreateScheduleTaskResponse.
        :type expire_time: datetime
        """
        self._expire_time = expire_time

    @property
    def description(self):
        r"""Gets the description of this CreateScheduleTaskResponse.

        任务描述。

        :return: The description of this CreateScheduleTaskResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateScheduleTaskResponse.

        任务描述。

        :param description: The description of this CreateScheduleTaskResponse.
        :type description: str
        """
        self._description = description

    @property
    def is_enable(self):
        r"""Gets the is_enable of this CreateScheduleTaskResponse.

        是否是开启状态。

        :return: The is_enable of this CreateScheduleTaskResponse.
        :rtype: bool
        """
        return self._is_enable

    @is_enable.setter
    def is_enable(self, is_enable):
        r"""Sets the is_enable of this CreateScheduleTaskResponse.

        是否是开启状态。

        :param is_enable: The is_enable of this CreateScheduleTaskResponse.
        :type is_enable: bool
        """
        self._is_enable = is_enable

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateScheduleTaskResponse.

        创建时间。

        :return: The create_time of this CreateScheduleTaskResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateScheduleTaskResponse.

        创建时间。

        :param create_time: The create_time of this CreateScheduleTaskResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateScheduleTaskResponse.

        更新时间。

        :return: The update_time of this CreateScheduleTaskResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateScheduleTaskResponse.

        更新时间。

        :param update_time: The update_time of this CreateScheduleTaskResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, CreateScheduleTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
