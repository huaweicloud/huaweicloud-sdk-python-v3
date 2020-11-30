# coding: utf-8

import pprint
import re

import six





class TrafficInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'traffic': 'int',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'traffic': 'traffic',
        'timestamp': 'timestamp'
    }

    def __init__(self, traffic=None, timestamp=None):
        """TrafficInfo - a model defined in huaweicloud sdk"""
        
        

        self._traffic = None
        self._timestamp = None
        self.discriminator = None

        self.traffic = traffic
        self.timestamp = timestamp

    @property
    def traffic(self):
        """Gets the traffic of this TrafficInfo.

        采样周期内的总流量，单位：byte

        :return: The traffic of this TrafficInfo.
        :rtype: int
        """
        return self._traffic

    @traffic.setter
    def traffic(self, traffic):
        """Sets the traffic of this TrafficInfo.

        采样周期内的总流量，单位：byte

        :param traffic: The traffic of this TrafficInfo.
        :type: int
        """
        self._traffic = traffic

    @property
    def timestamp(self):
        """Gets the timestamp of this TrafficInfo.

        流量数据采样周期起始时刻，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The timestamp of this TrafficInfo.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TrafficInfo.

        流量数据采样周期起始时刻，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :param timestamp: The timestamp of this TrafficInfo.
        :type: datetime
        """
        self._timestamp = timestamp

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
        if not isinstance(other, TrafficInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
