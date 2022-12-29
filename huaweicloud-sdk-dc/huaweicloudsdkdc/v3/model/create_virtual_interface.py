# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVirtualInterface:

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
        'direct_connect_id': 'str',
        'type': 'str',
        'service_type': 'str',
        'vlan': 'int',
        'bandwidth': 'int',
        'local_gateway_v4_ip': 'str',
        'remote_gateway_v4_ip': 'str',
        'address_family': 'str',
        'local_gateway_v6_ip': 'str',
        'remote_gateway_v6_ip': 'str',
        'vgw_id': 'str',
        'route_mode': 'str',
        'bgp_asn': 'int',
        'bgp_md5': 'str',
        'remote_ep_group': 'list[str]',
        'service_ep_group': 'list[str]',
        'enable_bfd': 'bool',
        'enable_nqa': 'bool',
        'lag_id': 'str',
        'resource_tenant_id': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'direct_connect_id': 'direct_connect_id',
        'type': 'type',
        'service_type': 'service_type',
        'vlan': 'vlan',
        'bandwidth': 'bandwidth',
        'local_gateway_v4_ip': 'local_gateway_v4_ip',
        'remote_gateway_v4_ip': 'remote_gateway_v4_ip',
        'address_family': 'address_family',
        'local_gateway_v6_ip': 'local_gateway_v6_ip',
        'remote_gateway_v6_ip': 'remote_gateway_v6_ip',
        'vgw_id': 'vgw_id',
        'route_mode': 'route_mode',
        'bgp_asn': 'bgp_asn',
        'bgp_md5': 'bgp_md5',
        'remote_ep_group': 'remote_ep_group',
        'service_ep_group': 'service_ep_group',
        'enable_bfd': 'enable_bfd',
        'enable_nqa': 'enable_nqa',
        'lag_id': 'lag_id',
        'resource_tenant_id': 'resource_tenant_id',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, direct_connect_id=None, type=None, service_type=None, vlan=None, bandwidth=None, local_gateway_v4_ip=None, remote_gateway_v4_ip=None, address_family=None, local_gateway_v6_ip=None, remote_gateway_v6_ip=None, vgw_id=None, route_mode=None, bgp_asn=None, bgp_md5=None, remote_ep_group=None, service_ep_group=None, enable_bfd=None, enable_nqa=None, lag_id=None, resource_tenant_id=None, enterprise_project_id=None, tags=None):
        """CreateVirtualInterface

        The model defined in huaweicloud sdk

        :param name: 虚拟接口名字
        :type name: str
        :param description: 虚拟接口描述信息
        :type description: str
        :param direct_connect_id: 虚拟接口关联的物理专线ID
        :type direct_connect_id: str
        :param type: 虚拟接口的类型,private
        :type type: str
        :param service_type: 接入网关类型：VGW/GDGW/LGW
        :type service_type: str
        :param vlan: 对接客户侧vlan
        :type vlan: int
        :param bandwidth: 虚拟接口接入带宽
        :type bandwidth: int
        :param local_gateway_v4_ip: 云侧网关IPv4接口地址,如果address_family是IPv4，是必选参数
        :type local_gateway_v4_ip: str
        :param remote_gateway_v4_ip: 客户侧网关IPv4接口地址,如果address_family是IPv4，是必选参数
        :type remote_gateway_v4_ip: str
        :param address_family: 接口的地址簇类型，ipv4，ipv6
        :type address_family: str
        :param local_gateway_v6_ip: 云侧网关IPv6接口地址,如果address_family是IPv6，是必选参数
        :type local_gateway_v6_ip: str
        :param remote_gateway_v6_ip: 客户侧网关IPv6接口地址,如果address_family是IPv6，是必选参数
        :type remote_gateway_v6_ip: str
        :param vgw_id: 虚拟风关连接的虚拟网关的ID
        :type vgw_id: str
        :param route_mode: 路由模式：static/bgp
        :type route_mode: str
        :param bgp_asn: 客户侧BGP邻居的AS号
        :type bgp_asn: int
        :param bgp_md5: BGP邻居的MD5密码
        :type bgp_md5: str
        :param remote_ep_group: 远端子网列表，记录租户侧的cidrs
        :type remote_ep_group: list[str]
        :param service_ep_group: 访问公网服务的子网列表
        :type service_ep_group: list[str]
        :param enable_bfd: 是否使能bfd功能：true或false
        :type enable_bfd: bool
        :param enable_nqa: 是否使能nqa功能：true或false
        :type enable_nqa: bool
        :param lag_id: 虚拟接口关联的链路聚合组ID
        :type lag_id: str
        :param resource_tenant_id: 目标的租户的ID,用于跨租户创建虚拟接口场景
        :type resource_tenant_id: str
        :param enterprise_project_id: 实例所属企业项目ID
        :type enterprise_project_id: str
        :param tags: 标签信息
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        
        

        self._name = None
        self._description = None
        self._direct_connect_id = None
        self._type = None
        self._service_type = None
        self._vlan = None
        self._bandwidth = None
        self._local_gateway_v4_ip = None
        self._remote_gateway_v4_ip = None
        self._address_family = None
        self._local_gateway_v6_ip = None
        self._remote_gateway_v6_ip = None
        self._vgw_id = None
        self._route_mode = None
        self._bgp_asn = None
        self._bgp_md5 = None
        self._remote_ep_group = None
        self._service_ep_group = None
        self._enable_bfd = None
        self._enable_nqa = None
        self._lag_id = None
        self._resource_tenant_id = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if direct_connect_id is not None:
            self.direct_connect_id = direct_connect_id
        self.type = type
        if service_type is not None:
            self.service_type = service_type
        self.vlan = vlan
        self.bandwidth = bandwidth
        if local_gateway_v4_ip is not None:
            self.local_gateway_v4_ip = local_gateway_v4_ip
        if remote_gateway_v4_ip is not None:
            self.remote_gateway_v4_ip = remote_gateway_v4_ip
        if address_family is not None:
            self.address_family = address_family
        if local_gateway_v6_ip is not None:
            self.local_gateway_v6_ip = local_gateway_v6_ip
        if remote_gateway_v6_ip is not None:
            self.remote_gateway_v6_ip = remote_gateway_v6_ip
        self.vgw_id = vgw_id
        self.route_mode = route_mode
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if bgp_md5 is not None:
            self.bgp_md5 = bgp_md5
        self.remote_ep_group = remote_ep_group
        if service_ep_group is not None:
            self.service_ep_group = service_ep_group
        if enable_bfd is not None:
            self.enable_bfd = enable_bfd
        if enable_nqa is not None:
            self.enable_nqa = enable_nqa
        if lag_id is not None:
            self.lag_id = lag_id
        if resource_tenant_id is not None:
            self.resource_tenant_id = resource_tenant_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateVirtualInterface.

        虚拟接口名字

        :return: The name of this CreateVirtualInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVirtualInterface.

        虚拟接口名字

        :param name: The name of this CreateVirtualInterface.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateVirtualInterface.

        虚拟接口描述信息

        :return: The description of this CreateVirtualInterface.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateVirtualInterface.

        虚拟接口描述信息

        :param description: The description of this CreateVirtualInterface.
        :type description: str
        """
        self._description = description

    @property
    def direct_connect_id(self):
        """Gets the direct_connect_id of this CreateVirtualInterface.

        虚拟接口关联的物理专线ID

        :return: The direct_connect_id of this CreateVirtualInterface.
        :rtype: str
        """
        return self._direct_connect_id

    @direct_connect_id.setter
    def direct_connect_id(self, direct_connect_id):
        """Sets the direct_connect_id of this CreateVirtualInterface.

        虚拟接口关联的物理专线ID

        :param direct_connect_id: The direct_connect_id of this CreateVirtualInterface.
        :type direct_connect_id: str
        """
        self._direct_connect_id = direct_connect_id

    @property
    def type(self):
        """Gets the type of this CreateVirtualInterface.

        虚拟接口的类型,private

        :return: The type of this CreateVirtualInterface.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateVirtualInterface.

        虚拟接口的类型,private

        :param type: The type of this CreateVirtualInterface.
        :type type: str
        """
        self._type = type

    @property
    def service_type(self):
        """Gets the service_type of this CreateVirtualInterface.

        接入网关类型：VGW/GDGW/LGW

        :return: The service_type of this CreateVirtualInterface.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this CreateVirtualInterface.

        接入网关类型：VGW/GDGW/LGW

        :param service_type: The service_type of this CreateVirtualInterface.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def vlan(self):
        """Gets the vlan of this CreateVirtualInterface.

        对接客户侧vlan

        :return: The vlan of this CreateVirtualInterface.
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this CreateVirtualInterface.

        对接客户侧vlan

        :param vlan: The vlan of this CreateVirtualInterface.
        :type vlan: int
        """
        self._vlan = vlan

    @property
    def bandwidth(self):
        """Gets the bandwidth of this CreateVirtualInterface.

        虚拟接口接入带宽

        :return: The bandwidth of this CreateVirtualInterface.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this CreateVirtualInterface.

        虚拟接口接入带宽

        :param bandwidth: The bandwidth of this CreateVirtualInterface.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def local_gateway_v4_ip(self):
        """Gets the local_gateway_v4_ip of this CreateVirtualInterface.

        云侧网关IPv4接口地址,如果address_family是IPv4，是必选参数

        :return: The local_gateway_v4_ip of this CreateVirtualInterface.
        :rtype: str
        """
        return self._local_gateway_v4_ip

    @local_gateway_v4_ip.setter
    def local_gateway_v4_ip(self, local_gateway_v4_ip):
        """Sets the local_gateway_v4_ip of this CreateVirtualInterface.

        云侧网关IPv4接口地址,如果address_family是IPv4，是必选参数

        :param local_gateway_v4_ip: The local_gateway_v4_ip of this CreateVirtualInterface.
        :type local_gateway_v4_ip: str
        """
        self._local_gateway_v4_ip = local_gateway_v4_ip

    @property
    def remote_gateway_v4_ip(self):
        """Gets the remote_gateway_v4_ip of this CreateVirtualInterface.

        客户侧网关IPv4接口地址,如果address_family是IPv4，是必选参数

        :return: The remote_gateway_v4_ip of this CreateVirtualInterface.
        :rtype: str
        """
        return self._remote_gateway_v4_ip

    @remote_gateway_v4_ip.setter
    def remote_gateway_v4_ip(self, remote_gateway_v4_ip):
        """Sets the remote_gateway_v4_ip of this CreateVirtualInterface.

        客户侧网关IPv4接口地址,如果address_family是IPv4，是必选参数

        :param remote_gateway_v4_ip: The remote_gateway_v4_ip of this CreateVirtualInterface.
        :type remote_gateway_v4_ip: str
        """
        self._remote_gateway_v4_ip = remote_gateway_v4_ip

    @property
    def address_family(self):
        """Gets the address_family of this CreateVirtualInterface.

        接口的地址簇类型，ipv4，ipv6

        :return: The address_family of this CreateVirtualInterface.
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this CreateVirtualInterface.

        接口的地址簇类型，ipv4，ipv6

        :param address_family: The address_family of this CreateVirtualInterface.
        :type address_family: str
        """
        self._address_family = address_family

    @property
    def local_gateway_v6_ip(self):
        """Gets the local_gateway_v6_ip of this CreateVirtualInterface.

        云侧网关IPv6接口地址,如果address_family是IPv6，是必选参数

        :return: The local_gateway_v6_ip of this CreateVirtualInterface.
        :rtype: str
        """
        return self._local_gateway_v6_ip

    @local_gateway_v6_ip.setter
    def local_gateway_v6_ip(self, local_gateway_v6_ip):
        """Sets the local_gateway_v6_ip of this CreateVirtualInterface.

        云侧网关IPv6接口地址,如果address_family是IPv6，是必选参数

        :param local_gateway_v6_ip: The local_gateway_v6_ip of this CreateVirtualInterface.
        :type local_gateway_v6_ip: str
        """
        self._local_gateway_v6_ip = local_gateway_v6_ip

    @property
    def remote_gateway_v6_ip(self):
        """Gets the remote_gateway_v6_ip of this CreateVirtualInterface.

        客户侧网关IPv6接口地址,如果address_family是IPv6，是必选参数

        :return: The remote_gateway_v6_ip of this CreateVirtualInterface.
        :rtype: str
        """
        return self._remote_gateway_v6_ip

    @remote_gateway_v6_ip.setter
    def remote_gateway_v6_ip(self, remote_gateway_v6_ip):
        """Sets the remote_gateway_v6_ip of this CreateVirtualInterface.

        客户侧网关IPv6接口地址,如果address_family是IPv6，是必选参数

        :param remote_gateway_v6_ip: The remote_gateway_v6_ip of this CreateVirtualInterface.
        :type remote_gateway_v6_ip: str
        """
        self._remote_gateway_v6_ip = remote_gateway_v6_ip

    @property
    def vgw_id(self):
        """Gets the vgw_id of this CreateVirtualInterface.

        虚拟风关连接的虚拟网关的ID

        :return: The vgw_id of this CreateVirtualInterface.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        """Sets the vgw_id of this CreateVirtualInterface.

        虚拟风关连接的虚拟网关的ID

        :param vgw_id: The vgw_id of this CreateVirtualInterface.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def route_mode(self):
        """Gets the route_mode of this CreateVirtualInterface.

        路由模式：static/bgp

        :return: The route_mode of this CreateVirtualInterface.
        :rtype: str
        """
        return self._route_mode

    @route_mode.setter
    def route_mode(self, route_mode):
        """Sets the route_mode of this CreateVirtualInterface.

        路由模式：static/bgp

        :param route_mode: The route_mode of this CreateVirtualInterface.
        :type route_mode: str
        """
        self._route_mode = route_mode

    @property
    def bgp_asn(self):
        """Gets the bgp_asn of this CreateVirtualInterface.

        客户侧BGP邻居的AS号

        :return: The bgp_asn of this CreateVirtualInterface.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        """Sets the bgp_asn of this CreateVirtualInterface.

        客户侧BGP邻居的AS号

        :param bgp_asn: The bgp_asn of this CreateVirtualInterface.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def bgp_md5(self):
        """Gets the bgp_md5 of this CreateVirtualInterface.

        BGP邻居的MD5密码

        :return: The bgp_md5 of this CreateVirtualInterface.
        :rtype: str
        """
        return self._bgp_md5

    @bgp_md5.setter
    def bgp_md5(self, bgp_md5):
        """Sets the bgp_md5 of this CreateVirtualInterface.

        BGP邻居的MD5密码

        :param bgp_md5: The bgp_md5 of this CreateVirtualInterface.
        :type bgp_md5: str
        """
        self._bgp_md5 = bgp_md5

    @property
    def remote_ep_group(self):
        """Gets the remote_ep_group of this CreateVirtualInterface.

        远端子网列表，记录租户侧的cidrs

        :return: The remote_ep_group of this CreateVirtualInterface.
        :rtype: list[str]
        """
        return self._remote_ep_group

    @remote_ep_group.setter
    def remote_ep_group(self, remote_ep_group):
        """Sets the remote_ep_group of this CreateVirtualInterface.

        远端子网列表，记录租户侧的cidrs

        :param remote_ep_group: The remote_ep_group of this CreateVirtualInterface.
        :type remote_ep_group: list[str]
        """
        self._remote_ep_group = remote_ep_group

    @property
    def service_ep_group(self):
        """Gets the service_ep_group of this CreateVirtualInterface.

        访问公网服务的子网列表

        :return: The service_ep_group of this CreateVirtualInterface.
        :rtype: list[str]
        """
        return self._service_ep_group

    @service_ep_group.setter
    def service_ep_group(self, service_ep_group):
        """Sets the service_ep_group of this CreateVirtualInterface.

        访问公网服务的子网列表

        :param service_ep_group: The service_ep_group of this CreateVirtualInterface.
        :type service_ep_group: list[str]
        """
        self._service_ep_group = service_ep_group

    @property
    def enable_bfd(self):
        """Gets the enable_bfd of this CreateVirtualInterface.

        是否使能bfd功能：true或false

        :return: The enable_bfd of this CreateVirtualInterface.
        :rtype: bool
        """
        return self._enable_bfd

    @enable_bfd.setter
    def enable_bfd(self, enable_bfd):
        """Sets the enable_bfd of this CreateVirtualInterface.

        是否使能bfd功能：true或false

        :param enable_bfd: The enable_bfd of this CreateVirtualInterface.
        :type enable_bfd: bool
        """
        self._enable_bfd = enable_bfd

    @property
    def enable_nqa(self):
        """Gets the enable_nqa of this CreateVirtualInterface.

        是否使能nqa功能：true或false

        :return: The enable_nqa of this CreateVirtualInterface.
        :rtype: bool
        """
        return self._enable_nqa

    @enable_nqa.setter
    def enable_nqa(self, enable_nqa):
        """Sets the enable_nqa of this CreateVirtualInterface.

        是否使能nqa功能：true或false

        :param enable_nqa: The enable_nqa of this CreateVirtualInterface.
        :type enable_nqa: bool
        """
        self._enable_nqa = enable_nqa

    @property
    def lag_id(self):
        """Gets the lag_id of this CreateVirtualInterface.

        虚拟接口关联的链路聚合组ID

        :return: The lag_id of this CreateVirtualInterface.
        :rtype: str
        """
        return self._lag_id

    @lag_id.setter
    def lag_id(self, lag_id):
        """Sets the lag_id of this CreateVirtualInterface.

        虚拟接口关联的链路聚合组ID

        :param lag_id: The lag_id of this CreateVirtualInterface.
        :type lag_id: str
        """
        self._lag_id = lag_id

    @property
    def resource_tenant_id(self):
        """Gets the resource_tenant_id of this CreateVirtualInterface.

        目标的租户的ID,用于跨租户创建虚拟接口场景

        :return: The resource_tenant_id of this CreateVirtualInterface.
        :rtype: str
        """
        return self._resource_tenant_id

    @resource_tenant_id.setter
    def resource_tenant_id(self, resource_tenant_id):
        """Sets the resource_tenant_id of this CreateVirtualInterface.

        目标的租户的ID,用于跨租户创建虚拟接口场景

        :param resource_tenant_id: The resource_tenant_id of this CreateVirtualInterface.
        :type resource_tenant_id: str
        """
        self._resource_tenant_id = resource_tenant_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateVirtualInterface.

        实例所属企业项目ID

        :return: The enterprise_project_id of this CreateVirtualInterface.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateVirtualInterface.

        实例所属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateVirtualInterface.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CreateVirtualInterface.

        标签信息

        :return: The tags of this CreateVirtualInterface.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateVirtualInterface.

        标签信息

        :param tags: The tags of this CreateVirtualInterface.
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateVirtualInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
