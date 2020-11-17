# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class NeutronListFirewallPoliciesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'firewall_policies': 'list[NeutronFirewallPolicy]',
        'firewall_policies_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'firewall_policies': 'firewall_policies',
        'firewall_policies_links': 'firewall_policies_links'
    }

    def __init__(self, firewall_policies=None, firewall_policies_links=None):
        """NeutronListFirewallPoliciesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._firewall_policies = None
        self._firewall_policies_links = None
        self.discriminator = None

        if firewall_policies is not None:
            self.firewall_policies = firewall_policies
        if firewall_policies_links is not None:
            self.firewall_policies_links = firewall_policies_links

    @property
    def firewall_policies(self):
        """Gets the firewall_policies of this NeutronListFirewallPoliciesResponse.

        firewall_policy对象列表

        :return: The firewall_policies of this NeutronListFirewallPoliciesResponse.
        :rtype: list[NeutronFirewallPolicy]
        """
        return self._firewall_policies

    @firewall_policies.setter
    def firewall_policies(self, firewall_policies):
        """Sets the firewall_policies of this NeutronListFirewallPoliciesResponse.

        firewall_policy对象列表

        :param firewall_policies: The firewall_policies of this NeutronListFirewallPoliciesResponse.
        :type: list[NeutronFirewallPolicy]
        """
        self._firewall_policies = firewall_policies

    @property
    def firewall_policies_links(self):
        """Gets the firewall_policies_links of this NeutronListFirewallPoliciesResponse.

        分页信息

        :return: The firewall_policies_links of this NeutronListFirewallPoliciesResponse.
        :rtype: list[NeutronPageLink]
        """
        return self._firewall_policies_links

    @firewall_policies_links.setter
    def firewall_policies_links(self, firewall_policies_links):
        """Sets the firewall_policies_links of this NeutronListFirewallPoliciesResponse.

        分页信息

        :param firewall_policies_links: The firewall_policies_links of this NeutronListFirewallPoliciesResponse.
        :type: list[NeutronPageLink]
        """
        self._firewall_policies_links = firewall_policies_links

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
        if not isinstance(other, NeutronListFirewallPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
