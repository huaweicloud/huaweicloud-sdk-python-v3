# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronUpdateSubnetOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dns_nameservers': 'list[str]',
        'enable_dhcp': 'bool',
        'host_routes': 'list[HostRoute]',
        'name': 'str',
        'allocation_pools': 'list[AllocationPool]'
    }

    attribute_map = {
        'dns_nameservers': 'dns_nameservers',
        'enable_dhcp': 'enable_dhcp',
        'host_routes': 'host_routes',
        'name': 'name',
        'allocation_pools': 'allocation_pools'
    }

    def __init__(self, dns_nameservers=None, enable_dhcp=None, host_routes=None, name=None, allocation_pools=None):
        """NeutronUpdateSubnetOption

        The model defined in huaweicloud sdk

        :param dns_nameservers: 功能说明：dns服务器 取值范围：IP地址格式例如：\&quot;dns_nameservers\&quot;: [\&quot;8.xx.xx.8\&quot;,\&quot;8.xx.xx.4\&quot;]，最多5个 默认值：不填时为空，无法使用云内网DNS功能 [内网DNS地址请参见](https://support.huaweicloud.com/dns_faq/dns_faq_002.html) [通过API获取请参见](https://support.huaweicloud.com/api-dns/dns_api_69001.html)
        :type dns_nameservers: list[str]
        :param enable_dhcp: 功能说明：是否启动dhcp，false表示不提供dhcp服务的能力 约束：只支持true
        :type enable_dhcp: bool
        :param host_routes: 功能说明：虚拟机静态路由，参见“host_route对象”表 约束：不支持，忽略输入信息
        :type host_routes: list[:class:`huaweicloudsdkvpc.v2.HostRoute`]
        :param name: 子网的名称
        :type name: str
        :param allocation_pools: 功能说明：可用的IP池，allocation_pool对象参见表 allocation_pool对象 例如：[ { \&quot;start\&quot;: \&quot;10.0.0.2\&quot;, \&quot;end\&quot;: \&quot;10.0.0.251\&quot;} ]每个子网的第1个和最后3个IP地址为系统保留地址。以192.168.1.0/24为例，192.168.1.0、 192.168.1.253、192.168.1.254和192.168.1.255这些地址是系统保留地址。系统预留地址默认不在allocation_pool范围内。 约束：更新时allocation_pool范围不能包含网关和广播地址的所有IP。
        :type allocation_pools: list[:class:`huaweicloudsdkvpc.v2.AllocationPool`]
        """
        
        

        self._dns_nameservers = None
        self._enable_dhcp = None
        self._host_routes = None
        self._name = None
        self._allocation_pools = None
        self.discriminator = None

        if dns_nameservers is not None:
            self.dns_nameservers = dns_nameservers
        if enable_dhcp is not None:
            self.enable_dhcp = enable_dhcp
        if host_routes is not None:
            self.host_routes = host_routes
        if name is not None:
            self.name = name
        if allocation_pools is not None:
            self.allocation_pools = allocation_pools

    @property
    def dns_nameservers(self):
        """Gets the dns_nameservers of this NeutronUpdateSubnetOption.

        功能说明：dns服务器 取值范围：IP地址格式例如：\"dns_nameservers\": [\"8.xx.xx.8\",\"8.xx.xx.4\"]，最多5个 默认值：不填时为空，无法使用云内网DNS功能 [内网DNS地址请参见](https://support.huaweicloud.com/dns_faq/dns_faq_002.html) [通过API获取请参见](https://support.huaweicloud.com/api-dns/dns_api_69001.html)

        :return: The dns_nameservers of this NeutronUpdateSubnetOption.
        :rtype: list[str]
        """
        return self._dns_nameservers

    @dns_nameservers.setter
    def dns_nameservers(self, dns_nameservers):
        """Sets the dns_nameservers of this NeutronUpdateSubnetOption.

        功能说明：dns服务器 取值范围：IP地址格式例如：\"dns_nameservers\": [\"8.xx.xx.8\",\"8.xx.xx.4\"]，最多5个 默认值：不填时为空，无法使用云内网DNS功能 [内网DNS地址请参见](https://support.huaweicloud.com/dns_faq/dns_faq_002.html) [通过API获取请参见](https://support.huaweicloud.com/api-dns/dns_api_69001.html)

        :param dns_nameservers: The dns_nameservers of this NeutronUpdateSubnetOption.
        :type dns_nameservers: list[str]
        """
        self._dns_nameservers = dns_nameservers

    @property
    def enable_dhcp(self):
        """Gets the enable_dhcp of this NeutronUpdateSubnetOption.

        功能说明：是否启动dhcp，false表示不提供dhcp服务的能力 约束：只支持true

        :return: The enable_dhcp of this NeutronUpdateSubnetOption.
        :rtype: bool
        """
        return self._enable_dhcp

    @enable_dhcp.setter
    def enable_dhcp(self, enable_dhcp):
        """Sets the enable_dhcp of this NeutronUpdateSubnetOption.

        功能说明：是否启动dhcp，false表示不提供dhcp服务的能力 约束：只支持true

        :param enable_dhcp: The enable_dhcp of this NeutronUpdateSubnetOption.
        :type enable_dhcp: bool
        """
        self._enable_dhcp = enable_dhcp

    @property
    def host_routes(self):
        """Gets the host_routes of this NeutronUpdateSubnetOption.

        功能说明：虚拟机静态路由，参见“host_route对象”表 约束：不支持，忽略输入信息

        :return: The host_routes of this NeutronUpdateSubnetOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.HostRoute`]
        """
        return self._host_routes

    @host_routes.setter
    def host_routes(self, host_routes):
        """Sets the host_routes of this NeutronUpdateSubnetOption.

        功能说明：虚拟机静态路由，参见“host_route对象”表 约束：不支持，忽略输入信息

        :param host_routes: The host_routes of this NeutronUpdateSubnetOption.
        :type host_routes: list[:class:`huaweicloudsdkvpc.v2.HostRoute`]
        """
        self._host_routes = host_routes

    @property
    def name(self):
        """Gets the name of this NeutronUpdateSubnetOption.

        子网的名称

        :return: The name of this NeutronUpdateSubnetOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronUpdateSubnetOption.

        子网的名称

        :param name: The name of this NeutronUpdateSubnetOption.
        :type name: str
        """
        self._name = name

    @property
    def allocation_pools(self):
        """Gets the allocation_pools of this NeutronUpdateSubnetOption.

        功能说明：可用的IP池，allocation_pool对象参见表 allocation_pool对象 例如：[ { \"start\": \"10.0.0.2\", \"end\": \"10.0.0.251\"} ]每个子网的第1个和最后3个IP地址为系统保留地址。以192.168.1.0/24为例，192.168.1.0、 192.168.1.253、192.168.1.254和192.168.1.255这些地址是系统保留地址。系统预留地址默认不在allocation_pool范围内。 约束：更新时allocation_pool范围不能包含网关和广播地址的所有IP。

        :return: The allocation_pools of this NeutronUpdateSubnetOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.AllocationPool`]
        """
        return self._allocation_pools

    @allocation_pools.setter
    def allocation_pools(self, allocation_pools):
        """Sets the allocation_pools of this NeutronUpdateSubnetOption.

        功能说明：可用的IP池，allocation_pool对象参见表 allocation_pool对象 例如：[ { \"start\": \"10.0.0.2\", \"end\": \"10.0.0.251\"} ]每个子网的第1个和最后3个IP地址为系统保留地址。以192.168.1.0/24为例，192.168.1.0、 192.168.1.253、192.168.1.254和192.168.1.255这些地址是系统保留地址。系统预留地址默认不在allocation_pool范围内。 约束：更新时allocation_pool范围不能包含网关和广播地址的所有IP。

        :param allocation_pools: The allocation_pools of this NeutronUpdateSubnetOption.
        :type allocation_pools: list[:class:`huaweicloudsdkvpc.v2.AllocationPool`]
        """
        self._allocation_pools = allocation_pools

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
        if not isinstance(other, NeutronUpdateSubnetOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
