# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublicipsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'offset': 'int',
        'limit': 'int',
        'fields': 'list[str]',
        'sort_key': 'str',
        'sort_dir': 'str',
        'id': 'list[str]',
        'ip_version': 'list[int]',
        'public_ip_address': 'list[str]',
        'public_ip_address_like': 'str',
        'public_ipv6_address': 'list[str]',
        'public_ipv6_address_like': 'str',
        'type': 'list[str]',
        'network_type': 'list[str]',
        'publicip_pool_name': 'list[str]',
        'status': 'list[str]',
        'alias_like': 'str',
        'alias': 'list[str]',
        'description': 'list[str]',
        'vnic_private_ip_address': 'list[str]',
        'vnic_private_ip_address_like': 'str',
        'vnic_device_id': 'list[str]',
        'vnic_device_owner': 'list[str]',
        'vnic_vpc_id': 'list[str]',
        'vnic_port_id': 'list[str]',
        'vnic_device_owner_prefixlike': 'str',
        'vnic_instance_type': 'list[str]',
        'vnic_instance_id': 'list[str]',
        'bandwidth_id': 'list[str]',
        'bandwidth_name': 'list[str]',
        'bandwidth_name_like': 'list[str]',
        'bandwidth_size': 'list[int]',
        'bandwidth_share_type': 'list[str]',
        'bandwidth_charge_mode': 'list[str]',
        'billing_info': 'list[str]',
        'billing_mode': 'str',
        'associate_instance_type': 'list[str]',
        'associate_instance_id': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'public_border_group': 'list[str]',
        'allow_share_bandwidth_type_any': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'offset': 'offset',
        'limit': 'limit',
        'fields': 'fields',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'ip_version': 'ip_version',
        'public_ip_address': 'public_ip_address',
        'public_ip_address_like': 'public_ip_address_like',
        'public_ipv6_address': 'public_ipv6_address',
        'public_ipv6_address_like': 'public_ipv6_address_like',
        'type': 'type',
        'network_type': 'network_type',
        'publicip_pool_name': 'publicip_pool_name',
        'status': 'status',
        'alias_like': 'alias_like',
        'alias': 'alias',
        'description': 'description',
        'vnic_private_ip_address': 'vnic.private_ip_address',
        'vnic_private_ip_address_like': 'vnic.private_ip_address_like',
        'vnic_device_id': 'vnic.device_id',
        'vnic_device_owner': 'vnic.device_owner',
        'vnic_vpc_id': 'vnic.vpc_id',
        'vnic_port_id': 'vnic.port_id',
        'vnic_device_owner_prefixlike': 'vnic.device_owner_prefixlike',
        'vnic_instance_type': 'vnic.instance_type',
        'vnic_instance_id': 'vnic.instance_id',
        'bandwidth_id': 'bandwidth.id',
        'bandwidth_name': 'bandwidth.name',
        'bandwidth_name_like': 'bandwidth.name_like',
        'bandwidth_size': 'bandwidth.size',
        'bandwidth_share_type': 'bandwidth.share_type',
        'bandwidth_charge_mode': 'bandwidth.charge_mode',
        'billing_info': 'billing_info',
        'billing_mode': 'billing_mode',
        'associate_instance_type': 'associate_instance_type',
        'associate_instance_id': 'associate_instance_id',
        'enterprise_project_id': 'enterprise_project_id',
        'public_border_group': 'public_border_group',
        'allow_share_bandwidth_type_any': 'allow_share_bandwidth_type_any'
    }

    def __init__(self, marker=None, offset=None, limit=None, fields=None, sort_key=None, sort_dir=None, id=None, ip_version=None, public_ip_address=None, public_ip_address_like=None, public_ipv6_address=None, public_ipv6_address_like=None, type=None, network_type=None, publicip_pool_name=None, status=None, alias_like=None, alias=None, description=None, vnic_private_ip_address=None, vnic_private_ip_address_like=None, vnic_device_id=None, vnic_device_owner=None, vnic_vpc_id=None, vnic_port_id=None, vnic_device_owner_prefixlike=None, vnic_instance_type=None, vnic_instance_id=None, bandwidth_id=None, bandwidth_name=None, bandwidth_name_like=None, bandwidth_size=None, bandwidth_share_type=None, bandwidth_charge_mode=None, billing_info=None, billing_mode=None, associate_instance_type=None, associate_instance_id=None, enterprise_project_id=None, public_border_group=None, allow_share_bandwidth_type_any=None):
        """ListPublicipsRequest

        The model defined in huaweicloud sdk

        :param marker: 分页查询起始的资源ID，为空时为查询第一页
        :type marker: str
        :param offset: 分页查询起始的资源序号
        :type offset: int
        :param limit: 每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定
        :type limit: int
        :param fields: 显示，形式为\&quot;fields&#x3D;id&amp;fields&#x3D;owner&amp;...\&quot;  支持字段：id/project_id/ip_version/type/public_ip_address/public_ipv6_address/network_type/status/description/created_at/updated_at/vnic/bandwidth/associate_instance_type/associate_instance_id/lock_status/billing_info/tags/enterprise_project_id/allow_share_bandwidth_types/public_border_group/alias/publicip_pool_name/publicip_pool_id
        :type fields: list[str]
        :param sort_key: 排序，形式为\&quot;sort_key&#x3D;id\&quot;  支持字段：id/public_ip_address/public_ipv6_address/ip_version/created_at/updated_at/public_border_group
        :type sort_key: str
        :param sort_dir: 排序方向  取值范围：asc、desc
        :type sort_dir: str
        :param id: 根据id过滤
        :type id: list[str]
        :param ip_version: 根据ip_version过滤  取值范围：4、6
        :type ip_version: list[int]
        :param public_ip_address: 根据public_ip_address过滤
        :type public_ip_address: list[str]
        :param public_ip_address_like: 根据public_ip_address过滤，模糊搜索
        :type public_ip_address_like: str
        :param public_ipv6_address: 根据public_ipv6_address过滤
        :type public_ipv6_address: list[str]
        :param public_ipv6_address_like: 根据public_ipv6_address过滤，模糊搜索
        :type public_ipv6_address_like: str
        :param type: 根据type过滤  取值范围：EIP、DUALSTACK、DUALSTACK_SUBNET  EIP: 弹性公网IP   DUALSTACK: 双栈IPV6   DUALSTACK_SUBNET: 双栈子网
        :type type: list[str]
        :param network_type: 根据network_type过滤  取值范围：5_telcom、5_union、5_bgp、5_sbgp、5_ipv6、5_graybgp
        :type network_type: list[str]
        :param publicip_pool_name: 根据publicip_pool_name过滤  取值范围：5_telcom、5_union、5_bgp、5_sbgp、5_ipv6、5_graybgp、专属池名称等
        :type publicip_pool_name: list[str]
        :param status: 根据status过滤  取值范围：FREEZED、DOWN、ACTIVE、ERROR
        :type status: list[str]
        :param alias_like: 根据alias模糊搜索
        :type alias_like: str
        :param alias: 根据alias过滤
        :type alias: list[str]
        :param description: 根据description过滤
        :type description: list[str]
        :param vnic_private_ip_address: 根据private_ip_address过滤
        :type vnic_private_ip_address: list[str]
        :param vnic_private_ip_address_like: 根据private_ip_address模糊搜索
        :type vnic_private_ip_address_like: str
        :param vnic_device_id: 根据device_id过滤
        :type vnic_device_id: list[str]
        :param vnic_device_owner: 根据device_owner过滤
        :type vnic_device_owner: list[str]
        :param vnic_vpc_id: 根据vpc_id过滤
        :type vnic_vpc_id: list[str]
        :param vnic_port_id: 根据port_id过滤
        :type vnic_port_id: list[str]
        :param vnic_device_owner_prefixlike: 根据device_owner_prefixlike模糊搜索
        :type vnic_device_owner_prefixlike: str
        :param vnic_instance_type: 根据instance_type过滤
        :type vnic_instance_type: list[str]
        :param vnic_instance_id: 根据instance_id过滤
        :type vnic_instance_id: list[str]
        :param bandwidth_id: 根据id过滤
        :type bandwidth_id: list[str]
        :param bandwidth_name: 根据name过滤
        :type bandwidth_name: list[str]
        :param bandwidth_name_like: 根据name模糊过滤
        :type bandwidth_name_like: list[str]
        :param bandwidth_size: 根据size过滤
        :type bandwidth_size: list[int]
        :param bandwidth_share_type: 根据share_type过滤
        :type bandwidth_share_type: list[str]
        :param bandwidth_charge_mode: 根据charge_mode过滤
        :type bandwidth_charge_mode: list[str]
        :param billing_info: 根据billing_info过滤
        :type billing_info: list[str]
        :param billing_mode: 根据订单模式过滤,   取值范围：YEARLY_MONTHLY、PAY_PER_USE
        :type billing_mode: str
        :param associate_instance_type: 根据associate_instance_type过滤  取值范围：PORT、NATGW、ELB、VPN、ELBV1
        :type associate_instance_type: list[str]
        :param associate_instance_id: 根据associate_instance_id过滤
        :type associate_instance_id: list[str]
        :param enterprise_project_id: 根据enterprise_project_id过滤
        :type enterprise_project_id: list[str]
        :param public_border_group: 根据public_border_group过滤
        :type public_border_group: list[str]
        :param allow_share_bandwidth_type_any: 共享带宽类型，根据任一共享带宽类型过滤EIP列表。 可以指定多个带宽类型，不同的带宽类型间用逗号分隔。
        :type allow_share_bandwidth_type_any: list[str]
        """
        
        

        self._marker = None
        self._offset = None
        self._limit = None
        self._fields = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._ip_version = None
        self._public_ip_address = None
        self._public_ip_address_like = None
        self._public_ipv6_address = None
        self._public_ipv6_address_like = None
        self._type = None
        self._network_type = None
        self._publicip_pool_name = None
        self._status = None
        self._alias_like = None
        self._alias = None
        self._description = None
        self._vnic_private_ip_address = None
        self._vnic_private_ip_address_like = None
        self._vnic_device_id = None
        self._vnic_device_owner = None
        self._vnic_vpc_id = None
        self._vnic_port_id = None
        self._vnic_device_owner_prefixlike = None
        self._vnic_instance_type = None
        self._vnic_instance_id = None
        self._bandwidth_id = None
        self._bandwidth_name = None
        self._bandwidth_name_like = None
        self._bandwidth_size = None
        self._bandwidth_share_type = None
        self._bandwidth_charge_mode = None
        self._billing_info = None
        self._billing_mode = None
        self._associate_instance_type = None
        self._associate_instance_id = None
        self._enterprise_project_id = None
        self._public_border_group = None
        self._allow_share_bandwidth_type_any = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if fields is not None:
            self.fields = fields
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if id is not None:
            self.id = id
        if ip_version is not None:
            self.ip_version = ip_version
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if public_ip_address_like is not None:
            self.public_ip_address_like = public_ip_address_like
        if public_ipv6_address is not None:
            self.public_ipv6_address = public_ipv6_address
        if public_ipv6_address_like is not None:
            self.public_ipv6_address_like = public_ipv6_address_like
        if type is not None:
            self.type = type
        if network_type is not None:
            self.network_type = network_type
        if publicip_pool_name is not None:
            self.publicip_pool_name = publicip_pool_name
        if status is not None:
            self.status = status
        if alias_like is not None:
            self.alias_like = alias_like
        if alias is not None:
            self.alias = alias
        if description is not None:
            self.description = description
        if vnic_private_ip_address is not None:
            self.vnic_private_ip_address = vnic_private_ip_address
        if vnic_private_ip_address_like is not None:
            self.vnic_private_ip_address_like = vnic_private_ip_address_like
        if vnic_device_id is not None:
            self.vnic_device_id = vnic_device_id
        if vnic_device_owner is not None:
            self.vnic_device_owner = vnic_device_owner
        if vnic_vpc_id is not None:
            self.vnic_vpc_id = vnic_vpc_id
        if vnic_port_id is not None:
            self.vnic_port_id = vnic_port_id
        if vnic_device_owner_prefixlike is not None:
            self.vnic_device_owner_prefixlike = vnic_device_owner_prefixlike
        if vnic_instance_type is not None:
            self.vnic_instance_type = vnic_instance_type
        if vnic_instance_id is not None:
            self.vnic_instance_id = vnic_instance_id
        if bandwidth_id is not None:
            self.bandwidth_id = bandwidth_id
        if bandwidth_name is not None:
            self.bandwidth_name = bandwidth_name
        if bandwidth_name_like is not None:
            self.bandwidth_name_like = bandwidth_name_like
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if bandwidth_share_type is not None:
            self.bandwidth_share_type = bandwidth_share_type
        if bandwidth_charge_mode is not None:
            self.bandwidth_charge_mode = bandwidth_charge_mode
        if billing_info is not None:
            self.billing_info = billing_info
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if associate_instance_type is not None:
            self.associate_instance_type = associate_instance_type
        if associate_instance_id is not None:
            self.associate_instance_id = associate_instance_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if allow_share_bandwidth_type_any is not None:
            self.allow_share_bandwidth_type_any = allow_share_bandwidth_type_any

    @property
    def marker(self):
        """Gets the marker of this ListPublicipsRequest.

        分页查询起始的资源ID，为空时为查询第一页

        :return: The marker of this ListPublicipsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPublicipsRequest.

        分页查询起始的资源ID，为空时为查询第一页

        :param marker: The marker of this ListPublicipsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListPublicipsRequest.

        分页查询起始的资源序号

        :return: The offset of this ListPublicipsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPublicipsRequest.

        分页查询起始的资源序号

        :param offset: The offset of this ListPublicipsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPublicipsRequest.

        每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定

        :return: The limit of this ListPublicipsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPublicipsRequest.

        每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定

        :param limit: The limit of this ListPublicipsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def fields(self):
        """Gets the fields of this ListPublicipsRequest.

        显示，形式为\"fields=id&fields=owner&...\"  支持字段：id/project_id/ip_version/type/public_ip_address/public_ipv6_address/network_type/status/description/created_at/updated_at/vnic/bandwidth/associate_instance_type/associate_instance_id/lock_status/billing_info/tags/enterprise_project_id/allow_share_bandwidth_types/public_border_group/alias/publicip_pool_name/publicip_pool_id

        :return: The fields of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListPublicipsRequest.

        显示，形式为\"fields=id&fields=owner&...\"  支持字段：id/project_id/ip_version/type/public_ip_address/public_ipv6_address/network_type/status/description/created_at/updated_at/vnic/bandwidth/associate_instance_type/associate_instance_id/lock_status/billing_info/tags/enterprise_project_id/allow_share_bandwidth_types/public_border_group/alias/publicip_pool_name/publicip_pool_id

        :param fields: The fields of this ListPublicipsRequest.
        :type fields: list[str]
        """
        self._fields = fields

    @property
    def sort_key(self):
        """Gets the sort_key of this ListPublicipsRequest.

        排序，形式为\"sort_key=id\"  支持字段：id/public_ip_address/public_ipv6_address/ip_version/created_at/updated_at/public_border_group

        :return: The sort_key of this ListPublicipsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListPublicipsRequest.

        排序，形式为\"sort_key=id\"  支持字段：id/public_ip_address/public_ipv6_address/ip_version/created_at/updated_at/public_border_group

        :param sort_key: The sort_key of this ListPublicipsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListPublicipsRequest.

        排序方向  取值范围：asc、desc

        :return: The sort_dir of this ListPublicipsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListPublicipsRequest.

        排序方向  取值范围：asc、desc

        :param sort_dir: The sort_dir of this ListPublicipsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        """Gets the id of this ListPublicipsRequest.

        根据id过滤

        :return: The id of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPublicipsRequest.

        根据id过滤

        :param id: The id of this ListPublicipsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def ip_version(self):
        """Gets the ip_version of this ListPublicipsRequest.

        根据ip_version过滤  取值范围：4、6

        :return: The ip_version of this ListPublicipsRequest.
        :rtype: list[int]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListPublicipsRequest.

        根据ip_version过滤  取值范围：4、6

        :param ip_version: The ip_version of this ListPublicipsRequest.
        :type ip_version: list[int]
        """
        self._ip_version = ip_version

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this ListPublicipsRequest.

        根据public_ip_address过滤

        :return: The public_ip_address of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this ListPublicipsRequest.

        根据public_ip_address过滤

        :param public_ip_address: The public_ip_address of this ListPublicipsRequest.
        :type public_ip_address: list[str]
        """
        self._public_ip_address = public_ip_address

    @property
    def public_ip_address_like(self):
        """Gets the public_ip_address_like of this ListPublicipsRequest.

        根据public_ip_address过滤，模糊搜索

        :return: The public_ip_address_like of this ListPublicipsRequest.
        :rtype: str
        """
        return self._public_ip_address_like

    @public_ip_address_like.setter
    def public_ip_address_like(self, public_ip_address_like):
        """Sets the public_ip_address_like of this ListPublicipsRequest.

        根据public_ip_address过滤，模糊搜索

        :param public_ip_address_like: The public_ip_address_like of this ListPublicipsRequest.
        :type public_ip_address_like: str
        """
        self._public_ip_address_like = public_ip_address_like

    @property
    def public_ipv6_address(self):
        """Gets the public_ipv6_address of this ListPublicipsRequest.

        根据public_ipv6_address过滤

        :return: The public_ipv6_address of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._public_ipv6_address

    @public_ipv6_address.setter
    def public_ipv6_address(self, public_ipv6_address):
        """Sets the public_ipv6_address of this ListPublicipsRequest.

        根据public_ipv6_address过滤

        :param public_ipv6_address: The public_ipv6_address of this ListPublicipsRequest.
        :type public_ipv6_address: list[str]
        """
        self._public_ipv6_address = public_ipv6_address

    @property
    def public_ipv6_address_like(self):
        """Gets the public_ipv6_address_like of this ListPublicipsRequest.

        根据public_ipv6_address过滤，模糊搜索

        :return: The public_ipv6_address_like of this ListPublicipsRequest.
        :rtype: str
        """
        return self._public_ipv6_address_like

    @public_ipv6_address_like.setter
    def public_ipv6_address_like(self, public_ipv6_address_like):
        """Sets the public_ipv6_address_like of this ListPublicipsRequest.

        根据public_ipv6_address过滤，模糊搜索

        :param public_ipv6_address_like: The public_ipv6_address_like of this ListPublicipsRequest.
        :type public_ipv6_address_like: str
        """
        self._public_ipv6_address_like = public_ipv6_address_like

    @property
    def type(self):
        """Gets the type of this ListPublicipsRequest.

        根据type过滤  取值范围：EIP、DUALSTACK、DUALSTACK_SUBNET  EIP: 弹性公网IP   DUALSTACK: 双栈IPV6   DUALSTACK_SUBNET: 双栈子网

        :return: The type of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListPublicipsRequest.

        根据type过滤  取值范围：EIP、DUALSTACK、DUALSTACK_SUBNET  EIP: 弹性公网IP   DUALSTACK: 双栈IPV6   DUALSTACK_SUBNET: 双栈子网

        :param type: The type of this ListPublicipsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def network_type(self):
        """Gets the network_type of this ListPublicipsRequest.

        根据network_type过滤  取值范围：5_telcom、5_union、5_bgp、5_sbgp、5_ipv6、5_graybgp

        :return: The network_type of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this ListPublicipsRequest.

        根据network_type过滤  取值范围：5_telcom、5_union、5_bgp、5_sbgp、5_ipv6、5_graybgp

        :param network_type: The network_type of this ListPublicipsRequest.
        :type network_type: list[str]
        """
        self._network_type = network_type

    @property
    def publicip_pool_name(self):
        """Gets the publicip_pool_name of this ListPublicipsRequest.

        根据publicip_pool_name过滤  取值范围：5_telcom、5_union、5_bgp、5_sbgp、5_ipv6、5_graybgp、专属池名称等

        :return: The publicip_pool_name of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._publicip_pool_name

    @publicip_pool_name.setter
    def publicip_pool_name(self, publicip_pool_name):
        """Sets the publicip_pool_name of this ListPublicipsRequest.

        根据publicip_pool_name过滤  取值范围：5_telcom、5_union、5_bgp、5_sbgp、5_ipv6、5_graybgp、专属池名称等

        :param publicip_pool_name: The publicip_pool_name of this ListPublicipsRequest.
        :type publicip_pool_name: list[str]
        """
        self._publicip_pool_name = publicip_pool_name

    @property
    def status(self):
        """Gets the status of this ListPublicipsRequest.

        根据status过滤  取值范围：FREEZED、DOWN、ACTIVE、ERROR

        :return: The status of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPublicipsRequest.

        根据status过滤  取值范围：FREEZED、DOWN、ACTIVE、ERROR

        :param status: The status of this ListPublicipsRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def alias_like(self):
        """Gets the alias_like of this ListPublicipsRequest.

        根据alias模糊搜索

        :return: The alias_like of this ListPublicipsRequest.
        :rtype: str
        """
        return self._alias_like

    @alias_like.setter
    def alias_like(self, alias_like):
        """Sets the alias_like of this ListPublicipsRequest.

        根据alias模糊搜索

        :param alias_like: The alias_like of this ListPublicipsRequest.
        :type alias_like: str
        """
        self._alias_like = alias_like

    @property
    def alias(self):
        """Gets the alias of this ListPublicipsRequest.

        根据alias过滤

        :return: The alias of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ListPublicipsRequest.

        根据alias过滤

        :param alias: The alias of this ListPublicipsRequest.
        :type alias: list[str]
        """
        self._alias = alias

    @property
    def description(self):
        """Gets the description of this ListPublicipsRequest.

        根据description过滤

        :return: The description of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListPublicipsRequest.

        根据description过滤

        :param description: The description of this ListPublicipsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def vnic_private_ip_address(self):
        """Gets the vnic_private_ip_address of this ListPublicipsRequest.

        根据private_ip_address过滤

        :return: The vnic_private_ip_address of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._vnic_private_ip_address

    @vnic_private_ip_address.setter
    def vnic_private_ip_address(self, vnic_private_ip_address):
        """Sets the vnic_private_ip_address of this ListPublicipsRequest.

        根据private_ip_address过滤

        :param vnic_private_ip_address: The vnic_private_ip_address of this ListPublicipsRequest.
        :type vnic_private_ip_address: list[str]
        """
        self._vnic_private_ip_address = vnic_private_ip_address

    @property
    def vnic_private_ip_address_like(self):
        """Gets the vnic_private_ip_address_like of this ListPublicipsRequest.

        根据private_ip_address模糊搜索

        :return: The vnic_private_ip_address_like of this ListPublicipsRequest.
        :rtype: str
        """
        return self._vnic_private_ip_address_like

    @vnic_private_ip_address_like.setter
    def vnic_private_ip_address_like(self, vnic_private_ip_address_like):
        """Sets the vnic_private_ip_address_like of this ListPublicipsRequest.

        根据private_ip_address模糊搜索

        :param vnic_private_ip_address_like: The vnic_private_ip_address_like of this ListPublicipsRequest.
        :type vnic_private_ip_address_like: str
        """
        self._vnic_private_ip_address_like = vnic_private_ip_address_like

    @property
    def vnic_device_id(self):
        """Gets the vnic_device_id of this ListPublicipsRequest.

        根据device_id过滤

        :return: The vnic_device_id of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._vnic_device_id

    @vnic_device_id.setter
    def vnic_device_id(self, vnic_device_id):
        """Sets the vnic_device_id of this ListPublicipsRequest.

        根据device_id过滤

        :param vnic_device_id: The vnic_device_id of this ListPublicipsRequest.
        :type vnic_device_id: list[str]
        """
        self._vnic_device_id = vnic_device_id

    @property
    def vnic_device_owner(self):
        """Gets the vnic_device_owner of this ListPublicipsRequest.

        根据device_owner过滤

        :return: The vnic_device_owner of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._vnic_device_owner

    @vnic_device_owner.setter
    def vnic_device_owner(self, vnic_device_owner):
        """Sets the vnic_device_owner of this ListPublicipsRequest.

        根据device_owner过滤

        :param vnic_device_owner: The vnic_device_owner of this ListPublicipsRequest.
        :type vnic_device_owner: list[str]
        """
        self._vnic_device_owner = vnic_device_owner

    @property
    def vnic_vpc_id(self):
        """Gets the vnic_vpc_id of this ListPublicipsRequest.

        根据vpc_id过滤

        :return: The vnic_vpc_id of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._vnic_vpc_id

    @vnic_vpc_id.setter
    def vnic_vpc_id(self, vnic_vpc_id):
        """Sets the vnic_vpc_id of this ListPublicipsRequest.

        根据vpc_id过滤

        :param vnic_vpc_id: The vnic_vpc_id of this ListPublicipsRequest.
        :type vnic_vpc_id: list[str]
        """
        self._vnic_vpc_id = vnic_vpc_id

    @property
    def vnic_port_id(self):
        """Gets the vnic_port_id of this ListPublicipsRequest.

        根据port_id过滤

        :return: The vnic_port_id of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._vnic_port_id

    @vnic_port_id.setter
    def vnic_port_id(self, vnic_port_id):
        """Sets the vnic_port_id of this ListPublicipsRequest.

        根据port_id过滤

        :param vnic_port_id: The vnic_port_id of this ListPublicipsRequest.
        :type vnic_port_id: list[str]
        """
        self._vnic_port_id = vnic_port_id

    @property
    def vnic_device_owner_prefixlike(self):
        """Gets the vnic_device_owner_prefixlike of this ListPublicipsRequest.

        根据device_owner_prefixlike模糊搜索

        :return: The vnic_device_owner_prefixlike of this ListPublicipsRequest.
        :rtype: str
        """
        return self._vnic_device_owner_prefixlike

    @vnic_device_owner_prefixlike.setter
    def vnic_device_owner_prefixlike(self, vnic_device_owner_prefixlike):
        """Sets the vnic_device_owner_prefixlike of this ListPublicipsRequest.

        根据device_owner_prefixlike模糊搜索

        :param vnic_device_owner_prefixlike: The vnic_device_owner_prefixlike of this ListPublicipsRequest.
        :type vnic_device_owner_prefixlike: str
        """
        self._vnic_device_owner_prefixlike = vnic_device_owner_prefixlike

    @property
    def vnic_instance_type(self):
        """Gets the vnic_instance_type of this ListPublicipsRequest.

        根据instance_type过滤

        :return: The vnic_instance_type of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._vnic_instance_type

    @vnic_instance_type.setter
    def vnic_instance_type(self, vnic_instance_type):
        """Sets the vnic_instance_type of this ListPublicipsRequest.

        根据instance_type过滤

        :param vnic_instance_type: The vnic_instance_type of this ListPublicipsRequest.
        :type vnic_instance_type: list[str]
        """
        self._vnic_instance_type = vnic_instance_type

    @property
    def vnic_instance_id(self):
        """Gets the vnic_instance_id of this ListPublicipsRequest.

        根据instance_id过滤

        :return: The vnic_instance_id of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._vnic_instance_id

    @vnic_instance_id.setter
    def vnic_instance_id(self, vnic_instance_id):
        """Sets the vnic_instance_id of this ListPublicipsRequest.

        根据instance_id过滤

        :param vnic_instance_id: The vnic_instance_id of this ListPublicipsRequest.
        :type vnic_instance_id: list[str]
        """
        self._vnic_instance_id = vnic_instance_id

    @property
    def bandwidth_id(self):
        """Gets the bandwidth_id of this ListPublicipsRequest.

        根据id过滤

        :return: The bandwidth_id of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        """Sets the bandwidth_id of this ListPublicipsRequest.

        根据id过滤

        :param bandwidth_id: The bandwidth_id of this ListPublicipsRequest.
        :type bandwidth_id: list[str]
        """
        self._bandwidth_id = bandwidth_id

    @property
    def bandwidth_name(self):
        """Gets the bandwidth_name of this ListPublicipsRequest.

        根据name过滤

        :return: The bandwidth_name of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._bandwidth_name

    @bandwidth_name.setter
    def bandwidth_name(self, bandwidth_name):
        """Sets the bandwidth_name of this ListPublicipsRequest.

        根据name过滤

        :param bandwidth_name: The bandwidth_name of this ListPublicipsRequest.
        :type bandwidth_name: list[str]
        """
        self._bandwidth_name = bandwidth_name

    @property
    def bandwidth_name_like(self):
        """Gets the bandwidth_name_like of this ListPublicipsRequest.

        根据name模糊过滤

        :return: The bandwidth_name_like of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._bandwidth_name_like

    @bandwidth_name_like.setter
    def bandwidth_name_like(self, bandwidth_name_like):
        """Sets the bandwidth_name_like of this ListPublicipsRequest.

        根据name模糊过滤

        :param bandwidth_name_like: The bandwidth_name_like of this ListPublicipsRequest.
        :type bandwidth_name_like: list[str]
        """
        self._bandwidth_name_like = bandwidth_name_like

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this ListPublicipsRequest.

        根据size过滤

        :return: The bandwidth_size of this ListPublicipsRequest.
        :rtype: list[int]
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this ListPublicipsRequest.

        根据size过滤

        :param bandwidth_size: The bandwidth_size of this ListPublicipsRequest.
        :type bandwidth_size: list[int]
        """
        self._bandwidth_size = bandwidth_size

    @property
    def bandwidth_share_type(self):
        """Gets the bandwidth_share_type of this ListPublicipsRequest.

        根据share_type过滤

        :return: The bandwidth_share_type of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._bandwidth_share_type

    @bandwidth_share_type.setter
    def bandwidth_share_type(self, bandwidth_share_type):
        """Sets the bandwidth_share_type of this ListPublicipsRequest.

        根据share_type过滤

        :param bandwidth_share_type: The bandwidth_share_type of this ListPublicipsRequest.
        :type bandwidth_share_type: list[str]
        """
        self._bandwidth_share_type = bandwidth_share_type

    @property
    def bandwidth_charge_mode(self):
        """Gets the bandwidth_charge_mode of this ListPublicipsRequest.

        根据charge_mode过滤

        :return: The bandwidth_charge_mode of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._bandwidth_charge_mode

    @bandwidth_charge_mode.setter
    def bandwidth_charge_mode(self, bandwidth_charge_mode):
        """Sets the bandwidth_charge_mode of this ListPublicipsRequest.

        根据charge_mode过滤

        :param bandwidth_charge_mode: The bandwidth_charge_mode of this ListPublicipsRequest.
        :type bandwidth_charge_mode: list[str]
        """
        self._bandwidth_charge_mode = bandwidth_charge_mode

    @property
    def billing_info(self):
        """Gets the billing_info of this ListPublicipsRequest.

        根据billing_info过滤

        :return: The billing_info of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this ListPublicipsRequest.

        根据billing_info过滤

        :param billing_info: The billing_info of this ListPublicipsRequest.
        :type billing_info: list[str]
        """
        self._billing_info = billing_info

    @property
    def billing_mode(self):
        """Gets the billing_mode of this ListPublicipsRequest.

        根据订单模式过滤,   取值范围：YEARLY_MONTHLY、PAY_PER_USE

        :return: The billing_mode of this ListPublicipsRequest.
        :rtype: str
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this ListPublicipsRequest.

        根据订单模式过滤,   取值范围：YEARLY_MONTHLY、PAY_PER_USE

        :param billing_mode: The billing_mode of this ListPublicipsRequest.
        :type billing_mode: str
        """
        self._billing_mode = billing_mode

    @property
    def associate_instance_type(self):
        """Gets the associate_instance_type of this ListPublicipsRequest.

        根据associate_instance_type过滤  取值范围：PORT、NATGW、ELB、VPN、ELBV1

        :return: The associate_instance_type of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_type

    @associate_instance_type.setter
    def associate_instance_type(self, associate_instance_type):
        """Sets the associate_instance_type of this ListPublicipsRequest.

        根据associate_instance_type过滤  取值范围：PORT、NATGW、ELB、VPN、ELBV1

        :param associate_instance_type: The associate_instance_type of this ListPublicipsRequest.
        :type associate_instance_type: list[str]
        """
        self._associate_instance_type = associate_instance_type

    @property
    def associate_instance_id(self):
        """Gets the associate_instance_id of this ListPublicipsRequest.

        根据associate_instance_id过滤

        :return: The associate_instance_id of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._associate_instance_id

    @associate_instance_id.setter
    def associate_instance_id(self, associate_instance_id):
        """Sets the associate_instance_id of this ListPublicipsRequest.

        根据associate_instance_id过滤

        :param associate_instance_id: The associate_instance_id of this ListPublicipsRequest.
        :type associate_instance_id: list[str]
        """
        self._associate_instance_id = associate_instance_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPublicipsRequest.

        根据enterprise_project_id过滤

        :return: The enterprise_project_id of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPublicipsRequest.

        根据enterprise_project_id过滤

        :param enterprise_project_id: The enterprise_project_id of this ListPublicipsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def public_border_group(self):
        """Gets the public_border_group of this ListPublicipsRequest.

        根据public_border_group过滤

        :return: The public_border_group of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this ListPublicipsRequest.

        根据public_border_group过滤

        :param public_border_group: The public_border_group of this ListPublicipsRequest.
        :type public_border_group: list[str]
        """
        self._public_border_group = public_border_group

    @property
    def allow_share_bandwidth_type_any(self):
        """Gets the allow_share_bandwidth_type_any of this ListPublicipsRequest.

        共享带宽类型，根据任一共享带宽类型过滤EIP列表。 可以指定多个带宽类型，不同的带宽类型间用逗号分隔。

        :return: The allow_share_bandwidth_type_any of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._allow_share_bandwidth_type_any

    @allow_share_bandwidth_type_any.setter
    def allow_share_bandwidth_type_any(self, allow_share_bandwidth_type_any):
        """Sets the allow_share_bandwidth_type_any of this ListPublicipsRequest.

        共享带宽类型，根据任一共享带宽类型过滤EIP列表。 可以指定多个带宽类型，不同的带宽类型间用逗号分隔。

        :param allow_share_bandwidth_type_any: The allow_share_bandwidth_type_any of this ListPublicipsRequest.
        :type allow_share_bandwidth_type_any: list[str]
        """
        self._allow_share_bandwidth_type_any = allow_share_bandwidth_type_any

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
        if not isinstance(other, ListPublicipsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
