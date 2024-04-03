# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectGeipBindingsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fields': 'str',
        'geip_id': 'str',
        'geip_ip_address': 'str',
        'public_border_group': 'str',
        'instance_type': 'str',
        'instance_id': 'str',
        'instance_vpc_id': 'str',
        'gcbandwidth_id': 'str',
        'gcbandwidth_admin_status': 'str',
        'gcbandwidth_size': 'int',
        'gcbandwidth_sla_level': 'str',
        'gcbandwidth_dscp': 'int',
        'vnic_private_ip_address': 'str',
        'vnic_vpc_id': 'str',
        'vnic_port_id': 'str',
        'vnic_device_id': 'str',
        'vnic_device_owner': 'str',
        'vnic_device_owner_prefixlike': 'str',
        'vnic_instance_type': 'str',
        'vnic_instance_id': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'fields': 'fields',
        'geip_id': 'geip_id',
        'geip_ip_address': 'geip_ip_address',
        'public_border_group': 'public_border_group',
        'instance_type': 'instance_type',
        'instance_id': 'instance_id',
        'instance_vpc_id': 'instance_vpc_id',
        'gcbandwidth_id': 'gcbandwidth.id',
        'gcbandwidth_admin_status': 'gcbandwidth.admin_status',
        'gcbandwidth_size': 'gcbandwidth.size',
        'gcbandwidth_sla_level': 'gcbandwidth.sla_level',
        'gcbandwidth_dscp': 'gcbandwidth.dscp',
        'vnic_private_ip_address': 'vnic.private_ip_address',
        'vnic_vpc_id': 'vnic.vpc_id',
        'vnic_port_id': 'vnic.port_id',
        'vnic_device_id': 'vnic.device_id',
        'vnic_device_owner': 'vnic.device_owner',
        'vnic_device_owner_prefixlike': 'vnic.device_owner_prefixlike',
        'vnic_instance_type': 'vnic.instance_type',
        'vnic_instance_id': 'vnic.instance_id',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker'
    }

    def __init__(self, fields=None, geip_id=None, geip_ip_address=None, public_border_group=None, instance_type=None, instance_id=None, instance_vpc_id=None, gcbandwidth_id=None, gcbandwidth_admin_status=None, gcbandwidth_size=None, gcbandwidth_sla_level=None, gcbandwidth_dscp=None, vnic_private_ip_address=None, vnic_vpc_id=None, vnic_port_id=None, vnic_device_id=None, vnic_device_owner=None, vnic_device_owner_prefixlike=None, vnic_instance_type=None, vnic_instance_id=None, sort_key=None, sort_dir=None, limit=None, offset=None, marker=None):
        """ListProjectGeipBindingsRequest

        The model defined in huaweicloud sdk

        :param fields: 形式为\\\&quot;fields&#x3D;geip_id&amp;fields&#x3D;geip_ip_address&amp;...\\\&quot;，支持字段：geip_id/geip_ip_address/instance_type/instance_id/vnic/vn_list/public_border_group/gcbandwidth/version/created_at/updated_at/instance_vpc_id
        :type fields: str
        :param geip_id: GEIP的uuid
        :type geip_id: str
        :param geip_ip_address: GEIP的ip地址
        :type geip_ip_address: str
        :param public_border_group: GEIP所处的出口位置
        :type public_border_group: str
        :param instance_type: 绑定的实例类型
        :type instance_type: str
        :param instance_id: 绑定的实例id
        :type instance_id: str
        :param instance_vpc_id: 绑定的实例vpcid
        :type instance_vpc_id: str
        :param gcbandwidth_id: 骨干带宽的uuid
        :type gcbandwidth_id: str
        :param gcbandwidth_admin_status: 骨干带宽的状态
        :type gcbandwidth_admin_status: str
        :param gcbandwidth_size: 骨干带宽的大小
        :type gcbandwidth_size: int
        :param gcbandwidth_sla_level: 描述网络等级，从高到低分为铂金、金、银、铜
        :type gcbandwidth_sla_level: str
        :param gcbandwidth_dscp: 线路质量金银铜对应的DSCP值
        :type gcbandwidth_dscp: int
        :param vnic_private_ip_address: 绑定实例的ip地址
        :type vnic_private_ip_address: str
        :param vnic_vpc_id: 绑定实例所在的vpcid
        :type vnic_vpc_id: str
        :param vnic_port_id: 绑定实例port的uuid
        :type vnic_port_id: str
        :param vnic_device_id: 绑定实例port对应的实例id
        :type vnic_device_id: str
        :param vnic_device_owner: 绑定实例port对应的实例所有者
        :type vnic_device_owner: str
        :param vnic_device_owner_prefixlike: 绑定实例port对应的实例所有者的前缀
        :type vnic_device_owner_prefixlike: str
        :param vnic_instance_type: 绑定实例port对应的实例类型
        :type vnic_instance_type: str
        :param vnic_instance_id: 绑定实例port对应的实例id
        :type vnic_instance_id: str
        :param sort_key: 排序，形式为\&quot;sort_key&#x3D;geip_id&amp;sort_dir&#x3D;asc\&quot;  支持字段：geip_id/version/public_border_group/ geip_ip_address/created_at/updated_at
        :type sort_key: str
        :param sort_dir: 排序方向  取值范围：asc、desc
        :type sort_dir: str
        :param limit: 每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定
        :type limit: int
        :param offset: 分页起始点
        :type offset: int
        :param marker: 分页起始点
        :type marker: str
        """
        
        

        self._fields = None
        self._geip_id = None
        self._geip_ip_address = None
        self._public_border_group = None
        self._instance_type = None
        self._instance_id = None
        self._instance_vpc_id = None
        self._gcbandwidth_id = None
        self._gcbandwidth_admin_status = None
        self._gcbandwidth_size = None
        self._gcbandwidth_sla_level = None
        self._gcbandwidth_dscp = None
        self._vnic_private_ip_address = None
        self._vnic_vpc_id = None
        self._vnic_port_id = None
        self._vnic_device_id = None
        self._vnic_device_owner = None
        self._vnic_device_owner_prefixlike = None
        self._vnic_instance_type = None
        self._vnic_instance_id = None
        self._sort_key = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self._marker = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if geip_id is not None:
            self.geip_id = geip_id
        if geip_ip_address is not None:
            self.geip_ip_address = geip_ip_address
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if instance_type is not None:
            self.instance_type = instance_type
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_vpc_id is not None:
            self.instance_vpc_id = instance_vpc_id
        if gcbandwidth_id is not None:
            self.gcbandwidth_id = gcbandwidth_id
        if gcbandwidth_admin_status is not None:
            self.gcbandwidth_admin_status = gcbandwidth_admin_status
        if gcbandwidth_size is not None:
            self.gcbandwidth_size = gcbandwidth_size
        if gcbandwidth_sla_level is not None:
            self.gcbandwidth_sla_level = gcbandwidth_sla_level
        if gcbandwidth_dscp is not None:
            self.gcbandwidth_dscp = gcbandwidth_dscp
        if vnic_private_ip_address is not None:
            self.vnic_private_ip_address = vnic_private_ip_address
        if vnic_vpc_id is not None:
            self.vnic_vpc_id = vnic_vpc_id
        if vnic_port_id is not None:
            self.vnic_port_id = vnic_port_id
        if vnic_device_id is not None:
            self.vnic_device_id = vnic_device_id
        if vnic_device_owner is not None:
            self.vnic_device_owner = vnic_device_owner
        if vnic_device_owner_prefixlike is not None:
            self.vnic_device_owner_prefixlike = vnic_device_owner_prefixlike
        if vnic_instance_type is not None:
            self.vnic_instance_type = vnic_instance_type
        if vnic_instance_id is not None:
            self.vnic_instance_id = vnic_instance_id
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if marker is not None:
            self.marker = marker

    @property
    def fields(self):
        """Gets the fields of this ListProjectGeipBindingsRequest.

        形式为\\\"fields=geip_id&fields=geip_ip_address&...\\\"，支持字段：geip_id/geip_ip_address/instance_type/instance_id/vnic/vn_list/public_border_group/gcbandwidth/version/created_at/updated_at/instance_vpc_id

        :return: The fields of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ListProjectGeipBindingsRequest.

        形式为\\\"fields=geip_id&fields=geip_ip_address&...\\\"，支持字段：geip_id/geip_ip_address/instance_type/instance_id/vnic/vn_list/public_border_group/gcbandwidth/version/created_at/updated_at/instance_vpc_id

        :param fields: The fields of this ListProjectGeipBindingsRequest.
        :type fields: str
        """
        self._fields = fields

    @property
    def geip_id(self):
        """Gets the geip_id of this ListProjectGeipBindingsRequest.

        GEIP的uuid

        :return: The geip_id of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._geip_id

    @geip_id.setter
    def geip_id(self, geip_id):
        """Sets the geip_id of this ListProjectGeipBindingsRequest.

        GEIP的uuid

        :param geip_id: The geip_id of this ListProjectGeipBindingsRequest.
        :type geip_id: str
        """
        self._geip_id = geip_id

    @property
    def geip_ip_address(self):
        """Gets the geip_ip_address of this ListProjectGeipBindingsRequest.

        GEIP的ip地址

        :return: The geip_ip_address of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._geip_ip_address

    @geip_ip_address.setter
    def geip_ip_address(self, geip_ip_address):
        """Sets the geip_ip_address of this ListProjectGeipBindingsRequest.

        GEIP的ip地址

        :param geip_ip_address: The geip_ip_address of this ListProjectGeipBindingsRequest.
        :type geip_ip_address: str
        """
        self._geip_ip_address = geip_ip_address

    @property
    def public_border_group(self):
        """Gets the public_border_group of this ListProjectGeipBindingsRequest.

        GEIP所处的出口位置

        :return: The public_border_group of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this ListProjectGeipBindingsRequest.

        GEIP所处的出口位置

        :param public_border_group: The public_border_group of this ListProjectGeipBindingsRequest.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def instance_type(self):
        """Gets the instance_type of this ListProjectGeipBindingsRequest.

        绑定的实例类型

        :return: The instance_type of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this ListProjectGeipBindingsRequest.

        绑定的实例类型

        :param instance_type: The instance_type of this ListProjectGeipBindingsRequest.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_id(self):
        """Gets the instance_id of this ListProjectGeipBindingsRequest.

        绑定的实例id

        :return: The instance_id of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListProjectGeipBindingsRequest.

        绑定的实例id

        :param instance_id: The instance_id of this ListProjectGeipBindingsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_vpc_id(self):
        """Gets the instance_vpc_id of this ListProjectGeipBindingsRequest.

        绑定的实例vpcid

        :return: The instance_vpc_id of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._instance_vpc_id

    @instance_vpc_id.setter
    def instance_vpc_id(self, instance_vpc_id):
        """Sets the instance_vpc_id of this ListProjectGeipBindingsRequest.

        绑定的实例vpcid

        :param instance_vpc_id: The instance_vpc_id of this ListProjectGeipBindingsRequest.
        :type instance_vpc_id: str
        """
        self._instance_vpc_id = instance_vpc_id

    @property
    def gcbandwidth_id(self):
        """Gets the gcbandwidth_id of this ListProjectGeipBindingsRequest.

        骨干带宽的uuid

        :return: The gcbandwidth_id of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._gcbandwidth_id

    @gcbandwidth_id.setter
    def gcbandwidth_id(self, gcbandwidth_id):
        """Sets the gcbandwidth_id of this ListProjectGeipBindingsRequest.

        骨干带宽的uuid

        :param gcbandwidth_id: The gcbandwidth_id of this ListProjectGeipBindingsRequest.
        :type gcbandwidth_id: str
        """
        self._gcbandwidth_id = gcbandwidth_id

    @property
    def gcbandwidth_admin_status(self):
        """Gets the gcbandwidth_admin_status of this ListProjectGeipBindingsRequest.

        骨干带宽的状态

        :return: The gcbandwidth_admin_status of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._gcbandwidth_admin_status

    @gcbandwidth_admin_status.setter
    def gcbandwidth_admin_status(self, gcbandwidth_admin_status):
        """Sets the gcbandwidth_admin_status of this ListProjectGeipBindingsRequest.

        骨干带宽的状态

        :param gcbandwidth_admin_status: The gcbandwidth_admin_status of this ListProjectGeipBindingsRequest.
        :type gcbandwidth_admin_status: str
        """
        self._gcbandwidth_admin_status = gcbandwidth_admin_status

    @property
    def gcbandwidth_size(self):
        """Gets the gcbandwidth_size of this ListProjectGeipBindingsRequest.

        骨干带宽的大小

        :return: The gcbandwidth_size of this ListProjectGeipBindingsRequest.
        :rtype: int
        """
        return self._gcbandwidth_size

    @gcbandwidth_size.setter
    def gcbandwidth_size(self, gcbandwidth_size):
        """Sets the gcbandwidth_size of this ListProjectGeipBindingsRequest.

        骨干带宽的大小

        :param gcbandwidth_size: The gcbandwidth_size of this ListProjectGeipBindingsRequest.
        :type gcbandwidth_size: int
        """
        self._gcbandwidth_size = gcbandwidth_size

    @property
    def gcbandwidth_sla_level(self):
        """Gets the gcbandwidth_sla_level of this ListProjectGeipBindingsRequest.

        描述网络等级，从高到低分为铂金、金、银、铜

        :return: The gcbandwidth_sla_level of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._gcbandwidth_sla_level

    @gcbandwidth_sla_level.setter
    def gcbandwidth_sla_level(self, gcbandwidth_sla_level):
        """Sets the gcbandwidth_sla_level of this ListProjectGeipBindingsRequest.

        描述网络等级，从高到低分为铂金、金、银、铜

        :param gcbandwidth_sla_level: The gcbandwidth_sla_level of this ListProjectGeipBindingsRequest.
        :type gcbandwidth_sla_level: str
        """
        self._gcbandwidth_sla_level = gcbandwidth_sla_level

    @property
    def gcbandwidth_dscp(self):
        """Gets the gcbandwidth_dscp of this ListProjectGeipBindingsRequest.

        线路质量金银铜对应的DSCP值

        :return: The gcbandwidth_dscp of this ListProjectGeipBindingsRequest.
        :rtype: int
        """
        return self._gcbandwidth_dscp

    @gcbandwidth_dscp.setter
    def gcbandwidth_dscp(self, gcbandwidth_dscp):
        """Sets the gcbandwidth_dscp of this ListProjectGeipBindingsRequest.

        线路质量金银铜对应的DSCP值

        :param gcbandwidth_dscp: The gcbandwidth_dscp of this ListProjectGeipBindingsRequest.
        :type gcbandwidth_dscp: int
        """
        self._gcbandwidth_dscp = gcbandwidth_dscp

    @property
    def vnic_private_ip_address(self):
        """Gets the vnic_private_ip_address of this ListProjectGeipBindingsRequest.

        绑定实例的ip地址

        :return: The vnic_private_ip_address of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._vnic_private_ip_address

    @vnic_private_ip_address.setter
    def vnic_private_ip_address(self, vnic_private_ip_address):
        """Sets the vnic_private_ip_address of this ListProjectGeipBindingsRequest.

        绑定实例的ip地址

        :param vnic_private_ip_address: The vnic_private_ip_address of this ListProjectGeipBindingsRequest.
        :type vnic_private_ip_address: str
        """
        self._vnic_private_ip_address = vnic_private_ip_address

    @property
    def vnic_vpc_id(self):
        """Gets the vnic_vpc_id of this ListProjectGeipBindingsRequest.

        绑定实例所在的vpcid

        :return: The vnic_vpc_id of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._vnic_vpc_id

    @vnic_vpc_id.setter
    def vnic_vpc_id(self, vnic_vpc_id):
        """Sets the vnic_vpc_id of this ListProjectGeipBindingsRequest.

        绑定实例所在的vpcid

        :param vnic_vpc_id: The vnic_vpc_id of this ListProjectGeipBindingsRequest.
        :type vnic_vpc_id: str
        """
        self._vnic_vpc_id = vnic_vpc_id

    @property
    def vnic_port_id(self):
        """Gets the vnic_port_id of this ListProjectGeipBindingsRequest.

        绑定实例port的uuid

        :return: The vnic_port_id of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._vnic_port_id

    @vnic_port_id.setter
    def vnic_port_id(self, vnic_port_id):
        """Sets the vnic_port_id of this ListProjectGeipBindingsRequest.

        绑定实例port的uuid

        :param vnic_port_id: The vnic_port_id of this ListProjectGeipBindingsRequest.
        :type vnic_port_id: str
        """
        self._vnic_port_id = vnic_port_id

    @property
    def vnic_device_id(self):
        """Gets the vnic_device_id of this ListProjectGeipBindingsRequest.

        绑定实例port对应的实例id

        :return: The vnic_device_id of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._vnic_device_id

    @vnic_device_id.setter
    def vnic_device_id(self, vnic_device_id):
        """Sets the vnic_device_id of this ListProjectGeipBindingsRequest.

        绑定实例port对应的实例id

        :param vnic_device_id: The vnic_device_id of this ListProjectGeipBindingsRequest.
        :type vnic_device_id: str
        """
        self._vnic_device_id = vnic_device_id

    @property
    def vnic_device_owner(self):
        """Gets the vnic_device_owner of this ListProjectGeipBindingsRequest.

        绑定实例port对应的实例所有者

        :return: The vnic_device_owner of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._vnic_device_owner

    @vnic_device_owner.setter
    def vnic_device_owner(self, vnic_device_owner):
        """Sets the vnic_device_owner of this ListProjectGeipBindingsRequest.

        绑定实例port对应的实例所有者

        :param vnic_device_owner: The vnic_device_owner of this ListProjectGeipBindingsRequest.
        :type vnic_device_owner: str
        """
        self._vnic_device_owner = vnic_device_owner

    @property
    def vnic_device_owner_prefixlike(self):
        """Gets the vnic_device_owner_prefixlike of this ListProjectGeipBindingsRequest.

        绑定实例port对应的实例所有者的前缀

        :return: The vnic_device_owner_prefixlike of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._vnic_device_owner_prefixlike

    @vnic_device_owner_prefixlike.setter
    def vnic_device_owner_prefixlike(self, vnic_device_owner_prefixlike):
        """Sets the vnic_device_owner_prefixlike of this ListProjectGeipBindingsRequest.

        绑定实例port对应的实例所有者的前缀

        :param vnic_device_owner_prefixlike: The vnic_device_owner_prefixlike of this ListProjectGeipBindingsRequest.
        :type vnic_device_owner_prefixlike: str
        """
        self._vnic_device_owner_prefixlike = vnic_device_owner_prefixlike

    @property
    def vnic_instance_type(self):
        """Gets the vnic_instance_type of this ListProjectGeipBindingsRequest.

        绑定实例port对应的实例类型

        :return: The vnic_instance_type of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._vnic_instance_type

    @vnic_instance_type.setter
    def vnic_instance_type(self, vnic_instance_type):
        """Sets the vnic_instance_type of this ListProjectGeipBindingsRequest.

        绑定实例port对应的实例类型

        :param vnic_instance_type: The vnic_instance_type of this ListProjectGeipBindingsRequest.
        :type vnic_instance_type: str
        """
        self._vnic_instance_type = vnic_instance_type

    @property
    def vnic_instance_id(self):
        """Gets the vnic_instance_id of this ListProjectGeipBindingsRequest.

        绑定实例port对应的实例id

        :return: The vnic_instance_id of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._vnic_instance_id

    @vnic_instance_id.setter
    def vnic_instance_id(self, vnic_instance_id):
        """Sets the vnic_instance_id of this ListProjectGeipBindingsRequest.

        绑定实例port对应的实例id

        :param vnic_instance_id: The vnic_instance_id of this ListProjectGeipBindingsRequest.
        :type vnic_instance_id: str
        """
        self._vnic_instance_id = vnic_instance_id

    @property
    def sort_key(self):
        """Gets the sort_key of this ListProjectGeipBindingsRequest.

        排序，形式为\"sort_key=geip_id&sort_dir=asc\"  支持字段：geip_id/version/public_border_group/ geip_ip_address/created_at/updated_at

        :return: The sort_key of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListProjectGeipBindingsRequest.

        排序，形式为\"sort_key=geip_id&sort_dir=asc\"  支持字段：geip_id/version/public_border_group/ geip_ip_address/created_at/updated_at

        :param sort_key: The sort_key of this ListProjectGeipBindingsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListProjectGeipBindingsRequest.

        排序方向  取值范围：asc、desc

        :return: The sort_dir of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListProjectGeipBindingsRequest.

        排序方向  取值范围：asc、desc

        :param sort_dir: The sort_dir of this ListProjectGeipBindingsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        """Gets the limit of this ListProjectGeipBindingsRequest.

        每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定

        :return: The limit of this ListProjectGeipBindingsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProjectGeipBindingsRequest.

        每页返回的个数取值范围：0~[2000]，其中2000为局点差异项，具体取值由局点决定

        :param limit: The limit of this ListProjectGeipBindingsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListProjectGeipBindingsRequest.

        分页起始点

        :return: The offset of this ListProjectGeipBindingsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProjectGeipBindingsRequest.

        分页起始点

        :param offset: The offset of this ListProjectGeipBindingsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        """Gets the marker of this ListProjectGeipBindingsRequest.

        分页起始点

        :return: The marker of this ListProjectGeipBindingsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListProjectGeipBindingsRequest.

        分页起始点

        :param marker: The marker of this ListProjectGeipBindingsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListProjectGeipBindingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
