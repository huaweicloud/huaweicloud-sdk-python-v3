# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronCreateSubnetOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'cidr': 'str',
        'network_id': 'str',
        'gateway_ip': 'str',
        'ip_version': 'int',
        'allocation_pools': 'list[AllocationPool]',
        'dns_nameservers': 'list[str]',
        'host_routes': 'list[HostRoute]',
        'enable_dhcp': 'bool',
        'ipv6_address_mode': 'str',
        'ipv6_ra_mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cidr': 'cidr',
        'network_id': 'network_id',
        'gateway_ip': 'gateway_ip',
        'ip_version': 'ip_version',
        'allocation_pools': 'allocation_pools',
        'dns_nameservers': 'dns_nameservers',
        'host_routes': 'host_routes',
        'enable_dhcp': 'enable_dhcp',
        'ipv6_address_mode': 'ipv6_address_mode',
        'ipv6_ra_mode': 'ipv6_ra_mode'
    }

    def __init__(self, name=None, cidr=None, network_id=None, gateway_ip=None, ip_version=None, allocation_pools=None, dns_nameservers=None, host_routes=None, enable_dhcp=None, ipv6_address_mode=None, ipv6_ra_mode=None):
        """NeutronCreateSubnetOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：子网的名称 取值范围：0-255个字符
        :type name: str
        :param cidr: 功能说明：子网网段 取值范围：必须是cidr格式，只支持10.0.0.0/8,172.16.0.0/12,192.168.0.0/16三个网段内的地址，掩码长度不能大于28
        :type cidr: str
        :param network_id: 功能说明：子网所属网络ID
        :type network_id: str
        :param gateway_ip: 功能说明：子网网关 取值范围：子网网段中的IP地址 约束：必须是ip格式
        :type gateway_ip: str
        :param ip_version: 功能说明：IP版本信息 取值范围：4或者6(特定局点)
        :type ip_version: int
        :param allocation_pools: 功能说明：可用的IP池，allocation_pool对象参见allocation_pool对象 例如：[ { \&quot;start\&quot;: \&quot;10.0.0.2\&quot;, \&quot;end\&quot;: \&quot;10.0.0.251\&quot;} ]每个子网的第1个和最后4个IP地址为系统保留地址。以192.168.1.0/24为例，192.168.1.0、 192.168.1.252、192.168.1.253、192.168.1.254和192.168.1.255这些地址是系统保留地址。系统预留地址默认不在allocation_pool范围内。 约束：更新时allocation_pool范围不能包含网关和广播地址的所有IP。
        :type allocation_pools: list[:class:`huaweicloudsdkvpc.v2.AllocationPool`]
        :param dns_nameservers: 功能说明：子网关联的DNS名称服务器列表 取值范围：IP地址格式例如：\&quot;dns_nameservers\&quot;: [\&quot;8.xx.xx.8\&quot;,\&quot;8.xx.xx.4\&quot;] 默认值：不填时为空，无法使用云内网DNS功能 [内网DNS地址请参见](https://support.huaweicloud.com/dns_faq/dns_faq_002.html) [通过API获取请参见](https://support.huaweicloud.com/api-dns/dns_api_69001.html)
        :type dns_nameservers: list[str]
        :param host_routes: 功能说明：虚拟机静态路由，参见“host_route对象”表 约束：不支持设置
        :type host_routes: list[:class:`huaweicloudsdkvpc.v2.HostRoute`]
        :param enable_dhcp: 功能说明：是否启动dhcp，false表示不提供dhcp服务的能力 约束：只支持true
        :type enable_dhcp: bool
        :param ipv6_address_mode: 功能说明：IPv6寻址模式 取值范围：dhcpv6-stateful
        :type ipv6_address_mode: str
        :param ipv6_ra_mode: 功能说明：IPv6路由广播模式 取值范围：dhcpv6-stateful
        :type ipv6_ra_mode: str
        """
        
        

        self._name = None
        self._cidr = None
        self._network_id = None
        self._gateway_ip = None
        self._ip_version = None
        self._allocation_pools = None
        self._dns_nameservers = None
        self._host_routes = None
        self._enable_dhcp = None
        self._ipv6_address_mode = None
        self._ipv6_ra_mode = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.cidr = cidr
        self.network_id = network_id
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip
        if ip_version is not None:
            self.ip_version = ip_version
        if allocation_pools is not None:
            self.allocation_pools = allocation_pools
        if dns_nameservers is not None:
            self.dns_nameservers = dns_nameservers
        if host_routes is not None:
            self.host_routes = host_routes
        if enable_dhcp is not None:
            self.enable_dhcp = enable_dhcp
        if ipv6_address_mode is not None:
            self.ipv6_address_mode = ipv6_address_mode
        if ipv6_ra_mode is not None:
            self.ipv6_ra_mode = ipv6_ra_mode

    @property
    def name(self):
        """Gets the name of this NeutronCreateSubnetOption.

        功能说明：子网的名称 取值范围：0-255个字符

        :return: The name of this NeutronCreateSubnetOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronCreateSubnetOption.

        功能说明：子网的名称 取值范围：0-255个字符

        :param name: The name of this NeutronCreateSubnetOption.
        :type name: str
        """
        self._name = name

    @property
    def cidr(self):
        """Gets the cidr of this NeutronCreateSubnetOption.

        功能说明：子网网段 取值范围：必须是cidr格式，只支持10.0.0.0/8,172.16.0.0/12,192.168.0.0/16三个网段内的地址，掩码长度不能大于28

        :return: The cidr of this NeutronCreateSubnetOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this NeutronCreateSubnetOption.

        功能说明：子网网段 取值范围：必须是cidr格式，只支持10.0.0.0/8,172.16.0.0/12,192.168.0.0/16三个网段内的地址，掩码长度不能大于28

        :param cidr: The cidr of this NeutronCreateSubnetOption.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def network_id(self):
        """Gets the network_id of this NeutronCreateSubnetOption.

        功能说明：子网所属网络ID

        :return: The network_id of this NeutronCreateSubnetOption.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this NeutronCreateSubnetOption.

        功能说明：子网所属网络ID

        :param network_id: The network_id of this NeutronCreateSubnetOption.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this NeutronCreateSubnetOption.

        功能说明：子网网关 取值范围：子网网段中的IP地址 约束：必须是ip格式

        :return: The gateway_ip of this NeutronCreateSubnetOption.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this NeutronCreateSubnetOption.

        功能说明：子网网关 取值范围：子网网段中的IP地址 约束：必须是ip格式

        :param gateway_ip: The gateway_ip of this NeutronCreateSubnetOption.
        :type gateway_ip: str
        """
        self._gateway_ip = gateway_ip

    @property
    def ip_version(self):
        """Gets the ip_version of this NeutronCreateSubnetOption.

        功能说明：IP版本信息 取值范围：4或者6(特定局点)

        :return: The ip_version of this NeutronCreateSubnetOption.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this NeutronCreateSubnetOption.

        功能说明：IP版本信息 取值范围：4或者6(特定局点)

        :param ip_version: The ip_version of this NeutronCreateSubnetOption.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def allocation_pools(self):
        """Gets the allocation_pools of this NeutronCreateSubnetOption.

        功能说明：可用的IP池，allocation_pool对象参见allocation_pool对象 例如：[ { \"start\": \"10.0.0.2\", \"end\": \"10.0.0.251\"} ]每个子网的第1个和最后4个IP地址为系统保留地址。以192.168.1.0/24为例，192.168.1.0、 192.168.1.252、192.168.1.253、192.168.1.254和192.168.1.255这些地址是系统保留地址。系统预留地址默认不在allocation_pool范围内。 约束：更新时allocation_pool范围不能包含网关和广播地址的所有IP。

        :return: The allocation_pools of this NeutronCreateSubnetOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.AllocationPool`]
        """
        return self._allocation_pools

    @allocation_pools.setter
    def allocation_pools(self, allocation_pools):
        """Sets the allocation_pools of this NeutronCreateSubnetOption.

        功能说明：可用的IP池，allocation_pool对象参见allocation_pool对象 例如：[ { \"start\": \"10.0.0.2\", \"end\": \"10.0.0.251\"} ]每个子网的第1个和最后4个IP地址为系统保留地址。以192.168.1.0/24为例，192.168.1.0、 192.168.1.252、192.168.1.253、192.168.1.254和192.168.1.255这些地址是系统保留地址。系统预留地址默认不在allocation_pool范围内。 约束：更新时allocation_pool范围不能包含网关和广播地址的所有IP。

        :param allocation_pools: The allocation_pools of this NeutronCreateSubnetOption.
        :type allocation_pools: list[:class:`huaweicloudsdkvpc.v2.AllocationPool`]
        """
        self._allocation_pools = allocation_pools

    @property
    def dns_nameservers(self):
        """Gets the dns_nameservers of this NeutronCreateSubnetOption.

        功能说明：子网关联的DNS名称服务器列表 取值范围：IP地址格式例如：\"dns_nameservers\": [\"8.xx.xx.8\",\"8.xx.xx.4\"] 默认值：不填时为空，无法使用云内网DNS功能 [内网DNS地址请参见](https://support.huaweicloud.com/dns_faq/dns_faq_002.html) [通过API获取请参见](https://support.huaweicloud.com/api-dns/dns_api_69001.html)

        :return: The dns_nameservers of this NeutronCreateSubnetOption.
        :rtype: list[str]
        """
        return self._dns_nameservers

    @dns_nameservers.setter
    def dns_nameservers(self, dns_nameservers):
        """Sets the dns_nameservers of this NeutronCreateSubnetOption.

        功能说明：子网关联的DNS名称服务器列表 取值范围：IP地址格式例如：\"dns_nameservers\": [\"8.xx.xx.8\",\"8.xx.xx.4\"] 默认值：不填时为空，无法使用云内网DNS功能 [内网DNS地址请参见](https://support.huaweicloud.com/dns_faq/dns_faq_002.html) [通过API获取请参见](https://support.huaweicloud.com/api-dns/dns_api_69001.html)

        :param dns_nameservers: The dns_nameservers of this NeutronCreateSubnetOption.
        :type dns_nameservers: list[str]
        """
        self._dns_nameservers = dns_nameservers

    @property
    def host_routes(self):
        """Gets the host_routes of this NeutronCreateSubnetOption.

        功能说明：虚拟机静态路由，参见“host_route对象”表 约束：不支持设置

        :return: The host_routes of this NeutronCreateSubnetOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.HostRoute`]
        """
        return self._host_routes

    @host_routes.setter
    def host_routes(self, host_routes):
        """Sets the host_routes of this NeutronCreateSubnetOption.

        功能说明：虚拟机静态路由，参见“host_route对象”表 约束：不支持设置

        :param host_routes: The host_routes of this NeutronCreateSubnetOption.
        :type host_routes: list[:class:`huaweicloudsdkvpc.v2.HostRoute`]
        """
        self._host_routes = host_routes

    @property
    def enable_dhcp(self):
        """Gets the enable_dhcp of this NeutronCreateSubnetOption.

        功能说明：是否启动dhcp，false表示不提供dhcp服务的能力 约束：只支持true

        :return: The enable_dhcp of this NeutronCreateSubnetOption.
        :rtype: bool
        """
        return self._enable_dhcp

    @enable_dhcp.setter
    def enable_dhcp(self, enable_dhcp):
        """Sets the enable_dhcp of this NeutronCreateSubnetOption.

        功能说明：是否启动dhcp，false表示不提供dhcp服务的能力 约束：只支持true

        :param enable_dhcp: The enable_dhcp of this NeutronCreateSubnetOption.
        :type enable_dhcp: bool
        """
        self._enable_dhcp = enable_dhcp

    @property
    def ipv6_address_mode(self):
        """Gets the ipv6_address_mode of this NeutronCreateSubnetOption.

        功能说明：IPv6寻址模式 取值范围：dhcpv6-stateful

        :return: The ipv6_address_mode of this NeutronCreateSubnetOption.
        :rtype: str
        """
        return self._ipv6_address_mode

    @ipv6_address_mode.setter
    def ipv6_address_mode(self, ipv6_address_mode):
        """Sets the ipv6_address_mode of this NeutronCreateSubnetOption.

        功能说明：IPv6寻址模式 取值范围：dhcpv6-stateful

        :param ipv6_address_mode: The ipv6_address_mode of this NeutronCreateSubnetOption.
        :type ipv6_address_mode: str
        """
        self._ipv6_address_mode = ipv6_address_mode

    @property
    def ipv6_ra_mode(self):
        """Gets the ipv6_ra_mode of this NeutronCreateSubnetOption.

        功能说明：IPv6路由广播模式 取值范围：dhcpv6-stateful

        :return: The ipv6_ra_mode of this NeutronCreateSubnetOption.
        :rtype: str
        """
        return self._ipv6_ra_mode

    @ipv6_ra_mode.setter
    def ipv6_ra_mode(self, ipv6_ra_mode):
        """Sets the ipv6_ra_mode of this NeutronCreateSubnetOption.

        功能说明：IPv6路由广播模式 取值范围：dhcpv6-stateful

        :param ipv6_ra_mode: The ipv6_ra_mode of this NeutronCreateSubnetOption.
        :type ipv6_ra_mode: str
        """
        self._ipv6_ra_mode = ipv6_ra_mode

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
        if not isinstance(other, NeutronCreateSubnetOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
