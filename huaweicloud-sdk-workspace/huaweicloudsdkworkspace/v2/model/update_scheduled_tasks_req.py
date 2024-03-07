# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScheduledTasksReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scheduled_type': 'str',
        'day_interval': 'int',
        'week_list': 'str',
        'month_list': 'str',
        'date_list': 'str',
        'scheduled_date': 'str',
        'scheduled_time': 'str',
        'expire_time': 'str',
        'gray_count': 'int',
        'gray_desktop_ids': 'list[str]',
        'gray_fail_threshold': 'int',
        'life_cycle_type': 'str',
        'time_zone': 'str',
        'task_name': 'str',
        'force_execute': 'bool',
        'description': 'str',
        'enable': 'bool',
        'extra_params': 'str',
        'apply_objects': 'list[ApplyObject]',
        'priority': 'int',
        'is_gray': 'bool'
    }

    attribute_map = {
        'scheduled_type': 'scheduled_type',
        'day_interval': 'day_interval',
        'week_list': 'week_list',
        'month_list': 'month_list',
        'date_list': 'date_list',
        'scheduled_date': 'scheduled_date',
        'scheduled_time': 'scheduled_time',
        'expire_time': 'expire_time',
        'gray_count': 'gray_count',
        'gray_desktop_ids': 'gray_desktop_ids',
        'gray_fail_threshold': 'gray_fail_threshold',
        'life_cycle_type': 'life_cycle_type',
        'time_zone': 'time_zone',
        'task_name': 'task_name',
        'force_execute': 'force_execute',
        'description': 'description',
        'enable': 'enable',
        'extra_params': 'extra_params',
        'apply_objects': 'apply_objects',
        'priority': 'priority',
        'is_gray': 'is_gray'
    }

    def __init__(self, scheduled_type=None, day_interval=None, week_list=None, month_list=None, date_list=None, scheduled_date=None, scheduled_time=None, expire_time=None, gray_count=None, gray_desktop_ids=None, gray_fail_threshold=None, life_cycle_type=None, time_zone=None, task_name=None, force_execute=None, description=None, enable=None, extra_params=None, apply_objects=None, priority=None, is_gray=None):
        """UpdateScheduledTasksReq

        The model defined in huaweicloud sdk

        :param scheduled_type: 执行周期类型，可选值为： - FIXED_TIME：指定时间。 - DAY：按天。 - WEEK：按周。 - MONTH：按月。 - LIFE_CYCLE：指定场景下触发。
        :type scheduled_type: str
        :param day_interval: 周期按天时：按x天间隔执行。
        :type day_interval: int
        :param week_list: 周期按周时：取值1~7，分别对应周日~周六，英文逗号分隔，如1,2,7。
        :type week_list: str
        :param month_list: 周期按月时：取值1~12，英文逗号分隔，如1,3,12。
        :type month_list: str
        :param date_list: 周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。
        :type date_list: str
        :param scheduled_date: 周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。
        :type scheduled_date: str
        :param scheduled_time: 指定的执行时间点，格式为HH:mm:ss。
        :type scheduled_time: str
        :param expire_time: 到期时间，格式为yyyy-MM-dd HH:mm:ss。
        :type expire_time: str
        :param gray_count: 灰度对象数量，优先级高于gray_desktop_ids。只支持脚本执行。
        :type gray_count: int
        :param gray_desktop_ids: 灰度执行的桌面id列表，优先级低于gray_count。只支持脚本执行。
        :type gray_desktop_ids: list[str]
        :param gray_fail_threshold: 灰度失败阈值，灰度执行失败次数达到该值时，不执行下一批任务。只支持脚本执行。
        :type gray_fail_threshold: int
        :param life_cycle_type: 触发场景。POST_CREATE_DESKTOP_SUCCESS：创建桌面成功后，POST_REBUILD_DESKTOP_SUCCESS：重建桌面成功后，POST_REATTACH_DESKTOP_SUCCESS：触发重建的分配用户任务成功后。
        :type life_cycle_type: str
        :param time_zone: 时区。
        :type time_zone: str
        :param task_name: 任务名称。
        :type task_name: str
        :param force_execute: 是否强制执行
        :type force_execute: bool
        :param description: 描述。
        :type description: str
        :param enable: 是否启用
        :type enable: bool
        :param extra_params: 扩展参数，json格式。
        :type extra_params: str
        :param apply_objects: 定时任务应用的对象列表。
        :type apply_objects: list[:class:`huaweicloudsdkworkspace.v2.ApplyObject`]
        :param priority: 优先级。触发式任务使用。
        :type priority: int
        :param is_gray: 任务是否灰度执行，供远程脚本使用。
        :type is_gray: bool
        """
        
        

        self._scheduled_type = None
        self._day_interval = None
        self._week_list = None
        self._month_list = None
        self._date_list = None
        self._scheduled_date = None
        self._scheduled_time = None
        self._expire_time = None
        self._gray_count = None
        self._gray_desktop_ids = None
        self._gray_fail_threshold = None
        self._life_cycle_type = None
        self._time_zone = None
        self._task_name = None
        self._force_execute = None
        self._description = None
        self._enable = None
        self._extra_params = None
        self._apply_objects = None
        self._priority = None
        self._is_gray = None
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
        if scheduled_date is not None:
            self.scheduled_date = scheduled_date
        if scheduled_time is not None:
            self.scheduled_time = scheduled_time
        if expire_time is not None:
            self.expire_time = expire_time
        if gray_count is not None:
            self.gray_count = gray_count
        if gray_desktop_ids is not None:
            self.gray_desktop_ids = gray_desktop_ids
        if gray_fail_threshold is not None:
            self.gray_fail_threshold = gray_fail_threshold
        if life_cycle_type is not None:
            self.life_cycle_type = life_cycle_type
        if time_zone is not None:
            self.time_zone = time_zone
        if task_name is not None:
            self.task_name = task_name
        if force_execute is not None:
            self.force_execute = force_execute
        if description is not None:
            self.description = description
        if enable is not None:
            self.enable = enable
        if extra_params is not None:
            self.extra_params = extra_params
        if apply_objects is not None:
            self.apply_objects = apply_objects
        if priority is not None:
            self.priority = priority
        if is_gray is not None:
            self.is_gray = is_gray

    @property
    def scheduled_type(self):
        """Gets the scheduled_type of this UpdateScheduledTasksReq.

        执行周期类型，可选值为： - FIXED_TIME：指定时间。 - DAY：按天。 - WEEK：按周。 - MONTH：按月。 - LIFE_CYCLE：指定场景下触发。

        :return: The scheduled_type of this UpdateScheduledTasksReq.
        :rtype: str
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        """Sets the scheduled_type of this UpdateScheduledTasksReq.

        执行周期类型，可选值为： - FIXED_TIME：指定时间。 - DAY：按天。 - WEEK：按周。 - MONTH：按月。 - LIFE_CYCLE：指定场景下触发。

        :param scheduled_type: The scheduled_type of this UpdateScheduledTasksReq.
        :type scheduled_type: str
        """
        self._scheduled_type = scheduled_type

    @property
    def day_interval(self):
        """Gets the day_interval of this UpdateScheduledTasksReq.

        周期按天时：按x天间隔执行。

        :return: The day_interval of this UpdateScheduledTasksReq.
        :rtype: int
        """
        return self._day_interval

    @day_interval.setter
    def day_interval(self, day_interval):
        """Sets the day_interval of this UpdateScheduledTasksReq.

        周期按天时：按x天间隔执行。

        :param day_interval: The day_interval of this UpdateScheduledTasksReq.
        :type day_interval: int
        """
        self._day_interval = day_interval

    @property
    def week_list(self):
        """Gets the week_list of this UpdateScheduledTasksReq.

        周期按周时：取值1~7，分别对应周日~周六，英文逗号分隔，如1,2,7。

        :return: The week_list of this UpdateScheduledTasksReq.
        :rtype: str
        """
        return self._week_list

    @week_list.setter
    def week_list(self, week_list):
        """Sets the week_list of this UpdateScheduledTasksReq.

        周期按周时：取值1~7，分别对应周日~周六，英文逗号分隔，如1,2,7。

        :param week_list: The week_list of this UpdateScheduledTasksReq.
        :type week_list: str
        """
        self._week_list = week_list

    @property
    def month_list(self):
        """Gets the month_list of this UpdateScheduledTasksReq.

        周期按月时：取值1~12，英文逗号分隔，如1,3,12。

        :return: The month_list of this UpdateScheduledTasksReq.
        :rtype: str
        """
        return self._month_list

    @month_list.setter
    def month_list(self, month_list):
        """Sets the month_list of this UpdateScheduledTasksReq.

        周期按月时：取值1~12，英文逗号分隔，如1,3,12。

        :param month_list: The month_list of this UpdateScheduledTasksReq.
        :type month_list: str
        """
        self._month_list = month_list

    @property
    def date_list(self):
        """Gets the date_list of this UpdateScheduledTasksReq.

        周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。

        :return: The date_list of this UpdateScheduledTasksReq.
        :rtype: str
        """
        return self._date_list

    @date_list.setter
    def date_list(self, date_list):
        """Sets the date_list of this UpdateScheduledTasksReq.

        周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。

        :param date_list: The date_list of this UpdateScheduledTasksReq.
        :type date_list: str
        """
        self._date_list = date_list

    @property
    def scheduled_date(self):
        """Gets the scheduled_date of this UpdateScheduledTasksReq.

        周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。

        :return: The scheduled_date of this UpdateScheduledTasksReq.
        :rtype: str
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        """Sets the scheduled_date of this UpdateScheduledTasksReq.

        周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。

        :param scheduled_date: The scheduled_date of this UpdateScheduledTasksReq.
        :type scheduled_date: str
        """
        self._scheduled_date = scheduled_date

    @property
    def scheduled_time(self):
        """Gets the scheduled_time of this UpdateScheduledTasksReq.

        指定的执行时间点，格式为HH:mm:ss。

        :return: The scheduled_time of this UpdateScheduledTasksReq.
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        """Sets the scheduled_time of this UpdateScheduledTasksReq.

        指定的执行时间点，格式为HH:mm:ss。

        :param scheduled_time: The scheduled_time of this UpdateScheduledTasksReq.
        :type scheduled_time: str
        """
        self._scheduled_time = scheduled_time

    @property
    def expire_time(self):
        """Gets the expire_time of this UpdateScheduledTasksReq.

        到期时间，格式为yyyy-MM-dd HH:mm:ss。

        :return: The expire_time of this UpdateScheduledTasksReq.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this UpdateScheduledTasksReq.

        到期时间，格式为yyyy-MM-dd HH:mm:ss。

        :param expire_time: The expire_time of this UpdateScheduledTasksReq.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def gray_count(self):
        """Gets the gray_count of this UpdateScheduledTasksReq.

        灰度对象数量，优先级高于gray_desktop_ids。只支持脚本执行。

        :return: The gray_count of this UpdateScheduledTasksReq.
        :rtype: int
        """
        return self._gray_count

    @gray_count.setter
    def gray_count(self, gray_count):
        """Sets the gray_count of this UpdateScheduledTasksReq.

        灰度对象数量，优先级高于gray_desktop_ids。只支持脚本执行。

        :param gray_count: The gray_count of this UpdateScheduledTasksReq.
        :type gray_count: int
        """
        self._gray_count = gray_count

    @property
    def gray_desktop_ids(self):
        """Gets the gray_desktop_ids of this UpdateScheduledTasksReq.

        灰度执行的桌面id列表，优先级低于gray_count。只支持脚本执行。

        :return: The gray_desktop_ids of this UpdateScheduledTasksReq.
        :rtype: list[str]
        """
        return self._gray_desktop_ids

    @gray_desktop_ids.setter
    def gray_desktop_ids(self, gray_desktop_ids):
        """Sets the gray_desktop_ids of this UpdateScheduledTasksReq.

        灰度执行的桌面id列表，优先级低于gray_count。只支持脚本执行。

        :param gray_desktop_ids: The gray_desktop_ids of this UpdateScheduledTasksReq.
        :type gray_desktop_ids: list[str]
        """
        self._gray_desktop_ids = gray_desktop_ids

    @property
    def gray_fail_threshold(self):
        """Gets the gray_fail_threshold of this UpdateScheduledTasksReq.

        灰度失败阈值，灰度执行失败次数达到该值时，不执行下一批任务。只支持脚本执行。

        :return: The gray_fail_threshold of this UpdateScheduledTasksReq.
        :rtype: int
        """
        return self._gray_fail_threshold

    @gray_fail_threshold.setter
    def gray_fail_threshold(self, gray_fail_threshold):
        """Sets the gray_fail_threshold of this UpdateScheduledTasksReq.

        灰度失败阈值，灰度执行失败次数达到该值时，不执行下一批任务。只支持脚本执行。

        :param gray_fail_threshold: The gray_fail_threshold of this UpdateScheduledTasksReq.
        :type gray_fail_threshold: int
        """
        self._gray_fail_threshold = gray_fail_threshold

    @property
    def life_cycle_type(self):
        """Gets the life_cycle_type of this UpdateScheduledTasksReq.

        触发场景。POST_CREATE_DESKTOP_SUCCESS：创建桌面成功后，POST_REBUILD_DESKTOP_SUCCESS：重建桌面成功后，POST_REATTACH_DESKTOP_SUCCESS：触发重建的分配用户任务成功后。

        :return: The life_cycle_type of this UpdateScheduledTasksReq.
        :rtype: str
        """
        return self._life_cycle_type

    @life_cycle_type.setter
    def life_cycle_type(self, life_cycle_type):
        """Sets the life_cycle_type of this UpdateScheduledTasksReq.

        触发场景。POST_CREATE_DESKTOP_SUCCESS：创建桌面成功后，POST_REBUILD_DESKTOP_SUCCESS：重建桌面成功后，POST_REATTACH_DESKTOP_SUCCESS：触发重建的分配用户任务成功后。

        :param life_cycle_type: The life_cycle_type of this UpdateScheduledTasksReq.
        :type life_cycle_type: str
        """
        self._life_cycle_type = life_cycle_type

    @property
    def time_zone(self):
        """Gets the time_zone of this UpdateScheduledTasksReq.

        时区。

        :return: The time_zone of this UpdateScheduledTasksReq.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this UpdateScheduledTasksReq.

        时区。

        :param time_zone: The time_zone of this UpdateScheduledTasksReq.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def task_name(self):
        """Gets the task_name of this UpdateScheduledTasksReq.

        任务名称。

        :return: The task_name of this UpdateScheduledTasksReq.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this UpdateScheduledTasksReq.

        任务名称。

        :param task_name: The task_name of this UpdateScheduledTasksReq.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def force_execute(self):
        """Gets the force_execute of this UpdateScheduledTasksReq.

        是否强制执行

        :return: The force_execute of this UpdateScheduledTasksReq.
        :rtype: bool
        """
        return self._force_execute

    @force_execute.setter
    def force_execute(self, force_execute):
        """Sets the force_execute of this UpdateScheduledTasksReq.

        是否强制执行

        :param force_execute: The force_execute of this UpdateScheduledTasksReq.
        :type force_execute: bool
        """
        self._force_execute = force_execute

    @property
    def description(self):
        """Gets the description of this UpdateScheduledTasksReq.

        描述。

        :return: The description of this UpdateScheduledTasksReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateScheduledTasksReq.

        描述。

        :param description: The description of this UpdateScheduledTasksReq.
        :type description: str
        """
        self._description = description

    @property
    def enable(self):
        """Gets the enable of this UpdateScheduledTasksReq.

        是否启用

        :return: The enable of this UpdateScheduledTasksReq.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this UpdateScheduledTasksReq.

        是否启用

        :param enable: The enable of this UpdateScheduledTasksReq.
        :type enable: bool
        """
        self._enable = enable

    @property
    def extra_params(self):
        """Gets the extra_params of this UpdateScheduledTasksReq.

        扩展参数，json格式。

        :return: The extra_params of this UpdateScheduledTasksReq.
        :rtype: str
        """
        return self._extra_params

    @extra_params.setter
    def extra_params(self, extra_params):
        """Sets the extra_params of this UpdateScheduledTasksReq.

        扩展参数，json格式。

        :param extra_params: The extra_params of this UpdateScheduledTasksReq.
        :type extra_params: str
        """
        self._extra_params = extra_params

    @property
    def apply_objects(self):
        """Gets the apply_objects of this UpdateScheduledTasksReq.

        定时任务应用的对象列表。

        :return: The apply_objects of this UpdateScheduledTasksReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ApplyObject`]
        """
        return self._apply_objects

    @apply_objects.setter
    def apply_objects(self, apply_objects):
        """Sets the apply_objects of this UpdateScheduledTasksReq.

        定时任务应用的对象列表。

        :param apply_objects: The apply_objects of this UpdateScheduledTasksReq.
        :type apply_objects: list[:class:`huaweicloudsdkworkspace.v2.ApplyObject`]
        """
        self._apply_objects = apply_objects

    @property
    def priority(self):
        """Gets the priority of this UpdateScheduledTasksReq.

        优先级。触发式任务使用。

        :return: The priority of this UpdateScheduledTasksReq.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this UpdateScheduledTasksReq.

        优先级。触发式任务使用。

        :param priority: The priority of this UpdateScheduledTasksReq.
        :type priority: int
        """
        self._priority = priority

    @property
    def is_gray(self):
        """Gets the is_gray of this UpdateScheduledTasksReq.

        任务是否灰度执行，供远程脚本使用。

        :return: The is_gray of this UpdateScheduledTasksReq.
        :rtype: bool
        """
        return self._is_gray

    @is_gray.setter
    def is_gray(self, is_gray):
        """Sets the is_gray of this UpdateScheduledTasksReq.

        任务是否灰度执行，供远程脚本使用。

        :param is_gray: The is_gray of this UpdateScheduledTasksReq.
        :type is_gray: bool
        """
        self._is_gray = is_gray

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
        if not isinstance(other, UpdateScheduledTasksReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
