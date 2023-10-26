# coding: utf-8

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
        'admin_state_up': 'bool',
        'bindinghost_id': 'str',
        'bindingprofile': 'object',
        'bindingvif_details': 'object',
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
        'extra_dhcp_opts': 'list[object]',
        'position_type': 'str',
        'instance_info': 'object',
        'tags': 'list[str]',
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
        """Port

        The model defined in huaweicloud sdk

        :param admin_state_up: 1、功能描述：管理状态 2、取值范围：true/false 3、约束：N/A 4、默认值：true 5、权限：N/A
        :type admin_state_up: bool
        :param bindinghost_id: 1、功能描述：主机ID 2、取值范围：N/A 3、约束：管理员权限，普通租户不可见 4、默认值：N/A 5、权限：N/A
        :type bindinghost_id: str
        :param bindingprofile: 1、功能描述：提供用户设置自定义信息 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type bindingprofile: object
        :param bindingvif_details: 1、功能描述：vif的详细信息， \&quot;ovs_hybrid_plug\&quot;: 是否为ovs/bridge混合模式 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type bindingvif_details: object
        :param bindingvif_type: 1、功能描述：端口的接口类型 (ovs/hw_veb等)(扩展属性) 2、取值范围：N/A 3、约束：管理员权限，普通租户不可见 4、默认值：N/A 5、权限：N/A
        :type bindingvif_type: str
        :param bindingvnic_type: 1、功能描述：绑定的vNIC类型normal: 软交换direct: SRIOV硬直通（不支持） 2、取值范围：normal或者direct 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type bindingvnic_type: str
        :param created_at: 1、功能说明：创建时间 2、取值范围：格式 \&quot;UTC时间 格式: yyyy-MM-ddTHH:mm:ss\&quot;  3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type created_at: datetime
        :param updated_at: 1、功能说明：创建时间 2、取值范围：格式 \&quot;UTC时间 格式: yyyy-MM-ddTHH:mm:ss\&quot;  3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type updated_at: datetime
        :param description: 1、功能说明：端口描述 2、取值范围：0-255个字符，不能包含“&lt;”和“&gt;” 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type description: str
        :param device_id: 1、功能描述：端口所属设备ID 2、取值范围：标准UUID 3、约束：不支持设置和更新，由系统自动维护 4、默认值：N/A 5、权限：N/A
        :type device_id: str
        :param device_owner: 1、功能描述：设备所属（DHCP/Router/ lb/Nova） 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type device_owner: str
        :param ecs_flavor: 1、功能描述：标识这个端口所属虚拟机的flavor 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type ecs_flavor: str
        :param id: 1、功能描述：端口唯一标识 2、取值范围：标准UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type id: str
        :param instance_id: 1、功能描述：端口所属实例ID，例如RDS实例ID 2、取值范围：N/A 3、约束：不支持设置和更新，由系统自动维护 4、默认值：N/A 5、权限：N/A
        :type instance_id: str
        :param instance_type: 1、功能描述：端口所属实例类型，例如“RDS” 2、取值范围：N/A 3、约束：不支持设置和更新，由系统自动维护 4、默认值：N/A 5、权限：N/A
        :type instance_type: str
        :param mac_address: 1、功能描述：MAC地址 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type mac_address: str
        :param name: 1、功能描述：端口名称 2、取值范围：默认为空，最大长度不超过255 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type name: str
        :param port_security_enabled: 1、功能描述：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效 2、取值范围：true/false 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type port_security_enabled: bool
        :param private_ips: 1、功能描述：port的私有IP地址 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type private_ips: list[:class:`huaweicloudsdkvpc.v3.PrivateIpInfo`]
        :param project_id: 1、功能描述：项目ID 2、取值范围：UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type project_id: str
        :param security_groups: 1、功能描述：安全组 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type security_groups: list[str]
        :param status: 1、功能描述：端口状态 2、取值范围：ACTIVE，BUILD，DOWN 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type status: str
        :param tenant_id: 1、功能描述：租户ID 2、取值范围：UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type tenant_id: str
        :param virsubnet_id: 1、功能描述：所属网络ID 2、取值范围：标准UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type virsubnet_id: str
        :param vpc_id: 1、功能描述：VPC的ID 2、取值范围：标准UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type vpc_id: str
        :param vpc_tenant_id: 1、功能描述：VPC_租户ID 2、取值范围：UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type vpc_tenant_id: str
        :param vtep_ip: 1、功能描述：本地IP 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type vtep_ip: str
        :param enable_efi: 1、功能描述：是否使能efi，使能则表示端口支持vRoCE能力 2、取值范围：true or false 3、约束：N/A 4、默认值：false 5、权限：N/A
        :type enable_efi: bool
        :param scope: 1、功能描述：作用域 2、取值范围：center，表示作用域为中心；{azId}，表示作用域为具体的可用区 3、约束：N/A 4、默认值：center 5、权限：N/A
        :type scope: str
        :param zone_id: 1、功能描述：端口所属的可用分区 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type zone_id: str
        :param bindingmigration_info: 1、功能描述：迁移目的节点信息，包括目的节点的binding:vif_details和binding:vif_type 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type bindingmigration_info: object
        :param extra_dhcp_opts: 1、功能描述：DHCP的扩展属性 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type extra_dhcp_opts: list[object]
        :param position_type: 1、功能描述：边缘场景位置类型 2、取值范围：N/A 3、约束：N/A 4、默认值：center 5、权限：N/A
        :type position_type: str
        :param instance_info: 1、功能描述：端口绑定实例信息 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type instance_info: object
        :param tags: 1、功能描述：端口标签 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A
        :type tags: list[str]
        :param allowed_address_pairs: 1、功能描述：IP/Mac对列表 2、取值范围：N/A 3、约束： - IP地址不允许为 “0.0.0.0/0” - 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。 - 如果allowed_address_pairs的IP地址为“1.1.1.1/0”，表示关闭源目地址检查开关。 - 被绑定的云服务器网卡allowed_address_pairs的IP地址填“1.1.1.1/0”。 4、默认值：N/A 5、权限：N/A
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
        """Gets the admin_state_up of this Port.

        1、功能描述：管理状态 2、取值范围：true/false 3、约束：N/A 4、默认值：true 5、权限：N/A

        :return: The admin_state_up of this Port.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this Port.

        1、功能描述：管理状态 2、取值范围：true/false 3、约束：N/A 4、默认值：true 5、权限：N/A

        :param admin_state_up: The admin_state_up of this Port.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def bindinghost_id(self):
        """Gets the bindinghost_id of this Port.

        1、功能描述：主机ID 2、取值范围：N/A 3、约束：管理员权限，普通租户不可见 4、默认值：N/A 5、权限：N/A

        :return: The bindinghost_id of this Port.
        :rtype: str
        """
        return self._bindinghost_id

    @bindinghost_id.setter
    def bindinghost_id(self, bindinghost_id):
        """Sets the bindinghost_id of this Port.

        1、功能描述：主机ID 2、取值范围：N/A 3、约束：管理员权限，普通租户不可见 4、默认值：N/A 5、权限：N/A

        :param bindinghost_id: The bindinghost_id of this Port.
        :type bindinghost_id: str
        """
        self._bindinghost_id = bindinghost_id

    @property
    def bindingprofile(self):
        """Gets the bindingprofile of this Port.

        1、功能描述：提供用户设置自定义信息 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The bindingprofile of this Port.
        :rtype: object
        """
        return self._bindingprofile

    @bindingprofile.setter
    def bindingprofile(self, bindingprofile):
        """Sets the bindingprofile of this Port.

        1、功能描述：提供用户设置自定义信息 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param bindingprofile: The bindingprofile of this Port.
        :type bindingprofile: object
        """
        self._bindingprofile = bindingprofile

    @property
    def bindingvif_details(self):
        """Gets the bindingvif_details of this Port.

        1、功能描述：vif的详细信息， \"ovs_hybrid_plug\": 是否为ovs/bridge混合模式 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The bindingvif_details of this Port.
        :rtype: object
        """
        return self._bindingvif_details

    @bindingvif_details.setter
    def bindingvif_details(self, bindingvif_details):
        """Sets the bindingvif_details of this Port.

        1、功能描述：vif的详细信息， \"ovs_hybrid_plug\": 是否为ovs/bridge混合模式 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param bindingvif_details: The bindingvif_details of this Port.
        :type bindingvif_details: object
        """
        self._bindingvif_details = bindingvif_details

    @property
    def bindingvif_type(self):
        """Gets the bindingvif_type of this Port.

        1、功能描述：端口的接口类型 (ovs/hw_veb等)(扩展属性) 2、取值范围：N/A 3、约束：管理员权限，普通租户不可见 4、默认值：N/A 5、权限：N/A

        :return: The bindingvif_type of this Port.
        :rtype: str
        """
        return self._bindingvif_type

    @bindingvif_type.setter
    def bindingvif_type(self, bindingvif_type):
        """Sets the bindingvif_type of this Port.

        1、功能描述：端口的接口类型 (ovs/hw_veb等)(扩展属性) 2、取值范围：N/A 3、约束：管理员权限，普通租户不可见 4、默认值：N/A 5、权限：N/A

        :param bindingvif_type: The bindingvif_type of this Port.
        :type bindingvif_type: str
        """
        self._bindingvif_type = bindingvif_type

    @property
    def bindingvnic_type(self):
        """Gets the bindingvnic_type of this Port.

        1、功能描述：绑定的vNIC类型normal: 软交换direct: SRIOV硬直通（不支持） 2、取值范围：normal或者direct 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The bindingvnic_type of this Port.
        :rtype: str
        """
        return self._bindingvnic_type

    @bindingvnic_type.setter
    def bindingvnic_type(self, bindingvnic_type):
        """Sets the bindingvnic_type of this Port.

        1、功能描述：绑定的vNIC类型normal: 软交换direct: SRIOV硬直通（不支持） 2、取值范围：normal或者direct 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param bindingvnic_type: The bindingvnic_type of this Port.
        :type bindingvnic_type: str
        """
        self._bindingvnic_type = bindingvnic_type

    @property
    def created_at(self):
        """Gets the created_at of this Port.

        1、功能说明：创建时间 2、取值范围：格式 \"UTC时间 格式: yyyy-MM-ddTHH:mm:ss\"  3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The created_at of this Port.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Port.

        1、功能说明：创建时间 2、取值范围：格式 \"UTC时间 格式: yyyy-MM-ddTHH:mm:ss\"  3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param created_at: The created_at of this Port.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Port.

        1、功能说明：创建时间 2、取值范围：格式 \"UTC时间 格式: yyyy-MM-ddTHH:mm:ss\"  3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The updated_at of this Port.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Port.

        1、功能说明：创建时间 2、取值范围：格式 \"UTC时间 格式: yyyy-MM-ddTHH:mm:ss\"  3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param updated_at: The updated_at of this Port.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def description(self):
        """Gets the description of this Port.

        1、功能说明：端口描述 2、取值范围：0-255个字符，不能包含“<”和“>” 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The description of this Port.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Port.

        1、功能说明：端口描述 2、取值范围：0-255个字符，不能包含“<”和“>” 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param description: The description of this Port.
        :type description: str
        """
        self._description = description

    @property
    def device_id(self):
        """Gets the device_id of this Port.

        1、功能描述：端口所属设备ID 2、取值范围：标准UUID 3、约束：不支持设置和更新，由系统自动维护 4、默认值：N/A 5、权限：N/A

        :return: The device_id of this Port.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Port.

        1、功能描述：端口所属设备ID 2、取值范围：标准UUID 3、约束：不支持设置和更新，由系统自动维护 4、默认值：N/A 5、权限：N/A

        :param device_id: The device_id of this Port.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_owner(self):
        """Gets the device_owner of this Port.

        1、功能描述：设备所属（DHCP/Router/ lb/Nova） 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The device_owner of this Port.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this Port.

        1、功能描述：设备所属（DHCP/Router/ lb/Nova） 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param device_owner: The device_owner of this Port.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def ecs_flavor(self):
        """Gets the ecs_flavor of this Port.

        1、功能描述：标识这个端口所属虚拟机的flavor 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The ecs_flavor of this Port.
        :rtype: str
        """
        return self._ecs_flavor

    @ecs_flavor.setter
    def ecs_flavor(self, ecs_flavor):
        """Sets the ecs_flavor of this Port.

        1、功能描述：标识这个端口所属虚拟机的flavor 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param ecs_flavor: The ecs_flavor of this Port.
        :type ecs_flavor: str
        """
        self._ecs_flavor = ecs_flavor

    @property
    def id(self):
        """Gets the id of this Port.

        1、功能描述：端口唯一标识 2、取值范围：标准UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The id of this Port.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Port.

        1、功能描述：端口唯一标识 2、取值范围：标准UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param id: The id of this Port.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this Port.

        1、功能描述：端口所属实例ID，例如RDS实例ID 2、取值范围：N/A 3、约束：不支持设置和更新，由系统自动维护 4、默认值：N/A 5、权限：N/A

        :return: The instance_id of this Port.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Port.

        1、功能描述：端口所属实例ID，例如RDS实例ID 2、取值范围：N/A 3、约束：不支持设置和更新，由系统自动维护 4、默认值：N/A 5、权限：N/A

        :param instance_id: The instance_id of this Port.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this Port.

        1、功能描述：端口所属实例类型，例如“RDS” 2、取值范围：N/A 3、约束：不支持设置和更新，由系统自动维护 4、默认值：N/A 5、权限：N/A

        :return: The instance_type of this Port.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this Port.

        1、功能描述：端口所属实例类型，例如“RDS” 2、取值范围：N/A 3、约束：不支持设置和更新，由系统自动维护 4、默认值：N/A 5、权限：N/A

        :param instance_type: The instance_type of this Port.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def mac_address(self):
        """Gets the mac_address of this Port.

        1、功能描述：MAC地址 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The mac_address of this Port.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this Port.

        1、功能描述：MAC地址 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param mac_address: The mac_address of this Port.
        :type mac_address: str
        """
        self._mac_address = mac_address

    @property
    def name(self):
        """Gets the name of this Port.

        1、功能描述：端口名称 2、取值范围：默认为空，最大长度不超过255 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The name of this Port.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Port.

        1、功能描述：端口名称 2、取值范围：默认为空，最大长度不超过255 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param name: The name of this Port.
        :type name: str
        """
        self._name = name

    @property
    def port_security_enabled(self):
        """Gets the port_security_enabled of this Port.

        1、功能描述：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效 2、取值范围：true/false 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The port_security_enabled of this Port.
        :rtype: bool
        """
        return self._port_security_enabled

    @port_security_enabled.setter
    def port_security_enabled(self, port_security_enabled):
        """Sets the port_security_enabled of this Port.

        1、功能描述：端口安全使能标记，如果不使能则安全组和dhcp防欺骗不生效 2、取值范围：true/false 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param port_security_enabled: The port_security_enabled of this Port.
        :type port_security_enabled: bool
        """
        self._port_security_enabled = port_security_enabled

    @property
    def private_ips(self):
        """Gets the private_ips of this Port.

        1、功能描述：port的私有IP地址 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The private_ips of this Port.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.PrivateIpInfo`]
        """
        return self._private_ips

    @private_ips.setter
    def private_ips(self, private_ips):
        """Sets the private_ips of this Port.

        1、功能描述：port的私有IP地址 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param private_ips: The private_ips of this Port.
        :type private_ips: list[:class:`huaweicloudsdkvpc.v3.PrivateIpInfo`]
        """
        self._private_ips = private_ips

    @property
    def project_id(self):
        """Gets the project_id of this Port.

        1、功能描述：项目ID 2、取值范围：UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The project_id of this Port.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Port.

        1、功能描述：项目ID 2、取值范围：UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param project_id: The project_id of this Port.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def security_groups(self):
        """Gets the security_groups of this Port.

        1、功能描述：安全组 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The security_groups of this Port.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this Port.

        1、功能描述：安全组 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param security_groups: The security_groups of this Port.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def status(self):
        """Gets the status of this Port.

        1、功能描述：端口状态 2、取值范围：ACTIVE，BUILD，DOWN 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The status of this Port.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Port.

        1、功能描述：端口状态 2、取值范围：ACTIVE，BUILD，DOWN 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param status: The status of this Port.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Port.

        1、功能描述：租户ID 2、取值范围：UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The tenant_id of this Port.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Port.

        1、功能描述：租户ID 2、取值范围：UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param tenant_id: The tenant_id of this Port.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this Port.

        1、功能描述：所属网络ID 2、取值范围：标准UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The virsubnet_id of this Port.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this Port.

        1、功能描述：所属网络ID 2、取值范围：标准UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param virsubnet_id: The virsubnet_id of this Port.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this Port.

        1、功能描述：VPC的ID 2、取值范围：标准UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The vpc_id of this Port.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this Port.

        1、功能描述：VPC的ID 2、取值范围：标准UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param vpc_id: The vpc_id of this Port.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_tenant_id(self):
        """Gets the vpc_tenant_id of this Port.

        1、功能描述：VPC_租户ID 2、取值范围：UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The vpc_tenant_id of this Port.
        :rtype: str
        """
        return self._vpc_tenant_id

    @vpc_tenant_id.setter
    def vpc_tenant_id(self, vpc_tenant_id):
        """Sets the vpc_tenant_id of this Port.

        1、功能描述：VPC_租户ID 2、取值范围：UUID 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param vpc_tenant_id: The vpc_tenant_id of this Port.
        :type vpc_tenant_id: str
        """
        self._vpc_tenant_id = vpc_tenant_id

    @property
    def vtep_ip(self):
        """Gets the vtep_ip of this Port.

        1、功能描述：本地IP 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The vtep_ip of this Port.
        :rtype: str
        """
        return self._vtep_ip

    @vtep_ip.setter
    def vtep_ip(self, vtep_ip):
        """Sets the vtep_ip of this Port.

        1、功能描述：本地IP 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param vtep_ip: The vtep_ip of this Port.
        :type vtep_ip: str
        """
        self._vtep_ip = vtep_ip

    @property
    def enable_efi(self):
        """Gets the enable_efi of this Port.

        1、功能描述：是否使能efi，使能则表示端口支持vRoCE能力 2、取值范围：true or false 3、约束：N/A 4、默认值：false 5、权限：N/A

        :return: The enable_efi of this Port.
        :rtype: bool
        """
        return self._enable_efi

    @enable_efi.setter
    def enable_efi(self, enable_efi):
        """Sets the enable_efi of this Port.

        1、功能描述：是否使能efi，使能则表示端口支持vRoCE能力 2、取值范围：true or false 3、约束：N/A 4、默认值：false 5、权限：N/A

        :param enable_efi: The enable_efi of this Port.
        :type enable_efi: bool
        """
        self._enable_efi = enable_efi

    @property
    def scope(self):
        """Gets the scope of this Port.

        1、功能描述：作用域 2、取值范围：center，表示作用域为中心；{azId}，表示作用域为具体的可用区 3、约束：N/A 4、默认值：center 5、权限：N/A

        :return: The scope of this Port.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Port.

        1、功能描述：作用域 2、取值范围：center，表示作用域为中心；{azId}，表示作用域为具体的可用区 3、约束：N/A 4、默认值：center 5、权限：N/A

        :param scope: The scope of this Port.
        :type scope: str
        """
        self._scope = scope

    @property
    def zone_id(self):
        """Gets the zone_id of this Port.

        1、功能描述：端口所属的可用分区 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The zone_id of this Port.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this Port.

        1、功能描述：端口所属的可用分区 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param zone_id: The zone_id of this Port.
        :type zone_id: str
        """
        self._zone_id = zone_id

    @property
    def bindingmigration_info(self):
        """Gets the bindingmigration_info of this Port.

        1、功能描述：迁移目的节点信息，包括目的节点的binding:vif_details和binding:vif_type 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The bindingmigration_info of this Port.
        :rtype: object
        """
        return self._bindingmigration_info

    @bindingmigration_info.setter
    def bindingmigration_info(self, bindingmigration_info):
        """Sets the bindingmigration_info of this Port.

        1、功能描述：迁移目的节点信息，包括目的节点的binding:vif_details和binding:vif_type 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param bindingmigration_info: The bindingmigration_info of this Port.
        :type bindingmigration_info: object
        """
        self._bindingmigration_info = bindingmigration_info

    @property
    def extra_dhcp_opts(self):
        """Gets the extra_dhcp_opts of this Port.

        1、功能描述：DHCP的扩展属性 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The extra_dhcp_opts of this Port.
        :rtype: list[object]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        """Sets the extra_dhcp_opts of this Port.

        1、功能描述：DHCP的扩展属性 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param extra_dhcp_opts: The extra_dhcp_opts of this Port.
        :type extra_dhcp_opts: list[object]
        """
        self._extra_dhcp_opts = extra_dhcp_opts

    @property
    def position_type(self):
        """Gets the position_type of this Port.

        1、功能描述：边缘场景位置类型 2、取值范围：N/A 3、约束：N/A 4、默认值：center 5、权限：N/A

        :return: The position_type of this Port.
        :rtype: str
        """
        return self._position_type

    @position_type.setter
    def position_type(self, position_type):
        """Sets the position_type of this Port.

        1、功能描述：边缘场景位置类型 2、取值范围：N/A 3、约束：N/A 4、默认值：center 5、权限：N/A

        :param position_type: The position_type of this Port.
        :type position_type: str
        """
        self._position_type = position_type

    @property
    def instance_info(self):
        """Gets the instance_info of this Port.

        1、功能描述：端口绑定实例信息 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The instance_info of this Port.
        :rtype: object
        """
        return self._instance_info

    @instance_info.setter
    def instance_info(self, instance_info):
        """Sets the instance_info of this Port.

        1、功能描述：端口绑定实例信息 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param instance_info: The instance_info of this Port.
        :type instance_info: object
        """
        self._instance_info = instance_info

    @property
    def tags(self):
        """Gets the tags of this Port.

        1、功能描述：端口标签 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The tags of this Port.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Port.

        1、功能描述：端口标签 2、取值范围：N/A 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param tags: The tags of this Port.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def allowed_address_pairs(self):
        """Gets the allowed_address_pairs of this Port.

        1、功能描述：IP/Mac对列表 2、取值范围：N/A 3、约束： - IP地址不允许为 “0.0.0.0/0” - 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。 - 如果allowed_address_pairs的IP地址为“1.1.1.1/0”，表示关闭源目地址检查开关。 - 被绑定的云服务器网卡allowed_address_pairs的IP地址填“1.1.1.1/0”。 4、默认值：N/A 5、权限：N/A

        :return: The allowed_address_pairs of this Port.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        """Sets the allowed_address_pairs of this Port.

        1、功能描述：IP/Mac对列表 2、取值范围：N/A 3、约束： - IP地址不允许为 “0.0.0.0/0” - 如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。 - 如果allowed_address_pairs的IP地址为“1.1.1.1/0”，表示关闭源目地址检查开关。 - 被绑定的云服务器网卡allowed_address_pairs的IP地址填“1.1.1.1/0”。 4、默认值：N/A 5、权限：N/A

        :param allowed_address_pairs: The allowed_address_pairs of this Port.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkvpc.v3.AllowedAddressPair`]
        """
        self._allowed_address_pairs = allowed_address_pairs

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
