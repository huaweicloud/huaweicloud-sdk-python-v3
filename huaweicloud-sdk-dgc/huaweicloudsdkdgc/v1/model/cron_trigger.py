# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CronTrigger:

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
        'expression': 'str',
        'expression_time_zone': 'str',
        'period': 'str',
        'depend_pre_period': 'bool',
        'depend_jobs': 'DependJob',
        'concurrent': 'int'
    }

    attribute_map = {
        'start_time': 'startTime',
        'end_time': 'endTime',
        'expression': 'expression',
        'expression_time_zone': 'expressionTimeZone',
        'period': 'period',
        'depend_pre_period': 'dependPrePeriod',
        'depend_jobs': 'dependJobs',
        'concurrent': 'concurrent'
    }

    def __init__(self, start_time=None, end_time=None, expression=None, expression_time_zone=None, period=None, depend_pre_period=None, depend_jobs=None, concurrent=None):
        """CronTrigger

        The model defined in huaweicloud sdk

        :param start_time: 调度开始时间，采用ISO 8601时间表示方法，格式为yyyy-MM-dd&#39;T&#39;HH:mm:ssZ，例如2018-10-22T23:59:59+08表示的时间为2018年10月22日23时59分59秒，在正8区，即北京时区。
        :type start_time: str
        :param end_time: 调度结束时间，采用ISO 8601时间表示方法，格式为yyyy-MM-dd&#39;T&#39;HH:mm:ssZ，例如2018-10-22T23:59:59+08表示的时间为2018年10月22日23时59分59秒，在正8区，即北京时区。如果结束时间不配置，作业会按照调度周期一直执行下去。
        :type end_time: str
        :param expression: Cron表达式
        :type expression: str
        :param expression_time_zone: 时区
        :type expression_time_zone: str
        :param period: 用于描述运行的间隔时间，格式为时间+时间单位。需要与expression中的表达式对应
        :type period: str
        :param depend_pre_period: 是否依赖本作业上一个运行周期任务的执行结果
        :type depend_pre_period: bool
        :param depend_jobs: 
        :type depend_jobs: :class:`huaweicloudsdkdgc.v1.DependJob`
        :param concurrent: 并发调用数
        :type concurrent: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self._expression = None
        self._expression_time_zone = None
        self._period = None
        self._depend_pre_period = None
        self._depend_jobs = None
        self._concurrent = None
        self.discriminator = None

        self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.expression = expression
        if expression_time_zone is not None:
            self.expression_time_zone = expression_time_zone
        self.period = period
        if depend_pre_period is not None:
            self.depend_pre_period = depend_pre_period
        if depend_jobs is not None:
            self.depend_jobs = depend_jobs
        if concurrent is not None:
            self.concurrent = concurrent

    @property
    def start_time(self):
        """Gets the start_time of this CronTrigger.

        调度开始时间，采用ISO 8601时间表示方法，格式为yyyy-MM-dd'T'HH:mm:ssZ，例如2018-10-22T23:59:59+08表示的时间为2018年10月22日23时59分59秒，在正8区，即北京时区。

        :return: The start_time of this CronTrigger.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CronTrigger.

        调度开始时间，采用ISO 8601时间表示方法，格式为yyyy-MM-dd'T'HH:mm:ssZ，例如2018-10-22T23:59:59+08表示的时间为2018年10月22日23时59分59秒，在正8区，即北京时区。

        :param start_time: The start_time of this CronTrigger.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this CronTrigger.

        调度结束时间，采用ISO 8601时间表示方法，格式为yyyy-MM-dd'T'HH:mm:ssZ，例如2018-10-22T23:59:59+08表示的时间为2018年10月22日23时59分59秒，在正8区，即北京时区。如果结束时间不配置，作业会按照调度周期一直执行下去。

        :return: The end_time of this CronTrigger.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CronTrigger.

        调度结束时间，采用ISO 8601时间表示方法，格式为yyyy-MM-dd'T'HH:mm:ssZ，例如2018-10-22T23:59:59+08表示的时间为2018年10月22日23时59分59秒，在正8区，即北京时区。如果结束时间不配置，作业会按照调度周期一直执行下去。

        :param end_time: The end_time of this CronTrigger.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def expression(self):
        """Gets the expression of this CronTrigger.

        Cron表达式

        :return: The expression of this CronTrigger.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this CronTrigger.

        Cron表达式

        :param expression: The expression of this CronTrigger.
        :type expression: str
        """
        self._expression = expression

    @property
    def expression_time_zone(self):
        """Gets the expression_time_zone of this CronTrigger.

        时区

        :return: The expression_time_zone of this CronTrigger.
        :rtype: str
        """
        return self._expression_time_zone

    @expression_time_zone.setter
    def expression_time_zone(self, expression_time_zone):
        """Sets the expression_time_zone of this CronTrigger.

        时区

        :param expression_time_zone: The expression_time_zone of this CronTrigger.
        :type expression_time_zone: str
        """
        self._expression_time_zone = expression_time_zone

    @property
    def period(self):
        """Gets the period of this CronTrigger.

        用于描述运行的间隔时间，格式为时间+时间单位。需要与expression中的表达式对应

        :return: The period of this CronTrigger.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CronTrigger.

        用于描述运行的间隔时间，格式为时间+时间单位。需要与expression中的表达式对应

        :param period: The period of this CronTrigger.
        :type period: str
        """
        self._period = period

    @property
    def depend_pre_period(self):
        """Gets the depend_pre_period of this CronTrigger.

        是否依赖本作业上一个运行周期任务的执行结果

        :return: The depend_pre_period of this CronTrigger.
        :rtype: bool
        """
        return self._depend_pre_period

    @depend_pre_period.setter
    def depend_pre_period(self, depend_pre_period):
        """Sets the depend_pre_period of this CronTrigger.

        是否依赖本作业上一个运行周期任务的执行结果

        :param depend_pre_period: The depend_pre_period of this CronTrigger.
        :type depend_pre_period: bool
        """
        self._depend_pre_period = depend_pre_period

    @property
    def depend_jobs(self):
        """Gets the depend_jobs of this CronTrigger.

        :return: The depend_jobs of this CronTrigger.
        :rtype: :class:`huaweicloudsdkdgc.v1.DependJob`
        """
        return self._depend_jobs

    @depend_jobs.setter
    def depend_jobs(self, depend_jobs):
        """Sets the depend_jobs of this CronTrigger.

        :param depend_jobs: The depend_jobs of this CronTrigger.
        :type depend_jobs: :class:`huaweicloudsdkdgc.v1.DependJob`
        """
        self._depend_jobs = depend_jobs

    @property
    def concurrent(self):
        """Gets the concurrent of this CronTrigger.

        并发调用数

        :return: The concurrent of this CronTrigger.
        :rtype: int
        """
        return self._concurrent

    @concurrent.setter
    def concurrent(self, concurrent):
        """Sets the concurrent of this CronTrigger.

        并发调用数

        :param concurrent: The concurrent of this CronTrigger.
        :type concurrent: int
        """
        self._concurrent = concurrent

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
        if not isinstance(other, CronTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
