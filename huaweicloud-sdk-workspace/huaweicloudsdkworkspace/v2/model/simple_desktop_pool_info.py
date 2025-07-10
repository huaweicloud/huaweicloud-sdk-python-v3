# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleDesktopPoolInfo:

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
        'name': 'str',
        'type': 'str',
        'description': 'str',
        'created_time': 'str',
        'charging_mode': 'str',
        'desktop_count': 'int',
        'desktop_used': 'int',
        'availability_zone': 'str',
        'subnet_id': 'str',
        'product': 'ProductInfo',
        'image_id': 'str',
        'image_name': 'str',
        'image_os_type': 'str',
        'image_os_version': 'str',
        'image_os_platform': 'str',
        'image_product_code': 'str',
        'root_volume': 'VolumeInfo',
        'data_volumes': 'list[VolumeInfo]',
        'security_groups': 'list[SecurityGroupInfo]',
        'disconnected_retention_period': 'int',
        'enable_autoscale': 'bool',
        'autoscale_policy': 'AutoscalePolicy',
        'status': 'str',
        'enterprise_project_id': 'str',
        'in_maintenance_mode': 'bool',
        'desktop_name_policy_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'created_time': 'created_time',
        'charging_mode': 'charging_mode',
        'desktop_count': 'desktop_count',
        'desktop_used': 'desktop_used',
        'availability_zone': 'availability_zone',
        'subnet_id': 'subnet_id',
        'product': 'product',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'image_os_type': 'image_os_type',
        'image_os_version': 'image_os_version',
        'image_os_platform': 'image_os_platform',
        'image_product_code': 'image_product_code',
        'root_volume': 'root_volume',
        'data_volumes': 'data_volumes',
        'security_groups': 'security_groups',
        'disconnected_retention_period': 'disconnected_retention_period',
        'enable_autoscale': 'enable_autoscale',
        'autoscale_policy': 'autoscale_policy',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id',
        'in_maintenance_mode': 'in_maintenance_mode',
        'desktop_name_policy_id': 'desktop_name_policy_id'
    }

    def __init__(self, id=None, name=None, type=None, description=None, created_time=None, charging_mode=None, desktop_count=None, desktop_used=None, availability_zone=None, subnet_id=None, product=None, image_id=None, image_name=None, image_os_type=None, image_os_version=None, image_os_platform=None, image_product_code=None, root_volume=None, data_volumes=None, security_groups=None, disconnected_retention_period=None, enable_autoscale=None, autoscale_policy=None, status=None, enterprise_project_id=None, in_maintenance_mode=None, desktop_name_policy_id=None):
        r"""SimpleDesktopPoolInfo

        The model defined in huaweicloud sdk

        :param id: 桌面池ID。
        :type id: str
        :param name: 桌面池名称。
        :type name: str
        :param type: 桌面池类型。DYNAMIC：动态池，STATIC：静态池。
        :type type: str
        :param description: 桌面池描述。
        :type description: str
        :param created_time: 创建时间，格式为：UTC格式，例如“2022-05-11T11:45:42.000Z”。
        :type created_time: str
        :param charging_mode: 计费模式，0：包周期，1：按需。
        :type charging_mode: str
        :param desktop_count: 桌面池总桌面数量。
        :type desktop_count: int
        :param desktop_used: 桌面池绑定用户的桌面个数。
        :type desktop_used: int
        :param availability_zone: 可用区。
        :type availability_zone: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param product: 
        :type product: :class:`huaweicloudsdkworkspace.v2.ProductInfo`
        :param image_id: 镜像ID。
        :type image_id: str
        :param image_name: 镜像名称。
        :type image_name: str
        :param image_os_type: 镜像OS类型。
        :type image_os_type: str
        :param image_os_version: 镜像OS版本。
        :type image_os_version: str
        :param image_os_platform: 镜像OS平台。
        :type image_os_platform: str
        :param image_product_code: 镜像的productCode（specCode）。
        :type image_product_code: str
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.VolumeInfo`
        :param data_volumes: 数据盘列表。
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.VolumeInfo`]
        :param security_groups: 桌面安全组。
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroupInfo`]
        :param disconnected_retention_period: 动态池桌面断连多少分钟内，保留用户与桌面的绑定关系，超时后自动解绑。
        :type disconnected_retention_period: int
        :param enable_autoscale: 桌面池是否开启弹性伸缩类型，为false则表示不开启弹性伸缩，为true则表示开启弹性伸缩。
        :type enable_autoscale: bool
        :param autoscale_policy: 
        :type autoscale_policy: :class:`huaweicloudsdkworkspace.v2.AutoscalePolicy`
        :param status: 桌面池状态。 - STEADY：稳态 - TEMPORARY：临时态 - EXIST_FROZEN：存在冻结桌面 - UNKNOWN：未知态
        :type status: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param in_maintenance_mode: 桌面池是否处于管理员维护模式。
        :type in_maintenance_mode: bool
        :param desktop_name_policy_id: 策略id，用于指定生成桌面名称策略。
        :type desktop_name_policy_id: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._description = None
        self._created_time = None
        self._charging_mode = None
        self._desktop_count = None
        self._desktop_used = None
        self._availability_zone = None
        self._subnet_id = None
        self._product = None
        self._image_id = None
        self._image_name = None
        self._image_os_type = None
        self._image_os_version = None
        self._image_os_platform = None
        self._image_product_code = None
        self._root_volume = None
        self._data_volumes = None
        self._security_groups = None
        self._disconnected_retention_period = None
        self._enable_autoscale = None
        self._autoscale_policy = None
        self._status = None
        self._enterprise_project_id = None
        self._in_maintenance_mode = None
        self._desktop_name_policy_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if created_time is not None:
            self.created_time = created_time
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if desktop_count is not None:
            self.desktop_count = desktop_count
        if desktop_used is not None:
            self.desktop_used = desktop_used
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if product is not None:
            self.product = product
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if image_os_type is not None:
            self.image_os_type = image_os_type
        if image_os_version is not None:
            self.image_os_version = image_os_version
        if image_os_platform is not None:
            self.image_os_platform = image_os_platform
        if image_product_code is not None:
            self.image_product_code = image_product_code
        if root_volume is not None:
            self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if security_groups is not None:
            self.security_groups = security_groups
        if disconnected_retention_period is not None:
            self.disconnected_retention_period = disconnected_retention_period
        if enable_autoscale is not None:
            self.enable_autoscale = enable_autoscale
        if autoscale_policy is not None:
            self.autoscale_policy = autoscale_policy
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if in_maintenance_mode is not None:
            self.in_maintenance_mode = in_maintenance_mode
        if desktop_name_policy_id is not None:
            self.desktop_name_policy_id = desktop_name_policy_id

    @property
    def id(self):
        r"""Gets the id of this SimpleDesktopPoolInfo.

        桌面池ID。

        :return: The id of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SimpleDesktopPoolInfo.

        桌面池ID。

        :param id: The id of this SimpleDesktopPoolInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SimpleDesktopPoolInfo.

        桌面池名称。

        :return: The name of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SimpleDesktopPoolInfo.

        桌面池名称。

        :param name: The name of this SimpleDesktopPoolInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this SimpleDesktopPoolInfo.

        桌面池类型。DYNAMIC：动态池，STATIC：静态池。

        :return: The type of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SimpleDesktopPoolInfo.

        桌面池类型。DYNAMIC：动态池，STATIC：静态池。

        :param type: The type of this SimpleDesktopPoolInfo.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this SimpleDesktopPoolInfo.

        桌面池描述。

        :return: The description of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SimpleDesktopPoolInfo.

        桌面池描述。

        :param description: The description of this SimpleDesktopPoolInfo.
        :type description: str
        """
        self._description = description

    @property
    def created_time(self):
        r"""Gets the created_time of this SimpleDesktopPoolInfo.

        创建时间，格式为：UTC格式，例如“2022-05-11T11:45:42.000Z”。

        :return: The created_time of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this SimpleDesktopPoolInfo.

        创建时间，格式为：UTC格式，例如“2022-05-11T11:45:42.000Z”。

        :param created_time: The created_time of this SimpleDesktopPoolInfo.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this SimpleDesktopPoolInfo.

        计费模式，0：包周期，1：按需。

        :return: The charging_mode of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this SimpleDesktopPoolInfo.

        计费模式，0：包周期，1：按需。

        :param charging_mode: The charging_mode of this SimpleDesktopPoolInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def desktop_count(self):
        r"""Gets the desktop_count of this SimpleDesktopPoolInfo.

        桌面池总桌面数量。

        :return: The desktop_count of this SimpleDesktopPoolInfo.
        :rtype: int
        """
        return self._desktop_count

    @desktop_count.setter
    def desktop_count(self, desktop_count):
        r"""Sets the desktop_count of this SimpleDesktopPoolInfo.

        桌面池总桌面数量。

        :param desktop_count: The desktop_count of this SimpleDesktopPoolInfo.
        :type desktop_count: int
        """
        self._desktop_count = desktop_count

    @property
    def desktop_used(self):
        r"""Gets the desktop_used of this SimpleDesktopPoolInfo.

        桌面池绑定用户的桌面个数。

        :return: The desktop_used of this SimpleDesktopPoolInfo.
        :rtype: int
        """
        return self._desktop_used

    @desktop_used.setter
    def desktop_used(self, desktop_used):
        r"""Sets the desktop_used of this SimpleDesktopPoolInfo.

        桌面池绑定用户的桌面个数。

        :param desktop_used: The desktop_used of this SimpleDesktopPoolInfo.
        :type desktop_used: int
        """
        self._desktop_used = desktop_used

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this SimpleDesktopPoolInfo.

        可用区。

        :return: The availability_zone of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this SimpleDesktopPoolInfo.

        可用区。

        :param availability_zone: The availability_zone of this SimpleDesktopPoolInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this SimpleDesktopPoolInfo.

        子网ID。

        :return: The subnet_id of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this SimpleDesktopPoolInfo.

        子网ID。

        :param subnet_id: The subnet_id of this SimpleDesktopPoolInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def product(self):
        r"""Gets the product of this SimpleDesktopPoolInfo.

        :return: The product of this SimpleDesktopPoolInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ProductInfo`
        """
        return self._product

    @product.setter
    def product(self, product):
        r"""Sets the product of this SimpleDesktopPoolInfo.

        :param product: The product of this SimpleDesktopPoolInfo.
        :type product: :class:`huaweicloudsdkworkspace.v2.ProductInfo`
        """
        self._product = product

    @property
    def image_id(self):
        r"""Gets the image_id of this SimpleDesktopPoolInfo.

        镜像ID。

        :return: The image_id of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this SimpleDesktopPoolInfo.

        镜像ID。

        :param image_id: The image_id of this SimpleDesktopPoolInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this SimpleDesktopPoolInfo.

        镜像名称。

        :return: The image_name of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this SimpleDesktopPoolInfo.

        镜像名称。

        :param image_name: The image_name of this SimpleDesktopPoolInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_os_type(self):
        r"""Gets the image_os_type of this SimpleDesktopPoolInfo.

        镜像OS类型。

        :return: The image_os_type of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._image_os_type

    @image_os_type.setter
    def image_os_type(self, image_os_type):
        r"""Sets the image_os_type of this SimpleDesktopPoolInfo.

        镜像OS类型。

        :param image_os_type: The image_os_type of this SimpleDesktopPoolInfo.
        :type image_os_type: str
        """
        self._image_os_type = image_os_type

    @property
    def image_os_version(self):
        r"""Gets the image_os_version of this SimpleDesktopPoolInfo.

        镜像OS版本。

        :return: The image_os_version of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._image_os_version

    @image_os_version.setter
    def image_os_version(self, image_os_version):
        r"""Sets the image_os_version of this SimpleDesktopPoolInfo.

        镜像OS版本。

        :param image_os_version: The image_os_version of this SimpleDesktopPoolInfo.
        :type image_os_version: str
        """
        self._image_os_version = image_os_version

    @property
    def image_os_platform(self):
        r"""Gets the image_os_platform of this SimpleDesktopPoolInfo.

        镜像OS平台。

        :return: The image_os_platform of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._image_os_platform

    @image_os_platform.setter
    def image_os_platform(self, image_os_platform):
        r"""Sets the image_os_platform of this SimpleDesktopPoolInfo.

        镜像OS平台。

        :param image_os_platform: The image_os_platform of this SimpleDesktopPoolInfo.
        :type image_os_platform: str
        """
        self._image_os_platform = image_os_platform

    @property
    def image_product_code(self):
        r"""Gets the image_product_code of this SimpleDesktopPoolInfo.

        镜像的productCode（specCode）。

        :return: The image_product_code of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._image_product_code

    @image_product_code.setter
    def image_product_code(self, image_product_code):
        r"""Sets the image_product_code of this SimpleDesktopPoolInfo.

        镜像的productCode（specCode）。

        :param image_product_code: The image_product_code of this SimpleDesktopPoolInfo.
        :type image_product_code: str
        """
        self._image_product_code = image_product_code

    @property
    def root_volume(self):
        r"""Gets the root_volume of this SimpleDesktopPoolInfo.

        :return: The root_volume of this SimpleDesktopPoolInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.VolumeInfo`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this SimpleDesktopPoolInfo.

        :param root_volume: The root_volume of this SimpleDesktopPoolInfo.
        :type root_volume: :class:`huaweicloudsdkworkspace.v2.VolumeInfo`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this SimpleDesktopPoolInfo.

        数据盘列表。

        :return: The data_volumes of this SimpleDesktopPoolInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.VolumeInfo`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this SimpleDesktopPoolInfo.

        数据盘列表。

        :param data_volumes: The data_volumes of this SimpleDesktopPoolInfo.
        :type data_volumes: list[:class:`huaweicloudsdkworkspace.v2.VolumeInfo`]
        """
        self._data_volumes = data_volumes

    @property
    def security_groups(self):
        r"""Gets the security_groups of this SimpleDesktopPoolInfo.

        桌面安全组。

        :return: The security_groups of this SimpleDesktopPoolInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroupInfo`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this SimpleDesktopPoolInfo.

        桌面安全组。

        :param security_groups: The security_groups of this SimpleDesktopPoolInfo.
        :type security_groups: list[:class:`huaweicloudsdkworkspace.v2.SecurityGroupInfo`]
        """
        self._security_groups = security_groups

    @property
    def disconnected_retention_period(self):
        r"""Gets the disconnected_retention_period of this SimpleDesktopPoolInfo.

        动态池桌面断连多少分钟内，保留用户与桌面的绑定关系，超时后自动解绑。

        :return: The disconnected_retention_period of this SimpleDesktopPoolInfo.
        :rtype: int
        """
        return self._disconnected_retention_period

    @disconnected_retention_period.setter
    def disconnected_retention_period(self, disconnected_retention_period):
        r"""Sets the disconnected_retention_period of this SimpleDesktopPoolInfo.

        动态池桌面断连多少分钟内，保留用户与桌面的绑定关系，超时后自动解绑。

        :param disconnected_retention_period: The disconnected_retention_period of this SimpleDesktopPoolInfo.
        :type disconnected_retention_period: int
        """
        self._disconnected_retention_period = disconnected_retention_period

    @property
    def enable_autoscale(self):
        r"""Gets the enable_autoscale of this SimpleDesktopPoolInfo.

        桌面池是否开启弹性伸缩类型，为false则表示不开启弹性伸缩，为true则表示开启弹性伸缩。

        :return: The enable_autoscale of this SimpleDesktopPoolInfo.
        :rtype: bool
        """
        return self._enable_autoscale

    @enable_autoscale.setter
    def enable_autoscale(self, enable_autoscale):
        r"""Sets the enable_autoscale of this SimpleDesktopPoolInfo.

        桌面池是否开启弹性伸缩类型，为false则表示不开启弹性伸缩，为true则表示开启弹性伸缩。

        :param enable_autoscale: The enable_autoscale of this SimpleDesktopPoolInfo.
        :type enable_autoscale: bool
        """
        self._enable_autoscale = enable_autoscale

    @property
    def autoscale_policy(self):
        r"""Gets the autoscale_policy of this SimpleDesktopPoolInfo.

        :return: The autoscale_policy of this SimpleDesktopPoolInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AutoscalePolicy`
        """
        return self._autoscale_policy

    @autoscale_policy.setter
    def autoscale_policy(self, autoscale_policy):
        r"""Sets the autoscale_policy of this SimpleDesktopPoolInfo.

        :param autoscale_policy: The autoscale_policy of this SimpleDesktopPoolInfo.
        :type autoscale_policy: :class:`huaweicloudsdkworkspace.v2.AutoscalePolicy`
        """
        self._autoscale_policy = autoscale_policy

    @property
    def status(self):
        r"""Gets the status of this SimpleDesktopPoolInfo.

        桌面池状态。 - STEADY：稳态 - TEMPORARY：临时态 - EXIST_FROZEN：存在冻结桌面 - UNKNOWN：未知态

        :return: The status of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SimpleDesktopPoolInfo.

        桌面池状态。 - STEADY：稳态 - TEMPORARY：临时态 - EXIST_FROZEN：存在冻结桌面 - UNKNOWN：未知态

        :param status: The status of this SimpleDesktopPoolInfo.
        :type status: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SimpleDesktopPoolInfo.

        企业项目ID。

        :return: The enterprise_project_id of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SimpleDesktopPoolInfo.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this SimpleDesktopPoolInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def in_maintenance_mode(self):
        r"""Gets the in_maintenance_mode of this SimpleDesktopPoolInfo.

        桌面池是否处于管理员维护模式。

        :return: The in_maintenance_mode of this SimpleDesktopPoolInfo.
        :rtype: bool
        """
        return self._in_maintenance_mode

    @in_maintenance_mode.setter
    def in_maintenance_mode(self, in_maintenance_mode):
        r"""Sets the in_maintenance_mode of this SimpleDesktopPoolInfo.

        桌面池是否处于管理员维护模式。

        :param in_maintenance_mode: The in_maintenance_mode of this SimpleDesktopPoolInfo.
        :type in_maintenance_mode: bool
        """
        self._in_maintenance_mode = in_maintenance_mode

    @property
    def desktop_name_policy_id(self):
        r"""Gets the desktop_name_policy_id of this SimpleDesktopPoolInfo.

        策略id，用于指定生成桌面名称策略。

        :return: The desktop_name_policy_id of this SimpleDesktopPoolInfo.
        :rtype: str
        """
        return self._desktop_name_policy_id

    @desktop_name_policy_id.setter
    def desktop_name_policy_id(self, desktop_name_policy_id):
        r"""Sets the desktop_name_policy_id of this SimpleDesktopPoolInfo.

        策略id，用于指定生成桌面名称策略。

        :param desktop_name_policy_id: The desktop_name_policy_id of this SimpleDesktopPoolInfo.
        :type desktop_name_policy_id: str
        """
        self._desktop_name_policy_id = desktop_name_policy_id

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
        if not isinstance(other, SimpleDesktopPoolInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
