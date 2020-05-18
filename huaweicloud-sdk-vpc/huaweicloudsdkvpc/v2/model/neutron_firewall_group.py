# coding: utf-8

import pprint
import re

import six


class NeutronFirewallGroup(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'admin_state_up': 'bool',
        'description': 'str',
        'egress_firewall_policy_id': 'str',
        'id': 'str',
        'ingress_firewall_policy_id': 'str',
        'name': 'str',
        'ports': 'list[str]',
        'public': 'bool',
        'status': 'str',
        'tenant_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'egress_firewall_policy_id': 'egress_firewall_policy_id',
        'id': 'id',
        'ingress_firewall_policy_id': 'ingress_firewall_policy_id',
        'name': 'name',
        'ports': 'ports',
        'public': 'public',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id'
    }

    def __init__(self, admin_state_up=None, description=None, egress_firewall_policy_id=None, id=None, ingress_firewall_policy_id=None, name=None, ports=None, public=None, status=None, tenant_id=None, project_id=None):  # noqa: E501
        """NeutronFirewallGroup - a model defined in huaweicloud sdk"""

        self._admin_state_up = None
        self._description = None
        self._egress_firewall_policy_id = None
        self._id = None
        self._ingress_firewall_policy_id = None
        self._name = None
        self._ports = None
        self._public = None
        self._status = None
        self._tenant_id = None
        self._project_id = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.description = description
        self.egress_firewall_policy_id = egress_firewall_policy_id
        self.id = id
        self.ingress_firewall_policy_id = ingress_firewall_policy_id
        self.name = name
        self.ports = ports
        self.public = public
        self.status = status
        self.tenant_id = tenant_id
        self.project_id = project_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronFirewallGroup.

        网络ACL防火墙是否受管理员控制。

        :return: The admin_state_up of this NeutronFirewallGroup.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronFirewallGroup.

        网络ACL防火墙是否受管理员控制。

        :param admin_state_up: The admin_state_up of this NeutronFirewallGroup.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this NeutronFirewallGroup.

        网络ACL防火墙组描述。

        :return: The description of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronFirewallGroup.

        网络ACL防火墙组描述。

        :param description: The description of this NeutronFirewallGroup.
        :type: str
        """
        self._description = description

    @property
    def egress_firewall_policy_id(self):
        """Gets the egress_firewall_policy_id of this NeutronFirewallGroup.

        出方向网络ACL防火墙策略。

        :return: The egress_firewall_policy_id of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._egress_firewall_policy_id

    @egress_firewall_policy_id.setter
    def egress_firewall_policy_id(self, egress_firewall_policy_id):
        """Sets the egress_firewall_policy_id of this NeutronFirewallGroup.

        出方向网络ACL防火墙策略。

        :param egress_firewall_policy_id: The egress_firewall_policy_id of this NeutronFirewallGroup.
        :type: str
        """
        self._egress_firewall_policy_id = egress_firewall_policy_id

    @property
    def id(self):
        """Gets the id of this NeutronFirewallGroup.

        网络ACL防火墙组的ID

        :return: The id of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronFirewallGroup.

        网络ACL防火墙组的ID

        :param id: The id of this NeutronFirewallGroup.
        :type: str
        """
        self._id = id

    @property
    def ingress_firewall_policy_id(self):
        """Gets the ingress_firewall_policy_id of this NeutronFirewallGroup.

        入方向网络ACL防火墙策略ID。

        :return: The ingress_firewall_policy_id of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._ingress_firewall_policy_id

    @ingress_firewall_policy_id.setter
    def ingress_firewall_policy_id(self, ingress_firewall_policy_id):
        """Sets the ingress_firewall_policy_id of this NeutronFirewallGroup.

        入方向网络ACL防火墙策略ID。

        :param ingress_firewall_policy_id: The ingress_firewall_policy_id of this NeutronFirewallGroup.
        :type: str
        """
        self._ingress_firewall_policy_id = ingress_firewall_policy_id

    @property
    def name(self):
        """Gets the name of this NeutronFirewallGroup.

        网络ACL防火墙组名称。

        :return: The name of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronFirewallGroup.

        网络ACL防火墙组名称。

        :param name: The name of this NeutronFirewallGroup.
        :type: str
        """
        self._name = name

    @property
    def ports(self):
        """Gets the ports of this NeutronFirewallGroup.

        网络ACL防火墙组绑定的端口列表。

        :return: The ports of this NeutronFirewallGroup.
        :rtype: list[str]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this NeutronFirewallGroup.

        网络ACL防火墙组绑定的端口列表。

        :param ports: The ports of this NeutronFirewallGroup.
        :type: list[str]
        """
        self._ports = ports

    @property
    def public(self):
        """Gets the public of this NeutronFirewallGroup.

        是否支持跨租户共享。

        :return: The public of this NeutronFirewallGroup.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this NeutronFirewallGroup.

        是否支持跨租户共享。

        :param public: The public of this NeutronFirewallGroup.
        :type: bool
        """
        self._public = public

    @property
    def status(self):
        """Gets the status of this NeutronFirewallGroup.

        网络ACL防火墙策略的状态。

        :return: The status of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NeutronFirewallGroup.

        网络ACL防火墙策略的状态。

        :param status: The status of this NeutronFirewallGroup.
        :type: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronFirewallGroup.

        项目ID

        :return: The tenant_id of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronFirewallGroup.

        项目ID

        :param tenant_id: The tenant_id of this NeutronFirewallGroup.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this NeutronFirewallGroup.

        项目ID

        :return: The project_id of this NeutronFirewallGroup.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronFirewallGroup.

        项目ID

        :param project_id: The project_id of this NeutronFirewallGroup.
        :type: str
        """
        self._project_id = project_id

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
        if not isinstance(other, NeutronFirewallGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
