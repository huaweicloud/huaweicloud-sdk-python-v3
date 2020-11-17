# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class NeutronShowFirewallGroupResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'firewall_group': 'NeutronFirewallGroup'
    }

    attribute_map = {
        'firewall_group': 'firewall_group'
    }

    def __init__(self, firewall_group=None):
        """NeutronShowFirewallGroupResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._firewall_group = None
        self.discriminator = None

        if firewall_group is not None:
            self.firewall_group = firewall_group

    @property
    def firewall_group(self):
        """Gets the firewall_group of this NeutronShowFirewallGroupResponse.


        :return: The firewall_group of this NeutronShowFirewallGroupResponse.
        :rtype: NeutronFirewallGroup
        """
        return self._firewall_group

    @firewall_group.setter
    def firewall_group(self, firewall_group):
        """Sets the firewall_group of this NeutronShowFirewallGroupResponse.


        :param firewall_group: The firewall_group of this NeutronShowFirewallGroupResponse.
        :type: NeutronFirewallGroup
        """
        self._firewall_group = firewall_group

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
        if not isinstance(other, NeutronShowFirewallGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
