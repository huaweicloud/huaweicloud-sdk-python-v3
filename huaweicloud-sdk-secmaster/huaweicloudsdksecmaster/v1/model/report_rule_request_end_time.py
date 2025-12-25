# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportRuleRequestEndTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'day': 'int',
        'week': 'int',
        'month': 'int',
        'time': 'str'
    }

    attribute_map = {
        'day': 'day',
        'week': 'week',
        'month': 'month',
        'time': 'time'
    }

    def __init__(self, day=None, week=None, month=None, time=None):
        r"""ReportRuleRequestEndTime

        The model defined in huaweicloud sdk

        :param day: 报告统计周期的日期，前一天为-1，当天为0
        :type day: int
        :param week: 报告统计周期的日期，前一周为-1，本周为0
        :type week: int
        :param month: 报告统计周期的日期，上一月为-1，本月为0
        :type month: int
        :param time: 报告统计周期的结束，具体时间，时分秒格式
        :type time: str
        """
        
        

        self._day = None
        self._week = None
        self._month = None
        self._time = None
        self.discriminator = None

        if day is not None:
            self.day = day
        if week is not None:
            self.week = week
        if month is not None:
            self.month = month
        if time is not None:
            self.time = time

    @property
    def day(self):
        r"""Gets the day of this ReportRuleRequestEndTime.

        报告统计周期的日期，前一天为-1，当天为0

        :return: The day of this ReportRuleRequestEndTime.
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        r"""Sets the day of this ReportRuleRequestEndTime.

        报告统计周期的日期，前一天为-1，当天为0

        :param day: The day of this ReportRuleRequestEndTime.
        :type day: int
        """
        self._day = day

    @property
    def week(self):
        r"""Gets the week of this ReportRuleRequestEndTime.

        报告统计周期的日期，前一周为-1，本周为0

        :return: The week of this ReportRuleRequestEndTime.
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        r"""Sets the week of this ReportRuleRequestEndTime.

        报告统计周期的日期，前一周为-1，本周为0

        :param week: The week of this ReportRuleRequestEndTime.
        :type week: int
        """
        self._week = week

    @property
    def month(self):
        r"""Gets the month of this ReportRuleRequestEndTime.

        报告统计周期的日期，上一月为-1，本月为0

        :return: The month of this ReportRuleRequestEndTime.
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        r"""Sets the month of this ReportRuleRequestEndTime.

        报告统计周期的日期，上一月为-1，本月为0

        :param month: The month of this ReportRuleRequestEndTime.
        :type month: int
        """
        self._month = month

    @property
    def time(self):
        r"""Gets the time of this ReportRuleRequestEndTime.

        报告统计周期的结束，具体时间，时分秒格式

        :return: The time of this ReportRuleRequestEndTime.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ReportRuleRequestEndTime.

        报告统计周期的结束，具体时间，时分秒格式

        :param time: The time of this ReportRuleRequestEndTime.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, ReportRuleRequestEndTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
