# coding: utf-8

import pprint
import re

import six


class NovaAttachInterfaceFixedIp(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'ip_address': 'str'
    }

    attribute_map = {
        'ip_address': 'ip_address'
    }

    def __init__(self, ip_address=None):  # noqa: E501
        """NovaAttachInterfaceFixedIp - a model defined in huaweicloud sdk"""

        self._ip_address = None
        self.discriminator = None

        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def ip_address(self):
        """Gets the ip_address of this NovaAttachInterfaceFixedIp.

        IP地址。

        :return: The ip_address of this NovaAttachInterfaceFixedIp.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this NovaAttachInterfaceFixedIp.

        IP地址。

        :param ip_address: The ip_address of this NovaAttachInterfaceFixedIp.
        :type: str
        """
        self._ip_address = ip_address

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
        if not isinstance(other, NovaAttachInterfaceFixedIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
