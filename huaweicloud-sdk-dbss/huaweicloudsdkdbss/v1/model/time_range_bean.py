# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimeRangeBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_time': 'str',
        'start_time': 'str',
        'time_range': 'str'
    }

    attribute_map = {
        'end_time': 'end_time',
        'start_time': 'start_time',
        'time_range': 'time_range'
    }

    def __init__(self, end_time=None, start_time=None, time_range=None):
        r"""TimeRangeBean

        The model defined in huaweicloud sdk

        :param end_time: 开始时间，必须和end_time成对出现。格式必须为yyyy-MM-dd HH:mm:ss。UTC时间
        :type end_time: str
        :param start_time: 结束时间，必须和start_time成对出现。格式必须为yyyy-MM-dd HH:mm:ss。UTC时间
        :type start_time: str
        :param time_range: 请求查询的时间段，和start_time，end_time不能同时使用，同时传该参数优先级更高。 - HALF_HOUR - HOUR - THREE_HOUR - TWELVE_HOUR - DAY - WEEK - MONTH
        :type time_range: str
        """
        
        

        self._end_time = None
        self._start_time = None
        self._time_range = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if start_time is not None:
            self.start_time = start_time
        if time_range is not None:
            self.time_range = time_range

    @property
    def end_time(self):
        r"""Gets the end_time of this TimeRangeBean.

        开始时间，必须和end_time成对出现。格式必须为yyyy-MM-dd HH:mm:ss。UTC时间

        :return: The end_time of this TimeRangeBean.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TimeRangeBean.

        开始时间，必须和end_time成对出现。格式必须为yyyy-MM-dd HH:mm:ss。UTC时间

        :param end_time: The end_time of this TimeRangeBean.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def start_time(self):
        r"""Gets the start_time of this TimeRangeBean.

        结束时间，必须和start_time成对出现。格式必须为yyyy-MM-dd HH:mm:ss。UTC时间

        :return: The start_time of this TimeRangeBean.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TimeRangeBean.

        结束时间，必须和start_time成对出现。格式必须为yyyy-MM-dd HH:mm:ss。UTC时间

        :param start_time: The start_time of this TimeRangeBean.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def time_range(self):
        r"""Gets the time_range of this TimeRangeBean.

        请求查询的时间段，和start_time，end_time不能同时使用，同时传该参数优先级更高。 - HALF_HOUR - HOUR - THREE_HOUR - TWELVE_HOUR - DAY - WEEK - MONTH

        :return: The time_range of this TimeRangeBean.
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        r"""Sets the time_range of this TimeRangeBean.

        请求查询的时间段，和start_time，end_time不能同时使用，同时传该参数优先级更高。 - HALF_HOUR - HOUR - THREE_HOUR - TWELVE_HOUR - DAY - WEEK - MONTH

        :param time_range: The time_range of this TimeRangeBean.
        :type time_range: str
        """
        self._time_range = time_range

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
        if not isinstance(other, TimeRangeBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
