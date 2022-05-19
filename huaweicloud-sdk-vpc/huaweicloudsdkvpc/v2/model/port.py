# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Port:

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
        'network_id': 'str',
        'admin_state_up': 'bool',
        'mac_address': 'str',
        'fixed_ips': 'list[FixedIp]',
        'device_id': 'str',
        'device_owner': 'str',
        'tenant_id': 'str',
        'status': 'str',
        'security_groups': 'list[str]',
        'allowed_address_pairs': 'list[AllowedAddressPair]',
        'extra_dhcp_opts': 'list[ExtraDhcpOpt]',
        'bindingvnic_type': 'str',
        'dns_assignment': 'list[DnsAssignMent]',
        'dns_name': 'str',
        'bindingvif_details': 'BindingVifDetails',
        'bindingprofile': 'object',
        'instance_id': 'str',
        'instance_type': 'str',
        'port_security_enabled': 'bool',
        'zone_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'network_id': 'network_id',
        'admin_state_up': 'admin_state_up',
        'mac_address': 'mac_address',
        'fixed_ips': 'fixed_ips',
        'device_id': 'device_id',
        'device_owner': 'device_owner',
        'tenant_id': 'tenant_id',
        'status': 'status',
        'security_groups': 'security_groups',
        'allowed_address_pairs': 'allowed_address_pairs',
        'extra_dhcp_opts': 'extra_dhcp_opts',
        'bindingvnic_type': 'binding:vnic_type',
        'dns_assignment': 'dns_assignment',
        'dns_name': 'dns_name',
        'bindingvif_details': 'binding:vif_details',
        'bindingprofile': 'binding:profile',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type',
        'port_security_enabled': 'port_security_enabled',
        'zone_id': 'zone_id'
    }

    def __init__(self, id=None, name=None, network_id=None, admin_state_up=None, mac_address=None, fixed_ips=None, device_id=None, device_owner=None, tenant_id=None, status=None, security_groups=None, allowed_address_pairs=None, extra_dhcp_opts=None, bindingvnic_type=None, dns_assignment=None, dns_name=None, bindingvif_details=None, bindingprofile=None, instance_id=None, instance_type=None, port_security_enabled=None, zone_id=None):
        """Port

        The model defined in huaweicloud sdk

        :param id: 端口ID
        :type id: str
        :param name: 功能说明：端口名称 取值范围：0~255个字符，支持中文、英文、字母、_(下划线)、-（中划线）
        :type name: str
        :param network_id: 端口所属网络的ID
        :type network_id: str
        :param admin_state_up: 功能说明：管理状态 约束：只支持true，默认为true 
        :type admin_state_up: bool
        :param mac_address: 功能描述：端口MAC地址 约束：由系统分配，不支持指定
        :type mac_address: str
        :param fixed_ips: 功能说明：端口IP 例如：\&quot;fixed_ips\&quot;: [{\&quot;subnet_id\&quot;: \&quot;4dc70db6-cb7f-4200-9790-a6a910776bba\&quot;, \&quot;ip_address\&quot;: \&quot;192.169.25.79\&quot;}] 约束：一个端口只支持一个fixed_ip，且不支持更新。
        :type fixed_ips: list[:class:`huaweicloudsdkvpc.v2.FixedIp`]
        :param device_id: 功能说明：端口所属设备ID 约束：不支持设置和更新，由系统自动维护
        :type device_id: str
        :param device_owner: 功能说明：设备所属 取值范围：合法设备所属，如network:dhcp、neutron:VIP_PORT、network:router_interface_distributed、network:router_centralized_snat 约束：不支持设置和更新，由系统自动维护
        :type device_owner: str
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param status: 功能说明：端口状态，Hana硬直通虚拟机端口状态总为DOWN 取值范围：ACTIVE、BUILD、DOWN
        :type status: str
        :param security_groups: 安全组的ID列表
        :type security_groups: list[str]
        :param allowed_address_pairs: 功能说明：IP/Mac对列表 约束：IP地址不允许为 “0.0.0.0” 如果配置地址池较大（CIDR掩码小于24位），建议为该port配置一个单独的安全组。
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v2.AllowedAddressPair`]
        :param extra_dhcp_opts: 功能说明：DHCP的扩展Option(扩展属性)
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOpt`]
        :param bindingvnic_type: 功能说明：绑定的vNIC类型 取值范围：  - normal（软交换）  - direct: SRIOV硬直通（不支持） 
        :type bindingvnic_type: str
        :param dns_assignment: 功能说明：主网卡默认内网域名信息 约束：不支持设置和更新，由系统自动维护
        :type dns_assignment: list[:class:`huaweicloudsdkvpc.v2.DnsAssignMent`]
        :param dns_name: 功能说明：主网卡默认内网DNS名称 约束：不支持设置和更新，由系统自动维护
        :type dns_name: str
        :param bindingvif_details: 
        :type bindingvif_details: :class:`huaweicloudsdkvpc.v2.BindingVifDetails`
        :param bindingprofile: 功能说明：提供用户设置自定义信息(扩展属性)
        :type bindingprofile: object
        :param instance_id: 功能说明：端口所属实例ID，例如RDS实例ID 约束：不支持设置和更新，由系统自动维护
        :type instance_id: str
        :param instance_type: 功能说明：端口所属实例类型，例如“RDS” 约束：不支持设置和更新，由系统自动维护
        :type instance_type: str
        :param port_security_enabled: 功能说明：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效 取值范围：启用（true）或禁用（false）
        :type port_security_enabled: bool
        :param zone_id: 功能说明：port所属的可用分区
        :type zone_id: str
        """
        
        

        self._id = None
        self._name = None
        self._network_id = None
        self._admin_state_up = None
        self._mac_address = None
        self._fixed_ips = None
        self._device_id = None
        self._device_owner = None
        self._tenant_id = None
        self._status = None
        self._security_groups = None
        self._allowed_address_pairs = None
        self._extra_dhcp_opts = None
        self._bindingvnic_type = None
        self._dns_assignment = None
        self._dns_name = None
        self._bindingvif_details = None
        self._bindingprofile = None
        self._instance_id = None
        self._instance_type = None
        self._port_security_enabled = None
        self._zone_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.network_id = network_id
        self.admin_state_up = admin_state_up
        self.mac_address = mac_address
        self.fixed_ips = fixed_ips
        self.device_id = device_id
        self.device_owner = device_owner
        self.tenant_id = tenant_id
        self.status = status
        self.security_groups = security_groups
        self.allowed_address_pairs = allowed_address_pairs
        self.extra_dhcp_opts = extra_dhcp_opts
        self.bindingvnic_type = bindingvnic_type
        self.dns_assignment = dns_assignment
        self.dns_name = dns_name
        self.bindingvif_details = bindingvif_details
        self.bindingprofile = bindingprofile
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.port_security_enabled = port_security_enabled
        self.zone_id = zone_id

    @property
    def id(self):
        """Gets the id of this Port.

        端口ID

        :return: The id of this Port.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Port.

        端口ID

        :param id: The id of this Port.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Port.

        功能说明：端口名称 取值范围：0~255个字符，支持中文、英文、字母、_(下划线)、-（中划线）

        :return: The name of this Port.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Port.

        功能说明：端口名称 取值范围：0~255个字符，支持中文、英文、字母、_(下划线)、-（中划线）

        :param name: The name of this Port.
        :type name: str
        """
        self._name = name

    @property
    def network_id(self):
        """Gets the network_id of this Port.

        端口所属网络的ID

        :return: The network_id of this Port.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this Port.

        端口所属网络的ID

        :param network_id: The network_id of this Port.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this Port.

        功能说明：管理状态 约束：只支持true，默认为true 

        :return: The admin_state_up of this Port.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this Port.

        功能说明：管理状态 约束：只支持true，默认为true 

        :param admin_state_up: The admin_state_up of this Port.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def mac_address(self):
        """Gets the mac_address of this Port.

        功能描述：端口MAC地址 约束：由系统分配，不支持指定

        :return: The mac_address of this Port.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this Port.

        功能描述：端口MAC地址 约束：由系统分配，不支持指定

        :param mac_address: The mac_address of this Port.
        :type mac_address: str
        """
        self._mac_address = mac_address

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this Port.

        功能说明：端口IP 例如：\"fixed_ips\": [{\"subnet_id\": \"4dc70db6-cb7f-4200-9790-a6a910776bba\", \"ip_address\": \"192.169.25.79\"}] 约束：一个端口只支持一个fixed_ip，且不支持更新。

        :return: The fixed_ips of this Port.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.FixedIp`]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this Port.

        功能说明：端口IP 例如：\"fixed_ips\": [{\"subnet_id\": \"4dc70db6-cb7f-4200-9790-a6a910776bba\", \"ip_address\": \"192.169.25.79\"}] 约束：一个端口只支持一个fixed_ip，且不支持更新。

        :param fixed_ips: The fixed_ips of this Port.
        :type fixed_ips: list[:class:`huaweicloudsdkvpc.v2.FixedIp`]
        """
        self._fixed_ips = fixed_ips

    @property
    def device_id(self):
        """Gets the device_id of this Port.

        功能说明：端口所属设备ID 约束：不支持设置和更新，由系统自动维护

        :return: The device_id of this Port.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Port.

        功能说明：端口所属设备ID 约束：不支持设置和更新，由系统自动维护

        :param device_id: The device_id of this Port.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_owner(self):
        """Gets the device_owner of this Port.

        功能说明：设备所属 取值范围：合法设备所属，如network:dhcp、neutron:VIP_PORT、network:router_interface_distributed、network:router_centralized_snat 约束：不支持设置和更新，由系统自动维护

        :return: The device_owner of this Port.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this Port.

        功能说明：设备所属 取值范围：合法设备所属，如network:dhcp、neutron:VIP_PORT、network:router_interface_distributed、network:router_centralized_snat 约束：不支持设置和更新，由系统自动维护

        :param device_owner: The device_owner of this Port.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Port.

        项目ID

        :return: The tenant_id of this Port.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Port.

        项目ID

        :param tenant_id: The tenant_id of this Port.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def status(self):
        """Gets the status of this Port.

        功能说明：端口状态，Hana硬直通虚拟机端口状态总为DOWN 取值范围：ACTIVE、BUILD、DOWN

        :return: The status of this Port.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Port.

        功能说明：端口状态，Hana硬直通虚拟机端口状态总为DOWN 取值范围：ACTIVE、BUILD、DOWN

        :param status: The status of this Port.
        :type status: str
        """
        self._status = status

    @property
    def security_groups(self):
        """Gets the security_groups of this Port.

        安全组的ID列表

        :return: The security_groups of this Port.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this Port.

        安全组的ID列表

        :param security_groups: The security_groups of this Port.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def allowed_address_pairs(self):
        """Gets the allowed_address_pairs of this Port.

        功能说明：IP/Mac对列表 约束：IP地址不允许为 “0.0.0.0” 如果配置地址池较大（CIDR掩码小于24位），建议为该port配置一个单独的安全组。

        :return: The allowed_address_pairs of this Port.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        """Sets the allowed_address_pairs of this Port.

        功能说明：IP/Mac对列表 约束：IP地址不允许为 “0.0.0.0” 如果配置地址池较大（CIDR掩码小于24位），建议为该port配置一个单独的安全组。

        :param allowed_address_pairs: The allowed_address_pairs of this Port.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v2.AllowedAddressPair`]
        """
        self._allowed_address_pairs = allowed_address_pairs

    @property
    def extra_dhcp_opts(self):
        """Gets the extra_dhcp_opts of this Port.

        功能说明：DHCP的扩展Option(扩展属性)

        :return: The extra_dhcp_opts of this Port.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOpt`]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        """Sets the extra_dhcp_opts of this Port.

        功能说明：DHCP的扩展Option(扩展属性)

        :param extra_dhcp_opts: The extra_dhcp_opts of this Port.
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOpt`]
        """
        self._extra_dhcp_opts = extra_dhcp_opts

    @property
    def bindingvnic_type(self):
        """Gets the bindingvnic_type of this Port.

        功能说明：绑定的vNIC类型 取值范围：  - normal（软交换）  - direct: SRIOV硬直通（不支持） 

        :return: The bindingvnic_type of this Port.
        :rtype: str
        """
        return self._bindingvnic_type

    @bindingvnic_type.setter
    def bindingvnic_type(self, bindingvnic_type):
        """Sets the bindingvnic_type of this Port.

        功能说明：绑定的vNIC类型 取值范围：  - normal（软交换）  - direct: SRIOV硬直通（不支持） 

        :param bindingvnic_type: The bindingvnic_type of this Port.
        :type bindingvnic_type: str
        """
        self._bindingvnic_type = bindingvnic_type

    @property
    def dns_assignment(self):
        """Gets the dns_assignment of this Port.

        功能说明：主网卡默认内网域名信息 约束：不支持设置和更新，由系统自动维护

        :return: The dns_assignment of this Port.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.DnsAssignMent`]
        """
        return self._dns_assignment

    @dns_assignment.setter
    def dns_assignment(self, dns_assignment):
        """Sets the dns_assignment of this Port.

        功能说明：主网卡默认内网域名信息 约束：不支持设置和更新，由系统自动维护

        :param dns_assignment: The dns_assignment of this Port.
        :type dns_assignment: list[:class:`huaweicloudsdkvpc.v2.DnsAssignMent`]
        """
        self._dns_assignment = dns_assignment

    @property
    def dns_name(self):
        """Gets the dns_name of this Port.

        功能说明：主网卡默认内网DNS名称 约束：不支持设置和更新，由系统自动维护

        :return: The dns_name of this Port.
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """Sets the dns_name of this Port.

        功能说明：主网卡默认内网DNS名称 约束：不支持设置和更新，由系统自动维护

        :param dns_name: The dns_name of this Port.
        :type dns_name: str
        """
        self._dns_name = dns_name

    @property
    def bindingvif_details(self):
        """Gets the bindingvif_details of this Port.


        :return: The bindingvif_details of this Port.
        :rtype: :class:`huaweicloudsdkvpc.v2.BindingVifDetails`
        """
        return self._bindingvif_details

    @bindingvif_details.setter
    def bindingvif_details(self, bindingvif_details):
        """Sets the bindingvif_details of this Port.


        :param bindingvif_details: The bindingvif_details of this Port.
        :type bindingvif_details: :class:`huaweicloudsdkvpc.v2.BindingVifDetails`
        """
        self._bindingvif_details = bindingvif_details

    @property
    def bindingprofile(self):
        """Gets the bindingprofile of this Port.

        功能说明：提供用户设置自定义信息(扩展属性)

        :return: The bindingprofile of this Port.
        :rtype: object
        """
        return self._bindingprofile

    @bindingprofile.setter
    def bindingprofile(self, bindingprofile):
        """Sets the bindingprofile of this Port.

        功能说明：提供用户设置自定义信息(扩展属性)

        :param bindingprofile: The bindingprofile of this Port.
        :type bindingprofile: object
        """
        self._bindingprofile = bindingprofile

    @property
    def instance_id(self):
        """Gets the instance_id of this Port.

        功能说明：端口所属实例ID，例如RDS实例ID 约束：不支持设置和更新，由系统自动维护

        :return: The instance_id of this Port.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Port.

        功能说明：端口所属实例ID，例如RDS实例ID 约束：不支持设置和更新，由系统自动维护

        :param instance_id: The instance_id of this Port.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this Port.

        功能说明：端口所属实例类型，例如“RDS” 约束：不支持设置和更新，由系统自动维护

        :return: The instance_type of this Port.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this Port.

        功能说明：端口所属实例类型，例如“RDS” 约束：不支持设置和更新，由系统自动维护

        :param instance_type: The instance_type of this Port.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def port_security_enabled(self):
        """Gets the port_security_enabled of this Port.

        功能说明：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效 取值范围：启用（true）或禁用（false）

        :return: The port_security_enabled of this Port.
        :rtype: bool
        """
        return self._port_security_enabled

    @port_security_enabled.setter
    def port_security_enabled(self, port_security_enabled):
        """Sets the port_security_enabled of this Port.

        功能说明：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效 取值范围：启用（true）或禁用（false）

        :param port_security_enabled: The port_security_enabled of this Port.
        :type port_security_enabled: bool
        """
        self._port_security_enabled = port_security_enabled

    @property
    def zone_id(self):
        """Gets the zone_id of this Port.

        功能说明：port所属的可用分区

        :return: The zone_id of this Port.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this Port.

        功能说明：port所属的可用分区

        :param zone_id: The zone_id of this Port.
        :type zone_id: str
        """
        self._zone_id = zone_id

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
        if not isinstance(other, Port):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
