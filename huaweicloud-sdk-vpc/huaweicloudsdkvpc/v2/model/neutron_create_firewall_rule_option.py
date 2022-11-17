# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronCreateFirewallRuleOption:

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
        'protocol': 'str',
        'action': 'str',
        'ip_version': 'int',
        'destination_ip_address': 'str',
        'destination_port': 'str',
        'source_ip_address': 'str',
        'source_port': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'protocol': 'protocol',
        'action': 'action',
        'ip_version': 'ip_version',
        'destination_ip_address': 'destination_ip_address',
        'destination_port': 'destination_port',
        'source_ip_address': 'source_ip_address',
        'source_port': 'source_port',
        'enabled': 'enabled'
    }

    def __init__(self, name=None, description=None, protocol=None, action=None, ip_version=None, destination_ip_address=None, destination_port=None, source_ip_address=None, source_port=None, enabled=None):
        """NeutronCreateFirewallRuleOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：网络ACL规则名称 取值范围：0-255个字符
        :type name: str
        :param description: 功能说明：网络ACL规则描述 取值范围：0-255个字符
        :type description: str
        :param protocol: 功能说明：IP协议 取值范围：支持TCP,UDP,ICMP, ICMPV6或者ip协议号（0-255）
        :type protocol: str
        :param action: 功能说明：对通过网络ACL的流量执行的操作 取值范围：DENY（拒绝）/ALLOW（允许）
        :type action: str
        :param ip_version: 功能说明：IP协议版本
        :type ip_version: int
        :param destination_ip_address: 功能说明：目的地址或者CIDR
        :type destination_ip_address: str
        :param destination_port: 功能说明：目的端口号或者一段端口范围
        :type destination_port: str
        :param source_ip_address: 功能说明：源地址或者CIDR
        :type source_ip_address: str
        :param source_port: 功能说明：源端口号或者一段端口范围
        :type source_port: str
        :param enabled: 功能说明：是否使能网络ACL防火墙规则。
        :type enabled: bool
        """
        
        

        self._name = None
        self._description = None
        self._protocol = None
        self._action = None
        self._ip_version = None
        self._destination_ip_address = None
        self._destination_port = None
        self._source_ip_address = None
        self._source_port = None
        self._enabled = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if protocol is not None:
            self.protocol = protocol
        if action is not None:
            self.action = action
        if ip_version is not None:
            self.ip_version = ip_version
        if destination_ip_address is not None:
            self.destination_ip_address = destination_ip_address
        if destination_port is not None:
            self.destination_port = destination_port
        if source_ip_address is not None:
            self.source_ip_address = source_ip_address
        if source_port is not None:
            self.source_port = source_port
        if enabled is not None:
            self.enabled = enabled

    @property
    def name(self):
        """Gets the name of this NeutronCreateFirewallRuleOption.

        功能说明：网络ACL规则名称 取值范围：0-255个字符

        :return: The name of this NeutronCreateFirewallRuleOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronCreateFirewallRuleOption.

        功能说明：网络ACL规则名称 取值范围：0-255个字符

        :param name: The name of this NeutronCreateFirewallRuleOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NeutronCreateFirewallRuleOption.

        功能说明：网络ACL规则描述 取值范围：0-255个字符

        :return: The description of this NeutronCreateFirewallRuleOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronCreateFirewallRuleOption.

        功能说明：网络ACL规则描述 取值范围：0-255个字符

        :param description: The description of this NeutronCreateFirewallRuleOption.
        :type description: str
        """
        self._description = description

    @property
    def protocol(self):
        """Gets the protocol of this NeutronCreateFirewallRuleOption.

        功能说明：IP协议 取值范围：支持TCP,UDP,ICMP, ICMPV6或者ip协议号（0-255）

        :return: The protocol of this NeutronCreateFirewallRuleOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NeutronCreateFirewallRuleOption.

        功能说明：IP协议 取值范围：支持TCP,UDP,ICMP, ICMPV6或者ip协议号（0-255）

        :param protocol: The protocol of this NeutronCreateFirewallRuleOption.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def action(self):
        """Gets the action of this NeutronCreateFirewallRuleOption.

        功能说明：对通过网络ACL的流量执行的操作 取值范围：DENY（拒绝）/ALLOW（允许）

        :return: The action of this NeutronCreateFirewallRuleOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NeutronCreateFirewallRuleOption.

        功能说明：对通过网络ACL的流量执行的操作 取值范围：DENY（拒绝）/ALLOW（允许）

        :param action: The action of this NeutronCreateFirewallRuleOption.
        :type action: str
        """
        self._action = action

    @property
    def ip_version(self):
        """Gets the ip_version of this NeutronCreateFirewallRuleOption.

        功能说明：IP协议版本

        :return: The ip_version of this NeutronCreateFirewallRuleOption.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this NeutronCreateFirewallRuleOption.

        功能说明：IP协议版本

        :param ip_version: The ip_version of this NeutronCreateFirewallRuleOption.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def destination_ip_address(self):
        """Gets the destination_ip_address of this NeutronCreateFirewallRuleOption.

        功能说明：目的地址或者CIDR

        :return: The destination_ip_address of this NeutronCreateFirewallRuleOption.
        :rtype: str
        """
        return self._destination_ip_address

    @destination_ip_address.setter
    def destination_ip_address(self, destination_ip_address):
        """Sets the destination_ip_address of this NeutronCreateFirewallRuleOption.

        功能说明：目的地址或者CIDR

        :param destination_ip_address: The destination_ip_address of this NeutronCreateFirewallRuleOption.
        :type destination_ip_address: str
        """
        self._destination_ip_address = destination_ip_address

    @property
    def destination_port(self):
        """Gets the destination_port of this NeutronCreateFirewallRuleOption.

        功能说明：目的端口号或者一段端口范围

        :return: The destination_port of this NeutronCreateFirewallRuleOption.
        :rtype: str
        """
        return self._destination_port

    @destination_port.setter
    def destination_port(self, destination_port):
        """Sets the destination_port of this NeutronCreateFirewallRuleOption.

        功能说明：目的端口号或者一段端口范围

        :param destination_port: The destination_port of this NeutronCreateFirewallRuleOption.
        :type destination_port: str
        """
        self._destination_port = destination_port

    @property
    def source_ip_address(self):
        """Gets the source_ip_address of this NeutronCreateFirewallRuleOption.

        功能说明：源地址或者CIDR

        :return: The source_ip_address of this NeutronCreateFirewallRuleOption.
        :rtype: str
        """
        return self._source_ip_address

    @source_ip_address.setter
    def source_ip_address(self, source_ip_address):
        """Sets the source_ip_address of this NeutronCreateFirewallRuleOption.

        功能说明：源地址或者CIDR

        :param source_ip_address: The source_ip_address of this NeutronCreateFirewallRuleOption.
        :type source_ip_address: str
        """
        self._source_ip_address = source_ip_address

    @property
    def source_port(self):
        """Gets the source_port of this NeutronCreateFirewallRuleOption.

        功能说明：源端口号或者一段端口范围

        :return: The source_port of this NeutronCreateFirewallRuleOption.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        """Sets the source_port of this NeutronCreateFirewallRuleOption.

        功能说明：源端口号或者一段端口范围

        :param source_port: The source_port of this NeutronCreateFirewallRuleOption.
        :type source_port: str
        """
        self._source_port = source_port

    @property
    def enabled(self):
        """Gets the enabled of this NeutronCreateFirewallRuleOption.

        功能说明：是否使能网络ACL防火墙规则。

        :return: The enabled of this NeutronCreateFirewallRuleOption.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NeutronCreateFirewallRuleOption.

        功能说明：是否使能网络ACL防火墙规则。

        :param enabled: The enabled of this NeutronCreateFirewallRuleOption.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, NeutronCreateFirewallRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
