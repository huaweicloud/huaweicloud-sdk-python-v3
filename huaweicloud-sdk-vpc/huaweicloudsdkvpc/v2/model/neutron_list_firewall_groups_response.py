# coding: utf-8

import pprint
import re

import six


class NeutronListFirewallGroupsResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'firewall_groups': 'list[NeutronFirewallGroup]'
    }

    attribute_map = {
        'firewall_groups': 'firewall_groups'
    }

    def __init__(self, firewall_groups=None):  # noqa: E501
        """NeutronListFirewallGroupsResponse - a model defined in huaweicloud sdk"""

        self._firewall_groups = None
        self.discriminator = None

        if firewall_groups is not None:
            self.firewall_groups = firewall_groups

    @property
    def firewall_groups(self):
        """Gets the firewall_groups of this NeutronListFirewallGroupsResponse.

        firewall_group对象列表

        :return: The firewall_groups of this NeutronListFirewallGroupsResponse.
        :rtype: list[NeutronFirewallGroup]
        """
        return self._firewall_groups

    @firewall_groups.setter
    def firewall_groups(self, firewall_groups):
        """Sets the firewall_groups of this NeutronListFirewallGroupsResponse.

        firewall_group对象列表

        :param firewall_groups: The firewall_groups of this NeutronListFirewallGroupsResponse.
        :type: list[NeutronFirewallGroup]
        """
        self._firewall_groups = firewall_groups

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
        if not isinstance(other, NeutronListFirewallGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
