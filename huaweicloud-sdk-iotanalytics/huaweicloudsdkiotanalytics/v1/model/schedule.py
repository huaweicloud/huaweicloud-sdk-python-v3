# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Schedule:

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
        'cron_expression': 'str',
        'computing_resource_id': 'str',
        'enable': 'bool',
        'conf': 'list[str]',
        'schedule_status': 'str',
        'next_fire_time': 'str',
        'prev_fire_time': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'cron_expression': 'cron_expression',
        'computing_resource_id': 'computing_resource_id',
        'enable': 'enable',
        'conf': 'conf',
        'schedule_status': 'schedule_status',
        'next_fire_time': 'next_fire_time',
        'prev_fire_time': 'prev_fire_time'
    }

    def __init__(self, start_time=None, end_time=None, cron_expression=None, computing_resource_id=None, enable=None, conf=None, schedule_status=None, next_fire_time=None, prev_fire_time=None):
        """Schedule

        The model defined in huaweicloud sdk

        :param start_time: 调度开始时间。时间格式为ISO时区日期时间。例如2021-03-03T10:15:30+08:00
        :type start_time: str
        :param end_time: 调度结束时间。时间格式为ISO时区日期时间。例如2021-03-03T10:15:30+08:00
        :type end_time: str
        :param cron_expression: Cron表达式，格式为&lt;秒&gt; &lt;分&gt; &lt;时&gt; &lt;天&gt; &lt;月&gt; &lt;星期&gt;
        :type cron_expression: str
        :param computing_resource_id: 计算资源ID。
        :type computing_resource_id: str
        :param enable: 调度启用状态. true: 调度中；false：停止调度。
        :type enable: bool
        :param conf: 作业运行配置信息。
        :type conf: list[str]
        :param schedule_status: 仅在查询作业和查询所有作业接口的响应返回。调度状态。1:NORMAL, 2:PAUSED, 3:COMPLETE, 4:ERROR, 5:BLOCKED
        :type schedule_status: str
        :param next_fire_time: 仅在查询作业和查询所有作业接口的响应返回。上一次调度开始时间。
        :type next_fire_time: str
        :param prev_fire_time: 仅在查询作业和查询所有作业接口的响应返回。下一次调度开始时间。
        :type prev_fire_time: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._cron_expression = None
        self._computing_resource_id = None
        self._enable = None
        self._conf = None
        self._schedule_status = None
        self._next_fire_time = None
        self._prev_fire_time = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.cron_expression = cron_expression
        self.computing_resource_id = computing_resource_id
        self.enable = enable
        if conf is not None:
            self.conf = conf
        if schedule_status is not None:
            self.schedule_status = schedule_status
        if next_fire_time is not None:
            self.next_fire_time = next_fire_time
        if prev_fire_time is not None:
            self.prev_fire_time = prev_fire_time

    @property
    def start_time(self):
        """Gets the start_time of this Schedule.

        调度开始时间。时间格式为ISO时区日期时间。例如2021-03-03T10:15:30+08:00

        :return: The start_time of this Schedule.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Schedule.

        调度开始时间。时间格式为ISO时区日期时间。例如2021-03-03T10:15:30+08:00

        :param start_time: The start_time of this Schedule.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Schedule.

        调度结束时间。时间格式为ISO时区日期时间。例如2021-03-03T10:15:30+08:00

        :return: The end_time of this Schedule.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Schedule.

        调度结束时间。时间格式为ISO时区日期时间。例如2021-03-03T10:15:30+08:00

        :param end_time: The end_time of this Schedule.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def cron_expression(self):
        """Gets the cron_expression of this Schedule.

        Cron表达式，格式为<秒> <分> <时> <天> <月> <星期>

        :return: The cron_expression of this Schedule.
        :rtype: str
        """
        return self._cron_expression

    @cron_expression.setter
    def cron_expression(self, cron_expression):
        """Sets the cron_expression of this Schedule.

        Cron表达式，格式为<秒> <分> <时> <天> <月> <星期>

        :param cron_expression: The cron_expression of this Schedule.
        :type cron_expression: str
        """
        self._cron_expression = cron_expression

    @property
    def computing_resource_id(self):
        """Gets the computing_resource_id of this Schedule.

        计算资源ID。

        :return: The computing_resource_id of this Schedule.
        :rtype: str
        """
        return self._computing_resource_id

    @computing_resource_id.setter
    def computing_resource_id(self, computing_resource_id):
        """Sets the computing_resource_id of this Schedule.

        计算资源ID。

        :param computing_resource_id: The computing_resource_id of this Schedule.
        :type computing_resource_id: str
        """
        self._computing_resource_id = computing_resource_id

    @property
    def enable(self):
        """Gets the enable of this Schedule.

        调度启用状态. true: 调度中；false：停止调度。

        :return: The enable of this Schedule.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this Schedule.

        调度启用状态. true: 调度中；false：停止调度。

        :param enable: The enable of this Schedule.
        :type enable: bool
        """
        self._enable = enable

    @property
    def conf(self):
        """Gets the conf of this Schedule.

        作业运行配置信息。

        :return: The conf of this Schedule.
        :rtype: list[str]
        """
        return self._conf

    @conf.setter
    def conf(self, conf):
        """Sets the conf of this Schedule.

        作业运行配置信息。

        :param conf: The conf of this Schedule.
        :type conf: list[str]
        """
        self._conf = conf

    @property
    def schedule_status(self):
        """Gets the schedule_status of this Schedule.

        仅在查询作业和查询所有作业接口的响应返回。调度状态。1:NORMAL, 2:PAUSED, 3:COMPLETE, 4:ERROR, 5:BLOCKED

        :return: The schedule_status of this Schedule.
        :rtype: str
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        """Sets the schedule_status of this Schedule.

        仅在查询作业和查询所有作业接口的响应返回。调度状态。1:NORMAL, 2:PAUSED, 3:COMPLETE, 4:ERROR, 5:BLOCKED

        :param schedule_status: The schedule_status of this Schedule.
        :type schedule_status: str
        """
        self._schedule_status = schedule_status

    @property
    def next_fire_time(self):
        """Gets the next_fire_time of this Schedule.

        仅在查询作业和查询所有作业接口的响应返回。上一次调度开始时间。

        :return: The next_fire_time of this Schedule.
        :rtype: str
        """
        return self._next_fire_time

    @next_fire_time.setter
    def next_fire_time(self, next_fire_time):
        """Sets the next_fire_time of this Schedule.

        仅在查询作业和查询所有作业接口的响应返回。上一次调度开始时间。

        :param next_fire_time: The next_fire_time of this Schedule.
        :type next_fire_time: str
        """
        self._next_fire_time = next_fire_time

    @property
    def prev_fire_time(self):
        """Gets the prev_fire_time of this Schedule.

        仅在查询作业和查询所有作业接口的响应返回。下一次调度开始时间。

        :return: The prev_fire_time of this Schedule.
        :rtype: str
        """
        return self._prev_fire_time

    @prev_fire_time.setter
    def prev_fire_time(self, prev_fire_time):
        """Sets the prev_fire_time of this Schedule.

        仅在查询作业和查询所有作业接口的响应返回。下一次调度开始时间。

        :param prev_fire_time: The prev_fire_time of this Schedule.
        :type prev_fire_time: str
        """
        self._prev_fire_time = prev_fire_time

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
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
