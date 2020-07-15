# coding: utf-8

import pprint
import re

import six





class Eip:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ip_type': 'str',
        'bandwidth': 'Bandwidth'
    }

    attribute_map = {
        'ip_type': 'ip_type',
        'bandwidth': 'bandwidth'
    }

    def __init__(self, ip_type=None, bandwidth=None):
        """Eip - a model defined in huaweicloud sdk"""
        
        

        self._ip_type = None
        self._bandwidth = None
        self.discriminator = None

        self.ip_type = ip_type
        self.bandwidth = bandwidth

    @property
    def ip_type(self):
        """Gets the ip_type of this Eip.

        弹性IP地址类型。类型枚举值：5_bgp：全动态BGP;5_sbgp：静态BGP;5_telcom：中国电信;5_union：中国联通;详情请参见《虚拟私有云接口参考》“申请弹性公网IP”章节的“publicip”字段说明。

        :return: The ip_type of this Eip.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        """Sets the ip_type of this Eip.

        弹性IP地址类型。类型枚举值：5_bgp：全动态BGP;5_sbgp：静态BGP;5_telcom：中国电信;5_union：中国联通;详情请参见《虚拟私有云接口参考》“申请弹性公网IP”章节的“publicip”字段说明。

        :param ip_type: The ip_type of this Eip.
        :type: str
        """
        self._ip_type = ip_type

    @property
    def bandwidth(self):
        """Gets the bandwidth of this Eip.


        :return: The bandwidth of this Eip.
        :rtype: Bandwidth
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this Eip.


        :param bandwidth: The bandwidth of this Eip.
        :type: Bandwidth
        """
        self._bandwidth = bandwidth

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
        if not isinstance(other, Eip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
