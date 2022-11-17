# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronSecurityGroupRule:

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
        'id': 'str',
        'port_range_max': 'int',
        'port_range_min': 'int',
        'protocol': 'str',
        'remote_group_id': 'str',
        'remote_ip_prefix': 'str',
        'remote_address_group_id': 'str',
        'security_group_id': 'str',
        'tenant_id': 'str',
        'project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'description': 'description',
        'direction': 'direction',
        'ethertype': 'ethertype',
        'id': 'id',
        'port_range_max': 'port_range_max',
        'port_range_min': 'port_range_min',
        'protocol': 'protocol',
        'remote_group_id': 'remote_group_id',
        'remote_ip_prefix': 'remote_ip_prefix',
        'remote_address_group_id': 'remote_address_group_id',
        'security_group_id': 'security_group_id',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, description=None, direction=None, ethertype=None, id=None, port_range_max=None, port_range_min=None, protocol=None, remote_group_id=None, remote_ip_prefix=None, remote_address_group_id=None, security_group_id=None, tenant_id=None, project_id=None, created_at=None, updated_at=None):
        """NeutronSecurityGroupRule

        The model defined in huaweicloud sdk

        :param description: 安全组规则描述
        :type description: str
        :param direction: 功能说明：规则方向 取值范围：ingress、egress
        :type direction: str
        :param ethertype: 功能说明：网络类型 取值范围：IPv4、IPv6
        :type ethertype: str
        :param id: 安全组规则ID，查询安全组规则非必选
        :type id: str
        :param port_range_max: 功能说明：最大端口 取值范围：当协议类型为ICMP时，该值表示ICMP的code
        :type port_range_max: int
        :param port_range_min: 功能说明：最小端口 当协议类型为ICMP时，该值表示ICMP的type。protocol为tcp和udp时，port_range_max和port_range_min必须同时输入，且port_range_max应大于等于port_range_min。protocol为icmp时，指定ICMP code（port_range_max）时，必须同时指定ICMP type（port_range_min）。
        :type port_range_min: int
        :param protocol: 功能说明：tcp/udp/icmp/icmpv6或IP协议编号（0~255） 约束：协议为icmpv6时，网络类型应该为IPv6；协议为icmp时，网络类型应该为IPv4
        :type protocol: str
        :param remote_group_id: 所属安全组的对端ID
        :type remote_group_id: str
        :param remote_ip_prefix: 对端ip网段
        :type remote_ip_prefix: str
        :param remote_address_group_id: 功能说明：远端IP地址组ID 约束：和remote_ip_prefix，remote_group_id互斥
        :type remote_address_group_id: str
        :param security_group_id: 所属安全组ID
        :type security_group_id: str
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param created_at: 功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        """
        
        

        self._description = None
        self._direction = None
        self._ethertype = None
        self._id = None
        self._port_range_max = None
        self._port_range_min = None
        self._protocol = None
        self._remote_group_id = None
        self._remote_ip_prefix = None
        self._remote_address_group_id = None
        self._security_group_id = None
        self._tenant_id = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.description = description
        self.direction = direction
        self.ethertype = ethertype
        self.id = id
        self.port_range_max = port_range_max
        self.port_range_min = port_range_min
        self.protocol = protocol
        self.remote_group_id = remote_group_id
        self.remote_ip_prefix = remote_ip_prefix
        if remote_address_group_id is not None:
            self.remote_address_group_id = remote_address_group_id
        self.security_group_id = security_group_id
        self.tenant_id = tenant_id
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def description(self):
        """Gets the description of this NeutronSecurityGroupRule.

        安全组规则描述

        :return: The description of this NeutronSecurityGroupRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NeutronSecurityGroupRule.

        安全组规则描述

        :param description: The description of this NeutronSecurityGroupRule.
        :type description: str
        """
        self._description = description

    @property
    def direction(self):
        """Gets the direction of this NeutronSecurityGroupRule.

        功能说明：规则方向 取值范围：ingress、egress

        :return: The direction of this NeutronSecurityGroupRule.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this NeutronSecurityGroupRule.

        功能说明：规则方向 取值范围：ingress、egress

        :param direction: The direction of this NeutronSecurityGroupRule.
        :type direction: str
        """
        self._direction = direction

    @property
    def ethertype(self):
        """Gets the ethertype of this NeutronSecurityGroupRule.

        功能说明：网络类型 取值范围：IPv4、IPv6

        :return: The ethertype of this NeutronSecurityGroupRule.
        :rtype: str
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, ethertype):
        """Sets the ethertype of this NeutronSecurityGroupRule.

        功能说明：网络类型 取值范围：IPv4、IPv6

        :param ethertype: The ethertype of this NeutronSecurityGroupRule.
        :type ethertype: str
        """
        self._ethertype = ethertype

    @property
    def id(self):
        """Gets the id of this NeutronSecurityGroupRule.

        安全组规则ID，查询安全组规则非必选

        :return: The id of this NeutronSecurityGroupRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronSecurityGroupRule.

        安全组规则ID，查询安全组规则非必选

        :param id: The id of this NeutronSecurityGroupRule.
        :type id: str
        """
        self._id = id

    @property
    def port_range_max(self):
        """Gets the port_range_max of this NeutronSecurityGroupRule.

        功能说明：最大端口 取值范围：当协议类型为ICMP时，该值表示ICMP的code

        :return: The port_range_max of this NeutronSecurityGroupRule.
        :rtype: int
        """
        return self._port_range_max

    @port_range_max.setter
    def port_range_max(self, port_range_max):
        """Sets the port_range_max of this NeutronSecurityGroupRule.

        功能说明：最大端口 取值范围：当协议类型为ICMP时，该值表示ICMP的code

        :param port_range_max: The port_range_max of this NeutronSecurityGroupRule.
        :type port_range_max: int
        """
        self._port_range_max = port_range_max

    @property
    def port_range_min(self):
        """Gets the port_range_min of this NeutronSecurityGroupRule.

        功能说明：最小端口 当协议类型为ICMP时，该值表示ICMP的type。protocol为tcp和udp时，port_range_max和port_range_min必须同时输入，且port_range_max应大于等于port_range_min。protocol为icmp时，指定ICMP code（port_range_max）时，必须同时指定ICMP type（port_range_min）。

        :return: The port_range_min of this NeutronSecurityGroupRule.
        :rtype: int
        """
        return self._port_range_min

    @port_range_min.setter
    def port_range_min(self, port_range_min):
        """Sets the port_range_min of this NeutronSecurityGroupRule.

        功能说明：最小端口 当协议类型为ICMP时，该值表示ICMP的type。protocol为tcp和udp时，port_range_max和port_range_min必须同时输入，且port_range_max应大于等于port_range_min。protocol为icmp时，指定ICMP code（port_range_max）时，必须同时指定ICMP type（port_range_min）。

        :param port_range_min: The port_range_min of this NeutronSecurityGroupRule.
        :type port_range_min: int
        """
        self._port_range_min = port_range_min

    @property
    def protocol(self):
        """Gets the protocol of this NeutronSecurityGroupRule.

        功能说明：tcp/udp/icmp/icmpv6或IP协议编号（0~255） 约束：协议为icmpv6时，网络类型应该为IPv6；协议为icmp时，网络类型应该为IPv4

        :return: The protocol of this NeutronSecurityGroupRule.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NeutronSecurityGroupRule.

        功能说明：tcp/udp/icmp/icmpv6或IP协议编号（0~255） 约束：协议为icmpv6时，网络类型应该为IPv6；协议为icmp时，网络类型应该为IPv4

        :param protocol: The protocol of this NeutronSecurityGroupRule.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def remote_group_id(self):
        """Gets the remote_group_id of this NeutronSecurityGroupRule.

        所属安全组的对端ID

        :return: The remote_group_id of this NeutronSecurityGroupRule.
        :rtype: str
        """
        return self._remote_group_id

    @remote_group_id.setter
    def remote_group_id(self, remote_group_id):
        """Sets the remote_group_id of this NeutronSecurityGroupRule.

        所属安全组的对端ID

        :param remote_group_id: The remote_group_id of this NeutronSecurityGroupRule.
        :type remote_group_id: str
        """
        self._remote_group_id = remote_group_id

    @property
    def remote_ip_prefix(self):
        """Gets the remote_ip_prefix of this NeutronSecurityGroupRule.

        对端ip网段

        :return: The remote_ip_prefix of this NeutronSecurityGroupRule.
        :rtype: str
        """
        return self._remote_ip_prefix

    @remote_ip_prefix.setter
    def remote_ip_prefix(self, remote_ip_prefix):
        """Sets the remote_ip_prefix of this NeutronSecurityGroupRule.

        对端ip网段

        :param remote_ip_prefix: The remote_ip_prefix of this NeutronSecurityGroupRule.
        :type remote_ip_prefix: str
        """
        self._remote_ip_prefix = remote_ip_prefix

    @property
    def remote_address_group_id(self):
        """Gets the remote_address_group_id of this NeutronSecurityGroupRule.

        功能说明：远端IP地址组ID 约束：和remote_ip_prefix，remote_group_id互斥

        :return: The remote_address_group_id of this NeutronSecurityGroupRule.
        :rtype: str
        """
        return self._remote_address_group_id

    @remote_address_group_id.setter
    def remote_address_group_id(self, remote_address_group_id):
        """Sets the remote_address_group_id of this NeutronSecurityGroupRule.

        功能说明：远端IP地址组ID 约束：和remote_ip_prefix，remote_group_id互斥

        :param remote_address_group_id: The remote_address_group_id of this NeutronSecurityGroupRule.
        :type remote_address_group_id: str
        """
        self._remote_address_group_id = remote_address_group_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this NeutronSecurityGroupRule.

        所属安全组ID

        :return: The security_group_id of this NeutronSecurityGroupRule.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this NeutronSecurityGroupRule.

        所属安全组ID

        :param security_group_id: The security_group_id of this NeutronSecurityGroupRule.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronSecurityGroupRule.

        项目ID

        :return: The tenant_id of this NeutronSecurityGroupRule.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronSecurityGroupRule.

        项目ID

        :param tenant_id: The tenant_id of this NeutronSecurityGroupRule.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this NeutronSecurityGroupRule.

        项目ID

        :return: The project_id of this NeutronSecurityGroupRule.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronSecurityGroupRule.

        项目ID

        :param project_id: The project_id of this NeutronSecurityGroupRule.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this NeutronSecurityGroupRule.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this NeutronSecurityGroupRule.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NeutronSecurityGroupRule.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this NeutronSecurityGroupRule.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NeutronSecurityGroupRule.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this NeutronSecurityGroupRule.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NeutronSecurityGroupRule.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this NeutronSecurityGroupRule.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, NeutronSecurityGroupRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
