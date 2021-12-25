# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'name': 'str',
        'project_id': 'str',
        'vip_subnet_cidr_id': 'str',
        'vip_address': 'str',
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
        'billing_info': 'str',
        'l4_flavor_id': 'str',
        'l4_scale_flavor_id': 'str',
        'l7_flavor_id': 'str',
        'l7_scale_flavor_id': 'str',
        'publicips': 'list[PublicIpInfo]',
        'elb_virsubnet_ids': 'list[str]',
        'elb_virsubnet_type': 'str',
        'ip_target_enable': 'bool',
        'frozen_scene': 'str',
        'ipv6_bandwidth': 'BandwidthRef',
        'deletion_protection_enable': 'bool',
        'autoscaling': 'AutoscalingRef'
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
        'name': 'name',
        'project_id': 'project_id',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'vip_address': 'vip_address',
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
        'billing_info': 'billing_info',
        'l4_flavor_id': 'l4_flavor_id',
        'l4_scale_flavor_id': 'l4_scale_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'l7_scale_flavor_id': 'l7_scale_flavor_id',
        'publicips': 'publicips',
        'elb_virsubnet_ids': 'elb_virsubnet_ids',
        'elb_virsubnet_type': 'elb_virsubnet_type',
        'ip_target_enable': 'ip_target_enable',
        'frozen_scene': 'frozen_scene',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'deletion_protection_enable': 'deletion_protection_enable',
        'autoscaling': 'autoscaling'
    }

    def __init__(self, id=None, description=None, provisioning_status=None, admin_state_up=None, provider=None, pools=None, listeners=None, operating_status=None, name=None, project_id=None, vip_subnet_cidr_id=None, vip_address=None, vip_port_id=None, tags=None, created_at=None, updated_at=None, guaranteed=None, vpc_id=None, eips=None, ipv6_vip_address=None, ipv6_vip_virsubnet_id=None, ipv6_vip_port_id=None, availability_zone_list=None, enterprise_project_id=None, billing_info=None, l4_flavor_id=None, l4_scale_flavor_id=None, l7_flavor_id=None, l7_scale_flavor_id=None, publicips=None, elb_virsubnet_ids=None, elb_virsubnet_type=None, ip_target_enable=None, frozen_scene=None, ipv6_bandwidth=None, deletion_protection_enable=None, autoscaling=None):
        """LoadBalancer - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._description = None
        self._provisioning_status = None
        self._admin_state_up = None
        self._provider = None
        self._pools = None
        self._listeners = None
        self._operating_status = None
        self._name = None
        self._project_id = None
        self._vip_subnet_cidr_id = None
        self._vip_address = None
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
        self._billing_info = None
        self._l4_flavor_id = None
        self._l4_scale_flavor_id = None
        self._l7_flavor_id = None
        self._l7_scale_flavor_id = None
        self._publicips = None
        self._elb_virsubnet_ids = None
        self._elb_virsubnet_type = None
        self._ip_target_enable = None
        self._frozen_scene = None
        self._ipv6_bandwidth = None
        self._deletion_protection_enable = None
        self._autoscaling = None
        self.discriminator = None

        self.id = id
        self.description = description
        self.provisioning_status = provisioning_status
        self.admin_state_up = admin_state_up
        self.provider = provider
        self.pools = pools
        self.listeners = listeners
        self.operating_status = operating_status
        self.name = name
        self.project_id = project_id
        self.vip_subnet_cidr_id = vip_subnet_cidr_id
        self.vip_address = vip_address
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
        self.enterprise_project_id = enterprise_project_id
        self.billing_info = billing_info
        self.l4_flavor_id = l4_flavor_id
        self.l4_scale_flavor_id = l4_scale_flavor_id
        self.l7_flavor_id = l7_flavor_id
        self.l7_scale_flavor_id = l7_scale_flavor_id
        self.publicips = publicips
        self.elb_virsubnet_ids = elb_virsubnet_ids
        self.elb_virsubnet_type = elb_virsubnet_type
        self.ip_target_enable = ip_target_enable
        self.frozen_scene = frozen_scene
        self.ipv6_bandwidth = ipv6_bandwidth
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable
        if autoscaling is not None:
            self.autoscaling = autoscaling

    @property
    def id(self):
        """Gets the id of this LoadBalancer.

        负载均衡器ID。

        :return: The id of this LoadBalancer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoadBalancer.

        负载均衡器ID。

        :param id: The id of this LoadBalancer.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this LoadBalancer.

        负载均衡器描述信息。

        :return: The description of this LoadBalancer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LoadBalancer.

        负载均衡器描述信息。

        :param description: The description of this LoadBalancer.
        :type: str
        """
        self._description = description

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this LoadBalancer.

        负载均衡器的配置状态。取值： - ACTIVE：使用中。 - PENDING_DELETE：删除中。

        :return: The provisioning_status of this LoadBalancer.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadBalancer.

        负载均衡器的配置状态。取值： - ACTIVE：使用中。 - PENDING_DELETE：删除中。

        :param provisioning_status: The provisioning_status of this LoadBalancer.
        :type: str
        """
        self._provisioning_status = provisioning_status

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this LoadBalancer.

        负载均衡器的管理状态。固定为true。

        :return: The admin_state_up of this LoadBalancer.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this LoadBalancer.

        负载均衡器的管理状态。固定为true。

        :param admin_state_up: The admin_state_up of this LoadBalancer.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def provider(self):
        """Gets the provider of this LoadBalancer.

        负载均衡器的生产者名称。固定为vlb。

        :return: The provider of this LoadBalancer.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this LoadBalancer.

        负载均衡器的生产者名称。固定为vlb。

        :param provider: The provider of this LoadBalancer.
        :type: str
        """
        self._provider = provider

    @property
    def pools(self):
        """Gets the pools of this LoadBalancer.

        负载均衡器直接关联的后端云服务器组的ID列表。

        :return: The pools of this LoadBalancer.
        :rtype: list[PoolRef]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this LoadBalancer.

        负载均衡器直接关联的后端云服务器组的ID列表。

        :param pools: The pools of this LoadBalancer.
        :type: list[PoolRef]
        """
        self._pools = pools

    @property
    def listeners(self):
        """Gets the listeners of this LoadBalancer.

        负载均衡器关联的监听器的ID列表。

        :return: The listeners of this LoadBalancer.
        :rtype: list[ListenerRef]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this LoadBalancer.

        负载均衡器关联的监听器的ID列表。

        :param listeners: The listeners of this LoadBalancer.
        :type: list[ListenerRef]
        """
        self._listeners = listeners

    @property
    def operating_status(self):
        """Gets the operating_status of this LoadBalancer.

        负载均衡器的操作状态。取值： - ONLINE：在线。

        :return: The operating_status of this LoadBalancer.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this LoadBalancer.

        负载均衡器的操作状态。取值： - ONLINE：在线。

        :param operating_status: The operating_status of this LoadBalancer.
        :type: str
        """
        self._operating_status = operating_status

    @property
    def name(self):
        """Gets the name of this LoadBalancer.

        负载均衡器的名称。

        :return: The name of this LoadBalancer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadBalancer.

        负载均衡器的名称。

        :param name: The name of this LoadBalancer.
        :type: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this LoadBalancer.

        负载均衡器所属的项目ID。

        :return: The project_id of this LoadBalancer.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this LoadBalancer.

        负载均衡器所属的项目ID。

        :param project_id: The project_id of this LoadBalancer.
        :type: str
        """
        self._project_id = project_id

    @property
    def vip_subnet_cidr_id(self):
        """Gets the vip_subnet_cidr_id of this LoadBalancer.

        负载均衡器所在子网的IPv4子网ID。

        :return: The vip_subnet_cidr_id of this LoadBalancer.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        """Sets the vip_subnet_cidr_id of this LoadBalancer.

        负载均衡器所在子网的IPv4子网ID。

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this LoadBalancer.
        :type: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def vip_address(self):
        """Gets the vip_address of this LoadBalancer.

        负载均衡器的IPv4虚拟IP地址。

        :return: The vip_address of this LoadBalancer.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this LoadBalancer.

        负载均衡器的IPv4虚拟IP地址。

        :param vip_address: The vip_address of this LoadBalancer.
        :type: str
        """
        self._vip_address = vip_address

    @property
    def vip_port_id(self):
        """Gets the vip_port_id of this LoadBalancer.

        负载均衡器的IPv4对应的port ID。

        :return: The vip_port_id of this LoadBalancer.
        :rtype: str
        """
        return self._vip_port_id

    @vip_port_id.setter
    def vip_port_id(self, vip_port_id):
        """Sets the vip_port_id of this LoadBalancer.

        负载均衡器的IPv4对应的port ID。

        :param vip_port_id: The vip_port_id of this LoadBalancer.
        :type: str
        """
        self._vip_port_id = vip_port_id

    @property
    def tags(self):
        """Gets the tags of this LoadBalancer.

        负载均衡的标签列表。

        :return: The tags of this LoadBalancer.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this LoadBalancer.

        负载均衡的标签列表。

        :param tags: The tags of this LoadBalancer.
        :type: list[Tag]
        """
        self._tags = tags

    @property
    def created_at(self):
        """Gets the created_at of this LoadBalancer.

        负载均衡器的创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'

        :return: The created_at of this LoadBalancer.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LoadBalancer.

        负载均衡器的创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'

        :param created_at: The created_at of this LoadBalancer.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this LoadBalancer.

        负载均衡器的更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'

        :return: The updated_at of this LoadBalancer.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LoadBalancer.

        负载均衡器的更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'

        :param updated_at: The updated_at of this LoadBalancer.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def guaranteed(self):
        """Gets the guaranteed of this LoadBalancer.

        是否独享型LB，取值： - false：共享型。 - true：独享型。

        :return: The guaranteed of this LoadBalancer.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        """Sets the guaranteed of this LoadBalancer.

        是否独享型LB，取值： - false：共享型。 - true：独享型。

        :param guaranteed: The guaranteed of this LoadBalancer.
        :type: bool
        """
        self._guaranteed = guaranteed

    @property
    def vpc_id(self):
        """Gets the vpc_id of this LoadBalancer.

        负载均衡器所在VPC ID。

        :return: The vpc_id of this LoadBalancer.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this LoadBalancer.

        负载均衡器所在VPC ID。

        :param vpc_id: The vpc_id of this LoadBalancer.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def eips(self):
        """Gets the eips of this LoadBalancer.

        负载均衡器绑定的EIP。只支持绑定一个EIP。  注：该字段与publicips一致。

        :return: The eips of this LoadBalancer.
        :rtype: list[EipInfo]
        """
        return self._eips

    @eips.setter
    def eips(self, eips):
        """Sets the eips of this LoadBalancer.

        负载均衡器绑定的EIP。只支持绑定一个EIP。  注：该字段与publicips一致。

        :param eips: The eips of this LoadBalancer.
        :type: list[EipInfo]
        """
        self._eips = eips

    @property
    def ipv6_vip_address(self):
        """Gets the ipv6_vip_address of this LoadBalancer.

        双栈类型负载均衡器的IPv6地址。  [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :return: The ipv6_vip_address of this LoadBalancer.
        :rtype: str
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        """Sets the ipv6_vip_address of this LoadBalancer.

        双栈类型负载均衡器的IPv6地址。  [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :param ipv6_vip_address: The ipv6_vip_address of this LoadBalancer.
        :type: str
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def ipv6_vip_virsubnet_id(self):
        """Gets the ipv6_vip_virsubnet_id of this LoadBalancer.

        双栈类型负载均衡器所在子网的IPv6网络ID。  [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :return: The ipv6_vip_virsubnet_id of this LoadBalancer.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        """Sets the ipv6_vip_virsubnet_id of this LoadBalancer.

        双栈类型负载均衡器所在子网的IPv6网络ID。  [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this LoadBalancer.
        :type: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def ipv6_vip_port_id(self):
        """Gets the ipv6_vip_port_id of this LoadBalancer.

        双栈类型负载均衡器的IPv6对应的port ID。  [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :return: The ipv6_vip_port_id of this LoadBalancer.
        :rtype: str
        """
        return self._ipv6_vip_port_id

    @ipv6_vip_port_id.setter
    def ipv6_vip_port_id(self, ipv6_vip_port_id):
        """Sets the ipv6_vip_port_id of this LoadBalancer.

        双栈类型负载均衡器的IPv6对应的port ID。  [不支持IPv6，请勿使用。](tag:dt,dt_test)

        :param ipv6_vip_port_id: The ipv6_vip_port_id of this LoadBalancer.
        :type: str
        """
        self._ipv6_vip_port_id = ipv6_vip_port_id

    @property
    def availability_zone_list(self):
        """Gets the availability_zone_list of this LoadBalancer.

        负载均衡器所在的可用区列表。

        :return: The availability_zone_list of this LoadBalancer.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        """Sets the availability_zone_list of this LoadBalancer.

        负载均衡器所在的可用区列表。

        :param availability_zone_list: The availability_zone_list of this LoadBalancer.
        :type: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this LoadBalancer.

        企业项目ID。  [不支持该字段，请勿使用](tag:dt,dt_test)

        :return: The enterprise_project_id of this LoadBalancer.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this LoadBalancer.

        企业项目ID。  [不支持该字段，请勿使用](tag:dt,dt_test)

        :param enterprise_project_id: The enterprise_project_id of this LoadBalancer.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def billing_info(self):
        """Gets the billing_info of this LoadBalancer.

        资源账单信息，取值： - 空：按需计费。 - 非空：包周期计费， 包周期计费billing_info字段的格式为：order_id&#58;product_id&#58;region_id&#58;project_id，如： CS2107161019CDJZZ&#58;OFFI569702121789763584&#58;eu-de&#58;057ef081eb00d2732fd1c01a9be75e6f 使用说明： - admin权限才能更新此字段。 [不支持该字段，请勿使用](tag:dt,dt_test)

        :return: The billing_info of this LoadBalancer.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this LoadBalancer.

        资源账单信息，取值： - 空：按需计费。 - 非空：包周期计费， 包周期计费billing_info字段的格式为：order_id&#58;product_id&#58;region_id&#58;project_id，如： CS2107161019CDJZZ&#58;OFFI569702121789763584&#58;eu-de&#58;057ef081eb00d2732fd1c01a9be75e6f 使用说明： - admin权限才能更新此字段。 [不支持该字段，请勿使用](tag:dt,dt_test)

        :param billing_info: The billing_info of this LoadBalancer.
        :type: str
        """
        self._billing_info = billing_info

    @property
    def l4_flavor_id(self):
        """Gets the l4_flavor_id of this LoadBalancer.

        四层Flavor ID。  [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hws,hcso)

        :return: The l4_flavor_id of this LoadBalancer.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        """Sets the l4_flavor_id of this LoadBalancer.

        四层Flavor ID。  [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hws,hcso)

        :param l4_flavor_id: The l4_flavor_id of this LoadBalancer.
        :type: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l4_scale_flavor_id(self):
        """Gets the l4_scale_flavor_id of this LoadBalancer.

        四层弹性Flavor ID。  不支持该字段，请勿使用。

        :return: The l4_scale_flavor_id of this LoadBalancer.
        :rtype: str
        """
        return self._l4_scale_flavor_id

    @l4_scale_flavor_id.setter
    def l4_scale_flavor_id(self, l4_scale_flavor_id):
        """Sets the l4_scale_flavor_id of this LoadBalancer.

        四层弹性Flavor ID。  不支持该字段，请勿使用。

        :param l4_scale_flavor_id: The l4_scale_flavor_id of this LoadBalancer.
        :type: str
        """
        self._l4_scale_flavor_id = l4_scale_flavor_id

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this LoadBalancer.

        七层Flavor ID。  [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hws,hcso)

        :return: The l7_flavor_id of this LoadBalancer.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this LoadBalancer.

        七层Flavor ID。  [hsco场景下所有LB实例共享带宽，该字段无效，请勿使用。](tag:hws,hcso)

        :param l7_flavor_id: The l7_flavor_id of this LoadBalancer.
        :type: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def l7_scale_flavor_id(self):
        """Gets the l7_scale_flavor_id of this LoadBalancer.

        七层弹性Flavor ID。  不支持该字段，请勿使用。

        :return: The l7_scale_flavor_id of this LoadBalancer.
        :rtype: str
        """
        return self._l7_scale_flavor_id

    @l7_scale_flavor_id.setter
    def l7_scale_flavor_id(self, l7_scale_flavor_id):
        """Sets the l7_scale_flavor_id of this LoadBalancer.

        七层弹性Flavor ID。  不支持该字段，请勿使用。

        :param l7_scale_flavor_id: The l7_scale_flavor_id of this LoadBalancer.
        :type: str
        """
        self._l7_scale_flavor_id = l7_scale_flavor_id

    @property
    def publicips(self):
        """Gets the publicips of this LoadBalancer.

        负载均衡器绑定的公网IP。只支持绑定一个公网IP。  注：该字段与eips一致。

        :return: The publicips of this LoadBalancer.
        :rtype: list[PublicIpInfo]
        """
        return self._publicips

    @publicips.setter
    def publicips(self, publicips):
        """Sets the publicips of this LoadBalancer.

        负载均衡器绑定的公网IP。只支持绑定一个公网IP。  注：该字段与eips一致。

        :param publicips: The publicips of this LoadBalancer.
        :type: list[PublicIpInfo]
        """
        self._publicips = publicips

    @property
    def elb_virsubnet_ids(self):
        """Gets the elb_virsubnet_ids of this LoadBalancer.

        下联面子网的网络ID列表。可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。 使用说明： - 若不指定该字段，则会在当前负载均衡器所在子网作为下联面子网。 - 若指定多个下联面子网，则按顺序优先使用第一个子网来为负载均衡器下联面端口分配ip地址。 - 下联面子网必须属于该LB所在的VPC。 - 不支持边缘云子网。

        :return: The elb_virsubnet_ids of this LoadBalancer.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        """Sets the elb_virsubnet_ids of this LoadBalancer.

        下联面子网的网络ID列表。可以通过GET https&#58;//{VPC_Endpoint}/v1/{project_id}/subnets 响应参数中的id得到。 使用说明： - 若不指定该字段，则会在当前负载均衡器所在子网作为下联面子网。 - 若指定多个下联面子网，则按顺序优先使用第一个子网来为负载均衡器下联面端口分配ip地址。 - 下联面子网必须属于该LB所在的VPC。 - 不支持边缘云子网。

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this LoadBalancer.
        :type: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def elb_virsubnet_type(self):
        """Gets the elb_virsubnet_type of this LoadBalancer.

        下联面子网类型 - ipv4：ipv4 - dualstack：双栈

        :return: The elb_virsubnet_type of this LoadBalancer.
        :rtype: str
        """
        return self._elb_virsubnet_type

    @elb_virsubnet_type.setter
    def elb_virsubnet_type(self, elb_virsubnet_type):
        """Sets the elb_virsubnet_type of this LoadBalancer.

        下联面子网类型 - ipv4：ipv4 - dualstack：双栈

        :param elb_virsubnet_type: The elb_virsubnet_type of this LoadBalancer.
        :type: str
        """
        self._elb_virsubnet_type = elb_virsubnet_type

    @property
    def ip_target_enable(self):
        """Gets the ip_target_enable of this LoadBalancer.

        是否启用跨VPC后端转发。取值： - true：开启。 - false：不开启。  仅独享型负载均衡器支持该特性。  开启跨VPC后端转发后，后端服务器组支持添加其他VPC、其他公有云、云下数据中心的服务器。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :return: The ip_target_enable of this LoadBalancer.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        """Sets the ip_target_enable of this LoadBalancer.

        是否启用跨VPC后端转发。取值： - true：开启。 - false：不开启。  仅独享型负载均衡器支持该特性。  开启跨VPC后端转发后，后端服务器组支持添加其他VPC、其他公有云、云下数据中心的服务器。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :param ip_target_enable: The ip_target_enable of this LoadBalancer.
        :type: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def frozen_scene(self):
        """Gets the frozen_scene of this LoadBalancer.

        负载均衡器的冻结场景。若负载均衡器有多个冻结场景，用逗号分隔。取值： - POLICE：公安冻结场景。 - ILLEGAL：违规冻结场景。 - VERIFY：客户未实名认证冻结场景。 - RTNER：合作伙伴冻结（合作伙伴冻结子客户资源）。 - REAR：欠费冻结场景。  [不支持该字段，请勿使用。](tag:dt,dt_test)

        :return: The frozen_scene of this LoadBalancer.
        :rtype: str
        """
        return self._frozen_scene

    @frozen_scene.setter
    def frozen_scene(self, frozen_scene):
        """Sets the frozen_scene of this LoadBalancer.

        负载均衡器的冻结场景。若负载均衡器有多个冻结场景，用逗号分隔。取值： - POLICE：公安冻结场景。 - ILLEGAL：违规冻结场景。 - VERIFY：客户未实名认证冻结场景。 - RTNER：合作伙伴冻结（合作伙伴冻结子客户资源）。 - REAR：欠费冻结场景。  [不支持该字段，请勿使用。](tag:dt,dt_test)

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

    @property
    def deletion_protection_enable(self):
        """Gets the deletion_protection_enable of this LoadBalancer.

        是否开启删除保护，取值： - false：不开启。 - true：开启。 >退场时需要先关闭所有资源的删除保护开关。  仅当前局点启用删除保护特性后才会返回该字段。

        :return: The deletion_protection_enable of this LoadBalancer.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        """Sets the deletion_protection_enable of this LoadBalancer.

        是否开启删除保护，取值： - false：不开启。 - true：开启。 >退场时需要先关闭所有资源的删除保护开关。  仅当前局点启用删除保护特性后才会返回该字段。

        :param deletion_protection_enable: The deletion_protection_enable of this LoadBalancer.
        :type: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def autoscaling(self):
        """Gets the autoscaling of this LoadBalancer.


        :return: The autoscaling of this LoadBalancer.
        :rtype: AutoscalingRef
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        """Sets the autoscaling of this LoadBalancer.


        :param autoscaling: The autoscaling of this LoadBalancer.
        :type: AutoscalingRef
        """
        self._autoscaling = autoscaling

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
        if not isinstance(other, LoadBalancer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
