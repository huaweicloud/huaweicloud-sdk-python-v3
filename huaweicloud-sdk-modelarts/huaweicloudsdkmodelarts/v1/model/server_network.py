# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ipv6_enable': 'bool',
        'roce_id': 'str',
        'security_group_id': 'str',
        'subnet_id': 'str',
        'vpc_id': 'str',
        'hyper_cluster': 'ServerNetworkHyperCluster',
        'allowed_address_pairs': 'list[AllowedAddressPairs]'
    }

    attribute_map = {
        'ipv6_enable': 'ipv6_enable',
        'roce_id': 'roce_id',
        'security_group_id': 'security_group_id',
        'subnet_id': 'subnet_id',
        'vpc_id': 'vpc_id',
        'hyper_cluster': 'hyper_cluster',
        'allowed_address_pairs': 'allowed_address_pairs'
    }

    def __init__(self, ipv6_enable=None, roce_id=None, security_group_id=None, subnet_id=None, vpc_id=None, hyper_cluster=None, allowed_address_pairs=None):
        r"""ServerNetwork

        The model defined in huaweicloud sdk

        :param ipv6_enable: **参数解释**：创建服务器是否启用IPv6。表示在创建服务器时是否启用IPv6支持。 **约束限制**：不涉及。 **取值范围**： - true：启用IPv6 - false：不启用IPv6 **默认取值**：不涉及。
        :type ipv6_enable: bool
        :param roce_id: **参数解释**：服务器RoCE网络ID。表示服务器的RoCE网络ID。 **约束限制**：不涉及。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。
        :type roce_id: str
        :param security_group_id: **参数解释**：服务器所在的安全组ID。表示服务器所属的安全组ID。 **约束限制**：不涉及。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。
        :type security_group_id: str
        :param subnet_id: **参数解释**：服务器所在子网ID。表示服务器所属的子网ID。 **约束限制**：不涉及。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。
        :type subnet_id: str
        :param vpc_id: **参数解释**：服务器所在虚拟私有云ID。表示服务器所属的虚拟私有云ID。 **约束限制**：不涉及。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。
        :type vpc_id: str
        :param hyper_cluster: 
        :type hyper_cluster: :class:`huaweicloudsdkmodelarts.v1.ServerNetworkHyperCluster`
        :param allowed_address_pairs: **参数解释：** IP/Mac对列表。 **约束限制：** - IP地址不允许为 “0.0.0.0/0”。 - 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。 - 如果allowed_address_pairs为“1.1.1.1/0”，表示关闭源目的地址检查开关。 - 如果是虚拟IP绑定云服务器，       则mac_address可为空或者填写被绑定云服务器网卡的Mac地址。       被绑定的云服务器网卡allowed_address_pairs的IP地址填“1.1.1.1/0”。 **取值范围：** 不涉及 **默认取值：** 不涉及\&quot;
        :type allowed_address_pairs: list[:class:`huaweicloudsdkmodelarts.v1.AllowedAddressPairs`]
        """
        
        

        self._ipv6_enable = None
        self._roce_id = None
        self._security_group_id = None
        self._subnet_id = None
        self._vpc_id = None
        self._hyper_cluster = None
        self._allowed_address_pairs = None
        self.discriminator = None

        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if roce_id is not None:
            self.roce_id = roce_id
        self.security_group_id = security_group_id
        self.subnet_id = subnet_id
        self.vpc_id = vpc_id
        if hyper_cluster is not None:
            self.hyper_cluster = hyper_cluster
        if allowed_address_pairs is not None:
            self.allowed_address_pairs = allowed_address_pairs

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this ServerNetwork.

        **参数解释**：创建服务器是否启用IPv6。表示在创建服务器时是否启用IPv6支持。 **约束限制**：不涉及。 **取值范围**： - true：启用IPv6 - false：不启用IPv6 **默认取值**：不涉及。

        :return: The ipv6_enable of this ServerNetwork.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this ServerNetwork.

        **参数解释**：创建服务器是否启用IPv6。表示在创建服务器时是否启用IPv6支持。 **约束限制**：不涉及。 **取值范围**： - true：启用IPv6 - false：不启用IPv6 **默认取值**：不涉及。

        :param ipv6_enable: The ipv6_enable of this ServerNetwork.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def roce_id(self):
        r"""Gets the roce_id of this ServerNetwork.

        **参数解释**：服务器RoCE网络ID。表示服务器的RoCE网络ID。 **约束限制**：不涉及。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。

        :return: The roce_id of this ServerNetwork.
        :rtype: str
        """
        return self._roce_id

    @roce_id.setter
    def roce_id(self, roce_id):
        r"""Sets the roce_id of this ServerNetwork.

        **参数解释**：服务器RoCE网络ID。表示服务器的RoCE网络ID。 **约束限制**：不涉及。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。

        :param roce_id: The roce_id of this ServerNetwork.
        :type roce_id: str
        """
        self._roce_id = roce_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ServerNetwork.

        **参数解释**：服务器所在的安全组ID。表示服务器所属的安全组ID。 **约束限制**：不涉及。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。

        :return: The security_group_id of this ServerNetwork.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ServerNetwork.

        **参数解释**：服务器所在的安全组ID。表示服务器所属的安全组ID。 **约束限制**：不涉及。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。

        :param security_group_id: The security_group_id of this ServerNetwork.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ServerNetwork.

        **参数解释**：服务器所在子网ID。表示服务器所属的子网ID。 **约束限制**：不涉及。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。

        :return: The subnet_id of this ServerNetwork.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ServerNetwork.

        **参数解释**：服务器所在子网ID。表示服务器所属的子网ID。 **约束限制**：不涉及。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。

        :param subnet_id: The subnet_id of this ServerNetwork.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ServerNetwork.

        **参数解释**：服务器所在虚拟私有云ID。表示服务器所属的虚拟私有云ID。 **约束限制**：不涉及。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。

        :return: The vpc_id of this ServerNetwork.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ServerNetwork.

        **参数解释**：服务器所在虚拟私有云ID。表示服务器所属的虚拟私有云ID。 **约束限制**：不涉及。 **取值范围**：必须是UUID格式的字符串。 **默认取值**：不涉及。

        :param vpc_id: The vpc_id of this ServerNetwork.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def hyper_cluster(self):
        r"""Gets the hyper_cluster of this ServerNetwork.

        :return: The hyper_cluster of this ServerNetwork.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServerNetworkHyperCluster`
        """
        return self._hyper_cluster

    @hyper_cluster.setter
    def hyper_cluster(self, hyper_cluster):
        r"""Sets the hyper_cluster of this ServerNetwork.

        :param hyper_cluster: The hyper_cluster of this ServerNetwork.
        :type hyper_cluster: :class:`huaweicloudsdkmodelarts.v1.ServerNetworkHyperCluster`
        """
        self._hyper_cluster = hyper_cluster

    @property
    def allowed_address_pairs(self):
        r"""Gets the allowed_address_pairs of this ServerNetwork.

        **参数解释：** IP/Mac对列表。 **约束限制：** - IP地址不允许为 “0.0.0.0/0”。 - 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。 - 如果allowed_address_pairs为“1.1.1.1/0”，表示关闭源目的地址检查开关。 - 如果是虚拟IP绑定云服务器，       则mac_address可为空或者填写被绑定云服务器网卡的Mac地址。       被绑定的云服务器网卡allowed_address_pairs的IP地址填“1.1.1.1/0”。 **取值范围：** 不涉及 **默认取值：** 不涉及\"

        :return: The allowed_address_pairs of this ServerNetwork.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AllowedAddressPairs`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        r"""Sets the allowed_address_pairs of this ServerNetwork.

        **参数解释：** IP/Mac对列表。 **约束限制：** - IP地址不允许为 “0.0.0.0/0”。 - 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。 - 如果allowed_address_pairs为“1.1.1.1/0”，表示关闭源目的地址检查开关。 - 如果是虚拟IP绑定云服务器，       则mac_address可为空或者填写被绑定云服务器网卡的Mac地址。       被绑定的云服务器网卡allowed_address_pairs的IP地址填“1.1.1.1/0”。 **取值范围：** 不涉及 **默认取值：** 不涉及\"

        :param allowed_address_pairs: The allowed_address_pairs of this ServerNetwork.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkmodelarts.v1.AllowedAddressPairs`]
        """
        self._allowed_address_pairs = allowed_address_pairs

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServerNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
