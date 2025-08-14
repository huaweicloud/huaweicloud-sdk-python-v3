# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerGroupResponse(SdkResponse):

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
        'description': 'str',
        'image_id': 'str',
        'os_type': 'OsTypeEnum',
        'product_id': 'str',
        'subnet_id': 'str',
        'system_disk_type': 'VolumeType',
        'system_disk_size': 'int',
        'is_vdi': 'bool',
        'extra_session_type': 'ExtraSessionTypeEnum',
        'extra_session_size': 'int',
        'app_type': 'AppTypeEnum',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'storage_mount_policy': 'StorageFolderMountType',
        'enterprise_project_id': 'str',
        'primary_server_group_ids': 'list[str]',
        'secondary_server_group_ids': 'list[str]',
        'server_group_status': 'bool',
        'site_type': 'str',
        'site_id': 'str',
        'app_server_flavor_count': 'int',
        'app_server_count': 'int',
        'app_group_count': 'int',
        'image_name': 'str',
        'product_info': 'ProductInfo',
        'subnet_name': 'str',
        'scaling_policy': 'ScalingPolicy',
        'tags': 'list[TmsTag]',
        'ou_name': 'str',
        'flavors': 'list[Flavor]',
        'project_name': 'str',
        'image_min_disk': 'int',
        'route_policy': 'RoutePolicy',
        'image_product_id': 'str',
        'image_type': 'str',
        'ip_virtual': 'IpVirtual'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'image_id': 'image_id',
        'os_type': 'os_type',
        'product_id': 'product_id',
        'subnet_id': 'subnet_id',
        'system_disk_type': 'system_disk_type',
        'system_disk_size': 'system_disk_size',
        'is_vdi': 'is_vdi',
        'extra_session_type': 'extra_session_type',
        'extra_session_size': 'extra_session_size',
        'app_type': 'app_type',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'storage_mount_policy': 'storage_mount_policy',
        'enterprise_project_id': 'enterprise_project_id',
        'primary_server_group_ids': 'primary_server_group_ids',
        'secondary_server_group_ids': 'secondary_server_group_ids',
        'server_group_status': 'server_group_status',
        'site_type': 'site_type',
        'site_id': 'site_id',
        'app_server_flavor_count': 'app_server_flavor_count',
        'app_server_count': 'app_server_count',
        'app_group_count': 'app_group_count',
        'image_name': 'image_name',
        'product_info': 'product_info',
        'subnet_name': 'subnet_name',
        'scaling_policy': 'scaling_policy',
        'tags': 'tags',
        'ou_name': 'ou_name',
        'flavors': 'flavors',
        'project_name': 'project_name',
        'image_min_disk': 'image_min_disk',
        'route_policy': 'route_policy',
        'image_product_id': 'image_product_id',
        'image_type': 'image_type',
        'ip_virtual': 'ip_virtual'
    }

    def __init__(self, id=None, name=None, description=None, image_id=None, os_type=None, product_id=None, subnet_id=None, system_disk_type=None, system_disk_size=None, is_vdi=None, extra_session_type=None, extra_session_size=None, app_type=None, create_time=None, update_time=None, storage_mount_policy=None, enterprise_project_id=None, primary_server_group_ids=None, secondary_server_group_ids=None, server_group_status=None, site_type=None, site_id=None, app_server_flavor_count=None, app_server_count=None, app_group_count=None, image_name=None, product_info=None, subnet_name=None, scaling_policy=None, tags=None, ou_name=None, flavors=None, project_name=None, image_min_disk=None, route_policy=None, image_product_id=None, image_type=None, ip_virtual=None):
        r"""ShowServerGroupResponse

        The model defined in huaweicloud sdk

        :param id: 服务器组的唯一标识。
        :type id: str
        :param name: 服务器组名称。
        :type name: str
        :param description: 服务器组描述。
        :type description: str
        :param image_id: 服务器组关联的镜像ID，用于创建对应组下的云服务器。
        :type image_id: str
        :param os_type: 
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        :param product_id: 产品id。
        :type product_id: str
        :param subnet_id: 网卡对应的子网ID。
        :type subnet_id: str
        :param system_disk_type: 
        :type system_disk_type: :class:`huaweicloudsdkworkspaceapp.v1.VolumeType`
        :param system_disk_size: 磁盘容量，单位GB。
        :type system_disk_size: int
        :param is_vdi: 是否为vdi单会话模式。
        :type is_vdi: bool
        :param extra_session_type: 
        :type extra_session_type: :class:`huaweicloudsdkworkspaceapp.v1.ExtraSessionTypeEnum`
        :param extra_session_size: 付费会话个数。
        :type extra_session_size: int
        :param app_type: 
        :type app_type: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        :param create_time: 服务器组创建时间。
        :type create_time: datetime
        :param update_time: 服务器组更新时间。
        :type update_time: datetime
        :param storage_mount_policy: 
        :type storage_mount_policy: :class:`huaweicloudsdkworkspaceapp.v1.StorageFolderMountType`
        :param enterprise_project_id: 企业项目ID(0表示默认企业项目Id)。
        :type enterprise_project_id: str
        :param primary_server_group_ids: 主服务器组id列表。
        :type primary_server_group_ids: list[str]
        :param secondary_server_group_ids: 备服务器组id列表。
        :type secondary_server_group_ids: list[str]
        :param server_group_status: 服务器是否处于启用状态，true表示处于启用状态 false表示处于禁用状态。
        :type server_group_status: bool
        :param site_type: 站点类型 - CENTER/IES。
        :type site_type: str
        :param site_id: 站点id。
        :type site_id: str
        :param app_server_flavor_count: 服务器配置总数量。
        :type app_server_flavor_count: int
        :param app_server_count: 服务器总数量。
        :type app_server_count: int
        :param app_group_count: 关联应用组的总数量。
        :type app_group_count: int
        :param image_name: 镜像名称。
        :type image_name: str
        :param product_info: 
        :type product_info: :class:`huaweicloudsdkworkspaceapp.v1.ProductInfo`
        :param subnet_name: 子网名称。
        :type subnet_name: str
        :param scaling_policy: 
        :type scaling_policy: :class:`huaweicloudsdkworkspaceapp.v1.ScalingPolicy`
        :param tags: 标签信息。
        :type tags: list[:class:`huaweicloudsdkworkspaceapp.v1.TmsTag`]
        :param ou_name: 默认组织名称。
        :type ou_name: str
        :param flavors: 服务器规格列表。
        :type flavors: list[:class:`huaweicloudsdkworkspaceapp.v1.Flavor`]
        :param project_name: 项目名称。
        :type project_name: str
        :param image_min_disk: 镜像运行的最小内存，单位为MB，默认设置为0。
        :type image_min_disk: int
        :param route_policy: 
        :type route_policy: :class:`huaweicloudsdkworkspaceapp.v1.RoutePolicy`
        :param image_product_id: 镜像的产品id。
        :type image_product_id: str
        :param image_type: 镜像类型。
        :type image_type: str
        :param ip_virtual: 
        :type ip_virtual: :class:`huaweicloudsdkworkspaceapp.v1.IpVirtual`
        """
        
        super(ShowServerGroupResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._image_id = None
        self._os_type = None
        self._product_id = None
        self._subnet_id = None
        self._system_disk_type = None
        self._system_disk_size = None
        self._is_vdi = None
        self._extra_session_type = None
        self._extra_session_size = None
        self._app_type = None
        self._create_time = None
        self._update_time = None
        self._storage_mount_policy = None
        self._enterprise_project_id = None
        self._primary_server_group_ids = None
        self._secondary_server_group_ids = None
        self._server_group_status = None
        self._site_type = None
        self._site_id = None
        self._app_server_flavor_count = None
        self._app_server_count = None
        self._app_group_count = None
        self._image_name = None
        self._product_info = None
        self._subnet_name = None
        self._scaling_policy = None
        self._tags = None
        self._ou_name = None
        self._flavors = None
        self._project_name = None
        self._image_min_disk = None
        self._route_policy = None
        self._image_product_id = None
        self._image_type = None
        self._ip_virtual = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if image_id is not None:
            self.image_id = image_id
        if os_type is not None:
            self.os_type = os_type
        if product_id is not None:
            self.product_id = product_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if system_disk_type is not None:
            self.system_disk_type = system_disk_type
        if system_disk_size is not None:
            self.system_disk_size = system_disk_size
        if is_vdi is not None:
            self.is_vdi = is_vdi
        if extra_session_type is not None:
            self.extra_session_type = extra_session_type
        if extra_session_size is not None:
            self.extra_session_size = extra_session_size
        if app_type is not None:
            self.app_type = app_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if storage_mount_policy is not None:
            self.storage_mount_policy = storage_mount_policy
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if primary_server_group_ids is not None:
            self.primary_server_group_ids = primary_server_group_ids
        if secondary_server_group_ids is not None:
            self.secondary_server_group_ids = secondary_server_group_ids
        if server_group_status is not None:
            self.server_group_status = server_group_status
        if site_type is not None:
            self.site_type = site_type
        if site_id is not None:
            self.site_id = site_id
        if app_server_flavor_count is not None:
            self.app_server_flavor_count = app_server_flavor_count
        if app_server_count is not None:
            self.app_server_count = app_server_count
        if app_group_count is not None:
            self.app_group_count = app_group_count
        if image_name is not None:
            self.image_name = image_name
        if product_info is not None:
            self.product_info = product_info
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if scaling_policy is not None:
            self.scaling_policy = scaling_policy
        if tags is not None:
            self.tags = tags
        if ou_name is not None:
            self.ou_name = ou_name
        if flavors is not None:
            self.flavors = flavors
        if project_name is not None:
            self.project_name = project_name
        if image_min_disk is not None:
            self.image_min_disk = image_min_disk
        if route_policy is not None:
            self.route_policy = route_policy
        if image_product_id is not None:
            self.image_product_id = image_product_id
        if image_type is not None:
            self.image_type = image_type
        if ip_virtual is not None:
            self.ip_virtual = ip_virtual

    @property
    def id(self):
        r"""Gets the id of this ShowServerGroupResponse.

        服务器组的唯一标识。

        :return: The id of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowServerGroupResponse.

        服务器组的唯一标识。

        :param id: The id of this ShowServerGroupResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowServerGroupResponse.

        服务器组名称。

        :return: The name of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowServerGroupResponse.

        服务器组名称。

        :param name: The name of this ShowServerGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowServerGroupResponse.

        服务器组描述。

        :return: The description of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowServerGroupResponse.

        服务器组描述。

        :param description: The description of this ShowServerGroupResponse.
        :type description: str
        """
        self._description = description

    @property
    def image_id(self):
        r"""Gets the image_id of this ShowServerGroupResponse.

        服务器组关联的镜像ID，用于创建对应组下的云服务器。

        :return: The image_id of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ShowServerGroupResponse.

        服务器组关联的镜像ID，用于创建对应组下的云服务器。

        :param image_id: The image_id of this ShowServerGroupResponse.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def os_type(self):
        r"""Gets the os_type of this ShowServerGroupResponse.

        :return: The os_type of this ShowServerGroupResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ShowServerGroupResponse.

        :param os_type: The os_type of this ShowServerGroupResponse.
        :type os_type: :class:`huaweicloudsdkworkspaceapp.v1.OsTypeEnum`
        """
        self._os_type = os_type

    @property
    def product_id(self):
        r"""Gets the product_id of this ShowServerGroupResponse.

        产品id。

        :return: The product_id of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ShowServerGroupResponse.

        产品id。

        :param product_id: The product_id of this ShowServerGroupResponse.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ShowServerGroupResponse.

        网卡对应的子网ID。

        :return: The subnet_id of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ShowServerGroupResponse.

        网卡对应的子网ID。

        :param subnet_id: The subnet_id of this ShowServerGroupResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def system_disk_type(self):
        r"""Gets the system_disk_type of this ShowServerGroupResponse.

        :return: The system_disk_type of this ShowServerGroupResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.VolumeType`
        """
        return self._system_disk_type

    @system_disk_type.setter
    def system_disk_type(self, system_disk_type):
        r"""Sets the system_disk_type of this ShowServerGroupResponse.

        :param system_disk_type: The system_disk_type of this ShowServerGroupResponse.
        :type system_disk_type: :class:`huaweicloudsdkworkspaceapp.v1.VolumeType`
        """
        self._system_disk_type = system_disk_type

    @property
    def system_disk_size(self):
        r"""Gets the system_disk_size of this ShowServerGroupResponse.

        磁盘容量，单位GB。

        :return: The system_disk_size of this ShowServerGroupResponse.
        :rtype: int
        """
        return self._system_disk_size

    @system_disk_size.setter
    def system_disk_size(self, system_disk_size):
        r"""Sets the system_disk_size of this ShowServerGroupResponse.

        磁盘容量，单位GB。

        :param system_disk_size: The system_disk_size of this ShowServerGroupResponse.
        :type system_disk_size: int
        """
        self._system_disk_size = system_disk_size

    @property
    def is_vdi(self):
        r"""Gets the is_vdi of this ShowServerGroupResponse.

        是否为vdi单会话模式。

        :return: The is_vdi of this ShowServerGroupResponse.
        :rtype: bool
        """
        return self._is_vdi

    @is_vdi.setter
    def is_vdi(self, is_vdi):
        r"""Sets the is_vdi of this ShowServerGroupResponse.

        是否为vdi单会话模式。

        :param is_vdi: The is_vdi of this ShowServerGroupResponse.
        :type is_vdi: bool
        """
        self._is_vdi = is_vdi

    @property
    def extra_session_type(self):
        r"""Gets the extra_session_type of this ShowServerGroupResponse.

        :return: The extra_session_type of this ShowServerGroupResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ExtraSessionTypeEnum`
        """
        return self._extra_session_type

    @extra_session_type.setter
    def extra_session_type(self, extra_session_type):
        r"""Sets the extra_session_type of this ShowServerGroupResponse.

        :param extra_session_type: The extra_session_type of this ShowServerGroupResponse.
        :type extra_session_type: :class:`huaweicloudsdkworkspaceapp.v1.ExtraSessionTypeEnum`
        """
        self._extra_session_type = extra_session_type

    @property
    def extra_session_size(self):
        r"""Gets the extra_session_size of this ShowServerGroupResponse.

        付费会话个数。

        :return: The extra_session_size of this ShowServerGroupResponse.
        :rtype: int
        """
        return self._extra_session_size

    @extra_session_size.setter
    def extra_session_size(self, extra_session_size):
        r"""Sets the extra_session_size of this ShowServerGroupResponse.

        付费会话个数。

        :param extra_session_size: The extra_session_size of this ShowServerGroupResponse.
        :type extra_session_size: int
        """
        self._extra_session_size = extra_session_size

    @property
    def app_type(self):
        r"""Gets the app_type of this ShowServerGroupResponse.

        :return: The app_type of this ShowServerGroupResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ShowServerGroupResponse.

        :param app_type: The app_type of this ShowServerGroupResponse.
        :type app_type: :class:`huaweicloudsdkworkspaceapp.v1.AppTypeEnum`
        """
        self._app_type = app_type

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowServerGroupResponse.

        服务器组创建时间。

        :return: The create_time of this ShowServerGroupResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowServerGroupResponse.

        服务器组创建时间。

        :param create_time: The create_time of this ShowServerGroupResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowServerGroupResponse.

        服务器组更新时间。

        :return: The update_time of this ShowServerGroupResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowServerGroupResponse.

        服务器组更新时间。

        :param update_time: The update_time of this ShowServerGroupResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def storage_mount_policy(self):
        r"""Gets the storage_mount_policy of this ShowServerGroupResponse.

        :return: The storage_mount_policy of this ShowServerGroupResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.StorageFolderMountType`
        """
        return self._storage_mount_policy

    @storage_mount_policy.setter
    def storage_mount_policy(self, storage_mount_policy):
        r"""Sets the storage_mount_policy of this ShowServerGroupResponse.

        :param storage_mount_policy: The storage_mount_policy of this ShowServerGroupResponse.
        :type storage_mount_policy: :class:`huaweicloudsdkworkspaceapp.v1.StorageFolderMountType`
        """
        self._storage_mount_policy = storage_mount_policy

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowServerGroupResponse.

        企业项目ID(0表示默认企业项目Id)。

        :return: The enterprise_project_id of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowServerGroupResponse.

        企业项目ID(0表示默认企业项目Id)。

        :param enterprise_project_id: The enterprise_project_id of this ShowServerGroupResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def primary_server_group_ids(self):
        r"""Gets the primary_server_group_ids of this ShowServerGroupResponse.

        主服务器组id列表。

        :return: The primary_server_group_ids of this ShowServerGroupResponse.
        :rtype: list[str]
        """
        return self._primary_server_group_ids

    @primary_server_group_ids.setter
    def primary_server_group_ids(self, primary_server_group_ids):
        r"""Sets the primary_server_group_ids of this ShowServerGroupResponse.

        主服务器组id列表。

        :param primary_server_group_ids: The primary_server_group_ids of this ShowServerGroupResponse.
        :type primary_server_group_ids: list[str]
        """
        self._primary_server_group_ids = primary_server_group_ids

    @property
    def secondary_server_group_ids(self):
        r"""Gets the secondary_server_group_ids of this ShowServerGroupResponse.

        备服务器组id列表。

        :return: The secondary_server_group_ids of this ShowServerGroupResponse.
        :rtype: list[str]
        """
        return self._secondary_server_group_ids

    @secondary_server_group_ids.setter
    def secondary_server_group_ids(self, secondary_server_group_ids):
        r"""Sets the secondary_server_group_ids of this ShowServerGroupResponse.

        备服务器组id列表。

        :param secondary_server_group_ids: The secondary_server_group_ids of this ShowServerGroupResponse.
        :type secondary_server_group_ids: list[str]
        """
        self._secondary_server_group_ids = secondary_server_group_ids

    @property
    def server_group_status(self):
        r"""Gets the server_group_status of this ShowServerGroupResponse.

        服务器是否处于启用状态，true表示处于启用状态 false表示处于禁用状态。

        :return: The server_group_status of this ShowServerGroupResponse.
        :rtype: bool
        """
        return self._server_group_status

    @server_group_status.setter
    def server_group_status(self, server_group_status):
        r"""Sets the server_group_status of this ShowServerGroupResponse.

        服务器是否处于启用状态，true表示处于启用状态 false表示处于禁用状态。

        :param server_group_status: The server_group_status of this ShowServerGroupResponse.
        :type server_group_status: bool
        """
        self._server_group_status = server_group_status

    @property
    def site_type(self):
        r"""Gets the site_type of this ShowServerGroupResponse.

        站点类型 - CENTER/IES。

        :return: The site_type of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._site_type

    @site_type.setter
    def site_type(self, site_type):
        r"""Sets the site_type of this ShowServerGroupResponse.

        站点类型 - CENTER/IES。

        :param site_type: The site_type of this ShowServerGroupResponse.
        :type site_type: str
        """
        self._site_type = site_type

    @property
    def site_id(self):
        r"""Gets the site_id of this ShowServerGroupResponse.

        站点id。

        :return: The site_id of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this ShowServerGroupResponse.

        站点id。

        :param site_id: The site_id of this ShowServerGroupResponse.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def app_server_flavor_count(self):
        r"""Gets the app_server_flavor_count of this ShowServerGroupResponse.

        服务器配置总数量。

        :return: The app_server_flavor_count of this ShowServerGroupResponse.
        :rtype: int
        """
        return self._app_server_flavor_count

    @app_server_flavor_count.setter
    def app_server_flavor_count(self, app_server_flavor_count):
        r"""Sets the app_server_flavor_count of this ShowServerGroupResponse.

        服务器配置总数量。

        :param app_server_flavor_count: The app_server_flavor_count of this ShowServerGroupResponse.
        :type app_server_flavor_count: int
        """
        self._app_server_flavor_count = app_server_flavor_count

    @property
    def app_server_count(self):
        r"""Gets the app_server_count of this ShowServerGroupResponse.

        服务器总数量。

        :return: The app_server_count of this ShowServerGroupResponse.
        :rtype: int
        """
        return self._app_server_count

    @app_server_count.setter
    def app_server_count(self, app_server_count):
        r"""Sets the app_server_count of this ShowServerGroupResponse.

        服务器总数量。

        :param app_server_count: The app_server_count of this ShowServerGroupResponse.
        :type app_server_count: int
        """
        self._app_server_count = app_server_count

    @property
    def app_group_count(self):
        r"""Gets the app_group_count of this ShowServerGroupResponse.

        关联应用组的总数量。

        :return: The app_group_count of this ShowServerGroupResponse.
        :rtype: int
        """
        return self._app_group_count

    @app_group_count.setter
    def app_group_count(self, app_group_count):
        r"""Sets the app_group_count of this ShowServerGroupResponse.

        关联应用组的总数量。

        :param app_group_count: The app_group_count of this ShowServerGroupResponse.
        :type app_group_count: int
        """
        self._app_group_count = app_group_count

    @property
    def image_name(self):
        r"""Gets the image_name of this ShowServerGroupResponse.

        镜像名称。

        :return: The image_name of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ShowServerGroupResponse.

        镜像名称。

        :param image_name: The image_name of this ShowServerGroupResponse.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def product_info(self):
        r"""Gets the product_info of this ShowServerGroupResponse.

        :return: The product_info of this ShowServerGroupResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ProductInfo`
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        r"""Sets the product_info of this ShowServerGroupResponse.

        :param product_info: The product_info of this ShowServerGroupResponse.
        :type product_info: :class:`huaweicloudsdkworkspaceapp.v1.ProductInfo`
        """
        self._product_info = product_info

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this ShowServerGroupResponse.

        子网名称。

        :return: The subnet_name of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this ShowServerGroupResponse.

        子网名称。

        :param subnet_name: The subnet_name of this ShowServerGroupResponse.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def scaling_policy(self):
        r"""Gets the scaling_policy of this ShowServerGroupResponse.

        :return: The scaling_policy of this ShowServerGroupResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ScalingPolicy`
        """
        return self._scaling_policy

    @scaling_policy.setter
    def scaling_policy(self, scaling_policy):
        r"""Sets the scaling_policy of this ShowServerGroupResponse.

        :param scaling_policy: The scaling_policy of this ShowServerGroupResponse.
        :type scaling_policy: :class:`huaweicloudsdkworkspaceapp.v1.ScalingPolicy`
        """
        self._scaling_policy = scaling_policy

    @property
    def tags(self):
        r"""Gets the tags of this ShowServerGroupResponse.

        标签信息。

        :return: The tags of this ShowServerGroupResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.TmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowServerGroupResponse.

        标签信息。

        :param tags: The tags of this ShowServerGroupResponse.
        :type tags: list[:class:`huaweicloudsdkworkspaceapp.v1.TmsTag`]
        """
        self._tags = tags

    @property
    def ou_name(self):
        r"""Gets the ou_name of this ShowServerGroupResponse.

        默认组织名称。

        :return: The ou_name of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        r"""Sets the ou_name of this ShowServerGroupResponse.

        默认组织名称。

        :param ou_name: The ou_name of this ShowServerGroupResponse.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def flavors(self):
        r"""Gets the flavors of this ShowServerGroupResponse.

        服务器规格列表。

        :return: The flavors of this ShowServerGroupResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.Flavor`]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        r"""Sets the flavors of this ShowServerGroupResponse.

        服务器规格列表。

        :param flavors: The flavors of this ShowServerGroupResponse.
        :type flavors: list[:class:`huaweicloudsdkworkspaceapp.v1.Flavor`]
        """
        self._flavors = flavors

    @property
    def project_name(self):
        r"""Gets the project_name of this ShowServerGroupResponse.

        项目名称。

        :return: The project_name of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ShowServerGroupResponse.

        项目名称。

        :param project_name: The project_name of this ShowServerGroupResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def image_min_disk(self):
        r"""Gets the image_min_disk of this ShowServerGroupResponse.

        镜像运行的最小内存，单位为MB，默认设置为0。

        :return: The image_min_disk of this ShowServerGroupResponse.
        :rtype: int
        """
        return self._image_min_disk

    @image_min_disk.setter
    def image_min_disk(self, image_min_disk):
        r"""Sets the image_min_disk of this ShowServerGroupResponse.

        镜像运行的最小内存，单位为MB，默认设置为0。

        :param image_min_disk: The image_min_disk of this ShowServerGroupResponse.
        :type image_min_disk: int
        """
        self._image_min_disk = image_min_disk

    @property
    def route_policy(self):
        r"""Gets the route_policy of this ShowServerGroupResponse.

        :return: The route_policy of this ShowServerGroupResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.RoutePolicy`
        """
        return self._route_policy

    @route_policy.setter
    def route_policy(self, route_policy):
        r"""Sets the route_policy of this ShowServerGroupResponse.

        :param route_policy: The route_policy of this ShowServerGroupResponse.
        :type route_policy: :class:`huaweicloudsdkworkspaceapp.v1.RoutePolicy`
        """
        self._route_policy = route_policy

    @property
    def image_product_id(self):
        r"""Gets the image_product_id of this ShowServerGroupResponse.

        镜像的产品id。

        :return: The image_product_id of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._image_product_id

    @image_product_id.setter
    def image_product_id(self, image_product_id):
        r"""Sets the image_product_id of this ShowServerGroupResponse.

        镜像的产品id。

        :param image_product_id: The image_product_id of this ShowServerGroupResponse.
        :type image_product_id: str
        """
        self._image_product_id = image_product_id

    @property
    def image_type(self):
        r"""Gets the image_type of this ShowServerGroupResponse.

        镜像类型。

        :return: The image_type of this ShowServerGroupResponse.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ShowServerGroupResponse.

        镜像类型。

        :param image_type: The image_type of this ShowServerGroupResponse.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def ip_virtual(self):
        r"""Gets the ip_virtual of this ShowServerGroupResponse.

        :return: The ip_virtual of this ShowServerGroupResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.IpVirtual`
        """
        return self._ip_virtual

    @ip_virtual.setter
    def ip_virtual(self, ip_virtual):
        r"""Sets the ip_virtual of this ShowServerGroupResponse.

        :param ip_virtual: The ip_virtual of this ShowServerGroupResponse.
        :type ip_virtual: :class:`huaweicloudsdkworkspaceapp.v1.IpVirtual`
        """
        self._ip_virtual = ip_virtual

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
        if not isinstance(other, ShowServerGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
