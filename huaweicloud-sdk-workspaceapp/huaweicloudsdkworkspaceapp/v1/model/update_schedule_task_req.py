# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScheduleTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scheduled_type': 'ScheduledTypeEnum',
        'day_interval': 'int',
        'week_list': 'str',
        'month_list': 'str',
        'date_list': 'str',
        'time_zone': 'str',
        'scheduled_date': 'str',
        'scheduled_time': 'str',
        'expire_time': 'datetime',
        'task_name': 'str',
        'task_type': 'ScheduleTaskTypeEnum',
        'schedule_task_policy': 'ScheduleTaskPolicy',
        'description': 'str',
        'is_enable': 'bool',
        'target_infos': 'list[TargetInfo]'
    }

    attribute_map = {
        'scheduled_type': 'scheduled_type',
        'day_interval': 'day_interval',
        'week_list': 'week_list',
        'month_list': 'month_list',
        'date_list': 'date_list',
        'time_zone': 'time_zone',
        'scheduled_date': 'scheduled_date',
        'scheduled_time': 'scheduled_time',
        'expire_time': 'expire_time',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'schedule_task_policy': 'schedule_task_policy',
        'description': 'description',
        'is_enable': 'is_enable',
        'target_infos': 'target_infos'
    }

    def __init__(self, scheduled_type=None, day_interval=None, week_list=None, month_list=None, date_list=None, time_zone=None, scheduled_date=None, scheduled_time=None, expire_time=None, task_name=None, task_type=None, schedule_task_policy=None, description=None, is_enable=None, target_infos=None):
        r"""UpdateScheduleTaskReq

        The model defined in huaweicloud sdk

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
        :param task_name: 任务名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成，不能有空格 2. 长度范围1~64个字符
        :type task_name: str
        :param task_type: 
        :type task_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        :param schedule_task_policy: 
        :type schedule_task_policy: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskPolicy`
        :param description: 任务描述。
        :type description: str
        :param is_enable: 是否启用： &#39;true&#39;: 启用 &#39;false&#39;: 禁用
        :type is_enable: bool
        :param target_infos: 定时任务对象列表。
        :type target_infos: list[:class:`huaweicloudsdkworkspaceapp.v1.TargetInfo`]
        """
        
        

        self._scheduled_type = None
        self._day_interval = None
        self._week_list = None
        self._month_list = None
        self._date_list = None
        self._time_zone = None
        self._scheduled_date = None
        self._scheduled_time = None
        self._expire_time = None
        self._task_name = None
        self._task_type = None
        self._schedule_task_policy = None
        self._description = None
        self._is_enable = None
        self._target_infos = None
        self.discriminator = None

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
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if schedule_task_policy is not None:
            self.schedule_task_policy = schedule_task_policy
        if description is not None:
            self.description = description
        if is_enable is not None:
            self.is_enable = is_enable
        if target_infos is not None:
            self.target_infos = target_infos

    @property
    def scheduled_type(self):
        r"""Gets the scheduled_type of this UpdateScheduleTaskReq.

        :return: The scheduled_type of this UpdateScheduleTaskReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduledTypeEnum`
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        r"""Sets the scheduled_type of this UpdateScheduleTaskReq.

        :param scheduled_type: The scheduled_type of this UpdateScheduleTaskReq.
        :type scheduled_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduledTypeEnum`
        """
        self._scheduled_type = scheduled_type

    @property
    def day_interval(self):
        r"""Gets the day_interval of this UpdateScheduleTaskReq.

        周期按天时：按x天间隔执行。

        :return: The day_interval of this UpdateScheduleTaskReq.
        :rtype: int
        """
        return self._day_interval

    @day_interval.setter
    def day_interval(self, day_interval):
        r"""Sets the day_interval of this UpdateScheduleTaskReq.

        周期按天时：按x天间隔执行。

        :param day_interval: The day_interval of this UpdateScheduleTaskReq.
        :type day_interval: int
        """
        self._day_interval = day_interval

    @property
    def week_list(self):
        r"""Gets the week_list of this UpdateScheduleTaskReq.

        周期按周时：取值1~7，英文逗号分隔，如1,2,7。

        :return: The week_list of this UpdateScheduleTaskReq.
        :rtype: str
        """
        return self._week_list

    @week_list.setter
    def week_list(self, week_list):
        r"""Sets the week_list of this UpdateScheduleTaskReq.

        周期按周时：取值1~7，英文逗号分隔，如1,2,7。

        :param week_list: The week_list of this UpdateScheduleTaskReq.
        :type week_list: str
        """
        self._week_list = week_list

    @property
    def month_list(self):
        r"""Gets the month_list of this UpdateScheduleTaskReq.

        周期按月时：取值1~12，英文逗号分隔，如1,3,12。

        :return: The month_list of this UpdateScheduleTaskReq.
        :rtype: str
        """
        return self._month_list

    @month_list.setter
    def month_list(self, month_list):
        r"""Sets the month_list of this UpdateScheduleTaskReq.

        周期按月时：取值1~12，英文逗号分隔，如1,3,12。

        :param month_list: The month_list of this UpdateScheduleTaskReq.
        :type month_list: str
        """
        self._month_list = month_list

    @property
    def date_list(self):
        r"""Gets the date_list of this UpdateScheduleTaskReq.

        周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。

        :return: The date_list of this UpdateScheduleTaskReq.
        :rtype: str
        """
        return self._date_list

    @date_list.setter
    def date_list(self, date_list):
        r"""Sets the date_list of this UpdateScheduleTaskReq.

        周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。

        :param date_list: The date_list of this UpdateScheduleTaskReq.
        :type date_list: str
        """
        self._date_list = date_list

    @property
    def time_zone(self):
        r"""Gets the time_zone of this UpdateScheduleTaskReq.

        时区。

        :return: The time_zone of this UpdateScheduleTaskReq.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this UpdateScheduleTaskReq.

        时区。

        :param time_zone: The time_zone of this UpdateScheduleTaskReq.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def scheduled_date(self):
        r"""Gets the scheduled_date of this UpdateScheduleTaskReq.

        周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。

        :return: The scheduled_date of this UpdateScheduleTaskReq.
        :rtype: str
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        r"""Sets the scheduled_date of this UpdateScheduleTaskReq.

        周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。

        :param scheduled_date: The scheduled_date of this UpdateScheduleTaskReq.
        :type scheduled_date: str
        """
        self._scheduled_date = scheduled_date

    @property
    def scheduled_time(self):
        r"""Gets the scheduled_time of this UpdateScheduleTaskReq.

        指定的执行时间点，格式为HH:mm:ss。

        :return: The scheduled_time of this UpdateScheduleTaskReq.
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        r"""Sets the scheduled_time of this UpdateScheduleTaskReq.

        指定的执行时间点，格式为HH:mm:ss。

        :param scheduled_time: The scheduled_time of this UpdateScheduleTaskReq.
        :type scheduled_time: str
        """
        self._scheduled_time = scheduled_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this UpdateScheduleTaskReq.

        到期时间。

        :return: The expire_time of this UpdateScheduleTaskReq.
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this UpdateScheduleTaskReq.

        到期时间。

        :param expire_time: The expire_time of this UpdateScheduleTaskReq.
        :type expire_time: datetime
        """
        self._expire_time = expire_time

    @property
    def task_name(self):
        r"""Gets the task_name of this UpdateScheduleTaskReq.

        任务名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成，不能有空格 2. 长度范围1~64个字符

        :return: The task_name of this UpdateScheduleTaskReq.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this UpdateScheduleTaskReq.

        任务名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成，不能有空格 2. 长度范围1~64个字符

        :param task_name: The task_name of this UpdateScheduleTaskReq.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        r"""Gets the task_type of this UpdateScheduleTaskReq.

        :return: The task_type of this UpdateScheduleTaskReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this UpdateScheduleTaskReq.

        :param task_type: The task_type of this UpdateScheduleTaskReq.
        :type task_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        """
        self._task_type = task_type

    @property
    def schedule_task_policy(self):
        r"""Gets the schedule_task_policy of this UpdateScheduleTaskReq.

        :return: The schedule_task_policy of this UpdateScheduleTaskReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskPolicy`
        """
        return self._schedule_task_policy

    @schedule_task_policy.setter
    def schedule_task_policy(self, schedule_task_policy):
        r"""Sets the schedule_task_policy of this UpdateScheduleTaskReq.

        :param schedule_task_policy: The schedule_task_policy of this UpdateScheduleTaskReq.
        :type schedule_task_policy: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskPolicy`
        """
        self._schedule_task_policy = schedule_task_policy

    @property
    def description(self):
        r"""Gets the description of this UpdateScheduleTaskReq.

        任务描述。

        :return: The description of this UpdateScheduleTaskReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateScheduleTaskReq.

        任务描述。

        :param description: The description of this UpdateScheduleTaskReq.
        :type description: str
        """
        self._description = description

    @property
    def is_enable(self):
        r"""Gets the is_enable of this UpdateScheduleTaskReq.

        是否启用： 'true': 启用 'false': 禁用

        :return: The is_enable of this UpdateScheduleTaskReq.
        :rtype: bool
        """
        return self._is_enable

    @is_enable.setter
    def is_enable(self, is_enable):
        r"""Sets the is_enable of this UpdateScheduleTaskReq.

        是否启用： 'true': 启用 'false': 禁用

        :param is_enable: The is_enable of this UpdateScheduleTaskReq.
        :type is_enable: bool
        """
        self._is_enable = is_enable

    @property
    def target_infos(self):
        r"""Gets the target_infos of this UpdateScheduleTaskReq.

        定时任务对象列表。

        :return: The target_infos of this UpdateScheduleTaskReq.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.TargetInfo`]
        """
        return self._target_infos

    @target_infos.setter
    def target_infos(self, target_infos):
        r"""Sets the target_infos of this UpdateScheduleTaskReq.

        定时任务对象列表。

        :param target_infos: The target_infos of this UpdateScheduleTaskReq.
        :type target_infos: list[:class:`huaweicloudsdkworkspaceapp.v1.TargetInfo`]
        """
        self._target_infos = target_infos

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
        if not isinstance(other, UpdateScheduleTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
