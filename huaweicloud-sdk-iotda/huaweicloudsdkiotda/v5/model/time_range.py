# coding: utf-8

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
        'start_time': 'str',
        'end_time': 'str',
        'days_of_week': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'days_of_week': 'days_of_week'
    }

    def __init__(self, start_time=None, end_time=None, days_of_week=None):
        r"""TimeRange

        The model defined in huaweicloud sdk

        :param start_time: **参数说明**：规则条件触发的开始时间，格式：HH:mm。
        :type start_time: str
        :param end_time: **参数说明**：规则条件触发的结束时间，格式：HH:mm。若结束时间与开始时间一致，则时间为全天。
        :type end_time: str
        :param days_of_week: **参数说明**：星期列表，以逗号分隔。1代表周日，2代表周一，依次类推，默认为每天。星期列表中的日期为开始时间的日期。
        :type days_of_week: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._days_of_week = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if days_of_week is not None:
            self.days_of_week = days_of_week

    @property
    def start_time(self):
        r"""Gets the start_time of this TimeRange.

        **参数说明**：规则条件触发的开始时间，格式：HH:mm。

        :return: The start_time of this TimeRange.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TimeRange.

        **参数说明**：规则条件触发的开始时间，格式：HH:mm。

        :param start_time: The start_time of this TimeRange.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this TimeRange.

        **参数说明**：规则条件触发的结束时间，格式：HH:mm。若结束时间与开始时间一致，则时间为全天。

        :return: The end_time of this TimeRange.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this TimeRange.

        **参数说明**：规则条件触发的结束时间，格式：HH:mm。若结束时间与开始时间一致，则时间为全天。

        :param end_time: The end_time of this TimeRange.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def days_of_week(self):
        r"""Gets the days_of_week of this TimeRange.

        **参数说明**：星期列表，以逗号分隔。1代表周日，2代表周一，依次类推，默认为每天。星期列表中的日期为开始时间的日期。

        :return: The days_of_week of this TimeRange.
        :rtype: str
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        r"""Sets the days_of_week of this TimeRange.

        **参数说明**：星期列表，以逗号分隔。1代表周日，2代表周一，依次类推，默认为每天。星期列表中的日期为开始时间的日期。

        :param days_of_week: The days_of_week of this TimeRange.
        :type days_of_week: str
        """
        self._days_of_week = days_of_week

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
