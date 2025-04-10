# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SchedulerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cron_expression': 'str',
        'end_time': 'str',
        'max_time_out': 'int',
        'interval': 'str',
        'schedule_type': 'str',
        'start_time': 'str',
        'job_id': 'int',
        'enabled': 'int'
    }

    attribute_map = {
        'cron_expression': 'cron_expression',
        'end_time': 'end_time',
        'max_time_out': 'max_time_out',
        'interval': 'interval',
        'schedule_type': 'schedule_type',
        'start_time': 'start_time',
        'job_id': 'job_id',
        'enabled': 'enabled'
    }

    def __init__(self, cron_expression=None, end_time=None, max_time_out=None, interval=None, schedule_type=None, start_time=None, job_id=None, enabled=None):
        r"""SchedulerInfo

        The model defined in huaweicloud sdk

        :param cron_expression: 表达式
        :type cron_expression: str
        :param end_time: 结束时间
        :type end_time: str
        :param max_time_out: 最大超时时间
        :type max_time_out: int
        :param interval: 间隔
        :type interval: str
        :param schedule_type: 调度类型
        :type schedule_type: str
        :param start_time: 开始时间
        :type start_time: str
        :param job_id: 工作id
        :type job_id: int
        :param enabled: 启用
        :type enabled: int
        """
        
        

        self._cron_expression = None
        self._end_time = None
        self._max_time_out = None
        self._interval = None
        self._schedule_type = None
        self._start_time = None
        self._job_id = None
        self._enabled = None
        self.discriminator = None

        if cron_expression is not None:
            self.cron_expression = cron_expression
        if end_time is not None:
            self.end_time = end_time
        if max_time_out is not None:
            self.max_time_out = max_time_out
        if interval is not None:
            self.interval = interval
        if schedule_type is not None:
            self.schedule_type = schedule_type
        if start_time is not None:
            self.start_time = start_time
        if job_id is not None:
            self.job_id = job_id
        if enabled is not None:
            self.enabled = enabled

    @property
    def cron_expression(self):
        r"""Gets the cron_expression of this SchedulerInfo.

        表达式

        :return: The cron_expression of this SchedulerInfo.
        :rtype: str
        """
        return self._cron_expression

    @cron_expression.setter
    def cron_expression(self, cron_expression):
        r"""Sets the cron_expression of this SchedulerInfo.

        表达式

        :param cron_expression: The cron_expression of this SchedulerInfo.
        :type cron_expression: str
        """
        self._cron_expression = cron_expression

    @property
    def end_time(self):
        r"""Gets the end_time of this SchedulerInfo.

        结束时间

        :return: The end_time of this SchedulerInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SchedulerInfo.

        结束时间

        :param end_time: The end_time of this SchedulerInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def max_time_out(self):
        r"""Gets the max_time_out of this SchedulerInfo.

        最大超时时间

        :return: The max_time_out of this SchedulerInfo.
        :rtype: int
        """
        return self._max_time_out

    @max_time_out.setter
    def max_time_out(self, max_time_out):
        r"""Sets the max_time_out of this SchedulerInfo.

        最大超时时间

        :param max_time_out: The max_time_out of this SchedulerInfo.
        :type max_time_out: int
        """
        self._max_time_out = max_time_out

    @property
    def interval(self):
        r"""Gets the interval of this SchedulerInfo.

        间隔

        :return: The interval of this SchedulerInfo.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this SchedulerInfo.

        间隔

        :param interval: The interval of this SchedulerInfo.
        :type interval: str
        """
        self._interval = interval

    @property
    def schedule_type(self):
        r"""Gets the schedule_type of this SchedulerInfo.

        调度类型

        :return: The schedule_type of this SchedulerInfo.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        r"""Sets the schedule_type of this SchedulerInfo.

        调度类型

        :param schedule_type: The schedule_type of this SchedulerInfo.
        :type schedule_type: str
        """
        self._schedule_type = schedule_type

    @property
    def start_time(self):
        r"""Gets the start_time of this SchedulerInfo.

        开始时间

        :return: The start_time of this SchedulerInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SchedulerInfo.

        开始时间

        :param start_time: The start_time of this SchedulerInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def job_id(self):
        r"""Gets the job_id of this SchedulerInfo.

        工作id

        :return: The job_id of this SchedulerInfo.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SchedulerInfo.

        工作id

        :param job_id: The job_id of this SchedulerInfo.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def enabled(self):
        r"""Gets the enabled of this SchedulerInfo.

        启用

        :return: The enabled of this SchedulerInfo.
        :rtype: int
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this SchedulerInfo.

        启用

        :param enabled: The enabled of this SchedulerInfo.
        :type enabled: int
        """
        self._enabled = enabled

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
        if not isinstance(other, SchedulerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
