# coding: utf-8

import pprint
import re

import six





class CreateSecurityGroupRuleOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'security_group_id': 'str',
        'description': 'str',
        'direction': 'str',
        'ethertype': 'str',
        'protocol': 'str',
        'port_range_min': 'int',
        'port_range_max': 'int',
        'remote_ip_prefix': 'str',
        'remote_group_id': 'str'
    }

    attribute_map = {
        'security_group_id': 'security_group_id',
        'description': 'description',
        'direction': 'direction',
        'ethertype': 'ethertype',
        'protocol': 'protocol',
        'port_range_min': 'port_range_min',
        'port_range_max': 'port_range_max',
        'remote_ip_prefix': 'remote_ip_prefix',
        'remote_group_id': 'remote_group_id'
    }

    def __init__(self, security_group_id=None, description=None, direction=None, ethertype=None, protocol=None, port_range_min=None, port_range_max=None, remote_ip_prefix=None, remote_group_id=None):
        """CreateSecurityGroupRuleOption - a model defined in huaweicloud sdk"""
        
        

        self._security_group_id = None
        self._description = None
        self._direction = None
        self._ethertype = None
        self._protocol = None
        self._port_range_min = None
        self._port_range_max = None
        self._remote_ip_prefix = None
        self._remote_group_id = None
        self.discriminator = None

        self.security_group_id = security_group_id
        if description is not None:
            self.description = description
        self.direction = direction
        if ethertype is not None:
            self.ethertype = ethertype
        if protocol is not None:
            self.protocol = protocol
        if port_range_min is not None:
            self.port_range_min = port_range_min
        if port_range_max is not None:
            self.port_range_max = port_range_max
        if remote_ip_prefix is not None:
            self.remote_ip_prefix = remote_ip_prefix
        if remote_group_id is not None:
            self.remote_group_id = remote_group_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateSecurityGroupRuleOption.

        安全组ID

        :return: The security_group_id of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateSecurityGroupRuleOption.

        安全组ID

        :param security_group_id: The security_group_id of this CreateSecurityGroupRuleOption.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def description(self):
        """Gets the description of this CreateSecurityGroupRuleOption.

        功能说明：安全组规则描述 取值范围：0-255个字符，支持数字、字母、中文字符

        :return: The description of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSecurityGroupRuleOption.

        功能说明：安全组规则描述 取值范围：0-255个字符，支持数字、字母、中文字符

        :param description: The description of this CreateSecurityGroupRuleOption.
        :type: str
        """
        self._description = description

    @property
    def direction(self):
        """Gets the direction of this CreateSecurityGroupRuleOption.

        功能说明：出入控制方向 取值范围： - egress：出方向 - ingress：入方向

        :return: The direction of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this CreateSecurityGroupRuleOption.

        功能说明：出入控制方向 取值范围： - egress：出方向 - ingress：入方向

        :param direction: The direction of this CreateSecurityGroupRuleOption.
        :type: str
        """
        self._direction = direction

    @property
    def ethertype(self):
        """Gets the ethertype of this CreateSecurityGroupRuleOption.

        功能说明：IP地址协议类型 取值范围：IPv4,IPv6 约束：默认值为IPv4

        :return: The ethertype of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, ethertype):
        """Sets the ethertype of this CreateSecurityGroupRuleOption.

        功能说明：IP地址协议类型 取值范围：IPv4,IPv6 约束：默认值为IPv4

        :param ethertype: The ethertype of this CreateSecurityGroupRuleOption.
        :type: str
        """
        self._ethertype = ethertype

    @property
    def protocol(self):
        """Gets the protocol of this CreateSecurityGroupRuleOption.

        功能说明：协议类型 取值范围：tcp、udp、icmp或IP协议编号（0~255） 约束：为空表示支持所有协议

        :return: The protocol of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateSecurityGroupRuleOption.

        功能说明：协议类型 取值范围：tcp、udp、icmp或IP协议编号（0~255） 约束：为空表示支持所有协议

        :param protocol: The protocol of this CreateSecurityGroupRuleOption.
        :type: str
        """
        self._protocol = protocol

    @property
    def port_range_min(self):
        """Gets the port_range_min of this CreateSecurityGroupRuleOption.

        功能说明：起始端口值 取值范围：1~65535 约束：不能大于port_range_max的值，为空表示所有端口，如果协议是icmp类型，取值范围请参见 [安全组规则icmp协议名称对应关系表](https://support.huaweicloud.com/api-vpc/vpc_api_0009.html)

        :return: The port_range_min of this CreateSecurityGroupRuleOption.
        :rtype: int
        """
        return self._port_range_min

    @port_range_min.setter
    def port_range_min(self, port_range_min):
        """Sets the port_range_min of this CreateSecurityGroupRuleOption.

        功能说明：起始端口值 取值范围：1~65535 约束：不能大于port_range_max的值，为空表示所有端口，如果协议是icmp类型，取值范围请参见 [安全组规则icmp协议名称对应关系表](https://support.huaweicloud.com/api-vpc/vpc_api_0009.html)

        :param port_range_min: The port_range_min of this CreateSecurityGroupRuleOption.
        :type: int
        """
        self._port_range_min = port_range_min

    @property
    def port_range_max(self):
        """Gets the port_range_max of this CreateSecurityGroupRuleOption.

        功能说明：结束端口值 取值范围：1~65535 约束：协议不为icmp时，取值不能小于port_range_min的值，为空表示所有端口，如果协议是icmp类型，取值范围请参见 [安全组规则icmp协议名称对应关系表](https://support.huaweicloud.com/api-vpc/vpc_api_0009.html)

        :return: The port_range_max of this CreateSecurityGroupRuleOption.
        :rtype: int
        """
        return self._port_range_max

    @port_range_max.setter
    def port_range_max(self, port_range_max):
        """Sets the port_range_max of this CreateSecurityGroupRuleOption.

        功能说明：结束端口值 取值范围：1~65535 约束：协议不为icmp时，取值不能小于port_range_min的值，为空表示所有端口，如果协议是icmp类型，取值范围请参见 [安全组规则icmp协议名称对应关系表](https://support.huaweicloud.com/api-vpc/vpc_api_0009.html)

        :param port_range_max: The port_range_max of this CreateSecurityGroupRuleOption.
        :type: int
        """
        self._port_range_max = port_range_max

    @property
    def remote_ip_prefix(self):
        """Gets the remote_ip_prefix of this CreateSecurityGroupRuleOption.

        功能说明：远端IP地址，当direction是egress时为虚拟机访问端的地址，当direction是ingress时为访问虚拟机的地址 取值范围：IP地址，或者cidr格式 约束：和remote_group_id互斥

        :return: The remote_ip_prefix of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._remote_ip_prefix

    @remote_ip_prefix.setter
    def remote_ip_prefix(self, remote_ip_prefix):
        """Sets the remote_ip_prefix of this CreateSecurityGroupRuleOption.

        功能说明：远端IP地址，当direction是egress时为虚拟机访问端的地址，当direction是ingress时为访问虚拟机的地址 取值范围：IP地址，或者cidr格式 约束：和remote_group_id互斥

        :param remote_ip_prefix: The remote_ip_prefix of this CreateSecurityGroupRuleOption.
        :type: str
        """
        self._remote_ip_prefix = remote_ip_prefix

    @property
    def remote_group_id(self):
        """Gets the remote_group_id of this CreateSecurityGroupRuleOption.

        功能说明：对端安全组ID 约束：和remote_ip_prefix互斥

        :return: The remote_group_id of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._remote_group_id

    @remote_group_id.setter
    def remote_group_id(self, remote_group_id):
        """Sets the remote_group_id of this CreateSecurityGroupRuleOption.

        功能说明：对端安全组ID 约束：和remote_ip_prefix互斥

        :param remote_group_id: The remote_group_id of this CreateSecurityGroupRuleOption.
        :type: str
        """
        self._remote_group_id = remote_group_id

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
        if not isinstance(other, CreateSecurityGroupRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
