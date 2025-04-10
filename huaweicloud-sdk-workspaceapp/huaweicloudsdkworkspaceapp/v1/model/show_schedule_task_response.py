# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowScheduleTaskResponse(SdkResponse):

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
        'task_type': 'ScheduleTaskTypeEnum',
        'task_name': 'str',
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
        'target_infos': 'list[TargetInfo]'
    }

    attribute_map = {
        'id': 'id',
        'task_type': 'task_type',
        'task_name': 'task_name',
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
        'target_infos': 'target_infos'
    }

    def __init__(self, id=None, task_type=None, task_name=None, schedule_task_policy=None, scheduled_type=None, day_interval=None, week_list=None, month_list=None, date_list=None, time_zone=None, scheduled_date=None, scheduled_time=None, expire_time=None, description=None, target_infos=None):
        r"""ShowScheduleTaskResponse

        The model defined in huaweicloud sdk

        :param id: 任务id。
        :type id: str
        :param task_type: 
        :type task_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        :param task_name: 任务名称。
        :type task_name: str
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
        :param expire_time: 到期时间，格式为。
        :type expire_time: datetime
        :param description: 描述。
        :type description: str
        :param target_infos: 定时任务应用的对象列表。
        :type target_infos: list[:class:`huaweicloudsdkworkspaceapp.v1.TargetInfo`]
        """
        
        super(ShowScheduleTaskResponse, self).__init__()

        self._id = None
        self._task_type = None
        self._task_name = None
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
        self._target_infos = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_type is not None:
            self.task_type = task_type
        if task_name is not None:
            self.task_name = task_name
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
        if target_infos is not None:
            self.target_infos = target_infos

    @property
    def id(self):
        r"""Gets the id of this ShowScheduleTaskResponse.

        任务id。

        :return: The id of this ShowScheduleTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowScheduleTaskResponse.

        任务id。

        :param id: The id of this ShowScheduleTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def task_type(self):
        r"""Gets the task_type of this ShowScheduleTaskResponse.

        :return: The task_type of this ShowScheduleTaskResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ShowScheduleTaskResponse.

        :param task_type: The task_type of this ShowScheduleTaskResponse.
        :type task_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskTypeEnum`
        """
        self._task_type = task_type

    @property
    def task_name(self):
        r"""Gets the task_name of this ShowScheduleTaskResponse.

        任务名称。

        :return: The task_name of this ShowScheduleTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ShowScheduleTaskResponse.

        任务名称。

        :param task_name: The task_name of this ShowScheduleTaskResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def schedule_task_policy(self):
        r"""Gets the schedule_task_policy of this ShowScheduleTaskResponse.

        :return: The schedule_task_policy of this ShowScheduleTaskResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskPolicy`
        """
        return self._schedule_task_policy

    @schedule_task_policy.setter
    def schedule_task_policy(self, schedule_task_policy):
        r"""Sets the schedule_task_policy of this ShowScheduleTaskResponse.

        :param schedule_task_policy: The schedule_task_policy of this ShowScheduleTaskResponse.
        :type schedule_task_policy: :class:`huaweicloudsdkworkspaceapp.v1.ScheduleTaskPolicy`
        """
        self._schedule_task_policy = schedule_task_policy

    @property
    def scheduled_type(self):
        r"""Gets the scheduled_type of this ShowScheduleTaskResponse.

        :return: The scheduled_type of this ShowScheduleTaskResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScheduledTypeEnum`
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        r"""Sets the scheduled_type of this ShowScheduleTaskResponse.

        :param scheduled_type: The scheduled_type of this ShowScheduleTaskResponse.
        :type scheduled_type: :class:`huaweicloudsdkworkspaceapp.v1.ScheduledTypeEnum`
        """
        self._scheduled_type = scheduled_type

    @property
    def day_interval(self):
        r"""Gets the day_interval of this ShowScheduleTaskResponse.

        周期按天时：按x天间隔执行。

        :return: The day_interval of this ShowScheduleTaskResponse.
        :rtype: int
        """
        return self._day_interval

    @day_interval.setter
    def day_interval(self, day_interval):
        r"""Sets the day_interval of this ShowScheduleTaskResponse.

        周期按天时：按x天间隔执行。

        :param day_interval: The day_interval of this ShowScheduleTaskResponse.
        :type day_interval: int
        """
        self._day_interval = day_interval

    @property
    def week_list(self):
        r"""Gets the week_list of this ShowScheduleTaskResponse.

        周期按周时：取值1~7，英文逗号分隔，如1,2,7。

        :return: The week_list of this ShowScheduleTaskResponse.
        :rtype: str
        """
        return self._week_list

    @week_list.setter
    def week_list(self, week_list):
        r"""Sets the week_list of this ShowScheduleTaskResponse.

        周期按周时：取值1~7，英文逗号分隔，如1,2,7。

        :param week_list: The week_list of this ShowScheduleTaskResponse.
        :type week_list: str
        """
        self._week_list = week_list

    @property
    def month_list(self):
        r"""Gets the month_list of this ShowScheduleTaskResponse.

        周期按月时：取值1~12，英文逗号分隔，如1,3,12。

        :return: The month_list of this ShowScheduleTaskResponse.
        :rtype: str
        """
        return self._month_list

    @month_list.setter
    def month_list(self, month_list):
        r"""Sets the month_list of this ShowScheduleTaskResponse.

        周期按月时：取值1~12，英文逗号分隔，如1,3,12。

        :param month_list: The month_list of this ShowScheduleTaskResponse.
        :type month_list: str
        """
        self._month_list = month_list

    @property
    def date_list(self):
        r"""Gets the date_list of this ShowScheduleTaskResponse.

        周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。

        :return: The date_list of this ShowScheduleTaskResponse.
        :rtype: str
        """
        return self._date_list

    @date_list.setter
    def date_list(self, date_list):
        r"""Sets the date_list of this ShowScheduleTaskResponse.

        周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。

        :param date_list: The date_list of this ShowScheduleTaskResponse.
        :type date_list: str
        """
        self._date_list = date_list

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ShowScheduleTaskResponse.

        时区。

        :return: The time_zone of this ShowScheduleTaskResponse.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ShowScheduleTaskResponse.

        时区。

        :param time_zone: The time_zone of this ShowScheduleTaskResponse.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def scheduled_date(self):
        r"""Gets the scheduled_date of this ShowScheduleTaskResponse.

        周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。

        :return: The scheduled_date of this ShowScheduleTaskResponse.
        :rtype: str
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        r"""Sets the scheduled_date of this ShowScheduleTaskResponse.

        周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。

        :param scheduled_date: The scheduled_date of this ShowScheduleTaskResponse.
        :type scheduled_date: str
        """
        self._scheduled_date = scheduled_date

    @property
    def scheduled_time(self):
        r"""Gets the scheduled_time of this ShowScheduleTaskResponse.

        指定的执行时间点，格式为HH:mm:ss。

        :return: The scheduled_time of this ShowScheduleTaskResponse.
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        r"""Sets the scheduled_time of this ShowScheduleTaskResponse.

        指定的执行时间点，格式为HH:mm:ss。

        :param scheduled_time: The scheduled_time of this ShowScheduleTaskResponse.
        :type scheduled_time: str
        """
        self._scheduled_time = scheduled_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ShowScheduleTaskResponse.

        到期时间，格式为。

        :return: The expire_time of this ShowScheduleTaskResponse.
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ShowScheduleTaskResponse.

        到期时间，格式为。

        :param expire_time: The expire_time of this ShowScheduleTaskResponse.
        :type expire_time: datetime
        """
        self._expire_time = expire_time

    @property
    def description(self):
        r"""Gets the description of this ShowScheduleTaskResponse.

        描述。

        :return: The description of this ShowScheduleTaskResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowScheduleTaskResponse.

        描述。

        :param description: The description of this ShowScheduleTaskResponse.
        :type description: str
        """
        self._description = description

    @property
    def target_infos(self):
        r"""Gets the target_infos of this ShowScheduleTaskResponse.

        定时任务应用的对象列表。

        :return: The target_infos of this ShowScheduleTaskResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.TargetInfo`]
        """
        return self._target_infos

    @target_infos.setter
    def target_infos(self, target_infos):
        r"""Sets the target_infos of this ShowScheduleTaskResponse.

        定时任务应用的对象列表。

        :param target_infos: The target_infos of this ShowScheduleTaskResponse.
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
        if not isinstance(other, ShowScheduleTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
