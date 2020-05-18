# coding: utf-8

import pprint
import re

import six


class NovaAddFloatingIpOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'address': 'str',
        'fixed_address': 'str'
    }

    attribute_map = {
        'address': 'address',
        'fixed_address': 'fixed_address'
    }

    def __init__(self, address=None, fixed_address=None):  # noqa: E501
        """NovaAddFloatingIpOption - a model defined in huaweicloud sdk"""

        self._address = None
        self._fixed_address = None
        self.discriminator = None

        self.address = address
        if fixed_address is not None:
            self.fixed_address = fixed_address

    @property
    def address(self):
        """Gets the address of this NovaAddFloatingIpOption.

        浮动IP的IP地址。

        :return: The address of this NovaAddFloatingIpOption.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this NovaAddFloatingIpOption.

        浮动IP的IP地址。

        :param address: The address of this NovaAddFloatingIpOption.
        :type: str
        """
        self._address = address

    @property
    def fixed_address(self):
        """Gets the fixed_address of this NovaAddFloatingIpOption.

        固定IP的IP地址，即你想要关联浮动IP的那个固定IP地址。

        :return: The fixed_address of this NovaAddFloatingIpOption.
        :rtype: str
        """
        return self._fixed_address

    @fixed_address.setter
    def fixed_address(self, fixed_address):
        """Sets the fixed_address of this NovaAddFloatingIpOption.

        固定IP的IP地址，即你想要关联浮动IP的那个固定IP地址。

        :param fixed_address: The fixed_address of this NovaAddFloatingIpOption.
        :type: str
        """
        self._fixed_address = fixed_address

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
        if not isinstance(other, NovaAddFloatingIpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
