# coding: utf-8

import pprint
import re

import six


class ListIpAddressGroupResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'address_groups': 'list[AddressGroupResp]'
    }

    attribute_map = {
        'address_groups': 'address_groups'
    }

    def __init__(self, address_groups=None):  # noqa: E501
        """ListIpAddressGroupResponse - a model defined in huaweicloud sdk"""

        self._address_groups = None
        self.discriminator = None

        if address_groups is not None:
            self.address_groups = address_groups

    @property
    def address_groups(self):
        """Gets the address_groups of this ListIpAddressGroupResponse.

        地址组对象列表

        :return: The address_groups of this ListIpAddressGroupResponse.
        :rtype: list[AddressGroupResp]
        """
        return self._address_groups

    @address_groups.setter
    def address_groups(self, address_groups):
        """Sets the address_groups of this ListIpAddressGroupResponse.

        地址组对象列表

        :param address_groups: The address_groups of this ListIpAddressGroupResponse.
        :type: list[AddressGroupResp]
        """
        self._address_groups = address_groups

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
        if not isinstance(other, ListIpAddressGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
