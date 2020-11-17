# coding: utf-8

import pprint
import re

import six





class NeutronUpdateFirewallRuleRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'firewall_rule': 'NeutronUpdateFirewallRuleOption'
    }

    attribute_map = {
        'firewall_rule': 'firewall_rule'
    }

    def __init__(self, firewall_rule=None):
        """NeutronUpdateFirewallRuleRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._firewall_rule = None
        self.discriminator = None

        self.firewall_rule = firewall_rule

    @property
    def firewall_rule(self):
        """Gets the firewall_rule of this NeutronUpdateFirewallRuleRequestBody.


        :return: The firewall_rule of this NeutronUpdateFirewallRuleRequestBody.
        :rtype: NeutronUpdateFirewallRuleOption
        """
        return self._firewall_rule

    @firewall_rule.setter
    def firewall_rule(self, firewall_rule):
        """Sets the firewall_rule of this NeutronUpdateFirewallRuleRequestBody.


        :param firewall_rule: The firewall_rule of this NeutronUpdateFirewallRuleRequestBody.
        :type: NeutronUpdateFirewallRuleOption
        """
        self._firewall_rule = firewall_rule

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
        if not isinstance(other, NeutronUpdateFirewallRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
