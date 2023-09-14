# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupplementDataInfoSupplementDataRunTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_of_day': 'str',
        'day_of_week': 'str',
        'day_of_month': 'str'
    }

    attribute_map = {
        'time_of_day': 'time_of_day',
        'day_of_week': 'day_of_week',
        'day_of_month': 'day_of_month'
    }

    def __init__(self, time_of_day=None, day_of_week=None, day_of_month=None):
        """SupplementDataInfoSupplementDataRunTime

        The model defined in huaweicloud sdk

        :param time_of_day: 每天的可补数据时间段，如：每天的10点15分到23点30分，表示：10:15-23:30
        :type time_of_day: str
        :param day_of_week: 每周的星期几可以补数据，如：每周一，周三的每天10点15分到23点30分。
        :type day_of_week: str
        :param day_of_month: 每个月的哪几天可以补数据，如每月1号，3号，表示：1,3
        :type day_of_month: str
        """
        
        

        self._time_of_day = None
        self._day_of_week = None
        self._day_of_month = None
        self.discriminator = None

        if time_of_day is not None:
            self.time_of_day = time_of_day
        if day_of_week is not None:
            self.day_of_week = day_of_week
        if day_of_month is not None:
            self.day_of_month = day_of_month

    @property
    def time_of_day(self):
        """Gets the time_of_day of this SupplementDataInfoSupplementDataRunTime.

        每天的可补数据时间段，如：每天的10点15分到23点30分，表示：10:15-23:30

        :return: The time_of_day of this SupplementDataInfoSupplementDataRunTime.
        :rtype: str
        """
        return self._time_of_day

    @time_of_day.setter
    def time_of_day(self, time_of_day):
        """Sets the time_of_day of this SupplementDataInfoSupplementDataRunTime.

        每天的可补数据时间段，如：每天的10点15分到23点30分，表示：10:15-23:30

        :param time_of_day: The time_of_day of this SupplementDataInfoSupplementDataRunTime.
        :type time_of_day: str
        """
        self._time_of_day = time_of_day

    @property
    def day_of_week(self):
        """Gets the day_of_week of this SupplementDataInfoSupplementDataRunTime.

        每周的星期几可以补数据，如：每周一，周三的每天10点15分到23点30分。

        :return: The day_of_week of this SupplementDataInfoSupplementDataRunTime.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this SupplementDataInfoSupplementDataRunTime.

        每周的星期几可以补数据，如：每周一，周三的每天10点15分到23点30分。

        :param day_of_week: The day_of_week of this SupplementDataInfoSupplementDataRunTime.
        :type day_of_week: str
        """
        self._day_of_week = day_of_week

    @property
    def day_of_month(self):
        """Gets the day_of_month of this SupplementDataInfoSupplementDataRunTime.

        每个月的哪几天可以补数据，如每月1号，3号，表示：1,3

        :return: The day_of_month of this SupplementDataInfoSupplementDataRunTime.
        :rtype: str
        """
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month):
        """Sets the day_of_month of this SupplementDataInfoSupplementDataRunTime.

        每个月的哪几天可以补数据，如每月1号，3号，表示：1,3

        :param day_of_month: The day_of_month of this SupplementDataInfoSupplementDataRunTime.
        :type day_of_month: str
        """
        self._day_of_month = day_of_month

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
        if not isinstance(other, SupplementDataInfoSupplementDataRunTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
