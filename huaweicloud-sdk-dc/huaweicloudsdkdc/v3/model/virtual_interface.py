# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VirtualInterface:

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
        'admin_state_up': 'bool',
        'bandwidth': 'int',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'description': 'str',
        'direct_connect_id': 'str',
        'service_type': 'str',
        'status': 'str',
        'tenant_id': 'str',
        'type': 'str',
        'vgw_id': 'str',
        'vlan': 'int',
        'route_limit': 'int',
        'enable_nqa': 'bool',
        'enable_bfd': 'bool',
        'lag_id': 'str',
        'device_id': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'local_gateway_v4_ip': 'str',
        'remote_gateway_v4_ip': 'str',
        'ies_id': 'str',
        'reason': 'str',
        'rate_limit': 'bool',
        'address_family': 'str',
        'local_gateway_v6_ip': 'str',
        'remote_gateway_v6_ip': 'str',
        'lgw_id': 'str',
        'gateway_id': 'str',
        'remote_ep_group': 'list[str]',
        'service_ep_group': 'list[str]',
        'bgp_route_limit': 'int',
        'priority': 'str',
        'vif_peers': 'list[VifPeer]',
        'extend_attribute': 'VifExtendAttribute'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'bandwidth': 'bandwidth',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'description': 'description',
        'direct_connect_id': 'direct_connect_id',
        'service_type': 'service_type',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'type': 'type',
        'vgw_id': 'vgw_id',
        'vlan': 'vlan',
        'route_limit': 'route_limit',
        'enable_nqa': 'enable_nqa',
        'enable_bfd': 'enable_bfd',
        'lag_id': 'lag_id',
        'device_id': 'device_id',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'local_gateway_v4_ip': 'local_gateway_v4_ip',
        'remote_gateway_v4_ip': 'remote_gateway_v4_ip',
        'ies_id': 'ies_id',
        'reason': 'reason',
        'rate_limit': 'rate_limit',
        'address_family': 'address_family',
        'local_gateway_v6_ip': 'local_gateway_v6_ip',
        'remote_gateway_v6_ip': 'remote_gateway_v6_ip',
        'lgw_id': 'lgw_id',
        'gateway_id': 'gateway_id',
        'remote_ep_group': 'remote_ep_group',
        'service_ep_group': 'service_ep_group',
        'bgp_route_limit': 'bgp_route_limit',
        'priority': 'priority',
        'vif_peers': 'vif_peers',
        'extend_attribute': 'extend_attribute'
    }

    def __init__(self, id=None, name=None, admin_state_up=None, bandwidth=None, create_time=None, update_time=None, description=None, direct_connect_id=None, service_type=None, status=None, tenant_id=None, type=None, vgw_id=None, vlan=None, route_limit=None, enable_nqa=None, enable_bfd=None, lag_id=None, device_id=None, enterprise_project_id=None, tags=None, local_gateway_v4_ip=None, remote_gateway_v4_ip=None, ies_id=None, reason=None, rate_limit=None, address_family=None, local_gateway_v6_ip=None, remote_gateway_v6_ip=None, lgw_id=None, gateway_id=None, remote_ep_group=None, service_ep_group=None, bgp_route_limit=None, priority=None, vif_peers=None, extend_attribute=None):
        """VirtualInterface

        The model defined in huaweicloud sdk

        :param id: 虚拟接口的ID
        :type id: str
        :param name: 虚拟接口的名字
        :type name: str
        :param admin_state_up: 管理状态：true或false
        :type admin_state_up: bool
        :param bandwidth: 虚拟接口接入带宽
        :type bandwidth: int
        :param create_time: 虚拟接口创建时间
        :type create_time: datetime
        :param update_time: 虚拟接口更新时间
        :type update_time: datetime
        :param description: 虚拟接口的描述
        :type description: str
        :param direct_connect_id: 物理专线的ID
        :type direct_connect_id: str
        :param service_type: 接入网关的类型：包括VGW,GDGW,LGW等
        :type service_type: str
        :param status: 操作状态，合法值是：ACTIVE，DOWN，BUILD，ERROR，PENDING_CREATE，PENDING_UPDATE，PENDING_DELETE，DELETED，AUTHORIZATION，REJECTED
        :type status: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param type: 表示接口类型：private
        :type type: str
        :param vgw_id: 虚拟网关的ID
        :type vgw_id: str
        :param vlan: 同用户网关对接的vlan, 配置范围0-3999
        :type vlan: int
        :param route_limit: VIF远端子网路由配置规格
        :type route_limit: int
        :param enable_nqa: 是否使能nqa功能：true或false
        :type enable_nqa: bool
        :param enable_bfd: 是否使能nqa功能：true或false
        :type enable_bfd: bool
        :param lag_id: VIF关联的链路聚合组ID
        :type lag_id: str
        :param device_id: 归属的设备ID
        :type device_id: str
        :param enterprise_project_id: 实例所属企业项目ID
        :type enterprise_project_id: str
        :param tags: 标签信息
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        :param local_gateway_v4_ip: 云侧网关IPv4接口地址，该字段现已经移到vifpeer参数列表中，未来将会废弃。
        :type local_gateway_v4_ip: str
        :param remote_gateway_v4_ip: 客户侧网关IPv4接口地址，该字段现已经移到vifpeer参数列表中，未来将会废弃。
        :type remote_gateway_v4_ip: str
        :param ies_id: 归属的IES站点的ID[（功能暂不支持）](tag:dt)
        :type ies_id: str
        :param reason: 如果资源的状态是Error的情况下，该参数会显示相关错误信息。
        :type reason: str
        :param rate_limit: 标识虚拟接口是否开启限速
        :type rate_limit: bool
        :param address_family: 接口的地址簇类型，ipv4，ipv6。该字段现已迁移到vifpeer参数列表中，未来将会废弃。
        :type address_family: str
        :param local_gateway_v6_ip: 云侧网关IPv6接口地址，该字段现已迁移到vifpeer参数列表中，未来将会废弃。
        :type local_gateway_v6_ip: str
        :param remote_gateway_v6_ip: 客户侧网关IPv6接口地址，该字段现已迁移到vifpeer参数列表中，未来将会废弃。
        :type remote_gateway_v6_ip: str
        :param lgw_id: 本地网关的ID，用于IES场景。[（功能暂不支持）](tag:dt)
        :type lgw_id: str
        :param gateway_id: 虚拟接口关联的网关的ID
        :type gateway_id: str
        :param remote_ep_group: 远端子网列表，记录租户侧的cidrs。该字段现已迁移到vifpeer参数列表中，未来将会废弃。
        :type remote_ep_group: list[str]
        :param service_ep_group: 该字段用于公网专线接口，表示租户可以访问云上公网服务地址列表。该字段现已迁移到vifpeer参数列表中，未来将会废弃。
        :type service_ep_group: list[str]
        :param bgp_route_limit: BGP的路由配置规格
        :type bgp_route_limit: int
        :param priority: 虚拟接口的优先级，支持两种优先级状态normal和low。 接口优先级相同时表示负载关系，接口优先级不同时表示主备关系，出云流量优先转到优先级更高的normal接口。 目前仅BGP模式接口支持。
        :type priority: str
        :param vif_peers: vif的Peer的相关信息
        :type vif_peers: list[:class:`huaweicloudsdkdc.v3.VifPeer`]
        :param extend_attribute: 
        :type extend_attribute: :class:`huaweicloudsdkdc.v3.VifExtendAttribute`
        """
        
        

        self._id = None
        self._name = None
        self._admin_state_up = None
        self._bandwidth = None
        self._create_time = None
        self._update_time = None
        self._description = None
        self._direct_connect_id = None
        self._service_type = None
        self._status = None
        self._tenant_id = None
        self._type = None
        self._vgw_id = None
        self._vlan = None
        self._route_limit = None
        self._enable_nqa = None
        self._enable_bfd = None
        self._lag_id = None
        self._device_id = None
        self._enterprise_project_id = None
        self._tags = None
        self._local_gateway_v4_ip = None
        self._remote_gateway_v4_ip = None
        self._ies_id = None
        self._reason = None
        self._rate_limit = None
        self._address_family = None
        self._local_gateway_v6_ip = None
        self._remote_gateway_v6_ip = None
        self._lgw_id = None
        self._gateway_id = None
        self._remote_ep_group = None
        self._service_ep_group = None
        self._bgp_route_limit = None
        self._priority = None
        self._vif_peers = None
        self._extend_attribute = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if description is not None:
            self.description = description
        if direct_connect_id is not None:
            self.direct_connect_id = direct_connect_id
        if service_type is not None:
            self.service_type = service_type
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type
        if vgw_id is not None:
            self.vgw_id = vgw_id
        if vlan is not None:
            self.vlan = vlan
        if route_limit is not None:
            self.route_limit = route_limit
        if enable_nqa is not None:
            self.enable_nqa = enable_nqa
        if enable_bfd is not None:
            self.enable_bfd = enable_bfd
        if lag_id is not None:
            self.lag_id = lag_id
        if device_id is not None:
            self.device_id = device_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if local_gateway_v4_ip is not None:
            self.local_gateway_v4_ip = local_gateway_v4_ip
        if remote_gateway_v4_ip is not None:
            self.remote_gateway_v4_ip = remote_gateway_v4_ip
        if ies_id is not None:
            self.ies_id = ies_id
        if reason is not None:
            self.reason = reason
        if rate_limit is not None:
            self.rate_limit = rate_limit
        if address_family is not None:
            self.address_family = address_family
        if local_gateway_v6_ip is not None:
            self.local_gateway_v6_ip = local_gateway_v6_ip
        if remote_gateway_v6_ip is not None:
            self.remote_gateway_v6_ip = remote_gateway_v6_ip
        if lgw_id is not None:
            self.lgw_id = lgw_id
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if remote_ep_group is not None:
            self.remote_ep_group = remote_ep_group
        if service_ep_group is not None:
            self.service_ep_group = service_ep_group
        if bgp_route_limit is not None:
            self.bgp_route_limit = bgp_route_limit
        if priority is not None:
            self.priority = priority
        if vif_peers is not None:
            self.vif_peers = vif_peers
        if extend_attribute is not None:
            self.extend_attribute = extend_attribute

    @property
    def id(self):
        """Gets the id of this VirtualInterface.

        虚拟接口的ID

        :return: The id of this VirtualInterface.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualInterface.

        虚拟接口的ID

        :param id: The id of this VirtualInterface.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this VirtualInterface.

        虚拟接口的名字

        :return: The name of this VirtualInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualInterface.

        虚拟接口的名字

        :param name: The name of this VirtualInterface.
        :type name: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this VirtualInterface.

        管理状态：true或false

        :return: The admin_state_up of this VirtualInterface.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this VirtualInterface.

        管理状态：true或false

        :param admin_state_up: The admin_state_up of this VirtualInterface.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def bandwidth(self):
        """Gets the bandwidth of this VirtualInterface.

        虚拟接口接入带宽

        :return: The bandwidth of this VirtualInterface.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this VirtualInterface.

        虚拟接口接入带宽

        :param bandwidth: The bandwidth of this VirtualInterface.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def create_time(self):
        """Gets the create_time of this VirtualInterface.

        虚拟接口创建时间

        :return: The create_time of this VirtualInterface.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VirtualInterface.

        虚拟接口创建时间

        :param create_time: The create_time of this VirtualInterface.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this VirtualInterface.

        虚拟接口更新时间

        :return: The update_time of this VirtualInterface.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this VirtualInterface.

        虚拟接口更新时间

        :param update_time: The update_time of this VirtualInterface.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def description(self):
        """Gets the description of this VirtualInterface.

        虚拟接口的描述

        :return: The description of this VirtualInterface.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualInterface.

        虚拟接口的描述

        :param description: The description of this VirtualInterface.
        :type description: str
        """
        self._description = description

    @property
    def direct_connect_id(self):
        """Gets the direct_connect_id of this VirtualInterface.

        物理专线的ID

        :return: The direct_connect_id of this VirtualInterface.
        :rtype: str
        """
        return self._direct_connect_id

    @direct_connect_id.setter
    def direct_connect_id(self, direct_connect_id):
        """Sets the direct_connect_id of this VirtualInterface.

        物理专线的ID

        :param direct_connect_id: The direct_connect_id of this VirtualInterface.
        :type direct_connect_id: str
        """
        self._direct_connect_id = direct_connect_id

    @property
    def service_type(self):
        """Gets the service_type of this VirtualInterface.

        接入网关的类型：包括VGW,GDGW,LGW等

        :return: The service_type of this VirtualInterface.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this VirtualInterface.

        接入网关的类型：包括VGW,GDGW,LGW等

        :param service_type: The service_type of this VirtualInterface.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def status(self):
        """Gets the status of this VirtualInterface.

        操作状态，合法值是：ACTIVE，DOWN，BUILD，ERROR，PENDING_CREATE，PENDING_UPDATE，PENDING_DELETE，DELETED，AUTHORIZATION，REJECTED

        :return: The status of this VirtualInterface.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VirtualInterface.

        操作状态，合法值是：ACTIVE，DOWN，BUILD，ERROR，PENDING_CREATE，PENDING_UPDATE，PENDING_DELETE，DELETED，AUTHORIZATION，REJECTED

        :param status: The status of this VirtualInterface.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this VirtualInterface.

        租户ID

        :return: The tenant_id of this VirtualInterface.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this VirtualInterface.

        租户ID

        :param tenant_id: The tenant_id of this VirtualInterface.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this VirtualInterface.

        表示接口类型：private

        :return: The type of this VirtualInterface.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VirtualInterface.

        表示接口类型：private

        :param type: The type of this VirtualInterface.
        :type type: str
        """
        self._type = type

    @property
    def vgw_id(self):
        """Gets the vgw_id of this VirtualInterface.

        虚拟网关的ID

        :return: The vgw_id of this VirtualInterface.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        """Sets the vgw_id of this VirtualInterface.

        虚拟网关的ID

        :param vgw_id: The vgw_id of this VirtualInterface.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def vlan(self):
        """Gets the vlan of this VirtualInterface.

        同用户网关对接的vlan, 配置范围0-3999

        :return: The vlan of this VirtualInterface.
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this VirtualInterface.

        同用户网关对接的vlan, 配置范围0-3999

        :param vlan: The vlan of this VirtualInterface.
        :type vlan: int
        """
        self._vlan = vlan

    @property
    def route_limit(self):
        """Gets the route_limit of this VirtualInterface.

        VIF远端子网路由配置规格

        :return: The route_limit of this VirtualInterface.
        :rtype: int
        """
        return self._route_limit

    @route_limit.setter
    def route_limit(self, route_limit):
        """Sets the route_limit of this VirtualInterface.

        VIF远端子网路由配置规格

        :param route_limit: The route_limit of this VirtualInterface.
        :type route_limit: int
        """
        self._route_limit = route_limit

    @property
    def enable_nqa(self):
        """Gets the enable_nqa of this VirtualInterface.

        是否使能nqa功能：true或false

        :return: The enable_nqa of this VirtualInterface.
        :rtype: bool
        """
        return self._enable_nqa

    @enable_nqa.setter
    def enable_nqa(self, enable_nqa):
        """Sets the enable_nqa of this VirtualInterface.

        是否使能nqa功能：true或false

        :param enable_nqa: The enable_nqa of this VirtualInterface.
        :type enable_nqa: bool
        """
        self._enable_nqa = enable_nqa

    @property
    def enable_bfd(self):
        """Gets the enable_bfd of this VirtualInterface.

        是否使能nqa功能：true或false

        :return: The enable_bfd of this VirtualInterface.
        :rtype: bool
        """
        return self._enable_bfd

    @enable_bfd.setter
    def enable_bfd(self, enable_bfd):
        """Sets the enable_bfd of this VirtualInterface.

        是否使能nqa功能：true或false

        :param enable_bfd: The enable_bfd of this VirtualInterface.
        :type enable_bfd: bool
        """
        self._enable_bfd = enable_bfd

    @property
    def lag_id(self):
        """Gets the lag_id of this VirtualInterface.

        VIF关联的链路聚合组ID

        :return: The lag_id of this VirtualInterface.
        :rtype: str
        """
        return self._lag_id

    @lag_id.setter
    def lag_id(self, lag_id):
        """Sets the lag_id of this VirtualInterface.

        VIF关联的链路聚合组ID

        :param lag_id: The lag_id of this VirtualInterface.
        :type lag_id: str
        """
        self._lag_id = lag_id

    @property
    def device_id(self):
        """Gets the device_id of this VirtualInterface.

        归属的设备ID

        :return: The device_id of this VirtualInterface.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this VirtualInterface.

        归属的设备ID

        :param device_id: The device_id of this VirtualInterface.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this VirtualInterface.

        实例所属企业项目ID

        :return: The enterprise_project_id of this VirtualInterface.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this VirtualInterface.

        实例所属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this VirtualInterface.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this VirtualInterface.

        标签信息

        :return: The tags of this VirtualInterface.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VirtualInterface.

        标签信息

        :param tags: The tags of this VirtualInterface.
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        self._tags = tags

    @property
    def local_gateway_v4_ip(self):
        """Gets the local_gateway_v4_ip of this VirtualInterface.

        云侧网关IPv4接口地址，该字段现已经移到vifpeer参数列表中，未来将会废弃。

        :return: The local_gateway_v4_ip of this VirtualInterface.
        :rtype: str
        """
        return self._local_gateway_v4_ip

    @local_gateway_v4_ip.setter
    def local_gateway_v4_ip(self, local_gateway_v4_ip):
        """Sets the local_gateway_v4_ip of this VirtualInterface.

        云侧网关IPv4接口地址，该字段现已经移到vifpeer参数列表中，未来将会废弃。

        :param local_gateway_v4_ip: The local_gateway_v4_ip of this VirtualInterface.
        :type local_gateway_v4_ip: str
        """
        self._local_gateway_v4_ip = local_gateway_v4_ip

    @property
    def remote_gateway_v4_ip(self):
        """Gets the remote_gateway_v4_ip of this VirtualInterface.

        客户侧网关IPv4接口地址，该字段现已经移到vifpeer参数列表中，未来将会废弃。

        :return: The remote_gateway_v4_ip of this VirtualInterface.
        :rtype: str
        """
        return self._remote_gateway_v4_ip

    @remote_gateway_v4_ip.setter
    def remote_gateway_v4_ip(self, remote_gateway_v4_ip):
        """Sets the remote_gateway_v4_ip of this VirtualInterface.

        客户侧网关IPv4接口地址，该字段现已经移到vifpeer参数列表中，未来将会废弃。

        :param remote_gateway_v4_ip: The remote_gateway_v4_ip of this VirtualInterface.
        :type remote_gateway_v4_ip: str
        """
        self._remote_gateway_v4_ip = remote_gateway_v4_ip

    @property
    def ies_id(self):
        """Gets the ies_id of this VirtualInterface.

        归属的IES站点的ID[（功能暂不支持）](tag:dt)

        :return: The ies_id of this VirtualInterface.
        :rtype: str
        """
        return self._ies_id

    @ies_id.setter
    def ies_id(self, ies_id):
        """Sets the ies_id of this VirtualInterface.

        归属的IES站点的ID[（功能暂不支持）](tag:dt)

        :param ies_id: The ies_id of this VirtualInterface.
        :type ies_id: str
        """
        self._ies_id = ies_id

    @property
    def reason(self):
        """Gets the reason of this VirtualInterface.

        如果资源的状态是Error的情况下，该参数会显示相关错误信息。

        :return: The reason of this VirtualInterface.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this VirtualInterface.

        如果资源的状态是Error的情况下，该参数会显示相关错误信息。

        :param reason: The reason of this VirtualInterface.
        :type reason: str
        """
        self._reason = reason

    @property
    def rate_limit(self):
        """Gets the rate_limit of this VirtualInterface.

        标识虚拟接口是否开启限速

        :return: The rate_limit of this VirtualInterface.
        :rtype: bool
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        """Sets the rate_limit of this VirtualInterface.

        标识虚拟接口是否开启限速

        :param rate_limit: The rate_limit of this VirtualInterface.
        :type rate_limit: bool
        """
        self._rate_limit = rate_limit

    @property
    def address_family(self):
        """Gets the address_family of this VirtualInterface.

        接口的地址簇类型，ipv4，ipv6。该字段现已迁移到vifpeer参数列表中，未来将会废弃。

        :return: The address_family of this VirtualInterface.
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this VirtualInterface.

        接口的地址簇类型，ipv4，ipv6。该字段现已迁移到vifpeer参数列表中，未来将会废弃。

        :param address_family: The address_family of this VirtualInterface.
        :type address_family: str
        """
        self._address_family = address_family

    @property
    def local_gateway_v6_ip(self):
        """Gets the local_gateway_v6_ip of this VirtualInterface.

        云侧网关IPv6接口地址，该字段现已迁移到vifpeer参数列表中，未来将会废弃。

        :return: The local_gateway_v6_ip of this VirtualInterface.
        :rtype: str
        """
        return self._local_gateway_v6_ip

    @local_gateway_v6_ip.setter
    def local_gateway_v6_ip(self, local_gateway_v6_ip):
        """Sets the local_gateway_v6_ip of this VirtualInterface.

        云侧网关IPv6接口地址，该字段现已迁移到vifpeer参数列表中，未来将会废弃。

        :param local_gateway_v6_ip: The local_gateway_v6_ip of this VirtualInterface.
        :type local_gateway_v6_ip: str
        """
        self._local_gateway_v6_ip = local_gateway_v6_ip

    @property
    def remote_gateway_v6_ip(self):
        """Gets the remote_gateway_v6_ip of this VirtualInterface.

        客户侧网关IPv6接口地址，该字段现已迁移到vifpeer参数列表中，未来将会废弃。

        :return: The remote_gateway_v6_ip of this VirtualInterface.
        :rtype: str
        """
        return self._remote_gateway_v6_ip

    @remote_gateway_v6_ip.setter
    def remote_gateway_v6_ip(self, remote_gateway_v6_ip):
        """Sets the remote_gateway_v6_ip of this VirtualInterface.

        客户侧网关IPv6接口地址，该字段现已迁移到vifpeer参数列表中，未来将会废弃。

        :param remote_gateway_v6_ip: The remote_gateway_v6_ip of this VirtualInterface.
        :type remote_gateway_v6_ip: str
        """
        self._remote_gateway_v6_ip = remote_gateway_v6_ip

    @property
    def lgw_id(self):
        """Gets the lgw_id of this VirtualInterface.

        本地网关的ID，用于IES场景。[（功能暂不支持）](tag:dt)

        :return: The lgw_id of this VirtualInterface.
        :rtype: str
        """
        return self._lgw_id

    @lgw_id.setter
    def lgw_id(self, lgw_id):
        """Sets the lgw_id of this VirtualInterface.

        本地网关的ID，用于IES场景。[（功能暂不支持）](tag:dt)

        :param lgw_id: The lgw_id of this VirtualInterface.
        :type lgw_id: str
        """
        self._lgw_id = lgw_id

    @property
    def gateway_id(self):
        """Gets the gateway_id of this VirtualInterface.

        虚拟接口关联的网关的ID

        :return: The gateway_id of this VirtualInterface.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this VirtualInterface.

        虚拟接口关联的网关的ID

        :param gateway_id: The gateway_id of this VirtualInterface.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def remote_ep_group(self):
        """Gets the remote_ep_group of this VirtualInterface.

        远端子网列表，记录租户侧的cidrs。该字段现已迁移到vifpeer参数列表中，未来将会废弃。

        :return: The remote_ep_group of this VirtualInterface.
        :rtype: list[str]
        """
        return self._remote_ep_group

    @remote_ep_group.setter
    def remote_ep_group(self, remote_ep_group):
        """Sets the remote_ep_group of this VirtualInterface.

        远端子网列表，记录租户侧的cidrs。该字段现已迁移到vifpeer参数列表中，未来将会废弃。

        :param remote_ep_group: The remote_ep_group of this VirtualInterface.
        :type remote_ep_group: list[str]
        """
        self._remote_ep_group = remote_ep_group

    @property
    def service_ep_group(self):
        """Gets the service_ep_group of this VirtualInterface.

        该字段用于公网专线接口，表示租户可以访问云上公网服务地址列表。该字段现已迁移到vifpeer参数列表中，未来将会废弃。

        :return: The service_ep_group of this VirtualInterface.
        :rtype: list[str]
        """
        return self._service_ep_group

    @service_ep_group.setter
    def service_ep_group(self, service_ep_group):
        """Sets the service_ep_group of this VirtualInterface.

        该字段用于公网专线接口，表示租户可以访问云上公网服务地址列表。该字段现已迁移到vifpeer参数列表中，未来将会废弃。

        :param service_ep_group: The service_ep_group of this VirtualInterface.
        :type service_ep_group: list[str]
        """
        self._service_ep_group = service_ep_group

    @property
    def bgp_route_limit(self):
        """Gets the bgp_route_limit of this VirtualInterface.

        BGP的路由配置规格

        :return: The bgp_route_limit of this VirtualInterface.
        :rtype: int
        """
        return self._bgp_route_limit

    @bgp_route_limit.setter
    def bgp_route_limit(self, bgp_route_limit):
        """Sets the bgp_route_limit of this VirtualInterface.

        BGP的路由配置规格

        :param bgp_route_limit: The bgp_route_limit of this VirtualInterface.
        :type bgp_route_limit: int
        """
        self._bgp_route_limit = bgp_route_limit

    @property
    def priority(self):
        """Gets the priority of this VirtualInterface.

        虚拟接口的优先级，支持两种优先级状态normal和low。 接口优先级相同时表示负载关系，接口优先级不同时表示主备关系，出云流量优先转到优先级更高的normal接口。 目前仅BGP模式接口支持。

        :return: The priority of this VirtualInterface.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this VirtualInterface.

        虚拟接口的优先级，支持两种优先级状态normal和low。 接口优先级相同时表示负载关系，接口优先级不同时表示主备关系，出云流量优先转到优先级更高的normal接口。 目前仅BGP模式接口支持。

        :param priority: The priority of this VirtualInterface.
        :type priority: str
        """
        self._priority = priority

    @property
    def vif_peers(self):
        """Gets the vif_peers of this VirtualInterface.

        vif的Peer的相关信息

        :return: The vif_peers of this VirtualInterface.
        :rtype: list[:class:`huaweicloudsdkdc.v3.VifPeer`]
        """
        return self._vif_peers

    @vif_peers.setter
    def vif_peers(self, vif_peers):
        """Sets the vif_peers of this VirtualInterface.

        vif的Peer的相关信息

        :param vif_peers: The vif_peers of this VirtualInterface.
        :type vif_peers: list[:class:`huaweicloudsdkdc.v3.VifPeer`]
        """
        self._vif_peers = vif_peers

    @property
    def extend_attribute(self):
        """Gets the extend_attribute of this VirtualInterface.

        :return: The extend_attribute of this VirtualInterface.
        :rtype: :class:`huaweicloudsdkdc.v3.VifExtendAttribute`
        """
        return self._extend_attribute

    @extend_attribute.setter
    def extend_attribute(self, extend_attribute):
        """Sets the extend_attribute of this VirtualInterface.

        :param extend_attribute: The extend_attribute of this VirtualInterface.
        :type extend_attribute: :class:`huaweicloudsdkdc.v3.VifExtendAttribute`
        """
        self._extend_attribute = extend_attribute

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
        if not isinstance(other, VirtualInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
