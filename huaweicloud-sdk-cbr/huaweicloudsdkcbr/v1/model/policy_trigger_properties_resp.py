# coding: utf-8

import pprint
import re

import six





class PolicyTriggerPropertiesResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pattern': 'list[str]',
        'start_time': 'str'
    }

    attribute_map = {
        'pattern': 'pattern',
        'start_time': 'start_time'
    }

    def __init__(self, pattern=None, start_time=None):
        """PolicyTriggerPropertiesResp - a model defined in huaweicloud sdk"""
        
        

        self._pattern = None
        self._start_time = None
        self.discriminator = None

        self.pattern = pattern
        if start_time is not None:
            self.start_time = start_time

    @property
    def pattern(self):
        """Gets the pattern of this PolicyTriggerPropertiesResp.

        调度器的调度策略，长度限制为10240个字符，参照iCalendar RFC 2445规范，但仅支持FREQ、BYDAY、BYHOUR、BYMINUTE四个参数，其中FREQ仅支持WEEKLY和DAILY，BYDAY支持一周七天（MO、TU、WE、TH、FR、SA、SU），BYHOUR支持0-23小时，BYMINUTE支持0-59分钟，并且时间点间隔不能小于一小时，一个备份策略可以同时设置多个备份时间点，一天最多可以设置24个时间点。

        :return: The pattern of this PolicyTriggerPropertiesResp.
        :rtype: list[str]
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this PolicyTriggerPropertiesResp.

        调度器的调度策略，长度限制为10240个字符，参照iCalendar RFC 2445规范，但仅支持FREQ、BYDAY、BYHOUR、BYMINUTE四个参数，其中FREQ仅支持WEEKLY和DAILY，BYDAY支持一周七天（MO、TU、WE、TH、FR、SA、SU），BYHOUR支持0-23小时，BYMINUTE支持0-59分钟，并且时间点间隔不能小于一小时，一个备份策略可以同时设置多个备份时间点，一天最多可以设置24个时间点。

        :param pattern: The pattern of this PolicyTriggerPropertiesResp.
        :type: list[str]
        """
        self._pattern = pattern

    @property
    def start_time(self):
        """Gets the start_time of this PolicyTriggerPropertiesResp.

        调度器开始时间，例如：\"2020-01-08 09:59:49\"

        :return: The start_time of this PolicyTriggerPropertiesResp.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PolicyTriggerPropertiesResp.

        调度器开始时间，例如：\"2020-01-08 09:59:49\"

        :param start_time: The start_time of this PolicyTriggerPropertiesResp.
        :type: str
        """
        self._start_time = start_time

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
        if not isinstance(other, PolicyTriggerPropertiesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
