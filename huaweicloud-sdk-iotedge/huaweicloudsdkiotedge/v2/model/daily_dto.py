# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DailyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exceptional_dates': 'ExceptionalDates',
        'time_spans': 'list[TimeSpans]',
        'weekdays': 'object'
    }

    attribute_map = {
        'exceptional_dates': 'exceptional_dates',
        'time_spans': 'time_spans',
        'weekdays': 'weekdays'
    }

    def __init__(self, exceptional_dates=None, time_spans=None, weekdays=None):
        """DailyDto

        The model defined in huaweicloud sdk

        :param exceptional_dates: 
        :type exceptional_dates: :class:`huaweicloudsdkiotedge.v2.ExceptionalDates`
        :param time_spans: 时间段描述
        :type time_spans: list[:class:`huaweicloudsdkiotedge.v2.TimeSpans`]
        :param weekdays: 描述此任务有效的星期几，为数组。如果为null，则表示start_time-endtime之间，每天都执行；如果为空数组，则表示start_time-endtime之间，每天都不执行；如果为[1, 2]，则表示每周一、二执行。
        :type weekdays: object
        """
        
        

        self._exceptional_dates = None
        self._time_spans = None
        self._weekdays = None
        self.discriminator = None

        if exceptional_dates is not None:
            self.exceptional_dates = exceptional_dates
        self.time_spans = time_spans
        if weekdays is not None:
            self.weekdays = weekdays

    @property
    def exceptional_dates(self):
        """Gets the exceptional_dates of this DailyDto.

        :return: The exceptional_dates of this DailyDto.
        :rtype: :class:`huaweicloudsdkiotedge.v2.ExceptionalDates`
        """
        return self._exceptional_dates

    @exceptional_dates.setter
    def exceptional_dates(self, exceptional_dates):
        """Sets the exceptional_dates of this DailyDto.

        :param exceptional_dates: The exceptional_dates of this DailyDto.
        :type exceptional_dates: :class:`huaweicloudsdkiotedge.v2.ExceptionalDates`
        """
        self._exceptional_dates = exceptional_dates

    @property
    def time_spans(self):
        """Gets the time_spans of this DailyDto.

        时间段描述

        :return: The time_spans of this DailyDto.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.TimeSpans`]
        """
        return self._time_spans

    @time_spans.setter
    def time_spans(self, time_spans):
        """Sets the time_spans of this DailyDto.

        时间段描述

        :param time_spans: The time_spans of this DailyDto.
        :type time_spans: list[:class:`huaweicloudsdkiotedge.v2.TimeSpans`]
        """
        self._time_spans = time_spans

    @property
    def weekdays(self):
        """Gets the weekdays of this DailyDto.

        描述此任务有效的星期几，为数组。如果为null，则表示start_time-endtime之间，每天都执行；如果为空数组，则表示start_time-endtime之间，每天都不执行；如果为[1, 2]，则表示每周一、二执行。

        :return: The weekdays of this DailyDto.
        :rtype: object
        """
        return self._weekdays

    @weekdays.setter
    def weekdays(self, weekdays):
        """Sets the weekdays of this DailyDto.

        描述此任务有效的星期几，为数组。如果为null，则表示start_time-endtime之间，每天都执行；如果为空数组，则表示start_time-endtime之间，每天都不执行；如果为[1, 2]，则表示每周一、二执行。

        :param weekdays: The weekdays of this DailyDto.
        :type weekdays: object
        """
        self._weekdays = weekdays

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
        if not isinstance(other, DailyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
