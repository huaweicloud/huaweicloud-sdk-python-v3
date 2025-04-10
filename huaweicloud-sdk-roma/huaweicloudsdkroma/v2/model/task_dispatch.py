# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskDispatch:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_datetime': 'int',
        'period': 'str',
        'dispatch_interval': 'int',
        'remark': 'str',
        'use_quartz_cron': 'bool',
        'cron': 'str'
    }

    attribute_map = {
        'start_datetime': 'start_datetime',
        'period': 'period',
        'dispatch_interval': 'dispatch_interval',
        'remark': 'remark',
        'use_quartz_cron': 'use_quartz_cron',
        'cron': 'cron'
    }

    def __init__(self, start_datetime=None, period=None, dispatch_interval=None, remark=None, use_quartz_cron=None, cron=None):
        r"""TaskDispatch

        The model defined in huaweicloud sdk

        :param start_datetime: 调度计划的执行开始时间
        :type start_datetime: int
        :param period: 调度计划执行周期的时间单位，当使用cron表达式时，为空 - MIN (分钟) - HOUR (小时) - DAY (日) - WEEK (周) - MON (月)
        :type period: str
        :param dispatch_interval: 调度计划的执行间隔时间周期
        :type dispatch_interval: int
        :param remark: 调度计划的备注信息
        :type remark: str
        :param use_quartz_cron: 调度计划是否使用cron表达式，允许如下值： - true (使用cron表达式) - false (不使用cron表达式)
        :type use_quartz_cron: bool
        :param cron: 调度计划的cron表达式
        :type cron: str
        """
        
        

        self._start_datetime = None
        self._period = None
        self._dispatch_interval = None
        self._remark = None
        self._use_quartz_cron = None
        self._cron = None
        self.discriminator = None

        if start_datetime is not None:
            self.start_datetime = start_datetime
        if period is not None:
            self.period = period
        if dispatch_interval is not None:
            self.dispatch_interval = dispatch_interval
        if remark is not None:
            self.remark = remark
        if use_quartz_cron is not None:
            self.use_quartz_cron = use_quartz_cron
        if cron is not None:
            self.cron = cron

    @property
    def start_datetime(self):
        r"""Gets the start_datetime of this TaskDispatch.

        调度计划的执行开始时间

        :return: The start_datetime of this TaskDispatch.
        :rtype: int
        """
        return self._start_datetime

    @start_datetime.setter
    def start_datetime(self, start_datetime):
        r"""Sets the start_datetime of this TaskDispatch.

        调度计划的执行开始时间

        :param start_datetime: The start_datetime of this TaskDispatch.
        :type start_datetime: int
        """
        self._start_datetime = start_datetime

    @property
    def period(self):
        r"""Gets the period of this TaskDispatch.

        调度计划执行周期的时间单位，当使用cron表达式时，为空 - MIN (分钟) - HOUR (小时) - DAY (日) - WEEK (周) - MON (月)

        :return: The period of this TaskDispatch.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this TaskDispatch.

        调度计划执行周期的时间单位，当使用cron表达式时，为空 - MIN (分钟) - HOUR (小时) - DAY (日) - WEEK (周) - MON (月)

        :param period: The period of this TaskDispatch.
        :type period: str
        """
        self._period = period

    @property
    def dispatch_interval(self):
        r"""Gets the dispatch_interval of this TaskDispatch.

        调度计划的执行间隔时间周期

        :return: The dispatch_interval of this TaskDispatch.
        :rtype: int
        """
        return self._dispatch_interval

    @dispatch_interval.setter
    def dispatch_interval(self, dispatch_interval):
        r"""Sets the dispatch_interval of this TaskDispatch.

        调度计划的执行间隔时间周期

        :param dispatch_interval: The dispatch_interval of this TaskDispatch.
        :type dispatch_interval: int
        """
        self._dispatch_interval = dispatch_interval

    @property
    def remark(self):
        r"""Gets the remark of this TaskDispatch.

        调度计划的备注信息

        :return: The remark of this TaskDispatch.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this TaskDispatch.

        调度计划的备注信息

        :param remark: The remark of this TaskDispatch.
        :type remark: str
        """
        self._remark = remark

    @property
    def use_quartz_cron(self):
        r"""Gets the use_quartz_cron of this TaskDispatch.

        调度计划是否使用cron表达式，允许如下值： - true (使用cron表达式) - false (不使用cron表达式)

        :return: The use_quartz_cron of this TaskDispatch.
        :rtype: bool
        """
        return self._use_quartz_cron

    @use_quartz_cron.setter
    def use_quartz_cron(self, use_quartz_cron):
        r"""Sets the use_quartz_cron of this TaskDispatch.

        调度计划是否使用cron表达式，允许如下值： - true (使用cron表达式) - false (不使用cron表达式)

        :param use_quartz_cron: The use_quartz_cron of this TaskDispatch.
        :type use_quartz_cron: bool
        """
        self._use_quartz_cron = use_quartz_cron

    @property
    def cron(self):
        r"""Gets the cron of this TaskDispatch.

        调度计划的cron表达式

        :return: The cron of this TaskDispatch.
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        r"""Sets the cron of this TaskDispatch.

        调度计划的cron表达式

        :param cron: The cron of this TaskDispatch.
        :type cron: str
        """
        self._cron = cron

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
        if not isinstance(other, TaskDispatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
