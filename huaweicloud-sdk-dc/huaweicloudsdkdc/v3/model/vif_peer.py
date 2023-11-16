# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VifPeer:

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
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'address_family': 'str',
        'local_gateway_ip': 'str',
        'remote_gateway_ip': 'str',
        'route_mode': 'str',
        'bgp_asn': 'int',
        'bgp_md5': 'str',
        'remote_ep_group': 'list[str]',
        'service_ep_group': 'list[str]',
        'device_id': 'str',
        'bgp_route_limit': 'int',
        'bgp_status': 'str',
        'status': 'str',
        'vif_id': 'str',
        'receive_route_num': 'int'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'address_family': 'address_family',
        'local_gateway_ip': 'local_gateway_ip',
        'remote_gateway_ip': 'remote_gateway_ip',
        'route_mode': 'route_mode',
        'bgp_asn': 'bgp_asn',
        'bgp_md5': 'bgp_md5',
        'remote_ep_group': 'remote_ep_group',
        'service_ep_group': 'service_ep_group',
        'device_id': 'device_id',
        'bgp_route_limit': 'bgp_route_limit',
        'bgp_status': 'bgp_status',
        'status': 'status',
        'vif_id': 'vif_id',
        'receive_route_num': 'receive_route_num'
    }

    def __init__(self, id=None, tenant_id=None, name=None, description=None, address_family=None, local_gateway_ip=None, remote_gateway_ip=None, route_mode=None, bgp_asn=None, bgp_md5=None, remote_ep_group=None, service_ep_group=None, device_id=None, bgp_route_limit=None, bgp_status=None, status=None, vif_id=None, receive_route_num=None):
        """VifPeer

        The model defined in huaweicloud sdk

        :param id: 资源ID
        :type id: str
        :param tenant_id: 归属租户ID
        :type tenant_id: str
        :param name: VIF对等体名字
        :type name: str
        :param description: VIF对等体名字描述信息
        :type description: str
        :param address_family: 接口的地址簇类型，ipv4，ipv6
        :type address_family: str
        :param local_gateway_ip: VIF对等体云侧接口地址
        :type local_gateway_ip: str
        :param remote_gateway_ip: VIF对等体客户侧接口地址
        :type remote_gateway_ip: str
        :param route_mode: 路由模式：static/bgp
        :type route_mode: str
        :param bgp_asn: BGP邻居的AS号
        :type bgp_asn: int
        :param bgp_md5: BGP邻居的MD5密码
        :type bgp_md5: str
        :param remote_ep_group: 远端子网列表，记录租户侧的cidrs
        :type remote_ep_group: list[str]
        :param service_ep_group: 该字段用于公网专线接口,表示租户可以访问云上公网服务地址列表
        :type service_ep_group: list[str]
        :param device_id: 归属的设备ID
        :type device_id: str
        :param bgp_route_limit: BGP的路由配置规格
        :type bgp_route_limit: int
        :param bgp_status: 接口BGP协议状态,如果是静态路由接口则状态为 null
        :type bgp_status: str
        :param status: VIF对等体状态
        :type status: str
        :param vif_id: vif对等体对应的虚拟接口ID
        :type vif_id: str
        :param receive_route_num: 路由模式为bgp：receive_route_num值为接收搭配BGP的路由数目； 路由模式为static：该字段无意义，值为-1； 注：若早期接入华为云的部分用户无法获取该字段信息，如需要请联系客服迁移专线端口。
        :type receive_route_num: int
        """
        
        

        self._id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._address_family = None
        self._local_gateway_ip = None
        self._remote_gateway_ip = None
        self._route_mode = None
        self._bgp_asn = None
        self._bgp_md5 = None
        self._remote_ep_group = None
        self._service_ep_group = None
        self._device_id = None
        self._bgp_route_limit = None
        self._bgp_status = None
        self._status = None
        self._vif_id = None
        self._receive_route_num = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if address_family is not None:
            self.address_family = address_family
        if local_gateway_ip is not None:
            self.local_gateway_ip = local_gateway_ip
        if remote_gateway_ip is not None:
            self.remote_gateway_ip = remote_gateway_ip
        if route_mode is not None:
            self.route_mode = route_mode
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if bgp_md5 is not None:
            self.bgp_md5 = bgp_md5
        if remote_ep_group is not None:
            self.remote_ep_group = remote_ep_group
        if service_ep_group is not None:
            self.service_ep_group = service_ep_group
        if device_id is not None:
            self.device_id = device_id
        if bgp_route_limit is not None:
            self.bgp_route_limit = bgp_route_limit
        if bgp_status is not None:
            self.bgp_status = bgp_status
        if status is not None:
            self.status = status
        if vif_id is not None:
            self.vif_id = vif_id
        if receive_route_num is not None:
            self.receive_route_num = receive_route_num

    @property
    def id(self):
        """Gets the id of this VifPeer.

        资源ID

        :return: The id of this VifPeer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VifPeer.

        资源ID

        :param id: The id of this VifPeer.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this VifPeer.

        归属租户ID

        :return: The tenant_id of this VifPeer.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this VifPeer.

        归属租户ID

        :param tenant_id: The tenant_id of this VifPeer.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this VifPeer.

        VIF对等体名字

        :return: The name of this VifPeer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VifPeer.

        VIF对等体名字

        :param name: The name of this VifPeer.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this VifPeer.

        VIF对等体名字描述信息

        :return: The description of this VifPeer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VifPeer.

        VIF对等体名字描述信息

        :param description: The description of this VifPeer.
        :type description: str
        """
        self._description = description

    @property
    def address_family(self):
        """Gets the address_family of this VifPeer.

        接口的地址簇类型，ipv4，ipv6

        :return: The address_family of this VifPeer.
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this VifPeer.

        接口的地址簇类型，ipv4，ipv6

        :param address_family: The address_family of this VifPeer.
        :type address_family: str
        """
        self._address_family = address_family

    @property
    def local_gateway_ip(self):
        """Gets the local_gateway_ip of this VifPeer.

        VIF对等体云侧接口地址

        :return: The local_gateway_ip of this VifPeer.
        :rtype: str
        """
        return self._local_gateway_ip

    @local_gateway_ip.setter
    def local_gateway_ip(self, local_gateway_ip):
        """Sets the local_gateway_ip of this VifPeer.

        VIF对等体云侧接口地址

        :param local_gateway_ip: The local_gateway_ip of this VifPeer.
        :type local_gateway_ip: str
        """
        self._local_gateway_ip = local_gateway_ip

    @property
    def remote_gateway_ip(self):
        """Gets the remote_gateway_ip of this VifPeer.

        VIF对等体客户侧接口地址

        :return: The remote_gateway_ip of this VifPeer.
        :rtype: str
        """
        return self._remote_gateway_ip

    @remote_gateway_ip.setter
    def remote_gateway_ip(self, remote_gateway_ip):
        """Sets the remote_gateway_ip of this VifPeer.

        VIF对等体客户侧接口地址

        :param remote_gateway_ip: The remote_gateway_ip of this VifPeer.
        :type remote_gateway_ip: str
        """
        self._remote_gateway_ip = remote_gateway_ip

    @property
    def route_mode(self):
        """Gets the route_mode of this VifPeer.

        路由模式：static/bgp

        :return: The route_mode of this VifPeer.
        :rtype: str
        """
        return self._route_mode

    @route_mode.setter
    def route_mode(self, route_mode):
        """Sets the route_mode of this VifPeer.

        路由模式：static/bgp

        :param route_mode: The route_mode of this VifPeer.
        :type route_mode: str
        """
        self._route_mode = route_mode

    @property
    def bgp_asn(self):
        """Gets the bgp_asn of this VifPeer.

        BGP邻居的AS号

        :return: The bgp_asn of this VifPeer.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        """Sets the bgp_asn of this VifPeer.

        BGP邻居的AS号

        :param bgp_asn: The bgp_asn of this VifPeer.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def bgp_md5(self):
        """Gets the bgp_md5 of this VifPeer.

        BGP邻居的MD5密码

        :return: The bgp_md5 of this VifPeer.
        :rtype: str
        """
        return self._bgp_md5

    @bgp_md5.setter
    def bgp_md5(self, bgp_md5):
        """Sets the bgp_md5 of this VifPeer.

        BGP邻居的MD5密码

        :param bgp_md5: The bgp_md5 of this VifPeer.
        :type bgp_md5: str
        """
        self._bgp_md5 = bgp_md5

    @property
    def remote_ep_group(self):
        """Gets the remote_ep_group of this VifPeer.

        远端子网列表，记录租户侧的cidrs

        :return: The remote_ep_group of this VifPeer.
        :rtype: list[str]
        """
        return self._remote_ep_group

    @remote_ep_group.setter
    def remote_ep_group(self, remote_ep_group):
        """Sets the remote_ep_group of this VifPeer.

        远端子网列表，记录租户侧的cidrs

        :param remote_ep_group: The remote_ep_group of this VifPeer.
        :type remote_ep_group: list[str]
        """
        self._remote_ep_group = remote_ep_group

    @property
    def service_ep_group(self):
        """Gets the service_ep_group of this VifPeer.

        该字段用于公网专线接口,表示租户可以访问云上公网服务地址列表

        :return: The service_ep_group of this VifPeer.
        :rtype: list[str]
        """
        return self._service_ep_group

    @service_ep_group.setter
    def service_ep_group(self, service_ep_group):
        """Sets the service_ep_group of this VifPeer.

        该字段用于公网专线接口,表示租户可以访问云上公网服务地址列表

        :param service_ep_group: The service_ep_group of this VifPeer.
        :type service_ep_group: list[str]
        """
        self._service_ep_group = service_ep_group

    @property
    def device_id(self):
        """Gets the device_id of this VifPeer.

        归属的设备ID

        :return: The device_id of this VifPeer.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this VifPeer.

        归属的设备ID

        :param device_id: The device_id of this VifPeer.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def bgp_route_limit(self):
        """Gets the bgp_route_limit of this VifPeer.

        BGP的路由配置规格

        :return: The bgp_route_limit of this VifPeer.
        :rtype: int
        """
        return self._bgp_route_limit

    @bgp_route_limit.setter
    def bgp_route_limit(self, bgp_route_limit):
        """Sets the bgp_route_limit of this VifPeer.

        BGP的路由配置规格

        :param bgp_route_limit: The bgp_route_limit of this VifPeer.
        :type bgp_route_limit: int
        """
        self._bgp_route_limit = bgp_route_limit

    @property
    def bgp_status(self):
        """Gets the bgp_status of this VifPeer.

        接口BGP协议状态,如果是静态路由接口则状态为 null

        :return: The bgp_status of this VifPeer.
        :rtype: str
        """
        return self._bgp_status

    @bgp_status.setter
    def bgp_status(self, bgp_status):
        """Sets the bgp_status of this VifPeer.

        接口BGP协议状态,如果是静态路由接口则状态为 null

        :param bgp_status: The bgp_status of this VifPeer.
        :type bgp_status: str
        """
        self._bgp_status = bgp_status

    @property
    def status(self):
        """Gets the status of this VifPeer.

        VIF对等体状态

        :return: The status of this VifPeer.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VifPeer.

        VIF对等体状态

        :param status: The status of this VifPeer.
        :type status: str
        """
        self._status = status

    @property
    def vif_id(self):
        """Gets the vif_id of this VifPeer.

        vif对等体对应的虚拟接口ID

        :return: The vif_id of this VifPeer.
        :rtype: str
        """
        return self._vif_id

    @vif_id.setter
    def vif_id(self, vif_id):
        """Sets the vif_id of this VifPeer.

        vif对等体对应的虚拟接口ID

        :param vif_id: The vif_id of this VifPeer.
        :type vif_id: str
        """
        self._vif_id = vif_id

    @property
    def receive_route_num(self):
        """Gets the receive_route_num of this VifPeer.

        路由模式为bgp：receive_route_num值为接收搭配BGP的路由数目； 路由模式为static：该字段无意义，值为-1； 注：若早期接入华为云的部分用户无法获取该字段信息，如需要请联系客服迁移专线端口。

        :return: The receive_route_num of this VifPeer.
        :rtype: int
        """
        return self._receive_route_num

    @receive_route_num.setter
    def receive_route_num(self, receive_route_num):
        """Sets the receive_route_num of this VifPeer.

        路由模式为bgp：receive_route_num值为接收搭配BGP的路由数目； 路由模式为static：该字段无意义，值为-1； 注：若早期接入华为云的部分用户无法获取该字段信息，如需要请联系客服迁移专线端口。

        :param receive_route_num: The receive_route_num of this VifPeer.
        :type receive_route_num: int
        """
        self._receive_route_num = receive_route_num

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
        if not isinstance(other, VifPeer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
