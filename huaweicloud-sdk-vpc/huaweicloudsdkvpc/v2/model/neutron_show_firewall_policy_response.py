# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class NeutronShowFirewallPolicyResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'firewall_policy': 'NeutronFirewallPolicy'
    }

    attribute_map = {
        'firewall_policy': 'firewall_policy'
    }

    def __init__(self, firewall_policy=None):
        """NeutronShowFirewallPolicyResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._firewall_policy = None
        self.discriminator = None

        if firewall_policy is not None:
            self.firewall_policy = firewall_policy

    @property
    def firewall_policy(self):
        """Gets the firewall_policy of this NeutronShowFirewallPolicyResponse.


        :return: The firewall_policy of this NeutronShowFirewallPolicyResponse.
        :rtype: NeutronFirewallPolicy
        """
        return self._firewall_policy

    @firewall_policy.setter
    def firewall_policy(self, firewall_policy):
        """Sets the firewall_policy of this NeutronShowFirewallPolicyResponse.


        :param firewall_policy: The firewall_policy of this NeutronShowFirewallPolicyResponse.
        :type: NeutronFirewallPolicy
        """
        self._firewall_policy = firewall_policy

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
        if not isinstance(other, NeutronShowFirewallPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
