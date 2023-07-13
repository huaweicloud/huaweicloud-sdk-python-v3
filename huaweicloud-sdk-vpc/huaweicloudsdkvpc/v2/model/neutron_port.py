# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronPort:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'allowed_address_pairs': 'list[AllowedAddressPair]',
        'bindingprofile': 'object',
        'bindingvif_details': 'BindingVifDetails',
        'bindingvnic_type': 'str',
        'device_id': 'str',
        'device_owner': 'str',
        'dns_assignment': 'list[DnsAssignMent]',
        'dns_name': 'str',
        'extra_dhcp_opts': 'list[ExtraDhcpOpt]',
        'fixed_ips': 'list[FixedIp]',
        'id': 'str',
        'mac_address': 'str',
        'name': 'str',
        'network_id': 'str',
        'port_security_enabled': 'bool',
        'security_groups': 'list[str]',
        'status': 'str',
        'tenant_id': 'str',
        'project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'allowed_address_pairs': 'allowed_address_pairs',
        'bindingprofile': 'binding:profile',
        'bindingvif_details': 'binding:vif_details',
        'bindingvnic_type': 'binding:vnic_type',
        'device_id': 'device_id',
        'device_owner': 'device_owner',
        'dns_assignment': 'dns_assignment',
        'dns_name': 'dns_name',
        'extra_dhcp_opts': 'extra_dhcp_opts',
        'fixed_ips': 'fixed_ips',
        'id': 'id',
        'mac_address': 'mac_address',
        'name': 'name',
        'network_id': 'network_id',
        'port_security_enabled': 'port_security_enabled',
        'security_groups': 'security_groups',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, admin_state_up=None, allowed_address_pairs=None, bindingprofile=None, bindingvif_details=None, bindingvnic_type=None, device_id=None, device_owner=None, dns_assignment=None, dns_name=None, extra_dhcp_opts=None, fixed_ips=None, id=None, mac_address=None, name=None, network_id=None, port_security_enabled=None, security_groups=None, status=None, tenant_id=None, project_id=None, created_at=None, updated_at=None):
        """NeutronPort

        The model defined in huaweicloud sdk

        :param admin_state_up: 功能说明：端口管理状态 约束：目前支持true
        :type admin_state_up: bool
        :param allowed_address_pairs: 功能说明：扩展属性：IP/Mac对列表，详情参见“allow_address_pair对象”表 约束：IP地址不允许为 “0.0.0.0”如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组硬件SDN环境不支持ip_address属性配置为CIDR格式。
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v2.AllowedAddressPair`]
        :param bindingprofile: 扩展属性：提供用户设置自定义信息 【使用说明】  internal_elb字段，布尔类型，普通租户可见。只有在创建内网ELB的虚拟IP的网卡时设置为true。普通租户没有权限更改该字段，由系统维护。 举例：{\&quot;internal_elb\&quot;: true}  disable_security_groups字段，布尔类型，普通租户可见。默认为false高性能通信场景下，允许指定为true普通租户可见。仅支持创建port和读取时指定。当前仅支持指定为true，不支持指定为false 举例：{\&quot;disable_security_groups\&quot;：true }， 当前仅支持指定为true，不支持指定为false，指定为true时，FWaaS功能不生效。  仅对于“华北-北京二”：udp_srvports和tcp_srvports，字段，字符串类型，默认不设置udp_srvports和tcp_srvports字段。允许指定udp_srvports和tcp_srvports字段为端口号，表示这些端口的tcp报文和udp报文可支持高并发连接，但是此类报文不受ACL和安全组规则的限制。udp_srvports和tcp_srvports字段同时支持更新操作。 − 格式： {\&quot;tcp_srvports\&quot;: \&quot;port1 port2 port3\&quot;, \&quot;udp_srvports\&quot;: \&quot;port1 port2 port3\&quot;} 端口号之间以空格间隔，最多允许指定的端口号总共为15个，端口号范围是1到65535。 − 示例：{\&quot;tcp_srvports\&quot;: \&quot;80 443\&quot;, \&quot;udp_srvports\&quot;: \&quot;53\&quot;} 示例表示入方向目的端口为80或者443的tcp报文可支持高并发连接。入方向目的端口为53的udp报文可支持高并发连接。但是此类报文不受ACL和安全组规则的限制。 
        :type bindingprofile: object
        :param bindingvif_details: 
        :type bindingvif_details: :class:`huaweicloudsdkvpc.v2.BindingVifDetails`
        :param bindingvnic_type: 功能说明：绑定的vNIC类型  - normal：软交换
        :type bindingvnic_type: str
        :param device_id: 功能说明：端口设备ID 约束：不支持设置和更新，由系统自动维护，该字段非空的端口不允许删除。
        :type device_id: str
        :param device_owner: 功能说明：端口设备所属（DHCP/Router/ Nova等） 约束：不支持更新，只允许用户在创建虚拟IP端口时，为虚拟IP端口设置device_owner为neutron:VIP_PORT，当端口的该字段不为空时，仅支持该字段为neutron:VIP_PORT时的端口删除。该字段非空的端口不允许删除。
        :type device_owner: str
        :param dns_assignment: 功能说明：扩展属性：主网卡默认内网域名信息 约束：不支持设置和更新，由系统自动维护  - hostname：与端口dns_name一致  - ip_address：端口ipv4私有地址  - fqdn：为端口创建默认内网fqdn
        :type dns_assignment: list[:class:`huaweicloudsdkvpc.v2.DnsAssignMent`]
        :param dns_name: 功能说明：扩展属性：主网卡默认内网DNS名称 约束：不支持设置和更新，由系统自动维护,访问该默认内网域名前，请确保子网使用当前系统提供的DNS
        :type dns_name: str
        :param extra_dhcp_opts: 功能说明：扩展属性：DHCP的扩展Option，详情参见“ExtraDhcpOpt对象”表
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOpt`]
        :param fixed_ips: 功能说明：端口的IP地址，参见“FixedIp对象”表 约束：device_owner为neutron: VIP_PORT时最多指定一个fixed_ip，给云服务器创建IPv6端口时，必须具备一个IPv4 subnet_id和一个IPv6 subnet_id 。
        :type fixed_ips: list[:class:`huaweicloudsdkvpc.v2.FixedIp`]
        :param id: 端口ID
        :type id: str
        :param mac_address: 功能说明：端口mac地址 约束：只支持系统动态分配，不支持指定
        :type mac_address: str
        :param name: 功能说明：端口的名称 取值范围：0-255个字符
        :type name: str
        :param network_id: 端口所属网络ID
        :type network_id: str
        :param port_security_enabled: 功能说明：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效 取值范围：启用（true）或禁用（false）
        :type port_security_enabled: bool
        :param security_groups: 功能说明：作用在该端口上的安全组的ID列表 约束：不支持更新为空
        :type security_groups: list[str]
        :param status: 功能说明：端口状态 取值范围：ACTIVE，BUILD，DOWN 约束：Hana硬直通虚拟机端口状态总为DOWN
        :type status: str
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param created_at: 功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        """
        
        

        self._admin_state_up = None
        self._allowed_address_pairs = None
        self._bindingprofile = None
        self._bindingvif_details = None
        self._bindingvnic_type = None
        self._device_id = None
        self._device_owner = None
        self._dns_assignment = None
        self._dns_name = None
        self._extra_dhcp_opts = None
        self._fixed_ips = None
        self._id = None
        self._mac_address = None
        self._name = None
        self._network_id = None
        self._port_security_enabled = None
        self._security_groups = None
        self._status = None
        self._tenant_id = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.allowed_address_pairs = allowed_address_pairs
        self.bindingprofile = bindingprofile
        self.bindingvif_details = bindingvif_details
        self.bindingvnic_type = bindingvnic_type
        self.device_id = device_id
        self.device_owner = device_owner
        self.dns_assignment = dns_assignment
        self.dns_name = dns_name
        self.extra_dhcp_opts = extra_dhcp_opts
        self.fixed_ips = fixed_ips
        self.id = id
        self.mac_address = mac_address
        self.name = name
        self.network_id = network_id
        self.port_security_enabled = port_security_enabled
        self.security_groups = security_groups
        self.status = status
        self.tenant_id = tenant_id
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronPort.

        功能说明：端口管理状态 约束：目前支持true

        :return: The admin_state_up of this NeutronPort.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronPort.

        功能说明：端口管理状态 约束：目前支持true

        :param admin_state_up: The admin_state_up of this NeutronPort.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def allowed_address_pairs(self):
        """Gets the allowed_address_pairs of this NeutronPort.

        功能说明：扩展属性：IP/Mac对列表，详情参见“allow_address_pair对象”表 约束：IP地址不允许为 “0.0.0.0”如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组硬件SDN环境不支持ip_address属性配置为CIDR格式。

        :return: The allowed_address_pairs of this NeutronPort.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        """Sets the allowed_address_pairs of this NeutronPort.

        功能说明：扩展属性：IP/Mac对列表，详情参见“allow_address_pair对象”表 约束：IP地址不允许为 “0.0.0.0”如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组硬件SDN环境不支持ip_address属性配置为CIDR格式。

        :param allowed_address_pairs: The allowed_address_pairs of this NeutronPort.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v2.AllowedAddressPair`]
        """
        self._allowed_address_pairs = allowed_address_pairs

    @property
    def bindingprofile(self):
        """Gets the bindingprofile of this NeutronPort.

        扩展属性：提供用户设置自定义信息 【使用说明】  internal_elb字段，布尔类型，普通租户可见。只有在创建内网ELB的虚拟IP的网卡时设置为true。普通租户没有权限更改该字段，由系统维护。 举例：{\"internal_elb\": true}  disable_security_groups字段，布尔类型，普通租户可见。默认为false高性能通信场景下，允许指定为true普通租户可见。仅支持创建port和读取时指定。当前仅支持指定为true，不支持指定为false 举例：{\"disable_security_groups\"：true }， 当前仅支持指定为true，不支持指定为false，指定为true时，FWaaS功能不生效。  仅对于“华北-北京二”：udp_srvports和tcp_srvports，字段，字符串类型，默认不设置udp_srvports和tcp_srvports字段。允许指定udp_srvports和tcp_srvports字段为端口号，表示这些端口的tcp报文和udp报文可支持高并发连接，但是此类报文不受ACL和安全组规则的限制。udp_srvports和tcp_srvports字段同时支持更新操作。 − 格式： {\"tcp_srvports\": \"port1 port2 port3\", \"udp_srvports\": \"port1 port2 port3\"} 端口号之间以空格间隔，最多允许指定的端口号总共为15个，端口号范围是1到65535。 − 示例：{\"tcp_srvports\": \"80 443\", \"udp_srvports\": \"53\"} 示例表示入方向目的端口为80或者443的tcp报文可支持高并发连接。入方向目的端口为53的udp报文可支持高并发连接。但是此类报文不受ACL和安全组规则的限制。 

        :return: The bindingprofile of this NeutronPort.
        :rtype: object
        """
        return self._bindingprofile

    @bindingprofile.setter
    def bindingprofile(self, bindingprofile):
        """Sets the bindingprofile of this NeutronPort.

        扩展属性：提供用户设置自定义信息 【使用说明】  internal_elb字段，布尔类型，普通租户可见。只有在创建内网ELB的虚拟IP的网卡时设置为true。普通租户没有权限更改该字段，由系统维护。 举例：{\"internal_elb\": true}  disable_security_groups字段，布尔类型，普通租户可见。默认为false高性能通信场景下，允许指定为true普通租户可见。仅支持创建port和读取时指定。当前仅支持指定为true，不支持指定为false 举例：{\"disable_security_groups\"：true }， 当前仅支持指定为true，不支持指定为false，指定为true时，FWaaS功能不生效。  仅对于“华北-北京二”：udp_srvports和tcp_srvports，字段，字符串类型，默认不设置udp_srvports和tcp_srvports字段。允许指定udp_srvports和tcp_srvports字段为端口号，表示这些端口的tcp报文和udp报文可支持高并发连接，但是此类报文不受ACL和安全组规则的限制。udp_srvports和tcp_srvports字段同时支持更新操作。 − 格式： {\"tcp_srvports\": \"port1 port2 port3\", \"udp_srvports\": \"port1 port2 port3\"} 端口号之间以空格间隔，最多允许指定的端口号总共为15个，端口号范围是1到65535。 − 示例：{\"tcp_srvports\": \"80 443\", \"udp_srvports\": \"53\"} 示例表示入方向目的端口为80或者443的tcp报文可支持高并发连接。入方向目的端口为53的udp报文可支持高并发连接。但是此类报文不受ACL和安全组规则的限制。 

        :param bindingprofile: The bindingprofile of this NeutronPort.
        :type bindingprofile: object
        """
        self._bindingprofile = bindingprofile

    @property
    def bindingvif_details(self):
        """Gets the bindingvif_details of this NeutronPort.

        :return: The bindingvif_details of this NeutronPort.
        :rtype: :class:`huaweicloudsdkvpc.v2.BindingVifDetails`
        """
        return self._bindingvif_details

    @bindingvif_details.setter
    def bindingvif_details(self, bindingvif_details):
        """Sets the bindingvif_details of this NeutronPort.

        :param bindingvif_details: The bindingvif_details of this NeutronPort.
        :type bindingvif_details: :class:`huaweicloudsdkvpc.v2.BindingVifDetails`
        """
        self._bindingvif_details = bindingvif_details

    @property
    def bindingvnic_type(self):
        """Gets the bindingvnic_type of this NeutronPort.

        功能说明：绑定的vNIC类型  - normal：软交换

        :return: The bindingvnic_type of this NeutronPort.
        :rtype: str
        """
        return self._bindingvnic_type

    @bindingvnic_type.setter
    def bindingvnic_type(self, bindingvnic_type):
        """Sets the bindingvnic_type of this NeutronPort.

        功能说明：绑定的vNIC类型  - normal：软交换

        :param bindingvnic_type: The bindingvnic_type of this NeutronPort.
        :type bindingvnic_type: str
        """
        self._bindingvnic_type = bindingvnic_type

    @property
    def device_id(self):
        """Gets the device_id of this NeutronPort.

        功能说明：端口设备ID 约束：不支持设置和更新，由系统自动维护，该字段非空的端口不允许删除。

        :return: The device_id of this NeutronPort.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this NeutronPort.

        功能说明：端口设备ID 约束：不支持设置和更新，由系统自动维护，该字段非空的端口不允许删除。

        :param device_id: The device_id of this NeutronPort.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_owner(self):
        """Gets the device_owner of this NeutronPort.

        功能说明：端口设备所属（DHCP/Router/ Nova等） 约束：不支持更新，只允许用户在创建虚拟IP端口时，为虚拟IP端口设置device_owner为neutron:VIP_PORT，当端口的该字段不为空时，仅支持该字段为neutron:VIP_PORT时的端口删除。该字段非空的端口不允许删除。

        :return: The device_owner of this NeutronPort.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this NeutronPort.

        功能说明：端口设备所属（DHCP/Router/ Nova等） 约束：不支持更新，只允许用户在创建虚拟IP端口时，为虚拟IP端口设置device_owner为neutron:VIP_PORT，当端口的该字段不为空时，仅支持该字段为neutron:VIP_PORT时的端口删除。该字段非空的端口不允许删除。

        :param device_owner: The device_owner of this NeutronPort.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def dns_assignment(self):
        """Gets the dns_assignment of this NeutronPort.

        功能说明：扩展属性：主网卡默认内网域名信息 约束：不支持设置和更新，由系统自动维护  - hostname：与端口dns_name一致  - ip_address：端口ipv4私有地址  - fqdn：为端口创建默认内网fqdn

        :return: The dns_assignment of this NeutronPort.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.DnsAssignMent`]
        """
        return self._dns_assignment

    @dns_assignment.setter
    def dns_assignment(self, dns_assignment):
        """Sets the dns_assignment of this NeutronPort.

        功能说明：扩展属性：主网卡默认内网域名信息 约束：不支持设置和更新，由系统自动维护  - hostname：与端口dns_name一致  - ip_address：端口ipv4私有地址  - fqdn：为端口创建默认内网fqdn

        :param dns_assignment: The dns_assignment of this NeutronPort.
        :type dns_assignment: list[:class:`huaweicloudsdkvpc.v2.DnsAssignMent`]
        """
        self._dns_assignment = dns_assignment

    @property
    def dns_name(self):
        """Gets the dns_name of this NeutronPort.

        功能说明：扩展属性：主网卡默认内网DNS名称 约束：不支持设置和更新，由系统自动维护,访问该默认内网域名前，请确保子网使用当前系统提供的DNS

        :return: The dns_name of this NeutronPort.
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """Sets the dns_name of this NeutronPort.

        功能说明：扩展属性：主网卡默认内网DNS名称 约束：不支持设置和更新，由系统自动维护,访问该默认内网域名前，请确保子网使用当前系统提供的DNS

        :param dns_name: The dns_name of this NeutronPort.
        :type dns_name: str
        """
        self._dns_name = dns_name

    @property
    def extra_dhcp_opts(self):
        """Gets the extra_dhcp_opts of this NeutronPort.

        功能说明：扩展属性：DHCP的扩展Option，详情参见“ExtraDhcpOpt对象”表

        :return: The extra_dhcp_opts of this NeutronPort.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOpt`]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        """Sets the extra_dhcp_opts of this NeutronPort.

        功能说明：扩展属性：DHCP的扩展Option，详情参见“ExtraDhcpOpt对象”表

        :param extra_dhcp_opts: The extra_dhcp_opts of this NeutronPort.
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOpt`]
        """
        self._extra_dhcp_opts = extra_dhcp_opts

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this NeutronPort.

        功能说明：端口的IP地址，参见“FixedIp对象”表 约束：device_owner为neutron: VIP_PORT时最多指定一个fixed_ip，给云服务器创建IPv6端口时，必须具备一个IPv4 subnet_id和一个IPv6 subnet_id 。

        :return: The fixed_ips of this NeutronPort.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.FixedIp`]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this NeutronPort.

        功能说明：端口的IP地址，参见“FixedIp对象”表 约束：device_owner为neutron: VIP_PORT时最多指定一个fixed_ip，给云服务器创建IPv6端口时，必须具备一个IPv4 subnet_id和一个IPv6 subnet_id 。

        :param fixed_ips: The fixed_ips of this NeutronPort.
        :type fixed_ips: list[:class:`huaweicloudsdkvpc.v2.FixedIp`]
        """
        self._fixed_ips = fixed_ips

    @property
    def id(self):
        """Gets the id of this NeutronPort.

        端口ID

        :return: The id of this NeutronPort.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronPort.

        端口ID

        :param id: The id of this NeutronPort.
        :type id: str
        """
        self._id = id

    @property
    def mac_address(self):
        """Gets the mac_address of this NeutronPort.

        功能说明：端口mac地址 约束：只支持系统动态分配，不支持指定

        :return: The mac_address of this NeutronPort.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this NeutronPort.

        功能说明：端口mac地址 约束：只支持系统动态分配，不支持指定

        :param mac_address: The mac_address of this NeutronPort.
        :type mac_address: str
        """
        self._mac_address = mac_address

    @property
    def name(self):
        """Gets the name of this NeutronPort.

        功能说明：端口的名称 取值范围：0-255个字符

        :return: The name of this NeutronPort.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronPort.

        功能说明：端口的名称 取值范围：0-255个字符

        :param name: The name of this NeutronPort.
        :type name: str
        """
        self._name = name

    @property
    def network_id(self):
        """Gets the network_id of this NeutronPort.

        端口所属网络ID

        :return: The network_id of this NeutronPort.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this NeutronPort.

        端口所属网络ID

        :param network_id: The network_id of this NeutronPort.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def port_security_enabled(self):
        """Gets the port_security_enabled of this NeutronPort.

        功能说明：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效 取值范围：启用（true）或禁用（false）

        :return: The port_security_enabled of this NeutronPort.
        :rtype: bool
        """
        return self._port_security_enabled

    @port_security_enabled.setter
    def port_security_enabled(self, port_security_enabled):
        """Sets the port_security_enabled of this NeutronPort.

        功能说明：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效 取值范围：启用（true）或禁用（false）

        :param port_security_enabled: The port_security_enabled of this NeutronPort.
        :type port_security_enabled: bool
        """
        self._port_security_enabled = port_security_enabled

    @property
    def security_groups(self):
        """Gets the security_groups of this NeutronPort.

        功能说明：作用在该端口上的安全组的ID列表 约束：不支持更新为空

        :return: The security_groups of this NeutronPort.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NeutronPort.

        功能说明：作用在该端口上的安全组的ID列表 约束：不支持更新为空

        :param security_groups: The security_groups of this NeutronPort.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def status(self):
        """Gets the status of this NeutronPort.

        功能说明：端口状态 取值范围：ACTIVE，BUILD，DOWN 约束：Hana硬直通虚拟机端口状态总为DOWN

        :return: The status of this NeutronPort.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NeutronPort.

        功能说明：端口状态 取值范围：ACTIVE，BUILD，DOWN 约束：Hana硬直通虚拟机端口状态总为DOWN

        :param status: The status of this NeutronPort.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronPort.

        项目ID

        :return: The tenant_id of this NeutronPort.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronPort.

        项目ID

        :param tenant_id: The tenant_id of this NeutronPort.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this NeutronPort.

        项目ID

        :return: The project_id of this NeutronPort.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronPort.

        项目ID

        :param project_id: The project_id of this NeutronPort.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this NeutronPort.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this NeutronPort.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NeutronPort.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this NeutronPort.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NeutronPort.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this NeutronPort.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NeutronPort.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this NeutronPort.
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
        if not isinstance(other, NeutronPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
