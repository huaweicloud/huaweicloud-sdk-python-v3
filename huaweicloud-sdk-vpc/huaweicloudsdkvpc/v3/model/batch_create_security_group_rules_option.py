# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateSecurityGroupRulesOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'direction': 'str',
        'ethertype': 'str',
        'protocol': 'str',
        'multiport': 'str',
        'remote_ip_prefix': 'str',
        'remote_group_id': 'str',
        'remote_address_group_id': 'str',
        'action': 'str',
        'priority': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'direction': 'direction',
        'ethertype': 'ethertype',
        'protocol': 'protocol',
        'multiport': 'multiport',
        'remote_ip_prefix': 'remote_ip_prefix',
        'remote_group_id': 'remote_group_id',
        'remote_address_group_id': 'remote_address_group_id',
        'action': 'action',
        'priority': 'priority',
        'enabled': 'enabled'
    }

    def __init__(self, description=None, direction=None, ethertype=None, protocol=None, multiport=None, remote_ip_prefix=None, remote_group_id=None, remote_address_group_id=None, action=None, priority=None, enabled=None):
        r"""BatchCreateSecurityGroupRulesOption

        The model defined in huaweicloud sdk

        :param description: 功能说明：安全组的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param direction: 功能说明：安全组规则的出入控制方向 取值范围：ingress 表示入方向；egress 表示出方向
        :type direction: str
        :param ethertype: 功能说明：IP地址协议类型 取值范围：IPv4，IPv6 约束：不填默认值为IPv4
        :type ethertype: str
        :param protocol: 功能说明：协议类型 取值范围：icmp、tcp、udp、icmpv6或IP协议号(0~255) 约束：为空表示支持所有协议。协议为icmpv6时，网络类型应该为IPv6；协议为icmp时，网络类型应该为IPv4
        :type protocol: str
        :param multiport: 功能说明：端口取值范围 取值范围：支持单端口(80)，连续端口(1-30)以及不连续端口(22,3389,80) 约束：端口值的范围1~65535
        :type multiport: str
        :param remote_ip_prefix: 功能说明：远端IP地址，当direction是egress时为虚拟机访问端的地址，当direction是ingress时为访问虚拟机的地址 取值范围：IP地址，或者cidr格式 约束：与remote_group_id、remote_address_group_id互斥
        :type remote_ip_prefix: str
        :param remote_group_id: 功能说明：远端安全组ID，表示该安全组内的流量允许或拒绝 取值范围：租户下存在的安全组ID 约束：与remote_ip_prefix，remote_address_group_id功能互斥
        :type remote_group_id: str
        :param remote_address_group_id: 功能说明：远端地址组ID 取值范围：租户下存在的地址组ID 约束：与remote_ip_prefix，remote_group_id功能互斥
        :type remote_address_group_id: str
        :param action: 功能说明：安全组规则生效策略 取值范围：allow 允许，deny 拒绝 约束：默认值为allow 
        :type action: str
        :param priority: 功能说明：规则在安全组中的优先级 取值范围：1~100，1代表最高优先级 约束：默认值为1
        :type priority: str
        :param enabled: 功能说明：是否启用安全组规则。 取值范围：true, false。 约束：默认值为true。
        :type enabled: bool
        """
        
        

        self._description = None
        self._direction = None
        self._ethertype = None
        self._protocol = None
        self._multiport = None
        self._remote_ip_prefix = None
        self._remote_group_id = None
        self._remote_address_group_id = None
        self._action = None
        self._priority = None
        self._enabled = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.direction = direction
        if ethertype is not None:
            self.ethertype = ethertype
        if protocol is not None:
            self.protocol = protocol
        if multiport is not None:
            self.multiport = multiport
        if remote_ip_prefix is not None:
            self.remote_ip_prefix = remote_ip_prefix
        if remote_group_id is not None:
            self.remote_group_id = remote_group_id
        if remote_address_group_id is not None:
            self.remote_address_group_id = remote_address_group_id
        if action is not None:
            self.action = action
        if priority is not None:
            self.priority = priority
        if enabled is not None:
            self.enabled = enabled

    @property
    def description(self):
        r"""Gets the description of this BatchCreateSecurityGroupRulesOption.

        功能说明：安全组的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this BatchCreateSecurityGroupRulesOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchCreateSecurityGroupRulesOption.

        功能说明：安全组的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this BatchCreateSecurityGroupRulesOption.
        :type description: str
        """
        self._description = description

    @property
    def direction(self):
        r"""Gets the direction of this BatchCreateSecurityGroupRulesOption.

        功能说明：安全组规则的出入控制方向 取值范围：ingress 表示入方向；egress 表示出方向

        :return: The direction of this BatchCreateSecurityGroupRulesOption.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this BatchCreateSecurityGroupRulesOption.

        功能说明：安全组规则的出入控制方向 取值范围：ingress 表示入方向；egress 表示出方向

        :param direction: The direction of this BatchCreateSecurityGroupRulesOption.
        :type direction: str
        """
        self._direction = direction

    @property
    def ethertype(self):
        r"""Gets the ethertype of this BatchCreateSecurityGroupRulesOption.

        功能说明：IP地址协议类型 取值范围：IPv4，IPv6 约束：不填默认值为IPv4

        :return: The ethertype of this BatchCreateSecurityGroupRulesOption.
        :rtype: str
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, ethertype):
        r"""Sets the ethertype of this BatchCreateSecurityGroupRulesOption.

        功能说明：IP地址协议类型 取值范围：IPv4，IPv6 约束：不填默认值为IPv4

        :param ethertype: The ethertype of this BatchCreateSecurityGroupRulesOption.
        :type ethertype: str
        """
        self._ethertype = ethertype

    @property
    def protocol(self):
        r"""Gets the protocol of this BatchCreateSecurityGroupRulesOption.

        功能说明：协议类型 取值范围：icmp、tcp、udp、icmpv6或IP协议号(0~255) 约束：为空表示支持所有协议。协议为icmpv6时，网络类型应该为IPv6；协议为icmp时，网络类型应该为IPv4

        :return: The protocol of this BatchCreateSecurityGroupRulesOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this BatchCreateSecurityGroupRulesOption.

        功能说明：协议类型 取值范围：icmp、tcp、udp、icmpv6或IP协议号(0~255) 约束：为空表示支持所有协议。协议为icmpv6时，网络类型应该为IPv6；协议为icmp时，网络类型应该为IPv4

        :param protocol: The protocol of this BatchCreateSecurityGroupRulesOption.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def multiport(self):
        r"""Gets the multiport of this BatchCreateSecurityGroupRulesOption.

        功能说明：端口取值范围 取值范围：支持单端口(80)，连续端口(1-30)以及不连续端口(22,3389,80) 约束：端口值的范围1~65535

        :return: The multiport of this BatchCreateSecurityGroupRulesOption.
        :rtype: str
        """
        return self._multiport

    @multiport.setter
    def multiport(self, multiport):
        r"""Sets the multiport of this BatchCreateSecurityGroupRulesOption.

        功能说明：端口取值范围 取值范围：支持单端口(80)，连续端口(1-30)以及不连续端口(22,3389,80) 约束：端口值的范围1~65535

        :param multiport: The multiport of this BatchCreateSecurityGroupRulesOption.
        :type multiport: str
        """
        self._multiport = multiport

    @property
    def remote_ip_prefix(self):
        r"""Gets the remote_ip_prefix of this BatchCreateSecurityGroupRulesOption.

        功能说明：远端IP地址，当direction是egress时为虚拟机访问端的地址，当direction是ingress时为访问虚拟机的地址 取值范围：IP地址，或者cidr格式 约束：与remote_group_id、remote_address_group_id互斥

        :return: The remote_ip_prefix of this BatchCreateSecurityGroupRulesOption.
        :rtype: str
        """
        return self._remote_ip_prefix

    @remote_ip_prefix.setter
    def remote_ip_prefix(self, remote_ip_prefix):
        r"""Sets the remote_ip_prefix of this BatchCreateSecurityGroupRulesOption.

        功能说明：远端IP地址，当direction是egress时为虚拟机访问端的地址，当direction是ingress时为访问虚拟机的地址 取值范围：IP地址，或者cidr格式 约束：与remote_group_id、remote_address_group_id互斥

        :param remote_ip_prefix: The remote_ip_prefix of this BatchCreateSecurityGroupRulesOption.
        :type remote_ip_prefix: str
        """
        self._remote_ip_prefix = remote_ip_prefix

    @property
    def remote_group_id(self):
        r"""Gets the remote_group_id of this BatchCreateSecurityGroupRulesOption.

        功能说明：远端安全组ID，表示该安全组内的流量允许或拒绝 取值范围：租户下存在的安全组ID 约束：与remote_ip_prefix，remote_address_group_id功能互斥

        :return: The remote_group_id of this BatchCreateSecurityGroupRulesOption.
        :rtype: str
        """
        return self._remote_group_id

    @remote_group_id.setter
    def remote_group_id(self, remote_group_id):
        r"""Sets the remote_group_id of this BatchCreateSecurityGroupRulesOption.

        功能说明：远端安全组ID，表示该安全组内的流量允许或拒绝 取值范围：租户下存在的安全组ID 约束：与remote_ip_prefix，remote_address_group_id功能互斥

        :param remote_group_id: The remote_group_id of this BatchCreateSecurityGroupRulesOption.
        :type remote_group_id: str
        """
        self._remote_group_id = remote_group_id

    @property
    def remote_address_group_id(self):
        r"""Gets the remote_address_group_id of this BatchCreateSecurityGroupRulesOption.

        功能说明：远端地址组ID 取值范围：租户下存在的地址组ID 约束：与remote_ip_prefix，remote_group_id功能互斥

        :return: The remote_address_group_id of this BatchCreateSecurityGroupRulesOption.
        :rtype: str
        """
        return self._remote_address_group_id

    @remote_address_group_id.setter
    def remote_address_group_id(self, remote_address_group_id):
        r"""Sets the remote_address_group_id of this BatchCreateSecurityGroupRulesOption.

        功能说明：远端地址组ID 取值范围：租户下存在的地址组ID 约束：与remote_ip_prefix，remote_group_id功能互斥

        :param remote_address_group_id: The remote_address_group_id of this BatchCreateSecurityGroupRulesOption.
        :type remote_address_group_id: str
        """
        self._remote_address_group_id = remote_address_group_id

    @property
    def action(self):
        r"""Gets the action of this BatchCreateSecurityGroupRulesOption.

        功能说明：安全组规则生效策略 取值范围：allow 允许，deny 拒绝 约束：默认值为allow 

        :return: The action of this BatchCreateSecurityGroupRulesOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchCreateSecurityGroupRulesOption.

        功能说明：安全组规则生效策略 取值范围：allow 允许，deny 拒绝 约束：默认值为allow 

        :param action: The action of this BatchCreateSecurityGroupRulesOption.
        :type action: str
        """
        self._action = action

    @property
    def priority(self):
        r"""Gets the priority of this BatchCreateSecurityGroupRulesOption.

        功能说明：规则在安全组中的优先级 取值范围：1~100，1代表最高优先级 约束：默认值为1

        :return: The priority of this BatchCreateSecurityGroupRulesOption.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this BatchCreateSecurityGroupRulesOption.

        功能说明：规则在安全组中的优先级 取值范围：1~100，1代表最高优先级 约束：默认值为1

        :param priority: The priority of this BatchCreateSecurityGroupRulesOption.
        :type priority: str
        """
        self._priority = priority

    @property
    def enabled(self):
        r"""Gets the enabled of this BatchCreateSecurityGroupRulesOption.

        功能说明：是否启用安全组规则。 取值范围：true, false。 约束：默认值为true。

        :return: The enabled of this BatchCreateSecurityGroupRulesOption.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this BatchCreateSecurityGroupRulesOption.

        功能说明：是否启用安全组规则。 取值范围：true, false。 约束：默认值为true。

        :param enabled: The enabled of this BatchCreateSecurityGroupRulesOption.
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
        if not isinstance(other, BatchCreateSecurityGroupRulesOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
