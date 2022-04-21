# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """NeutronListFirewallRulesResponse

        The model defined in huaweicloud sdk

        :param firewall_rules: firewall_rule对象列表
        :type firewall_rules: list[:class:`huaweicloudsdkvpc.v2.NeutronFirewallRule`]
        :param firewall_rules_links: 分页信息
        :type firewall_rules_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        
        super(NeutronListFirewallRulesResponse, self).__init__()

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
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronFirewallRule`]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """Sets the firewall_rules of this NeutronListFirewallRulesResponse.

        firewall_rule对象列表

        :param firewall_rules: The firewall_rules of this NeutronListFirewallRulesResponse.
        :type firewall_rules: list[:class:`huaweicloudsdkvpc.v2.NeutronFirewallRule`]
        """
        self._firewall_rules = firewall_rules

    @property
    def firewall_rules_links(self):
        """Gets the firewall_rules_links of this NeutronListFirewallRulesResponse.

        分页信息

        :return: The firewall_rules_links of this NeutronListFirewallRulesResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        return self._firewall_rules_links

    @firewall_rules_links.setter
    def firewall_rules_links(self, firewall_rules_links):
        """Sets the firewall_rules_links of this NeutronListFirewallRulesResponse.

        分页信息

        :param firewall_rules_links: The firewall_rules_links of this NeutronListFirewallRulesResponse.
        :type firewall_rules_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NeutronListFirewallRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
