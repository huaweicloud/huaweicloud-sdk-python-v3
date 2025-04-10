# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledTaskConfig:

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
        'time_zone': 'str',
        'scheduled_date': 'str',
        'scheduled_time': 'str',
        'expire_time': 'datetime'
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
        'expire_time': 'expire_time'
    }

    def __init__(self, scheduled_type=None, day_interval=None, week_list=None, month_list=None, date_list=None, time_zone=None, scheduled_date=None, scheduled_time=None, expire_time=None):
        r"""ScheduledTaskConfig

        The model defined in huaweicloud sdk

        :param scheduled_type: 执行周期类型，可选值为： - FIXED_TIME：指定时间。 - DAY：按天。 - WEEK：按周。 - MONTH：按月。
        :type scheduled_type: str
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

    @property
    def scheduled_type(self):
        r"""Gets the scheduled_type of this ScheduledTaskConfig.

        执行周期类型，可选值为： - FIXED_TIME：指定时间。 - DAY：按天。 - WEEK：按周。 - MONTH：按月。

        :return: The scheduled_type of this ScheduledTaskConfig.
        :rtype: str
        """
        return self._scheduled_type

    @scheduled_type.setter
    def scheduled_type(self, scheduled_type):
        r"""Sets the scheduled_type of this ScheduledTaskConfig.

        执行周期类型，可选值为： - FIXED_TIME：指定时间。 - DAY：按天。 - WEEK：按周。 - MONTH：按月。

        :param scheduled_type: The scheduled_type of this ScheduledTaskConfig.
        :type scheduled_type: str
        """
        self._scheduled_type = scheduled_type

    @property
    def day_interval(self):
        r"""Gets the day_interval of this ScheduledTaskConfig.

        周期按天时：按x天间隔执行。

        :return: The day_interval of this ScheduledTaskConfig.
        :rtype: int
        """
        return self._day_interval

    @day_interval.setter
    def day_interval(self, day_interval):
        r"""Sets the day_interval of this ScheduledTaskConfig.

        周期按天时：按x天间隔执行。

        :param day_interval: The day_interval of this ScheduledTaskConfig.
        :type day_interval: int
        """
        self._day_interval = day_interval

    @property
    def week_list(self):
        r"""Gets the week_list of this ScheduledTaskConfig.

        周期按周时：取值1~7，英文逗号分隔，如1,2,7。

        :return: The week_list of this ScheduledTaskConfig.
        :rtype: str
        """
        return self._week_list

    @week_list.setter
    def week_list(self, week_list):
        r"""Sets the week_list of this ScheduledTaskConfig.

        周期按周时：取值1~7，英文逗号分隔，如1,2,7。

        :param week_list: The week_list of this ScheduledTaskConfig.
        :type week_list: str
        """
        self._week_list = week_list

    @property
    def month_list(self):
        r"""Gets the month_list of this ScheduledTaskConfig.

        周期按月时：取值1~12，英文逗号分隔，如1,3,12。

        :return: The month_list of this ScheduledTaskConfig.
        :rtype: str
        """
        return self._month_list

    @month_list.setter
    def month_list(self, month_list):
        r"""Sets the month_list of this ScheduledTaskConfig.

        周期按月时：取值1~12，英文逗号分隔，如1,3,12。

        :param month_list: The month_list of this ScheduledTaskConfig.
        :type month_list: str
        """
        self._month_list = month_list

    @property
    def date_list(self):
        r"""Gets the date_list of this ScheduledTaskConfig.

        周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。

        :return: The date_list of this ScheduledTaskConfig.
        :rtype: str
        """
        return self._date_list

    @date_list.setter
    def date_list(self, date_list):
        r"""Sets the date_list of this ScheduledTaskConfig.

        周期按月时：取值1~31及L(代表当月最后一天)，英文逗号分隔，如1,2,28,L。

        :param date_list: The date_list of this ScheduledTaskConfig.
        :type date_list: str
        """
        self._date_list = date_list

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ScheduledTaskConfig.

        时区。

        :return: The time_zone of this ScheduledTaskConfig.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ScheduledTaskConfig.

        时区。

        :param time_zone: The time_zone of this ScheduledTaskConfig.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def scheduled_date(self):
        r"""Gets the scheduled_date of this ScheduledTaskConfig.

        周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。

        :return: The scheduled_date of this ScheduledTaskConfig.
        :rtype: str
        """
        return self._scheduled_date

    @scheduled_date.setter
    def scheduled_date(self, scheduled_date):
        r"""Sets the scheduled_date of this ScheduledTaskConfig.

        周期指定时间时：表示指定的日期，格式为yyyy-MM-dd。

        :param scheduled_date: The scheduled_date of this ScheduledTaskConfig.
        :type scheduled_date: str
        """
        self._scheduled_date = scheduled_date

    @property
    def scheduled_time(self):
        r"""Gets the scheduled_time of this ScheduledTaskConfig.

        指定的执行时间点，格式为HH:mm:ss。

        :return: The scheduled_time of this ScheduledTaskConfig.
        :rtype: str
        """
        return self._scheduled_time

    @scheduled_time.setter
    def scheduled_time(self, scheduled_time):
        r"""Sets the scheduled_time of this ScheduledTaskConfig.

        指定的执行时间点，格式为HH:mm:ss。

        :param scheduled_time: The scheduled_time of this ScheduledTaskConfig.
        :type scheduled_time: str
        """
        self._scheduled_time = scheduled_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ScheduledTaskConfig.

        到期时间。

        :return: The expire_time of this ScheduledTaskConfig.
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ScheduledTaskConfig.

        到期时间。

        :param expire_time: The expire_time of this ScheduledTaskConfig.
        :type expire_time: datetime
        """
        self._expire_time = expire_time

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
        if not isinstance(other, ScheduledTaskConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
