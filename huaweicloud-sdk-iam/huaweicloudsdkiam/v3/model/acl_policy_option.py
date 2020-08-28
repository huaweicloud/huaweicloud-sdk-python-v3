# coding: utf-8

import pprint
import re

import six





class AclPolicyOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'allow_address_netmasks': 'list[AllowAddressNetmasksOption]',
        'allow_ip_ranges': 'list[AllowIpRangesOption]'
    }

    attribute_map = {
        'allow_address_netmasks': 'allow_address_netmasks',
        'allow_ip_ranges': 'allow_ip_ranges'
    }

    def __init__(self, allow_address_netmasks=None, allow_ip_ranges=None):
        """AclPolicyOption - a model defined in huaweicloud sdk"""
        
        

        self._allow_address_netmasks = None
        self._allow_ip_ranges = None
        self.discriminator = None

        self.allow_address_netmasks = allow_address_netmasks
        self.allow_ip_ranges = allow_ip_ranges

    @property
    def allow_address_netmasks(self):
        """Gets the allow_address_netmasks of this AclPolicyOption.

        允许访问的IP地址或网段。

        :return: The allow_address_netmasks of this AclPolicyOption.
        :rtype: list[AllowAddressNetmasksOption]
        """
        return self._allow_address_netmasks

    @allow_address_netmasks.setter
    def allow_address_netmasks(self, allow_address_netmasks):
        """Sets the allow_address_netmasks of this AclPolicyOption.

        允许访问的IP地址或网段。

        :param allow_address_netmasks: The allow_address_netmasks of this AclPolicyOption.
        :type: list[AllowAddressNetmasksOption]
        """
        self._allow_address_netmasks = allow_address_netmasks

    @property
    def allow_ip_ranges(self):
        """Gets the allow_ip_ranges of this AclPolicyOption.

        允许访问的IP地址区间

        :return: The allow_ip_ranges of this AclPolicyOption.
        :rtype: list[AllowIpRangesOption]
        """
        return self._allow_ip_ranges

    @allow_ip_ranges.setter
    def allow_ip_ranges(self, allow_ip_ranges):
        """Sets the allow_ip_ranges of this AclPolicyOption.

        允许访问的IP地址区间

        :param allow_ip_ranges: The allow_ip_ranges of this AclPolicyOption.
        :type: list[AllowIpRangesOption]
        """
        self._allow_ip_ranges = allow_ip_ranges

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
        if not isinstance(other, AclPolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
