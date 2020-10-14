# coding: utf-8

import pprint
import re

import six





class TrafficData:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'value': 'int',
        'time': 'str'
    }

    attribute_map = {
        'value': 'value',
        'time': 'time'
    }

    def __init__(self, value=None, time=None):
        """TrafficData - a model defined in huaweicloud sdk"""
        
        

        self._value = None
        self._time = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if time is not None:
            self.time = time

    @property
    def value(self):
        """Gets the value of this TrafficData.

        采样值，单位为byte。

        :return: The value of this TrafficData.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TrafficData.

        采样值，单位为byte。

        :param value: The value of this TrafficData.
        :type: int
        """
        self._value = value

    @property
    def time(self):
        """Gets the time of this TrafficData.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :return: The time of this TrafficData.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TrafficData.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :param time: The time of this TrafficData.
        :type: str
        """
        self._time = time

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
        if not isinstance(other, TrafficData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
