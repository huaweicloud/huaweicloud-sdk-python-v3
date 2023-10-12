# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleConf:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schedule_start': 'str',
        'schedule_end': 'str',
        'schedule_type': 'str',
        'schedule_date': 'list[int]',
        'schedule_time': 'list[str]'
    }

    attribute_map = {
        'schedule_start': 'schedule_start',
        'schedule_end': 'schedule_end',
        'schedule_type': 'schedule_type',
        'schedule_date': 'schedule_date',
        'schedule_time': 'schedule_time'
    }

    def __init__(self, schedule_start=None, schedule_end=None, schedule_type=None, schedule_date=None, schedule_time=None):
        """ScheduleConf

        The model defined in huaweicloud sdk

        :param schedule_start: 调度开始时间
        :type schedule_start: str
        :param schedule_end: 调度结束时间
        :type schedule_end: str
        :param schedule_type: 调度类型
        :type schedule_type: str
        :param schedule_date: 调度日期
        :type schedule_date: list[int]
        :param schedule_time: 调度时间列表
        :type schedule_time: list[str]
        """
        
        

        self._schedule_start = None
        self._schedule_end = None
        self._schedule_type = None
        self._schedule_date = None
        self._schedule_time = None
        self.discriminator = None

        if schedule_start is not None:
            self.schedule_start = schedule_start
        if schedule_end is not None:
            self.schedule_end = schedule_end
        if schedule_type is not None:
            self.schedule_type = schedule_type
        if schedule_date is not None:
            self.schedule_date = schedule_date
        if schedule_time is not None:
            self.schedule_time = schedule_time

    @property
    def schedule_start(self):
        """Gets the schedule_start of this ScheduleConf.

        调度开始时间

        :return: The schedule_start of this ScheduleConf.
        :rtype: str
        """
        return self._schedule_start

    @schedule_start.setter
    def schedule_start(self, schedule_start):
        """Sets the schedule_start of this ScheduleConf.

        调度开始时间

        :param schedule_start: The schedule_start of this ScheduleConf.
        :type schedule_start: str
        """
        self._schedule_start = schedule_start

    @property
    def schedule_end(self):
        """Gets the schedule_end of this ScheduleConf.

        调度结束时间

        :return: The schedule_end of this ScheduleConf.
        :rtype: str
        """
        return self._schedule_end

    @schedule_end.setter
    def schedule_end(self, schedule_end):
        """Sets the schedule_end of this ScheduleConf.

        调度结束时间

        :param schedule_end: The schedule_end of this ScheduleConf.
        :type schedule_end: str
        """
        self._schedule_end = schedule_end

    @property
    def schedule_type(self):
        """Gets the schedule_type of this ScheduleConf.

        调度类型

        :return: The schedule_type of this ScheduleConf.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this ScheduleConf.

        调度类型

        :param schedule_type: The schedule_type of this ScheduleConf.
        :type schedule_type: str
        """
        self._schedule_type = schedule_type

    @property
    def schedule_date(self):
        """Gets the schedule_date of this ScheduleConf.

        调度日期

        :return: The schedule_date of this ScheduleConf.
        :rtype: list[int]
        """
        return self._schedule_date

    @schedule_date.setter
    def schedule_date(self, schedule_date):
        """Sets the schedule_date of this ScheduleConf.

        调度日期

        :param schedule_date: The schedule_date of this ScheduleConf.
        :type schedule_date: list[int]
        """
        self._schedule_date = schedule_date

    @property
    def schedule_time(self):
        """Gets the schedule_time of this ScheduleConf.

        调度时间列表

        :return: The schedule_time of this ScheduleConf.
        :rtype: list[str]
        """
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, schedule_time):
        """Sets the schedule_time of this ScheduleConf.

        调度时间列表

        :param schedule_time: The schedule_time of this ScheduleConf.
        :type schedule_time: list[str]
        """
        self._schedule_time = schedule_time

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
        if not isinstance(other, ScheduleConf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
