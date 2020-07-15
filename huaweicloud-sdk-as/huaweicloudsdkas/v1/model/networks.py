# coding: utf-8

import pprint
import re

import six





class Networks:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'ipv6_enable': 'bool',
        'ipv6_bandwidth': 'Ipv6Bandwidth'
    }

    attribute_map = {
        'id': 'id',
        'ipv6_enable': 'ipv6_enable',
        'ipv6_bandwidth': 'ipv6_bandwidth'
    }

    def __init__(self, id=None, ipv6_enable=None, ipv6_bandwidth=None):
        """Networks - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._ipv6_enable = None
        self._ipv6_bandwidth = None
        self.discriminator = None

        self.id = id
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth

    @property
    def id(self):
        """Gets the id of this Networks.

        网络ID。

        :return: The id of this Networks.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Networks.

        网络ID。

        :param id: The id of this Networks.
        :type: str
        """
        self._id = id

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this Networks.

        是否启用IPv6。取值为true时，标识此网卡已启用IPv6。

        :return: The ipv6_enable of this Networks.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this Networks.

        是否启用IPv6。取值为true时，标识此网卡已启用IPv6。

        :param ipv6_enable: The ipv6_enable of this Networks.
        :type: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def ipv6_bandwidth(self):
        """Gets the ipv6_bandwidth of this Networks.


        :return: The ipv6_bandwidth of this Networks.
        :rtype: Ipv6Bandwidth
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        """Sets the ipv6_bandwidth of this Networks.


        :param ipv6_bandwidth: The ipv6_bandwidth of this Networks.
        :type: Ipv6Bandwidth
        """
        self._ipv6_bandwidth = ipv6_bandwidth

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
        if not isinstance(other, Networks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
