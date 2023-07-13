# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronCreatePortOption:

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
        'network_id': 'str',
        'admin_state_up': 'bool',
        'fixed_ips': 'list[FixedIp]',
        'security_groups': 'list[str]',
        'device_owner': 'str',
        'allowed_address_pairs': 'list[AllowedAddressPair]',
        'extra_dhcp_opts': 'list[ExtraDhcpOpt]',
        'bindingprofile': 'dict(str, object)',
        'port_security_enabled': 'bool',
        'bindingvnic_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'network_id': 'network_id',
        'admin_state_up': 'admin_state_up',
        'fixed_ips': 'fixed_ips',
        'security_groups': 'security_groups',
        'device_owner': 'device_owner',
        'allowed_address_pairs': 'allowed_address_pairs',
        'extra_dhcp_opts': 'extra_dhcp_opts',
        'bindingprofile': 'binding:profile',
        'port_security_enabled': 'port_security_enabled',
        'bindingvnic_type': 'binding:vnic_type'
    }

    def __init__(self, name=None, network_id=None, admin_state_up=None, fixed_ips=None, security_groups=None, device_owner=None, allowed_address_pairs=None, extra_dhcp_opts=None, bindingprofile=None, port_security_enabled=None, bindingvnic_type=None):
        """NeutronCreatePortOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：端口的名称 取值范围：0-255个字符
        :type name: str
        :param network_id: 端口所属网络ID
        :type network_id: str
        :param admin_state_up: 功能说明：管理状态 约束：只支持true
        :type admin_state_up: bool
        :param fixed_ips: 功能说明：端口的IP地址，参见“FixedIp对象”表 约束：device_owner为neutron: VIP_PORT时最多指定一个fixed_ip，给云服务器创建IPv6端口时，必须具备一个IPv4 subnet_id和一个IPv6 subnet_id 。
        :type fixed_ips: list[:class:`huaweicloudsdkvpc.v2.FixedIp`]
        :param security_groups: 功能说明：作用在该端口上的安全组的ID列表 约束：不支持更新为空
        :type security_groups: list[str]
        :param device_owner: 功能说明：端口设备所属 取值范围：目前只支持指定\&quot;\&quot;和\&quot;neutron:VIP_PORT\&quot;；neutron:VIP_PORT表示创建的是VIP
        :type device_owner: str
        :param allowed_address_pairs: 功能说明：扩展属性：IP/Mac对列表，详情参见“allow_address_pair对象”表 约束：IP地址不允许为 “0.0.0.0”如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组硬件SDN环境不支持ip_address属性配置为CIDR格式。
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v2.AllowedAddressPair`]
        :param extra_dhcp_opts: 功能说明：扩展属性：DHCP的扩展Option，详情参见“ExtraDhcpOpt对象”表
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOpt`]
        :param bindingprofile: 扩展属性：提供用户设置自定义信息 【使用说明】  internal_elb字段，布尔类型，普通租户可见。只有在创建内网ELB的虚拟IP的网卡时设置为true。普通租户没有权限更改该字段，由系统维护。 举例：{\&quot;internal_elb\&quot;: true}  disable_security_groups字段，布尔类型，普通租户可见。默认为false高性能通信场景下，允许指定为true普通租户可见。仅支持创建port和读取时指定。当前仅支持指定为true，不支持指定为false 举例：{\&quot;disable_security_groups\&quot;：true }， 当前仅支持指定为true，不支持指定为false，指定为true时，FWaaS功能不生效。  仅对于“华北-北京二”：udp_srvports和tcp_srvports，字段，字符串类型，默认不设置udp_srvports和tcp_srvports字段。允许指定udp_srvports和tcp_srvports字段为端口号，表示这些端口的tcp报文和udp报文可支持高并发连接，但是此类报文不受ACL和安全组规则的限制。udp_srvports和tcp_srvports字段同时支持更新操作。 − 格式： {\&quot;tcp_srvports\&quot;: \&quot;port1 port2 port3\&quot;, \&quot;udp_srvports\&quot;: \&quot;port1 port2 port3\&quot;} 端口号之间以空格间隔，最多允许指定的端口号总共为15个，端口号范围是1到65535。 − 示例：{\&quot;tcp_srvports\&quot;: \&quot;80 443\&quot;, \&quot;udp_srvports\&quot;: \&quot;53\&quot;} 示例表示入方向目的端口为80或者443的tcp报文可支持高并发连接。入方向目的端口为53的udp报文可支持高并发连接。但是此类报文不受ACL和安全组规则的限制。 
        :type bindingprofile: dict(str, object)
        :param port_security_enabled: 功能说明：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效 取值范围：启用（true）或禁用（false）
        :type port_security_enabled: bool
        :param bindingvnic_type: 绑定的vNIC类型  - normal: 软交换
        :type bindingvnic_type: str
        """
        
        

        self._name = None
        self._network_id = None
        self._admin_state_up = None
        self._fixed_ips = None
        self._security_groups = None
        self._device_owner = None
        self._allowed_address_pairs = None
        self._extra_dhcp_opts = None
        self._bindingprofile = None
        self._port_security_enabled = None
        self._bindingvnic_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.network_id = network_id
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
        if security_groups is not None:
            self.security_groups = security_groups
        if device_owner is not None:
            self.device_owner = device_owner
        if allowed_address_pairs is not None:
            self.allowed_address_pairs = allowed_address_pairs
        if extra_dhcp_opts is not None:
            self.extra_dhcp_opts = extra_dhcp_opts
        if bindingprofile is not None:
            self.bindingprofile = bindingprofile
        if port_security_enabled is not None:
            self.port_security_enabled = port_security_enabled
        if bindingvnic_type is not None:
            self.bindingvnic_type = bindingvnic_type

    @property
    def name(self):
        """Gets the name of this NeutronCreatePortOption.

        功能说明：端口的名称 取值范围：0-255个字符

        :return: The name of this NeutronCreatePortOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronCreatePortOption.

        功能说明：端口的名称 取值范围：0-255个字符

        :param name: The name of this NeutronCreatePortOption.
        :type name: str
        """
        self._name = name

    @property
    def network_id(self):
        """Gets the network_id of this NeutronCreatePortOption.

        端口所属网络ID

        :return: The network_id of this NeutronCreatePortOption.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this NeutronCreatePortOption.

        端口所属网络ID

        :param network_id: The network_id of this NeutronCreatePortOption.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronCreatePortOption.

        功能说明：管理状态 约束：只支持true

        :return: The admin_state_up of this NeutronCreatePortOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronCreatePortOption.

        功能说明：管理状态 约束：只支持true

        :param admin_state_up: The admin_state_up of this NeutronCreatePortOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this NeutronCreatePortOption.

        功能说明：端口的IP地址，参见“FixedIp对象”表 约束：device_owner为neutron: VIP_PORT时最多指定一个fixed_ip，给云服务器创建IPv6端口时，必须具备一个IPv4 subnet_id和一个IPv6 subnet_id 。

        :return: The fixed_ips of this NeutronCreatePortOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.FixedIp`]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this NeutronCreatePortOption.

        功能说明：端口的IP地址，参见“FixedIp对象”表 约束：device_owner为neutron: VIP_PORT时最多指定一个fixed_ip，给云服务器创建IPv6端口时，必须具备一个IPv4 subnet_id和一个IPv6 subnet_id 。

        :param fixed_ips: The fixed_ips of this NeutronCreatePortOption.
        :type fixed_ips: list[:class:`huaweicloudsdkvpc.v2.FixedIp`]
        """
        self._fixed_ips = fixed_ips

    @property
    def security_groups(self):
        """Gets the security_groups of this NeutronCreatePortOption.

        功能说明：作用在该端口上的安全组的ID列表 约束：不支持更新为空

        :return: The security_groups of this NeutronCreatePortOption.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NeutronCreatePortOption.

        功能说明：作用在该端口上的安全组的ID列表 约束：不支持更新为空

        :param security_groups: The security_groups of this NeutronCreatePortOption.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def device_owner(self):
        """Gets the device_owner of this NeutronCreatePortOption.

        功能说明：端口设备所属 取值范围：目前只支持指定\"\"和\"neutron:VIP_PORT\"；neutron:VIP_PORT表示创建的是VIP

        :return: The device_owner of this NeutronCreatePortOption.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this NeutronCreatePortOption.

        功能说明：端口设备所属 取值范围：目前只支持指定\"\"和\"neutron:VIP_PORT\"；neutron:VIP_PORT表示创建的是VIP

        :param device_owner: The device_owner of this NeutronCreatePortOption.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def allowed_address_pairs(self):
        """Gets the allowed_address_pairs of this NeutronCreatePortOption.

        功能说明：扩展属性：IP/Mac对列表，详情参见“allow_address_pair对象”表 约束：IP地址不允许为 “0.0.0.0”如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组硬件SDN环境不支持ip_address属性配置为CIDR格式。

        :return: The allowed_address_pairs of this NeutronCreatePortOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        """Sets the allowed_address_pairs of this NeutronCreatePortOption.

        功能说明：扩展属性：IP/Mac对列表，详情参见“allow_address_pair对象”表 约束：IP地址不允许为 “0.0.0.0”如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组硬件SDN环境不支持ip_address属性配置为CIDR格式。

        :param allowed_address_pairs: The allowed_address_pairs of this NeutronCreatePortOption.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v2.AllowedAddressPair`]
        """
        self._allowed_address_pairs = allowed_address_pairs

    @property
    def extra_dhcp_opts(self):
        """Gets the extra_dhcp_opts of this NeutronCreatePortOption.

        功能说明：扩展属性：DHCP的扩展Option，详情参见“ExtraDhcpOpt对象”表

        :return: The extra_dhcp_opts of this NeutronCreatePortOption.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOpt`]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        """Sets the extra_dhcp_opts of this NeutronCreatePortOption.

        功能说明：扩展属性：DHCP的扩展Option，详情参见“ExtraDhcpOpt对象”表

        :param extra_dhcp_opts: The extra_dhcp_opts of this NeutronCreatePortOption.
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOpt`]
        """
        self._extra_dhcp_opts = extra_dhcp_opts

    @property
    def bindingprofile(self):
        """Gets the bindingprofile of this NeutronCreatePortOption.

        扩展属性：提供用户设置自定义信息 【使用说明】  internal_elb字段，布尔类型，普通租户可见。只有在创建内网ELB的虚拟IP的网卡时设置为true。普通租户没有权限更改该字段，由系统维护。 举例：{\"internal_elb\": true}  disable_security_groups字段，布尔类型，普通租户可见。默认为false高性能通信场景下，允许指定为true普通租户可见。仅支持创建port和读取时指定。当前仅支持指定为true，不支持指定为false 举例：{\"disable_security_groups\"：true }， 当前仅支持指定为true，不支持指定为false，指定为true时，FWaaS功能不生效。  仅对于“华北-北京二”：udp_srvports和tcp_srvports，字段，字符串类型，默认不设置udp_srvports和tcp_srvports字段。允许指定udp_srvports和tcp_srvports字段为端口号，表示这些端口的tcp报文和udp报文可支持高并发连接，但是此类报文不受ACL和安全组规则的限制。udp_srvports和tcp_srvports字段同时支持更新操作。 − 格式： {\"tcp_srvports\": \"port1 port2 port3\", \"udp_srvports\": \"port1 port2 port3\"} 端口号之间以空格间隔，最多允许指定的端口号总共为15个，端口号范围是1到65535。 − 示例：{\"tcp_srvports\": \"80 443\", \"udp_srvports\": \"53\"} 示例表示入方向目的端口为80或者443的tcp报文可支持高并发连接。入方向目的端口为53的udp报文可支持高并发连接。但是此类报文不受ACL和安全组规则的限制。 

        :return: The bindingprofile of this NeutronCreatePortOption.
        :rtype: dict(str, object)
        """
        return self._bindingprofile

    @bindingprofile.setter
    def bindingprofile(self, bindingprofile):
        """Sets the bindingprofile of this NeutronCreatePortOption.

        扩展属性：提供用户设置自定义信息 【使用说明】  internal_elb字段，布尔类型，普通租户可见。只有在创建内网ELB的虚拟IP的网卡时设置为true。普通租户没有权限更改该字段，由系统维护。 举例：{\"internal_elb\": true}  disable_security_groups字段，布尔类型，普通租户可见。默认为false高性能通信场景下，允许指定为true普通租户可见。仅支持创建port和读取时指定。当前仅支持指定为true，不支持指定为false 举例：{\"disable_security_groups\"：true }， 当前仅支持指定为true，不支持指定为false，指定为true时，FWaaS功能不生效。  仅对于“华北-北京二”：udp_srvports和tcp_srvports，字段，字符串类型，默认不设置udp_srvports和tcp_srvports字段。允许指定udp_srvports和tcp_srvports字段为端口号，表示这些端口的tcp报文和udp报文可支持高并发连接，但是此类报文不受ACL和安全组规则的限制。udp_srvports和tcp_srvports字段同时支持更新操作。 − 格式： {\"tcp_srvports\": \"port1 port2 port3\", \"udp_srvports\": \"port1 port2 port3\"} 端口号之间以空格间隔，最多允许指定的端口号总共为15个，端口号范围是1到65535。 − 示例：{\"tcp_srvports\": \"80 443\", \"udp_srvports\": \"53\"} 示例表示入方向目的端口为80或者443的tcp报文可支持高并发连接。入方向目的端口为53的udp报文可支持高并发连接。但是此类报文不受ACL和安全组规则的限制。 

        :param bindingprofile: The bindingprofile of this NeutronCreatePortOption.
        :type bindingprofile: dict(str, object)
        """
        self._bindingprofile = bindingprofile

    @property
    def port_security_enabled(self):
        """Gets the port_security_enabled of this NeutronCreatePortOption.

        功能说明：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效 取值范围：启用（true）或禁用（false）

        :return: The port_security_enabled of this NeutronCreatePortOption.
        :rtype: bool
        """
        return self._port_security_enabled

    @port_security_enabled.setter
    def port_security_enabled(self, port_security_enabled):
        """Sets the port_security_enabled of this NeutronCreatePortOption.

        功能说明：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效 取值范围：启用（true）或禁用（false）

        :param port_security_enabled: The port_security_enabled of this NeutronCreatePortOption.
        :type port_security_enabled: bool
        """
        self._port_security_enabled = port_security_enabled

    @property
    def bindingvnic_type(self):
        """Gets the bindingvnic_type of this NeutronCreatePortOption.

        绑定的vNIC类型  - normal: 软交换

        :return: The bindingvnic_type of this NeutronCreatePortOption.
        :rtype: str
        """
        return self._bindingvnic_type

    @bindingvnic_type.setter
    def bindingvnic_type(self, bindingvnic_type):
        """Sets the bindingvnic_type of this NeutronCreatePortOption.

        绑定的vNIC类型  - normal: 软交换

        :param bindingvnic_type: The bindingvnic_type of this NeutronCreatePortOption.
        :type bindingvnic_type: str
        """
        self._bindingvnic_type = bindingvnic_type

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
        if not isinstance(other, NeutronCreatePortOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
