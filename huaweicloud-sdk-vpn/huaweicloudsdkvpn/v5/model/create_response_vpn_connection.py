# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResponseVpnConnection:

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
        'name': 'str',
        'vgw_id': 'str',
        'vgw_ip': 'str',
        'style': 'str',
        'cgw_id': 'str',
        'peer_subnets': 'list[str]',
        'tunnel_local_address': 'str',
        'tunnel_peer_address': 'str',
        'enable_nqa': 'bool',
        'policy_rules': 'list[PolicyRule]',
        'ikepolicy': 'IkePolicy',
        'ipsecpolicy': 'IpsecPolicy',
        'created_at': 'str',
        'updated_at': 'str',
        'enterprise_project_id': 'str',
        'connection_monitor_id': 'str',
        'ha_role': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vgw_id': 'vgw_id',
        'vgw_ip': 'vgw_ip',
        'style': 'style',
        'cgw_id': 'cgw_id',
        'peer_subnets': 'peer_subnets',
        'tunnel_local_address': 'tunnel_local_address',
        'tunnel_peer_address': 'tunnel_peer_address',
        'enable_nqa': 'enable_nqa',
        'policy_rules': 'policy_rules',
        'ikepolicy': 'ikepolicy',
        'ipsecpolicy': 'ipsecpolicy',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'enterprise_project_id': 'enterprise_project_id',
        'connection_monitor_id': 'connection_monitor_id',
        'ha_role': 'ha_role'
    }

    def __init__(self, id=None, name=None, vgw_id=None, vgw_ip=None, style=None, cgw_id=None, peer_subnets=None, tunnel_local_address=None, tunnel_peer_address=None, enable_nqa=None, policy_rules=None, ikepolicy=None, ipsecpolicy=None, created_at=None, updated_at=None, enterprise_project_id=None, connection_monitor_id=None, ha_role=None):
        """CreateResponseVpnConnection

        The model defined in huaweicloud sdk

        :param id: VPN连接ID
        :type id: str
        :param name: VPN连接名称
        :type name: str
        :param vgw_id: VPN网关ID
        :type vgw_id: str
        :param vgw_ip: VGW IP
        :type vgw_ip: str
        :param style: 连接模式 允许范围[POLICY, STATIC, BGP] POLICY: 策略模式 STATIC: 静态路由模式 BGP: bgp路由模式
        :type style: str
        :param cgw_id: 对端网关ID
        :type cgw_id: str
        :param peer_subnets: 对端网段
        :type peer_subnets: list[str]
        :param tunnel_local_address: 本端隧道口地址
        :type tunnel_local_address: str
        :param tunnel_peer_address: 对端隧道口地址
        :type tunnel_peer_address: str
        :param enable_nqa: 开启NQA检测
        :type enable_nqa: bool
        :param policy_rules: 策略模式的策略规则组
        :type policy_rules: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        :param ikepolicy: 
        :type ikepolicy: :class:`huaweicloudsdkvpn.v5.IkePolicy`
        :param ipsecpolicy: 
        :type ipsecpolicy: :class:`huaweicloudsdkvpn.v5.IpsecPolicy`
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param connection_monitor_id: 连接监控ID
        :type connection_monitor_id: str
        :param ha_role: 连接的HA角色
        :type ha_role: str
        """
        
        

        self._id = None
        self._name = None
        self._vgw_id = None
        self._vgw_ip = None
        self._style = None
        self._cgw_id = None
        self._peer_subnets = None
        self._tunnel_local_address = None
        self._tunnel_peer_address = None
        self._enable_nqa = None
        self._policy_rules = None
        self._ikepolicy = None
        self._ipsecpolicy = None
        self._created_at = None
        self._updated_at = None
        self._enterprise_project_id = None
        self._connection_monitor_id = None
        self._ha_role = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if vgw_id is not None:
            self.vgw_id = vgw_id
        if vgw_ip is not None:
            self.vgw_ip = vgw_ip
        if style is not None:
            self.style = style
        if cgw_id is not None:
            self.cgw_id = cgw_id
        if peer_subnets is not None:
            self.peer_subnets = peer_subnets
        if tunnel_local_address is not None:
            self.tunnel_local_address = tunnel_local_address
        if tunnel_peer_address is not None:
            self.tunnel_peer_address = tunnel_peer_address
        if enable_nqa is not None:
            self.enable_nqa = enable_nqa
        if policy_rules is not None:
            self.policy_rules = policy_rules
        if ikepolicy is not None:
            self.ikepolicy = ikepolicy
        if ipsecpolicy is not None:
            self.ipsecpolicy = ipsecpolicy
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if connection_monitor_id is not None:
            self.connection_monitor_id = connection_monitor_id
        if ha_role is not None:
            self.ha_role = ha_role

    @property
    def id(self):
        """Gets the id of this CreateResponseVpnConnection.

        VPN连接ID

        :return: The id of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateResponseVpnConnection.

        VPN连接ID

        :param id: The id of this CreateResponseVpnConnection.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateResponseVpnConnection.

        VPN连接名称

        :return: The name of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateResponseVpnConnection.

        VPN连接名称

        :param name: The name of this CreateResponseVpnConnection.
        :type name: str
        """
        self._name = name

    @property
    def vgw_id(self):
        """Gets the vgw_id of this CreateResponseVpnConnection.

        VPN网关ID

        :return: The vgw_id of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        """Sets the vgw_id of this CreateResponseVpnConnection.

        VPN网关ID

        :param vgw_id: The vgw_id of this CreateResponseVpnConnection.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def vgw_ip(self):
        """Gets the vgw_ip of this CreateResponseVpnConnection.

        VGW IP

        :return: The vgw_ip of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._vgw_ip

    @vgw_ip.setter
    def vgw_ip(self, vgw_ip):
        """Sets the vgw_ip of this CreateResponseVpnConnection.

        VGW IP

        :param vgw_ip: The vgw_ip of this CreateResponseVpnConnection.
        :type vgw_ip: str
        """
        self._vgw_ip = vgw_ip

    @property
    def style(self):
        """Gets the style of this CreateResponseVpnConnection.

        连接模式 允许范围[POLICY, STATIC, BGP] POLICY: 策略模式 STATIC: 静态路由模式 BGP: bgp路由模式

        :return: The style of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this CreateResponseVpnConnection.

        连接模式 允许范围[POLICY, STATIC, BGP] POLICY: 策略模式 STATIC: 静态路由模式 BGP: bgp路由模式

        :param style: The style of this CreateResponseVpnConnection.
        :type style: str
        """
        self._style = style

    @property
    def cgw_id(self):
        """Gets the cgw_id of this CreateResponseVpnConnection.

        对端网关ID

        :return: The cgw_id of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._cgw_id

    @cgw_id.setter
    def cgw_id(self, cgw_id):
        """Sets the cgw_id of this CreateResponseVpnConnection.

        对端网关ID

        :param cgw_id: The cgw_id of this CreateResponseVpnConnection.
        :type cgw_id: str
        """
        self._cgw_id = cgw_id

    @property
    def peer_subnets(self):
        """Gets the peer_subnets of this CreateResponseVpnConnection.

        对端网段

        :return: The peer_subnets of this CreateResponseVpnConnection.
        :rtype: list[str]
        """
        return self._peer_subnets

    @peer_subnets.setter
    def peer_subnets(self, peer_subnets):
        """Sets the peer_subnets of this CreateResponseVpnConnection.

        对端网段

        :param peer_subnets: The peer_subnets of this CreateResponseVpnConnection.
        :type peer_subnets: list[str]
        """
        self._peer_subnets = peer_subnets

    @property
    def tunnel_local_address(self):
        """Gets the tunnel_local_address of this CreateResponseVpnConnection.

        本端隧道口地址

        :return: The tunnel_local_address of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._tunnel_local_address

    @tunnel_local_address.setter
    def tunnel_local_address(self, tunnel_local_address):
        """Sets the tunnel_local_address of this CreateResponseVpnConnection.

        本端隧道口地址

        :param tunnel_local_address: The tunnel_local_address of this CreateResponseVpnConnection.
        :type tunnel_local_address: str
        """
        self._tunnel_local_address = tunnel_local_address

    @property
    def tunnel_peer_address(self):
        """Gets the tunnel_peer_address of this CreateResponseVpnConnection.

        对端隧道口地址

        :return: The tunnel_peer_address of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._tunnel_peer_address

    @tunnel_peer_address.setter
    def tunnel_peer_address(self, tunnel_peer_address):
        """Sets the tunnel_peer_address of this CreateResponseVpnConnection.

        对端隧道口地址

        :param tunnel_peer_address: The tunnel_peer_address of this CreateResponseVpnConnection.
        :type tunnel_peer_address: str
        """
        self._tunnel_peer_address = tunnel_peer_address

    @property
    def enable_nqa(self):
        """Gets the enable_nqa of this CreateResponseVpnConnection.

        开启NQA检测

        :return: The enable_nqa of this CreateResponseVpnConnection.
        :rtype: bool
        """
        return self._enable_nqa

    @enable_nqa.setter
    def enable_nqa(self, enable_nqa):
        """Sets the enable_nqa of this CreateResponseVpnConnection.

        开启NQA检测

        :param enable_nqa: The enable_nqa of this CreateResponseVpnConnection.
        :type enable_nqa: bool
        """
        self._enable_nqa = enable_nqa

    @property
    def policy_rules(self):
        """Gets the policy_rules of this CreateResponseVpnConnection.

        策略模式的策略规则组

        :return: The policy_rules of this CreateResponseVpnConnection.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        return self._policy_rules

    @policy_rules.setter
    def policy_rules(self, policy_rules):
        """Sets the policy_rules of this CreateResponseVpnConnection.

        策略模式的策略规则组

        :param policy_rules: The policy_rules of this CreateResponseVpnConnection.
        :type policy_rules: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        self._policy_rules = policy_rules

    @property
    def ikepolicy(self):
        """Gets the ikepolicy of this CreateResponseVpnConnection.

        :return: The ikepolicy of this CreateResponseVpnConnection.
        :rtype: :class:`huaweicloudsdkvpn.v5.IkePolicy`
        """
        return self._ikepolicy

    @ikepolicy.setter
    def ikepolicy(self, ikepolicy):
        """Sets the ikepolicy of this CreateResponseVpnConnection.

        :param ikepolicy: The ikepolicy of this CreateResponseVpnConnection.
        :type ikepolicy: :class:`huaweicloudsdkvpn.v5.IkePolicy`
        """
        self._ikepolicy = ikepolicy

    @property
    def ipsecpolicy(self):
        """Gets the ipsecpolicy of this CreateResponseVpnConnection.

        :return: The ipsecpolicy of this CreateResponseVpnConnection.
        :rtype: :class:`huaweicloudsdkvpn.v5.IpsecPolicy`
        """
        return self._ipsecpolicy

    @ipsecpolicy.setter
    def ipsecpolicy(self, ipsecpolicy):
        """Sets the ipsecpolicy of this CreateResponseVpnConnection.

        :param ipsecpolicy: The ipsecpolicy of this CreateResponseVpnConnection.
        :type ipsecpolicy: :class:`huaweicloudsdkvpn.v5.IpsecPolicy`
        """
        self._ipsecpolicy = ipsecpolicy

    @property
    def created_at(self):
        """Gets the created_at of this CreateResponseVpnConnection.

        创建时间

        :return: The created_at of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateResponseVpnConnection.

        创建时间

        :param created_at: The created_at of this CreateResponseVpnConnection.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateResponseVpnConnection.

        更新时间

        :return: The updated_at of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateResponseVpnConnection.

        更新时间

        :param updated_at: The updated_at of this CreateResponseVpnConnection.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateResponseVpnConnection.

        企业项目ID

        :return: The enterprise_project_id of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateResponseVpnConnection.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateResponseVpnConnection.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def connection_monitor_id(self):
        """Gets the connection_monitor_id of this CreateResponseVpnConnection.

        连接监控ID

        :return: The connection_monitor_id of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._connection_monitor_id

    @connection_monitor_id.setter
    def connection_monitor_id(self, connection_monitor_id):
        """Sets the connection_monitor_id of this CreateResponseVpnConnection.

        连接监控ID

        :param connection_monitor_id: The connection_monitor_id of this CreateResponseVpnConnection.
        :type connection_monitor_id: str
        """
        self._connection_monitor_id = connection_monitor_id

    @property
    def ha_role(self):
        """Gets the ha_role of this CreateResponseVpnConnection.

        连接的HA角色

        :return: The ha_role of this CreateResponseVpnConnection.
        :rtype: str
        """
        return self._ha_role

    @ha_role.setter
    def ha_role(self, ha_role):
        """Sets the ha_role of this CreateResponseVpnConnection.

        连接的HA角色

        :param ha_role: The ha_role of this CreateResponseVpnConnection.
        :type ha_role: str
        """
        self._ha_role = ha_role

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
        if not isinstance(other, CreateResponseVpnConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
