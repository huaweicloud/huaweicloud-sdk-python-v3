# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubnetCidr:

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
        'ip_version': 'str',
        'cidr': 'str',
        'gateway_ip': 'str',
        'enable_dhcp': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'ip_version': 'ip_version',
        'cidr': 'cidr',
        'gateway_ip': 'gateway_ip',
        'enable_dhcp': 'enable_dhcp'
    }

    def __init__(self, id=None, ip_version=None, cidr=None, gateway_ip=None, enable_dhcp=None):
        r"""SubnetCidr

        The model defined in huaweicloud sdk

        :param id: **参数解释**： OpenStack Neutron子网的资源ID。 **取值范围**： 带“-”的标准UUID格式。
        :type id: str
        :param ip_version: **参数解释**： OpenStack Neutron子网的IP版本。 **取值范围**： - 4：IPv4子网。 - 6：IPv6子网。
        :type ip_version: str
        :param cidr: **参数解释**： OpenStack Neutron子网的IP网段。 **取值范围**： CIDR格式，如IPv4网段：192.168.23.0/24，IPv6网段：2420:2023:410:d5d::/64。
        :type cidr: str
        :param gateway_ip: **参数解释**： OpenStack Neutron子网的网关IP地址。 **取值范围**： 不涉及。
        :type gateway_ip: str
        :param enable_dhcp: **参数解释**： OpenStack Neutron子网是否开启DHCP功能。 **取值范围**： - true：开启DHCP功能。 - false：未开启DHCP功能。
        :type enable_dhcp: bool
        """
        
        

        self._id = None
        self._ip_version = None
        self._cidr = None
        self._gateway_ip = None
        self._enable_dhcp = None
        self.discriminator = None

        self.id = id
        self.ip_version = ip_version
        self.cidr = cidr
        self.gateway_ip = gateway_ip
        self.enable_dhcp = enable_dhcp

    @property
    def id(self):
        r"""Gets the id of this SubnetCidr.

        **参数解释**： OpenStack Neutron子网的资源ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The id of this SubnetCidr.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SubnetCidr.

        **参数解释**： OpenStack Neutron子网的资源ID。 **取值范围**： 带“-”的标准UUID格式。

        :param id: The id of this SubnetCidr.
        :type id: str
        """
        self._id = id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this SubnetCidr.

        **参数解释**： OpenStack Neutron子网的IP版本。 **取值范围**： - 4：IPv4子网。 - 6：IPv6子网。

        :return: The ip_version of this SubnetCidr.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this SubnetCidr.

        **参数解释**： OpenStack Neutron子网的IP版本。 **取值范围**： - 4：IPv4子网。 - 6：IPv6子网。

        :param ip_version: The ip_version of this SubnetCidr.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def cidr(self):
        r"""Gets the cidr of this SubnetCidr.

        **参数解释**： OpenStack Neutron子网的IP网段。 **取值范围**： CIDR格式，如IPv4网段：192.168.23.0/24，IPv6网段：2420:2023:410:d5d::/64。

        :return: The cidr of this SubnetCidr.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this SubnetCidr.

        **参数解释**： OpenStack Neutron子网的IP网段。 **取值范围**： CIDR格式，如IPv4网段：192.168.23.0/24，IPv6网段：2420:2023:410:d5d::/64。

        :param cidr: The cidr of this SubnetCidr.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def gateway_ip(self):
        r"""Gets the gateway_ip of this SubnetCidr.

        **参数解释**： OpenStack Neutron子网的网关IP地址。 **取值范围**： 不涉及。

        :return: The gateway_ip of this SubnetCidr.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        r"""Sets the gateway_ip of this SubnetCidr.

        **参数解释**： OpenStack Neutron子网的网关IP地址。 **取值范围**： 不涉及。

        :param gateway_ip: The gateway_ip of this SubnetCidr.
        :type gateway_ip: str
        """
        self._gateway_ip = gateway_ip

    @property
    def enable_dhcp(self):
        r"""Gets the enable_dhcp of this SubnetCidr.

        **参数解释**： OpenStack Neutron子网是否开启DHCP功能。 **取值范围**： - true：开启DHCP功能。 - false：未开启DHCP功能。

        :return: The enable_dhcp of this SubnetCidr.
        :rtype: bool
        """
        return self._enable_dhcp

    @enable_dhcp.setter
    def enable_dhcp(self, enable_dhcp):
        r"""Sets the enable_dhcp of this SubnetCidr.

        **参数解释**： OpenStack Neutron子网是否开启DHCP功能。 **取值范围**： - true：开启DHCP功能。 - false：未开启DHCP功能。

        :param enable_dhcp: The enable_dhcp of this SubnetCidr.
        :type enable_dhcp: bool
        """
        self._enable_dhcp = enable_dhcp

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
        if not isinstance(other, SubnetCidr):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
