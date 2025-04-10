# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CycleParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_date': 'str',
        'end_date': 'str',
        'cycle': 'str',
        'interval': 'int',
        'point': 'list[int]',
        'pre_remind_days': 'int'
    }

    attribute_map = {
        'start_date': 'startDate',
        'end_date': 'endDate',
        'cycle': 'cycle',
        'interval': 'interval',
        'point': 'point',
        'pre_remind_days': 'preRemindDays'
    }

    def __init__(self, start_date=None, end_date=None, cycle=None, interval=None, point=None, pre_remind_days=None):
        r"""CycleParams

        The model defined in huaweicloud sdk

        :param start_date: 周期会议的开始日期，格式：YYYY-MM-DD。 开始日期不能早于当前日期。 &gt; 日期是timeZoneID指定的时区的日期，非UTC时间的日期。
        :type start_date: str
        :param end_date: 周期会议的结束日期，格式：YYYY-MM-DD。 开始日期和结束日期间的时间间隔最长不能超过1年。开始日期和结束日期之间最多允许50个子会议，若超过50个子会议，会自动调整结束日期。 &gt; 日期是timeZoneID指定的时区的日期，非UTC时间的日期。
        :type end_date: str
        :param cycle: 周期类型。 - Day: 天 - Week: 星期 - Month: 月
        :type cycle: str
        :param interval: 子会议间隔。 - cycle选择了Day，表示每几天召开一次，取值范围[1,15] - cycle选择了Week，表示每几周召开一次，取值范围[1,5] - cycle选择了Month，Interval表示隔几月，取值范围[1,3]
        :type interval: int
        :param point: 周期内的会议召开点。仅当按周和月时有效。 - cycle选择了Week，point中填入了两个元素1和3，则表示每个周一和周三召开会议，0表示周日 - cycle选择了Month，point中填入了12和20则表示每个月的12号和20号召开会议，取值范围为[1,31]，若当月没有该值，则为月末
        :type point: list[int]
        :param pre_remind_days: 提前通知天数。所有与会者在每个子会议开始前N天收到会议通知。取值范围[0,30]。 默认值是1。
        :type pre_remind_days: int
        """
        
        

        self._start_date = None
        self._end_date = None
        self._cycle = None
        self._interval = None
        self._point = None
        self._pre_remind_days = None
        self.discriminator = None

        self.start_date = start_date
        self.end_date = end_date
        self.cycle = cycle
        if interval is not None:
            self.interval = interval
        if point is not None:
            self.point = point
        self.pre_remind_days = pre_remind_days

    @property
    def start_date(self):
        r"""Gets the start_date of this CycleParams.

        周期会议的开始日期，格式：YYYY-MM-DD。 开始日期不能早于当前日期。 > 日期是timeZoneID指定的时区的日期，非UTC时间的日期。

        :return: The start_date of this CycleParams.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this CycleParams.

        周期会议的开始日期，格式：YYYY-MM-DD。 开始日期不能早于当前日期。 > 日期是timeZoneID指定的时区的日期，非UTC时间的日期。

        :param start_date: The start_date of this CycleParams.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        r"""Gets the end_date of this CycleParams.

        周期会议的结束日期，格式：YYYY-MM-DD。 开始日期和结束日期间的时间间隔最长不能超过1年。开始日期和结束日期之间最多允许50个子会议，若超过50个子会议，会自动调整结束日期。 > 日期是timeZoneID指定的时区的日期，非UTC时间的日期。

        :return: The end_date of this CycleParams.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        r"""Sets the end_date of this CycleParams.

        周期会议的结束日期，格式：YYYY-MM-DD。 开始日期和结束日期间的时间间隔最长不能超过1年。开始日期和结束日期之间最多允许50个子会议，若超过50个子会议，会自动调整结束日期。 > 日期是timeZoneID指定的时区的日期，非UTC时间的日期。

        :param end_date: The end_date of this CycleParams.
        :type end_date: str
        """
        self._end_date = end_date

    @property
    def cycle(self):
        r"""Gets the cycle of this CycleParams.

        周期类型。 - Day: 天 - Week: 星期 - Month: 月

        :return: The cycle of this CycleParams.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        r"""Sets the cycle of this CycleParams.

        周期类型。 - Day: 天 - Week: 星期 - Month: 月

        :param cycle: The cycle of this CycleParams.
        :type cycle: str
        """
        self._cycle = cycle

    @property
    def interval(self):
        r"""Gets the interval of this CycleParams.

        子会议间隔。 - cycle选择了Day，表示每几天召开一次，取值范围[1,15] - cycle选择了Week，表示每几周召开一次，取值范围[1,5] - cycle选择了Month，Interval表示隔几月，取值范围[1,3]

        :return: The interval of this CycleParams.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this CycleParams.

        子会议间隔。 - cycle选择了Day，表示每几天召开一次，取值范围[1,15] - cycle选择了Week，表示每几周召开一次，取值范围[1,5] - cycle选择了Month，Interval表示隔几月，取值范围[1,3]

        :param interval: The interval of this CycleParams.
        :type interval: int
        """
        self._interval = interval

    @property
    def point(self):
        r"""Gets the point of this CycleParams.

        周期内的会议召开点。仅当按周和月时有效。 - cycle选择了Week，point中填入了两个元素1和3，则表示每个周一和周三召开会议，0表示周日 - cycle选择了Month，point中填入了12和20则表示每个月的12号和20号召开会议，取值范围为[1,31]，若当月没有该值，则为月末

        :return: The point of this CycleParams.
        :rtype: list[int]
        """
        return self._point

    @point.setter
    def point(self, point):
        r"""Sets the point of this CycleParams.

        周期内的会议召开点。仅当按周和月时有效。 - cycle选择了Week，point中填入了两个元素1和3，则表示每个周一和周三召开会议，0表示周日 - cycle选择了Month，point中填入了12和20则表示每个月的12号和20号召开会议，取值范围为[1,31]，若当月没有该值，则为月末

        :param point: The point of this CycleParams.
        :type point: list[int]
        """
        self._point = point

    @property
    def pre_remind_days(self):
        r"""Gets the pre_remind_days of this CycleParams.

        提前通知天数。所有与会者在每个子会议开始前N天收到会议通知。取值范围[0,30]。 默认值是1。

        :return: The pre_remind_days of this CycleParams.
        :rtype: int
        """
        return self._pre_remind_days

    @pre_remind_days.setter
    def pre_remind_days(self, pre_remind_days):
        r"""Sets the pre_remind_days of this CycleParams.

        提前通知天数。所有与会者在每个子会议开始前N天收到会议通知。取值范围[0,30]。 默认值是1。

        :param pre_remind_days: The pre_remind_days of this CycleParams.
        :type pre_remind_days: int
        """
        self._pre_remind_days = pre_remind_days

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
        if not isinstance(other, CycleParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
