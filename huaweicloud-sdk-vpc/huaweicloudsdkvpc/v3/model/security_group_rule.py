# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityGroupRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'description': 'str',
        'security_group_id': 'str',
        'direction': 'str',
        'protocol': 'str',
        'ethertype': 'str',
        'multiport': 'str',
        'action': 'str',
        'priority': 'int',
        'remote_group_id': 'str',
        'remote_ip_prefix': 'str',
        'remote_address_group_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'security_group_id': 'security_group_id',
        'direction': 'direction',
        'protocol': 'protocol',
        'ethertype': 'ethertype',
        'multiport': 'multiport',
        'action': 'action',
        'priority': 'priority',
        'remote_group_id': 'remote_group_id',
        'remote_ip_prefix': 'remote_ip_prefix',
        'remote_address_group_id': 'remote_address_group_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'project_id': 'project_id'
    }

    def __init__(self, id=None, description=None, security_group_id=None, direction=None, protocol=None, ethertype=None, multiport=None, action=None, priority=None, remote_group_id=None, remote_ip_prefix=None, remote_address_group_id=None, created_at=None, updated_at=None, project_id=None):
        """SecurityGroupRule

        The model defined in huaweicloud sdk

        :param id: 功能描述：安全组规则对应的唯一标识 取值范围：带“-”的标准UUID格式
        :type id: str
        :param description: 功能说明：安全组的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param security_group_id: 功能说明：安全组规则所属的安全组ID
        :type security_group_id: str
        :param direction: 功能说明：安全组规则的出入控制方向 取值范围：ingress 表示入方向；egress 表示出方向
        :type direction: str
        :param protocol: 功能说明：协议类型 取值范围：icmp、tcp、udp、icmpv6或IP协议号 约束：为空表示支持所有协议。协议为icmpv6时，网络类型应该为IPv6；协议为icmp时，网络类型应该为IPv4
        :type protocol: str
        :param ethertype: 功能说明：IP地址协议类型 取值范围：IPv4，IPv6 约束：不填默认值为IPv4
        :type ethertype: str
        :param multiport: 功能说明：端口取值范围 取值范围：支持单端口(80)，连续端口(1-30)以及不连续端口(22,3389,80)
        :type multiport: str
        :param action: 功能说明：安全组规则生效策略 取值范围：allow 允许，deny 拒绝 约束：默认值为deny
        :type action: str
        :param priority: 功能说明：优先级 取值范围：1~100，1代表最高优先级
        :type priority: int
        :param remote_group_id: 功能说明：远端安全组ID，表示该安全组内的流量允许或拒绝 取值范围：租户下存在的安全组ID 约束：与remote_ip_prefix，remote_address_group_id功能互斥
        :type remote_group_id: str
        :param remote_ip_prefix: 功能说明：远端IP地址，当direction是egress时为虚拟机访问端的地址，当direction是ingress时为访问虚拟机的地址 取值范围：IP地址，或者cidr格式 约束：与remote_group_id、remote_address_group_id互斥
        :type remote_ip_prefix: str
        :param remote_address_group_id: 功能说明：远端地址组ID 取值范围：租户下存在的地址组ID 约束：与remote_ip_prefix，remote_group_id功能互斥
        :type remote_address_group_id: str
        :param created_at: 功能说明：安全组规则创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 功能说明：安全组规则更新时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        :param project_id: 功能说明：安全组规则所属项目ID
        :type project_id: str
        """
        
        

        self._id = None
        self._description = None
        self._security_group_id = None
        self._direction = None
        self._protocol = None
        self._ethertype = None
        self._multiport = None
        self._action = None
        self._priority = None
        self._remote_group_id = None
        self._remote_ip_prefix = None
        self._remote_address_group_id = None
        self._created_at = None
        self._updated_at = None
        self._project_id = None
        self.discriminator = None

        self.id = id
        self.description = description
        self.security_group_id = security_group_id
        self.direction = direction
        self.protocol = protocol
        self.ethertype = ethertype
        self.multiport = multiport
        self.action = action
        self.priority = priority
        self.remote_group_id = remote_group_id
        self.remote_ip_prefix = remote_ip_prefix
        self.remote_address_group_id = remote_address_group_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.project_id = project_id

    @property
    def id(self):
        """Gets the id of this SecurityGroupRule.

        功能描述：安全组规则对应的唯一标识 取值范围：带“-”的标准UUID格式

        :return: The id of this SecurityGroupRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SecurityGroupRule.

        功能描述：安全组规则对应的唯一标识 取值范围：带“-”的标准UUID格式

        :param id: The id of this SecurityGroupRule.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this SecurityGroupRule.

        功能说明：安全组的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this SecurityGroupRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecurityGroupRule.

        功能说明：安全组的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this SecurityGroupRule.
        :type description: str
        """
        self._description = description

    @property
    def security_group_id(self):
        """Gets the security_group_id of this SecurityGroupRule.

        功能说明：安全组规则所属的安全组ID

        :return: The security_group_id of this SecurityGroupRule.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this SecurityGroupRule.

        功能说明：安全组规则所属的安全组ID

        :param security_group_id: The security_group_id of this SecurityGroupRule.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def direction(self):
        """Gets the direction of this SecurityGroupRule.

        功能说明：安全组规则的出入控制方向 取值范围：ingress 表示入方向；egress 表示出方向

        :return: The direction of this SecurityGroupRule.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this SecurityGroupRule.

        功能说明：安全组规则的出入控制方向 取值范围：ingress 表示入方向；egress 表示出方向

        :param direction: The direction of this SecurityGroupRule.
        :type direction: str
        """
        self._direction = direction

    @property
    def protocol(self):
        """Gets the protocol of this SecurityGroupRule.

        功能说明：协议类型 取值范围：icmp、tcp、udp、icmpv6或IP协议号 约束：为空表示支持所有协议。协议为icmpv6时，网络类型应该为IPv6；协议为icmp时，网络类型应该为IPv4

        :return: The protocol of this SecurityGroupRule.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SecurityGroupRule.

        功能说明：协议类型 取值范围：icmp、tcp、udp、icmpv6或IP协议号 约束：为空表示支持所有协议。协议为icmpv6时，网络类型应该为IPv6；协议为icmp时，网络类型应该为IPv4

        :param protocol: The protocol of this SecurityGroupRule.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def ethertype(self):
        """Gets the ethertype of this SecurityGroupRule.

        功能说明：IP地址协议类型 取值范围：IPv4，IPv6 约束：不填默认值为IPv4

        :return: The ethertype of this SecurityGroupRule.
        :rtype: str
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, ethertype):
        """Sets the ethertype of this SecurityGroupRule.

        功能说明：IP地址协议类型 取值范围：IPv4，IPv6 约束：不填默认值为IPv4

        :param ethertype: The ethertype of this SecurityGroupRule.
        :type ethertype: str
        """
        self._ethertype = ethertype

    @property
    def multiport(self):
        """Gets the multiport of this SecurityGroupRule.

        功能说明：端口取值范围 取值范围：支持单端口(80)，连续端口(1-30)以及不连续端口(22,3389,80)

        :return: The multiport of this SecurityGroupRule.
        :rtype: str
        """
        return self._multiport

    @multiport.setter
    def multiport(self, multiport):
        """Sets the multiport of this SecurityGroupRule.

        功能说明：端口取值范围 取值范围：支持单端口(80)，连续端口(1-30)以及不连续端口(22,3389,80)

        :param multiport: The multiport of this SecurityGroupRule.
        :type multiport: str
        """
        self._multiport = multiport

    @property
    def action(self):
        """Gets the action of this SecurityGroupRule.

        功能说明：安全组规则生效策略 取值范围：allow 允许，deny 拒绝 约束：默认值为deny

        :return: The action of this SecurityGroupRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this SecurityGroupRule.

        功能说明：安全组规则生效策略 取值范围：allow 允许，deny 拒绝 约束：默认值为deny

        :param action: The action of this SecurityGroupRule.
        :type action: str
        """
        self._action = action

    @property
    def priority(self):
        """Gets the priority of this SecurityGroupRule.

        功能说明：优先级 取值范围：1~100，1代表最高优先级

        :return: The priority of this SecurityGroupRule.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this SecurityGroupRule.

        功能说明：优先级 取值范围：1~100，1代表最高优先级

        :param priority: The priority of this SecurityGroupRule.
        :type priority: int
        """
        self._priority = priority

    @property
    def remote_group_id(self):
        """Gets the remote_group_id of this SecurityGroupRule.

        功能说明：远端安全组ID，表示该安全组内的流量允许或拒绝 取值范围：租户下存在的安全组ID 约束：与remote_ip_prefix，remote_address_group_id功能互斥

        :return: The remote_group_id of this SecurityGroupRule.
        :rtype: str
        """
        return self._remote_group_id

    @remote_group_id.setter
    def remote_group_id(self, remote_group_id):
        """Sets the remote_group_id of this SecurityGroupRule.

        功能说明：远端安全组ID，表示该安全组内的流量允许或拒绝 取值范围：租户下存在的安全组ID 约束：与remote_ip_prefix，remote_address_group_id功能互斥

        :param remote_group_id: The remote_group_id of this SecurityGroupRule.
        :type remote_group_id: str
        """
        self._remote_group_id = remote_group_id

    @property
    def remote_ip_prefix(self):
        """Gets the remote_ip_prefix of this SecurityGroupRule.

        功能说明：远端IP地址，当direction是egress时为虚拟机访问端的地址，当direction是ingress时为访问虚拟机的地址 取值范围：IP地址，或者cidr格式 约束：与remote_group_id、remote_address_group_id互斥

        :return: The remote_ip_prefix of this SecurityGroupRule.
        :rtype: str
        """
        return self._remote_ip_prefix

    @remote_ip_prefix.setter
    def remote_ip_prefix(self, remote_ip_prefix):
        """Sets the remote_ip_prefix of this SecurityGroupRule.

        功能说明：远端IP地址，当direction是egress时为虚拟机访问端的地址，当direction是ingress时为访问虚拟机的地址 取值范围：IP地址，或者cidr格式 约束：与remote_group_id、remote_address_group_id互斥

        :param remote_ip_prefix: The remote_ip_prefix of this SecurityGroupRule.
        :type remote_ip_prefix: str
        """
        self._remote_ip_prefix = remote_ip_prefix

    @property
    def remote_address_group_id(self):
        """Gets the remote_address_group_id of this SecurityGroupRule.

        功能说明：远端地址组ID 取值范围：租户下存在的地址组ID 约束：与remote_ip_prefix，remote_group_id功能互斥

        :return: The remote_address_group_id of this SecurityGroupRule.
        :rtype: str
        """
        return self._remote_address_group_id

    @remote_address_group_id.setter
    def remote_address_group_id(self, remote_address_group_id):
        """Sets the remote_address_group_id of this SecurityGroupRule.

        功能说明：远端地址组ID 取值范围：租户下存在的地址组ID 约束：与remote_ip_prefix，remote_group_id功能互斥

        :param remote_address_group_id: The remote_address_group_id of this SecurityGroupRule.
        :type remote_address_group_id: str
        """
        self._remote_address_group_id = remote_address_group_id

    @property
    def created_at(self):
        """Gets the created_at of this SecurityGroupRule.

        功能说明：安全组规则创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this SecurityGroupRule.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SecurityGroupRule.

        功能说明：安全组规则创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this SecurityGroupRule.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SecurityGroupRule.

        功能说明：安全组规则更新时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this SecurityGroupRule.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SecurityGroupRule.

        功能说明：安全组规则更新时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this SecurityGroupRule.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        """Gets the project_id of this SecurityGroupRule.

        功能说明：安全组规则所属项目ID

        :return: The project_id of this SecurityGroupRule.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SecurityGroupRule.

        功能说明：安全组规则所属项目ID

        :param project_id: The project_id of this SecurityGroupRule.
        :type project_id: str
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
        if not isinstance(other, SecurityGroupRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
