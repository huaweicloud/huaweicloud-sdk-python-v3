# coding: utf-8

import pprint
import re

import six


class NeutronRemoveFirewallRuleResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'description': 'str',
        'audited': 'bool',
        'firewall_rules': 'list[str]',
        'id': 'str',
        'name': 'str',
        'public': 'bool',
        'tenant_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'audited': 'audited',
        'firewall_rules': 'firewall_rules',
        'id': 'id',
        'name': 'name',
        'public': 'public',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, description=None, audited=False, firewall_rules=None, id=None, name=None, public=False, tenant_id=None):  # noqa: E501
        """NeutronRemoveFirewallRuleResponse - a model defined in huaweicloud sdk"""

        self._description = None
        self._audited = None
        self._firewall_rules = None
        self._id = None
        self._name = None
        self._public = None
        self._tenant_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if audited is not None:
            self.audited = audited
        if firewall_rules is not None:
            self.firewall_rules = firewall_rules
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if public is not None:
            self.public = public
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def description(self):
        """Gets the description of this NeutronRemoveFirewallRuleResponse.

        对policy的描述信息

        :return: The description of this NeutronRemoveFirewallRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronRemoveFirewallRuleResponse.

        对policy的描述信息

        :param description: The description of this NeutronRemoveFirewallRuleResponse.
        :type: str
        """
        self._description = description

    @property
    def audited(self):
        """Gets the audited of this NeutronRemoveFirewallRuleResponse.

        每次policy或者它相关的rule有变动，该参数将会被置为False

        :return: The audited of this NeutronRemoveFirewallRuleResponse.
        :rtype: bool
        """
        return self._audited

    @audited.setter
    def audited(self, audited):
        """Sets the audited of this NeutronRemoveFirewallRuleResponse.

        每次policy或者它相关的rule有变动，该参数将会被置为False

        :param audited: The audited of this NeutronRemoveFirewallRuleResponse.
        :type: bool
        """
        self._audited = audited

    @property
    def firewall_rules(self):
        """Gets the firewall_rules of this NeutronRemoveFirewallRuleResponse.

        与当前policy相关联的rule的ID列表

        :return: The firewall_rules of this NeutronRemoveFirewallRuleResponse.
        :rtype: list[str]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """Sets the firewall_rules of this NeutronRemoveFirewallRuleResponse.

        与当前policy相关联的rule的ID列表

        :param firewall_rules: The firewall_rules of this NeutronRemoveFirewallRuleResponse.
        :type: list[str]
        """
        self._firewall_rules = firewall_rules

    @property
    def id(self):
        """Gets the id of this NeutronRemoveFirewallRuleResponse.

        Policy ID

        :return: The id of this NeutronRemoveFirewallRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronRemoveFirewallRuleResponse.

        Policy ID

        :param id: The id of this NeutronRemoveFirewallRuleResponse.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NeutronRemoveFirewallRuleResponse.

        Policy 名称

        :return: The name of this NeutronRemoveFirewallRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronRemoveFirewallRuleResponse.

        Policy 名称

        :param name: The name of this NeutronRemoveFirewallRuleResponse.
        :type: str
        """
        self._name = name

    @property
    def public(self):
        """Gets the public of this NeutronRemoveFirewallRuleResponse.

        如果为True, 该policy对于其他项目网络ACL防火墙策略可见， 默认不可见

        :return: The public of this NeutronRemoveFirewallRuleResponse.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this NeutronRemoveFirewallRuleResponse.

        如果为True, 该policy对于其他项目网络ACL防火墙策略可见， 默认不可见

        :param public: The public of this NeutronRemoveFirewallRuleResponse.
        :type: bool
        """
        self._public = public

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronRemoveFirewallRuleResponse.

        项目ID

        :return: The tenant_id of this NeutronRemoveFirewallRuleResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronRemoveFirewallRuleResponse.

        项目ID

        :param tenant_id: The tenant_id of this NeutronRemoveFirewallRuleResponse.
        :type: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, NeutronRemoveFirewallRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
