# coding: utf-8

import pprint
import re

import six





class BandwidthInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bw_bps': 'int',
        'timestamp': 'str'
    }

    attribute_map = {
        'bw_bps': 'bw_bps',
        'timestamp': 'timestamp'
    }

    def __init__(self, bw_bps=None, timestamp=None):
        """BandwidthInfo - a model defined in huaweicloud sdk"""
        
        

        self._bw_bps = None
        self._timestamp = None
        self.discriminator = None

        self.bw_bps = bw_bps
        self.timestamp = timestamp

    @property
    def bw_bps(self):
        """Gets the bw_bps of this BandwidthInfo.

        带宽峰值，单位：bps

        :return: The bw_bps of this BandwidthInfo.
        :rtype: int
        """
        return self._bw_bps

    @bw_bps.setter
    def bw_bps(self, bw_bps):
        """Sets the bw_bps of this BandwidthInfo.

        带宽峰值，单位：bps

        :param bw_bps: The bw_bps of this BandwidthInfo.
        :type: int
        """
        self._bw_bps = bw_bps

    @property
    def timestamp(self):
        """Gets the timestamp of this BandwidthInfo.

        带宽数据采样周期起始时刻，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The timestamp of this BandwidthInfo.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BandwidthInfo.

        带宽数据采样周期起始时刻，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :param timestamp: The timestamp of this BandwidthInfo.
        :type: str
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
        if not isinstance(other, BandwidthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
