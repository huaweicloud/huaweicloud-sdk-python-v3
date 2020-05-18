# coding: utf-8

import pprint
import re

import six


class NeutronSubnet(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'allocation_pools': 'list[AllocationPool]',
        'cidr': 'str',
        'dns_nameservers': 'list[str]',
        'enable_dhcp': 'bool',
        'gateway_ip': 'str',
        'host_routes': 'list[HostRoute]',
        'id': 'str',
        'ip_version': 'int',
        'ipv6_address_mode': 'str',
        'ipv6_ra_mode': 'str',
        'name': 'str',
        'network_id': 'str',
        'tenant_id': 'str',
        'project_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'allocation_pools': 'allocation_pools',
        'cidr': 'cidr',
        'dns_nameservers': 'dns_nameservers',
        'enable_dhcp': 'enable_dhcp',
        'gateway_ip': 'gateway_ip',
        'host_routes': 'host_routes',
        'id': 'id',
        'ip_version': 'ip_version',
        'ipv6_address_mode': 'ipv6_address_mode',
        'ipv6_ra_mode': 'ipv6_ra_mode',
        'name': 'name',
        'network_id': 'network_id',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, allocation_pools=None, cidr=None, dns_nameservers=None, enable_dhcp=None, gateway_ip=None, host_routes=None, id=None, ip_version=None, ipv6_address_mode=None, ipv6_ra_mode=None, name=None, network_id=None, tenant_id=None, project_id=None, created_at=None, updated_at=None):  # noqa: E501
        """NeutronSubnet - a model defined in huaweicloud sdk"""

        self._allocation_pools = None
        self._cidr = None
        self._dns_nameservers = None
        self._enable_dhcp = None
        self._gateway_ip = None
        self._host_routes = None
        self._id = None
        self._ip_version = None
        self._ipv6_address_mode = None
        self._ipv6_ra_mode = None
        self._name = None
        self._network_id = None
        self._tenant_id = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.allocation_pools = allocation_pools
        self.cidr = cidr
        self.dns_nameservers = dns_nameservers
        self.enable_dhcp = enable_dhcp
        self.gateway_ip = gateway_ip
        self.host_routes = host_routes
        self.id = id
        self.ip_version = ip_version
        self.ipv6_address_mode = ipv6_address_mode
        self.ipv6_ra_mode = ipv6_ra_mode
        self.name = name
        self.network_id = network_id
        self.tenant_id = tenant_id
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def allocation_pools(self):
        """Gets the allocation_pools of this NeutronSubnet.

        功能说明：可用的IP池，allocation_pool对象参见 allocation_pool对象 例如：[ { \"start\": \"10.0.0.2\", \"end\": \"10.0.0.251\"} ]每个子网的第1个和最后4个IP地址为系统保留地址。以192.168.1.0/24为例，192.168.1.0、 192.168.1.252、192.168.1.253、192.168.1.254和192.168.1.255这些地址是系统保留地址。系统预留地址默认不在allocation_pool范围内 约束：更新时allocation_pool范围不能包含网关和广播地址的所有IP。

        :return: The allocation_pools of this NeutronSubnet.
        :rtype: list[AllocationPool]
        """
        return self._allocation_pools

    @allocation_pools.setter
    def allocation_pools(self, allocation_pools):
        """Sets the allocation_pools of this NeutronSubnet.

        功能说明：可用的IP池，allocation_pool对象参见 allocation_pool对象 例如：[ { \"start\": \"10.0.0.2\", \"end\": \"10.0.0.251\"} ]每个子网的第1个和最后4个IP地址为系统保留地址。以192.168.1.0/24为例，192.168.1.0、 192.168.1.252、192.168.1.253、192.168.1.254和192.168.1.255这些地址是系统保留地址。系统预留地址默认不在allocation_pool范围内 约束：更新时allocation_pool范围不能包含网关和广播地址的所有IP。

        :param allocation_pools: The allocation_pools of this NeutronSubnet.
        :type: list[AllocationPool]
        """
        self._allocation_pools = allocation_pools

    @property
    def cidr(self):
        """Gets the cidr of this NeutronSubnet.

        功能说明：子网网段 取值范围：CIDR格式，只支持10.0.0.0/8,172.16.0.0/12,192.168.0.0/16三个网段内的地址，掩码长度不能大于28 约束：当ip_version=6时，该字段不支持设置

        :return: The cidr of this NeutronSubnet.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this NeutronSubnet.

        功能说明：子网网段 取值范围：CIDR格式，只支持10.0.0.0/8,172.16.0.0/12,192.168.0.0/16三个网段内的地址，掩码长度不能大于28 约束：当ip_version=6时，该字段不支持设置

        :param cidr: The cidr of this NeutronSubnet.
        :type: str
        """
        self._cidr = cidr

    @property
    def dns_nameservers(self):
        """Gets the dns_nameservers of this NeutronSubnet.

        功能说明：子网关联的DNS名称服务器列表 取值范围：IP地址格式例如：\"dns_nameservers\": [\"8.xx.xx.8\",\"8.xx.xx.4\"]

        :return: The dns_nameservers of this NeutronSubnet.
        :rtype: list[str]
        """
        return self._dns_nameservers

    @dns_nameservers.setter
    def dns_nameservers(self, dns_nameservers):
        """Sets the dns_nameservers of this NeutronSubnet.

        功能说明：子网关联的DNS名称服务器列表 取值范围：IP地址格式例如：\"dns_nameservers\": [\"8.xx.xx.8\",\"8.xx.xx.4\"]

        :param dns_nameservers: The dns_nameservers of this NeutronSubnet.
        :type: list[str]
        """
        self._dns_nameservers = dns_nameservers

    @property
    def enable_dhcp(self):
        """Gets the enable_dhcp of this NeutronSubnet.

        功能说明：是否启动dhcp 取值范围：只支持true

        :return: The enable_dhcp of this NeutronSubnet.
        :rtype: bool
        """
        return self._enable_dhcp

    @enable_dhcp.setter
    def enable_dhcp(self, enable_dhcp):
        """Sets the enable_dhcp of this NeutronSubnet.

        功能说明：是否启动dhcp 取值范围：只支持true

        :param enable_dhcp: The enable_dhcp of this NeutronSubnet.
        :type: bool
        """
        self._enable_dhcp = enable_dhcp

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this NeutronSubnet.

        功能说明：子网网关IP  取值范围：本子网网段内的可用IP  约束：不允许和allocation_pools地址块冲突；ip_version=6时该字段不支持设置 默认值：本子网网段内第一个可用IP

        :return: The gateway_ip of this NeutronSubnet.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this NeutronSubnet.

        功能说明：子网网关IP  取值范围：本子网网段内的可用IP  约束：不允许和allocation_pools地址块冲突；ip_version=6时该字段不支持设置 默认值：本子网网段内第一个可用IP

        :param gateway_ip: The gateway_ip of this NeutronSubnet.
        :type: str
        """
        self._gateway_ip = gateway_ip

    @property
    def host_routes(self):
        """Gets the host_routes of this NeutronSubnet.

        虚拟机静态路由，参见“host_route对象”表

        :return: The host_routes of this NeutronSubnet.
        :rtype: list[HostRoute]
        """
        return self._host_routes

    @host_routes.setter
    def host_routes(self, host_routes):
        """Sets the host_routes of this NeutronSubnet.

        虚拟机静态路由，参见“host_route对象”表

        :param host_routes: The host_routes of this NeutronSubnet.
        :type: list[HostRoute]
        """
        self._host_routes = host_routes

    @property
    def id(self):
        """Gets the id of this NeutronSubnet.

        子网ID

        :return: The id of this NeutronSubnet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronSubnet.

        子网ID

        :param id: The id of this NeutronSubnet.
        :type: str
        """
        self._id = id

    @property
    def ip_version(self):
        """Gets the ip_version of this NeutronSubnet.

        功能说明：IP协议版本 取值范围：4或6(支持后)

        :return: The ip_version of this NeutronSubnet.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this NeutronSubnet.

        功能说明：IP协议版本 取值范围：4或6(支持后)

        :param ip_version: The ip_version of this NeutronSubnet.
        :type: int
        """
        self._ip_version = ip_version

    @property
    def ipv6_address_mode(self):
        """Gets the ipv6_address_mode of this NeutronSubnet.

        功能说明：IPv6寻址模式 取值范围：dhcpv6-stateful

        :return: The ipv6_address_mode of this NeutronSubnet.
        :rtype: str
        """
        return self._ipv6_address_mode

    @ipv6_address_mode.setter
    def ipv6_address_mode(self, ipv6_address_mode):
        """Sets the ipv6_address_mode of this NeutronSubnet.

        功能说明：IPv6寻址模式 取值范围：dhcpv6-stateful

        :param ipv6_address_mode: The ipv6_address_mode of this NeutronSubnet.
        :type: str
        """
        self._ipv6_address_mode = ipv6_address_mode

    @property
    def ipv6_ra_mode(self):
        """Gets the ipv6_ra_mode of this NeutronSubnet.

        功能说明：IPv6路由广播模式 取值范围：dhcpv6-stateful

        :return: The ipv6_ra_mode of this NeutronSubnet.
        :rtype: str
        """
        return self._ipv6_ra_mode

    @ipv6_ra_mode.setter
    def ipv6_ra_mode(self, ipv6_ra_mode):
        """Sets the ipv6_ra_mode of this NeutronSubnet.

        功能说明：IPv6路由广播模式 取值范围：dhcpv6-stateful

        :param ipv6_ra_mode: The ipv6_ra_mode of this NeutronSubnet.
        :type: str
        """
        self._ipv6_ra_mode = ipv6_ra_mode

    @property
    def name(self):
        """Gets the name of this NeutronSubnet.

        功能说明：子网的名称 取值范围：0-255个字符

        :return: The name of this NeutronSubnet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronSubnet.

        功能说明：子网的名称 取值范围：0-255个字符

        :param name: The name of this NeutronSubnet.
        :type: str
        """
        self._name = name

    @property
    def network_id(self):
        """Gets the network_id of this NeutronSubnet.

        所属网络的ID

        :return: The network_id of this NeutronSubnet.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this NeutronSubnet.

        所属网络的ID

        :param network_id: The network_id of this NeutronSubnet.
        :type: str
        """
        self._network_id = network_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronSubnet.

        项目ID

        :return: The tenant_id of this NeutronSubnet.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronSubnet.

        项目ID

        :param tenant_id: The tenant_id of this NeutronSubnet.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this NeutronSubnet.

        项目ID

        :return: The project_id of this NeutronSubnet.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronSubnet.

        项目ID

        :param project_id: The project_id of this NeutronSubnet.
        :type: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this NeutronSubnet.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this NeutronSubnet.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NeutronSubnet.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this NeutronSubnet.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NeutronSubnet.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this NeutronSubnet.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NeutronSubnet.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this NeutronSubnet.
        :type: str
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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NeutronSubnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
