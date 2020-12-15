# coding: utf-8

import pprint
import re

import six





class LoadBalancer:


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
        'description': 'str',
        'provisioning_status': 'str',
        'admin_state_up': 'bool',
        'provider': 'str',
        'pools': 'list[PoolRef]',
        'listeners': 'list[ListenerRef]',
        'operating_status': 'str',
        'vip_address': 'str',
        'vip_subnet_cidr_id': 'str',
        'name': 'str',
        'project_id': 'str',
        'vip_port_id': 'str',
        'tags': 'list[Tag]',
        'created_at': 'str',
        'updated_at': 'str',
        'guaranteed': 'bool',
        'vpc_id': 'str',
        'eips': 'list[EipInfo]',
        'ipv6_vip_address': 'str',
        'ipv6_vip_virsubnet_id': 'str',
        'ipv6_vip_port_id': 'str',
        'availability_zone_list': 'list[str]',
        'enterprise_project_id': 'str',
        'l4_flavor_id': 'str',
        'l4_scale_flavor_id': 'str',
        'l7_flavor_id': 'str',
        'l7_scale_flavor_id': 'str',
        'publicips': 'list[PublicIpInfo]',
        'elb_virsubnet_ids': 'list[str]',
        'elb_virsubnet_type': 'str',
        'ip_target_enable': 'bool',
        'deletion_protection_enable': 'str',
        'frozen_scene': 'str',
        'ipv6_bandwidth': 'BandwidthRef'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'provisioning_status': 'provisioning_status',
        'admin_state_up': 'admin_state_up',
        'provider': 'provider',
        'pools': 'pools',
        'listeners': 'listeners',
        'operating_status': 'operating_status',
        'vip_address': 'vip_address',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'name': 'name',
        'project_id': 'project_id',
        'vip_port_id': 'vip_port_id',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'guaranteed': 'guaranteed',
        'vpc_id': 'vpc_id',
        'eips': 'eips',
        'ipv6_vip_address': 'ipv6_vip_address',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'ipv6_vip_port_id': 'ipv6_vip_port_id',
        'availability_zone_list': 'availability_zone_list',
        'enterprise_project_id': 'enterprise_project_id',
        'l4_flavor_id': 'l4_flavor_id',
        'l4_scale_flavor_id': 'l4_scale_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'l7_scale_flavor_id': 'l7_scale_flavor_id',
        'publicips': 'publicips',
        'elb_virsubnet_ids': 'elb_virsubnet_ids',
        'elb_virsubnet_type': 'elb_virsubnet_type',
        'ip_target_enable': 'ip_target_enable',
        'deletion_protection_enable': 'deletion_protection_enable',
        'frozen_scene': 'frozen_scene',
        'ipv6_bandwidth': 'ipv6_bandwidth'
    }

    def __init__(self, id=None, description=None, provisioning_status=None, admin_state_up=None, provider=None, pools=None, listeners=None, operating_status=None, vip_address=None, vip_subnet_cidr_id=None, name=None, project_id=None, vip_port_id=None, tags=None, created_at=None, updated_at=None, guaranteed=None, vpc_id=None, eips=None, ipv6_vip_address=None, ipv6_vip_virsubnet_id=None, ipv6_vip_port_id=None, availability_zone_list=None, enterprise_project_id=None, l4_flavor_id=None, l4_scale_flavor_id=None, l7_flavor_id=None, l7_scale_flavor_id=None, publicips=None, elb_virsubnet_ids=None, elb_virsubnet_type=None, ip_target_enable=None, deletion_protection_enable=None, frozen_scene=None, ipv6_bandwidth=None):
        """LoadBalancer - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._description = None
        self._provisioning_status = None
        self._admin_state_up = None
        self._provider = None
        self._pools = None
        self._listeners = None
        self._operating_status = None
        self._vip_address = None
        self._vip_subnet_cidr_id = None
        self._name = None
        self._project_id = None
        self._vip_port_id = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self._guaranteed = None
        self._vpc_id = None
        self._eips = None
        self._ipv6_vip_address = None
        self._ipv6_vip_virsubnet_id = None
        self._ipv6_vip_port_id = None
        self._availability_zone_list = None
        self._enterprise_project_id = None
        self._l4_flavor_id = None
        self._l4_scale_flavor_id = None
        self._l7_flavor_id = None
        self._l7_scale_flavor_id = None
        self._publicips = None
        self._elb_virsubnet_ids = None
        self._elb_virsubnet_type = None
        self._ip_target_enable = None
        self._deletion_protection_enable = None
        self._frozen_scene = None
        self._ipv6_bandwidth = None
        self.discriminator = None

        self.id = id
        self.description = description
        self.provisioning_status = provisioning_status
        self.admin_state_up = admin_state_up
        self.provider = provider
        self.pools = pools
        self.listeners = listeners
        self.operating_status = operating_status
        self.vip_address = vip_address
        self.vip_subnet_cidr_id = vip_subnet_cidr_id
        self.name = name
        self.project_id = project_id
        self.vip_port_id = vip_port_id
        self.tags = tags
        self.created_at = created_at
        self.updated_at = updated_at
        self.guaranteed = guaranteed
        self.vpc_id = vpc_id
        self.eips = eips
        self.ipv6_vip_address = ipv6_vip_address
        self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        self.ipv6_vip_port_id = ipv6_vip_port_id
        self.availability_zone_list = availability_zone_list
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.l4_flavor_id = l4_flavor_id
        self.l4_scale_flavor_id = l4_scale_flavor_id
        self.l7_flavor_id = l7_flavor_id
        self.l7_scale_flavor_id = l7_scale_flavor_id
        if publicips is not None:
            self.publicips = publicips
        if elb_virsubnet_ids is not None:
            self.elb_virsubnet_ids = elb_virsubnet_ids
        if elb_virsubnet_type is not None:
            self.elb_virsubnet_type = elb_virsubnet_type
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable
        self.frozen_scene = frozen_scene
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth

    @property
    def id(self):
        """Gets the id of this LoadBalancer.

        功能描述：负载均衡器ID。

        :return: The id of this LoadBalancer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoadBalancer.

        功能描述：负载均衡器ID。

        :param id: The id of this LoadBalancer.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this LoadBalancer.

        功能描述：负载均衡器描述信息。

        :return: The description of this LoadBalancer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LoadBalancer.

        功能描述：负载均衡器描述信息。

        :param description: The description of this LoadBalancer.
        :type: str
        """
        self._description = description

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this LoadBalancer.

        功能描述：负载均衡器的配置状态。 取值范围：ACTIVE、PENDING_CREATE 或者ERROR。 约束：该字段为预留字段，暂未启用，默认为ACTIVE。

        :return: The provisioning_status of this LoadBalancer.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadBalancer.

        功能描述：负载均衡器的配置状态。 取值范围：ACTIVE、PENDING_CREATE 或者ERROR。 约束：该字段为预留字段，暂未启用，默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this LoadBalancer.
        :type: str
        """
        self._provisioning_status = provisioning_status

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this LoadBalancer.

        功能描述：负载均衡器的管理状态。 约束：只支持设定为true。

        :return: The admin_state_up of this LoadBalancer.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this LoadBalancer.

        功能描述：负载均衡器的管理状态。 约束：只支持设定为true。

        :param admin_state_up: The admin_state_up of this LoadBalancer.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def provider(self):
        """Gets the provider of this LoadBalancer.

        功能描述：负载均衡器的生产者名称。 约束：只支持vlb。

        :return: The provider of this LoadBalancer.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this LoadBalancer.

        功能描述：负载均衡器的生产者名称。 约束：只支持vlb。

        :param provider: The provider of this LoadBalancer.
        :type: str
        """
        self._provider = provider

    @property
    def pools(self):
        """Gets the pools of this LoadBalancer.

        功能描述：负载均衡器关联的后端云服务器组ID的列表。

        :return: The pools of this LoadBalancer.
        :rtype: list[PoolRef]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this LoadBalancer.

        功能描述：负载均衡器关联的后端云服务器组ID的列表。

        :param pools: The pools of this LoadBalancer.
        :type: list[PoolRef]
        """
        self._pools = pools

    @property
    def listeners(self):
        """Gets the listeners of this LoadBalancer.

        功能描述：负载均衡器关联的监听器ID的列表。

        :return: The listeners of this LoadBalancer.
        :rtype: list[ListenerRef]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this LoadBalancer.

        功能描述：负载均衡器关联的监听器ID的列表。

        :param listeners: The listeners of this LoadBalancer.
        :type: list[ListenerRef]
        """
        self._listeners = listeners

    @property
    def operating_status(self):
        """Gets the operating_status of this LoadBalancer.

        功能描述：负载均衡器的操作状态。 取值范围：ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。 约束：该字段为预留字段，暂未启用，默认为ONLINE。

        :return: The operating_status of this LoadBalancer.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this LoadBalancer.

        功能描述：负载均衡器的操作状态。 取值范围：ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。 约束：该字段为预留字段，暂未启用，默认为ONLINE。

        :param operating_status: The operating_status of this LoadBalancer.
        :type: str
        """
        self._operating_status = operating_status

    @property
    def vip_address(self):
        """Gets the vip_address of this LoadBalancer.

        功能描述：负载均衡器的虚拟IP。

        :return: The vip_address of this LoadBalancer.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this LoadBalancer.

        功能描述：负载均衡器的虚拟IP。

        :param vip_address: The vip_address of this LoadBalancer.
        :type: str
        """
        self._vip_address = vip_address

    @property
    def vip_subnet_cidr_id(self):
        """Gets the vip_subnet_cidr_id of this LoadBalancer.

        功能描述：负载均衡器所在的子网ID。 约束：vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :return: The vip_subnet_cidr_id of this LoadBalancer.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        """Sets the vip_subnet_cidr_id of this LoadBalancer.

        功能描述：负载均衡器所在的子网ID。 约束：vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this LoadBalancer.
        :type: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def name(self):
        """Gets the name of this LoadBalancer.

        功能描述：负载均衡器的负载均衡器名称。

        :return: The name of this LoadBalancer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadBalancer.

        功能描述：负载均衡器的负载均衡器名称。

        :param name: The name of this LoadBalancer.
        :type: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this LoadBalancer.

        负载均衡器所在的项目ID。

        :return: The project_id of this LoadBalancer.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this LoadBalancer.

        负载均衡器所在的项目ID。

        :param project_id: The project_id of this LoadBalancer.
        :type: str
        """
        self._project_id = project_id

    @property
    def vip_port_id(self):
        """Gets the vip_port_id of this LoadBalancer.

        负载均衡器虚拟IP对应的端口ID。

        :return: The vip_port_id of this LoadBalancer.
        :rtype: str
        """
        return self._vip_port_id

    @vip_port_id.setter
    def vip_port_id(self, vip_port_id):
        """Sets the vip_port_id of this LoadBalancer.

        负载均衡器虚拟IP对应的端口ID。

        :param vip_port_id: The vip_port_id of this LoadBalancer.
        :type: str
        """
        self._vip_port_id = vip_port_id

    @property
    def tags(self):
        """Gets the tags of this LoadBalancer.

        功能描述：负载均衡的标签列表。

        :return: The tags of this LoadBalancer.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this LoadBalancer.

        功能描述：负载均衡的标签列表。

        :param tags: The tags of this LoadBalancer.
        :type: list[Tag]
        """
        self._tags = tags

    @property
    def created_at(self):
        """Gets the created_at of this LoadBalancer.

        功能描述：负载均衡器的创建时间。

        :return: The created_at of this LoadBalancer.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LoadBalancer.

        功能描述：负载均衡器的创建时间。

        :param created_at: The created_at of this LoadBalancer.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this LoadBalancer.

        功能描述：负载均衡器的更新时间。

        :return: The updated_at of this LoadBalancer.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LoadBalancer.

        功能描述：负载均衡器的更新时间。

        :param updated_at: The updated_at of this LoadBalancer.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def guaranteed(self):
        """Gets the guaranteed of this LoadBalancer.

        功能描述：是否是性能保障性实例 取值范围：共享型：false；性能保障型：true

        :return: The guaranteed of this LoadBalancer.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        """Sets the guaranteed of this LoadBalancer.

        功能描述：是否是性能保障性实例 取值范围：共享型：false；性能保障型：true

        :param guaranteed: The guaranteed of this LoadBalancer.
        :type: bool
        """
        self._guaranteed = guaranteed

    @property
    def vpc_id(self):
        """Gets the vpc_id of this LoadBalancer.

        功能描述：实例对应的vpc属性。若无，则从vip_subnet_cidr_id获取。  约束：vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :return: The vpc_id of this LoadBalancer.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this LoadBalancer.

        功能描述：实例对应的vpc属性。若无，则从vip_subnet_cidr_id获取。  约束：vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :param vpc_id: The vpc_id of this LoadBalancer.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def eips(self):
        """Gets the eips of this LoadBalancer.

        功能描述：公网ELB实例绑定EIP信息。

        :return: The eips of this LoadBalancer.
        :rtype: list[EipInfo]
        """
        return self._eips

    @eips.setter
    def eips(self, eips):
        """Sets the eips of this LoadBalancer.

        功能描述：公网ELB实例绑定EIP信息。

        :param eips: The eips of this LoadBalancer.
        :type: list[EipInfo]
        """
        self._eips = eips

    @property
    def ipv6_vip_address(self):
        """Gets the ipv6_vip_address of this LoadBalancer.

        功能描述：双栈实例对应v6的ip地址。 

        :return: The ipv6_vip_address of this LoadBalancer.
        :rtype: str
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        """Sets the ipv6_vip_address of this LoadBalancer.

        功能描述：双栈实例对应v6的ip地址。 

        :param ipv6_vip_address: The ipv6_vip_address of this LoadBalancer.
        :type: str
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def ipv6_vip_virsubnet_id(self):
        """Gets the ipv6_vip_virsubnet_id of this LoadBalancer.

        功能描述：双栈实例对应v6的网络id 。 约束： 1、默认为空，只有开启IPv6时才会传入。 2、vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :return: The ipv6_vip_virsubnet_id of this LoadBalancer.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        """Sets the ipv6_vip_virsubnet_id of this LoadBalancer.

        功能描述：双栈实例对应v6的网络id 。 约束： 1、默认为空，只有开启IPv6时才会传入。 2、vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this LoadBalancer.
        :type: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def ipv6_vip_port_id(self):
        """Gets the ipv6_vip_port_id of this LoadBalancer.

        功能描述：IPv6的VIP端口id。

        :return: The ipv6_vip_port_id of this LoadBalancer.
        :rtype: str
        """
        return self._ipv6_vip_port_id

    @ipv6_vip_port_id.setter
    def ipv6_vip_port_id(self, ipv6_vip_port_id):
        """Sets the ipv6_vip_port_id of this LoadBalancer.

        功能描述：IPv6的VIP端口id。

        :param ipv6_vip_port_id: The ipv6_vip_port_id of this LoadBalancer.
        :type: str
        """
        self._ipv6_vip_port_id = ipv6_vip_port_id

    @property
    def availability_zone_list(self):
        """Gets the availability_zone_list of this LoadBalancer.

        功能描述：可用区列表。默认指定所有可利用的AZ。可调用nova接口（/v2/{project_id}/os-availability-zone）查询可用AZ

        :return: The availability_zone_list of this LoadBalancer.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        """Sets the availability_zone_list of this LoadBalancer.

        功能描述：可用区列表。默认指定所有可利用的AZ。可调用nova接口（/v2/{project_id}/os-availability-zone）查询可用AZ

        :param availability_zone_list: The availability_zone_list of this LoadBalancer.
        :type: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this LoadBalancer.

        功能描述：企业项目ID

        :return: The enterprise_project_id of this LoadBalancer.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this LoadBalancer.

        功能描述：企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this LoadBalancer.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def l4_flavor_id(self):
        """Gets the l4_flavor_id of this LoadBalancer.

        功能描述：四层Flavor。

        :return: The l4_flavor_id of this LoadBalancer.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        """Sets the l4_flavor_id of this LoadBalancer.

        功能描述：四层Flavor。

        :param l4_flavor_id: The l4_flavor_id of this LoadBalancer.
        :type: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l4_scale_flavor_id(self):
        """Gets the l4_scale_flavor_id of this LoadBalancer.

        功能描述：预留L4 弹性flavor。

        :return: The l4_scale_flavor_id of this LoadBalancer.
        :rtype: str
        """
        return self._l4_scale_flavor_id

    @l4_scale_flavor_id.setter
    def l4_scale_flavor_id(self, l4_scale_flavor_id):
        """Sets the l4_scale_flavor_id of this LoadBalancer.

        功能描述：预留L4 弹性flavor。

        :param l4_scale_flavor_id: The l4_scale_flavor_id of this LoadBalancer.
        :type: str
        """
        self._l4_scale_flavor_id = l4_scale_flavor_id

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this LoadBalancer.

        功能描述：七层Flavor。

        :return: The l7_flavor_id of this LoadBalancer.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this LoadBalancer.

        功能描述：七层Flavor。

        :param l7_flavor_id: The l7_flavor_id of this LoadBalancer.
        :type: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def l7_scale_flavor_id(self):
        """Gets the l7_scale_flavor_id of this LoadBalancer.

        功能描述：预留弹性flavor。 

        :return: The l7_scale_flavor_id of this LoadBalancer.
        :rtype: str
        """
        return self._l7_scale_flavor_id

    @l7_scale_flavor_id.setter
    def l7_scale_flavor_id(self, l7_scale_flavor_id):
        """Sets the l7_scale_flavor_id of this LoadBalancer.

        功能描述：预留弹性flavor。 

        :param l7_scale_flavor_id: The l7_scale_flavor_id of this LoadBalancer.
        :type: str
        """
        self._l7_scale_flavor_id = l7_scale_flavor_id

    @property
    def publicips(self):
        """Gets the publicips of this LoadBalancer.

        功能描述：弹性公网EIP信息

        :return: The publicips of this LoadBalancer.
        :rtype: list[PublicIpInfo]
        """
        return self._publicips

    @publicips.setter
    def publicips(self, publicips):
        """Sets the publicips of this LoadBalancer.

        功能描述：弹性公网EIP信息

        :param publicips: The publicips of this LoadBalancer.
        :type: list[PublicIpInfo]
        """
        self._publicips = publicips

    @property
    def elb_virsubnet_ids(self):
        """Gets the elb_virsubnet_ids of this LoadBalancer.

        功能描述：下联面子网ID  loadbalancer使用的下联面端口会动态的从这些网络中占用IP

        :return: The elb_virsubnet_ids of this LoadBalancer.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        """Sets the elb_virsubnet_ids of this LoadBalancer.

        功能描述：下联面子网ID  loadbalancer使用的下联面端口会动态的从这些网络中占用IP

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this LoadBalancer.
        :type: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def elb_virsubnet_type(self):
        """Gets the elb_virsubnet_type of this LoadBalancer.

        功能描述：下联面子网类型

        :return: The elb_virsubnet_type of this LoadBalancer.
        :rtype: str
        """
        return self._elb_virsubnet_type

    @elb_virsubnet_type.setter
    def elb_virsubnet_type(self, elb_virsubnet_type):
        """Sets the elb_virsubnet_type of this LoadBalancer.

        功能描述：下联面子网类型

        :param elb_virsubnet_type: The elb_virsubnet_type of this LoadBalancer.
        :type: str
        """
        self._elb_virsubnet_type = elb_virsubnet_type

    @property
    def ip_target_enable(self):
        """Gets the ip_target_enable of this LoadBalancer.

        是否启用跨VPC后端转发

        :return: The ip_target_enable of this LoadBalancer.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        """Sets the ip_target_enable of this LoadBalancer.

        是否启用跨VPC后端转发

        :param ip_target_enable: The ip_target_enable of this LoadBalancer.
        :type: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def deletion_protection_enable(self):
        """Gets the deletion_protection_enable of this LoadBalancer.

        是否开启删除保护

        :return: The deletion_protection_enable of this LoadBalancer.
        :rtype: str
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        """Sets the deletion_protection_enable of this LoadBalancer.

        是否开启删除保护

        :param deletion_protection_enable: The deletion_protection_enable of this LoadBalancer.
        :type: str
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def frozen_scene(self):
        """Gets the frozen_scene of this LoadBalancer.

        负载均衡器的冻结场景。若负载均衡器有多个冻结场景，用逗号分隔 POLICE：公安冻结场景。 ILLEGAL：违规冻结场景。 VERIFY：客户未实名认证冻结场景。 PARTNER：合作伙伴冻结（合作伙伴冻结子客户资源）。 ARREAR：欠费冻结场景。

        :return: The frozen_scene of this LoadBalancer.
        :rtype: str
        """
        return self._frozen_scene

    @frozen_scene.setter
    def frozen_scene(self, frozen_scene):
        """Sets the frozen_scene of this LoadBalancer.

        负载均衡器的冻结场景。若负载均衡器有多个冻结场景，用逗号分隔 POLICE：公安冻结场景。 ILLEGAL：违规冻结场景。 VERIFY：客户未实名认证冻结场景。 PARTNER：合作伙伴冻结（合作伙伴冻结子客户资源）。 ARREAR：欠费冻结场景。

        :param frozen_scene: The frozen_scene of this LoadBalancer.
        :type: str
        """
        self._frozen_scene = frozen_scene

    @property
    def ipv6_bandwidth(self):
        """Gets the ipv6_bandwidth of this LoadBalancer.


        :return: The ipv6_bandwidth of this LoadBalancer.
        :rtype: BandwidthRef
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        """Sets the ipv6_bandwidth of this LoadBalancer.


        :param ipv6_bandwidth: The ipv6_bandwidth of this LoadBalancer.
        :type: BandwidthRef
        """
        self._ipv6_bandwidth = ipv6_bandwidth

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoadBalancer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
