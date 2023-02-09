# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecurrenceSchedule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'day_of_month': 'str',
        'day_of_week': 'str',
        'hour': 'str',
        'minute': 'str',
        'month': 'str',
        'year': 'str'
    }

    attribute_map = {
        'day_of_month': 'day_of_month',
        'day_of_week': 'day_of_week',
        'hour': 'hour',
        'minute': 'minute',
        'month': 'month',
        'year': 'year'
    }

    def __init__(self, day_of_month=None, day_of_week=None, hour=None, minute=None, month=None, year=None):
        """RecurrenceSchedule

        The model defined in huaweicloud sdk

        :param day_of_month: 日期按月
        :type day_of_month: str
        :param day_of_week: 日期按星期
        :type day_of_week: str
        :param hour: 时
        :type hour: str
        :param minute: 分
        :type minute: str
        :param month: 月
        :type month: str
        :param year: 年
        :type year: str
        """
        
        

        self._day_of_month = None
        self._day_of_week = None
        self._hour = None
        self._minute = None
        self._month = None
        self._year = None
        self.discriminator = None

        if day_of_month is not None:
            self.day_of_month = day_of_month
        if day_of_week is not None:
            self.day_of_week = day_of_week
        if hour is not None:
            self.hour = hour
        if minute is not None:
            self.minute = minute
        if month is not None:
            self.month = month
        if year is not None:
            self.year = year

    @property
    def day_of_month(self):
        """Gets the day_of_month of this RecurrenceSchedule.

        日期按月

        :return: The day_of_month of this RecurrenceSchedule.
        :rtype: str
        """
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month):
        """Sets the day_of_month of this RecurrenceSchedule.

        日期按月

        :param day_of_month: The day_of_month of this RecurrenceSchedule.
        :type day_of_month: str
        """
        self._day_of_month = day_of_month

    @property
    def day_of_week(self):
        """Gets the day_of_week of this RecurrenceSchedule.

        日期按星期

        :return: The day_of_week of this RecurrenceSchedule.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this RecurrenceSchedule.

        日期按星期

        :param day_of_week: The day_of_week of this RecurrenceSchedule.
        :type day_of_week: str
        """
        self._day_of_week = day_of_week

    @property
    def hour(self):
        """Gets the hour of this RecurrenceSchedule.

        时

        :return: The hour of this RecurrenceSchedule.
        :rtype: str
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Sets the hour of this RecurrenceSchedule.

        时

        :param hour: The hour of this RecurrenceSchedule.
        :type hour: str
        """
        self._hour = hour

    @property
    def minute(self):
        """Gets the minute of this RecurrenceSchedule.

        分

        :return: The minute of this RecurrenceSchedule.
        :rtype: str
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Sets the minute of this RecurrenceSchedule.

        分

        :param minute: The minute of this RecurrenceSchedule.
        :type minute: str
        """
        self._minute = minute

    @property
    def month(self):
        """Gets the month of this RecurrenceSchedule.

        月

        :return: The month of this RecurrenceSchedule.
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this RecurrenceSchedule.

        月

        :param month: The month of this RecurrenceSchedule.
        :type month: str
        """
        self._month = month

    @property
    def year(self):
        """Gets the year of this RecurrenceSchedule.

        年

        :return: The year of this RecurrenceSchedule.
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this RecurrenceSchedule.

        年

        :param year: The year of this RecurrenceSchedule.
        :type year: str
        """
        self._year = year

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
        if not isinstance(other, RecurrenceSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
