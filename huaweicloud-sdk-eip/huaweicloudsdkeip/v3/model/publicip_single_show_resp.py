# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicipSingleShowResp:

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
        'project_id': 'str',
        'ip_version': 'int',
        'public_ip_address': 'str',
        'public_ipv6_address': 'str',
        'network_type': 'str',
        'status': 'str',
        'description': 'str',
        'public_border_group': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'type': 'str',
        'vnic': 'VnicInfo',
        'bandwidth': 'PublicipBandwidthInfo',
        'enterprise_project_id': 'str',
        'billing_info': 'str',
        'lock_status': 'str',
        'associate_instance_type': 'str',
        'associate_instance_id': 'str',
        'publicip_pool_id': 'str',
        'publicip_pool_name': 'str',
        'alias': 'str',
        'profile': 'ProfileInfo',
        'fake_network_type': 'bool',
        'tags': 'list[str]',
        'associate_instance_metadata': 'str',
        'associate_mode': 'str',
        'allow_share_bandwidth_types': 'list[str]',
        'cascade_delete_by_instance': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'ip_version': 'ip_version',
        'public_ip_address': 'public_ip_address',
        'public_ipv6_address': 'public_ipv6_address',
        'network_type': 'network_type',
        'status': 'status',
        'description': 'description',
        'public_border_group': 'public_border_group',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'type': 'type',
        'vnic': 'vnic',
        'bandwidth': 'bandwidth',
        'enterprise_project_id': 'enterprise_project_id',
        'billing_info': 'billing_info',
        'lock_status': 'lock_status',
        'associate_instance_type': 'associate_instance_type',
        'associate_instance_id': 'associate_instance_id',
        'publicip_pool_id': 'publicip_pool_id',
        'publicip_pool_name': 'publicip_pool_name',
        'alias': 'alias',
        'profile': 'profile',
        'fake_network_type': 'fake_network_type',
        'tags': 'tags',
        'associate_instance_metadata': 'associate_instance_metadata',
        'associate_mode': 'associate_mode',
        'allow_share_bandwidth_types': 'allow_share_bandwidth_types',
        'cascade_delete_by_instance': 'cascade_delete_by_instance'
    }

    def __init__(self, id=None, project_id=None, ip_version=None, public_ip_address=None, public_ipv6_address=None, network_type=None, status=None, description=None, public_border_group=None, created_at=None, updated_at=None, type=None, vnic=None, bandwidth=None, enterprise_project_id=None, billing_info=None, lock_status=None, associate_instance_type=None, associate_instance_id=None, publicip_pool_id=None, publicip_pool_name=None, alias=None, profile=None, fake_network_type=None, tags=None, associate_instance_metadata=None, associate_mode=None, allow_share_bandwidth_types=None, cascade_delete_by_instance=None):
        """PublicipSingleShowResp

        The model defined in huaweicloud sdk

        :param id: 功能说明：弹性公网IP唯一标识
        :type id: str
        :param project_id: 功能说明：项目ID
        :type project_id: str
        :param ip_version: 功能说明：IP版本信息 取值范围：4表示公网IP地址为public_ip_address地址;6表示公网IP地址为public_ipv6_address地址\&quot;
        :type ip_version: int
        :param public_ip_address: 功能说明：弹性公网IP或者IPv6端口的地址
        :type public_ip_address: str
        :param public_ipv6_address: 功能说明：IPv4时无此字段，IPv6时为申请到的弹性公网IP地址
        :type public_ipv6_address: str
        :param network_type: 废弃，功能由publicip_pool_name继承，默认不显示。功能说明：弹性公网IP的网络类型
        :type network_type: str
        :param status: 功能说明：弹性公网IP的状态  取值范围：冻结FREEZED，绑定失败BIND_ERROR，绑定中BINDING，释放中PENDING_DELETE， 创建中PENDING_CREATE，创建中NOTIFYING，释放中NOTIFY_DELETE，更新中PENDING_UPDATE， 未绑定DOWN ，绑定ACTIVE，绑定ELB，绑定VPN，失败ERROR。
        :type status: str
        :param description: 功能说明：弹性公网IP描述信息 约束：用户以自定义方式标识资源，系统不感知
        :type description: str
        :param public_border_group: 功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：publicip只能绑定该字段相同的资源
        :type public_border_group: str
        :param created_at: 功能说明：资源创建UTC时间 格式:yyyy-MM-ddTHH:mm:ssZ
        :type created_at: datetime
        :param updated_at: 功能说明：资源更新UTC时间 格式:yyyy-MM-ddTHH:mm:ssZ
        :type updated_at: datetime
        :param type: 功能说明：弹性公网IP类型
        :type type: str
        :param vnic: 
        :type vnic: :class:`huaweicloudsdkeip.v3.VnicInfo`
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkeip.v3.PublicipBandwidthInfo`
        :param enterprise_project_id: 功能说明：企业项目ID。最大长度36字节,带“-”连字符的UUID格式,或者是字符串“0”。创建弹性公网IP时,给弹性公网IP绑定企业项目ID。
        :type enterprise_project_id: str
        :param billing_info: 功能说明：公网IP的订单信息 约束：包周期才会有订单信息，按需资源此字段为空
        :type billing_info: str
        :param lock_status: 功能说明：记录公网IP当前的冻结状态 约束：metadata类型，标识欠费冻结、公安冻结 取值范围：police，locked
        :type lock_status: str
        :param associate_instance_type: 功能说明：公网IP绑定的实例类型 取值范围：PORT、NATGW、ELB、ELBV1、VPN、null
        :type associate_instance_type: str
        :param associate_instance_id: 功能说明：公网IP绑定的实例ID
        :type associate_instance_id: str
        :param publicip_pool_id: 功能说明：公网IP所属网络的ID。publicip_pool_name对应的网络ID
        :type publicip_pool_id: str
        :param publicip_pool_name: 功能说明：弹性公网IP的网络类型, 包括公共池类型，如5_bgp/5_sbgp...，和用户购买的专属池。 专属池见publcip_pool相关接口
        :type publicip_pool_name: str
        :param alias: 功能说明：弹性公网IP名称
        :type alias: str
        :param profile: 
        :type profile: :class:`huaweicloudsdkeip.v3.ProfileInfo`
        :param fake_network_type: 默认不显示。该字段仅仅用于表示eip的bgp类型是否是真实的静态sbgp * 1. 如果为true，则该eip可以切换bgp类型 * 2. 如果为false，则该eip不可以切换bgp类型
        :type fake_network_type: bool
        :param tags: 默认不显示。用户标签
        :type tags: list[str]
        :param associate_instance_metadata: 默认不显示。记录实例的更上一层归属。例如associate_instance_type为PORT，此字段记录PORT的device_id和device_owner信息。仅有限场景记录。
        :type associate_instance_metadata: str
        :param associate_mode: 默认不显示。开启支持直通模式后展示，表示直通模式的标识。
        :type associate_mode: str
        :param allow_share_bandwidth_types: 功能说明：表示此publicip可以加入的共享带宽类型列表，如果为空列表，则表示该           publicip不能加入任何共享带宽 约束：publicip只能加入到有该带宽类型的共享带宽中
        :type allow_share_bandwidth_types: list[str]
        :param cascade_delete_by_instance: 默认不显示。表示该eip是否支持与实例同步删除。
        :type cascade_delete_by_instance: bool
        """
        
        

        self._id = None
        self._project_id = None
        self._ip_version = None
        self._public_ip_address = None
        self._public_ipv6_address = None
        self._network_type = None
        self._status = None
        self._description = None
        self._public_border_group = None
        self._created_at = None
        self._updated_at = None
        self._type = None
        self._vnic = None
        self._bandwidth = None
        self._enterprise_project_id = None
        self._billing_info = None
        self._lock_status = None
        self._associate_instance_type = None
        self._associate_instance_id = None
        self._publicip_pool_id = None
        self._publicip_pool_name = None
        self._alias = None
        self._profile = None
        self._fake_network_type = None
        self._tags = None
        self._associate_instance_metadata = None
        self._associate_mode = None
        self._allow_share_bandwidth_types = None
        self._cascade_delete_by_instance = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if ip_version is not None:
            self.ip_version = ip_version
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if public_ipv6_address is not None:
            self.public_ipv6_address = public_ipv6_address
        if network_type is not None:
            self.network_type = network_type
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if type is not None:
            self.type = type
        if vnic is not None:
            self.vnic = vnic
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if billing_info is not None:
            self.billing_info = billing_info
        if lock_status is not None:
            self.lock_status = lock_status
        if associate_instance_type is not None:
            self.associate_instance_type = associate_instance_type
        if associate_instance_id is not None:
            self.associate_instance_id = associate_instance_id
        if publicip_pool_id is not None:
            self.publicip_pool_id = publicip_pool_id
        if publicip_pool_name is not None:
            self.publicip_pool_name = publicip_pool_name
        if alias is not None:
            self.alias = alias
        if profile is not None:
            self.profile = profile
        if fake_network_type is not None:
            self.fake_network_type = fake_network_type
        if tags is not None:
            self.tags = tags
        if associate_instance_metadata is not None:
            self.associate_instance_metadata = associate_instance_metadata
        if associate_mode is not None:
            self.associate_mode = associate_mode
        if allow_share_bandwidth_types is not None:
            self.allow_share_bandwidth_types = allow_share_bandwidth_types
        if cascade_delete_by_instance is not None:
            self.cascade_delete_by_instance = cascade_delete_by_instance

    @property
    def id(self):
        """Gets the id of this PublicipSingleShowResp.

        功能说明：弹性公网IP唯一标识

        :return: The id of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicipSingleShowResp.

        功能说明：弹性公网IP唯一标识

        :param id: The id of this PublicipSingleShowResp.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this PublicipSingleShowResp.

        功能说明：项目ID

        :return: The project_id of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PublicipSingleShowResp.

        功能说明：项目ID

        :param project_id: The project_id of this PublicipSingleShowResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ip_version(self):
        """Gets the ip_version of this PublicipSingleShowResp.

        功能说明：IP版本信息 取值范围：4表示公网IP地址为public_ip_address地址;6表示公网IP地址为public_ipv6_address地址\"

        :return: The ip_version of this PublicipSingleShowResp.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this PublicipSingleShowResp.

        功能说明：IP版本信息 取值范围：4表示公网IP地址为public_ip_address地址;6表示公网IP地址为public_ipv6_address地址\"

        :param ip_version: The ip_version of this PublicipSingleShowResp.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this PublicipSingleShowResp.

        功能说明：弹性公网IP或者IPv6端口的地址

        :return: The public_ip_address of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this PublicipSingleShowResp.

        功能说明：弹性公网IP或者IPv6端口的地址

        :param public_ip_address: The public_ip_address of this PublicipSingleShowResp.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def public_ipv6_address(self):
        """Gets the public_ipv6_address of this PublicipSingleShowResp.

        功能说明：IPv4时无此字段，IPv6时为申请到的弹性公网IP地址

        :return: The public_ipv6_address of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._public_ipv6_address

    @public_ipv6_address.setter
    def public_ipv6_address(self, public_ipv6_address):
        """Sets the public_ipv6_address of this PublicipSingleShowResp.

        功能说明：IPv4时无此字段，IPv6时为申请到的弹性公网IP地址

        :param public_ipv6_address: The public_ipv6_address of this PublicipSingleShowResp.
        :type public_ipv6_address: str
        """
        self._public_ipv6_address = public_ipv6_address

    @property
    def network_type(self):
        """Gets the network_type of this PublicipSingleShowResp.

        废弃，功能由publicip_pool_name继承，默认不显示。功能说明：弹性公网IP的网络类型

        :return: The network_type of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this PublicipSingleShowResp.

        废弃，功能由publicip_pool_name继承，默认不显示。功能说明：弹性公网IP的网络类型

        :param network_type: The network_type of this PublicipSingleShowResp.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def status(self):
        """Gets the status of this PublicipSingleShowResp.

        功能说明：弹性公网IP的状态  取值范围：冻结FREEZED，绑定失败BIND_ERROR，绑定中BINDING，释放中PENDING_DELETE， 创建中PENDING_CREATE，创建中NOTIFYING，释放中NOTIFY_DELETE，更新中PENDING_UPDATE， 未绑定DOWN ，绑定ACTIVE，绑定ELB，绑定VPN，失败ERROR。

        :return: The status of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PublicipSingleShowResp.

        功能说明：弹性公网IP的状态  取值范围：冻结FREEZED，绑定失败BIND_ERROR，绑定中BINDING，释放中PENDING_DELETE， 创建中PENDING_CREATE，创建中NOTIFYING，释放中NOTIFY_DELETE，更新中PENDING_UPDATE， 未绑定DOWN ，绑定ACTIVE，绑定ELB，绑定VPN，失败ERROR。

        :param status: The status of this PublicipSingleShowResp.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this PublicipSingleShowResp.

        功能说明：弹性公网IP描述信息 约束：用户以自定义方式标识资源，系统不感知

        :return: The description of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PublicipSingleShowResp.

        功能说明：弹性公网IP描述信息 约束：用户以自定义方式标识资源，系统不感知

        :param description: The description of this PublicipSingleShowResp.
        :type description: str
        """
        self._description = description

    @property
    def public_border_group(self):
        """Gets the public_border_group of this PublicipSingleShowResp.

        功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：publicip只能绑定该字段相同的资源

        :return: The public_border_group of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this PublicipSingleShowResp.

        功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：publicip只能绑定该字段相同的资源

        :param public_border_group: The public_border_group of this PublicipSingleShowResp.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def created_at(self):
        """Gets the created_at of this PublicipSingleShowResp.

        功能说明：资源创建UTC时间 格式:yyyy-MM-ddTHH:mm:ssZ

        :return: The created_at of this PublicipSingleShowResp.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PublicipSingleShowResp.

        功能说明：资源创建UTC时间 格式:yyyy-MM-ddTHH:mm:ssZ

        :param created_at: The created_at of this PublicipSingleShowResp.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PublicipSingleShowResp.

        功能说明：资源更新UTC时间 格式:yyyy-MM-ddTHH:mm:ssZ

        :return: The updated_at of this PublicipSingleShowResp.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PublicipSingleShowResp.

        功能说明：资源更新UTC时间 格式:yyyy-MM-ddTHH:mm:ssZ

        :param updated_at: The updated_at of this PublicipSingleShowResp.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def type(self):
        """Gets the type of this PublicipSingleShowResp.

        功能说明：弹性公网IP类型

        :return: The type of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PublicipSingleShowResp.

        功能说明：弹性公网IP类型

        :param type: The type of this PublicipSingleShowResp.
        :type type: str
        """
        self._type = type

    @property
    def vnic(self):
        """Gets the vnic of this PublicipSingleShowResp.

        :return: The vnic of this PublicipSingleShowResp.
        :rtype: :class:`huaweicloudsdkeip.v3.VnicInfo`
        """
        return self._vnic

    @vnic.setter
    def vnic(self, vnic):
        """Sets the vnic of this PublicipSingleShowResp.

        :param vnic: The vnic of this PublicipSingleShowResp.
        :type vnic: :class:`huaweicloudsdkeip.v3.VnicInfo`
        """
        self._vnic = vnic

    @property
    def bandwidth(self):
        """Gets the bandwidth of this PublicipSingleShowResp.

        :return: The bandwidth of this PublicipSingleShowResp.
        :rtype: :class:`huaweicloudsdkeip.v3.PublicipBandwidthInfo`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this PublicipSingleShowResp.

        :param bandwidth: The bandwidth of this PublicipSingleShowResp.
        :type bandwidth: :class:`huaweicloudsdkeip.v3.PublicipBandwidthInfo`
        """
        self._bandwidth = bandwidth

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PublicipSingleShowResp.

        功能说明：企业项目ID。最大长度36字节,带“-”连字符的UUID格式,或者是字符串“0”。创建弹性公网IP时,给弹性公网IP绑定企业项目ID。

        :return: The enterprise_project_id of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PublicipSingleShowResp.

        功能说明：企业项目ID。最大长度36字节,带“-”连字符的UUID格式,或者是字符串“0”。创建弹性公网IP时,给弹性公网IP绑定企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this PublicipSingleShowResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def billing_info(self):
        """Gets the billing_info of this PublicipSingleShowResp.

        功能说明：公网IP的订单信息 约束：包周期才会有订单信息，按需资源此字段为空

        :return: The billing_info of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this PublicipSingleShowResp.

        功能说明：公网IP的订单信息 约束：包周期才会有订单信息，按需资源此字段为空

        :param billing_info: The billing_info of this PublicipSingleShowResp.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def lock_status(self):
        """Gets the lock_status of this PublicipSingleShowResp.

        功能说明：记录公网IP当前的冻结状态 约束：metadata类型，标识欠费冻结、公安冻结 取值范围：police，locked

        :return: The lock_status of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        """Sets the lock_status of this PublicipSingleShowResp.

        功能说明：记录公网IP当前的冻结状态 约束：metadata类型，标识欠费冻结、公安冻结 取值范围：police，locked

        :param lock_status: The lock_status of this PublicipSingleShowResp.
        :type lock_status: str
        """
        self._lock_status = lock_status

    @property
    def associate_instance_type(self):
        """Gets the associate_instance_type of this PublicipSingleShowResp.

        功能说明：公网IP绑定的实例类型 取值范围：PORT、NATGW、ELB、ELBV1、VPN、null

        :return: The associate_instance_type of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._associate_instance_type

    @associate_instance_type.setter
    def associate_instance_type(self, associate_instance_type):
        """Sets the associate_instance_type of this PublicipSingleShowResp.

        功能说明：公网IP绑定的实例类型 取值范围：PORT、NATGW、ELB、ELBV1、VPN、null

        :param associate_instance_type: The associate_instance_type of this PublicipSingleShowResp.
        :type associate_instance_type: str
        """
        self._associate_instance_type = associate_instance_type

    @property
    def associate_instance_id(self):
        """Gets the associate_instance_id of this PublicipSingleShowResp.

        功能说明：公网IP绑定的实例ID

        :return: The associate_instance_id of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._associate_instance_id

    @associate_instance_id.setter
    def associate_instance_id(self, associate_instance_id):
        """Sets the associate_instance_id of this PublicipSingleShowResp.

        功能说明：公网IP绑定的实例ID

        :param associate_instance_id: The associate_instance_id of this PublicipSingleShowResp.
        :type associate_instance_id: str
        """
        self._associate_instance_id = associate_instance_id

    @property
    def publicip_pool_id(self):
        """Gets the publicip_pool_id of this PublicipSingleShowResp.

        功能说明：公网IP所属网络的ID。publicip_pool_name对应的网络ID

        :return: The publicip_pool_id of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._publicip_pool_id

    @publicip_pool_id.setter
    def publicip_pool_id(self, publicip_pool_id):
        """Sets the publicip_pool_id of this PublicipSingleShowResp.

        功能说明：公网IP所属网络的ID。publicip_pool_name对应的网络ID

        :param publicip_pool_id: The publicip_pool_id of this PublicipSingleShowResp.
        :type publicip_pool_id: str
        """
        self._publicip_pool_id = publicip_pool_id

    @property
    def publicip_pool_name(self):
        """Gets the publicip_pool_name of this PublicipSingleShowResp.

        功能说明：弹性公网IP的网络类型, 包括公共池类型，如5_bgp/5_sbgp...，和用户购买的专属池。 专属池见publcip_pool相关接口

        :return: The publicip_pool_name of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._publicip_pool_name

    @publicip_pool_name.setter
    def publicip_pool_name(self, publicip_pool_name):
        """Sets the publicip_pool_name of this PublicipSingleShowResp.

        功能说明：弹性公网IP的网络类型, 包括公共池类型，如5_bgp/5_sbgp...，和用户购买的专属池。 专属池见publcip_pool相关接口

        :param publicip_pool_name: The publicip_pool_name of this PublicipSingleShowResp.
        :type publicip_pool_name: str
        """
        self._publicip_pool_name = publicip_pool_name

    @property
    def alias(self):
        """Gets the alias of this PublicipSingleShowResp.

        功能说明：弹性公网IP名称

        :return: The alias of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this PublicipSingleShowResp.

        功能说明：弹性公网IP名称

        :param alias: The alias of this PublicipSingleShowResp.
        :type alias: str
        """
        self._alias = alias

    @property
    def profile(self):
        """Gets the profile of this PublicipSingleShowResp.

        :return: The profile of this PublicipSingleShowResp.
        :rtype: :class:`huaweicloudsdkeip.v3.ProfileInfo`
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this PublicipSingleShowResp.

        :param profile: The profile of this PublicipSingleShowResp.
        :type profile: :class:`huaweicloudsdkeip.v3.ProfileInfo`
        """
        self._profile = profile

    @property
    def fake_network_type(self):
        """Gets the fake_network_type of this PublicipSingleShowResp.

        默认不显示。该字段仅仅用于表示eip的bgp类型是否是真实的静态sbgp * 1. 如果为true，则该eip可以切换bgp类型 * 2. 如果为false，则该eip不可以切换bgp类型

        :return: The fake_network_type of this PublicipSingleShowResp.
        :rtype: bool
        """
        return self._fake_network_type

    @fake_network_type.setter
    def fake_network_type(self, fake_network_type):
        """Sets the fake_network_type of this PublicipSingleShowResp.

        默认不显示。该字段仅仅用于表示eip的bgp类型是否是真实的静态sbgp * 1. 如果为true，则该eip可以切换bgp类型 * 2. 如果为false，则该eip不可以切换bgp类型

        :param fake_network_type: The fake_network_type of this PublicipSingleShowResp.
        :type fake_network_type: bool
        """
        self._fake_network_type = fake_network_type

    @property
    def tags(self):
        """Gets the tags of this PublicipSingleShowResp.

        默认不显示。用户标签

        :return: The tags of this PublicipSingleShowResp.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PublicipSingleShowResp.

        默认不显示。用户标签

        :param tags: The tags of this PublicipSingleShowResp.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def associate_instance_metadata(self):
        """Gets the associate_instance_metadata of this PublicipSingleShowResp.

        默认不显示。记录实例的更上一层归属。例如associate_instance_type为PORT，此字段记录PORT的device_id和device_owner信息。仅有限场景记录。

        :return: The associate_instance_metadata of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._associate_instance_metadata

    @associate_instance_metadata.setter
    def associate_instance_metadata(self, associate_instance_metadata):
        """Sets the associate_instance_metadata of this PublicipSingleShowResp.

        默认不显示。记录实例的更上一层归属。例如associate_instance_type为PORT，此字段记录PORT的device_id和device_owner信息。仅有限场景记录。

        :param associate_instance_metadata: The associate_instance_metadata of this PublicipSingleShowResp.
        :type associate_instance_metadata: str
        """
        self._associate_instance_metadata = associate_instance_metadata

    @property
    def associate_mode(self):
        """Gets the associate_mode of this PublicipSingleShowResp.

        默认不显示。开启支持直通模式后展示，表示直通模式的标识。

        :return: The associate_mode of this PublicipSingleShowResp.
        :rtype: str
        """
        return self._associate_mode

    @associate_mode.setter
    def associate_mode(self, associate_mode):
        """Sets the associate_mode of this PublicipSingleShowResp.

        默认不显示。开启支持直通模式后展示，表示直通模式的标识。

        :param associate_mode: The associate_mode of this PublicipSingleShowResp.
        :type associate_mode: str
        """
        self._associate_mode = associate_mode

    @property
    def allow_share_bandwidth_types(self):
        """Gets the allow_share_bandwidth_types of this PublicipSingleShowResp.

        功能说明：表示此publicip可以加入的共享带宽类型列表，如果为空列表，则表示该           publicip不能加入任何共享带宽 约束：publicip只能加入到有该带宽类型的共享带宽中

        :return: The allow_share_bandwidth_types of this PublicipSingleShowResp.
        :rtype: list[str]
        """
        return self._allow_share_bandwidth_types

    @allow_share_bandwidth_types.setter
    def allow_share_bandwidth_types(self, allow_share_bandwidth_types):
        """Sets the allow_share_bandwidth_types of this PublicipSingleShowResp.

        功能说明：表示此publicip可以加入的共享带宽类型列表，如果为空列表，则表示该           publicip不能加入任何共享带宽 约束：publicip只能加入到有该带宽类型的共享带宽中

        :param allow_share_bandwidth_types: The allow_share_bandwidth_types of this PublicipSingleShowResp.
        :type allow_share_bandwidth_types: list[str]
        """
        self._allow_share_bandwidth_types = allow_share_bandwidth_types

    @property
    def cascade_delete_by_instance(self):
        """Gets the cascade_delete_by_instance of this PublicipSingleShowResp.

        默认不显示。表示该eip是否支持与实例同步删除。

        :return: The cascade_delete_by_instance of this PublicipSingleShowResp.
        :rtype: bool
        """
        return self._cascade_delete_by_instance

    @cascade_delete_by_instance.setter
    def cascade_delete_by_instance(self, cascade_delete_by_instance):
        """Sets the cascade_delete_by_instance of this PublicipSingleShowResp.

        默认不显示。表示该eip是否支持与实例同步删除。

        :param cascade_delete_by_instance: The cascade_delete_by_instance of this PublicipSingleShowResp.
        :type cascade_delete_by_instance: bool
        """
        self._cascade_delete_by_instance = cascade_delete_by_instance

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
        if not isinstance(other, PublicipSingleShowResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
