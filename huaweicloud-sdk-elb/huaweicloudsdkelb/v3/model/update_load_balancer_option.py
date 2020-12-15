# coding: utf-8

import pprint
import re

import six





class UpdateLoadBalancerOption:


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
        'admin_state_up': 'bool',
        'description': 'str',
        'ipv6_vip_virsubnet_id': 'str',
        'vip_subnet_cidr_id': 'str',
        'vip_address': 'str',
        'l4_flavor_id': 'str',
        'l7_flavor_id': 'str',
        'ipv6_bandwidth': 'BandwidthRef',
        'ip_target_enable': 'bool',
        'deletion_protection_enable': 'bool',
        'elb_virsubnet_ids': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'ipv6_vip_virsubnet_id': 'ipv6_vip_virsubnet_id',
        'vip_subnet_cidr_id': 'vip_subnet_cidr_id',
        'vip_address': 'vip_address',
        'l4_flavor_id': 'l4_flavor_id',
        'l7_flavor_id': 'l7_flavor_id',
        'ipv6_bandwidth': 'ipv6_bandwidth',
        'ip_target_enable': 'ip_target_enable',
        'deletion_protection_enable': 'deletion_protection_enable',
        'elb_virsubnet_ids': 'elb_virsubnet_ids'
    }

    def __init__(self, name=None, admin_state_up=None, description=None, ipv6_vip_virsubnet_id=None, vip_subnet_cidr_id=None, vip_address=None, l4_flavor_id=None, l7_flavor_id=None, ipv6_bandwidth=None, ip_target_enable=None, deletion_protection_enable=None, elb_virsubnet_ids=None):
        """UpdateLoadBalancerOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._admin_state_up = None
        self._description = None
        self._ipv6_vip_virsubnet_id = None
        self._vip_subnet_cidr_id = None
        self._vip_address = None
        self._l4_flavor_id = None
        self._l7_flavor_id = None
        self._ipv6_bandwidth = None
        self._ip_target_enable = None
        self._deletion_protection_enable = None
        self._elb_virsubnet_ids = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        if ipv6_vip_virsubnet_id is not None:
            self.ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id
        if vip_subnet_cidr_id is not None:
            self.vip_subnet_cidr_id = vip_subnet_cidr_id
        if vip_address is not None:
            self.vip_address = vip_address
        if l4_flavor_id is not None:
            self.l4_flavor_id = l4_flavor_id
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if ipv6_bandwidth is not None:
            self.ipv6_bandwidth = ipv6_bandwidth
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if deletion_protection_enable is not None:
            self.deletion_protection_enable = deletion_protection_enable
        if elb_virsubnet_ids is not None:
            self.elb_virsubnet_ids = elb_virsubnet_ids

    @property
    def name(self):
        """Gets the name of this UpdateLoadBalancerOption.

        负载均衡器名称。 

        :return: The name of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateLoadBalancerOption.

        负载均衡器名称。 

        :param name: The name of this UpdateLoadBalancerOption.
        :type: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateLoadBalancerOption.

        负载均衡器的管理状态。 说明：负载均衡器的管理状态。只支持设定为true。

        :return: The admin_state_up of this UpdateLoadBalancerOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateLoadBalancerOption.

        负载均衡器的管理状态。 说明：负载均衡器的管理状态。只支持设定为true。

        :param admin_state_up: The admin_state_up of this UpdateLoadBalancerOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this UpdateLoadBalancerOption.

        负载均衡器功能说明。

        :return: The description of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateLoadBalancerOption.

        负载均衡器功能说明。

        :param description: The description of this UpdateLoadBalancerOption.
        :type: str
        """
        self._description = description

    @property
    def ipv6_vip_virsubnet_id(self):
        """Gets the ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.

        双栈实例对应v6的网络id 。 注： 1.默认为空，只有开启IPv6时才会传入。 2.仅当guaranteed是true的场合，才支持更新。 3.解绑ipv6的情况下，输入null

        :return: The ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._ipv6_vip_virsubnet_id

    @ipv6_vip_virsubnet_id.setter
    def ipv6_vip_virsubnet_id(self, ipv6_vip_virsubnet_id):
        """Sets the ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.

        双栈实例对应v6的网络id 。 注： 1.默认为空，只有开启IPv6时才会传入。 2.仅当guaranteed是true的场合，才支持更新。 3.解绑ipv6的情况下，输入null

        :param ipv6_vip_virsubnet_id: The ipv6_vip_virsubnet_id of this UpdateLoadBalancerOption.
        :type: str
        """
        self._ipv6_vip_virsubnet_id = ipv6_vip_virsubnet_id

    @property
    def vip_subnet_cidr_id(self):
        """Gets the vip_subnet_cidr_id of this UpdateLoadBalancerOption.

        负载均衡器所在的子网ID。 注： 1.仅当guaranteed是true的场合，才支持更新。 2.解绑ipv4私网的情况下，输入null

        :return: The vip_subnet_cidr_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_subnet_cidr_id

    @vip_subnet_cidr_id.setter
    def vip_subnet_cidr_id(self, vip_subnet_cidr_id):
        """Sets the vip_subnet_cidr_id of this UpdateLoadBalancerOption.

        负载均衡器所在的子网ID。 注： 1.仅当guaranteed是true的场合，才支持更新。 2.解绑ipv4私网的情况下，输入null

        :param vip_subnet_cidr_id: The vip_subnet_cidr_id of this UpdateLoadBalancerOption.
        :type: str
        """
        self._vip_subnet_cidr_id = vip_subnet_cidr_id

    @property
    def vip_address(self):
        """Gets the vip_address of this UpdateLoadBalancerOption.

        负载均衡器的虚拟IP。 说明： 1.传入vip_address时必须传入vip_subnet_cidr_id 2.不传入vip_address，自动分配虚拟IP。 3.传入vip_address，需要保证该ip地址在子网中未被占用 注：仅当guaranteed是true的场合，才支持更新。

        :return: The vip_address of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this UpdateLoadBalancerOption.

        负载均衡器的虚拟IP。 说明： 1.传入vip_address时必须传入vip_subnet_cidr_id 2.不传入vip_address，自动分配虚拟IP。 3.传入vip_address，需要保证该ip地址在子网中未被占用 注：仅当guaranteed是true的场合，才支持更新。

        :param vip_address: The vip_address of this UpdateLoadBalancerOption.
        :type: str
        """
        self._vip_address = vip_address

    @property
    def l4_flavor_id(self):
        """Gets the l4_flavor_id of this UpdateLoadBalancerOption.

        四层Flavor。 注：1.仅当guaranteed是true的场合，才支持更新。 2.不允许非null变成null，null变成非null，只允许改大，不允许改小。

        :return: The l4_flavor_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._l4_flavor_id

    @l4_flavor_id.setter
    def l4_flavor_id(self, l4_flavor_id):
        """Sets the l4_flavor_id of this UpdateLoadBalancerOption.

        四层Flavor。 注：1.仅当guaranteed是true的场合，才支持更新。 2.不允许非null变成null，null变成非null，只允许改大，不允许改小。

        :param l4_flavor_id: The l4_flavor_id of this UpdateLoadBalancerOption.
        :type: str
        """
        self._l4_flavor_id = l4_flavor_id

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this UpdateLoadBalancerOption.

        七层Flavor。 注：1.仅当guaranteed是true的场合，才支持更新。 2.不允许非null变成null，null变成非null；只允许改大，不允许改小。

        :return: The l7_flavor_id of this UpdateLoadBalancerOption.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this UpdateLoadBalancerOption.

        七层Flavor。 注：1.仅当guaranteed是true的场合，才支持更新。 2.不允许非null变成null，null变成非null；只允许改大，不允许改小。

        :param l7_flavor_id: The l7_flavor_id of this UpdateLoadBalancerOption.
        :type: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def ipv6_bandwidth(self):
        """Gets the ipv6_bandwidth of this UpdateLoadBalancerOption.


        :return: The ipv6_bandwidth of this UpdateLoadBalancerOption.
        :rtype: BandwidthRef
        """
        return self._ipv6_bandwidth

    @ipv6_bandwidth.setter
    def ipv6_bandwidth(self, ipv6_bandwidth):
        """Sets the ipv6_bandwidth of this UpdateLoadBalancerOption.


        :param ipv6_bandwidth: The ipv6_bandwidth of this UpdateLoadBalancerOption.
        :type: BandwidthRef
        """
        self._ipv6_bandwidth = ipv6_bandwidth

    @property
    def ip_target_enable(self):
        """Gets the ip_target_enable of this UpdateLoadBalancerOption.

        是否启用跨VPC后端转发，值只允许为true

        :return: The ip_target_enable of this UpdateLoadBalancerOption.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        """Sets the ip_target_enable of this UpdateLoadBalancerOption.

        是否启用跨VPC后端转发，值只允许为true

        :param ip_target_enable: The ip_target_enable of this UpdateLoadBalancerOption.
        :type: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def deletion_protection_enable(self):
        """Gets the deletion_protection_enable of this UpdateLoadBalancerOption.

        是否开启删除保护

        :return: The deletion_protection_enable of this UpdateLoadBalancerOption.
        :rtype: bool
        """
        return self._deletion_protection_enable

    @deletion_protection_enable.setter
    def deletion_protection_enable(self, deletion_protection_enable):
        """Sets the deletion_protection_enable of this UpdateLoadBalancerOption.

        是否开启删除保护

        :param deletion_protection_enable: The deletion_protection_enable of this UpdateLoadBalancerOption.
        :type: bool
        """
        self._deletion_protection_enable = deletion_protection_enable

    @property
    def elb_virsubnet_ids(self):
        """Gets the elb_virsubnet_ids of this UpdateLoadBalancerOption.

        【描述】下联面网络ID列表，若该字段不指定，在loadbalancer所属的VPC中任意选一个网络id，优选双栈网络。 【约束】 1、所有ID同属一个VPC 2、不允许移除已被ELB使用的子网 3、不支持边缘云子网 4、负载均衡实例不处于ACTIVE状态时，不支持该字段更新 

        :return: The elb_virsubnet_ids of this UpdateLoadBalancerOption.
        :rtype: list[str]
        """
        return self._elb_virsubnet_ids

    @elb_virsubnet_ids.setter
    def elb_virsubnet_ids(self, elb_virsubnet_ids):
        """Sets the elb_virsubnet_ids of this UpdateLoadBalancerOption.

        【描述】下联面网络ID列表，若该字段不指定，在loadbalancer所属的VPC中任意选一个网络id，优选双栈网络。 【约束】 1、所有ID同属一个VPC 2、不允许移除已被ELB使用的子网 3、不支持边缘云子网 4、负载均衡实例不处于ACTIVE状态时，不支持该字段更新 

        :param elb_virsubnet_ids: The elb_virsubnet_ids of this UpdateLoadBalancerOption.
        :type: list[str]
        """
        self._elb_virsubnet_ids = elb_virsubnet_ids

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
        if not isinstance(other, UpdateLoadBalancerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
