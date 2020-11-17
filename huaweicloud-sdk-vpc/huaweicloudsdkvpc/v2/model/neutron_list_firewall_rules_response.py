# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class NeutronListFirewallRulesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'firewall_rules': 'list[NeutronFirewallRule]',
        'firewall_rules_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'firewall_rules': 'firewall_rules',
        'firewall_rules_links': 'firewall_rules_links'
    }

    def __init__(self, firewall_rules=None, firewall_rules_links=None):
        """NeutronListFirewallRulesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._firewall_rules = None
        self._firewall_rules_links = None
        self.discriminator = None

        if firewall_rules is not None:
            self.firewall_rules = firewall_rules
        if firewall_rules_links is not None:
            self.firewall_rules_links = firewall_rules_links

    @property
    def firewall_rules(self):
        """Gets the firewall_rules of this NeutronListFirewallRulesResponse.

        firewall_rule对象列表

        :return: The firewall_rules of this NeutronListFirewallRulesResponse.
        :rtype: list[NeutronFirewallRule]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """Sets the firewall_rules of this NeutronListFirewallRulesResponse.

        firewall_rule对象列表

        :param firewall_rules: The firewall_rules of this NeutronListFirewallRulesResponse.
        :type: list[NeutronFirewallRule]
        """
        self._firewall_rules = firewall_rules

    @property
    def firewall_rules_links(self):
        """Gets the firewall_rules_links of this NeutronListFirewallRulesResponse.

        分页信息

        :return: The firewall_rules_links of this NeutronListFirewallRulesResponse.
        :rtype: list[NeutronPageLink]
        """
        return self._firewall_rules_links

    @firewall_rules_links.setter
    def firewall_rules_links(self, firewall_rules_links):
        """Sets the firewall_rules_links of this NeutronListFirewallRulesResponse.

        分页信息

        :param firewall_rules_links: The firewall_rules_links of this NeutronListFirewallRulesResponse.
        :type: list[NeutronPageLink]
        """
        self._firewall_rules_links = firewall_rules_links

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
        if not isinstance(other, NeutronListFirewallRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
