# coding: utf-8

import pprint
import re

import six





class UpdateFirewallRuleOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'egress_firewall_policy': 'FirewallPolicy',
        'ingress_firewall_policy': 'FirewallPolicy'
    }

    attribute_map = {
        'egress_firewall_policy': 'egress_firewall_policy',
        'ingress_firewall_policy': 'ingress_firewall_policy'
    }

    def __init__(self, egress_firewall_policy=None, ingress_firewall_policy=None):
        """UpdateFirewallRuleOption - a model defined in huaweicloud sdk"""
        
        

        self._egress_firewall_policy = None
        self._ingress_firewall_policy = None
        self.discriminator = None

        self.egress_firewall_policy = egress_firewall_policy
        self.ingress_firewall_policy = ingress_firewall_policy

    @property
    def egress_firewall_policy(self):
        """Gets the egress_firewall_policy of this UpdateFirewallRuleOption.


        :return: The egress_firewall_policy of this UpdateFirewallRuleOption.
        :rtype: FirewallPolicy
        """
        return self._egress_firewall_policy

    @egress_firewall_policy.setter
    def egress_firewall_policy(self, egress_firewall_policy):
        """Sets the egress_firewall_policy of this UpdateFirewallRuleOption.


        :param egress_firewall_policy: The egress_firewall_policy of this UpdateFirewallRuleOption.
        :type: FirewallPolicy
        """
        self._egress_firewall_policy = egress_firewall_policy

    @property
    def ingress_firewall_policy(self):
        """Gets the ingress_firewall_policy of this UpdateFirewallRuleOption.


        :return: The ingress_firewall_policy of this UpdateFirewallRuleOption.
        :rtype: FirewallPolicy
        """
        return self._ingress_firewall_policy

    @ingress_firewall_policy.setter
    def ingress_firewall_policy(self, ingress_firewall_policy):
        """Sets the ingress_firewall_policy of this UpdateFirewallRuleOption.


        :param ingress_firewall_policy: The ingress_firewall_policy of this UpdateFirewallRuleOption.
        :type: FirewallPolicy
        """
        self._ingress_firewall_policy = ingress_firewall_policy

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
        if not isinstance(other, UpdateFirewallRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
