# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstancevirtualListResp:

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
        'owner': 'str',
        'location': 'str',
        'forward_mode': 'str',
        'cluster_id': 'str',
        'hash_mode': 'str',
        'type': 'str',
        'vni': 'int',
        'nexthops': 'list[NexthopDict]',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'owner': 'owner',
        'location': 'location',
        'forward_mode': 'forward_mode',
        'cluster_id': 'cluster_id',
        'hash_mode': 'hash_mode',
        'type': 'type',
        'vni': 'vni',
        'nexthops': 'nexthops',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, owner=None, location=None, forward_mode=None, cluster_id=None, hash_mode=None, type=None, vni=None, nexthops=None, created_at=None, updated_at=None):
        r"""InstancevirtualListResp

        The model defined in huaweicloud sdk

        :param id: virtualnexthop的uuid
        :type id: str
        :param owner: virtualnexthop的所有者
        :type owner: str
        :param location: 标识网关所在位置POD、AZ、REGION、GLOBAL
        :type location: str
        :param forward_mode: 功能说明：nexthops的转发模式  取值范围：&#39;ACTIVE-ACTIVE&#39;多活模式、&#39;ACTIVE-STANDBY&#39;主备模式
        :type forward_mode: str
        :param cluster_id: 功能说明：网关所在集群信息，可为空  取值范围：0-36长度的字符串
        :type cluster_id: str
        :param hash_mode: 功能说明：nexthops在底层的负载均衡策略  取值范围：&#39;2_TUPLE&#39;二元组、&#39;3_TUPLE&#39;三元组、&#39;5_TUPLE&#39;五元组
        :type hash_mode: str
        :param type: 功能说明：下一跳所属网络类型  取值范围：&#39;VXLAN&#39;、&#39;VLAN&#39;
        :type type: str
        :param vni: 功能说明：网络id标识，与type组合使用  取值范围：type&#x3D;VXLAN时取值0-16777215,type&#x3D;VLAN时取值0-4095
        :type vni: int
        :param nexthops: 下一跳信息列表
        :type nexthops: list[:class:`huaweicloudsdkeip.v3.NexthopDict`]
        :param created_at: 功能说明：VirtualNexthop对象创建时间，UTC格式
        :type created_at: str
        :param updated_at: 功能说明：VirtualNexthop对象更新时间，UTC格式
        :type updated_at: str
        """
        
        

        self._id = None
        self._owner = None
        self._location = None
        self._forward_mode = None
        self._cluster_id = None
        self._hash_mode = None
        self._type = None
        self._vni = None
        self._nexthops = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if owner is not None:
            self.owner = owner
        if location is not None:
            self.location = location
        if forward_mode is not None:
            self.forward_mode = forward_mode
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if hash_mode is not None:
            self.hash_mode = hash_mode
        if type is not None:
            self.type = type
        if vni is not None:
            self.vni = vni
        if nexthops is not None:
            self.nexthops = nexthops
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this InstancevirtualListResp.

        virtualnexthop的uuid

        :return: The id of this InstancevirtualListResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InstancevirtualListResp.

        virtualnexthop的uuid

        :param id: The id of this InstancevirtualListResp.
        :type id: str
        """
        self._id = id

    @property
    def owner(self):
        r"""Gets the owner of this InstancevirtualListResp.

        virtualnexthop的所有者

        :return: The owner of this InstancevirtualListResp.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this InstancevirtualListResp.

        virtualnexthop的所有者

        :param owner: The owner of this InstancevirtualListResp.
        :type owner: str
        """
        self._owner = owner

    @property
    def location(self):
        r"""Gets the location of this InstancevirtualListResp.

        标识网关所在位置POD、AZ、REGION、GLOBAL

        :return: The location of this InstancevirtualListResp.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this InstancevirtualListResp.

        标识网关所在位置POD、AZ、REGION、GLOBAL

        :param location: The location of this InstancevirtualListResp.
        :type location: str
        """
        self._location = location

    @property
    def forward_mode(self):
        r"""Gets the forward_mode of this InstancevirtualListResp.

        功能说明：nexthops的转发模式  取值范围：'ACTIVE-ACTIVE'多活模式、'ACTIVE-STANDBY'主备模式

        :return: The forward_mode of this InstancevirtualListResp.
        :rtype: str
        """
        return self._forward_mode

    @forward_mode.setter
    def forward_mode(self, forward_mode):
        r"""Sets the forward_mode of this InstancevirtualListResp.

        功能说明：nexthops的转发模式  取值范围：'ACTIVE-ACTIVE'多活模式、'ACTIVE-STANDBY'主备模式

        :param forward_mode: The forward_mode of this InstancevirtualListResp.
        :type forward_mode: str
        """
        self._forward_mode = forward_mode

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this InstancevirtualListResp.

        功能说明：网关所在集群信息，可为空  取值范围：0-36长度的字符串

        :return: The cluster_id of this InstancevirtualListResp.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this InstancevirtualListResp.

        功能说明：网关所在集群信息，可为空  取值范围：0-36长度的字符串

        :param cluster_id: The cluster_id of this InstancevirtualListResp.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def hash_mode(self):
        r"""Gets the hash_mode of this InstancevirtualListResp.

        功能说明：nexthops在底层的负载均衡策略  取值范围：'2_TUPLE'二元组、'3_TUPLE'三元组、'5_TUPLE'五元组

        :return: The hash_mode of this InstancevirtualListResp.
        :rtype: str
        """
        return self._hash_mode

    @hash_mode.setter
    def hash_mode(self, hash_mode):
        r"""Sets the hash_mode of this InstancevirtualListResp.

        功能说明：nexthops在底层的负载均衡策略  取值范围：'2_TUPLE'二元组、'3_TUPLE'三元组、'5_TUPLE'五元组

        :param hash_mode: The hash_mode of this InstancevirtualListResp.
        :type hash_mode: str
        """
        self._hash_mode = hash_mode

    @property
    def type(self):
        r"""Gets the type of this InstancevirtualListResp.

        功能说明：下一跳所属网络类型  取值范围：'VXLAN'、'VLAN'

        :return: The type of this InstancevirtualListResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this InstancevirtualListResp.

        功能说明：下一跳所属网络类型  取值范围：'VXLAN'、'VLAN'

        :param type: The type of this InstancevirtualListResp.
        :type type: str
        """
        self._type = type

    @property
    def vni(self):
        r"""Gets the vni of this InstancevirtualListResp.

        功能说明：网络id标识，与type组合使用  取值范围：type=VXLAN时取值0-16777215,type=VLAN时取值0-4095

        :return: The vni of this InstancevirtualListResp.
        :rtype: int
        """
        return self._vni

    @vni.setter
    def vni(self, vni):
        r"""Sets the vni of this InstancevirtualListResp.

        功能说明：网络id标识，与type组合使用  取值范围：type=VXLAN时取值0-16777215,type=VLAN时取值0-4095

        :param vni: The vni of this InstancevirtualListResp.
        :type vni: int
        """
        self._vni = vni

    @property
    def nexthops(self):
        r"""Gets the nexthops of this InstancevirtualListResp.

        下一跳信息列表

        :return: The nexthops of this InstancevirtualListResp.
        :rtype: list[:class:`huaweicloudsdkeip.v3.NexthopDict`]
        """
        return self._nexthops

    @nexthops.setter
    def nexthops(self, nexthops):
        r"""Sets the nexthops of this InstancevirtualListResp.

        下一跳信息列表

        :param nexthops: The nexthops of this InstancevirtualListResp.
        :type nexthops: list[:class:`huaweicloudsdkeip.v3.NexthopDict`]
        """
        self._nexthops = nexthops

    @property
    def created_at(self):
        r"""Gets the created_at of this InstancevirtualListResp.

        功能说明：VirtualNexthop对象创建时间，UTC格式

        :return: The created_at of this InstancevirtualListResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this InstancevirtualListResp.

        功能说明：VirtualNexthop对象创建时间，UTC格式

        :param created_at: The created_at of this InstancevirtualListResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this InstancevirtualListResp.

        功能说明：VirtualNexthop对象更新时间，UTC格式

        :return: The updated_at of this InstancevirtualListResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this InstancevirtualListResp.

        功能说明：VirtualNexthop对象更新时间，UTC格式

        :param updated_at: The updated_at of this InstancevirtualListResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, InstancevirtualListResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
