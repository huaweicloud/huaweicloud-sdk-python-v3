# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_address': 'str',
        'ipv6_address': 'str',
        'bandwidth_size': 'int'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'ipv6_address': 'ipv6_address',
        'bandwidth_size': 'bandwidth_size'
    }

    def __init__(self, ip_address=None, ipv6_address=None, bandwidth_size=None):
        """IpDetails

        The model defined in huaweicloud sdk

        :param ip_address: IP地址
        :type ip_address: str
        :param ipv6_address: IPV6地址
        :type ipv6_address: str
        :param bandwidth_size: 带宽大小
        :type bandwidth_size: int
        """
        
        

        self._ip_address = None
        self._ipv6_address = None
        self._bandwidth_size = None
        self.discriminator = None

        if ip_address is not None:
            self.ip_address = ip_address
        if ipv6_address is not None:
            self.ipv6_address = ipv6_address
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size

    @property
    def ip_address(self):
        """Gets the ip_address of this IpDetails.

        IP地址

        :return: The ip_address of this IpDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this IpDetails.

        IP地址

        :param ip_address: The ip_address of this IpDetails.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def ipv6_address(self):
        """Gets the ipv6_address of this IpDetails.

        IPV6地址

        :return: The ipv6_address of this IpDetails.
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """Sets the ipv6_address of this IpDetails.

        IPV6地址

        :param ipv6_address: The ipv6_address of this IpDetails.
        :type ipv6_address: str
        """
        self._ipv6_address = ipv6_address

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this IpDetails.

        带宽大小

        :return: The bandwidth_size of this IpDetails.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this IpDetails.

        带宽大小

        :param bandwidth_size: The bandwidth_size of this IpDetails.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

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
        if not isinstance(other, IpDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
