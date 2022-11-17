# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskTiming:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'timezone': 'str',
        'days_of_week': 'list[int]',
        'days_of_month': 'list[int]',
        'date': 'str',
        'periods': 'list[TaskTimingPeriods]',
        'frequency': 'TaskTimingFrequency'
    }

    attribute_map = {
        'type': 'type',
        'timezone': 'timezone',
        'days_of_week': 'days_of_week',
        'days_of_month': 'days_of_month',
        'date': 'date',
        'periods': 'periods',
        'frequency': 'frequency'
    }

    def __init__(self, type=None, timezone=None, days_of_week=None, days_of_month=None, date=None, periods=None, frequency=None):
        """TaskTiming

        The model defined in huaweicloud sdk

        :param type: 计划任务的类型，使用计划任务时必填。可选类型分别为once（仅执行一次），daily（每日执行），weekly（每周执行），monthly（每月执行）。
        :type type: str
        :param timezone: 用户所处的时区，使用计划任务时必填。精确到分钟。
        :type timezone: str
        :param days_of_week: 作业会在一周的哪几天执行，当且仅当计划任务类型为weekly时，该字段需填且必填。1~7分别指代星期一至星期日。
        :type days_of_week: list[int]
        :param days_of_month: 作业会在一个月的哪几天执行，当且仅当计划任务类型为monthly时，该字段需填且必填。1~31分别指代一个月中的1日至31日。
        :type days_of_month: list[int]
        :param date: 作业的执行日。当且仅当计划任务类型为once且为频率模式时，该字段需填且必填。格式形如yyyy-MM-dd。
        :type date: str
        :param periods: 时间段模式配置。和frequency字段二选一，不可共存。时间段模式下，至少需指定一个时间段。
        :type periods: list[:class:`huaweicloudsdkvas.v2.TaskTimingPeriods`]
        :param frequency: 
        :type frequency: :class:`huaweicloudsdkvas.v2.TaskTimingFrequency`
        """
        
        

        self._type = None
        self._timezone = None
        self._days_of_week = None
        self._days_of_month = None
        self._date = None
        self._periods = None
        self._frequency = None
        self.discriminator = None

        self.type = type
        self.timezone = timezone
        if days_of_week is not None:
            self.days_of_week = days_of_week
        if days_of_month is not None:
            self.days_of_month = days_of_month
        if date is not None:
            self.date = date
        if periods is not None:
            self.periods = periods
        if frequency is not None:
            self.frequency = frequency

    @property
    def type(self):
        """Gets the type of this TaskTiming.

        计划任务的类型，使用计划任务时必填。可选类型分别为once（仅执行一次），daily（每日执行），weekly（每周执行），monthly（每月执行）。

        :return: The type of this TaskTiming.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskTiming.

        计划任务的类型，使用计划任务时必填。可选类型分别为once（仅执行一次），daily（每日执行），weekly（每周执行），monthly（每月执行）。

        :param type: The type of this TaskTiming.
        :type type: str
        """
        self._type = type

    @property
    def timezone(self):
        """Gets the timezone of this TaskTiming.

        用户所处的时区，使用计划任务时必填。精确到分钟。

        :return: The timezone of this TaskTiming.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this TaskTiming.

        用户所处的时区，使用计划任务时必填。精确到分钟。

        :param timezone: The timezone of this TaskTiming.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def days_of_week(self):
        """Gets the days_of_week of this TaskTiming.

        作业会在一周的哪几天执行，当且仅当计划任务类型为weekly时，该字段需填且必填。1~7分别指代星期一至星期日。

        :return: The days_of_week of this TaskTiming.
        :rtype: list[int]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        """Sets the days_of_week of this TaskTiming.

        作业会在一周的哪几天执行，当且仅当计划任务类型为weekly时，该字段需填且必填。1~7分别指代星期一至星期日。

        :param days_of_week: The days_of_week of this TaskTiming.
        :type days_of_week: list[int]
        """
        self._days_of_week = days_of_week

    @property
    def days_of_month(self):
        """Gets the days_of_month of this TaskTiming.

        作业会在一个月的哪几天执行，当且仅当计划任务类型为monthly时，该字段需填且必填。1~31分别指代一个月中的1日至31日。

        :return: The days_of_month of this TaskTiming.
        :rtype: list[int]
        """
        return self._days_of_month

    @days_of_month.setter
    def days_of_month(self, days_of_month):
        """Sets the days_of_month of this TaskTiming.

        作业会在一个月的哪几天执行，当且仅当计划任务类型为monthly时，该字段需填且必填。1~31分别指代一个月中的1日至31日。

        :param days_of_month: The days_of_month of this TaskTiming.
        :type days_of_month: list[int]
        """
        self._days_of_month = days_of_month

    @property
    def date(self):
        """Gets the date of this TaskTiming.

        作业的执行日。当且仅当计划任务类型为once且为频率模式时，该字段需填且必填。格式形如yyyy-MM-dd。

        :return: The date of this TaskTiming.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TaskTiming.

        作业的执行日。当且仅当计划任务类型为once且为频率模式时，该字段需填且必填。格式形如yyyy-MM-dd。

        :param date: The date of this TaskTiming.
        :type date: str
        """
        self._date = date

    @property
    def periods(self):
        """Gets the periods of this TaskTiming.

        时间段模式配置。和frequency字段二选一，不可共存。时间段模式下，至少需指定一个时间段。

        :return: The periods of this TaskTiming.
        :rtype: list[:class:`huaweicloudsdkvas.v2.TaskTimingPeriods`]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this TaskTiming.

        时间段模式配置。和frequency字段二选一，不可共存。时间段模式下，至少需指定一个时间段。

        :param periods: The periods of this TaskTiming.
        :type periods: list[:class:`huaweicloudsdkvas.v2.TaskTimingPeriods`]
        """
        self._periods = periods

    @property
    def frequency(self):
        """Gets the frequency of this TaskTiming.

        :return: The frequency of this TaskTiming.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskTimingFrequency`
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this TaskTiming.

        :param frequency: The frequency of this TaskTiming.
        :type frequency: :class:`huaweicloudsdkvas.v2.TaskTimingFrequency`
        """
        self._frequency = frequency

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
        if not isinstance(other, TaskTiming):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
