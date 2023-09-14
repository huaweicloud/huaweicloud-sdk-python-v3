# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScheduleReqDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'enabled': 'bool',
        'start_time': 'int',
        'end_time': 'int',
        'priority': 'int',
        'daily': 'DailyDto',
        'tasks': 'list[ScheduleTask]'
    }

    attribute_map = {
        'name': 'name',
        'enabled': 'enabled',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'priority': 'priority',
        'daily': 'daily',
        'tasks': 'tasks'
    }

    def __init__(self, name=None, enabled=None, start_time=None, end_time=None, priority=None, daily=None, tasks=None):
        """UpdateScheduleReqDTO

        The model defined in huaweicloud sdk

        :param name: 调度计划名称
        :type name: str
        :param enabled: 调度计划是否生效
        :type enabled: bool
        :param start_time: 调度计划起始时间，毫秒级别的时间戳
        :type start_time: int
        :param end_time: 调度计划结束时间，毫秒级别的时间戳
        :type end_time: int
        :param priority: 调度计划优先级。
        :type priority: int
        :param daily: 
        :type daily: :class:`huaweicloudsdkiotedge.v2.DailyDto`
        :param tasks: 调度任务信息
        :type tasks: list[:class:`huaweicloudsdkiotedge.v2.ScheduleTask`]
        """
        
        

        self._name = None
        self._enabled = None
        self._start_time = None
        self._end_time = None
        self._priority = None
        self._daily = None
        self._tasks = None
        self.discriminator = None

        self.name = name
        self.enabled = enabled
        if start_time is not None:
            self.start_time = start_time
        self.end_time = end_time
        self.priority = priority
        if daily is not None:
            self.daily = daily
        self.tasks = tasks

    @property
    def name(self):
        """Gets the name of this UpdateScheduleReqDTO.

        调度计划名称

        :return: The name of this UpdateScheduleReqDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateScheduleReqDTO.

        调度计划名称

        :param name: The name of this UpdateScheduleReqDTO.
        :type name: str
        """
        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this UpdateScheduleReqDTO.

        调度计划是否生效

        :return: The enabled of this UpdateScheduleReqDTO.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateScheduleReqDTO.

        调度计划是否生效

        :param enabled: The enabled of this UpdateScheduleReqDTO.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def start_time(self):
        """Gets the start_time of this UpdateScheduleReqDTO.

        调度计划起始时间，毫秒级别的时间戳

        :return: The start_time of this UpdateScheduleReqDTO.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this UpdateScheduleReqDTO.

        调度计划起始时间，毫秒级别的时间戳

        :param start_time: The start_time of this UpdateScheduleReqDTO.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this UpdateScheduleReqDTO.

        调度计划结束时间，毫秒级别的时间戳

        :return: The end_time of this UpdateScheduleReqDTO.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this UpdateScheduleReqDTO.

        调度计划结束时间，毫秒级别的时间戳

        :param end_time: The end_time of this UpdateScheduleReqDTO.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def priority(self):
        """Gets the priority of this UpdateScheduleReqDTO.

        调度计划优先级。

        :return: The priority of this UpdateScheduleReqDTO.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this UpdateScheduleReqDTO.

        调度计划优先级。

        :param priority: The priority of this UpdateScheduleReqDTO.
        :type priority: int
        """
        self._priority = priority

    @property
    def daily(self):
        """Gets the daily of this UpdateScheduleReqDTO.

        :return: The daily of this UpdateScheduleReqDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.DailyDto`
        """
        return self._daily

    @daily.setter
    def daily(self, daily):
        """Sets the daily of this UpdateScheduleReqDTO.

        :param daily: The daily of this UpdateScheduleReqDTO.
        :type daily: :class:`huaweicloudsdkiotedge.v2.DailyDto`
        """
        self._daily = daily

    @property
    def tasks(self):
        """Gets the tasks of this UpdateScheduleReqDTO.

        调度任务信息

        :return: The tasks of this UpdateScheduleReqDTO.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.ScheduleTask`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this UpdateScheduleReqDTO.

        调度任务信息

        :param tasks: The tasks of this UpdateScheduleReqDTO.
        :type tasks: list[:class:`huaweicloudsdkiotedge.v2.ScheduleTask`]
        """
        self._tasks = tasks

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
        if not isinstance(other, UpdateScheduleReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
