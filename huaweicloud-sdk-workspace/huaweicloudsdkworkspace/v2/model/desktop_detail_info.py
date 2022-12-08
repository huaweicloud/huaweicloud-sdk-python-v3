# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopDetailInfo:

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
        'addresses': 'dict(str, list[AddressInfo])',
        'ip_addresses': 'list[str]',
        'desktop_type': 'str',
        'metadata': 'dict(str, str)',
        'flavor': 'FlavorInfo',
        'status': 'str',
        'task_status': 'str',
        'created': 'str',
        'security_groups': 'list[SecurityGroupInfo]',
        'login_status': 'str',
        'user_name': 'str',
        'product_id': 'str',
        'root_volume': 'VolumeDetail',
        'data_volumes': 'list[VolumeDetail]',
        'user_group': 'str',
        'availability_zone': 'str',
        'site_type': 'str',
        'site_name': 'str',
        'product': 'ProductDetailInfo',
        'ou_name': 'str',
        'os_version': 'str',
        'sid': 'str',
        'order_id': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'computer_name': 'computer_name',
        'addresses': 'addresses',
        'ip_addresses': 'ip_addresses',
        'desktop_type': 'desktop_type',
        'metadata': 'metadata',
        'flavor': 'flavor',
        'status': 'status',
        'task_status': 'task_status',
        'created': 'created',
        'security_groups': 'security_groups',
        'login_status': 'login_status',
        'user_name': 'user_name',
        'product_id': 'product_id',
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
        'tags': 'tags'
    }

    def __init__(self, desktop_id=None, computer_name=None, addresses=None, ip_addresses=None, desktop_type=None, metadata=None, flavor=None, status=None, task_status=None, created=None, security_groups=None, login_status=None, user_name=None, product_id=None, root_volume=None, data_volumes=None, user_group=None, availability_zone=None, site_type=None, site_name=None, product=None, ou_name=None, os_version=None, sid=None, order_id=None, tags=None):
        """DesktopDetailInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param computer_name: 桌面名。
        :type computer_name: str
        :param addresses: 桌面IP地址列表。
        :type addresses: dict(str, list[AddressInfo])
        :param ip_addresses: IP地址列表。
        :type ip_addresses: list[str]
        :param desktop_type: 桌面类型。  - DEDICATED：专属桌面。
        :type desktop_type: str
        :param metadata: 桌面元数据。  - charging_mode 周期套餐标识，1表示包周期，0表示按需。 - image_name 创建桌面的镜像名称。 - metering.image_id 镜像ID。 - metering.resourcespeccode 桌面资源编码。 - metering.resourcetype 桌面资源类型。 - os_bit 操作系统位数：32或64。 - os_type 操作系统类型：Linux、Windows或Others。 - desktop_os_version 操作系统版本。
        :type metadata: dict(str, str)
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkworkspace.v2.FlavorInfo`
        :param status: 桌面状态。
        :type status: str
        :param task_status: 任务状态。  - scheduling：创建中，正在进行调度。 - block_device_mapping：创建中，正在准备磁盘。 - networking：创建中，正在准备网络。 - spawning：创建中，正在内部创建。 - rebooting：重启中。 - reboot_pending：重启中，正在下发重启。 - reboot_started：重启中，开始内部重启。 - rebooting_hard：强制重启中。 - reboot_pending_hard：强制重启中，正在下发重启。 - reboot_started_hard：强制重启中，开始内部重启。 - rebuilding：重建中。 - rebuild_block_device_mapping：重建中，正在准备磁盘。 - rebuild_spawning：重建中，正在内部重建。 - migrating：热迁移中。 - resize_prep：调整规格中，正在准备阶段。 - resize_migrating：调整规格中，正在迁移阶段。 - resize_migrated：调整规格中，已经完成迁移。 - resize_finish：调整规格中，正在完成调整。 - resize_reverting：调整规格中，正在回退调整。 - powering-off：停止中。 - powering-on：启动中。 - deleting：删除中。 - deleteFailed：删除失败。
        :type task_status: str
        :param created: 桌面创建时间。
        :type created: str
        :param security_groups: 桌面安全组。
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroupInfo`]
        :param login_status: 桌面的登录状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功登录，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。
        :type login_status: str
        :param user_name: 桌面所属用户。
        :type user_name: str
        :param product_id: 产品ID。
        :type product_id: str
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.VolumeDetail`
        :param data_volumes: 数据盘列表。
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.VolumeDetail`]
        :param user_group: 桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。
        :type user_group: str
        :param availability_zone: 可用分区。
        :type availability_zone: str
        :param site_type: 站点类型
        :type site_type: str
        :param site_name: 站点名字
        :type site_name: str
        :param product: 
        :type product: :class:`huaweicloudsdkworkspace.v2.ProductDetailInfo`
        :param ou_name: 创建桌面时加入的OU名称。
        :type ou_name: str
        :param os_version: 操作系统版本号。
        :type os_version: str
        :param sid: SID
        :type sid: str
        :param order_id: 包周期产品的订单ID。
        :type order_id: str
        :param tags: 桌面标签列表。
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        
        

        self._desktop_id = None
        self._computer_name = None
        self._addresses = None
        self._ip_addresses = None
        self._desktop_type = None
        self._metadata = None
        self._flavor = None
        self._status = None
        self._task_status = None
        self._created = None
        self._security_groups = None
        self._login_status = None
        self._user_name = None
        self._product_id = None
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
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if computer_name is not None:
            self.computer_name = computer_name
        if addresses is not None:
            self.addresses = addresses
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if desktop_type is not None:
            self.desktop_type = desktop_type
        if metadata is not None:
            self.metadata = metadata
        if flavor is not None:
            self.flavor = flavor
        if status is not None:
            self.status = status
        if task_status is not None:
            self.task_status = task_status
        if created is not None:
            self.created = created
        if security_groups is not None:
            self.security_groups = security_groups
        if login_status is not None:
            self.login_status = login_status
        if user_name is not None:
            self.user_name = user_name
        if product_id is not None:
            self.product_id = product_id
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

    @property
    def desktop_id(self):
        """Gets the desktop_id of this DesktopDetailInfo.

        桌面ID。

        :return: The desktop_id of this DesktopDetailInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this DesktopDetailInfo.

        桌面ID。

        :param desktop_id: The desktop_id of this DesktopDetailInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def computer_name(self):
        """Gets the computer_name of this DesktopDetailInfo.

        桌面名。

        :return: The computer_name of this DesktopDetailInfo.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this DesktopDetailInfo.

        桌面名。

        :param computer_name: The computer_name of this DesktopDetailInfo.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def addresses(self):
        """Gets the addresses of this DesktopDetailInfo.

        桌面IP地址列表。

        :return: The addresses of this DesktopDetailInfo.
        :rtype: dict(str, list[AddressInfo])
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this DesktopDetailInfo.

        桌面IP地址列表。

        :param addresses: The addresses of this DesktopDetailInfo.
        :type addresses: dict(str, list[AddressInfo])
        """
        self._addresses = addresses

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this DesktopDetailInfo.

        IP地址列表。

        :return: The ip_addresses of this DesktopDetailInfo.
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this DesktopDetailInfo.

        IP地址列表。

        :param ip_addresses: The ip_addresses of this DesktopDetailInfo.
        :type ip_addresses: list[str]
        """
        self._ip_addresses = ip_addresses

    @property
    def desktop_type(self):
        """Gets the desktop_type of this DesktopDetailInfo.

        桌面类型。  - DEDICATED：专属桌面。

        :return: The desktop_type of this DesktopDetailInfo.
        :rtype: str
        """
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):
        """Sets the desktop_type of this DesktopDetailInfo.

        桌面类型。  - DEDICATED：专属桌面。

        :param desktop_type: The desktop_type of this DesktopDetailInfo.
        :type desktop_type: str
        """
        self._desktop_type = desktop_type

    @property
    def metadata(self):
        """Gets the metadata of this DesktopDetailInfo.

        桌面元数据。  - charging_mode 周期套餐标识，1表示包周期，0表示按需。 - image_name 创建桌面的镜像名称。 - metering.image_id 镜像ID。 - metering.resourcespeccode 桌面资源编码。 - metering.resourcetype 桌面资源类型。 - os_bit 操作系统位数：32或64。 - os_type 操作系统类型：Linux、Windows或Others。 - desktop_os_version 操作系统版本。

        :return: The metadata of this DesktopDetailInfo.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DesktopDetailInfo.

        桌面元数据。  - charging_mode 周期套餐标识，1表示包周期，0表示按需。 - image_name 创建桌面的镜像名称。 - metering.image_id 镜像ID。 - metering.resourcespeccode 桌面资源编码。 - metering.resourcetype 桌面资源类型。 - os_bit 操作系统位数：32或64。 - os_type 操作系统类型：Linux、Windows或Others。 - desktop_os_version 操作系统版本。

        :param metadata: The metadata of this DesktopDetailInfo.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def flavor(self):
        """Gets the flavor of this DesktopDetailInfo.

        :return: The flavor of this DesktopDetailInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.FlavorInfo`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this DesktopDetailInfo.

        :param flavor: The flavor of this DesktopDetailInfo.
        :type flavor: :class:`huaweicloudsdkworkspace.v2.FlavorInfo`
        """
        self._flavor = flavor

    @property
    def status(self):
        """Gets the status of this DesktopDetailInfo.

        桌面状态。

        :return: The status of this DesktopDetailInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DesktopDetailInfo.

        桌面状态。

        :param status: The status of this DesktopDetailInfo.
        :type status: str
        """
        self._status = status

    @property
    def task_status(self):
        """Gets the task_status of this DesktopDetailInfo.

        任务状态。  - scheduling：创建中，正在进行调度。 - block_device_mapping：创建中，正在准备磁盘。 - networking：创建中，正在准备网络。 - spawning：创建中，正在内部创建。 - rebooting：重启中。 - reboot_pending：重启中，正在下发重启。 - reboot_started：重启中，开始内部重启。 - rebooting_hard：强制重启中。 - reboot_pending_hard：强制重启中，正在下发重启。 - reboot_started_hard：强制重启中，开始内部重启。 - rebuilding：重建中。 - rebuild_block_device_mapping：重建中，正在准备磁盘。 - rebuild_spawning：重建中，正在内部重建。 - migrating：热迁移中。 - resize_prep：调整规格中，正在准备阶段。 - resize_migrating：调整规格中，正在迁移阶段。 - resize_migrated：调整规格中，已经完成迁移。 - resize_finish：调整规格中，正在完成调整。 - resize_reverting：调整规格中，正在回退调整。 - powering-off：停止中。 - powering-on：启动中。 - deleting：删除中。 - deleteFailed：删除失败。

        :return: The task_status of this DesktopDetailInfo.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this DesktopDetailInfo.

        任务状态。  - scheduling：创建中，正在进行调度。 - block_device_mapping：创建中，正在准备磁盘。 - networking：创建中，正在准备网络。 - spawning：创建中，正在内部创建。 - rebooting：重启中。 - reboot_pending：重启中，正在下发重启。 - reboot_started：重启中，开始内部重启。 - rebooting_hard：强制重启中。 - reboot_pending_hard：强制重启中，正在下发重启。 - reboot_started_hard：强制重启中，开始内部重启。 - rebuilding：重建中。 - rebuild_block_device_mapping：重建中，正在准备磁盘。 - rebuild_spawning：重建中，正在内部重建。 - migrating：热迁移中。 - resize_prep：调整规格中，正在准备阶段。 - resize_migrating：调整规格中，正在迁移阶段。 - resize_migrated：调整规格中，已经完成迁移。 - resize_finish：调整规格中，正在完成调整。 - resize_reverting：调整规格中，正在回退调整。 - powering-off：停止中。 - powering-on：启动中。 - deleting：删除中。 - deleteFailed：删除失败。

        :param task_status: The task_status of this DesktopDetailInfo.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def created(self):
        """Gets the created of this DesktopDetailInfo.

        桌面创建时间。

        :return: The created of this DesktopDetailInfo.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DesktopDetailInfo.

        桌面创建时间。

        :param created: The created of this DesktopDetailInfo.
        :type created: str
        """
        self._created = created

    @property
    def security_groups(self):
        """Gets the security_groups of this DesktopDetailInfo.

        桌面安全组。

        :return: The security_groups of this DesktopDetailInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroupInfo`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this DesktopDetailInfo.

        桌面安全组。

        :param security_groups: The security_groups of this DesktopDetailInfo.
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroupInfo`]
        """
        self._security_groups = security_groups

    @property
    def login_status(self):
        """Gets the login_status of this DesktopDetailInfo.

        桌面的登录状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功登录，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。

        :return: The login_status of this DesktopDetailInfo.
        :rtype: str
        """
        return self._login_status

    @login_status.setter
    def login_status(self, login_status):
        """Sets the login_status of this DesktopDetailInfo.

        桌面的登录状态。  - UNREGISTER：表示桌面未注册时的状态（桌面启动后，会自动注册）。关机后也会出现未注册的状态。 - REGISTERED：表示桌面注册以后，等待用户连接的状态。 - CONNECTED：表示用户已经成功登录，正在使用桌面。 - DISCONNECTED：表示桌面与客户端断开会话后显示的状态，可能为关闭客户端窗口，或客户端与桌面网络断开引起。

        :param login_status: The login_status of this DesktopDetailInfo.
        :type login_status: str
        """
        self._login_status = login_status

    @property
    def user_name(self):
        """Gets the user_name of this DesktopDetailInfo.

        桌面所属用户。

        :return: The user_name of this DesktopDetailInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this DesktopDetailInfo.

        桌面所属用户。

        :param user_name: The user_name of this DesktopDetailInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def product_id(self):
        """Gets the product_id of this DesktopDetailInfo.

        产品ID。

        :return: The product_id of this DesktopDetailInfo.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this DesktopDetailInfo.

        产品ID。

        :param product_id: The product_id of this DesktopDetailInfo.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def root_volume(self):
        """Gets the root_volume of this DesktopDetailInfo.

        :return: The root_volume of this DesktopDetailInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.VolumeDetail`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this DesktopDetailInfo.

        :param root_volume: The root_volume of this DesktopDetailInfo.
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.VolumeDetail`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        """Gets the data_volumes of this DesktopDetailInfo.

        数据盘列表。

        :return: The data_volumes of this DesktopDetailInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.VolumeDetail`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this DesktopDetailInfo.

        数据盘列表。

        :param data_volumes: The data_volumes of this DesktopDetailInfo.
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.VolumeDetail`]
        """
        self._data_volumes = data_volumes

    @property
    def user_group(self):
        """Gets the user_group of this DesktopDetailInfo.

        桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :return: The user_group of this DesktopDetailInfo.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this DesktopDetailInfo.

        桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :param user_group: The user_group of this DesktopDetailInfo.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def availability_zone(self):
        """Gets the availability_zone of this DesktopDetailInfo.

        可用分区。

        :return: The availability_zone of this DesktopDetailInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this DesktopDetailInfo.

        可用分区。

        :param availability_zone: The availability_zone of this DesktopDetailInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def site_type(self):
        """Gets the site_type of this DesktopDetailInfo.

        站点类型

        :return: The site_type of this DesktopDetailInfo.
        :rtype: str
        """
        return self._site_type

    @site_type.setter
    def site_type(self, site_type):
        """Sets the site_type of this DesktopDetailInfo.

        站点类型

        :param site_type: The site_type of this DesktopDetailInfo.
        :type site_type: str
        """
        self._site_type = site_type

    @property
    def site_name(self):
        """Gets the site_name of this DesktopDetailInfo.

        站点名字

        :return: The site_name of this DesktopDetailInfo.
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        """Sets the site_name of this DesktopDetailInfo.

        站点名字

        :param site_name: The site_name of this DesktopDetailInfo.
        :type site_name: str
        """
        self._site_name = site_name

    @property
    def product(self):
        """Gets the product of this DesktopDetailInfo.

        :return: The product of this DesktopDetailInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ProductDetailInfo`
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this DesktopDetailInfo.

        :param product: The product of this DesktopDetailInfo.
        :type product: :class:`huaweicloudsdkworkspace.v2.ProductDetailInfo`
        """
        self._product = product

    @property
    def ou_name(self):
        """Gets the ou_name of this DesktopDetailInfo.

        创建桌面时加入的OU名称。

        :return: The ou_name of this DesktopDetailInfo.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        """Sets the ou_name of this DesktopDetailInfo.

        创建桌面时加入的OU名称。

        :param ou_name: The ou_name of this DesktopDetailInfo.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def os_version(self):
        """Gets the os_version of this DesktopDetailInfo.

        操作系统版本号。

        :return: The os_version of this DesktopDetailInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this DesktopDetailInfo.

        操作系统版本号。

        :param os_version: The os_version of this DesktopDetailInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def sid(self):
        """Gets the sid of this DesktopDetailInfo.

        SID

        :return: The sid of this DesktopDetailInfo.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this DesktopDetailInfo.

        SID

        :param sid: The sid of this DesktopDetailInfo.
        :type sid: str
        """
        self._sid = sid

    @property
    def order_id(self):
        """Gets the order_id of this DesktopDetailInfo.

        包周期产品的订单ID。

        :return: The order_id of this DesktopDetailInfo.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this DesktopDetailInfo.

        包周期产品的订单ID。

        :param order_id: The order_id of this DesktopDetailInfo.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def tags(self):
        """Gets the tags of this DesktopDetailInfo.

        桌面标签列表。

        :return: The tags of this DesktopDetailInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DesktopDetailInfo.

        桌面标签列表。

        :param tags: The tags of this DesktopDetailInfo.
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
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
        if not isinstance(other, DesktopDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
