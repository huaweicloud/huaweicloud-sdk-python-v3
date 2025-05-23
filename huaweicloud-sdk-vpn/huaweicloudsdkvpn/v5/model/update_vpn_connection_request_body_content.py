# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpnConnectionRequestBodyContent:

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
        'cgw_id': 'str',
        'peer_subnets': 'list[str]',
        'tunnel_local_address': 'str',
        'tunnel_peer_address': 'str',
        'enable_hub': 'bool',
        'psk': 'str',
        'policy_rules': 'list[PolicyRule]',
        'ikepolicy': 'UpdateIkePolicy',
        'ipsecpolicy': 'UpdateIpsecPolicy',
        'peer_subnets_v6': 'list[str]',
        'policy_rules_v6': 'list[PolicyRule]'
    }

    attribute_map = {
        'name': 'name',
        'cgw_id': 'cgw_id',
        'peer_subnets': 'peer_subnets',
        'tunnel_local_address': 'tunnel_local_address',
        'tunnel_peer_address': 'tunnel_peer_address',
        'enable_hub': 'enable_hub',
        'psk': 'psk',
        'policy_rules': 'policy_rules',
        'ikepolicy': 'ikepolicy',
        'ipsecpolicy': 'ipsecpolicy',
        'peer_subnets_v6': 'peer_subnets_v6',
        'policy_rules_v6': 'policy_rules_v6'
    }

    def __init__(self, name=None, cgw_id=None, peer_subnets=None, tunnel_local_address=None, tunnel_peer_address=None, enable_hub=None, psk=None, policy_rules=None, ikepolicy=None, ipsecpolicy=None, peer_subnets_v6=None, policy_rules_v6=None):
        r"""UpdateVpnConnectionRequestBodyContent

        The model defined in huaweicloud sdk

        :param name: VPN连接名称
        :type name: str
        :param cgw_id: 对端网关ID
        :type cgw_id: str
        :param peer_subnets: 对端网段
        :type peer_subnets: list[str]
        :param tunnel_local_address: 本端隧道口地址
        :type tunnel_local_address: str
        :param tunnel_peer_address: 对端隧道口地址
        :type tunnel_peer_address: str
        :param enable_hub: 开启分支互联
        :type enable_hub: bool
        :param psk: 预共享密钥，只能包含大写字母、小写字母、数字和特殊字符(~!@#$%^()-_+&#x3D;{ },./:;)且至少包含四种字符的三种
        :type psk: str
        :param policy_rules: 策略模式的策略规则组
        :type policy_rules: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        :param ikepolicy: 
        :type ikepolicy: :class:`huaweicloudsdkvpn.v5.UpdateIkePolicy`
        :param ipsecpolicy: 
        :type ipsecpolicy: :class:`huaweicloudsdkvpn.v5.UpdateIpsecPolicy`
        :param peer_subnets_v6: 使能ipv6的对端子网
        :type peer_subnets_v6: list[str]
        :param policy_rules_v6: 策略模式的ipv6策略规则组
        :type policy_rules_v6: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        
        

        self._name = None
        self._cgw_id = None
        self._peer_subnets = None
        self._tunnel_local_address = None
        self._tunnel_peer_address = None
        self._enable_hub = None
        self._psk = None
        self._policy_rules = None
        self._ikepolicy = None
        self._ipsecpolicy = None
        self._peer_subnets_v6 = None
        self._policy_rules_v6 = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if cgw_id is not None:
            self.cgw_id = cgw_id
        if peer_subnets is not None:
            self.peer_subnets = peer_subnets
        if tunnel_local_address is not None:
            self.tunnel_local_address = tunnel_local_address
        if tunnel_peer_address is not None:
            self.tunnel_peer_address = tunnel_peer_address
        if enable_hub is not None:
            self.enable_hub = enable_hub
        if psk is not None:
            self.psk = psk
        if policy_rules is not None:
            self.policy_rules = policy_rules
        if ikepolicy is not None:
            self.ikepolicy = ikepolicy
        if ipsecpolicy is not None:
            self.ipsecpolicy = ipsecpolicy
        if peer_subnets_v6 is not None:
            self.peer_subnets_v6 = peer_subnets_v6
        if policy_rules_v6 is not None:
            self.policy_rules_v6 = policy_rules_v6

    @property
    def name(self):
        r"""Gets the name of this UpdateVpnConnectionRequestBodyContent.

        VPN连接名称

        :return: The name of this UpdateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateVpnConnectionRequestBodyContent.

        VPN连接名称

        :param name: The name of this UpdateVpnConnectionRequestBodyContent.
        :type name: str
        """
        self._name = name

    @property
    def cgw_id(self):
        r"""Gets the cgw_id of this UpdateVpnConnectionRequestBodyContent.

        对端网关ID

        :return: The cgw_id of this UpdateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._cgw_id

    @cgw_id.setter
    def cgw_id(self, cgw_id):
        r"""Sets the cgw_id of this UpdateVpnConnectionRequestBodyContent.

        对端网关ID

        :param cgw_id: The cgw_id of this UpdateVpnConnectionRequestBodyContent.
        :type cgw_id: str
        """
        self._cgw_id = cgw_id

    @property
    def peer_subnets(self):
        r"""Gets the peer_subnets of this UpdateVpnConnectionRequestBodyContent.

        对端网段

        :return: The peer_subnets of this UpdateVpnConnectionRequestBodyContent.
        :rtype: list[str]
        """
        return self._peer_subnets

    @peer_subnets.setter
    def peer_subnets(self, peer_subnets):
        r"""Sets the peer_subnets of this UpdateVpnConnectionRequestBodyContent.

        对端网段

        :param peer_subnets: The peer_subnets of this UpdateVpnConnectionRequestBodyContent.
        :type peer_subnets: list[str]
        """
        self._peer_subnets = peer_subnets

    @property
    def tunnel_local_address(self):
        r"""Gets the tunnel_local_address of this UpdateVpnConnectionRequestBodyContent.

        本端隧道口地址

        :return: The tunnel_local_address of this UpdateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._tunnel_local_address

    @tunnel_local_address.setter
    def tunnel_local_address(self, tunnel_local_address):
        r"""Sets the tunnel_local_address of this UpdateVpnConnectionRequestBodyContent.

        本端隧道口地址

        :param tunnel_local_address: The tunnel_local_address of this UpdateVpnConnectionRequestBodyContent.
        :type tunnel_local_address: str
        """
        self._tunnel_local_address = tunnel_local_address

    @property
    def tunnel_peer_address(self):
        r"""Gets the tunnel_peer_address of this UpdateVpnConnectionRequestBodyContent.

        对端隧道口地址

        :return: The tunnel_peer_address of this UpdateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._tunnel_peer_address

    @tunnel_peer_address.setter
    def tunnel_peer_address(self, tunnel_peer_address):
        r"""Sets the tunnel_peer_address of this UpdateVpnConnectionRequestBodyContent.

        对端隧道口地址

        :param tunnel_peer_address: The tunnel_peer_address of this UpdateVpnConnectionRequestBodyContent.
        :type tunnel_peer_address: str
        """
        self._tunnel_peer_address = tunnel_peer_address

    @property
    def enable_hub(self):
        r"""Gets the enable_hub of this UpdateVpnConnectionRequestBodyContent.

        开启分支互联

        :return: The enable_hub of this UpdateVpnConnectionRequestBodyContent.
        :rtype: bool
        """
        return self._enable_hub

    @enable_hub.setter
    def enable_hub(self, enable_hub):
        r"""Sets the enable_hub of this UpdateVpnConnectionRequestBodyContent.

        开启分支互联

        :param enable_hub: The enable_hub of this UpdateVpnConnectionRequestBodyContent.
        :type enable_hub: bool
        """
        self._enable_hub = enable_hub

    @property
    def psk(self):
        r"""Gets the psk of this UpdateVpnConnectionRequestBodyContent.

        预共享密钥，只能包含大写字母、小写字母、数字和特殊字符(~!@#$%^()-_+={ },./:;)且至少包含四种字符的三种

        :return: The psk of this UpdateVpnConnectionRequestBodyContent.
        :rtype: str
        """
        return self._psk

    @psk.setter
    def psk(self, psk):
        r"""Sets the psk of this UpdateVpnConnectionRequestBodyContent.

        预共享密钥，只能包含大写字母、小写字母、数字和特殊字符(~!@#$%^()-_+={ },./:;)且至少包含四种字符的三种

        :param psk: The psk of this UpdateVpnConnectionRequestBodyContent.
        :type psk: str
        """
        self._psk = psk

    @property
    def policy_rules(self):
        r"""Gets the policy_rules of this UpdateVpnConnectionRequestBodyContent.

        策略模式的策略规则组

        :return: The policy_rules of this UpdateVpnConnectionRequestBodyContent.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        return self._policy_rules

    @policy_rules.setter
    def policy_rules(self, policy_rules):
        r"""Sets the policy_rules of this UpdateVpnConnectionRequestBodyContent.

        策略模式的策略规则组

        :param policy_rules: The policy_rules of this UpdateVpnConnectionRequestBodyContent.
        :type policy_rules: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        self._policy_rules = policy_rules

    @property
    def ikepolicy(self):
        r"""Gets the ikepolicy of this UpdateVpnConnectionRequestBodyContent.

        :return: The ikepolicy of this UpdateVpnConnectionRequestBodyContent.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateIkePolicy`
        """
        return self._ikepolicy

    @ikepolicy.setter
    def ikepolicy(self, ikepolicy):
        r"""Sets the ikepolicy of this UpdateVpnConnectionRequestBodyContent.

        :param ikepolicy: The ikepolicy of this UpdateVpnConnectionRequestBodyContent.
        :type ikepolicy: :class:`huaweicloudsdkvpn.v5.UpdateIkePolicy`
        """
        self._ikepolicy = ikepolicy

    @property
    def ipsecpolicy(self):
        r"""Gets the ipsecpolicy of this UpdateVpnConnectionRequestBodyContent.

        :return: The ipsecpolicy of this UpdateVpnConnectionRequestBodyContent.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateIpsecPolicy`
        """
        return self._ipsecpolicy

    @ipsecpolicy.setter
    def ipsecpolicy(self, ipsecpolicy):
        r"""Sets the ipsecpolicy of this UpdateVpnConnectionRequestBodyContent.

        :param ipsecpolicy: The ipsecpolicy of this UpdateVpnConnectionRequestBodyContent.
        :type ipsecpolicy: :class:`huaweicloudsdkvpn.v5.UpdateIpsecPolicy`
        """
        self._ipsecpolicy = ipsecpolicy

    @property
    def peer_subnets_v6(self):
        r"""Gets the peer_subnets_v6 of this UpdateVpnConnectionRequestBodyContent.

        使能ipv6的对端子网

        :return: The peer_subnets_v6 of this UpdateVpnConnectionRequestBodyContent.
        :rtype: list[str]
        """
        return self._peer_subnets_v6

    @peer_subnets_v6.setter
    def peer_subnets_v6(self, peer_subnets_v6):
        r"""Sets the peer_subnets_v6 of this UpdateVpnConnectionRequestBodyContent.

        使能ipv6的对端子网

        :param peer_subnets_v6: The peer_subnets_v6 of this UpdateVpnConnectionRequestBodyContent.
        :type peer_subnets_v6: list[str]
        """
        self._peer_subnets_v6 = peer_subnets_v6

    @property
    def policy_rules_v6(self):
        r"""Gets the policy_rules_v6 of this UpdateVpnConnectionRequestBodyContent.

        策略模式的ipv6策略规则组

        :return: The policy_rules_v6 of this UpdateVpnConnectionRequestBodyContent.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        return self._policy_rules_v6

    @policy_rules_v6.setter
    def policy_rules_v6(self, policy_rules_v6):
        r"""Sets the policy_rules_v6 of this UpdateVpnConnectionRequestBodyContent.

        策略模式的ipv6策略规则组

        :param policy_rules_v6: The policy_rules_v6 of this UpdateVpnConnectionRequestBodyContent.
        :type policy_rules_v6: list[:class:`huaweicloudsdkvpn.v5.PolicyRule`]
        """
        self._policy_rules_v6 = policy_rules_v6

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
        if not isinstance(other, UpdateVpnConnectionRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
