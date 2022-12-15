# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Cron:

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
        'depend_pre_period': 'bool',
        'depend_jobs': 'list[DependJob]'
    }

    attribute_map = {
        'start_time': 'startTime',
        'end_time': 'endTime',
        'expression': 'expression',
        'depend_pre_period': 'dependPrePeriod',
        'depend_jobs': 'dependJobs'
    }

    def __init__(self, start_time=None, end_time=None, expression=None, depend_pre_period=None, depend_jobs=None):
        """Cron

        The model defined in huaweicloud sdk

        :param start_time: 
        :type start_time: str
        :param end_time: 
        :type end_time: str
        :param expression: Cron表达式
        :type expression: str
        :param depend_pre_period: 是否依赖本作业上一个运行周期任务的执行结果
        :type depend_pre_period: bool
        :param depend_jobs: 依赖其它作业列表
        :type depend_jobs: list[:class:`huaweicloudsdkdlf.v1.DependJob`]
        """
        
        

        self._start_time = None
        self._end_time = None
        self._expression = None
        self._depend_pre_period = None
        self._depend_jobs = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if expression is not None:
            self.expression = expression
        if depend_pre_period is not None:
            self.depend_pre_period = depend_pre_period
        if depend_jobs is not None:
            self.depend_jobs = depend_jobs

    @property
    def start_time(self):
        """Gets the start_time of this Cron.

        :return: The start_time of this Cron.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Cron.

        :param start_time: The start_time of this Cron.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Cron.

        :return: The end_time of this Cron.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Cron.

        :param end_time: The end_time of this Cron.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def expression(self):
        """Gets the expression of this Cron.

        Cron表达式

        :return: The expression of this Cron.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this Cron.

        Cron表达式

        :param expression: The expression of this Cron.
        :type expression: str
        """
        self._expression = expression

    @property
    def depend_pre_period(self):
        """Gets the depend_pre_period of this Cron.

        是否依赖本作业上一个运行周期任务的执行结果

        :return: The depend_pre_period of this Cron.
        :rtype: bool
        """
        return self._depend_pre_period

    @depend_pre_period.setter
    def depend_pre_period(self, depend_pre_period):
        """Sets the depend_pre_period of this Cron.

        是否依赖本作业上一个运行周期任务的执行结果

        :param depend_pre_period: The depend_pre_period of this Cron.
        :type depend_pre_period: bool
        """
        self._depend_pre_period = depend_pre_period

    @property
    def depend_jobs(self):
        """Gets the depend_jobs of this Cron.

        依赖其它作业列表

        :return: The depend_jobs of this Cron.
        :rtype: list[:class:`huaweicloudsdkdlf.v1.DependJob`]
        """
        return self._depend_jobs

    @depend_jobs.setter
    def depend_jobs(self, depend_jobs):
        """Sets the depend_jobs of this Cron.

        依赖其它作业列表

        :param depend_jobs: The depend_jobs of this Cron.
        :type depend_jobs: list[:class:`huaweicloudsdkdlf.v1.DependJob`]
        """
        self._depend_jobs = depend_jobs

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
        if not isinstance(other, Cron):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
