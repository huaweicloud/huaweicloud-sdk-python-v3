# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'description': 'str',
        'security_group_id': 'str',
        'direction': 'str',
        'ethertype': 'str',
        'protocol': 'str',
        'port_range_min': 'int',
        'port_range_max': 'int',
        'remote_group_id': 'str',
        'remote_ip_prefix': 'str',
        'action': 'str',
        'priority': 'int'
    }

    attribute_map = {
        'description': 'description',
        'security_group_id': 'security_group_id',
        'direction': 'direction',
        'ethertype': 'ethertype',
        'protocol': 'protocol',
        'port_range_min': 'port_range_min',
        'port_range_max': 'port_range_max',
        'remote_group_id': 'remote_group_id',
        'remote_ip_prefix': 'remote_ip_prefix',
        'action': 'action',
        'priority': 'priority'
    }

    def __init__(self, description=None, security_group_id=None, direction=None, ethertype=None, protocol=None, port_range_min=None, port_range_max=None, remote_group_id=None, remote_ip_prefix=None, action=None, priority=None):
        """CreateSecurityGroupRuleOption

        The model defined in huaweicloud sdk

        :param description: 安全组规则描述信息。
        :type description: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param direction: 出入控制方向。  取值范围：  - egress：出方向  - ingress：入方向
        :type direction: str
        :param ethertype: IP协议类型。  取值范围：IPv4[,IPv6](tag:hide)
        :type ethertype: str
        :param protocol: 协议类型。  取值范围：icmp、tcp、udp等  约束：为空表示支持所有协议
        :type protocol: str
        :param port_range_min: 起始端口值。  取值范围：1~65535  约束：取值不能大于port_range_max的值，为空表示所有端口。 
        :type port_range_min: int
        :param port_range_max: 结束端口值。  取值范围：1~65535  约束：取值不能小于port_range_min的值，为空表示所有端口。 
        :type port_range_max: int
        :param remote_group_id: 对端安全组id。  约束：和remote_ip_prefix互斥 
        :type remote_group_id: str
        :param remote_ip_prefix: 远端IP地址，当direction是egress时为虚拟机访问端的地址，当direction是ingress时为访问虚拟机的地址。  取值范围：IP地址，或者cidr格式  约束：和remote_group_id互斥
        :type remote_ip_prefix: str
        :param action: 安全组规则生效策略 取值范围：allow 允许，deny 拒绝  约束：默认值为allow
        :type action: str
        :param priority: 规则在安全组中的优先级  取值范围：1~100，1代表最高优先级  约束：默认值为1
        :type priority: int
        """
        
        

        self._description = None
        self._security_group_id = None
        self._direction = None
        self._ethertype = None
        self._protocol = None
        self._port_range_min = None
        self._port_range_max = None
        self._remote_group_id = None
        self._remote_ip_prefix = None
        self._action = None
        self._priority = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.security_group_id = security_group_id
        self.direction = direction
        if ethertype is not None:
            self.ethertype = ethertype
        if protocol is not None:
            self.protocol = protocol
        if port_range_min is not None:
            self.port_range_min = port_range_min
        if port_range_max is not None:
            self.port_range_max = port_range_max
        if remote_group_id is not None:
            self.remote_group_id = remote_group_id
        if remote_ip_prefix is not None:
            self.remote_ip_prefix = remote_ip_prefix
        if action is not None:
            self.action = action
        if priority is not None:
            self.priority = priority

    @property
    def description(self):
        """Gets the description of this CreateSecurityGroupRuleOption.

        安全组规则描述信息。

        :return: The description of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSecurityGroupRuleOption.

        安全组规则描述信息。

        :param description: The description of this CreateSecurityGroupRuleOption.
        :type description: str
        """
        self._description = description

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateSecurityGroupRuleOption.

        安全组ID。

        :return: The security_group_id of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateSecurityGroupRuleOption.

        安全组ID。

        :param security_group_id: The security_group_id of this CreateSecurityGroupRuleOption.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def direction(self):
        """Gets the direction of this CreateSecurityGroupRuleOption.

        出入控制方向。  取值范围：  - egress：出方向  - ingress：入方向

        :return: The direction of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this CreateSecurityGroupRuleOption.

        出入控制方向。  取值范围：  - egress：出方向  - ingress：入方向

        :param direction: The direction of this CreateSecurityGroupRuleOption.
        :type direction: str
        """
        self._direction = direction

    @property
    def ethertype(self):
        """Gets the ethertype of this CreateSecurityGroupRuleOption.

        IP协议类型。  取值范围：IPv4[,IPv6](tag:hide)

        :return: The ethertype of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, ethertype):
        """Sets the ethertype of this CreateSecurityGroupRuleOption.

        IP协议类型。  取值范围：IPv4[,IPv6](tag:hide)

        :param ethertype: The ethertype of this CreateSecurityGroupRuleOption.
        :type ethertype: str
        """
        self._ethertype = ethertype

    @property
    def protocol(self):
        """Gets the protocol of this CreateSecurityGroupRuleOption.

        协议类型。  取值范围：icmp、tcp、udp等  约束：为空表示支持所有协议

        :return: The protocol of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this CreateSecurityGroupRuleOption.

        协议类型。  取值范围：icmp、tcp、udp等  约束：为空表示支持所有协议

        :param protocol: The protocol of this CreateSecurityGroupRuleOption.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def port_range_min(self):
        """Gets the port_range_min of this CreateSecurityGroupRuleOption.

        起始端口值。  取值范围：1~65535  约束：取值不能大于port_range_max的值，为空表示所有端口。 

        :return: The port_range_min of this CreateSecurityGroupRuleOption.
        :rtype: int
        """
        return self._port_range_min

    @port_range_min.setter
    def port_range_min(self, port_range_min):
        """Sets the port_range_min of this CreateSecurityGroupRuleOption.

        起始端口值。  取值范围：1~65535  约束：取值不能大于port_range_max的值，为空表示所有端口。 

        :param port_range_min: The port_range_min of this CreateSecurityGroupRuleOption.
        :type port_range_min: int
        """
        self._port_range_min = port_range_min

    @property
    def port_range_max(self):
        """Gets the port_range_max of this CreateSecurityGroupRuleOption.

        结束端口值。  取值范围：1~65535  约束：取值不能小于port_range_min的值，为空表示所有端口。 

        :return: The port_range_max of this CreateSecurityGroupRuleOption.
        :rtype: int
        """
        return self._port_range_max

    @port_range_max.setter
    def port_range_max(self, port_range_max):
        """Sets the port_range_max of this CreateSecurityGroupRuleOption.

        结束端口值。  取值范围：1~65535  约束：取值不能小于port_range_min的值，为空表示所有端口。 

        :param port_range_max: The port_range_max of this CreateSecurityGroupRuleOption.
        :type port_range_max: int
        """
        self._port_range_max = port_range_max

    @property
    def remote_group_id(self):
        """Gets the remote_group_id of this CreateSecurityGroupRuleOption.

        对端安全组id。  约束：和remote_ip_prefix互斥 

        :return: The remote_group_id of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._remote_group_id

    @remote_group_id.setter
    def remote_group_id(self, remote_group_id):
        """Sets the remote_group_id of this CreateSecurityGroupRuleOption.

        对端安全组id。  约束：和remote_ip_prefix互斥 

        :param remote_group_id: The remote_group_id of this CreateSecurityGroupRuleOption.
        :type remote_group_id: str
        """
        self._remote_group_id = remote_group_id

    @property
    def remote_ip_prefix(self):
        """Gets the remote_ip_prefix of this CreateSecurityGroupRuleOption.

        远端IP地址，当direction是egress时为虚拟机访问端的地址，当direction是ingress时为访问虚拟机的地址。  取值范围：IP地址，或者cidr格式  约束：和remote_group_id互斥

        :return: The remote_ip_prefix of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._remote_ip_prefix

    @remote_ip_prefix.setter
    def remote_ip_prefix(self, remote_ip_prefix):
        """Sets the remote_ip_prefix of this CreateSecurityGroupRuleOption.

        远端IP地址，当direction是egress时为虚拟机访问端的地址，当direction是ingress时为访问虚拟机的地址。  取值范围：IP地址，或者cidr格式  约束：和remote_group_id互斥

        :param remote_ip_prefix: The remote_ip_prefix of this CreateSecurityGroupRuleOption.
        :type remote_ip_prefix: str
        """
        self._remote_ip_prefix = remote_ip_prefix

    @property
    def action(self):
        """Gets the action of this CreateSecurityGroupRuleOption.

        安全组规则生效策略 取值范围：allow 允许，deny 拒绝  约束：默认值为allow

        :return: The action of this CreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateSecurityGroupRuleOption.

        安全组规则生效策略 取值范围：allow 允许，deny 拒绝  约束：默认值为allow

        :param action: The action of this CreateSecurityGroupRuleOption.
        :type action: str
        """
        self._action = action

    @property
    def priority(self):
        """Gets the priority of this CreateSecurityGroupRuleOption.

        规则在安全组中的优先级  取值范围：1~100，1代表最高优先级  约束：默认值为1

        :return: The priority of this CreateSecurityGroupRuleOption.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateSecurityGroupRuleOption.

        规则在安全组中的优先级  取值范围：1~100，1代表最高优先级  约束：默认值为1

        :param priority: The priority of this CreateSecurityGroupRuleOption.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, CreateSecurityGroupRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
