# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseVpnConnection:

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
        'status': 'str',
        'vgw_id': 'str',
        'vgw_ip': 'str',
        'style': 'str',
        'cgw_id': 'str',
        'peer_subnets': 'list[str]',
        'tunnel_local_address': 'str',
        'tunnel_peer_address': 'str',
        'enable_nqa': 'bool',
        'enable_hub': 'bool',
        'policy_rules': 'list[PolicyRule]',
        'ikepolicy': 'IkePolicy',
        'ipsecpolicy': 'IpsecPolicy',
        'created_at': 'str',
        'updated_at': 'str',
        'enterprise_project_id': 'str',
        'connection_monitor_id': 'str',
        'ha_role': 'str',
        'tags': 'list[VpnResourceTag]',
        'peer_subnets_v6': 'list[str]',
        'policy_rules_v6': 'list[PolicyRule]',
        'bgp_peer': 'BgpPeer'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'vgw_id': 'vgw_id',
        'vgw_ip': 'vgw_ip',
        'style': 'style',
        'cgw_id': 'cgw_id',
        'peer_subnets': 'peer_subnets',
        'tunnel_local_address': 'tunnel_local_address',
        'tunnel_peer_address': 'tunnel_peer_address',
        'enable_nqa': 'enable_nqa',
        'enable_hub': 'enable_hub',
        'policy_rules': 'policy_rules',
        'ikepolicy': 'ikepolicy',
        'ipsecpolicy': 'ipsecpolicy',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'enterprise_project_id': 'enterprise_project_id',
        'connection_monitor_id': 'connection_monitor_id',
        'ha_role': 'ha_role',
        'tags': 'tags',
        'peer_subnets_v6': 'peer_subnets_v6',
        'policy_rules_v6': 'policy_rules_v6',
        'bgp_peer': 'bgp_peer'
    }

    def __init__(self, id=None, name=None, status=None, vgw_id=None, vgw_ip=None, style=None, cgw_id=None, peer_subnets=None, tunnel_local_address=None, tunnel_peer_address=None, enable_nqa=None, enable_hub=None, policy_rules=None, ikepolicy=None, ipsecpolicy=None, created_at=None, updated_at=None, enterprise_project_id=None, connection_monitor_id=None, ha_role=None, tags=None, peer_subnets_v6=None, policy_rules_v6=None, bgp_peer=None):
        r"""ResponseVpnConnection

        The model defined in huaweicloud sdk

        :param id: VPN连接ID
        :type id: str
        :param name: VPN连接名称
        :type name: str
        :param status: VPN连接状态
        :type status: str
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
        :param enable_hub: 开启分支互联
        :type enable_hub: bool
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
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        :param peer_subnets_v6: 使能ipv6的对端子网
        :type peer_subnets_v6: list[str]
        :param policy_rules_v6: 策略模式的ipv6策略规则组
        :type policy_rules_v6: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        :param bgp_peer: 
        :type bgp_peer: :class:`huaweicloudsdkvpn.v5.BgpPeer`
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._vgw_id = None
        self._vgw_ip = None
        self._style = None
        self._cgw_id = None
        self._peer_subnets = None
        self._tunnel_local_address = None
        self._tunnel_peer_address = None
        self._enable_nqa = None
        self._enable_hub = None
        self._policy_rules = None
        self._ikepolicy = None
        self._ipsecpolicy = None
        self._created_at = None
        self._updated_at = None
        self._enterprise_project_id = None
        self._connection_monitor_id = None
        self._ha_role = None
        self._tags = None
        self._peer_subnets_v6 = None
        self._policy_rules_v6 = None
        self._bgp_peer = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
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
        if enable_hub is not None:
            self.enable_hub = enable_hub
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
        if tags is not None:
            self.tags = tags
        if peer_subnets_v6 is not None:
            self.peer_subnets_v6 = peer_subnets_v6
        if policy_rules_v6 is not None:
            self.policy_rules_v6 = policy_rules_v6
        if bgp_peer is not None:
            self.bgp_peer = bgp_peer

    @property
    def id(self):
        r"""Gets the id of this ResponseVpnConnection.

        VPN连接ID

        :return: The id of this ResponseVpnConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResponseVpnConnection.

        VPN连接ID

        :param id: The id of this ResponseVpnConnection.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ResponseVpnConnection.

        VPN连接名称

        :return: The name of this ResponseVpnConnection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResponseVpnConnection.

        VPN连接名称

        :param name: The name of this ResponseVpnConnection.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ResponseVpnConnection.

        VPN连接状态

        :return: The status of this ResponseVpnConnection.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResponseVpnConnection.

        VPN连接状态

        :param status: The status of this ResponseVpnConnection.
        :type status: str
        """
        self._status = status

    @property
    def vgw_id(self):
        r"""Gets the vgw_id of this ResponseVpnConnection.

        VPN网关ID

        :return: The vgw_id of this ResponseVpnConnection.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        r"""Sets the vgw_id of this ResponseVpnConnection.

        VPN网关ID

        :param vgw_id: The vgw_id of this ResponseVpnConnection.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def vgw_ip(self):
        r"""Gets the vgw_ip of this ResponseVpnConnection.

        VGW IP

        :return: The vgw_ip of this ResponseVpnConnection.
        :rtype: str
        """
        return self._vgw_ip

    @vgw_ip.setter
    def vgw_ip(self, vgw_ip):
        r"""Sets the vgw_ip of this ResponseVpnConnection.

        VGW IP

        :param vgw_ip: The vgw_ip of this ResponseVpnConnection.
        :type vgw_ip: str
        """
        self._vgw_ip = vgw_ip

    @property
    def style(self):
        r"""Gets the style of this ResponseVpnConnection.

        连接模式 允许范围[POLICY, STATIC, BGP] POLICY: 策略模式 STATIC: 静态路由模式 BGP: bgp路由模式

        :return: The style of this ResponseVpnConnection.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        r"""Sets the style of this ResponseVpnConnection.

        连接模式 允许范围[POLICY, STATIC, BGP] POLICY: 策略模式 STATIC: 静态路由模式 BGP: bgp路由模式

        :param style: The style of this ResponseVpnConnection.
        :type style: str
        """
        self._style = style

    @property
    def cgw_id(self):
        r"""Gets the cgw_id of this ResponseVpnConnection.

        对端网关ID

        :return: The cgw_id of this ResponseVpnConnection.
        :rtype: str
        """
        return self._cgw_id

    @cgw_id.setter
    def cgw_id(self, cgw_id):
        r"""Sets the cgw_id of this ResponseVpnConnection.

        对端网关ID

        :param cgw_id: The cgw_id of this ResponseVpnConnection.
        :type cgw_id: str
        """
        self._cgw_id = cgw_id

    @property
    def peer_subnets(self):
        r"""Gets the peer_subnets of this ResponseVpnConnection.

        对端网段

        :return: The peer_subnets of this ResponseVpnConnection.
        :rtype: list[str]
        """
        return self._peer_subnets

    @peer_subnets.setter
    def peer_subnets(self, peer_subnets):
        r"""Sets the peer_subnets of this ResponseVpnConnection.

        对端网段

        :param peer_subnets: The peer_subnets of this ResponseVpnConnection.
        :type peer_subnets: list[str]
        """
        self._peer_subnets = peer_subnets

    @property
    def tunnel_local_address(self):
        r"""Gets the tunnel_local_address of this ResponseVpnConnection.

        本端隧道口地址

        :return: The tunnel_local_address of this ResponseVpnConnection.
        :rtype: str
        """
        return self._tunnel_local_address

    @tunnel_local_address.setter
    def tunnel_local_address(self, tunnel_local_address):
        r"""Sets the tunnel_local_address of this ResponseVpnConnection.

        本端隧道口地址

        :param tunnel_local_address: The tunnel_local_address of this ResponseVpnConnection.
        :type tunnel_local_address: str
        """
        self._tunnel_local_address = tunnel_local_address

    @property
    def tunnel_peer_address(self):
        r"""Gets the tunnel_peer_address of this ResponseVpnConnection.

        对端隧道口地址

        :return: The tunnel_peer_address of this ResponseVpnConnection.
        :rtype: str
        """
        return self._tunnel_peer_address

    @tunnel_peer_address.setter
    def tunnel_peer_address(self, tunnel_peer_address):
        r"""Sets the tunnel_peer_address of this ResponseVpnConnection.

        对端隧道口地址

        :param tunnel_peer_address: The tunnel_peer_address of this ResponseVpnConnection.
        :type tunnel_peer_address: str
        """
        self._tunnel_peer_address = tunnel_peer_address

    @property
    def enable_nqa(self):
        r"""Gets the enable_nqa of this ResponseVpnConnection.

        开启NQA检测

        :return: The enable_nqa of this ResponseVpnConnection.
        :rtype: bool
        """
        return self._enable_nqa

    @enable_nqa.setter
    def enable_nqa(self, enable_nqa):
        r"""Sets the enable_nqa of this ResponseVpnConnection.

        开启NQA检测

        :param enable_nqa: The enable_nqa of this ResponseVpnConnection.
        :type enable_nqa: bool
        """
        self._enable_nqa = enable_nqa

    @property
    def enable_hub(self):
        r"""Gets the enable_hub of this ResponseVpnConnection.

        开启分支互联

        :return: The enable_hub of this ResponseVpnConnection.
        :rtype: bool
        """
        return self._enable_hub

    @enable_hub.setter
    def enable_hub(self, enable_hub):
        r"""Sets the enable_hub of this ResponseVpnConnection.

        开启分支互联

        :param enable_hub: The enable_hub of this ResponseVpnConnection.
        :type enable_hub: bool
        """
        self._enable_hub = enable_hub

    @property
    def policy_rules(self):
        r"""Gets the policy_rules of this ResponseVpnConnection.

        策略模式的策略规则组

        :return: The policy_rules of this ResponseVpnConnection.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        return self._policy_rules

    @policy_rules.setter
    def policy_rules(self, policy_rules):
        r"""Sets the policy_rules of this ResponseVpnConnection.

        策略模式的策略规则组

        :param policy_rules: The policy_rules of this ResponseVpnConnection.
        :type policy_rules: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        self._policy_rules = policy_rules

    @property
    def ikepolicy(self):
        r"""Gets the ikepolicy of this ResponseVpnConnection.

        :return: The ikepolicy of this ResponseVpnConnection.
        :rtype: :class:`huaweicloudsdkvpn.v5.IkePolicy`
        """
        return self._ikepolicy

    @ikepolicy.setter
    def ikepolicy(self, ikepolicy):
        r"""Sets the ikepolicy of this ResponseVpnConnection.

        :param ikepolicy: The ikepolicy of this ResponseVpnConnection.
        :type ikepolicy: :class:`huaweicloudsdkvpn.v5.IkePolicy`
        """
        self._ikepolicy = ikepolicy

    @property
    def ipsecpolicy(self):
        r"""Gets the ipsecpolicy of this ResponseVpnConnection.

        :return: The ipsecpolicy of this ResponseVpnConnection.
        :rtype: :class:`huaweicloudsdkvpn.v5.IpsecPolicy`
        """
        return self._ipsecpolicy

    @ipsecpolicy.setter
    def ipsecpolicy(self, ipsecpolicy):
        r"""Sets the ipsecpolicy of this ResponseVpnConnection.

        :param ipsecpolicy: The ipsecpolicy of this ResponseVpnConnection.
        :type ipsecpolicy: :class:`huaweicloudsdkvpn.v5.IpsecPolicy`
        """
        self._ipsecpolicy = ipsecpolicy

    @property
    def created_at(self):
        r"""Gets the created_at of this ResponseVpnConnection.

        创建时间

        :return: The created_at of this ResponseVpnConnection.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ResponseVpnConnection.

        创建时间

        :param created_at: The created_at of this ResponseVpnConnection.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ResponseVpnConnection.

        更新时间

        :return: The updated_at of this ResponseVpnConnection.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ResponseVpnConnection.

        更新时间

        :param updated_at: The updated_at of this ResponseVpnConnection.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ResponseVpnConnection.

        企业项目ID

        :return: The enterprise_project_id of this ResponseVpnConnection.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ResponseVpnConnection.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ResponseVpnConnection.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def connection_monitor_id(self):
        r"""Gets the connection_monitor_id of this ResponseVpnConnection.

        连接监控ID

        :return: The connection_monitor_id of this ResponseVpnConnection.
        :rtype: str
        """
        return self._connection_monitor_id

    @connection_monitor_id.setter
    def connection_monitor_id(self, connection_monitor_id):
        r"""Sets the connection_monitor_id of this ResponseVpnConnection.

        连接监控ID

        :param connection_monitor_id: The connection_monitor_id of this ResponseVpnConnection.
        :type connection_monitor_id: str
        """
        self._connection_monitor_id = connection_monitor_id

    @property
    def ha_role(self):
        r"""Gets the ha_role of this ResponseVpnConnection.

        连接的HA角色

        :return: The ha_role of this ResponseVpnConnection.
        :rtype: str
        """
        return self._ha_role

    @ha_role.setter
    def ha_role(self, ha_role):
        r"""Sets the ha_role of this ResponseVpnConnection.

        连接的HA角色

        :param ha_role: The ha_role of this ResponseVpnConnection.
        :type ha_role: str
        """
        self._ha_role = ha_role

    @property
    def tags(self):
        r"""Gets the tags of this ResponseVpnConnection.

        标签

        :return: The tags of this ResponseVpnConnection.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ResponseVpnConnection.

        标签

        :param tags: The tags of this ResponseVpnConnection.
        :type tags: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        self._tags = tags

    @property
    def peer_subnets_v6(self):
        r"""Gets the peer_subnets_v6 of this ResponseVpnConnection.

        使能ipv6的对端子网

        :return: The peer_subnets_v6 of this ResponseVpnConnection.
        :rtype: list[str]
        """
        return self._peer_subnets_v6

    @peer_subnets_v6.setter
    def peer_subnets_v6(self, peer_subnets_v6):
        r"""Sets the peer_subnets_v6 of this ResponseVpnConnection.

        使能ipv6的对端子网

        :param peer_subnets_v6: The peer_subnets_v6 of this ResponseVpnConnection.
        :type peer_subnets_v6: list[str]
        """
        self._peer_subnets_v6 = peer_subnets_v6

    @property
    def policy_rules_v6(self):
        r"""Gets the policy_rules_v6 of this ResponseVpnConnection.

        策略模式的ipv6策略规则组

        :return: The policy_rules_v6 of this ResponseVpnConnection.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        return self._policy_rules_v6

    @policy_rules_v6.setter
    def policy_rules_v6(self, policy_rules_v6):
        r"""Sets the policy_rules_v6 of this ResponseVpnConnection.

        策略模式的ipv6策略规则组

        :param policy_rules_v6: The policy_rules_v6 of this ResponseVpnConnection.
        :type policy_rules_v6: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        self._policy_rules_v6 = policy_rules_v6

    @property
    def bgp_peer(self):
        r"""Gets the bgp_peer of this ResponseVpnConnection.

        :return: The bgp_peer of this ResponseVpnConnection.
        :rtype: :class:`huaweicloudsdkvpn.v5.BgpPeer`
        """
        return self._bgp_peer

    @bgp_peer.setter
    def bgp_peer(self, bgp_peer):
        r"""Sets the bgp_peer of this ResponseVpnConnection.

        :param bgp_peer: The bgp_peer of this ResponseVpnConnection.
        :type bgp_peer: :class:`huaweicloudsdkvpn.v5.BgpPeer`
        """
        self._bgp_peer = bgp_peer

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
        if not isinstance(other, ResponseVpnConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
