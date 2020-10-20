# coding: utf-8

import pprint
import re

import six





class CreateLoadBalancerOption:


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
        'description': 'str',
        'vip_address': 'str',
        'vip_subnet_cidr_id': 'str',
        'ipv6_vip_virsubnet_id': 'str',
        'provider': 'str',
        'l4_flavor_id': 'str',
        'project_id': 'str',
        'guaranteed': 'bool',
        'vpc_id': 'str',
        'availability_zone_list': 'list[str]',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'admin_state_up': 'bool',
        'l7_flavor_id': 'str',
        'billing_info': 'str',
        'ipv6_bandwidth': 'BandwidthRef',
        'publicip_ids': 'list[str]',
        'publicip': 'CreateLoadBalancerPublicIpOption',
        'elb_virsubnet_ids': 'list[str]',
        'ip_target_enable': 'bool',
        'deletion_protection_enable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'vip_address': 'vip_address',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'provider': 'provider',
        'l4_flavor_id': 'l4_flavor_id',
        'project_id': 'project_id',
        'guaranteed': 'guaranteed',
        'vpc_id': 'vpc_id',
        'availability_zone_list': 'availability_zone_list',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'admin_state_up': 'admin_state_up',
        'l7_flavor_id': 'l7_flavor_id',
        'billing_info': 'billing_info',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'publicip_ids': 'publicip_ids',
        'publicip': 'publicip',
        'elb_virsubnet_ids': 'elb_virsubnet_ids',
        'ip_target_enable': 'ip_target_enable',
        'deletion_protection_enable': 'deletion_protection_enable'
    }

    def __init__(self, name=None, description=None, vip_address=None, vip_subnet_cidr_id=None, ipv6_vip_virsubnet_id=None, provider=None, l4_flavor_id=None, project_id=None, guaranteed=True, vpc_id=None, availability_zone_list=None, enterprise_project_id=None, tags=None, admin_state_up=True, l7_flavor_id=None, billing_info=None, ipv6_bandwidth=None, publicip_ids=None, publicip=None, elb_virsubnet_ids=None, ip_target_enable=False, deletion_protection_enable=False):
        """CreateLoadBalancerOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._vip_address = None
        self._vip_subnet_cidr_id = None
        self._ipv6_vip_virsubnet_id = None
        self._provider = None
        self._l4_flavor_id = None
        self._project_id = None
        self._guaranteed = None
        self._vpc_id = None
        self._availability_zone_list = None
        self._enterprise_project_id = None
        self._tags = None
        self._admin_state_up = None
        self._l7_flavor_id = None
        self._billing_info = None
        self._ipv6_bandwidth = None
        self._publicip_ids = None
        self._publicip = None
        self._elb_virsubnet_ids = None
        self._ip_target_enable = None
        self._deletion_protection_enable = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if vip_address is not None:
            self.vip_address = vip_address
        if vip_subnet_cidr_id is not None:
            self.vip_subnet_cidr_id = vip_subnet_cidr_id
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if provider is not None:
            self.provider = provider
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if project_id is not None:
            self.project_id = project_id
        if guaranteed is not None:
            self.guaranteed = guaranteed
        if vpc_id is not None:
            self.vpc_id = vpc_id
        self.availability_zone_list = availability_zone_list
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if billing_info is not None:
            self.billing_info = billing_info
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth
        if publicip_ids is not None:
            self.publicip_ids = publicip_ids
        if publicip is not None:
            self.publicip = publicip
        if elb_virsubnet_ids is not None:
            self.elb_virsubnet_ids = elb_virsubnet_ids
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable

    @property
    def name(self):
        """Gets the name of this CreateLoadBalancerOption.

        负载均衡器名称。

        :return: The name of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLoadBalancerOption.

        负载均衡器名称。

        :param name: The name of this CreateLoadBalancerOption.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateLoadBalancerOption.

        负载均衡器功能说明。

        :return: The description of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateLoadBalancerOption.

        负载均衡器功能说明。

        :param description: The description of this CreateLoadBalancerOption.
        :type: str
        """
        self._description = description

    @property
    def vip_address(self):
        """Gets the vip_address of this CreateLoadBalancerOption.

        负载均衡器的虚拟IP。 1.传入vip_address时必须传入vip_subnet_cidr_id 2.不传入vip_address，自动分配虚拟IP 3.传入vip_address，需要保证该ip地址在子网中未被占用

        :return: The vip_address of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this CreateLoadBalancerOption.

        负载均衡器的虚拟IP。 1.传入vip_address时必须传入vip_subnet_cidr_id 2.不传入vip_address，自动分配虚拟IP 3.传入vip_address，需要保证该ip地址在子网中未被占用

        :param vip_address: The vip_address of this CreateLoadBalancerOption.
        :type: str
        """
        self._vip_address = vip_address

    @property
    def vip_subnet_cidr_id(self):
        """Gets the vip_subnet_cidr_id of this CreateLoadBalancerOption.

        负载均衡器所在的子网ID。 说明：vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :return: The vip_subnet_cidr_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        """Sets the vip_subnet_cidr_id of this CreateLoadBalancerOption.

        负载均衡器所在的子网ID。 说明：vpc_id , vip_subnet_cidr_id, ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def ipv6_vip_virsubnet_id(self):
        """Gets the ipv6_vip_virsubnet_id of this CreateLoadBalancerOption.

        双栈实例对应v6的网络id 。注：默认为空，只有开启IPv6时才会传入。  说明：vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :return: The ipv6_vip_virsubnet_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        """Sets the ipv6_vip_virsubnet_id of this CreateLoadBalancerOption.

        双栈实例对应v6的网络id 。注：默认为空，只有开启IPv6时才会传入。  说明：vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def provider(self):
        """Gets the provider of this CreateLoadBalancerOption.

        负载均衡器的生产者名称。只支持vlb。

        :return: The provider of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateLoadBalancerOption.

        负载均衡器的生产者名称。只支持vlb。

        :param provider: The provider of this CreateLoadBalancerOption.
        :type: str
        """
        self._provider = provider

    @property
    def l4_flavor_id(self):
        """Gets the l4_flavor_id of this CreateLoadBalancerOption.

        四层Flavor。

        :return: The l4_flavor_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        """Sets the l4_flavor_id of this CreateLoadBalancerOption.

        四层Flavor。

        :param l4_flavor_id: The l4_flavor_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateLoadBalancerOption.

        负载均衡器所在的项目ID。

        :return: The project_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateLoadBalancerOption.

        负载均衡器所在的项目ID。

        :param project_id: The project_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._project_id = project_id

    @property
    def guaranteed(self):
        """Gets the guaranteed of this CreateLoadBalancerOption.

        共享型：false 保障型：true，当前只支持true。

        :return: The guaranteed of this CreateLoadBalancerOption.
        :rtype: bool
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        """Sets the guaranteed of this CreateLoadBalancerOption.

        共享型：false 保障型：true，当前只支持true。

        :param guaranteed: The guaranteed of this CreateLoadBalancerOption.
        :type: bool
        """
        self._guaranteed = guaranteed

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateLoadBalancerOption.

        实例对应的vpc属性。 说明：vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :return: The vpc_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateLoadBalancerOption.

        实例对应的vpc属性。 说明：vpc_id，vip_subnet_cidr_id，ipv6_vip_virsubnet_id不能同时为空，且需要在同一个vpc下。

        :param vpc_id: The vpc_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def availability_zone_list(self):
        """Gets the availability_zone_list of this CreateLoadBalancerOption.

        可用区列表。默认指定所有可利用的AZ。 注： 可用AZ的查询方式可用通过调用nova接口查询 /v2/{project_id}/os-availability-zone

        :return: The availability_zone_list of this CreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._availability_zone_list

    @availability_zone_list.setter
    def availability_zone_list(self, availability_zone_list):
        """Sets the availability_zone_list of this CreateLoadBalancerOption.

        可用区列表。默认指定所有可利用的AZ。 注： 可用AZ的查询方式可用通过调用nova接口查询 /v2/{project_id}/os-availability-zone

        :param availability_zone_list: The availability_zone_list of this CreateLoadBalancerOption.
        :type: list[str]
        """
        self._availability_zone_list = availability_zone_list

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateLoadBalancerOption.

        企业项目ID。

        :return: The enterprise_project_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateLoadBalancerOption.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateLoadBalancerOption.

        负载均衡的标签列表。示例如下：\"tags\":[{\"key\":\"aaaa\",\"value\":\"mmmaaaaa\"}]

        :return: The tags of this CreateLoadBalancerOption.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateLoadBalancerOption.

        负载均衡的标签列表。示例如下：\"tags\":[{\"key\":\"aaaa\",\"value\":\"mmmaaaaa\"}]

        :param tags: The tags of this CreateLoadBalancerOption.
        :type: list[Tag]
        """
        self._tags = tags

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateLoadBalancerOption.

        负载均衡器的管理状态。说明：负载均衡器的管理状态。只支持设定为true。

        :return: The admin_state_up of this CreateLoadBalancerOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateLoadBalancerOption.

        负载均衡器的管理状态。说明：负载均衡器的管理状态。只支持设定为true。

        :param admin_state_up: The admin_state_up of this CreateLoadBalancerOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this CreateLoadBalancerOption.

        七层Flavor。 

        :return: The l7_flavor_id of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this CreateLoadBalancerOption.

        七层Flavor。 

        :param l7_flavor_id: The l7_flavor_id of this CreateLoadBalancerOption.
        :type: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def billing_info(self):
        """Gets the billing_info of this CreateLoadBalancerOption.

        预留资源账单信息。

        :return: The billing_info of this CreateLoadBalancerOption.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this CreateLoadBalancerOption.

        预留资源账单信息。

        :param billing_info: The billing_info of this CreateLoadBalancerOption.
        :type: str
        """
        self._billing_info = billing_info

    @property
    def ipv6_bandwidth(self):
        """Gets the ipv6_bandwidth of this CreateLoadBalancerOption.


        :return: The ipv6_bandwidth of this CreateLoadBalancerOption.
        :rtype: BandwidthRef
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        """Sets the ipv6_bandwidth of this CreateLoadBalancerOption.


        :param ipv6_bandwidth: The ipv6_bandwidth of this CreateLoadBalancerOption.
        :type: BandwidthRef
        """
        self._ipv6_bandwidth = ipv6_bandwidth

    @property
    def publicip_ids(self):
        """Gets the publicip_ids of this CreateLoadBalancerOption.

        公网EIP的ID，目前只支持一个

        :return: The publicip_ids of this CreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._publicip_ids

    @publicip_ids.setter
    def publicip_ids(self, publicip_ids):
        """Sets the publicip_ids of this CreateLoadBalancerOption.

        公网EIP的ID，目前只支持一个

        :param publicip_ids: The publicip_ids of this CreateLoadBalancerOption.
        :type: list[str]
        """
        self._publicip_ids = publicip_ids

    @property
    def publicip(self):
        """Gets the publicip of this CreateLoadBalancerOption.


        :return: The publicip of this CreateLoadBalancerOption.
        :rtype: CreateLoadBalancerPublicIpOption
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this CreateLoadBalancerOption.


        :param publicip: The publicip of this CreateLoadBalancerOption.
        :type: CreateLoadBalancerPublicIpOption
        """
        self._publicip = publicip

    @property
    def elb_virsubnet_ids(self):
        """Gets the elb_virsubnet_ids of this CreateLoadBalancerOption.

        下联面网络id列表 若该字段不指定，在loadbalancer所属的VPC中任意选一个网络id，优选双栈网络

        :return: The elb_virsubnet_ids of this CreateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        """Sets the elb_virsubnet_ids of this CreateLoadBalancerOption.

        下联面网络id列表 若该字段不指定，在loadbalancer所属的VPC中任意选一个网络id，优选双栈网络

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this CreateLoadBalancerOption.
        :type: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def ip_target_enable(self):
        """Gets the ip_target_enable of this CreateLoadBalancerOption.

        是否启用跨VPC后端转发

        :return: The ip_target_enable of this CreateLoadBalancerOption.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        """Sets the ip_target_enable of this CreateLoadBalancerOption.

        是否启用跨VPC后端转发

        :param ip_target_enable: The ip_target_enable of this CreateLoadBalancerOption.
        :type: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def deletion_protection_enable(self):
        """Gets the deletion_protection_enable of this CreateLoadBalancerOption.

        是否开启删除保护，默认不开启

        :return: The deletion_protection_enable of this CreateLoadBalancerOption.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        """Sets the deletion_protection_enable of this CreateLoadBalancerOption.

        是否开启删除保护，默认不开启

        :param deletion_protection_enable: The deletion_protection_enable of this CreateLoadBalancerOption.
        :type: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

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
        if not isinstance(other, CreateLoadBalancerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
