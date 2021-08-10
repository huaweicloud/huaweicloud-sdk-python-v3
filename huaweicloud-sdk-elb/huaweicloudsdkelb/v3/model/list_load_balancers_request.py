# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLoadBalancersRequest:


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
        'availability_zone_list': 'list[str]',
        'billing_info': 'list[str]',
        'deletion_protection_enable': 'bool',
        'description': 'list[str]',
        'eips': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'guaranteed': 'bool',
        'id': 'list[str]',
        'ip_version': 'list[int]',
        'ipv6_vip_address': 'list[str]',
        'ipv6_vip_port_id': 'list[str]',
        'ipv6_vip_virsubnet_id': 'list[str]',
        'l4_flavor_id': 'list[str]',
        'l4_scale_flavor_id': 'list[str]',
        'l7_flavor_id': 'list[str]',
        'l7_scale_flavor_id': 'list[str]',
        'limit': 'int',
        'marker': 'str',
        'member_address': 'list[str]',
        'member_device_id': 'list[str]',
        'name': 'list[str]',
        'operating_status': 'list[str]',
        'page_reverse': 'bool',
        'provisioning_status': 'list[str]',
        'publicips': 'list[str]',
        'vip_address': 'list[str]',
        'vip_port_id': 'list[str]',
        'vip_subnet_cidr_id': 'list[str]',
        'vpc_id': 'list[str]'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'availability_zone_list': 'availability_zone_list',
        'billing_info': 'billing_info',
        'deletion_protection_enable': 'deletion_protection_enable',
        'description': 'description',
        'eips': 'eips',
        'enterprise_project_id': 'enterprise_project_id',
        'guaranteed': 'guaranteed',
        'id': 'id',
        'ip_version': 'ip_version',
        'ipv6_vip_address': 'ipv6_vip_address',
        'ipv6_vip_port_id': 'ipv6_vip_port_id',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'l4_flavor_id': 'l4_flavor_id',
        'l4_scale_flavor_id': 'l4_scale_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'l7_scale_flavor_id': 'l7_scale_flavor_id',
        'limit': 'limit',
        'marker': 'marker',
        'member_address': 'member_address',
        'member_device_id': 'member_device_id',
        'name': 'name',
        'operating_status': 'operating_status',
        'page_reverse': 'page_reverse',
        'provisioning_status': 'provisioning_status',
        'publicips': 'publicips',
        'vip_address': 'vip_address',
        'vip_port_id': 'vip_port_id',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, admin_state_up=None, availability_zone_list=None, billing_info=None, deletion_protection_enable=None, description=None, eips=None, enterprise_project_id=None, guaranteed=None, id=None, ip_version=None, ipv6_vip_address=None, ipv6_vip_port_id=None, ipv6_vip_virsubnet_id=None, l4_flavor_id=None, l4_scale_flavor_id=None, l7_flavor_id=None, l7_scale_flavor_id=None, limit=None, marker=None, member_address=None, member_device_id=None, name=None, operating_status=None, page_reverse=None, provisioning_status=None, publicips=None, vip_address=None, vip_port_id=None, vip_subnet_cidr_id=None, vpc_id=None):
        """ListLoadBalancersRequest - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._availability_zone_list = None
        self._billing_info = None
        self._deletion_protection_enable = None
        self._description = None
        self._eips = None
        self._enterprise_project_id = None
        self._guaranteed = None
        self._id = None
        self._ip_version = None
        self._ipv6_vip_address = None
        self._ipv6_vip_port_id = None
        self._ipv6_vip_virsubnet_id = None
        self._l4_flavor_id = None
        self._l4_scale_flavor_id = None
        self._l7_flavor_id = None
        self._l7_scale_flavor_id = None
        self._limit = None
        self._marker = None
        self._member_address = None
        self._member_device_id = None
        self._name = None
        self._operating_status = None
        self._page_reverse = None
        self._provisioning_status = None
        self._publicips = None
        self._vip_address = None
        self._vip_port_id = None
        self._vip_subnet_cidr_id = None
        self._vpc_id = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if availability_zone_list is not None:
            self.availability_zone_list = availability_zone_list
        if billing_info is not None:
            self.billing_info = billing_info
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable
        if description is not None:
            self.description = description
        if eips is not None:
            self.eips = eips
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if guaranteed is not None:
            self.guaranteed = guaranteed
        if id is not None:
            self.id = id
        if ip_version is not None:
            self.ip_version = ip_version
        if ipv6_vip_address is not None:
            self.ipv6_vip_address = ipv6_vip_address
        if ipv6_vip_port_id is not None:
            self.ipv6_vip_port_id = ipv6_vip_port_id
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if l4_scale_flavor_id is not None:
            self.l4_scale_flavor_id = l4_scale_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if l7_scale_flavor_id is not None:
            self.l7_scale_flavor_id = l7_scale_flavor_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if member_address is not None:
            self.member_address = member_address
        if member_device_id is not None:
            self.member_device_id = member_device_id
        if name is not None:
            self.name = name
        if operating_status is not None:
            self.operating_status = operating_status
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if publicips is not None:
            self.publicips = publicips
        if vip_address is not None:
            self.vip_address = vip_address
        if vip_port_id is not None:
            self.vip_port_id = vip_port_id
        if vip_subnet_cidr_id is not None:
            self.vip_subnet_cidr_id = vip_subnet_cidr_id
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListLoadBalancersRequest.

        负载均衡器的管理状态。只支持设定为true。

        :return: The admin_state_up of this ListLoadBalancersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListLoadBalancersRequest.

        负载均衡器的管理状态。只支持设定为true。

        :param admin_state_up: The admin_state_up of this ListLoadBalancersRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def availability_zone_list(self):
        """Gets the availability_zone_list of this ListLoadBalancersRequest.

        可用区。 注： 可用AZ的查询方式可用通过调用nova接口查询 /v2/{project_id}/os-availability-zone

        :return: The availability_zone_list of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        """Sets the availability_zone_list of this ListLoadBalancersRequest.

        可用区。 注： 可用AZ的查询方式可用通过调用nova接口查询 /v2/{project_id}/os-availability-zone

        :param availability_zone_list: The availability_zone_list of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def billing_info(self):
        """Gets the billing_info of this ListLoadBalancersRequest.

        预留资源账单信息，默认为空表示按需计费， 非空为包周期。admin权限才能更新此字段。

        :return: The billing_info of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this ListLoadBalancersRequest.

        预留资源账单信息，默认为空表示按需计费， 非空为包周期。admin权限才能更新此字段。

        :param billing_info: The billing_info of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._billing_info = billing_info

    @property
    def deletion_protection_enable(self):
        """Gets the deletion_protection_enable of this ListLoadBalancersRequest.

        是否开启删除保护，false不开启，默认为空都查询

        :return: The deletion_protection_enable of this ListLoadBalancersRequest.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        """Sets the deletion_protection_enable of this ListLoadBalancersRequest.

        是否开启删除保护，false不开启，默认为空都查询

        :param deletion_protection_enable: The deletion_protection_enable of this ListLoadBalancersRequest.
        :type: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def description(self):
        """Gets the description of this ListLoadBalancersRequest.

        负载均衡器的描述信息。

        :return: The description of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListLoadBalancersRequest.

        负载均衡器的描述信息。

        :param description: The description of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._description = description

    @property
    def eips(self):
        """Gets the eips of this ListLoadBalancersRequest.

        公网ELB实例绑定EIP。 示例如下：  \"eips\": [             {                 \"eip_id\": \"a6ded276-c88a-4c58-95e0-5b6d1d2297b3\",                 \"eip_address\": \"2001:db8:a583:86:cf24:5cc5:8117:6eaa\",                 \"ip_version\": 6             }         ] 查询时指定：eips=eip_id=XXXX

        :return: The eips of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._eips

    @eips.setter
    def eips(self, eips):
        """Sets the eips of this ListLoadBalancersRequest.

        公网ELB实例绑定EIP。 示例如下：  \"eips\": [             {                 \"eip_id\": \"a6ded276-c88a-4c58-95e0-5b6d1d2297b3\",                 \"eip_address\": \"2001:db8:a583:86:cf24:5cc5:8117:6eaa\",                 \"ip_version\": 6             }         ] 查询时指定：eips=eip_id=XXXX

        :param eips: The eips of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._eips = eips

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListLoadBalancersRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListLoadBalancersRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def guaranteed(self):
        """Gets the guaranteed of this ListLoadBalancersRequest.

        共享型：false 性能保障型：true

        :return: The guaranteed of this ListLoadBalancersRequest.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        """Sets the guaranteed of this ListLoadBalancersRequest.

        共享型：false 性能保障型：true

        :param guaranteed: The guaranteed of this ListLoadBalancersRequest.
        :type: bool
        """
        self._guaranteed = guaranteed

    @property
    def id(self):
        """Gets the id of this ListLoadBalancersRequest.

        负载均衡器ID。

        :return: The id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListLoadBalancersRequest.

        负载均衡器ID。

        :param id: The id of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def ip_version(self):
        """Gets the ip_version of this ListLoadBalancersRequest.

        IP版本信息。 取值范围：4和6 4：IPv4 6：IPv6

        :return: The ip_version of this ListLoadBalancersRequest.
        :rtype: list[int]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListLoadBalancersRequest.

        IP版本信息。 取值范围：4和6 4：IPv4 6：IPv6

        :param ip_version: The ip_version of this ListLoadBalancersRequest.
        :type: list[int]
        """
        self._ip_version = ip_version

    @property
    def ipv6_vip_address(self):
        """Gets the ipv6_vip_address of this ListLoadBalancersRequest.

        双栈实例对应v6的ip地址。

        :return: The ipv6_vip_address of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        """Sets the ipv6_vip_address of this ListLoadBalancersRequest.

        双栈实例对应v6的ip地址。

        :param ipv6_vip_address: The ipv6_vip_address of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def ipv6_vip_port_id(self):
        """Gets the ipv6_vip_port_id of this ListLoadBalancersRequest.

        双栈实例对应v6的端口。

        :return: The ipv6_vip_port_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._ipv6_vip_port_id

    @ipv6_vip_port_id.setter
    def ipv6_vip_port_id(self, ipv6_vip_port_id):
        """Sets the ipv6_vip_port_id of this ListLoadBalancersRequest.

        双栈实例对应v6的端口。

        :param ipv6_vip_port_id: The ipv6_vip_port_id of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._ipv6_vip_port_id = ipv6_vip_port_id

    @property
    def ipv6_vip_virsubnet_id(self):
        """Gets the ipv6_vip_virsubnet_id of this ListLoadBalancersRequest.

        双栈实例对应v6的网络id 。 说明：vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空。

        :return: The ipv6_vip_virsubnet_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        """Sets the ipv6_vip_virsubnet_id of this ListLoadBalancersRequest.

        双栈实例对应v6的网络id 。 说明：vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空。

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def l4_flavor_id(self):
        """Gets the l4_flavor_id of this ListLoadBalancersRequest.

        四层Flavor， 按需计费不填， 包周期由用户设置。

        :return: The l4_flavor_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        """Sets the l4_flavor_id of this ListLoadBalancersRequest.

        四层Flavor， 按需计费不填， 包周期由用户设置。

        :param l4_flavor_id: The l4_flavor_id of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l4_scale_flavor_id(self):
        """Gets the l4_scale_flavor_id of this ListLoadBalancersRequest.

        预留弹性flavor。

        :return: The l4_scale_flavor_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._l4_scale_flavor_id

    @l4_scale_flavor_id.setter
    def l4_scale_flavor_id(self, l4_scale_flavor_id):
        """Sets the l4_scale_flavor_id of this ListLoadBalancersRequest.

        预留弹性flavor。

        :param l4_scale_flavor_id: The l4_scale_flavor_id of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._l4_scale_flavor_id = l4_scale_flavor_id

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this ListLoadBalancersRequest.

        七层Flavor， 按需计费不填， 包周期由用户设置。

        :return: The l7_flavor_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this ListLoadBalancersRequest.

        七层Flavor， 按需计费不填， 包周期由用户设置。

        :param l7_flavor_id: The l7_flavor_id of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def l7_scale_flavor_id(self):
        """Gets the l7_scale_flavor_id of this ListLoadBalancersRequest.

        预留弹性flavor。

        :return: The l7_scale_flavor_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._l7_scale_flavor_id

    @l7_scale_flavor_id.setter
    def l7_scale_flavor_id(self, l7_scale_flavor_id):
        """Sets the l7_scale_flavor_id of this ListLoadBalancersRequest.

        预留弹性flavor。

        :param l7_scale_flavor_id: The l7_scale_flavor_id of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._l7_scale_flavor_id = l7_scale_flavor_id

    @property
    def limit(self):
        """Gets the limit of this ListLoadBalancersRequest.

        每页返回的个数。

        :return: The limit of this ListLoadBalancersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListLoadBalancersRequest.

        每页返回的个数。

        :param limit: The limit of this ListLoadBalancersRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListLoadBalancersRequest.

        上一页最后一条记录的ID。  使用说明：  - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListLoadBalancersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListLoadBalancersRequest.

        上一页最后一条记录的ID。  使用说明：  - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListLoadBalancersRequest.
        :type: str
        """
        self._marker = marker

    @property
    def member_address(self):
        """Gets the member_address of this ListLoadBalancersRequest.

        后端云服务器的IP地址。

        :return: The member_address of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        """Sets the member_address of this ListLoadBalancersRequest.

        后端云服务器的IP地址。

        :param member_address: The member_address of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._member_address = member_address

    @property
    def member_device_id(self):
        """Gets the member_device_id of this ListLoadBalancersRequest.

        后端云服务器对应的弹性云服务器的ID。

        :return: The member_device_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        """Sets the member_device_id of this ListLoadBalancersRequest.

        后端云服务器对应的弹性云服务器的ID。

        :param member_device_id: The member_device_id of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._member_device_id = member_device_id

    @property
    def name(self):
        """Gets the name of this ListLoadBalancersRequest.

        负载均衡器名称。

        :return: The name of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListLoadBalancersRequest.

        负载均衡器名称。

        :param name: The name of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def operating_status(self):
        """Gets the operating_status of this ListLoadBalancersRequest.

        负载均衡器的操作状态。 可以为：ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。 说明 该字段为预留字段，暂未启用。

        :return: The operating_status of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this ListLoadBalancersRequest.

        负载均衡器的操作状态。 可以为：ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。 说明 该字段为预留字段，暂未启用。

        :param operating_status: The operating_status of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._operating_status = operating_status

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListLoadBalancersRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。 使用说明：必须与limit一起使用。

        :return: The page_reverse of this ListLoadBalancersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListLoadBalancersRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。 使用说明：必须与limit一起使用。

        :param page_reverse: The page_reverse of this ListLoadBalancersRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this ListLoadBalancersRequest.

        负载均衡器的配置状态。 可以为：ACTIVE、PENDING_CREATE 或者ERROR。 说明 该字段为预留字段，暂未启用。

        :return: The provisioning_status of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this ListLoadBalancersRequest.

        负载均衡器的配置状态。 可以为：ACTIVE、PENDING_CREATE 或者ERROR。 说明 该字段为预留字段，暂未启用。

        :param provisioning_status: The provisioning_status of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._provisioning_status = provisioning_status

    @property
    def publicips(self):
        """Gets the publicips of this ListLoadBalancersRequest.

        公网IP 示例如下：  \"publicips\": [             {                 \"publicip_id\": \"a6ded276-c88a-4c58-95e0-5b6d1d2297b3\",                 \"publicip_address\": \"2001:db8:a583:86:cf24:5cc5:8117:6eaa\",                 \"publicip_ip_version\": 6             }         ] 查询时指定：publicips=publicip_id=XXXX,YYYY

        :return: The publicips of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._publicips

    @publicips.setter
    def publicips(self, publicips):
        """Sets the publicips of this ListLoadBalancersRequest.

        公网IP 示例如下：  \"publicips\": [             {                 \"publicip_id\": \"a6ded276-c88a-4c58-95e0-5b6d1d2297b3\",                 \"publicip_address\": \"2001:db8:a583:86:cf24:5cc5:8117:6eaa\",                 \"publicip_ip_version\": 6             }         ] 查询时指定：publicips=publicip_id=XXXX,YYYY

        :param publicips: The publicips of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._publicips = publicips

    @property
    def vip_address(self):
        """Gets the vip_address of this ListLoadBalancersRequest.

        负载均衡器的虚拟IP。

        :return: The vip_address of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this ListLoadBalancersRequest.

        负载均衡器的虚拟IP。

        :param vip_address: The vip_address of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._vip_address = vip_address

    @property
    def vip_port_id(self):
        """Gets the vip_port_id of this ListLoadBalancersRequest.

        负载均衡器虚拟IP对应的端口ID。

        :return: The vip_port_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._vip_port_id

    @vip_port_id.setter
    def vip_port_id(self, vip_port_id):
        """Sets the vip_port_id of this ListLoadBalancersRequest.

        负载均衡器虚拟IP对应的端口ID。

        :param vip_port_id: The vip_port_id of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._vip_port_id = vip_port_id

    @property
    def vip_subnet_cidr_id(self):
        """Gets the vip_subnet_cidr_id of this ListLoadBalancersRequest.

        负载均衡器所在的子网ID，仅支持内网类型。 说明：vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空。

        :return: The vip_subnet_cidr_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        """Sets the vip_subnet_cidr_id of this ListLoadBalancersRequest.

        负载均衡器所在的子网ID，仅支持内网类型。 说明：vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空。

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListLoadBalancersRequest.

        实例对应的vpc属性。 若无，则从vip_subnet_cidr_id获取。  说明：vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空。

        :return: The vpc_id of this ListLoadBalancersRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListLoadBalancersRequest.

        实例对应的vpc属性。 若无，则从vip_subnet_cidr_id获取。  说明：vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空。

        :param vpc_id: The vpc_id of this ListLoadBalancersRequest.
        :type: list[str]
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, ListLoadBalancersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
