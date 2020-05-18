# coding: utf-8

import pprint
import re

import six


class NeutronFirewallRule(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'action': 'str',
        'description': 'str',
        'destination_ip_address': 'str',
        'destination_port': 'str',
        'enabled': 'bool',
        'id': 'str',
        'ip_version': 'int',
        'name': 'str',
        'protocol': 'str',
        'public': 'bool',
        'source_ip_address': 'str',
        'source_port': 'str',
        'tenant_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'description': 'description',
        'destination_ip_address': 'destination_ip_address',
        'destination_port': 'destination_port',
        'enabled': 'enabled',
        'id': 'id',
        'ip_version': 'ip_version',
        'name': 'name',
        'protocol': 'protocol',
        'public': 'public',
        'source_ip_address': 'source_ip_address',
        'source_port': 'source_port',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id'
    }

    def __init__(self, action=None, description=None, destination_ip_address=None, destination_port=None, enabled=None, id=None, ip_version=None, name=None, protocol=None, public=None, source_ip_address=None, source_port=None, tenant_id=None, project_id=None):  # noqa: E501
        """NeutronFirewallRule - a model defined in huaweicloud sdk"""

        self._action = None
        self._description = None
        self._destination_ip_address = None
        self._destination_port = None
        self._enabled = None
        self._id = None
        self._ip_version = None
        self._name = None
        self._protocol = None
        self._public = None
        self._source_ip_address = None
        self._source_port = None
        self._tenant_id = None
        self._project_id = None
        self.discriminator = None

        self.action = action
        self.description = description
        self.destination_ip_address = destination_ip_address
        self.destination_port = destination_port
        self.enabled = enabled
        self.id = id
        self.ip_version = ip_version
        self.name = name
        self.protocol = protocol
        self.public = public
        self.source_ip_address = source_ip_address
        self.source_port = source_port
        self.tenant_id = tenant_id
        self.project_id = project_id

    @property
    def action(self):
        """Gets the action of this NeutronFirewallRule.

        对通过网络ACL防火墙的流量执行的操作。

        :return: The action of this NeutronFirewallRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NeutronFirewallRule.

        对通过网络ACL防火墙的流量执行的操作。

        :param action: The action of this NeutronFirewallRule.
        :type: str
        """
        self._action = action

    @property
    def description(self):
        """Gets the description of this NeutronFirewallRule.

        网络ACL防火墙规则描述。

        :return: The description of this NeutronFirewallRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronFirewallRule.

        网络ACL防火墙规则描述。

        :param description: The description of this NeutronFirewallRule.
        :type: str
        """
        self._description = description

    @property
    def destination_ip_address(self):
        """Gets the destination_ip_address of this NeutronFirewallRule.

        目的地址或者CIDR。

        :return: The destination_ip_address of this NeutronFirewallRule.
        :rtype: str
        """
        return self._destination_ip_address

    @destination_ip_address.setter
    def destination_ip_address(self, destination_ip_address):
        """Sets the destination_ip_address of this NeutronFirewallRule.

        目的地址或者CIDR。

        :param destination_ip_address: The destination_ip_address of this NeutronFirewallRule.
        :type: str
        """
        self._destination_ip_address = destination_ip_address

    @property
    def destination_port(self):
        """Gets the destination_port of this NeutronFirewallRule.

        目的端口号或者一段端口范围。

        :return: The destination_port of this NeutronFirewallRule.
        :rtype: str
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, destination_port):
        """Sets the destination_port of this NeutronFirewallRule.

        目的端口号或者一段端口范围。

        :param destination_port: The destination_port of this NeutronFirewallRule.
        :type: str
        """
        self._destination_port = destination_port

    @property
    def enabled(self):
        """Gets the enabled of this NeutronFirewallRule.

        是否使能网络ACL防火墙规则。

        :return: The enabled of this NeutronFirewallRule.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NeutronFirewallRule.

        是否使能网络ACL防火墙规则。

        :param enabled: The enabled of this NeutronFirewallRule.
        :type: bool
        """
        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this NeutronFirewallRule.

        网络ACL防火墙规则的uuid标识。

        :return: The id of this NeutronFirewallRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronFirewallRule.

        网络ACL防火墙规则的uuid标识。

        :param id: The id of this NeutronFirewallRule.
        :type: str
        """
        self._id = id

    @property
    def ip_version(self):
        """Gets the ip_version of this NeutronFirewallRule.

        IP协议版本。

        :return: The ip_version of this NeutronFirewallRule.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this NeutronFirewallRule.

        IP协议版本。

        :param ip_version: The ip_version of this NeutronFirewallRule.
        :type: int
        """
        self._ip_version = ip_version

    @property
    def name(self):
        """Gets the name of this NeutronFirewallRule.

        网络ACL防火墙规则名称。

        :return: The name of this NeutronFirewallRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronFirewallRule.

        网络ACL防火墙规则名称。

        :param name: The name of this NeutronFirewallRule.
        :type: str
        """
        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this NeutronFirewallRule.

        IP协议，支持TCP,UDP,ICMP, ICMPV6或者IP协议号（0-255）

        :return: The protocol of this NeutronFirewallRule.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NeutronFirewallRule.

        IP协议，支持TCP,UDP,ICMP, ICMPV6或者IP协议号（0-255）

        :param protocol: The protocol of this NeutronFirewallRule.
        :type: str
        """
        self._protocol = protocol

    @property
    def public(self):
        """Gets the public of this NeutronFirewallRule.

        是否支持跨租户共享。

        :return: The public of this NeutronFirewallRule.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this NeutronFirewallRule.

        是否支持跨租户共享。

        :param public: The public of this NeutronFirewallRule.
        :type: bool
        """
        self._public = public

    @property
    def source_ip_address(self):
        """Gets the source_ip_address of this NeutronFirewallRule.

        源地址或者CIDR。

        :return: The source_ip_address of this NeutronFirewallRule.
        :rtype: str
        """
        return self._source_ip_address

    @source_ip_address.setter
    def source_ip_address(self, source_ip_address):
        """Sets the source_ip_address of this NeutronFirewallRule.

        源地址或者CIDR。

        :param source_ip_address: The source_ip_address of this NeutronFirewallRule.
        :type: str
        """
        self._source_ip_address = source_ip_address

    @property
    def source_port(self):
        """Gets the source_port of this NeutronFirewallRule.

        源端口号或者一段端口范围。

        :return: The source_port of this NeutronFirewallRule.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        """Sets the source_port of this NeutronFirewallRule.

        源端口号或者一段端口范围。

        :param source_port: The source_port of this NeutronFirewallRule.
        :type: str
        """
        self._source_port = source_port

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronFirewallRule.

        项目ID

        :return: The tenant_id of this NeutronFirewallRule.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronFirewallRule.

        项目ID

        :param tenant_id: The tenant_id of this NeutronFirewallRule.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this NeutronFirewallRule.

        项目ID

        :return: The project_id of this NeutronFirewallRule.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronFirewallRule.

        项目ID

        :param project_id: The project_id of this NeutronFirewallRule.
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
        if not isinstance(other, NeutronFirewallRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
