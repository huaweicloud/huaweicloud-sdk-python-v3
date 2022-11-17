# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronUpdateFirewallRuleOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'description': 'str',
        'destination_ip_address': 'str',
        'destination_port': 'str',
        'enabled': 'bool',
        'ip_version': 'int',
        'name': 'str',
        'protocol': 'str',
        'source_ip_address': 'str',
        'source_port': 'str'
    }

    attribute_map = {
        'action': 'action',
        'description': 'description',
        'destination_ip_address': 'destination_ip_address',
        'destination_port': 'destination_port',
        'enabled': 'enabled',
        'ip_version': 'ip_version',
        'name': 'name',
        'protocol': 'protocol',
        'source_ip_address': 'source_ip_address',
        'source_port': 'source_port'
    }

    def __init__(self, action=None, description=None, destination_ip_address=None, destination_port=None, enabled=None, ip_version=None, name=None, protocol=None, source_ip_address=None, source_port=None):
        """NeutronUpdateFirewallRuleOption

        The model defined in huaweicloud sdk

        :param action: 对通过网络ACL防火墙的流量执行的操作。
        :type action: str
        :param description: 网络ACL防火墙规则描述。
        :type description: str
        :param destination_ip_address: 目的地址或者CIDR。
        :type destination_ip_address: str
        :param destination_port: 目的端口号或者一段端口范围。
        :type destination_port: str
        :param enabled: 是否使能网络ACL防火墙规则。
        :type enabled: bool
        :param ip_version: IP协议版本。
        :type ip_version: int
        :param name: 网络ACL防火墙规则名称。
        :type name: str
        :param protocol: IP协议，支持TCP,UDP,ICMP, ICMPV6或者IP协议号（0-255）
        :type protocol: str
        :param source_ip_address: 源地址或者CIDR。
        :type source_ip_address: str
        :param source_port: 源端口号或者一段端口范围。
        :type source_port: str
        """
        
        

        self._action = None
        self._description = None
        self._destination_ip_address = None
        self._destination_port = None
        self._enabled = None
        self._ip_version = None
        self._name = None
        self._protocol = None
        self._source_ip_address = None
        self._source_port = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if description is not None:
            self.description = description
        if destination_ip_address is not None:
            self.destination_ip_address = destination_ip_address
        if destination_port is not None:
            self.destination_port = destination_port
        if enabled is not None:
            self.enabled = enabled
        if ip_version is not None:
            self.ip_version = ip_version
        if name is not None:
            self.name = name
        if protocol is not None:
            self.protocol = protocol
        if source_ip_address is not None:
            self.source_ip_address = source_ip_address
        if source_port is not None:
            self.source_port = source_port

    @property
    def action(self):
        """Gets the action of this NeutronUpdateFirewallRuleOption.

        对通过网络ACL防火墙的流量执行的操作。

        :return: The action of this NeutronUpdateFirewallRuleOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NeutronUpdateFirewallRuleOption.

        对通过网络ACL防火墙的流量执行的操作。

        :param action: The action of this NeutronUpdateFirewallRuleOption.
        :type action: str
        """
        self._action = action

    @property
    def description(self):
        """Gets the description of this NeutronUpdateFirewallRuleOption.

        网络ACL防火墙规则描述。

        :return: The description of this NeutronUpdateFirewallRuleOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronUpdateFirewallRuleOption.

        网络ACL防火墙规则描述。

        :param description: The description of this NeutronUpdateFirewallRuleOption.
        :type description: str
        """
        self._description = description

    @property
    def destination_ip_address(self):
        """Gets the destination_ip_address of this NeutronUpdateFirewallRuleOption.

        目的地址或者CIDR。

        :return: The destination_ip_address of this NeutronUpdateFirewallRuleOption.
        :rtype: str
        """
        return self._destination_ip_address

    @destination_ip_address.setter
    def destination_ip_address(self, destination_ip_address):
        """Sets the destination_ip_address of this NeutronUpdateFirewallRuleOption.

        目的地址或者CIDR。

        :param destination_ip_address: The destination_ip_address of this NeutronUpdateFirewallRuleOption.
        :type destination_ip_address: str
        """
        self._destination_ip_address = destination_ip_address

    @property
    def destination_port(self):
        """Gets the destination_port of this NeutronUpdateFirewallRuleOption.

        目的端口号或者一段端口范围。

        :return: The destination_port of this NeutronUpdateFirewallRuleOption.
        :rtype: str
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, destination_port):
        """Sets the destination_port of this NeutronUpdateFirewallRuleOption.

        目的端口号或者一段端口范围。

        :param destination_port: The destination_port of this NeutronUpdateFirewallRuleOption.
        :type destination_port: str
        """
        self._destination_port = destination_port

    @property
    def enabled(self):
        """Gets the enabled of this NeutronUpdateFirewallRuleOption.

        是否使能网络ACL防火墙规则。

        :return: The enabled of this NeutronUpdateFirewallRuleOption.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NeutronUpdateFirewallRuleOption.

        是否使能网络ACL防火墙规则。

        :param enabled: The enabled of this NeutronUpdateFirewallRuleOption.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def ip_version(self):
        """Gets the ip_version of this NeutronUpdateFirewallRuleOption.

        IP协议版本。

        :return: The ip_version of this NeutronUpdateFirewallRuleOption.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this NeutronUpdateFirewallRuleOption.

        IP协议版本。

        :param ip_version: The ip_version of this NeutronUpdateFirewallRuleOption.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def name(self):
        """Gets the name of this NeutronUpdateFirewallRuleOption.

        网络ACL防火墙规则名称。

        :return: The name of this NeutronUpdateFirewallRuleOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronUpdateFirewallRuleOption.

        网络ACL防火墙规则名称。

        :param name: The name of this NeutronUpdateFirewallRuleOption.
        :type name: str
        """
        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this NeutronUpdateFirewallRuleOption.

        IP协议，支持TCP,UDP,ICMP, ICMPV6或者IP协议号（0-255）

        :return: The protocol of this NeutronUpdateFirewallRuleOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NeutronUpdateFirewallRuleOption.

        IP协议，支持TCP,UDP,ICMP, ICMPV6或者IP协议号（0-255）

        :param protocol: The protocol of this NeutronUpdateFirewallRuleOption.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def source_ip_address(self):
        """Gets the source_ip_address of this NeutronUpdateFirewallRuleOption.

        源地址或者CIDR。

        :return: The source_ip_address of this NeutronUpdateFirewallRuleOption.
        :rtype: str
        """
        return self._source_ip_address

    @source_ip_address.setter
    def source_ip_address(self, source_ip_address):
        """Sets the source_ip_address of this NeutronUpdateFirewallRuleOption.

        源地址或者CIDR。

        :param source_ip_address: The source_ip_address of this NeutronUpdateFirewallRuleOption.
        :type source_ip_address: str
        """
        self._source_ip_address = source_ip_address

    @property
    def source_port(self):
        """Gets the source_port of this NeutronUpdateFirewallRuleOption.

        源端口号或者一段端口范围。

        :return: The source_port of this NeutronUpdateFirewallRuleOption.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        """Sets the source_port of this NeutronUpdateFirewallRuleOption.

        源端口号或者一段端口范围。

        :param source_port: The source_port of this NeutronUpdateFirewallRuleOption.
        :type source_port: str
        """
        self._source_port = source_port

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
        if not isinstance(other, NeutronUpdateFirewallRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
