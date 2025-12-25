# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcEip:

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
        'alias': 'str',
        'protected_status': 'str',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'ip_version': 'int',
        'public_ip_address': 'str',
        'public_ipv6_address': 'str',
        'publicip_pool_name': 'str',
        'publicip_pool_id': 'str',
        'status': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'type': 'str',
        'vnic': 'HwcEipVnic',
        'bandwidth': 'HwcEipBandwidth',
        'lock_status': 'str',
        'associate_instance_type': 'str',
        'associate_instance_id': 'str',
        'allow_share_bandwidth_types': 'list[str]',
        'created_at': 'str',
        'updated_at': 'str',
        'public_border_group': 'str'
    }

    attribute_map = {
        'id': 'id',
        'alias': 'alias',
        'protected_status': 'protected_status',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'ip_version': 'ip_version',
        'public_ip_address': 'public_ip_address',
        'public_ipv6_address': 'public_ipv6_address',
        'publicip_pool_name': 'publicip_pool_name',
        'publicip_pool_id': 'publicip_pool_id',
        'status': 'status',
        'description': 'description',
        'tags': 'tags',
        'type': 'type',
        'vnic': 'vnic',
        'bandwidth': 'bandwidth',
        'lock_status': 'lock_status',
        'associate_instance_type': 'associate_instance_type',
        'associate_instance_id': 'associate_instance_id',
        'allow_share_bandwidth_types': 'allow_share_bandwidth_types',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, id=None, alias=None, protected_status=None, project_id=None, enterprise_project_id=None, ip_version=None, public_ip_address=None, public_ipv6_address=None, publicip_pool_name=None, publicip_pool_id=None, status=None, description=None, tags=None, type=None, vnic=None, bandwidth=None, lock_status=None, associate_instance_type=None, associate_instance_id=None, allow_share_bandwidth_types=None, created_at=None, updated_at=None, public_border_group=None):
        r"""HwcEip

        The model defined in huaweicloud sdk

        :param id: 弹性公网IP唯一标识
        :type id: str
        :param alias: 弹性公网IP名称
        :type alias: str
        :param protected_status: DDoss或CFW开启状态：OPEN | CLOSE
        :type protected_status: str
        :param project_id: 项目ID
        :type project_id: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param ip_version: IP版本信息 取值范围： 4：公网IP地址为public_ip_address地址 6：公网IP地址为public_ipv6_address地址
        :type ip_version: int
        :param public_ip_address: 弹性公网IP或者IPv6端口的地址
        :type public_ip_address: str
        :param public_ipv6_address: IPv4时无此字段，IPv6时为申请到的弹性公网IP
        :type public_ipv6_address: str
        :param publicip_pool_name: 弹性公网IP的网络类型, 包括公共池类型，如5_bgp/5_sbgp...，和用户购买的专属池。
        :type publicip_pool_name: str
        :param publicip_pool_id: 公网IP所属网络的ID，publicip_pool_name对应的网络ID
        :type publicip_pool_id: str
        :param status: 弹性公网IP的状态 取值范围： FREEZED：冻结 BIND_ERROR：绑定失败 BINDING：绑定中 PENDING_DELETE：释放中 PENDING_CREATE：创建中 NOTIFYING：创建中 NOTIFY_DELETE：释放中 PENDING_UPDATE：更新中 DOWN：未绑定 ACTIVE：绑定 ELB：绑定ELB VPN：绑定VPN ERROR：失败
        :type status: str
        :param description: 弹性公网IP描述信息
        :type description: str
        :param tags: 功能说明：用户标签。（默认不显示）
        :type tags: list[str]
        :param type: 弹性公网IP类型 枚举值： EIP DUALSTACK DUALSTACK_SUBNET
        :type type: str
        :param vnic: 
        :type vnic: :class:`huaweicloudsdksecmaster.v1.HwcEipVnic`
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdksecmaster.v1.HwcEipBandwidth`
        :param lock_status: 记录公网IP当前的冻结状态 约束：metadata类型，标识欠费冻结、公安冻结 取值范围： police locked
        :type lock_status: str
        :param associate_instance_type: 公网IP绑定的实例类型 取值范围： PORT NATGW ELB ELBV1 VPN null
        :type associate_instance_type: str
        :param associate_instance_id: 公网IP绑定的实例ID
        :type associate_instance_id: str
        :param allow_share_bandwidth_types: 表示此publicip可以加入的共享带宽类型列表，如果为空列表，则表示该 publicip不能加入任何共享带宽 约束：publicip只能加入到有该带宽类型的共享带宽中
        :type allow_share_bandwidth_types: list[str]
        :param created_at: 资产创建UTC时间 格式：yyyy-MM-ddTHH:mm:ssZ
        :type created_at: str
        :param updated_at: 资产更新UTC时间 格式：yyyy-MM-ddTHH:mm:ssZ
        :type updated_at: str
        :param public_border_group: 表示中心站点资产或者边缘站点资产 取值范围： center、边缘站点名称 约束：publicip只能绑定该字段相同的资产
        :type public_border_group: str
        """
        
        

        self._id = None
        self._alias = None
        self._protected_status = None
        self._project_id = None
        self._enterprise_project_id = None
        self._ip_version = None
        self._public_ip_address = None
        self._public_ipv6_address = None
        self._publicip_pool_name = None
        self._publicip_pool_id = None
        self._status = None
        self._description = None
        self._tags = None
        self._type = None
        self._vnic = None
        self._bandwidth = None
        self._lock_status = None
        self._associate_instance_type = None
        self._associate_instance_id = None
        self._allow_share_bandwidth_types = None
        self._created_at = None
        self._updated_at = None
        self._public_border_group = None
        self.discriminator = None

        self.id = id
        self.alias = alias
        self.protected_status = protected_status
        self.project_id = project_id
        self.enterprise_project_id = enterprise_project_id
        self.ip_version = ip_version
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if public_ipv6_address is not None:
            self.public_ipv6_address = public_ipv6_address
        if publicip_pool_name is not None:
            self.publicip_pool_name = publicip_pool_name
        if publicip_pool_id is not None:
            self.publicip_pool_id = publicip_pool_id
        self.status = status
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if vnic is not None:
            self.vnic = vnic
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if lock_status is not None:
            self.lock_status = lock_status
        if associate_instance_type is not None:
            self.associate_instance_type = associate_instance_type
        if associate_instance_id is not None:
            self.associate_instance_id = associate_instance_id
        if allow_share_bandwidth_types is not None:
            self.allow_share_bandwidth_types = allow_share_bandwidth_types
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def id(self):
        r"""Gets the id of this HwcEip.

        弹性公网IP唯一标识

        :return: The id of this HwcEip.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HwcEip.

        弹性公网IP唯一标识

        :param id: The id of this HwcEip.
        :type id: str
        """
        self._id = id

    @property
    def alias(self):
        r"""Gets the alias of this HwcEip.

        弹性公网IP名称

        :return: The alias of this HwcEip.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this HwcEip.

        弹性公网IP名称

        :param alias: The alias of this HwcEip.
        :type alias: str
        """
        self._alias = alias

    @property
    def protected_status(self):
        r"""Gets the protected_status of this HwcEip.

        DDoss或CFW开启状态：OPEN | CLOSE

        :return: The protected_status of this HwcEip.
        :rtype: str
        """
        return self._protected_status

    @protected_status.setter
    def protected_status(self, protected_status):
        r"""Sets the protected_status of this HwcEip.

        DDoss或CFW开启状态：OPEN | CLOSE

        :param protected_status: The protected_status of this HwcEip.
        :type protected_status: str
        """
        self._protected_status = protected_status

    @property
    def project_id(self):
        r"""Gets the project_id of this HwcEip.

        项目ID

        :return: The project_id of this HwcEip.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this HwcEip.

        项目ID

        :param project_id: The project_id of this HwcEip.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this HwcEip.

        企业项目ID。

        :return: The enterprise_project_id of this HwcEip.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this HwcEip.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this HwcEip.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this HwcEip.

        IP版本信息 取值范围： 4：公网IP地址为public_ip_address地址 6：公网IP地址为public_ipv6_address地址

        :return: The ip_version of this HwcEip.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this HwcEip.

        IP版本信息 取值范围： 4：公网IP地址为public_ip_address地址 6：公网IP地址为public_ipv6_address地址

        :param ip_version: The ip_version of this HwcEip.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def public_ip_address(self):
        r"""Gets the public_ip_address of this HwcEip.

        弹性公网IP或者IPv6端口的地址

        :return: The public_ip_address of this HwcEip.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        r"""Sets the public_ip_address of this HwcEip.

        弹性公网IP或者IPv6端口的地址

        :param public_ip_address: The public_ip_address of this HwcEip.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def public_ipv6_address(self):
        r"""Gets the public_ipv6_address of this HwcEip.

        IPv4时无此字段，IPv6时为申请到的弹性公网IP

        :return: The public_ipv6_address of this HwcEip.
        :rtype: str
        """
        return self._public_ipv6_address

    @public_ipv6_address.setter
    def public_ipv6_address(self, public_ipv6_address):
        r"""Sets the public_ipv6_address of this HwcEip.

        IPv4时无此字段，IPv6时为申请到的弹性公网IP

        :param public_ipv6_address: The public_ipv6_address of this HwcEip.
        :type public_ipv6_address: str
        """
        self._public_ipv6_address = public_ipv6_address

    @property
    def publicip_pool_name(self):
        r"""Gets the publicip_pool_name of this HwcEip.

        弹性公网IP的网络类型, 包括公共池类型，如5_bgp/5_sbgp...，和用户购买的专属池。

        :return: The publicip_pool_name of this HwcEip.
        :rtype: str
        """
        return self._publicip_pool_name

    @publicip_pool_name.setter
    def publicip_pool_name(self, publicip_pool_name):
        r"""Sets the publicip_pool_name of this HwcEip.

        弹性公网IP的网络类型, 包括公共池类型，如5_bgp/5_sbgp...，和用户购买的专属池。

        :param publicip_pool_name: The publicip_pool_name of this HwcEip.
        :type publicip_pool_name: str
        """
        self._publicip_pool_name = publicip_pool_name

    @property
    def publicip_pool_id(self):
        r"""Gets the publicip_pool_id of this HwcEip.

        公网IP所属网络的ID，publicip_pool_name对应的网络ID

        :return: The publicip_pool_id of this HwcEip.
        :rtype: str
        """
        return self._publicip_pool_id

    @publicip_pool_id.setter
    def publicip_pool_id(self, publicip_pool_id):
        r"""Sets the publicip_pool_id of this HwcEip.

        公网IP所属网络的ID，publicip_pool_name对应的网络ID

        :param publicip_pool_id: The publicip_pool_id of this HwcEip.
        :type publicip_pool_id: str
        """
        self._publicip_pool_id = publicip_pool_id

    @property
    def status(self):
        r"""Gets the status of this HwcEip.

        弹性公网IP的状态 取值范围： FREEZED：冻结 BIND_ERROR：绑定失败 BINDING：绑定中 PENDING_DELETE：释放中 PENDING_CREATE：创建中 NOTIFYING：创建中 NOTIFY_DELETE：释放中 PENDING_UPDATE：更新中 DOWN：未绑定 ACTIVE：绑定 ELB：绑定ELB VPN：绑定VPN ERROR：失败

        :return: The status of this HwcEip.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HwcEip.

        弹性公网IP的状态 取值范围： FREEZED：冻结 BIND_ERROR：绑定失败 BINDING：绑定中 PENDING_DELETE：释放中 PENDING_CREATE：创建中 NOTIFYING：创建中 NOTIFY_DELETE：释放中 PENDING_UPDATE：更新中 DOWN：未绑定 ACTIVE：绑定 ELB：绑定ELB VPN：绑定VPN ERROR：失败

        :param status: The status of this HwcEip.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this HwcEip.

        弹性公网IP描述信息

        :return: The description of this HwcEip.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this HwcEip.

        弹性公网IP描述信息

        :param description: The description of this HwcEip.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this HwcEip.

        功能说明：用户标签。（默认不显示）

        :return: The tags of this HwcEip.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this HwcEip.

        功能说明：用户标签。（默认不显示）

        :param tags: The tags of this HwcEip.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def type(self):
        r"""Gets the type of this HwcEip.

        弹性公网IP类型 枚举值： EIP DUALSTACK DUALSTACK_SUBNET

        :return: The type of this HwcEip.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HwcEip.

        弹性公网IP类型 枚举值： EIP DUALSTACK DUALSTACK_SUBNET

        :param type: The type of this HwcEip.
        :type type: str
        """
        self._type = type

    @property
    def vnic(self):
        r"""Gets the vnic of this HwcEip.

        :return: The vnic of this HwcEip.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcEipVnic`
        """
        return self._vnic

    @vnic.setter
    def vnic(self, vnic):
        r"""Sets the vnic of this HwcEip.

        :param vnic: The vnic of this HwcEip.
        :type vnic: :class:`huaweicloudsdksecmaster.v1.HwcEipVnic`
        """
        self._vnic = vnic

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this HwcEip.

        :return: The bandwidth of this HwcEip.
        :rtype: :class:`huaweicloudsdksecmaster.v1.HwcEipBandwidth`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this HwcEip.

        :param bandwidth: The bandwidth of this HwcEip.
        :type bandwidth: :class:`huaweicloudsdksecmaster.v1.HwcEipBandwidth`
        """
        self._bandwidth = bandwidth

    @property
    def lock_status(self):
        r"""Gets the lock_status of this HwcEip.

        记录公网IP当前的冻结状态 约束：metadata类型，标识欠费冻结、公安冻结 取值范围： police locked

        :return: The lock_status of this HwcEip.
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        r"""Sets the lock_status of this HwcEip.

        记录公网IP当前的冻结状态 约束：metadata类型，标识欠费冻结、公安冻结 取值范围： police locked

        :param lock_status: The lock_status of this HwcEip.
        :type lock_status: str
        """
        self._lock_status = lock_status

    @property
    def associate_instance_type(self):
        r"""Gets the associate_instance_type of this HwcEip.

        公网IP绑定的实例类型 取值范围： PORT NATGW ELB ELBV1 VPN null

        :return: The associate_instance_type of this HwcEip.
        :rtype: str
        """
        return self._associate_instance_type

    @associate_instance_type.setter
    def associate_instance_type(self, associate_instance_type):
        r"""Sets the associate_instance_type of this HwcEip.

        公网IP绑定的实例类型 取值范围： PORT NATGW ELB ELBV1 VPN null

        :param associate_instance_type: The associate_instance_type of this HwcEip.
        :type associate_instance_type: str
        """
        self._associate_instance_type = associate_instance_type

    @property
    def associate_instance_id(self):
        r"""Gets the associate_instance_id of this HwcEip.

        公网IP绑定的实例ID

        :return: The associate_instance_id of this HwcEip.
        :rtype: str
        """
        return self._associate_instance_id

    @associate_instance_id.setter
    def associate_instance_id(self, associate_instance_id):
        r"""Sets the associate_instance_id of this HwcEip.

        公网IP绑定的实例ID

        :param associate_instance_id: The associate_instance_id of this HwcEip.
        :type associate_instance_id: str
        """
        self._associate_instance_id = associate_instance_id

    @property
    def allow_share_bandwidth_types(self):
        r"""Gets the allow_share_bandwidth_types of this HwcEip.

        表示此publicip可以加入的共享带宽类型列表，如果为空列表，则表示该 publicip不能加入任何共享带宽 约束：publicip只能加入到有该带宽类型的共享带宽中

        :return: The allow_share_bandwidth_types of this HwcEip.
        :rtype: list[str]
        """
        return self._allow_share_bandwidth_types

    @allow_share_bandwidth_types.setter
    def allow_share_bandwidth_types(self, allow_share_bandwidth_types):
        r"""Sets the allow_share_bandwidth_types of this HwcEip.

        表示此publicip可以加入的共享带宽类型列表，如果为空列表，则表示该 publicip不能加入任何共享带宽 约束：publicip只能加入到有该带宽类型的共享带宽中

        :param allow_share_bandwidth_types: The allow_share_bandwidth_types of this HwcEip.
        :type allow_share_bandwidth_types: list[str]
        """
        self._allow_share_bandwidth_types = allow_share_bandwidth_types

    @property
    def created_at(self):
        r"""Gets the created_at of this HwcEip.

        资产创建UTC时间 格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The created_at of this HwcEip.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this HwcEip.

        资产创建UTC时间 格式：yyyy-MM-ddTHH:mm:ssZ

        :param created_at: The created_at of this HwcEip.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this HwcEip.

        资产更新UTC时间 格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The updated_at of this HwcEip.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this HwcEip.

        资产更新UTC时间 格式：yyyy-MM-ddTHH:mm:ssZ

        :param updated_at: The updated_at of this HwcEip.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this HwcEip.

        表示中心站点资产或者边缘站点资产 取值范围： center、边缘站点名称 约束：publicip只能绑定该字段相同的资产

        :return: The public_border_group of this HwcEip.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this HwcEip.

        表示中心站点资产或者边缘站点资产 取值范围： center、边缘站点名称 约束：publicip只能绑定该字段相同的资产

        :param public_border_group: The public_border_group of this HwcEip.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HwcEip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
