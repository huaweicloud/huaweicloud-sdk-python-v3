# coding: utf-8

import pprint
import re

import six





class NetAddress:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'port': 'int',
        'domain': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'port': 'port',
        'domain': 'domain'
    }

    def __init__(self, ip=None, port=None, domain=None):
        """NetAddress - a model defined in huaweicloud sdk"""
        
        

        self._ip = None
        self._port = None
        self._domain = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if domain is not None:
            self.domain = domain

    @property
    def ip(self):
        """Gets the ip of this NetAddress.

        服务的对应IP

        :return: The ip of this NetAddress.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this NetAddress.

        服务的对应IP

        :param ip: The ip of this NetAddress.
        :type: str
        """
        self._ip = ip

    @property
    def port(self):
        """Gets the port of this NetAddress.

        服务对应端口

        :return: The port of this NetAddress.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this NetAddress.

        服务对应端口

        :param port: The port of this NetAddress.
        :type: int
        """
        self._port = port

    @property
    def domain(self):
        """Gets the domain of this NetAddress.

        服务对应的域名

        :return: The domain of this NetAddress.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this NetAddress.

        服务对应的域名

        :param domain: The domain of this NetAddress.
        :type: str
        """
        self._domain = domain

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
        if not isinstance(other, NetAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
