# coding: utf-8

import pprint
import re

import six





class TaskPolicy:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'schedule_time': 'str',
        'retry_count': 'int',
        'retry_interval': 'int'
    }

    attribute_map = {
        'schedule_time': 'schedule_time',
        'retry_count': 'retry_count',
        'retry_interval': 'retry_interval'
    }

    def __init__(self, schedule_time=None, retry_count=None, retry_interval=None):
        """TaskPolicy - a model defined in huaweicloud sdk"""
        
        

        self._schedule_time = None
        self._retry_count = None
        self._retry_interval = None
        self.discriminator = None

        if schedule_time is not None:
            self.schedule_time = schedule_time
        if retry_count is not None:
            self.retry_count = retry_count
        if retry_interval is not None:
            self.retry_interval = retry_interval

    @property
    def schedule_time(self):
        """Gets the schedule_time of this TaskPolicy.

        批量任务指定执行时间，取值范围为7天内，不传入此参数表示立即执行，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The schedule_time of this TaskPolicy.
        :rtype: str
        """
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, schedule_time):
        """Sets the schedule_time of this TaskPolicy.

        批量任务指定执行时间，取值范围为7天内，不传入此参数表示立即执行，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param schedule_time: The schedule_time of this TaskPolicy.
        :type: str
        """
        self._schedule_time = schedule_time

    @property
    def retry_count(self):
        """Gets the retry_count of this TaskPolicy.

        批量任务子任务自动重试次数，如果传入retry_interval参数，则需传入该参数，最大支持重试5次。

        :return: The retry_count of this TaskPolicy.
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """Sets the retry_count of this TaskPolicy.

        批量任务子任务自动重试次数，如果传入retry_interval参数，则需传入该参数，最大支持重试5次。

        :param retry_count: The retry_count of this TaskPolicy.
        :type: int
        """
        self._retry_count = retry_count

    @property
    def retry_interval(self):
        """Gets the retry_interval of this TaskPolicy.

        批量任务子任务失败后，自动重试时间间隔，单位：分钟，最大1440(24小时)，不传入此参数表示不重试，如果传入retry_count参数则需要传入该参数。

        :return: The retry_interval of this TaskPolicy.
        :rtype: int
        """
        return self._retry_interval

    @retry_interval.setter
    def retry_interval(self, retry_interval):
        """Sets the retry_interval of this TaskPolicy.

        批量任务子任务失败后，自动重试时间间隔，单位：分钟，最大1440(24小时)，不传入此参数表示不重试，如果传入retry_count参数则需要传入该参数。

        :param retry_interval: The retry_interval of this TaskPolicy.
        :type: int
        """
        self._retry_interval = retry_interval

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
        if not isinstance(other, TaskPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
