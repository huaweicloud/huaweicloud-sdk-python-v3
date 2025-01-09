# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDesktopReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_type': 'str',
        'availability_zone': 'str',
        'product_id': 'str',
        'flavor_id': 'str',
        'share_resource_sku': 'str',
        'image_type': 'str',
        'image_id': 'str',
        'root_volume': 'Volume',
        'data_volumes': 'list[Volume]',
        'nics': 'list[Nic]',
        'security_groups': 'list[SecurityGroup]',
        'desktops': 'list[Desktop]',
        'desktop_name': 'str',
        'desktop_ips': 'list[str]',
        'size': 'int',
        'email_notification': 'bool',
        'enterprise_id': 'str',
        'enterprise_project_id': 'str',
        'order_id': 'str',
        'ou_name': 'str',
        'vpc_id': 'str',
        'subnet_ids': 'list[str]',
        'tags': 'list[Tag]',
        'scheduler_hints': 'WdhParam',
        'desktop_isv': 'str',
        'access_mode': 'str',
        'apply_shared_vpc_dedicated_param': 'ApplySharedVpcDedicatedParam',
        'dedicated_subnets': 'str',
        'eip': 'Eip',
        'adn': 'Adn',
        'exclusive_host_id': 'str',
        'desktop_name_policy_id': 'str',
        'hour_package_product_id': 'str',
        'hour_package_offering_id': 'str',
        'root_resource_ids': 'list[str]',
        'inst_info_ids': 'list[str]'
    }

    attribute_map = {
        'desktop_type': 'desktop_type',
        'availability_zone': 'availability_zone',
        'product_id': 'product_id',
        'flavor_id': 'flavor_id',
        'share_resource_sku': 'share_resource_sku',
        'image_type': 'image_type',
        'image_id': 'image_id',
        'root_volume': 'root_volume',
        'data_volumes': 'data_volumes',
        'nics': 'nics',
        'security_groups': 'security_groups',
        'desktops': 'desktops',
        'desktop_name': 'desktop_name',
        'desktop_ips': 'desktop_ips',
        'size': 'size',
        'email_notification': 'email_notification',
        'enterprise_id': 'enterprise_id',
        'enterprise_project_id': 'enterprise_project_id',
        'order_id': 'order_id',
        'ou_name': 'ou_name',
        'vpc_id': 'vpc_id',
        'subnet_ids': 'subnet_ids',
        'tags': 'tags',
        'scheduler_hints': 'scheduler_hints',
        'desktop_isv': 'desktop_isv',
        'access_mode': 'access_mode',
        'apply_shared_vpc_dedicated_param': 'apply_shared_vpc_dedicated_param',
        'dedicated_subnets': 'dedicated_subnets',
        'eip': 'eip',
        'adn': 'adn',
        'exclusive_host_id': 'exclusive_host_id',
        'desktop_name_policy_id': 'desktop_name_policy_id',
        'hour_package_product_id': 'hour_package_product_id',
        'hour_package_offering_id': 'hour_package_offering_id',
        'root_resource_ids': 'root_resource_ids',
        'inst_info_ids': 'inst_info_ids'
    }

    def __init__(self, desktop_type=None, availability_zone=None, product_id=None, flavor_id=None, share_resource_sku=None, image_type=None, image_id=None, root_volume=None, data_volumes=None, nics=None, security_groups=None, desktops=None, desktop_name=None, desktop_ips=None, size=None, email_notification=None, enterprise_id=None, enterprise_project_id=None, order_id=None, ou_name=None, vpc_id=None, subnet_ids=None, tags=None, scheduler_hints=None, desktop_isv=None, access_mode=None, apply_shared_vpc_dedicated_param=None, dedicated_subnets=None, eip=None, adn=None, exclusive_host_id=None, desktop_name_policy_id=None, hour_package_product_id=None, hour_package_offering_id=None, root_resource_ids=None, inst_info_ids=None):
        """CreateDesktopReq

        The model defined in huaweicloud sdk

        :param desktop_type: 云桌面类型。 - DEDICATED：专属桌面，单用户。 - SHARED: 多用户共享桌面。
        :type desktop_type: str
        :param availability_zone: 可用分区。将桌面创建到指定的可用分区。如果不指定则使用系统随机的可用分区。
        :type availability_zone: str
        :param product_id: 套餐ID。
        :type product_id: str
        :param flavor_id: 套餐flavorID。
        :type flavor_id: str
        :param share_resource_sku: 桌面协同资源SKU码
        :type share_resource_sku: str
        :param image_type: 镜像类型。默认值为private。  - private：私有镜像。 - gold：公共镜像。
        :type image_type: str
        :param image_id: 镜像ID，用于私有镜像创建桌面场景，配合product_id使用。
        :type image_id: str
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.Volume`
        :param data_volumes: 数据盘列表。
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        :param nics: 桌面对应的网卡信息，如果不指定则使用默认网卡。
        :type nics: list[:class:`huaweicloudsdkworkspace.v2.Nic`]
        :param security_groups: 桌面使用的安全组，如果不指定则默认使用桌面代理中指定的安全组。
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroup`]
        :param desktops: 创建桌面使用的参数列表。长度为1-100。  当前不支持一批桌面不同配置，所有桌面的配置和第一台的一致，如果第一台未设置参数，则取外层的同名参数。
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.Desktop`]
        :param desktop_name: 搭配size使用，当size为1时代表桌面名，位数1-15，当size大于1时代表桌面名前缀，位数：1-13。
        :type desktop_name: str
        :param desktop_ips: 桌面指定分配的ip地址列表,最小为0，最大为100。
        :type desktop_ips: list[str]
        :param size: 创建不分配用户的桌面的个数，和desktops不能同时生效，搭配desktop_name使用。
        :type size: int
        :param email_notification: 创建成功后是否发送邮件通知桌面用户，默认为true。
        :type email_notification: bool
        :param enterprise_id: 企业ID，在非对接AD场景首次创建桌面时使用。
        :type enterprise_id: str
        :param enterprise_project_id: 企业项目ID，默认\&quot;0\&quot;
        :type enterprise_project_id: str
        :param order_id: 包周期订购ID，CBC订购回调时使用。
        :type order_id: str
        :param ou_name: OU名称，在对接AD时使用，需提前在AD中创建OU。
        :type ou_name: str
        :param vpc_id: 在非对接AD场景首次创建桌面时使用。
        :type vpc_id: str
        :param subnet_ids: 在非对接AD场景首次创建桌面时使用。
        :type subnet_ids: list[str]
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        :param scheduler_hints: 
        :type scheduler_hints: :class:`huaweicloudsdkworkspace.v2.WdhParam`
        :param desktop_isv: 桌面来源。  - DEFAULT：默认桌面来源 - ONEMOBILE：协同办公云桌面OneMobile
        :type desktop_isv: str
        :param access_mode: 接入模式。在非对接AD场景首次创建桌面时使用。 - INTERNET：互联网接入。 - DEDICATED：专线接入。 - BOTH：代表两种接入方式都支持。
        :type access_mode: str
        :param apply_shared_vpc_dedicated_param: 
        :type apply_shared_vpc_dedicated_param: :class:`huaweicloudsdkworkspace.v2.ApplySharedVpcDedicatedParam`
        :param dedicated_subnets: 专线接入网段列表，多个网段信息用分号隔开，列表长度不超过5。在非对接AD场景首次创建桌面时使用。
        :type dedicated_subnets: str
        :param eip: 
        :type eip: :class:`huaweicloudsdkworkspace.v2.Eip`
        :param adn: 
        :type adn: :class:`huaweicloudsdkworkspace.v2.Adn`
        :param exclusive_host_id: 专享主机ID，创建专享桌面时如果在指定专享主机中创建则必选
        :type exclusive_host_id: str
        :param desktop_name_policy_id: 策略id，用于指定生成桌面名称策略，如果指定了桌面名称则优先使用指定的桌面名称。
        :type desktop_name_policy_id: str
        :param hour_package_product_id: 桌面小时包套餐ID。
        :type hour_package_product_id: str
        :param hour_package_offering_id: 桌面小时包offeringID。
        :type hour_package_offering_id: str
        :param root_resource_ids: 根资源ID列表，创建小时包桌面时使用，最小为0，最大为100。
        :type root_resource_ids: list[str]
        :param inst_info_ids: instInfoId列表，创建小时包桌面时使用，最小为0，最大为100。
        :type inst_info_ids: list[str]
        """
        
        

        self._desktop_type = None
        self._availability_zone = None
        self._product_id = None
        self._flavor_id = None
        self._share_resource_sku = None
        self._image_type = None
        self._image_id = None
        self._root_volume = None
        self._data_volumes = None
        self._nics = None
        self._security_groups = None
        self._desktops = None
        self._desktop_name = None
        self._desktop_ips = None
        self._size = None
        self._email_notification = None
        self._enterprise_id = None
        self._enterprise_project_id = None
        self._order_id = None
        self._ou_name = None
        self._vpc_id = None
        self._subnet_ids = None
        self._tags = None
        self._scheduler_hints = None
        self._desktop_isv = None
        self._access_mode = None
        self._apply_shared_vpc_dedicated_param = None
        self._dedicated_subnets = None
        self._eip = None
        self._adn = None
        self._exclusive_host_id = None
        self._desktop_name_policy_id = None
        self._hour_package_product_id = None
        self._hour_package_offering_id = None
        self._root_resource_ids = None
        self._inst_info_ids = None
        self.discriminator = None

        self.desktop_type = desktop_type
        if availability_zone is not None:
            self.availability_zone = availability_zone
        self.product_id = product_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if share_resource_sku is not None:
            self.share_resource_sku = share_resource_sku
        self.image_type = image_type
        self.image_id = image_id
        self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if nics is not None:
            self.nics = nics
        if security_groups is not None:
            self.security_groups = security_groups
        if desktops is not None:
            self.desktops = desktops
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if desktop_ips is not None:
            self.desktop_ips = desktop_ips
        if size is not None:
            self.size = size
        if email_notification is not None:
            self.email_notification = email_notification
        if enterprise_id is not None:
            self.enterprise_id = enterprise_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if order_id is not None:
            self.order_id = order_id
        if ou_name is not None:
            self.ou_name = ou_name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if tags is not None:
            self.tags = tags
        if scheduler_hints is not None:
            self.scheduler_hints = scheduler_hints
        if desktop_isv is not None:
            self.desktop_isv = desktop_isv
        if access_mode is not None:
            self.access_mode = access_mode
        if apply_shared_vpc_dedicated_param is not None:
            self.apply_shared_vpc_dedicated_param = apply_shared_vpc_dedicated_param
        if dedicated_subnets is not None:
            self.dedicated_subnets = dedicated_subnets
        if eip is not None:
            self.eip = eip
        if adn is not None:
            self.adn = adn
        if exclusive_host_id is not None:
            self.exclusive_host_id = exclusive_host_id
        if desktop_name_policy_id is not None:
            self.desktop_name_policy_id = desktop_name_policy_id
        if hour_package_product_id is not None:
            self.hour_package_product_id = hour_package_product_id
        if hour_package_offering_id is not None:
            self.hour_package_offering_id = hour_package_offering_id
        if root_resource_ids is not None:
            self.root_resource_ids = root_resource_ids
        if inst_info_ids is not None:
            self.inst_info_ids = inst_info_ids

    @property
    def desktop_type(self):
        """Gets the desktop_type of this CreateDesktopReq.

        云桌面类型。 - DEDICATED：专属桌面，单用户。 - SHARED: 多用户共享桌面。

        :return: The desktop_type of this CreateDesktopReq.
        :rtype: str
        """
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):
        """Sets the desktop_type of this CreateDesktopReq.

        云桌面类型。 - DEDICATED：专属桌面，单用户。 - SHARED: 多用户共享桌面。

        :param desktop_type: The desktop_type of this CreateDesktopReq.
        :type desktop_type: str
        """
        self._desktop_type = desktop_type

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateDesktopReq.

        可用分区。将桌面创建到指定的可用分区。如果不指定则使用系统随机的可用分区。

        :return: The availability_zone of this CreateDesktopReq.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateDesktopReq.

        可用分区。将桌面创建到指定的可用分区。如果不指定则使用系统随机的可用分区。

        :param availability_zone: The availability_zone of this CreateDesktopReq.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def product_id(self):
        """Gets the product_id of this CreateDesktopReq.

        套餐ID。

        :return: The product_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateDesktopReq.

        套餐ID。

        :param product_id: The product_id of this CreateDesktopReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def flavor_id(self):
        """Gets the flavor_id of this CreateDesktopReq.

        套餐flavorID。

        :return: The flavor_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this CreateDesktopReq.

        套餐flavorID。

        :param flavor_id: The flavor_id of this CreateDesktopReq.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def share_resource_sku(self):
        """Gets the share_resource_sku of this CreateDesktopReq.

        桌面协同资源SKU码

        :return: The share_resource_sku of this CreateDesktopReq.
        :rtype: str
        """
        return self._share_resource_sku

    @share_resource_sku.setter
    def share_resource_sku(self, share_resource_sku):
        """Sets the share_resource_sku of this CreateDesktopReq.

        桌面协同资源SKU码

        :param share_resource_sku: The share_resource_sku of this CreateDesktopReq.
        :type share_resource_sku: str
        """
        self._share_resource_sku = share_resource_sku

    @property
    def image_type(self):
        """Gets the image_type of this CreateDesktopReq.

        镜像类型。默认值为private。  - private：私有镜像。 - gold：公共镜像。

        :return: The image_type of this CreateDesktopReq.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this CreateDesktopReq.

        镜像类型。默认值为private。  - private：私有镜像。 - gold：公共镜像。

        :param image_type: The image_type of this CreateDesktopReq.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_id(self):
        """Gets the image_id of this CreateDesktopReq.

        镜像ID，用于私有镜像创建桌面场景，配合product_id使用。

        :return: The image_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this CreateDesktopReq.

        镜像ID，用于私有镜像创建桌面场景，配合product_id使用。

        :param image_id: The image_id of this CreateDesktopReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def root_volume(self):
        """Gets the root_volume of this CreateDesktopReq.

        :return: The root_volume of this CreateDesktopReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Volume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this CreateDesktopReq.

        :param root_volume: The root_volume of this CreateDesktopReq.
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.Volume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        """Gets the data_volumes of this CreateDesktopReq.

        数据盘列表。

        :return: The data_volumes of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        """Sets the data_volumes of this CreateDesktopReq.

        数据盘列表。

        :param data_volumes: The data_volumes of this CreateDesktopReq.
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.Volume`]
        """
        self._data_volumes = data_volumes

    @property
    def nics(self):
        """Gets the nics of this CreateDesktopReq.

        桌面对应的网卡信息，如果不指定则使用默认网卡。

        :return: The nics of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Nic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this CreateDesktopReq.

        桌面对应的网卡信息，如果不指定则使用默认网卡。

        :param nics: The nics of this CreateDesktopReq.
        :type nics: list[:class:`huaweicloudsdkworkspace.v2.Nic`]
        """
        self._nics = nics

    @property
    def security_groups(self):
        """Gets the security_groups of this CreateDesktopReq.

        桌面使用的安全组，如果不指定则默认使用桌面代理中指定的安全组。

        :return: The security_groups of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this CreateDesktopReq.

        桌面使用的安全组，如果不指定则默认使用桌面代理中指定的安全组。

        :param security_groups: The security_groups of this CreateDesktopReq.
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def desktops(self):
        """Gets the desktops of this CreateDesktopReq.

        创建桌面使用的参数列表。长度为1-100。  当前不支持一批桌面不同配置，所有桌面的配置和第一台的一致，如果第一台未设置参数，则取外层的同名参数。

        :return: The desktops of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Desktop`]
        """
        return self._desktops

    @desktops.setter
    def desktops(self, desktops):
        """Sets the desktops of this CreateDesktopReq.

        创建桌面使用的参数列表。长度为1-100。  当前不支持一批桌面不同配置，所有桌面的配置和第一台的一致，如果第一台未设置参数，则取外层的同名参数。

        :param desktops: The desktops of this CreateDesktopReq.
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.Desktop`]
        """
        self._desktops = desktops

    @property
    def desktop_name(self):
        """Gets the desktop_name of this CreateDesktopReq.

        搭配size使用，当size为1时代表桌面名，位数1-15，当size大于1时代表桌面名前缀，位数：1-13。

        :return: The desktop_name of this CreateDesktopReq.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        """Sets the desktop_name of this CreateDesktopReq.

        搭配size使用，当size为1时代表桌面名，位数1-15，当size大于1时代表桌面名前缀，位数：1-13。

        :param desktop_name: The desktop_name of this CreateDesktopReq.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def desktop_ips(self):
        """Gets the desktop_ips of this CreateDesktopReq.

        桌面指定分配的ip地址列表,最小为0，最大为100。

        :return: The desktop_ips of this CreateDesktopReq.
        :rtype: list[str]
        """
        return self._desktop_ips

    @desktop_ips.setter
    def desktop_ips(self, desktop_ips):
        """Sets the desktop_ips of this CreateDesktopReq.

        桌面指定分配的ip地址列表,最小为0，最大为100。

        :param desktop_ips: The desktop_ips of this CreateDesktopReq.
        :type desktop_ips: list[str]
        """
        self._desktop_ips = desktop_ips

    @property
    def size(self):
        """Gets the size of this CreateDesktopReq.

        创建不分配用户的桌面的个数，和desktops不能同时生效，搭配desktop_name使用。

        :return: The size of this CreateDesktopReq.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateDesktopReq.

        创建不分配用户的桌面的个数，和desktops不能同时生效，搭配desktop_name使用。

        :param size: The size of this CreateDesktopReq.
        :type size: int
        """
        self._size = size

    @property
    def email_notification(self):
        """Gets the email_notification of this CreateDesktopReq.

        创建成功后是否发送邮件通知桌面用户，默认为true。

        :return: The email_notification of this CreateDesktopReq.
        :rtype: bool
        """
        return self._email_notification

    @email_notification.setter
    def email_notification(self, email_notification):
        """Sets the email_notification of this CreateDesktopReq.

        创建成功后是否发送邮件通知桌面用户，默认为true。

        :param email_notification: The email_notification of this CreateDesktopReq.
        :type email_notification: bool
        """
        self._email_notification = email_notification

    @property
    def enterprise_id(self):
        """Gets the enterprise_id of this CreateDesktopReq.

        企业ID，在非对接AD场景首次创建桌面时使用。

        :return: The enterprise_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, enterprise_id):
        """Sets the enterprise_id of this CreateDesktopReq.

        企业ID，在非对接AD场景首次创建桌面时使用。

        :param enterprise_id: The enterprise_id of this CreateDesktopReq.
        :type enterprise_id: str
        """
        self._enterprise_id = enterprise_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateDesktopReq.

        企业项目ID，默认\"0\"

        :return: The enterprise_project_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateDesktopReq.

        企业项目ID，默认\"0\"

        :param enterprise_project_id: The enterprise_project_id of this CreateDesktopReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def order_id(self):
        """Gets the order_id of this CreateDesktopReq.

        包周期订购ID，CBC订购回调时使用。

        :return: The order_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CreateDesktopReq.

        包周期订购ID，CBC订购回调时使用。

        :param order_id: The order_id of this CreateDesktopReq.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def ou_name(self):
        """Gets the ou_name of this CreateDesktopReq.

        OU名称，在对接AD时使用，需提前在AD中创建OU。

        :return: The ou_name of this CreateDesktopReq.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        """Sets the ou_name of this CreateDesktopReq.

        OU名称，在对接AD时使用，需提前在AD中创建OU。

        :param ou_name: The ou_name of this CreateDesktopReq.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateDesktopReq.

        在非对接AD场景首次创建桌面时使用。

        :return: The vpc_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateDesktopReq.

        在非对接AD场景首次创建桌面时使用。

        :param vpc_id: The vpc_id of this CreateDesktopReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this CreateDesktopReq.

        在非对接AD场景首次创建桌面时使用。

        :return: The subnet_ids of this CreateDesktopReq.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this CreateDesktopReq.

        在非对接AD场景首次创建桌面时使用。

        :param subnet_ids: The subnet_ids of this CreateDesktopReq.
        :type subnet_ids: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def tags(self):
        """Gets the tags of this CreateDesktopReq.

        标签列表。

        :return: The tags of this CreateDesktopReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateDesktopReq.

        标签列表。

        :param tags: The tags of this CreateDesktopReq.
        :type tags: list[:class:`huaweicloudsdkworkspace.v2.Tag`]
        """
        self._tags = tags

    @property
    def scheduler_hints(self):
        """Gets the scheduler_hints of this CreateDesktopReq.

        :return: The scheduler_hints of this CreateDesktopReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.WdhParam`
        """
        return self._scheduler_hints

    @scheduler_hints.setter
    def scheduler_hints(self, scheduler_hints):
        """Sets the scheduler_hints of this CreateDesktopReq.

        :param scheduler_hints: The scheduler_hints of this CreateDesktopReq.
        :type scheduler_hints: :class:`huaweicloudsdkworkspace.v2.WdhParam`
        """
        self._scheduler_hints = scheduler_hints

    @property
    def desktop_isv(self):
        """Gets the desktop_isv of this CreateDesktopReq.

        桌面来源。  - DEFAULT：默认桌面来源 - ONEMOBILE：协同办公云桌面OneMobile

        :return: The desktop_isv of this CreateDesktopReq.
        :rtype: str
        """
        return self._desktop_isv

    @desktop_isv.setter
    def desktop_isv(self, desktop_isv):
        """Sets the desktop_isv of this CreateDesktopReq.

        桌面来源。  - DEFAULT：默认桌面来源 - ONEMOBILE：协同办公云桌面OneMobile

        :param desktop_isv: The desktop_isv of this CreateDesktopReq.
        :type desktop_isv: str
        """
        self._desktop_isv = desktop_isv

    @property
    def access_mode(self):
        """Gets the access_mode of this CreateDesktopReq.

        接入模式。在非对接AD场景首次创建桌面时使用。 - INTERNET：互联网接入。 - DEDICATED：专线接入。 - BOTH：代表两种接入方式都支持。

        :return: The access_mode of this CreateDesktopReq.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this CreateDesktopReq.

        接入模式。在非对接AD场景首次创建桌面时使用。 - INTERNET：互联网接入。 - DEDICATED：专线接入。 - BOTH：代表两种接入方式都支持。

        :param access_mode: The access_mode of this CreateDesktopReq.
        :type access_mode: str
        """
        self._access_mode = access_mode

    @property
    def apply_shared_vpc_dedicated_param(self):
        """Gets the apply_shared_vpc_dedicated_param of this CreateDesktopReq.

        :return: The apply_shared_vpc_dedicated_param of this CreateDesktopReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplySharedVpcDedicatedParam`
        """
        return self._apply_shared_vpc_dedicated_param

    @apply_shared_vpc_dedicated_param.setter
    def apply_shared_vpc_dedicated_param(self, apply_shared_vpc_dedicated_param):
        """Sets the apply_shared_vpc_dedicated_param of this CreateDesktopReq.

        :param apply_shared_vpc_dedicated_param: The apply_shared_vpc_dedicated_param of this CreateDesktopReq.
        :type apply_shared_vpc_dedicated_param: :class:`huaweicloudsdkworkspace.v2.ApplySharedVpcDedicatedParam`
        """
        self._apply_shared_vpc_dedicated_param = apply_shared_vpc_dedicated_param

    @property
    def dedicated_subnets(self):
        """Gets the dedicated_subnets of this CreateDesktopReq.

        专线接入网段列表，多个网段信息用分号隔开，列表长度不超过5。在非对接AD场景首次创建桌面时使用。

        :return: The dedicated_subnets of this CreateDesktopReq.
        :rtype: str
        """
        return self._dedicated_subnets

    @dedicated_subnets.setter
    def dedicated_subnets(self, dedicated_subnets):
        """Sets the dedicated_subnets of this CreateDesktopReq.

        专线接入网段列表，多个网段信息用分号隔开，列表长度不超过5。在非对接AD场景首次创建桌面时使用。

        :param dedicated_subnets: The dedicated_subnets of this CreateDesktopReq.
        :type dedicated_subnets: str
        """
        self._dedicated_subnets = dedicated_subnets

    @property
    def eip(self):
        """Gets the eip of this CreateDesktopReq.

        :return: The eip of this CreateDesktopReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Eip`
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this CreateDesktopReq.

        :param eip: The eip of this CreateDesktopReq.
        :type eip: :class:`huaweicloudsdkworkspace.v2.Eip`
        """
        self._eip = eip

    @property
    def adn(self):
        """Gets the adn of this CreateDesktopReq.

        :return: The adn of this CreateDesktopReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Adn`
        """
        return self._adn

    @adn.setter
    def adn(self, adn):
        """Sets the adn of this CreateDesktopReq.

        :param adn: The adn of this CreateDesktopReq.
        :type adn: :class:`huaweicloudsdkworkspace.v2.Adn`
        """
        self._adn = adn

    @property
    def exclusive_host_id(self):
        """Gets the exclusive_host_id of this CreateDesktopReq.

        专享主机ID，创建专享桌面时如果在指定专享主机中创建则必选

        :return: The exclusive_host_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._exclusive_host_id

    @exclusive_host_id.setter
    def exclusive_host_id(self, exclusive_host_id):
        """Sets the exclusive_host_id of this CreateDesktopReq.

        专享主机ID，创建专享桌面时如果在指定专享主机中创建则必选

        :param exclusive_host_id: The exclusive_host_id of this CreateDesktopReq.
        :type exclusive_host_id: str
        """
        self._exclusive_host_id = exclusive_host_id

    @property
    def desktop_name_policy_id(self):
        """Gets the desktop_name_policy_id of this CreateDesktopReq.

        策略id，用于指定生成桌面名称策略，如果指定了桌面名称则优先使用指定的桌面名称。

        :return: The desktop_name_policy_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._desktop_name_policy_id

    @desktop_name_policy_id.setter
    def desktop_name_policy_id(self, desktop_name_policy_id):
        """Sets the desktop_name_policy_id of this CreateDesktopReq.

        策略id，用于指定生成桌面名称策略，如果指定了桌面名称则优先使用指定的桌面名称。

        :param desktop_name_policy_id: The desktop_name_policy_id of this CreateDesktopReq.
        :type desktop_name_policy_id: str
        """
        self._desktop_name_policy_id = desktop_name_policy_id

    @property
    def hour_package_product_id(self):
        """Gets the hour_package_product_id of this CreateDesktopReq.

        桌面小时包套餐ID。

        :return: The hour_package_product_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._hour_package_product_id

    @hour_package_product_id.setter
    def hour_package_product_id(self, hour_package_product_id):
        """Sets the hour_package_product_id of this CreateDesktopReq.

        桌面小时包套餐ID。

        :param hour_package_product_id: The hour_package_product_id of this CreateDesktopReq.
        :type hour_package_product_id: str
        """
        self._hour_package_product_id = hour_package_product_id

    @property
    def hour_package_offering_id(self):
        """Gets the hour_package_offering_id of this CreateDesktopReq.

        桌面小时包offeringID。

        :return: The hour_package_offering_id of this CreateDesktopReq.
        :rtype: str
        """
        return self._hour_package_offering_id

    @hour_package_offering_id.setter
    def hour_package_offering_id(self, hour_package_offering_id):
        """Sets the hour_package_offering_id of this CreateDesktopReq.

        桌面小时包offeringID。

        :param hour_package_offering_id: The hour_package_offering_id of this CreateDesktopReq.
        :type hour_package_offering_id: str
        """
        self._hour_package_offering_id = hour_package_offering_id

    @property
    def root_resource_ids(self):
        """Gets the root_resource_ids of this CreateDesktopReq.

        根资源ID列表，创建小时包桌面时使用，最小为0，最大为100。

        :return: The root_resource_ids of this CreateDesktopReq.
        :rtype: list[str]
        """
        return self._root_resource_ids

    @root_resource_ids.setter
    def root_resource_ids(self, root_resource_ids):
        """Sets the root_resource_ids of this CreateDesktopReq.

        根资源ID列表，创建小时包桌面时使用，最小为0，最大为100。

        :param root_resource_ids: The root_resource_ids of this CreateDesktopReq.
        :type root_resource_ids: list[str]
        """
        self._root_resource_ids = root_resource_ids

    @property
    def inst_info_ids(self):
        """Gets the inst_info_ids of this CreateDesktopReq.

        instInfoId列表，创建小时包桌面时使用，最小为0，最大为100。

        :return: The inst_info_ids of this CreateDesktopReq.
        :rtype: list[str]
        """
        return self._inst_info_ids

    @inst_info_ids.setter
    def inst_info_ids(self, inst_info_ids):
        """Sets the inst_info_ids of this CreateDesktopReq.

        instInfoId列表，创建小时包桌面时使用，最小为0，最大为100。

        :param inst_info_ids: The inst_info_ids of this CreateDesktopReq.
        :type inst_info_ids: list[str]
        """
        self._inst_info_ids = inst_info_ids

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
        if not isinstance(other, CreateDesktopReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
