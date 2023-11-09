# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpnConnectionRequestBodyContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('psk')

    openapi_types = {
        'name': 'str',
        'vgw_id': 'str',
        'vgw_ip': 'str',
        'style': 'str',
        'cgw_id': 'str',
        'peer_subnets': 'list[str]',
        'tunnel_local_address': 'str',
        'tunnel_peer_address': 'str',
        'enable_nqa': 'bool',
        'psk': 'str',
        'policy_rules': 'list[PolicyRule]',
        'ikepolicy': 'IkePolicy',
        'ipsecpolicy': 'IpsecPolicy',
        'ha_role': 'str'
    }

    attribute_map = {
        'name': 'name',
        'vgw_id': 'vgw_id',
        'vgw_ip': 'vgw_ip',
        'style': 'style',
        'cgw_id': 'cgw_id',
        'peer_subnets': 'peer_subnets',
        'tunnel_local_address': 'tunnel_local_address',
        'tunnel_peer_address': 'tunnel_peer_address',
        'enable_nqa': 'enable_nqa',
        'psk': 'psk',
        'policy_rules': 'policy_rules',
        'ikepolicy': 'ikepolicy',
        'ipsecpolicy': 'ipsecpolicy',
        'ha_role': 'ha_role'
    }

    def __init__(self, name=None, vgw_id=None, vgw_ip=None, style=None, cgw_id=None, peer_subnets=None, tunnel_local_address=None, tunnel_peer_address=None, enable_nqa=None, psk=None, policy_rules=None, ikepolicy=None, ipsecpolicy=None, ha_role=None):
        """CreateVpnConnectionRequestBodyContent

        The model defined in huaweicloud sdk

        :param name: VPN连接名称
        :type name: str
        :param vgw_id: VPN网关ID
        :type vgw_id: str
        :param vgw_ip: VGW IP
        :type vgw_ip: str
        :param style: 连接模式 允许范围[policy, static, bgp] policy: 策略模式 static: 静态路由模式 bgp: bgp路由模式
        :type style: str
        :param cgw_id: 对端网关ID
        :type cgw_id: str
        :param peer_subnets: 对端子网
        :type peer_subnets: list[str]
        :param tunnel_local_address: 本端隧道口地址
        :type tunnel_local_address: str
        :param tunnel_peer_address: 对端隧道口地址
        :type tunnel_peer_address: str
        :param enable_nqa: 开启NQA检测
        :type enable_nqa: bool
        :param psk: 预共享密钥，只能包含大写字母、小写字母、数字和特殊字符(~!@#$%^()-_+&#x3D;{ },./:;)且至少包含四种字符的三种
        :type psk: str
        :param policy_rules: 策略模式的策略规则组
        :type policy_rules: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        :param ikepolicy: 
        :type ikepolicy: :class:`huaweicloudsdkvpn.v5.IkePolicy`
        :param ipsecpolicy: 
        :type ipsecpolicy: :class:`huaweicloudsdkvpn.v5.IpsecPolicy`
        :param ha_role: 连接的HA角色
        :type ha_role: str
        """
        
        

        self._name = None
        self._vgw_id = None
        self._vgw_ip = None
        self._style = None
        self._cgw_id = None
        self._peer_subnets = None
        self._tunnel_local_address = None
        self._tunnel_peer_address = None
        self._enable_nqa = None
        self._psk = None
        self._policy_rules = None
        self._ikepolicy = None
        self._ipsecpolicy = None
        self._ha_role = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.vgw_id = vgw_id
        self.vgw_ip = vgw_ip
        if style is not None:
            self.style = style
        self.cgw_id = cgw_id
        if peer_subnets is not None:
            self.peer_subnets = peer_subnets
        if tunnel_local_address is not None:
            self.tunnel_local_address = tunnel_local_address
        if tunnel_peer_address is not None:
            self.tunnel_peer_address = tunnel_peer_address
        if enable_nqa is not None:
            self.enable_nqa = enable_nqa
        if psk is not None:
            self.psk = psk
        if policy_rules is not None:
            self.policy_rules = policy_rules
        if ikepolicy is not None:
            self.ikepolicy = ikepolicy
        if ipsecpolicy is not None:
            self.ipsecpolicy = ipsecpolicy
        if ha_role is not None:
            self.ha_role = ha_role

    @property
    def name(self):
        """Gets the name of this CreateVpnConnectionRequestBodyContent.

        VPN连接名称

        :return: The name of this CreateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVpnConnectionRequestBodyContent.

        VPN连接名称

        :param name: The name of this CreateVpnConnectionRequestBodyContent.
        :type name: str
        """
        self._name = name

    @property
    def vgw_id(self):
        """Gets the vgw_id of this CreateVpnConnectionRequestBodyContent.

        VPN网关ID

        :return: The vgw_id of this CreateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        """Sets the vgw_id of this CreateVpnConnectionRequestBodyContent.

        VPN网关ID

        :param vgw_id: The vgw_id of this CreateVpnConnectionRequestBodyContent.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def vgw_ip(self):
        """Gets the vgw_ip of this CreateVpnConnectionRequestBodyContent.

        VGW IP

        :return: The vgw_ip of this CreateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._vgw_ip

    @vgw_ip.setter
    def vgw_ip(self, vgw_ip):
        """Sets the vgw_ip of this CreateVpnConnectionRequestBodyContent.

        VGW IP

        :param vgw_ip: The vgw_ip of this CreateVpnConnectionRequestBodyContent.
        :type vgw_ip: str
        """
        self._vgw_ip = vgw_ip

    @property
    def style(self):
        """Gets the style of this CreateVpnConnectionRequestBodyContent.

        连接模式 允许范围[policy, static, bgp] policy: 策略模式 static: 静态路由模式 bgp: bgp路由模式

        :return: The style of this CreateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this CreateVpnConnectionRequestBodyContent.

        连接模式 允许范围[policy, static, bgp] policy: 策略模式 static: 静态路由模式 bgp: bgp路由模式

        :param style: The style of this CreateVpnConnectionRequestBodyContent.
        :type style: str
        """
        self._style = style

    @property
    def cgw_id(self):
        """Gets the cgw_id of this CreateVpnConnectionRequestBodyContent.

        对端网关ID

        :return: The cgw_id of this CreateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._cgw_id

    @cgw_id.setter
    def cgw_id(self, cgw_id):
        """Sets the cgw_id of this CreateVpnConnectionRequestBodyContent.

        对端网关ID

        :param cgw_id: The cgw_id of this CreateVpnConnectionRequestBodyContent.
        :type cgw_id: str
        """
        self._cgw_id = cgw_id

    @property
    def peer_subnets(self):
        """Gets the peer_subnets of this CreateVpnConnectionRequestBodyContent.

        对端子网

        :return: The peer_subnets of this CreateVpnConnectionRequestBodyContent.
        :rtype: list[str]
        """
        return self._peer_subnets

    @peer_subnets.setter
    def peer_subnets(self, peer_subnets):
        """Sets the peer_subnets of this CreateVpnConnectionRequestBodyContent.

        对端子网

        :param peer_subnets: The peer_subnets of this CreateVpnConnectionRequestBodyContent.
        :type peer_subnets: list[str]
        """
        self._peer_subnets = peer_subnets

    @property
    def tunnel_local_address(self):
        """Gets the tunnel_local_address of this CreateVpnConnectionRequestBodyContent.

        本端隧道口地址

        :return: The tunnel_local_address of this CreateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._tunnel_local_address

    @tunnel_local_address.setter
    def tunnel_local_address(self, tunnel_local_address):
        """Sets the tunnel_local_address of this CreateVpnConnectionRequestBodyContent.

        本端隧道口地址

        :param tunnel_local_address: The tunnel_local_address of this CreateVpnConnectionRequestBodyContent.
        :type tunnel_local_address: str
        """
        self._tunnel_local_address = tunnel_local_address

    @property
    def tunnel_peer_address(self):
        """Gets the tunnel_peer_address of this CreateVpnConnectionRequestBodyContent.

        对端隧道口地址

        :return: The tunnel_peer_address of this CreateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._tunnel_peer_address

    @tunnel_peer_address.setter
    def tunnel_peer_address(self, tunnel_peer_address):
        """Sets the tunnel_peer_address of this CreateVpnConnectionRequestBodyContent.

        对端隧道口地址

        :param tunnel_peer_address: The tunnel_peer_address of this CreateVpnConnectionRequestBodyContent.
        :type tunnel_peer_address: str
        """
        self._tunnel_peer_address = tunnel_peer_address

    @property
    def enable_nqa(self):
        """Gets the enable_nqa of this CreateVpnConnectionRequestBodyContent.

        开启NQA检测

        :return: The enable_nqa of this CreateVpnConnectionRequestBodyContent.
        :rtype: bool
        """
        return self._enable_nqa

    @enable_nqa.setter
    def enable_nqa(self, enable_nqa):
        """Sets the enable_nqa of this CreateVpnConnectionRequestBodyContent.

        开启NQA检测

        :param enable_nqa: The enable_nqa of this CreateVpnConnectionRequestBodyContent.
        :type enable_nqa: bool
        """
        self._enable_nqa = enable_nqa

    @property
    def psk(self):
        """Gets the psk of this CreateVpnConnectionRequestBodyContent.

        预共享密钥，只能包含大写字母、小写字母、数字和特殊字符(~!@#$%^()-_+={ },./:;)且至少包含四种字符的三种

        :return: The psk of this CreateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._psk

    @psk.setter
    def psk(self, psk):
        """Sets the psk of this CreateVpnConnectionRequestBodyContent.

        预共享密钥，只能包含大写字母、小写字母、数字和特殊字符(~!@#$%^()-_+={ },./:;)且至少包含四种字符的三种

        :param psk: The psk of this CreateVpnConnectionRequestBodyContent.
        :type psk: str
        """
        self._psk = psk

    @property
    def policy_rules(self):
        """Gets the policy_rules of this CreateVpnConnectionRequestBodyContent.

        策略模式的策略规则组

        :return: The policy_rules of this CreateVpnConnectionRequestBodyContent.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        return self._policy_rules

    @policy_rules.setter
    def policy_rules(self, policy_rules):
        """Sets the policy_rules of this CreateVpnConnectionRequestBodyContent.

        策略模式的策略规则组

        :param policy_rules: The policy_rules of this CreateVpnConnectionRequestBodyContent.
        :type policy_rules: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        self._policy_rules = policy_rules

    @property
    def ikepolicy(self):
        """Gets the ikepolicy of this CreateVpnConnectionRequestBodyContent.

        :return: The ikepolicy of this CreateVpnConnectionRequestBodyContent.
        :rtype: :class:`huaweicloudsdkvpn.v5.IkePolicy`
        """
        return self._ikepolicy

    @ikepolicy.setter
    def ikepolicy(self, ikepolicy):
        """Sets the ikepolicy of this CreateVpnConnectionRequestBodyContent.

        :param ikepolicy: The ikepolicy of this CreateVpnConnectionRequestBodyContent.
        :type ikepolicy: :class:`huaweicloudsdkvpn.v5.IkePolicy`
        """
        self._ikepolicy = ikepolicy

    @property
    def ipsecpolicy(self):
        """Gets the ipsecpolicy of this CreateVpnConnectionRequestBodyContent.

        :return: The ipsecpolicy of this CreateVpnConnectionRequestBodyContent.
        :rtype: :class:`huaweicloudsdkvpn.v5.IpsecPolicy`
        """
        return self._ipsecpolicy

    @ipsecpolicy.setter
    def ipsecpolicy(self, ipsecpolicy):
        """Sets the ipsecpolicy of this CreateVpnConnectionRequestBodyContent.

        :param ipsecpolicy: The ipsecpolicy of this CreateVpnConnectionRequestBodyContent.
        :type ipsecpolicy: :class:`huaweicloudsdkvpn.v5.IpsecPolicy`
        """
        self._ipsecpolicy = ipsecpolicy

    @property
    def ha_role(self):
        """Gets the ha_role of this CreateVpnConnectionRequestBodyContent.

        连接的HA角色

        :return: The ha_role of this CreateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._ha_role

    @ha_role.setter
    def ha_role(self, ha_role):
        """Sets the ha_role of this CreateVpnConnectionRequestBodyContent.

        连接的HA角色

        :param ha_role: The ha_role of this CreateVpnConnectionRequestBodyContent.
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
        if not isinstance(other, CreateVpnConnectionRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
