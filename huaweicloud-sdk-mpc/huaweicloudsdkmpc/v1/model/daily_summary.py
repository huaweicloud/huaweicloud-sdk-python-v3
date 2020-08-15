# coding: utf-8

import pprint
import re

import six





class DailySummary:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'duration': 'float',
        'task_count': 'int',
        'date': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'task_count': 'task_count',
        'date': 'date'
    }

    def __init__(self, duration=None, task_count=None, date=None):
        """DailySummary - a model defined in huaweicloud sdk"""
        
        

        self._duration = None
        self._task_count = None
        self._date = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if task_count is not None:
            self.task_count = task_count
        if date is not None:
            self.date = date

    @property
    def duration(self):
        """Gets the duration of this DailySummary.

        转码源文件时长，单位：分钟，精确到小数点后两位。 

        :return: The duration of this DailySummary.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DailySummary.

        转码源文件时长，单位：分钟，精确到小数点后两位。 

        :param duration: The duration of this DailySummary.
        :type: float
        """
        self._duration = duration

    @property
    def task_count(self):
        """Gets the task_count of this DailySummary.

        任务数

        :return: The task_count of this DailySummary.
        :rtype: int
        """
        return self._task_count

    @task_count.setter
    def task_count(self, task_count):
        """Sets the task_count of this DailySummary.

        任务数

        :param task_count: The task_count of this DailySummary.
        :type: int
        """
        self._task_count = task_count

    @property
    def date(self):
        """Gets the date of this DailySummary.

        日期,格式样例：2018/03/01. 

        :return: The date of this DailySummary.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DailySummary.

        日期,格式样例：2018/03/01. 

        :param date: The date of this DailySummary.
        :type: str
        """
        self._date = date

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DailySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
