# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TriggerTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_zone': 'str',
        'policy': 'str',
        'single_scheduled_time': 'int',
        'periodic_scheduled_time': 'str',
        'period': 'str',
        'cron': 'str',
        'scheduled_close_time': 'int'
    }

    attribute_map = {
        'time_zone': 'time_zone',
        'policy': 'policy',
        'single_scheduled_time': 'single_scheduled_time',
        'periodic_scheduled_time': 'periodic_scheduled_time',
        'period': 'period',
        'cron': 'cron',
        'scheduled_close_time': 'scheduled_close_time'
    }

    def __init__(self, time_zone=None, policy=None, single_scheduled_time=None, periodic_scheduled_time=None, period=None, cron=None, scheduled_close_time=None):
        r"""TriggerTime

        The model defined in huaweicloud sdk

        :param time_zone: 时区
        :type time_zone: str
        :param policy: 策略
        :type policy: str
        :param single_scheduled_time: 单次执行的执行时间戳
        :type single_scheduled_time: int
        :param periodic_scheduled_time: 周期执行的执行当天的时间 \&quot;00:00:00\&quot;
        :type periodic_scheduled_time: str
        :param period: 周期执行时的具体星期列表按逗号分割, 如星期日为\&quot;1\&quot;,星期一为\&quot;2\&quot;
        :type period: str
        :param cron: cron表达式
        :type cron: str
        :param scheduled_close_time: 定时任务规则截止日期时间戳
        :type scheduled_close_time: int
        """
        
        

        self._time_zone = None
        self._policy = None
        self._single_scheduled_time = None
        self._periodic_scheduled_time = None
        self._period = None
        self._cron = None
        self._scheduled_close_time = None
        self.discriminator = None

        self.time_zone = time_zone
        self.policy = policy
        if single_scheduled_time is not None:
            self.single_scheduled_time = single_scheduled_time
        if periodic_scheduled_time is not None:
            self.periodic_scheduled_time = periodic_scheduled_time
        if period is not None:
            self.period = period
        if cron is not None:
            self.cron = cron
        if scheduled_close_time is not None:
            self.scheduled_close_time = scheduled_close_time

    @property
    def time_zone(self):
        r"""Gets the time_zone of this TriggerTime.

        时区

        :return: The time_zone of this TriggerTime.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this TriggerTime.

        时区

        :param time_zone: The time_zone of this TriggerTime.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def policy(self):
        r"""Gets the policy of this TriggerTime.

        策略

        :return: The policy of this TriggerTime.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this TriggerTime.

        策略

        :param policy: The policy of this TriggerTime.
        :type policy: str
        """
        self._policy = policy

    @property
    def single_scheduled_time(self):
        r"""Gets the single_scheduled_time of this TriggerTime.

        单次执行的执行时间戳

        :return: The single_scheduled_time of this TriggerTime.
        :rtype: int
        """
        return self._single_scheduled_time

    @single_scheduled_time.setter
    def single_scheduled_time(self, single_scheduled_time):
        r"""Sets the single_scheduled_time of this TriggerTime.

        单次执行的执行时间戳

        :param single_scheduled_time: The single_scheduled_time of this TriggerTime.
        :type single_scheduled_time: int
        """
        self._single_scheduled_time = single_scheduled_time

    @property
    def periodic_scheduled_time(self):
        r"""Gets the periodic_scheduled_time of this TriggerTime.

        周期执行的执行当天的时间 \"00:00:00\"

        :return: The periodic_scheduled_time of this TriggerTime.
        :rtype: str
        """
        return self._periodic_scheduled_time

    @periodic_scheduled_time.setter
    def periodic_scheduled_time(self, periodic_scheduled_time):
        r"""Sets the periodic_scheduled_time of this TriggerTime.

        周期执行的执行当天的时间 \"00:00:00\"

        :param periodic_scheduled_time: The periodic_scheduled_time of this TriggerTime.
        :type periodic_scheduled_time: str
        """
        self._periodic_scheduled_time = periodic_scheduled_time

    @property
    def period(self):
        r"""Gets the period of this TriggerTime.

        周期执行时的具体星期列表按逗号分割, 如星期日为\"1\",星期一为\"2\"

        :return: The period of this TriggerTime.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this TriggerTime.

        周期执行时的具体星期列表按逗号分割, 如星期日为\"1\",星期一为\"2\"

        :param period: The period of this TriggerTime.
        :type period: str
        """
        self._period = period

    @property
    def cron(self):
        r"""Gets the cron of this TriggerTime.

        cron表达式

        :return: The cron of this TriggerTime.
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        r"""Sets the cron of this TriggerTime.

        cron表达式

        :param cron: The cron of this TriggerTime.
        :type cron: str
        """
        self._cron = cron

    @property
    def scheduled_close_time(self):
        r"""Gets the scheduled_close_time of this TriggerTime.

        定时任务规则截止日期时间戳

        :return: The scheduled_close_time of this TriggerTime.
        :rtype: int
        """
        return self._scheduled_close_time

    @scheduled_close_time.setter
    def scheduled_close_time(self, scheduled_close_time):
        r"""Sets the scheduled_close_time of this TriggerTime.

        定时任务规则截止日期时间戳

        :param scheduled_close_time: The scheduled_close_time of this TriggerTime.
        :type scheduled_close_time: int
        """
        self._scheduled_close_time = scheduled_close_time

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
        if not isinstance(other, TriggerTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
