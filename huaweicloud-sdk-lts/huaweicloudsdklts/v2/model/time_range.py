# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimeRange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_time_zone': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'start_time_gt': 'bool',
        'end_time_lt': 'bool'
    }

    attribute_map = {
        'sql_time_zone': 'sql_time_zone',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'start_time_gt': 'start_time_gt',
        'end_time_lt': 'end_time_lt'
    }

    def __init__(self, sql_time_zone=None, start_time=None, end_time=None, start_time_gt=None, end_time_lt=None):
        """TimeRange

        The model defined in huaweicloud sdk

        :param sql_time_zone: 时区信息，默认为“UTC”。
        :type sql_time_zone: str
        :param start_time: 搜索起始时间（UTC时间，毫秒级）。
        :type start_time: str
        :param end_time: 搜索起始时间（UTC时间，毫秒级）。
        :type end_time: str
        :param start_time_gt: 搜索是否包含起始时间点，默认为false。
        :type start_time_gt: bool
        :param end_time_lt: 搜索是否包含结束时间点，默认为false。
        :type end_time_lt: bool
        """
        
        

        self._sql_time_zone = None
        self._start_time = None
        self._end_time = None
        self._start_time_gt = None
        self._end_time_lt = None
        self.discriminator = None

        if sql_time_zone is not None:
            self.sql_time_zone = sql_time_zone
        self.start_time = start_time
        self.end_time = end_time
        if start_time_gt is not None:
            self.start_time_gt = start_time_gt
        if end_time_lt is not None:
            self.end_time_lt = end_time_lt

    @property
    def sql_time_zone(self):
        """Gets the sql_time_zone of this TimeRange.

        时区信息，默认为“UTC”。

        :return: The sql_time_zone of this TimeRange.
        :rtype: str
        """
        return self._sql_time_zone

    @sql_time_zone.setter
    def sql_time_zone(self, sql_time_zone):
        """Sets the sql_time_zone of this TimeRange.

        时区信息，默认为“UTC”。

        :param sql_time_zone: The sql_time_zone of this TimeRange.
        :type sql_time_zone: str
        """
        self._sql_time_zone = sql_time_zone

    @property
    def start_time(self):
        """Gets the start_time of this TimeRange.

        搜索起始时间（UTC时间，毫秒级）。

        :return: The start_time of this TimeRange.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TimeRange.

        搜索起始时间（UTC时间，毫秒级）。

        :param start_time: The start_time of this TimeRange.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TimeRange.

        搜索起始时间（UTC时间，毫秒级）。

        :return: The end_time of this TimeRange.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TimeRange.

        搜索起始时间（UTC时间，毫秒级）。

        :param end_time: The end_time of this TimeRange.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def start_time_gt(self):
        """Gets the start_time_gt of this TimeRange.

        搜索是否包含起始时间点，默认为false。

        :return: The start_time_gt of this TimeRange.
        :rtype: bool
        """
        return self._start_time_gt

    @start_time_gt.setter
    def start_time_gt(self, start_time_gt):
        """Sets the start_time_gt of this TimeRange.

        搜索是否包含起始时间点，默认为false。

        :param start_time_gt: The start_time_gt of this TimeRange.
        :type start_time_gt: bool
        """
        self._start_time_gt = start_time_gt

    @property
    def end_time_lt(self):
        """Gets the end_time_lt of this TimeRange.

        搜索是否包含结束时间点，默认为false。

        :return: The end_time_lt of this TimeRange.
        :rtype: bool
        """
        return self._end_time_lt

    @end_time_lt.setter
    def end_time_lt(self, end_time_lt):
        """Sets the end_time_lt of this TimeRange.

        搜索是否包含结束时间点，默认为false。

        :param end_time_lt: The end_time_lt of this TimeRange.
        :type end_time_lt: bool
        """
        self._end_time_lt = end_time_lt

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
        if not isinstance(other, TimeRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
