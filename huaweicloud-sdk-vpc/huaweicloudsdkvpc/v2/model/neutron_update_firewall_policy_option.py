# coding: utf-8

import pprint
import re

import six





class NeutronUpdateFirewallPolicyOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'firewall_rules': 'list[str]',
        'audited': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'firewall_rules': 'firewall_rules',
        'audited': 'audited'
    }

    def __init__(self, name=None, description=None, firewall_rules=None, audited=False):
        """NeutronUpdateFirewallPolicyOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._firewall_rules = None
        self._audited = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if firewall_rules is not None:
            self.firewall_rules = firewall_rules
        if audited is not None:
            self.audited = audited

    @property
    def name(self):
        """Gets the name of this NeutronUpdateFirewallPolicyOption.

        功能说明：网络ACL防火墙策略名称 取值范围：最长255个字符

        :return: The name of this NeutronUpdateFirewallPolicyOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronUpdateFirewallPolicyOption.

        功能说明：网络ACL防火墙策略名称 取值范围：最长255个字符

        :param name: The name of this NeutronUpdateFirewallPolicyOption.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NeutronUpdateFirewallPolicyOption.

        功能说明：网络ACL防火墙策略描述 取值范围：最长255个字符

        :return: The description of this NeutronUpdateFirewallPolicyOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronUpdateFirewallPolicyOption.

        功能说明：网络ACL防火墙策略描述 取值范围：最长255个字符

        :param description: The description of this NeutronUpdateFirewallPolicyOption.
        :type: str
        """
        self._description = description

    @property
    def firewall_rules(self):
        """Gets the firewall_rules of this NeutronUpdateFirewallPolicyOption.

        功能说明：网络ACL策略关联的规则列表

        :return: The firewall_rules of this NeutronUpdateFirewallPolicyOption.
        :rtype: list[str]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """Sets the firewall_rules of this NeutronUpdateFirewallPolicyOption.

        功能说明：网络ACL策略关联的规则列表

        :param firewall_rules: The firewall_rules of this NeutronUpdateFirewallPolicyOption.
        :type: list[str]
        """
        self._firewall_rules = firewall_rules

    @property
    def audited(self):
        """Gets the audited of this NeutronUpdateFirewallPolicyOption.

        审计标记。

        :return: The audited of this NeutronUpdateFirewallPolicyOption.
        :rtype: bool
        """
        return self._audited

    @audited.setter
    def audited(self, audited):
        """Sets the audited of this NeutronUpdateFirewallPolicyOption.

        审计标记。

        :param audited: The audited of this NeutronUpdateFirewallPolicyOption.
        :type: bool
        """
        self._audited = audited

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
        if not isinstance(other, NeutronUpdateFirewallPolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
