# coding: utf-8

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
        'admin_state_up': 'bool',
        'bindinghost_id': 'str',
        'bindingprofile': 'object',
        'bindingvif_details': 'BindingVifDetails',
        'bindingvif_type': 'str',
        'bindingvnic_type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'description': 'str',
        'device_id': 'str',
        'device_owner': 'str',
        'ecs_flavor': 'str',
        'id': 'str',
        'instance_id': 'str',
        'instance_type': 'str',
        'mac_address': 'str',
        'name': 'str',
        'port_security_enabled': 'bool',
        'private_ips': 'list[PrivateIpInfo]',
        'project_id': 'str',
        'security_groups': 'list[str]',
        'status': 'str',
        'tenant_id': 'str',
        'virsubnet_id': 'str',
        'vpc_id': 'str',
        'vpc_tenant_id': 'str',
        'vtep_ip': 'str',
        'enable_efi': 'bool',
        'scope': 'str',
        'zone_id': 'str',
        'bindingmigration_info': 'object',
        'extra_dhcp_opts': 'list[PortExtraDhcpOpt]',
        'position_type': 'str',
        'instance_info': 'object',
        'tags': 'list[ResponseTag]',
        'allowed_address_pairs': 'list[AllowedAddressPair]'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'bindinghost_id': 'binding:host_id',
        'bindingprofile': 'binding:profile',
        'bindingvif_details': 'binding:vif_details',
        'bindingvif_type': 'binding:vif_type',
        'bindingvnic_type': 'binding:vnic_type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'description': 'description',
        'device_id': 'device_id',
        'device_owner': 'device_owner',
        'ecs_flavor': 'ecs_flavor',
        'id': 'id',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type',
        'mac_address': 'mac_address',
        'name': 'name',
        'port_security_enabled': 'port_security_enabled',
        'private_ips': 'private_ips',
        'project_id': 'project_id',
        'security_groups': 'security_groups',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'virsubnet_id': 'virsubnet_id',
        'vpc_id': 'vpc_id',
        'vpc_tenant_id': 'vpc_tenant_id',
        'vtep_ip': 'vtep_ip',
        'enable_efi': 'enable_efi',
        'scope': 'scope',
        'zone_id': 'zone_id',
        'bindingmigration_info': 'binding:migration_info',
        'extra_dhcp_opts': 'extra_dhcp_opts',
        'position_type': 'position_type',
        'instance_info': 'instance_info',
        'tags': 'tags',
        'allowed_address_pairs': 'allowed_address_pairs'
    }

    def __init__(self, admin_state_up=None, bindinghost_id=None, bindingprofile=None, bindingvif_details=None, bindingvif_type=None, bindingvnic_type=None, created_at=None, updated_at=None, description=None, device_id=None, device_owner=None, ecs_flavor=None, id=None, instance_id=None, instance_type=None, mac_address=None, name=None, port_security_enabled=None, private_ips=None, project_id=None, security_groups=None, status=None, tenant_id=None, virsubnet_id=None, vpc_id=None, vpc_tenant_id=None, vtep_ip=None, enable_efi=None, scope=None, zone_id=None, bindingmigration_info=None, extra_dhcp_opts=None, position_type=None, instance_info=None, tags=None, allowed_address_pairs=None):
        r"""Port

        The model defined in huaweicloud sdk

        :param admin_state_up: **参数解释**： 端口的管理状态。 **取值范围**： true，false，默认值true。
        :type admin_state_up: bool
        :param bindinghost_id: **参数解释**： 端口所在的主机ID。 **取值范围**： 不涉及。
        :type bindinghost_id: str
        :param bindingprofile: **参数解释**： 端口的用户自定义信息。 **取值范围**： 不涉及。
        :type bindingprofile: object
        :param bindingvif_details: 
        :type bindingvif_details: :class:`huaweicloudsdkvpc.v3.BindingVifDetails`
        :param bindingvif_type: **参数解释**： 端口绑定的虚拟接口类型 (ovs/hw_veb等)，扩展属性。 **取值范围**： - ovs：表示使用 Open vSwitch（OVS）作为虚拟交换机 - bridge：表示使用 Linux 内核桥接（bridge）实现虚拟网络 - hw_veb：表示硬件虚拟以太网桥（Hardware Virtual Ethernet Bridge），通常用于支持 SR-IOV 的硬件网卡 - vhostuser：表示使用 vhost-user 协议（基于 Unix 域套接字）与外部虚拟交换机通信 - distributed：表示用于分布式虚拟交换机 - binding_failed：表示端口绑定失败 - unbound：表示该端口未绑定到任何网络后端
        :type bindingvif_type: str
        :param bindingvnic_type: **参数解释**： 绑定的vNIC类型。 **取值范围**： - normal: 软交换。 - direct: SRIOV硬直通（不支持）。 - baremetal：用于裸金属服务器。
        :type bindingvnic_type: str
        :param created_at: **参数解释**： 端口的创建时间。 **取值范围**： UTC时间，格式: yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: **参数解释**： 端口的最近一次更新的时间。 **取值范围**： UTC时间，格式: yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param description: **参数解释**： 端口的描述信息。 **取值范围**： 0-255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param device_id: **参数解释**： 端口所属的设备ID。 **取值范围**： 带“-”的标准UUID格式。
        :type device_id: str
        :param device_owner: **参数解释**： 端口所属的设备名称。 **取值范围**： - network:dhcp, 表示DHCP服务 - network:router_interface_distributed, 表示子网网关地址 - compute:xxx, 表示云服务器网卡私有IP地址，其中XXX对应具体的可用区名称，例如compute:aa-bb-cc表示私有IP地址被可用区aa-bb-cc内的云服务器使用 - neutron:VIP_PORT, 表示虚拟IP地址 - neutron:LOADBALANCERV2, 表示共享型ELB - neutron:LOADBALANCERV3, 表示独享型ELB - network:endpoint_interface, 表示VPC终端节点 - network:nat_gateway, 表示NAT网关 - network:ucmp, 表示UCMP端口，为企业路由器服务所用
        :type device_owner: str
        :param ecs_flavor: **参数解释**： 标识此端口所属云服务器的flavor。 **取值范围**： 不涉及。
        :type ecs_flavor: str
        :param id: **参数解释**： 端口的资源ID。 **取值范围**： 带“-”的标准UUID格式。
        :type id: str
        :param instance_id: **参数解释**： 端口所属的云服务实例ID，例如RDS实例ID。 **取值范围**： 不涉及。
        :type instance_id: str
        :param instance_type: **参数解释**： 端口所属的云服务实例类型，例如“RDS”。 **取值范围**： 不涉及。
        :type instance_type: str
        :param mac_address: **参数解释**： 端口的MAC地址。 **取值范围**： 不涉及
        :type mac_address: str
        :param name: **参数解释**： 端口的名称。 **取值范围**： 默认为空，最大长度不超过255。
        :type name: str
        :param port_security_enabled: **参数解释**： 端口的安全使能标记，如果不使能，则安全组和DHCP防欺骗不生效。 **取值范围**： - true：使能端口安全。 - false：未使能端口安全。
        :type port_security_enabled: bool
        :param private_ips: **参数解释**： 端口的私有IP地址。 **取值范围**： 不涉及。
        :type private_ips: list[:class:`huaweicloudsdkvpc.v3.PrivateIpInfo`]
        :param project_id: **参数解释**： 端口所属的项目ID。 **取值范围**： 不涉及。
        :type project_id: str
        :param security_groups: **参数解释**： 端口绑定的安全组列表。 **取值范围**： 不涉及。
        :type security_groups: list[str]
        :param status: **参数解释**： 端口的状态。 **取值范围**： - ACTIVE：端口处于活动状态，可以正常进行网络通信。 - BUILD：端口正在创建或配置中。 - DOWN：端口处于非活动状态，不能进行网络通信。Hana 硬直通虚拟机端口状态总为DOWN。
        :type status: str
        :param tenant_id: **参数解释**： 端口所属的租户ID。 **取值范围**： 不涉及。
        :type tenant_id: str
        :param virsubnet_id: **参数解释**： 端口所在的虚拟子网ID。 **取值范围**： 带“-”的标准UUID格式。
        :type virsubnet_id: str
        :param vpc_id: **参数解释**： 端口所在的VPC的ID。 **取值范围**： 带“-”的标准UUID格式。
        :type vpc_id: str
        :param vpc_tenant_id: **参数解释**： 端口所在的VPC的租户ID。 **取值范围**： 不涉及。
        :type vpc_tenant_id: str
        :param vtep_ip: **参数解释**： 端口的VTEP IP地址，即虚拟隧道端点的 IP 地址。 **取值范围**： 不涉及。
        :type vtep_ip: str
        :param enable_efi: **参数解释**： 是否使能efi，使能则表示端口支持vRoCE能力。 **取值范围**： - true：使能efi。 - false：未使能efi。
        :type enable_efi: bool
        :param scope: **参数解释**： 端口所在子网的作用域（边缘云场景）。 **取值范围**： - center：表示作用域为中心。 - {publicBorderGroup}：表示作用域为具体的公网边界组。公网边界组限制子网的可用区范围，可关联多个边缘可用区。
        :type scope: str
        :param zone_id: **参数解释**： 端口所属的可用分区的ID。 **取值范围**： 不涉及。
        :type zone_id: str
        :param bindingmigration_info: **参数解释**： 端口迁移的目的节点信息，包括目的节点的binding:vif_details和binding:vif_type。 **取值范围**： 不涉及。
        :type bindingmigration_info: object
        :param extra_dhcp_opts: **参数解释**： DHCP的扩展属性。 **取值范围**： 不涉及。
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v3.PortExtraDhcpOpt`]
        :param position_type: **参数解释**： 边缘场景端口的位置类型。 **取值范围**： 默认值center。
        :type position_type: str
        :param instance_info: **参数解释**： 端口绑定的实例信息。 **取值范围**： 不涉及。
        :type instance_info: object
        :param tags: **参数解释**： 端口的标签信息，包括标签键和标签值，可用来分类和标识资源。详情请参见Tag对象。 **取值范围**： 不涉及。
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResponseTag`]
        :param allowed_address_pairs: **参数解释**： 端口的IP/Mac对列表。 **取值范围**： - IP地址不允许为 “0.0.0.0/0”。 - 如果allowed_address_pairs配置地址池较大的IP网段（掩码小于24位），建议为该端口配置一个单独的安全组。 - 如果allowed_address_pairs的IP地址为“1.1.1.1/0”，表示关闭源目地址检查开关。 - 被绑定的云服务器网卡allowed_address_pairs的IP地址填“1.1.1.1/0”。
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v3.AllowedAddressPair`]
        """
        
        

        self._admin_state_up = None
        self._bindinghost_id = None
        self._bindingprofile = None
        self._bindingvif_details = None
        self._bindingvif_type = None
        self._bindingvnic_type = None
        self._created_at = None
        self._updated_at = None
        self._description = None
        self._device_id = None
        self._device_owner = None
        self._ecs_flavor = None
        self._id = None
        self._instance_id = None
        self._instance_type = None
        self._mac_address = None
        self._name = None
        self._port_security_enabled = None
        self._private_ips = None
        self._project_id = None
        self._security_groups = None
        self._status = None
        self._tenant_id = None
        self._virsubnet_id = None
        self._vpc_id = None
        self._vpc_tenant_id = None
        self._vtep_ip = None
        self._enable_efi = None
        self._scope = None
        self._zone_id = None
        self._bindingmigration_info = None
        self._extra_dhcp_opts = None
        self._position_type = None
        self._instance_info = None
        self._tags = None
        self._allowed_address_pairs = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.bindinghost_id = bindinghost_id
        self.bindingprofile = bindingprofile
        self.bindingvif_details = bindingvif_details
        self.bindingvif_type = bindingvif_type
        self.bindingvnic_type = bindingvnic_type
        self.created_at = created_at
        self.updated_at = updated_at
        self.description = description
        self.device_id = device_id
        self.device_owner = device_owner
        self.ecs_flavor = ecs_flavor
        self.id = id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.mac_address = mac_address
        self.name = name
        self.port_security_enabled = port_security_enabled
        self.private_ips = private_ips
        self.project_id = project_id
        self.security_groups = security_groups
        self.status = status
        self.tenant_id = tenant_id
        self.virsubnet_id = virsubnet_id
        self.vpc_id = vpc_id
        self.vpc_tenant_id = vpc_tenant_id
        self.vtep_ip = vtep_ip
        self.enable_efi = enable_efi
        self.scope = scope
        self.zone_id = zone_id
        self.bindingmigration_info = bindingmigration_info
        self.extra_dhcp_opts = extra_dhcp_opts
        self.position_type = position_type
        self.instance_info = instance_info
        self.tags = tags
        self.allowed_address_pairs = allowed_address_pairs

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this Port.

        **参数解释**： 端口的管理状态。 **取值范围**： true，false，默认值true。

        :return: The admin_state_up of this Port.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this Port.

        **参数解释**： 端口的管理状态。 **取值范围**： true，false，默认值true。

        :param admin_state_up: The admin_state_up of this Port.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def bindinghost_id(self):
        r"""Gets the bindinghost_id of this Port.

        **参数解释**： 端口所在的主机ID。 **取值范围**： 不涉及。

        :return: The bindinghost_id of this Port.
        :rtype: str
        """
        return self._bindinghost_id

    @bindinghost_id.setter
    def bindinghost_id(self, bindinghost_id):
        r"""Sets the bindinghost_id of this Port.

        **参数解释**： 端口所在的主机ID。 **取值范围**： 不涉及。

        :param bindinghost_id: The bindinghost_id of this Port.
        :type bindinghost_id: str
        """
        self._bindinghost_id = bindinghost_id

    @property
    def bindingprofile(self):
        r"""Gets the bindingprofile of this Port.

        **参数解释**： 端口的用户自定义信息。 **取值范围**： 不涉及。

        :return: The bindingprofile of this Port.
        :rtype: object
        """
        return self._bindingprofile

    @bindingprofile.setter
    def bindingprofile(self, bindingprofile):
        r"""Sets the bindingprofile of this Port.

        **参数解释**： 端口的用户自定义信息。 **取值范围**： 不涉及。

        :param bindingprofile: The bindingprofile of this Port.
        :type bindingprofile: object
        """
        self._bindingprofile = bindingprofile

    @property
    def bindingvif_details(self):
        r"""Gets the bindingvif_details of this Port.

        :return: The bindingvif_details of this Port.
        :rtype: :class:`huaweicloudsdkvpc.v3.BindingVifDetails`
        """
        return self._bindingvif_details

    @bindingvif_details.setter
    def bindingvif_details(self, bindingvif_details):
        r"""Sets the bindingvif_details of this Port.

        :param bindingvif_details: The bindingvif_details of this Port.
        :type bindingvif_details: :class:`huaweicloudsdkvpc.v3.BindingVifDetails`
        """
        self._bindingvif_details = bindingvif_details

    @property
    def bindingvif_type(self):
        r"""Gets the bindingvif_type of this Port.

        **参数解释**： 端口绑定的虚拟接口类型 (ovs/hw_veb等)，扩展属性。 **取值范围**： - ovs：表示使用 Open vSwitch（OVS）作为虚拟交换机 - bridge：表示使用 Linux 内核桥接（bridge）实现虚拟网络 - hw_veb：表示硬件虚拟以太网桥（Hardware Virtual Ethernet Bridge），通常用于支持 SR-IOV 的硬件网卡 - vhostuser：表示使用 vhost-user 协议（基于 Unix 域套接字）与外部虚拟交换机通信 - distributed：表示用于分布式虚拟交换机 - binding_failed：表示端口绑定失败 - unbound：表示该端口未绑定到任何网络后端

        :return: The bindingvif_type of this Port.
        :rtype: str
        """
        return self._bindingvif_type

    @bindingvif_type.setter
    def bindingvif_type(self, bindingvif_type):
        r"""Sets the bindingvif_type of this Port.

        **参数解释**： 端口绑定的虚拟接口类型 (ovs/hw_veb等)，扩展属性。 **取值范围**： - ovs：表示使用 Open vSwitch（OVS）作为虚拟交换机 - bridge：表示使用 Linux 内核桥接（bridge）实现虚拟网络 - hw_veb：表示硬件虚拟以太网桥（Hardware Virtual Ethernet Bridge），通常用于支持 SR-IOV 的硬件网卡 - vhostuser：表示使用 vhost-user 协议（基于 Unix 域套接字）与外部虚拟交换机通信 - distributed：表示用于分布式虚拟交换机 - binding_failed：表示端口绑定失败 - unbound：表示该端口未绑定到任何网络后端

        :param bindingvif_type: The bindingvif_type of this Port.
        :type bindingvif_type: str
        """
        self._bindingvif_type = bindingvif_type

    @property
    def bindingvnic_type(self):
        r"""Gets the bindingvnic_type of this Port.

        **参数解释**： 绑定的vNIC类型。 **取值范围**： - normal: 软交换。 - direct: SRIOV硬直通（不支持）。 - baremetal：用于裸金属服务器。

        :return: The bindingvnic_type of this Port.
        :rtype: str
        """
        return self._bindingvnic_type

    @bindingvnic_type.setter
    def bindingvnic_type(self, bindingvnic_type):
        r"""Sets the bindingvnic_type of this Port.

        **参数解释**： 绑定的vNIC类型。 **取值范围**： - normal: 软交换。 - direct: SRIOV硬直通（不支持）。 - baremetal：用于裸金属服务器。

        :param bindingvnic_type: The bindingvnic_type of this Port.
        :type bindingvnic_type: str
        """
        self._bindingvnic_type = bindingvnic_type

    @property
    def created_at(self):
        r"""Gets the created_at of this Port.

        **参数解释**： 端口的创建时间。 **取值范围**： UTC时间，格式: yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this Port.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Port.

        **参数解释**： 端口的创建时间。 **取值范围**： UTC时间，格式: yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this Port.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Port.

        **参数解释**： 端口的最近一次更新的时间。 **取值范围**： UTC时间，格式: yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this Port.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Port.

        **参数解释**： 端口的最近一次更新的时间。 **取值范围**： UTC时间，格式: yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this Port.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def description(self):
        r"""Gets the description of this Port.

        **参数解释**： 端口的描述信息。 **取值范围**： 0-255个字符，不能包含“<”和“>”。

        :return: The description of this Port.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Port.

        **参数解释**： 端口的描述信息。 **取值范围**： 0-255个字符，不能包含“<”和“>”。

        :param description: The description of this Port.
        :type description: str
        """
        self._description = description

    @property
    def device_id(self):
        r"""Gets the device_id of this Port.

        **参数解释**： 端口所属的设备ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The device_id of this Port.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this Port.

        **参数解释**： 端口所属的设备ID。 **取值范围**： 带“-”的标准UUID格式。

        :param device_id: The device_id of this Port.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_owner(self):
        r"""Gets the device_owner of this Port.

        **参数解释**： 端口所属的设备名称。 **取值范围**： - network:dhcp, 表示DHCP服务 - network:router_interface_distributed, 表示子网网关地址 - compute:xxx, 表示云服务器网卡私有IP地址，其中XXX对应具体的可用区名称，例如compute:aa-bb-cc表示私有IP地址被可用区aa-bb-cc内的云服务器使用 - neutron:VIP_PORT, 表示虚拟IP地址 - neutron:LOADBALANCERV2, 表示共享型ELB - neutron:LOADBALANCERV3, 表示独享型ELB - network:endpoint_interface, 表示VPC终端节点 - network:nat_gateway, 表示NAT网关 - network:ucmp, 表示UCMP端口，为企业路由器服务所用

        :return: The device_owner of this Port.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        r"""Sets the device_owner of this Port.

        **参数解释**： 端口所属的设备名称。 **取值范围**： - network:dhcp, 表示DHCP服务 - network:router_interface_distributed, 表示子网网关地址 - compute:xxx, 表示云服务器网卡私有IP地址，其中XXX对应具体的可用区名称，例如compute:aa-bb-cc表示私有IP地址被可用区aa-bb-cc内的云服务器使用 - neutron:VIP_PORT, 表示虚拟IP地址 - neutron:LOADBALANCERV2, 表示共享型ELB - neutron:LOADBALANCERV3, 表示独享型ELB - network:endpoint_interface, 表示VPC终端节点 - network:nat_gateway, 表示NAT网关 - network:ucmp, 表示UCMP端口，为企业路由器服务所用

        :param device_owner: The device_owner of this Port.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def ecs_flavor(self):
        r"""Gets the ecs_flavor of this Port.

        **参数解释**： 标识此端口所属云服务器的flavor。 **取值范围**： 不涉及。

        :return: The ecs_flavor of this Port.
        :rtype: str
        """
        return self._ecs_flavor

    @ecs_flavor.setter
    def ecs_flavor(self, ecs_flavor):
        r"""Sets the ecs_flavor of this Port.

        **参数解释**： 标识此端口所属云服务器的flavor。 **取值范围**： 不涉及。

        :param ecs_flavor: The ecs_flavor of this Port.
        :type ecs_flavor: str
        """
        self._ecs_flavor = ecs_flavor

    @property
    def id(self):
        r"""Gets the id of this Port.

        **参数解释**： 端口的资源ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The id of this Port.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Port.

        **参数解释**： 端口的资源ID。 **取值范围**： 带“-”的标准UUID格式。

        :param id: The id of this Port.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this Port.

        **参数解释**： 端口所属的云服务实例ID，例如RDS实例ID。 **取值范围**： 不涉及。

        :return: The instance_id of this Port.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this Port.

        **参数解释**： 端口所属的云服务实例ID，例如RDS实例ID。 **取值范围**： 不涉及。

        :param instance_id: The instance_id of this Port.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this Port.

        **参数解释**： 端口所属的云服务实例类型，例如“RDS”。 **取值范围**： 不涉及。

        :return: The instance_type of this Port.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this Port.

        **参数解释**： 端口所属的云服务实例类型，例如“RDS”。 **取值范围**： 不涉及。

        :param instance_type: The instance_type of this Port.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def mac_address(self):
        r"""Gets the mac_address of this Port.

        **参数解释**： 端口的MAC地址。 **取值范围**： 不涉及

        :return: The mac_address of this Port.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        r"""Sets the mac_address of this Port.

        **参数解释**： 端口的MAC地址。 **取值范围**： 不涉及

        :param mac_address: The mac_address of this Port.
        :type mac_address: str
        """
        self._mac_address = mac_address

    @property
    def name(self):
        r"""Gets the name of this Port.

        **参数解释**： 端口的名称。 **取值范围**： 默认为空，最大长度不超过255。

        :return: The name of this Port.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Port.

        **参数解释**： 端口的名称。 **取值范围**： 默认为空，最大长度不超过255。

        :param name: The name of this Port.
        :type name: str
        """
        self._name = name

    @property
    def port_security_enabled(self):
        r"""Gets the port_security_enabled of this Port.

        **参数解释**： 端口的安全使能标记，如果不使能，则安全组和DHCP防欺骗不生效。 **取值范围**： - true：使能端口安全。 - false：未使能端口安全。

        :return: The port_security_enabled of this Port.
        :rtype: bool
        """
        return self._port_security_enabled

    @port_security_enabled.setter
    def port_security_enabled(self, port_security_enabled):
        r"""Sets the port_security_enabled of this Port.

        **参数解释**： 端口的安全使能标记，如果不使能，则安全组和DHCP防欺骗不生效。 **取值范围**： - true：使能端口安全。 - false：未使能端口安全。

        :param port_security_enabled: The port_security_enabled of this Port.
        :type port_security_enabled: bool
        """
        self._port_security_enabled = port_security_enabled

    @property
    def private_ips(self):
        r"""Gets the private_ips of this Port.

        **参数解释**： 端口的私有IP地址。 **取值范围**： 不涉及。

        :return: The private_ips of this Port.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.PrivateIpInfo`]
        """
        return self._private_ips

    @private_ips.setter
    def private_ips(self, private_ips):
        r"""Sets the private_ips of this Port.

        **参数解释**： 端口的私有IP地址。 **取值范围**： 不涉及。

        :param private_ips: The private_ips of this Port.
        :type private_ips: list[:class:`huaweicloudsdkvpc.v3.PrivateIpInfo`]
        """
        self._private_ips = private_ips

    @property
    def project_id(self):
        r"""Gets the project_id of this Port.

        **参数解释**： 端口所属的项目ID。 **取值范围**： 不涉及。

        :return: The project_id of this Port.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Port.

        **参数解释**： 端口所属的项目ID。 **取值范围**： 不涉及。

        :param project_id: The project_id of this Port.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def security_groups(self):
        r"""Gets the security_groups of this Port.

        **参数解释**： 端口绑定的安全组列表。 **取值范围**： 不涉及。

        :return: The security_groups of this Port.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this Port.

        **参数解释**： 端口绑定的安全组列表。 **取值范围**： 不涉及。

        :param security_groups: The security_groups of this Port.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def status(self):
        r"""Gets the status of this Port.

        **参数解释**： 端口的状态。 **取值范围**： - ACTIVE：端口处于活动状态，可以正常进行网络通信。 - BUILD：端口正在创建或配置中。 - DOWN：端口处于非活动状态，不能进行网络通信。Hana 硬直通虚拟机端口状态总为DOWN。

        :return: The status of this Port.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Port.

        **参数解释**： 端口的状态。 **取值范围**： - ACTIVE：端口处于活动状态，可以正常进行网络通信。 - BUILD：端口正在创建或配置中。 - DOWN：端口处于非活动状态，不能进行网络通信。Hana 硬直通虚拟机端口状态总为DOWN。

        :param status: The status of this Port.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this Port.

        **参数解释**： 端口所属的租户ID。 **取值范围**： 不涉及。

        :return: The tenant_id of this Port.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this Port.

        **参数解释**： 端口所属的租户ID。 **取值范围**： 不涉及。

        :param tenant_id: The tenant_id of this Port.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this Port.

        **参数解释**： 端口所在的虚拟子网ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The virsubnet_id of this Port.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this Port.

        **参数解释**： 端口所在的虚拟子网ID。 **取值范围**： 带“-”的标准UUID格式。

        :param virsubnet_id: The virsubnet_id of this Port.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this Port.

        **参数解释**： 端口所在的VPC的ID。 **取值范围**： 带“-”的标准UUID格式。

        :return: The vpc_id of this Port.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this Port.

        **参数解释**： 端口所在的VPC的ID。 **取值范围**： 带“-”的标准UUID格式。

        :param vpc_id: The vpc_id of this Port.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_tenant_id(self):
        r"""Gets the vpc_tenant_id of this Port.

        **参数解释**： 端口所在的VPC的租户ID。 **取值范围**： 不涉及。

        :return: The vpc_tenant_id of this Port.
        :rtype: str
        """
        return self._vpc_tenant_id

    @vpc_tenant_id.setter
    def vpc_tenant_id(self, vpc_tenant_id):
        r"""Sets the vpc_tenant_id of this Port.

        **参数解释**： 端口所在的VPC的租户ID。 **取值范围**： 不涉及。

        :param vpc_tenant_id: The vpc_tenant_id of this Port.
        :type vpc_tenant_id: str
        """
        self._vpc_tenant_id = vpc_tenant_id

    @property
    def vtep_ip(self):
        r"""Gets the vtep_ip of this Port.

        **参数解释**： 端口的VTEP IP地址，即虚拟隧道端点的 IP 地址。 **取值范围**： 不涉及。

        :return: The vtep_ip of this Port.
        :rtype: str
        """
        return self._vtep_ip

    @vtep_ip.setter
    def vtep_ip(self, vtep_ip):
        r"""Sets the vtep_ip of this Port.

        **参数解释**： 端口的VTEP IP地址，即虚拟隧道端点的 IP 地址。 **取值范围**： 不涉及。

        :param vtep_ip: The vtep_ip of this Port.
        :type vtep_ip: str
        """
        self._vtep_ip = vtep_ip

    @property
    def enable_efi(self):
        r"""Gets the enable_efi of this Port.

        **参数解释**： 是否使能efi，使能则表示端口支持vRoCE能力。 **取值范围**： - true：使能efi。 - false：未使能efi。

        :return: The enable_efi of this Port.
        :rtype: bool
        """
        return self._enable_efi

    @enable_efi.setter
    def enable_efi(self, enable_efi):
        r"""Sets the enable_efi of this Port.

        **参数解释**： 是否使能efi，使能则表示端口支持vRoCE能力。 **取值范围**： - true：使能efi。 - false：未使能efi。

        :param enable_efi: The enable_efi of this Port.
        :type enable_efi: bool
        """
        self._enable_efi = enable_efi

    @property
    def scope(self):
        r"""Gets the scope of this Port.

        **参数解释**： 端口所在子网的作用域（边缘云场景）。 **取值范围**： - center：表示作用域为中心。 - {publicBorderGroup}：表示作用域为具体的公网边界组。公网边界组限制子网的可用区范围，可关联多个边缘可用区。

        :return: The scope of this Port.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this Port.

        **参数解释**： 端口所在子网的作用域（边缘云场景）。 **取值范围**： - center：表示作用域为中心。 - {publicBorderGroup}：表示作用域为具体的公网边界组。公网边界组限制子网的可用区范围，可关联多个边缘可用区。

        :param scope: The scope of this Port.
        :type scope: str
        """
        self._scope = scope

    @property
    def zone_id(self):
        r"""Gets the zone_id of this Port.

        **参数解释**： 端口所属的可用分区的ID。 **取值范围**： 不涉及。

        :return: The zone_id of this Port.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        r"""Sets the zone_id of this Port.

        **参数解释**： 端口所属的可用分区的ID。 **取值范围**： 不涉及。

        :param zone_id: The zone_id of this Port.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def bindingmigration_info(self):
        r"""Gets the bindingmigration_info of this Port.

        **参数解释**： 端口迁移的目的节点信息，包括目的节点的binding:vif_details和binding:vif_type。 **取值范围**： 不涉及。

        :return: The bindingmigration_info of this Port.
        :rtype: object
        """
        return self._bindingmigration_info

    @bindingmigration_info.setter
    def bindingmigration_info(self, bindingmigration_info):
        r"""Sets the bindingmigration_info of this Port.

        **参数解释**： 端口迁移的目的节点信息，包括目的节点的binding:vif_details和binding:vif_type。 **取值范围**： 不涉及。

        :param bindingmigration_info: The bindingmigration_info of this Port.
        :type bindingmigration_info: object
        """
        self._bindingmigration_info = bindingmigration_info

    @property
    def extra_dhcp_opts(self):
        r"""Gets the extra_dhcp_opts of this Port.

        **参数解释**： DHCP的扩展属性。 **取值范围**： 不涉及。

        :return: The extra_dhcp_opts of this Port.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.PortExtraDhcpOpt`]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        r"""Sets the extra_dhcp_opts of this Port.

        **参数解释**： DHCP的扩展属性。 **取值范围**： 不涉及。

        :param extra_dhcp_opts: The extra_dhcp_opts of this Port.
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v3.PortExtraDhcpOpt`]
        """
        self._extra_dhcp_opts = extra_dhcp_opts

    @property
    def position_type(self):
        r"""Gets the position_type of this Port.

        **参数解释**： 边缘场景端口的位置类型。 **取值范围**： 默认值center。

        :return: The position_type of this Port.
        :rtype: str
        """
        return self._position_type

    @position_type.setter
    def position_type(self, position_type):
        r"""Sets the position_type of this Port.

        **参数解释**： 边缘场景端口的位置类型。 **取值范围**： 默认值center。

        :param position_type: The position_type of this Port.
        :type position_type: str
        """
        self._position_type = position_type

    @property
    def instance_info(self):
        r"""Gets the instance_info of this Port.

        **参数解释**： 端口绑定的实例信息。 **取值范围**： 不涉及。

        :return: The instance_info of this Port.
        :rtype: object
        """
        return self._instance_info

    @instance_info.setter
    def instance_info(self, instance_info):
        r"""Sets the instance_info of this Port.

        **参数解释**： 端口绑定的实例信息。 **取值范围**： 不涉及。

        :param instance_info: The instance_info of this Port.
        :type instance_info: object
        """
        self._instance_info = instance_info

    @property
    def tags(self):
        r"""Gets the tags of this Port.

        **参数解释**： 端口的标签信息，包括标签键和标签值，可用来分类和标识资源。详情请参见Tag对象。 **取值范围**： 不涉及。

        :return: The tags of this Port.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.ResponseTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Port.

        **参数解释**： 端口的标签信息，包括标签键和标签值，可用来分类和标识资源。详情请参见Tag对象。 **取值范围**： 不涉及。

        :param tags: The tags of this Port.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.ResponseTag`]
        """
        self._tags = tags

    @property
    def allowed_address_pairs(self):
        r"""Gets the allowed_address_pairs of this Port.

        **参数解释**： 端口的IP/Mac对列表。 **取值范围**： - IP地址不允许为 “0.0.0.0/0”。 - 如果allowed_address_pairs配置地址池较大的IP网段（掩码小于24位），建议为该端口配置一个单独的安全组。 - 如果allowed_address_pairs的IP地址为“1.1.1.1/0”，表示关闭源目地址检查开关。 - 被绑定的云服务器网卡allowed_address_pairs的IP地址填“1.1.1.1/0”。

        :return: The allowed_address_pairs of this Port.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        r"""Sets the allowed_address_pairs of this Port.

        **参数解释**： 端口的IP/Mac对列表。 **取值范围**： - IP地址不允许为 “0.0.0.0/0”。 - 如果allowed_address_pairs配置地址池较大的IP网段（掩码小于24位），建议为该端口配置一个单独的安全组。 - 如果allowed_address_pairs的IP地址为“1.1.1.1/0”，表示关闭源目地址检查开关。 - 被绑定的云服务器网卡allowed_address_pairs的IP地址填“1.1.1.1/0”。

        :param allowed_address_pairs: The allowed_address_pairs of this Port.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v3.AllowedAddressPair`]
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
        if not isinstance(other, Port):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
