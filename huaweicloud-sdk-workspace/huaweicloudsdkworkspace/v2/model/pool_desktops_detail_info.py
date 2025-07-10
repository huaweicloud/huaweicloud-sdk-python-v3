# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolDesktopsDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'computer_name': 'str',
        'os_host_name': 'str',
        'addresses': 'dict(str, list[AddressInfo])',
        'ip_addresses': 'list[str]',
        'ipv4': 'str',
        'ipv6': 'str',
        'user_list': 'list[str]',
        'user_group_list': 'list[str]',
        'desktop_type': 'str',
        'resource_type': 'str',
        'metadata': 'dict(str, str)',
        'flavor': 'FlavorInfo',
        'status': 'str',
        'task_status': 'str',
        'in_maintenance_mode': 'bool',
        'created': 'str',
        'security_groups': 'list[SecurityGroupInfo]',
        'login_status': 'str',
        'user_name': 'str',
        'attach_user_infos': 'list[AttachInstancesUserInfo]',
        'product_id': 'str',
        'share_resource_sku': 'str',
        'root_volume': 'VolumeDetail',
        'data_volumes': 'list[VolumeDetail]',
        'user_group': 'str',
        'availability_zone': 'str',
        'site_type': 'str',
        'site_name': 'str',
        'product': 'ProductInfo',
        'ou_name': 'str',
        'os_version': 'str',
        'sid': 'str',
        'order_id': 'str',
        'tags': 'list[Tag]',
        'is_support_internet': 'bool',
        'internet_mode': 'str',
        'internet_mode_list': 'list[str]',
        'is_attaching_eip': 'bool',
        'attach_state': 'str',
        'enterprise_project_id': 'str',
        'subnet_id': 'str',
        'bill_resource_id': 'str',
        'process': 'int',
        'root_resource_id': 'str',
        'hour_package_info': 'HourPackageInfo',
        'inconsistent_types': 'list[str]'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'computer_name': 'computer_name',
        'os_host_name': 'os_host_name',
        'addresses': 'addresses',
        'ip_addresses': 'ip_addresses',
        'ipv4': 'ipv4',
        'ipv6': 'ipv6',
        'user_list': 'user_list',
        'user_group_list': 'user_group_list',
        'desktop_type': 'desktop_type',
        'resource_type': 'resource_type',
        'metadata': 'metadata',
        'flavor': 'flavor',
        'status': 'status',
        'task_status': 'task_status',
        'in_maintenance_mode': 'in_maintenance_mode',
        'created': 'created',
        'security_groups': 'security_groups',
        'login_status': 'login_status',
        'user_name': 'user_name',
        'attach_user_infos': 'attach_user_infos',
        'product_id': 'product_id',
        'share_resource_sku': 'share_resource_sku',
        'root_volume': 'root_volume',
        'data_volumes': 'data_volumes',
        'user_group': 'user_group',
        'availability_zone': 'availability_zone',
        'site_type': 'site_type',
        'site_name': 'site_name',
        'product': 'product',
        'ou_name': 'ou_name',
        'os_version': 'os_version',
        'sid': 'sid',
        'order_id': 'order_id',
        'tags': 'tags',
        'is_support_internet': 'is_support_internet',
        'internet_mode': 'internet_mode',
        'internet_mode_list': 'internet_mode_list',
        'is_attaching_eip': 'is_attaching_eip',
        'attach_state': 'attach_state',
        'enterprise_project_id': 'enterprise_project_id',
        'subnet_id': 'subnet_id',
        'bill_resource_id': 'bill_resource_id',
        'process': 'process',
        'root_resource_id': 'root_resource_id',
        'hour_package_info': 'hour_package_info',
        'inconsistent_types': 'inconsistent_types'
    }

    def __init__(self, desktop_id=None, computer_name=None, os_host_name=None, addresses=None, ip_addresses=None, ipv4=None, ipv6=None, user_list=None, user_group_list=None, desktop_type=None, resource_type=None, metadata=None, flavor=None, status=None, task_status=None, in_maintenance_mode=None, created=None, security_groups=None, login_status=None, user_name=None, attach_user_infos=None, product_id=None, share_resource_sku=None, root_volume=None, data_volumes=None, user_group=None, availability_zone=None, site_type=None, site_name=None, product=None, ou_name=None, os_version=None, sid=None, order_id=None, tags=None, is_support_internet=None, internet_mode=None, internet_mode_list=None, is_attaching_eip=None, attach_state=None, enterprise_project_id=None, subnet_id=None, bill_resource_id=None, process=None, root_resource_id=None, hour_package_info=None, inconsistent_types=None):
        r"""PoolDesktopsDetailInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param computer_name: 桌面名。
        :type computer_name: str
        :param os_host_name: 系统计算机名。
        :type os_host_name: str
        :param addresses: 桌面IP地址列表。
        :type addresses: dict(str, list[AddressInfo])
        :param ip_addresses: IP地址列表。
        :type ip_addresses: list[str]
        :param ipv4: 系统计算机IPV4。
        :type ipv4: str
        :param ipv6: 系统计算机IPV6。
        :type ipv6: str
        :param user_list: 用户列表。
        :type user_list: list[str]
        :param user_group_list: 用户组列表。
        :type user_group_list: list[str]
        :param desktop_type: 桌面类型。  - DEDICATED：专属桌面。
        :type desktop_type: str
        :param resource_type: resource_type字段，分别表示：专属桌面（DEDICATED_DESKTOP）、池桌面（POOLED_DESKTOP）、渲染桌面（RENDER_DESKTOP）、专享主机（EXCLUSIVE_HOST）、多用户桌面(SHARED_DESKTOP)。
        :type resource_type: str
        :param metadata: 桌面元数据。  - charging_mode 周期套餐标识，1表示包周期，0表示按需。 - image_name 创建桌面的镜像名称。 - bill_resource_id 镜像计费资源ID。 - metering.image_id 镜像ID。 - metering.resourcespeccode 桌面资源编码。 - metering.resourcetype 桌面资源类型。 - os_bit 操作系统位数：32或64。 - os_type 操作系统类型：Linux、Windows或Others。 - desktop_os_version 操作系统版本。
        :type metadata: dict(str, str)
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkworkspace.v2.FlavorInfo`
        :param status: 桌面状态。
        :type status: str
        :param task_status: 任务状态。  - scheduling：创建中，正在进行调度。 - block_device_mapping：创建中，正在准备磁盘。 - networking：创建中，正在准备网络。 - spawning：创建中，正在内部创建。 - rebooting：重启中。 - reboot_pending：重启中，正在下发重启。 - reboot_started：重启中，开始内部重启。 - rebooting_hard：强制重启中。 - reboot_pending_hard：强制重启中，正在下发重启。 - reboot_started_hard：强制重启中，开始内部重启。 - rebuilding：重建中。 - rebuild_block_device_mapping：重建中，正在准备磁盘。 - rebuild_spawning：重建中，正在内部重建。 - migrating：热迁移中。 - resize_prep：调整规格中，正在准备阶段。 - resize_migrating：调整规格中，正在迁移阶段。 - resize_migrated：调整规格中，已经完成迁移。 - resize_finish：调整规格中，正在完成调整。 - resize_reverting：调整规格中，正在回退调整。 - powering-off：停止中。 - powering-on：启动中。 - deleting：删除中。 - deleteFailed：删除失败。 - updating: 更新中。 - desktopNetworkChanging: 切换网络中。
        :type task_status: str
        :param in_maintenance_mode: 是否处于维护模式,true表示维护模式，false表示不处于维护模式。
        :type in_maintenance_mode: bool
        :param created: 桌面创建时间。
        :type created: str
        :param security_groups: 桌面安全组。
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroupInfo`]
        :param login_status: 桌面的登录状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功登录，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。
        :type login_status: str
        :param user_name: 桌面所属用户。
        :type user_name: str
        :param attach_user_infos: 桌面已分配的用户信息列表。
        :type attach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        :param product_id: 产品ID。
        :type product_id: str
        :param share_resource_sku: 桌面协同资源SKU码。
        :type share_resource_sku: str
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.VolumeDetail`
        :param data_volumes: 数据盘列表。
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.VolumeDetail`]
        :param user_group: 桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。
        :type user_group: str
        :param availability_zone: 可用分区。
        :type availability_zone: str
        :param site_type: 站点类型。
        :type site_type: str
        :param site_name: 站点名字。
        :type site_name: str
        :param product: 
        :type product: :class:`huaweicloudsdkworkspace.v2.ProductInfo`
        :param ou_name: 创建桌面时加入的OU名称。
        :type ou_name: str
        :param os_version: 操作系统版本号。
        :type os_version: str
        :param sid: SID。
        :type sid: str
        :param order_id: 包周期产品的订单ID。
        :type order_id: str
        :param tags: 桌面标签列表。
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        :param is_support_internet: 是否开通互联网，true：已开通，false：未开通。
        :type is_support_internet: bool
        :param internet_mode: 上网方式。 - NAT：表示NAT上网方式。 - EIP：表示EIP上网方式。 - BOTH：表示两种上网方式都支持。
        :type internet_mode: str
        :param internet_mode_list: 桌面使用的上网方式列表。
        :type internet_mode_list: list[str]
        :param is_attaching_eip: 桌面是否正在绑定EIP。
        :type is_attaching_eip: bool
        :param attach_state: 分配状态。 - ATTACHED：已分配。 - UNATTACH：未分配 表示未关联。 - DEATTACHED：已解分配。 - ATTACHING：分配中。 - DEATTACHING：解分配中。 - ATTACHFAIL：分配失败。 - DEATTACHFAIL：解分配失败。 - WAITING：等待被分配中,描述从批量分配（解分配）下发到转入分配（解分配）的中间状态 同时方便单个关联流程的状态独立性。 - ATTACH_FAIL_CAN_ATTACH_AGAIN：分配失败,还可以再关联。 - DEATTACH_FAIL_CAN_DEATTACH_AGAIN：解分配失败,还可以再解分配。
        :type attach_state: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param subnet_id: 桌面的子网ID。
        :type subnet_id: str
        :param bill_resource_id: 桌面计费资源ID。
        :type bill_resource_id: str
        :param process: 桌面任务进度， 取值范围0-100以及null，null表示该桌面无任务，0-100表明该任务进度的百分比。
        :type process: int
        :param root_resource_id: 整机实例根资源ID。
        :type root_resource_id: str
        :param hour_package_info: 
        :type hour_package_info: :class:`huaweicloudsdkworkspace.v2.HourPackageInfo`
        :param inconsistent_types: 桌面与桌面池不一致的规格类型: - PRODUCT: 产品ID不一致 - IMAGE: 镜像ID不一致
        :type inconsistent_types: list[str]
        """
        
        

        self._desktop_id = None
        self._computer_name = None
        self._os_host_name = None
        self._addresses = None
        self._ip_addresses = None
        self._ipv4 = None
        self._ipv6 = None
        self._user_list = None
        self._user_group_list = None
        self._desktop_type = None
        self._resource_type = None
        self._metadata = None
        self._flavor = None
        self._status = None
        self._task_status = None
        self._in_maintenance_mode = None
        self._created = None
        self._security_groups = None
        self._login_status = None
        self._user_name = None
        self._attach_user_infos = None
        self._product_id = None
        self._share_resource_sku = None
        self._root_volume = None
        self._data_volumes = None
        self._user_group = None
        self._availability_zone = None
        self._site_type = None
        self._site_name = None
        self._product = None
        self._ou_name = None
        self._os_version = None
        self._sid = None
        self._order_id = None
        self._tags = None
        self._is_support_internet = None
        self._internet_mode = None
        self._internet_mode_list = None
        self._is_attaching_eip = None
        self._attach_state = None
        self._enterprise_project_id = None
        self._subnet_id = None
        self._bill_resource_id = None
        self._process = None
        self._root_resource_id = None
        self._hour_package_info = None
        self._inconsistent_types = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if computer_name is not None:
            self.computer_name = computer_name
        if os_host_name is not None:
            self.os_host_name = os_host_name
        if addresses is not None:
            self.addresses = addresses
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if ipv4 is not None:
            self.ipv4 = ipv4
        if ipv6 is not None:
            self.ipv6 = ipv6
        if user_list is not None:
            self.user_list = user_list
        if user_group_list is not None:
            self.user_group_list = user_group_list
        if desktop_type is not None:
            self.desktop_type = desktop_type
        if resource_type is not None:
            self.resource_type = resource_type
        if metadata is not None:
            self.metadata = metadata
        if flavor is not None:
            self.flavor = flavor
        if status is not None:
            self.status = status
        if task_status is not None:
            self.task_status = task_status
        if in_maintenance_mode is not None:
            self.in_maintenance_mode = in_maintenance_mode
        if created is not None:
            self.created = created
        if security_groups is not None:
            self.security_groups = security_groups
        if login_status is not None:
            self.login_status = login_status
        if user_name is not None:
            self.user_name = user_name
        if attach_user_infos is not None:
            self.attach_user_infos = attach_user_infos
        if product_id is not None:
            self.product_id = product_id
        if share_resource_sku is not None:
            self.share_resource_sku = share_resource_sku
        if root_volume is not None:
            self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if user_group is not None:
            self.user_group = user_group
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if site_type is not None:
            self.site_type = site_type
        if site_name is not None:
            self.site_name = site_name
        if product is not None:
            self.product = product
        if ou_name is not None:
            self.ou_name = ou_name
        if os_version is not None:
            self.os_version = os_version
        if sid is not None:
            self.sid = sid
        if order_id is not None:
            self.order_id = order_id
        if tags is not None:
            self.tags = tags
        if is_support_internet is not None:
            self.is_support_internet = is_support_internet
        if internet_mode is not None:
            self.internet_mode = internet_mode
        if internet_mode_list is not None:
            self.internet_mode_list = internet_mode_list
        if is_attaching_eip is not None:
            self.is_attaching_eip = is_attaching_eip
        if attach_state is not None:
            self.attach_state = attach_state
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if bill_resource_id is not None:
            self.bill_resource_id = bill_resource_id
        if process is not None:
            self.process = process
        if root_resource_id is not None:
            self.root_resource_id = root_resource_id
        if hour_package_info is not None:
            self.hour_package_info = hour_package_info
        if inconsistent_types is not None:
            self.inconsistent_types = inconsistent_types

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this PoolDesktopsDetailInfo.

        桌面ID。

        :return: The desktop_id of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this PoolDesktopsDetailInfo.

        桌面ID。

        :param desktop_id: The desktop_id of this PoolDesktopsDetailInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def computer_name(self):
        r"""Gets the computer_name of this PoolDesktopsDetailInfo.

        桌面名。

        :return: The computer_name of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        r"""Sets the computer_name of this PoolDesktopsDetailInfo.

        桌面名。

        :param computer_name: The computer_name of this PoolDesktopsDetailInfo.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def os_host_name(self):
        r"""Gets the os_host_name of this PoolDesktopsDetailInfo.

        系统计算机名。

        :return: The os_host_name of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._os_host_name

    @os_host_name.setter
    def os_host_name(self, os_host_name):
        r"""Sets the os_host_name of this PoolDesktopsDetailInfo.

        系统计算机名。

        :param os_host_name: The os_host_name of this PoolDesktopsDetailInfo.
        :type os_host_name: str
        """
        self._os_host_name = os_host_name

    @property
    def addresses(self):
        r"""Gets the addresses of this PoolDesktopsDetailInfo.

        桌面IP地址列表。

        :return: The addresses of this PoolDesktopsDetailInfo.
        :rtype: dict(str, list[AddressInfo])
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        r"""Sets the addresses of this PoolDesktopsDetailInfo.

        桌面IP地址列表。

        :param addresses: The addresses of this PoolDesktopsDetailInfo.
        :type addresses: dict(str, list[AddressInfo])
        """
        self._addresses = addresses

    @property
    def ip_addresses(self):
        r"""Gets the ip_addresses of this PoolDesktopsDetailInfo.

        IP地址列表。

        :return: The ip_addresses of this PoolDesktopsDetailInfo.
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        r"""Sets the ip_addresses of this PoolDesktopsDetailInfo.

        IP地址列表。

        :param ip_addresses: The ip_addresses of this PoolDesktopsDetailInfo.
        :type ip_addresses: list[str]
        """
        self._ip_addresses = ip_addresses

    @property
    def ipv4(self):
        r"""Gets the ipv4 of this PoolDesktopsDetailInfo.

        系统计算机IPV4。

        :return: The ipv4 of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        r"""Sets the ipv4 of this PoolDesktopsDetailInfo.

        系统计算机IPV4。

        :param ipv4: The ipv4 of this PoolDesktopsDetailInfo.
        :type ipv4: str
        """
        self._ipv4 = ipv4

    @property
    def ipv6(self):
        r"""Gets the ipv6 of this PoolDesktopsDetailInfo.

        系统计算机IPV6。

        :return: The ipv6 of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        r"""Sets the ipv6 of this PoolDesktopsDetailInfo.

        系统计算机IPV6。

        :param ipv6: The ipv6 of this PoolDesktopsDetailInfo.
        :type ipv6: str
        """
        self._ipv6 = ipv6

    @property
    def user_list(self):
        r"""Gets the user_list of this PoolDesktopsDetailInfo.

        用户列表。

        :return: The user_list of this PoolDesktopsDetailInfo.
        :rtype: list[str]
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        r"""Sets the user_list of this PoolDesktopsDetailInfo.

        用户列表。

        :param user_list: The user_list of this PoolDesktopsDetailInfo.
        :type user_list: list[str]
        """
        self._user_list = user_list

    @property
    def user_group_list(self):
        r"""Gets the user_group_list of this PoolDesktopsDetailInfo.

        用户组列表。

        :return: The user_group_list of this PoolDesktopsDetailInfo.
        :rtype: list[str]
        """
        return self._user_group_list

    @user_group_list.setter
    def user_group_list(self, user_group_list):
        r"""Sets the user_group_list of this PoolDesktopsDetailInfo.

        用户组列表。

        :param user_group_list: The user_group_list of this PoolDesktopsDetailInfo.
        :type user_group_list: list[str]
        """
        self._user_group_list = user_group_list

    @property
    def desktop_type(self):
        r"""Gets the desktop_type of this PoolDesktopsDetailInfo.

        桌面类型。  - DEDICATED：专属桌面。

        :return: The desktop_type of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):
        r"""Sets the desktop_type of this PoolDesktopsDetailInfo.

        桌面类型。  - DEDICATED：专属桌面。

        :param desktop_type: The desktop_type of this PoolDesktopsDetailInfo.
        :type desktop_type: str
        """
        self._desktop_type = desktop_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this PoolDesktopsDetailInfo.

        resource_type字段，分别表示：专属桌面（DEDICATED_DESKTOP）、池桌面（POOLED_DESKTOP）、渲染桌面（RENDER_DESKTOP）、专享主机（EXCLUSIVE_HOST）、多用户桌面(SHARED_DESKTOP)。

        :return: The resource_type of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this PoolDesktopsDetailInfo.

        resource_type字段，分别表示：专属桌面（DEDICATED_DESKTOP）、池桌面（POOLED_DESKTOP）、渲染桌面（RENDER_DESKTOP）、专享主机（EXCLUSIVE_HOST）、多用户桌面(SHARED_DESKTOP)。

        :param resource_type: The resource_type of this PoolDesktopsDetailInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def metadata(self):
        r"""Gets the metadata of this PoolDesktopsDetailInfo.

        桌面元数据。  - charging_mode 周期套餐标识，1表示包周期，0表示按需。 - image_name 创建桌面的镜像名称。 - bill_resource_id 镜像计费资源ID。 - metering.image_id 镜像ID。 - metering.resourcespeccode 桌面资源编码。 - metering.resourcetype 桌面资源类型。 - os_bit 操作系统位数：32或64。 - os_type 操作系统类型：Linux、Windows或Others。 - desktop_os_version 操作系统版本。

        :return: The metadata of this PoolDesktopsDetailInfo.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this PoolDesktopsDetailInfo.

        桌面元数据。  - charging_mode 周期套餐标识，1表示包周期，0表示按需。 - image_name 创建桌面的镜像名称。 - bill_resource_id 镜像计费资源ID。 - metering.image_id 镜像ID。 - metering.resourcespeccode 桌面资源编码。 - metering.resourcetype 桌面资源类型。 - os_bit 操作系统位数：32或64。 - os_type 操作系统类型：Linux、Windows或Others。 - desktop_os_version 操作系统版本。

        :param metadata: The metadata of this PoolDesktopsDetailInfo.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def flavor(self):
        r"""Gets the flavor of this PoolDesktopsDetailInfo.

        :return: The flavor of this PoolDesktopsDetailInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.FlavorInfo`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this PoolDesktopsDetailInfo.

        :param flavor: The flavor of this PoolDesktopsDetailInfo.
        :type flavor: :class:`huaweicloudsdkworkspace.v2.FlavorInfo`
        """
        self._flavor = flavor

    @property
    def status(self):
        r"""Gets the status of this PoolDesktopsDetailInfo.

        桌面状态。

        :return: The status of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PoolDesktopsDetailInfo.

        桌面状态。

        :param status: The status of this PoolDesktopsDetailInfo.
        :type status: str
        """
        self._status = status

    @property
    def task_status(self):
        r"""Gets the task_status of this PoolDesktopsDetailInfo.

        任务状态。  - scheduling：创建中，正在进行调度。 - block_device_mapping：创建中，正在准备磁盘。 - networking：创建中，正在准备网络。 - spawning：创建中，正在内部创建。 - rebooting：重启中。 - reboot_pending：重启中，正在下发重启。 - reboot_started：重启中，开始内部重启。 - rebooting_hard：强制重启中。 - reboot_pending_hard：强制重启中，正在下发重启。 - reboot_started_hard：强制重启中，开始内部重启。 - rebuilding：重建中。 - rebuild_block_device_mapping：重建中，正在准备磁盘。 - rebuild_spawning：重建中，正在内部重建。 - migrating：热迁移中。 - resize_prep：调整规格中，正在准备阶段。 - resize_migrating：调整规格中，正在迁移阶段。 - resize_migrated：调整规格中，已经完成迁移。 - resize_finish：调整规格中，正在完成调整。 - resize_reverting：调整规格中，正在回退调整。 - powering-off：停止中。 - powering-on：启动中。 - deleting：删除中。 - deleteFailed：删除失败。 - updating: 更新中。 - desktopNetworkChanging: 切换网络中。

        :return: The task_status of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this PoolDesktopsDetailInfo.

        任务状态。  - scheduling：创建中，正在进行调度。 - block_device_mapping：创建中，正在准备磁盘。 - networking：创建中，正在准备网络。 - spawning：创建中，正在内部创建。 - rebooting：重启中。 - reboot_pending：重启中，正在下发重启。 - reboot_started：重启中，开始内部重启。 - rebooting_hard：强制重启中。 - reboot_pending_hard：强制重启中，正在下发重启。 - reboot_started_hard：强制重启中，开始内部重启。 - rebuilding：重建中。 - rebuild_block_device_mapping：重建中，正在准备磁盘。 - rebuild_spawning：重建中，正在内部重建。 - migrating：热迁移中。 - resize_prep：调整规格中，正在准备阶段。 - resize_migrating：调整规格中，正在迁移阶段。 - resize_migrated：调整规格中，已经完成迁移。 - resize_finish：调整规格中，正在完成调整。 - resize_reverting：调整规格中，正在回退调整。 - powering-off：停止中。 - powering-on：启动中。 - deleting：删除中。 - deleteFailed：删除失败。 - updating: 更新中。 - desktopNetworkChanging: 切换网络中。

        :param task_status: The task_status of this PoolDesktopsDetailInfo.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def in_maintenance_mode(self):
        r"""Gets the in_maintenance_mode of this PoolDesktopsDetailInfo.

        是否处于维护模式,true表示维护模式，false表示不处于维护模式。

        :return: The in_maintenance_mode of this PoolDesktopsDetailInfo.
        :rtype: bool
        """
        return self._in_maintenance_mode

    @in_maintenance_mode.setter
    def in_maintenance_mode(self, in_maintenance_mode):
        r"""Sets the in_maintenance_mode of this PoolDesktopsDetailInfo.

        是否处于维护模式,true表示维护模式，false表示不处于维护模式。

        :param in_maintenance_mode: The in_maintenance_mode of this PoolDesktopsDetailInfo.
        :type in_maintenance_mode: bool
        """
        self._in_maintenance_mode = in_maintenance_mode

    @property
    def created(self):
        r"""Gets the created of this PoolDesktopsDetailInfo.

        桌面创建时间。

        :return: The created of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this PoolDesktopsDetailInfo.

        桌面创建时间。

        :param created: The created of this PoolDesktopsDetailInfo.
        :type created: str
        """
        self._created = created

    @property
    def security_groups(self):
        r"""Gets the security_groups of this PoolDesktopsDetailInfo.

        桌面安全组。

        :return: The security_groups of this PoolDesktopsDetailInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroupInfo`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this PoolDesktopsDetailInfo.

        桌面安全组。

        :param security_groups: The security_groups of this PoolDesktopsDetailInfo.
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroupInfo`]
        """
        self._security_groups = security_groups

    @property
    def login_status(self):
        r"""Gets the login_status of this PoolDesktopsDetailInfo.

        桌面的登录状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功登录，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。

        :return: The login_status of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._login_status

    @login_status.setter
    def login_status(self, login_status):
        r"""Sets the login_status of this PoolDesktopsDetailInfo.

        桌面的登录状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功登录，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。

        :param login_status: The login_status of this PoolDesktopsDetailInfo.
        :type login_status: str
        """
        self._login_status = login_status

    @property
    def user_name(self):
        r"""Gets the user_name of this PoolDesktopsDetailInfo.

        桌面所属用户。

        :return: The user_name of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this PoolDesktopsDetailInfo.

        桌面所属用户。

        :param user_name: The user_name of this PoolDesktopsDetailInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def attach_user_infos(self):
        r"""Gets the attach_user_infos of this PoolDesktopsDetailInfo.

        桌面已分配的用户信息列表。

        :return: The attach_user_infos of this PoolDesktopsDetailInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        return self._attach_user_infos

    @attach_user_infos.setter
    def attach_user_infos(self, attach_user_infos):
        r"""Sets the attach_user_infos of this PoolDesktopsDetailInfo.

        桌面已分配的用户信息列表。

        :param attach_user_infos: The attach_user_infos of this PoolDesktopsDetailInfo.
        :type attach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        self._attach_user_infos = attach_user_infos

    @property
    def product_id(self):
        r"""Gets the product_id of this PoolDesktopsDetailInfo.

        产品ID。

        :return: The product_id of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this PoolDesktopsDetailInfo.

        产品ID。

        :param product_id: The product_id of this PoolDesktopsDetailInfo.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def share_resource_sku(self):
        r"""Gets the share_resource_sku of this PoolDesktopsDetailInfo.

        桌面协同资源SKU码。

        :return: The share_resource_sku of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._share_resource_sku

    @share_resource_sku.setter
    def share_resource_sku(self, share_resource_sku):
        r"""Sets the share_resource_sku of this PoolDesktopsDetailInfo.

        桌面协同资源SKU码。

        :param share_resource_sku: The share_resource_sku of this PoolDesktopsDetailInfo.
        :type share_resource_sku: str
        """
        self._share_resource_sku = share_resource_sku

    @property
    def root_volume(self):
        r"""Gets the root_volume of this PoolDesktopsDetailInfo.

        :return: The root_volume of this PoolDesktopsDetailInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.VolumeDetail`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this PoolDesktopsDetailInfo.

        :param root_volume: The root_volume of this PoolDesktopsDetailInfo.
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.VolumeDetail`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this PoolDesktopsDetailInfo.

        数据盘列表。

        :return: The data_volumes of this PoolDesktopsDetailInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.VolumeDetail`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this PoolDesktopsDetailInfo.

        数据盘列表。

        :param data_volumes: The data_volumes of this PoolDesktopsDetailInfo.
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.VolumeDetail`]
        """
        self._data_volumes = data_volumes

    @property
    def user_group(self):
        r"""Gets the user_group of this PoolDesktopsDetailInfo.

        桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :return: The user_group of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        r"""Sets the user_group of this PoolDesktopsDetailInfo.

        桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :param user_group: The user_group of this PoolDesktopsDetailInfo.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this PoolDesktopsDetailInfo.

        可用分区。

        :return: The availability_zone of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this PoolDesktopsDetailInfo.

        可用分区。

        :param availability_zone: The availability_zone of this PoolDesktopsDetailInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def site_type(self):
        r"""Gets the site_type of this PoolDesktopsDetailInfo.

        站点类型。

        :return: The site_type of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._site_type

    @site_type.setter
    def site_type(self, site_type):
        r"""Sets the site_type of this PoolDesktopsDetailInfo.

        站点类型。

        :param site_type: The site_type of this PoolDesktopsDetailInfo.
        :type site_type: str
        """
        self._site_type = site_type

    @property
    def site_name(self):
        r"""Gets the site_name of this PoolDesktopsDetailInfo.

        站点名字。

        :return: The site_name of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        r"""Sets the site_name of this PoolDesktopsDetailInfo.

        站点名字。

        :param site_name: The site_name of this PoolDesktopsDetailInfo.
        :type site_name: str
        """
        self._site_name = site_name

    @property
    def product(self):
        r"""Gets the product of this PoolDesktopsDetailInfo.

        :return: The product of this PoolDesktopsDetailInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ProductInfo`
        """
        return self._product

    @product.setter
    def product(self, product):
        r"""Sets the product of this PoolDesktopsDetailInfo.

        :param product: The product of this PoolDesktopsDetailInfo.
        :type product: :class:`huaweicloudsdkworkspace.v2.ProductInfo`
        """
        self._product = product

    @property
    def ou_name(self):
        r"""Gets the ou_name of this PoolDesktopsDetailInfo.

        创建桌面时加入的OU名称。

        :return: The ou_name of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        r"""Sets the ou_name of this PoolDesktopsDetailInfo.

        创建桌面时加入的OU名称。

        :param ou_name: The ou_name of this PoolDesktopsDetailInfo.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def os_version(self):
        r"""Gets the os_version of this PoolDesktopsDetailInfo.

        操作系统版本号。

        :return: The os_version of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this PoolDesktopsDetailInfo.

        操作系统版本号。

        :param os_version: The os_version of this PoolDesktopsDetailInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def sid(self):
        r"""Gets the sid of this PoolDesktopsDetailInfo.

        SID。

        :return: The sid of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        r"""Sets the sid of this PoolDesktopsDetailInfo.

        SID。

        :param sid: The sid of this PoolDesktopsDetailInfo.
        :type sid: str
        """
        self._sid = sid

    @property
    def order_id(self):
        r"""Gets the order_id of this PoolDesktopsDetailInfo.

        包周期产品的订单ID。

        :return: The order_id of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this PoolDesktopsDetailInfo.

        包周期产品的订单ID。

        :param order_id: The order_id of this PoolDesktopsDetailInfo.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def tags(self):
        r"""Gets the tags of this PoolDesktopsDetailInfo.

        桌面标签列表。

        :return: The tags of this PoolDesktopsDetailInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this PoolDesktopsDetailInfo.

        桌面标签列表。

        :param tags: The tags of this PoolDesktopsDetailInfo.
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        self._tags = tags

    @property
    def is_support_internet(self):
        r"""Gets the is_support_internet of this PoolDesktopsDetailInfo.

        是否开通互联网，true：已开通，false：未开通。

        :return: The is_support_internet of this PoolDesktopsDetailInfo.
        :rtype: bool
        """
        return self._is_support_internet

    @is_support_internet.setter
    def is_support_internet(self, is_support_internet):
        r"""Sets the is_support_internet of this PoolDesktopsDetailInfo.

        是否开通互联网，true：已开通，false：未开通。

        :param is_support_internet: The is_support_internet of this PoolDesktopsDetailInfo.
        :type is_support_internet: bool
        """
        self._is_support_internet = is_support_internet

    @property
    def internet_mode(self):
        r"""Gets the internet_mode of this PoolDesktopsDetailInfo.

        上网方式。 - NAT：表示NAT上网方式。 - EIP：表示EIP上网方式。 - BOTH：表示两种上网方式都支持。

        :return: The internet_mode of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._internet_mode

    @internet_mode.setter
    def internet_mode(self, internet_mode):
        r"""Sets the internet_mode of this PoolDesktopsDetailInfo.

        上网方式。 - NAT：表示NAT上网方式。 - EIP：表示EIP上网方式。 - BOTH：表示两种上网方式都支持。

        :param internet_mode: The internet_mode of this PoolDesktopsDetailInfo.
        :type internet_mode: str
        """
        self._internet_mode = internet_mode

    @property
    def internet_mode_list(self):
        r"""Gets the internet_mode_list of this PoolDesktopsDetailInfo.

        桌面使用的上网方式列表。

        :return: The internet_mode_list of this PoolDesktopsDetailInfo.
        :rtype: list[str]
        """
        return self._internet_mode_list

    @internet_mode_list.setter
    def internet_mode_list(self, internet_mode_list):
        r"""Sets the internet_mode_list of this PoolDesktopsDetailInfo.

        桌面使用的上网方式列表。

        :param internet_mode_list: The internet_mode_list of this PoolDesktopsDetailInfo.
        :type internet_mode_list: list[str]
        """
        self._internet_mode_list = internet_mode_list

    @property
    def is_attaching_eip(self):
        r"""Gets the is_attaching_eip of this PoolDesktopsDetailInfo.

        桌面是否正在绑定EIP。

        :return: The is_attaching_eip of this PoolDesktopsDetailInfo.
        :rtype: bool
        """
        return self._is_attaching_eip

    @is_attaching_eip.setter
    def is_attaching_eip(self, is_attaching_eip):
        r"""Sets the is_attaching_eip of this PoolDesktopsDetailInfo.

        桌面是否正在绑定EIP。

        :param is_attaching_eip: The is_attaching_eip of this PoolDesktopsDetailInfo.
        :type is_attaching_eip: bool
        """
        self._is_attaching_eip = is_attaching_eip

    @property
    def attach_state(self):
        r"""Gets the attach_state of this PoolDesktopsDetailInfo.

        分配状态。 - ATTACHED：已分配。 - UNATTACH：未分配 表示未关联。 - DEATTACHED：已解分配。 - ATTACHING：分配中。 - DEATTACHING：解分配中。 - ATTACHFAIL：分配失败。 - DEATTACHFAIL：解分配失败。 - WAITING：等待被分配中,描述从批量分配（解分配）下发到转入分配（解分配）的中间状态 同时方便单个关联流程的状态独立性。 - ATTACH_FAIL_CAN_ATTACH_AGAIN：分配失败,还可以再关联。 - DEATTACH_FAIL_CAN_DEATTACH_AGAIN：解分配失败,还可以再解分配。

        :return: The attach_state of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._attach_state

    @attach_state.setter
    def attach_state(self, attach_state):
        r"""Sets the attach_state of this PoolDesktopsDetailInfo.

        分配状态。 - ATTACHED：已分配。 - UNATTACH：未分配 表示未关联。 - DEATTACHED：已解分配。 - ATTACHING：分配中。 - DEATTACHING：解分配中。 - ATTACHFAIL：分配失败。 - DEATTACHFAIL：解分配失败。 - WAITING：等待被分配中,描述从批量分配（解分配）下发到转入分配（解分配）的中间状态 同时方便单个关联流程的状态独立性。 - ATTACH_FAIL_CAN_ATTACH_AGAIN：分配失败,还可以再关联。 - DEATTACH_FAIL_CAN_DEATTACH_AGAIN：解分配失败,还可以再解分配。

        :param attach_state: The attach_state of this PoolDesktopsDetailInfo.
        :type attach_state: str
        """
        self._attach_state = attach_state

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this PoolDesktopsDetailInfo.

        企业项目ID。

        :return: The enterprise_project_id of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this PoolDesktopsDetailInfo.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this PoolDesktopsDetailInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this PoolDesktopsDetailInfo.

        桌面的子网ID。

        :return: The subnet_id of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this PoolDesktopsDetailInfo.

        桌面的子网ID。

        :param subnet_id: The subnet_id of this PoolDesktopsDetailInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def bill_resource_id(self):
        r"""Gets the bill_resource_id of this PoolDesktopsDetailInfo.

        桌面计费资源ID。

        :return: The bill_resource_id of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._bill_resource_id

    @bill_resource_id.setter
    def bill_resource_id(self, bill_resource_id):
        r"""Sets the bill_resource_id of this PoolDesktopsDetailInfo.

        桌面计费资源ID。

        :param bill_resource_id: The bill_resource_id of this PoolDesktopsDetailInfo.
        :type bill_resource_id: str
        """
        self._bill_resource_id = bill_resource_id

    @property
    def process(self):
        r"""Gets the process of this PoolDesktopsDetailInfo.

        桌面任务进度， 取值范围0-100以及null，null表示该桌面无任务，0-100表明该任务进度的百分比。

        :return: The process of this PoolDesktopsDetailInfo.
        :rtype: int
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this PoolDesktopsDetailInfo.

        桌面任务进度， 取值范围0-100以及null，null表示该桌面无任务，0-100表明该任务进度的百分比。

        :param process: The process of this PoolDesktopsDetailInfo.
        :type process: int
        """
        self._process = process

    @property
    def root_resource_id(self):
        r"""Gets the root_resource_id of this PoolDesktopsDetailInfo.

        整机实例根资源ID。

        :return: The root_resource_id of this PoolDesktopsDetailInfo.
        :rtype: str
        """
        return self._root_resource_id

    @root_resource_id.setter
    def root_resource_id(self, root_resource_id):
        r"""Sets the root_resource_id of this PoolDesktopsDetailInfo.

        整机实例根资源ID。

        :param root_resource_id: The root_resource_id of this PoolDesktopsDetailInfo.
        :type root_resource_id: str
        """
        self._root_resource_id = root_resource_id

    @property
    def hour_package_info(self):
        r"""Gets the hour_package_info of this PoolDesktopsDetailInfo.

        :return: The hour_package_info of this PoolDesktopsDetailInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.HourPackageInfo`
        """
        return self._hour_package_info

    @hour_package_info.setter
    def hour_package_info(self, hour_package_info):
        r"""Sets the hour_package_info of this PoolDesktopsDetailInfo.

        :param hour_package_info: The hour_package_info of this PoolDesktopsDetailInfo.
        :type hour_package_info: :class:`huaweicloudsdkworkspace.v2.HourPackageInfo`
        """
        self._hour_package_info = hour_package_info

    @property
    def inconsistent_types(self):
        r"""Gets the inconsistent_types of this PoolDesktopsDetailInfo.

        桌面与桌面池不一致的规格类型: - PRODUCT: 产品ID不一致 - IMAGE: 镜像ID不一致

        :return: The inconsistent_types of this PoolDesktopsDetailInfo.
        :rtype: list[str]
        """
        return self._inconsistent_types

    @inconsistent_types.setter
    def inconsistent_types(self, inconsistent_types):
        r"""Sets the inconsistent_types of this PoolDesktopsDetailInfo.

        桌面与桌面池不一致的规格类型: - PRODUCT: 产品ID不一致 - IMAGE: 镜像ID不一致

        :param inconsistent_types: The inconsistent_types of this PoolDesktopsDetailInfo.
        :type inconsistent_types: list[str]
        """
        self._inconsistent_types = inconsistent_types

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
        if not isinstance(other, PoolDesktopsDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
