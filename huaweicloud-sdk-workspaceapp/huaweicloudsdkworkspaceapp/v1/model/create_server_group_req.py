# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServerGroupReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'image_id': 'str',
        'image_product_id': 'str',
        'image_type': 'str',
        'os_type': 'str',
        'description': 'str',
        'route_policy': 'RoutePolicy',
        'product_id': 'str',
        'flavor_id': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'system_disk_type': 'str',
        'system_disk_size': 'int',
        'ou_name': 'str',
        'cluster_id': 'str',
        'availability_zone': 'str',
        'ip_virtual': 'IpVirtual',
        'is_vdi': 'bool',
        'app_type': 'str',
        'extra_session_type': 'str',
        'extra_session_size': 'int',
        'tags': 'list[TmsTag]',
        'enterprise_project_id': 'str',
        'primary_server_group_id': 'str',
        'server_group_status': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'image_id': 'image_id',
        'image_product_id': 'image_product_id',
        'image_type': 'image_type',
        'os_type': 'os_type',
        'description': 'description',
        'route_policy': 'route_policy',
        'product_id': 'product_id',
        'flavor_id': 'flavor_id',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'system_disk_type': 'system_disk_type',
        'system_disk_size': 'system_disk_size',
        'ou_name': 'ou_name',
        'cluster_id': 'cluster_id',
        'availability_zone': 'availability_zone',
        'ip_virtual': 'ip_virtual',
        'is_vdi': 'is_vdi',
        'app_type': 'app_type',
        'extra_session_type': 'extra_session_type',
        'extra_session_size': 'extra_session_size',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'primary_server_group_id': 'primary_server_group_id',
        'server_group_status': 'server_group_status'
    }

    def __init__(self, name=None, image_id=None, image_product_id=None, image_type=None, os_type=None, description=None, route_policy=None, product_id=None, flavor_id=None, vpc_id=None, subnet_id=None, system_disk_type=None, system_disk_size=None, ou_name=None, cluster_id=None, availability_zone=None, ip_virtual=None, is_vdi=None, app_type=None, extra_session_type=None, extra_session_size=None, tags=None, enterprise_project_id=None, primary_server_group_id=None, server_group_status=None):
        r"""CreateServerGroupReq

        The model defined in huaweicloud sdk

        :param name: 服务器组名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成，不能有空格。 2. 长度范围1~64个字符。
        :type name: str
        :param image_id: 服务器组关联的镜像ID，用于创建对应组下的云服务器。
        :type image_id: str
        :param image_product_id: 服务器组的镜像产品ID，当镜像为云市场镜像时，该字段必填。
        :type image_product_id: str
        :param image_type: 镜像类型： * &#x60;gold&#x60; - 云市场镜像 * &#x60;public&#x60; - 公共镜像 * &#x60;private&#x60; - 私有镜像 * &#x60;shared&#x60; - 共享镜像 * &#x60;other&#x60; - 其他
        :type image_type: str
        :param os_type: 系统类型，当前仅支持Windows。 * &#x60;Linux&#x60; - * &#x60;Windows&#x60; - * &#x60;Other&#x60; -
        :type os_type: str
        :param description: 服务器组描述。
        :type description: str
        :param route_policy: 
        :type route_policy: :class:`huaweicloudsdkworkspaceapp.v1.RoutePolicy`
        :param product_id: 产品ID。 &gt; - 获取方式详见产品套餐管理ListProduct：\&quot;GET  /v1/{project_id}/product\&quot;。
        :type product_id: str
        :param flavor_id: 规格ID。
        :type flavor_id: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 网卡对应的子网ID。
        :type subnet_id: str
        :param system_disk_type: 磁盘类型，获取可用磁盘类型详见接口磁盘管理ListVolumeType。 * &#x60;ESSD&#x60; - 极速型SSD * &#x60;SSD&#x60; - 超高IO * &#x60;GPSSD&#x60; - 通用型SSD * &#x60;SAS&#x60; - 高IO * &#x60;SATA&#x60; - 普通IO
        :type system_disk_type: str
        :param system_disk_size: 磁盘容量，单位GB。
        :type system_disk_size: int
        :param ou_name: 默认组织名称。
        :type ou_name: str
        :param cluster_id: 云服务器系统盘对应的存储池的ID。
        :type cluster_id: str
        :param availability_zone: 可用分区。 &gt; - 将服务创建到指定的可用分区，如果不指定则使用系统随机的可用分区。 &gt; - 获取方式详见可用区管理ListAvailabilityZone：\&quot;GET  /v1/{project_id}/availability-zone\&quot;。
        :type availability_zone: str
        :param ip_virtual: 
        :type ip_virtual: :class:`huaweicloudsdkworkspaceapp.v1.IpVirtual`
        :param is_vdi: 是否为vdi单会话模式。
        :type is_vdi: bool
        :param app_type: 服务器组应用类型： * &#x60;SESSION_DESKTOP_APP&#x60; - 会话桌面app * &#x60;COMMON_APP&#x60; - 普通app
        :type app_type: str
        :param extra_session_type: 付费会话类型 * &#x60;GPU&#x60; - GPU规格会话 * &#x60;CPU&#x60; - 普通CPU规格会话
        :type extra_session_type: str
        :param extra_session_size: 付费会话数，单位/个。
        :type extra_session_size: int
        :param tags: 标签信息，最多包含20个key,不允许重复。
        :type tags: list[:class:`huaweicloudsdkworkspaceapp.v1.TmsTag`]
        :param enterprise_project_id: 企业项目ID,仅企业项目需配置(字段为空或者0表示使用默认default企业项目)。
        :type enterprise_project_id: str
        :param primary_server_group_id: 主服务器组id,绑定主服务器组，则创建的是备服务器。
        :type primary_server_group_id: str
        :param server_group_status: 是否启用服务器组。
        :type server_group_status: bool
        """
        
        

        self._name = None
        self._image_id = None
        self._image_product_id = None
        self._image_type = None
        self._os_type = None
        self._description = None
        self._route_policy = None
        self._product_id = None
        self._flavor_id = None
        self._vpc_id = None
        self._subnet_id = None
        self._system_disk_type = None
        self._system_disk_size = None
        self._ou_name = None
        self._cluster_id = None
        self._availability_zone = None
        self._ip_virtual = None
        self._is_vdi = None
        self._app_type = None
        self._extra_session_type = None
        self._extra_session_size = None
        self._tags = None
        self._enterprise_project_id = None
        self._primary_server_group_id = None
        self._server_group_status = None
        self.discriminator = None

        self.name = name
        self.image_id = image_id
        if image_product_id is not None:
            self.image_product_id = image_product_id
        self.image_type = image_type
        self.os_type = os_type
        if description is not None:
            self.description = description
        if route_policy is not None:
            self.route_policy = route_policy
        self.product_id = product_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.system_disk_type = system_disk_type
        self.system_disk_size = system_disk_size
        if ou_name is not None:
            self.ou_name = ou_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if ip_virtual is not None:
            self.ip_virtual = ip_virtual
        if is_vdi is not None:
            self.is_vdi = is_vdi
        if app_type is not None:
            self.app_type = app_type
        if extra_session_type is not None:
            self.extra_session_type = extra_session_type
        if extra_session_size is not None:
            self.extra_session_size = extra_session_size
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if primary_server_group_id is not None:
            self.primary_server_group_id = primary_server_group_id
        if server_group_status is not None:
            self.server_group_status = server_group_status

    @property
    def name(self):
        r"""Gets the name of this CreateServerGroupReq.

        服务器组名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成，不能有空格。 2. 长度范围1~64个字符。

        :return: The name of this CreateServerGroupReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateServerGroupReq.

        服务器组名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-组成，不能有空格。 2. 长度范围1~64个字符。

        :param name: The name of this CreateServerGroupReq.
        :type name: str
        """
        self._name = name

    @property
    def image_id(self):
        r"""Gets the image_id of this CreateServerGroupReq.

        服务器组关联的镜像ID，用于创建对应组下的云服务器。

        :return: The image_id of this CreateServerGroupReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this CreateServerGroupReq.

        服务器组关联的镜像ID，用于创建对应组下的云服务器。

        :param image_id: The image_id of this CreateServerGroupReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_product_id(self):
        r"""Gets the image_product_id of this CreateServerGroupReq.

        服务器组的镜像产品ID，当镜像为云市场镜像时，该字段必填。

        :return: The image_product_id of this CreateServerGroupReq.
        :rtype: str
        """
        return self._image_product_id

    @image_product_id.setter
    def image_product_id(self, image_product_id):
        r"""Sets the image_product_id of this CreateServerGroupReq.

        服务器组的镜像产品ID，当镜像为云市场镜像时，该字段必填。

        :param image_product_id: The image_product_id of this CreateServerGroupReq.
        :type image_product_id: str
        """
        self._image_product_id = image_product_id

    @property
    def image_type(self):
        r"""Gets the image_type of this CreateServerGroupReq.

        镜像类型： * `gold` - 云市场镜像 * `public` - 公共镜像 * `private` - 私有镜像 * `shared` - 共享镜像 * `other` - 其他

        :return: The image_type of this CreateServerGroupReq.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this CreateServerGroupReq.

        镜像类型： * `gold` - 云市场镜像 * `public` - 公共镜像 * `private` - 私有镜像 * `shared` - 共享镜像 * `other` - 其他

        :param image_type: The image_type of this CreateServerGroupReq.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def os_type(self):
        r"""Gets the os_type of this CreateServerGroupReq.

        系统类型，当前仅支持Windows。 * `Linux` - * `Windows` - * `Other` -

        :return: The os_type of this CreateServerGroupReq.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this CreateServerGroupReq.

        系统类型，当前仅支持Windows。 * `Linux` - * `Windows` - * `Other` -

        :param os_type: The os_type of this CreateServerGroupReq.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def description(self):
        r"""Gets the description of this CreateServerGroupReq.

        服务器组描述。

        :return: The description of this CreateServerGroupReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateServerGroupReq.

        服务器组描述。

        :param description: The description of this CreateServerGroupReq.
        :type description: str
        """
        self._description = description

    @property
    def route_policy(self):
        r"""Gets the route_policy of this CreateServerGroupReq.

        :return: The route_policy of this CreateServerGroupReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.RoutePolicy`
        """
        return self._route_policy

    @route_policy.setter
    def route_policy(self, route_policy):
        r"""Sets the route_policy of this CreateServerGroupReq.

        :param route_policy: The route_policy of this CreateServerGroupReq.
        :type route_policy: :class:`huaweicloudsdkworkspaceapp.v1.RoutePolicy`
        """
        self._route_policy = route_policy

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateServerGroupReq.

        产品ID。 > - 获取方式详见产品套餐管理ListProduct：\"GET  /v1/{project_id}/product\"。

        :return: The product_id of this CreateServerGroupReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateServerGroupReq.

        产品ID。 > - 获取方式详见产品套餐管理ListProduct：\"GET  /v1/{project_id}/product\"。

        :param product_id: The product_id of this CreateServerGroupReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this CreateServerGroupReq.

        规格ID。

        :return: The flavor_id of this CreateServerGroupReq.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this CreateServerGroupReq.

        规格ID。

        :param flavor_id: The flavor_id of this CreateServerGroupReq.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateServerGroupReq.

        虚拟私有云ID。

        :return: The vpc_id of this CreateServerGroupReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateServerGroupReq.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this CreateServerGroupReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateServerGroupReq.

        网卡对应的子网ID。

        :return: The subnet_id of this CreateServerGroupReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateServerGroupReq.

        网卡对应的子网ID。

        :param subnet_id: The subnet_id of this CreateServerGroupReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def system_disk_type(self):
        r"""Gets the system_disk_type of this CreateServerGroupReq.

        磁盘类型，获取可用磁盘类型详见接口磁盘管理ListVolumeType。 * `ESSD` - 极速型SSD * `SSD` - 超高IO * `GPSSD` - 通用型SSD * `SAS` - 高IO * `SATA` - 普通IO

        :return: The system_disk_type of this CreateServerGroupReq.
        :rtype: str
        """
        return self._system_disk_type

    @system_disk_type.setter
    def system_disk_type(self, system_disk_type):
        r"""Sets the system_disk_type of this CreateServerGroupReq.

        磁盘类型，获取可用磁盘类型详见接口磁盘管理ListVolumeType。 * `ESSD` - 极速型SSD * `SSD` - 超高IO * `GPSSD` - 通用型SSD * `SAS` - 高IO * `SATA` - 普通IO

        :param system_disk_type: The system_disk_type of this CreateServerGroupReq.
        :type system_disk_type: str
        """
        self._system_disk_type = system_disk_type

    @property
    def system_disk_size(self):
        r"""Gets the system_disk_size of this CreateServerGroupReq.

        磁盘容量，单位GB。

        :return: The system_disk_size of this CreateServerGroupReq.
        :rtype: int
        """
        return self._system_disk_size

    @system_disk_size.setter
    def system_disk_size(self, system_disk_size):
        r"""Sets the system_disk_size of this CreateServerGroupReq.

        磁盘容量，单位GB。

        :param system_disk_size: The system_disk_size of this CreateServerGroupReq.
        :type system_disk_size: int
        """
        self._system_disk_size = system_disk_size

    @property
    def ou_name(self):
        r"""Gets the ou_name of this CreateServerGroupReq.

        默认组织名称。

        :return: The ou_name of this CreateServerGroupReq.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        r"""Sets the ou_name of this CreateServerGroupReq.

        默认组织名称。

        :param ou_name: The ou_name of this CreateServerGroupReq.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CreateServerGroupReq.

        云服务器系统盘对应的存储池的ID。

        :return: The cluster_id of this CreateServerGroupReq.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CreateServerGroupReq.

        云服务器系统盘对应的存储池的ID。

        :param cluster_id: The cluster_id of this CreateServerGroupReq.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CreateServerGroupReq.

        可用分区。 > - 将服务创建到指定的可用分区，如果不指定则使用系统随机的可用分区。 > - 获取方式详见可用区管理ListAvailabilityZone：\"GET  /v1/{project_id}/availability-zone\"。

        :return: The availability_zone of this CreateServerGroupReq.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CreateServerGroupReq.

        可用分区。 > - 将服务创建到指定的可用分区，如果不指定则使用系统随机的可用分区。 > - 获取方式详见可用区管理ListAvailabilityZone：\"GET  /v1/{project_id}/availability-zone\"。

        :param availability_zone: The availability_zone of this CreateServerGroupReq.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def ip_virtual(self):
        r"""Gets the ip_virtual of this CreateServerGroupReq.

        :return: The ip_virtual of this CreateServerGroupReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.IpVirtual`
        """
        return self._ip_virtual

    @ip_virtual.setter
    def ip_virtual(self, ip_virtual):
        r"""Sets the ip_virtual of this CreateServerGroupReq.

        :param ip_virtual: The ip_virtual of this CreateServerGroupReq.
        :type ip_virtual: :class:`huaweicloudsdkworkspaceapp.v1.IpVirtual`
        """
        self._ip_virtual = ip_virtual

    @property
    def is_vdi(self):
        r"""Gets the is_vdi of this CreateServerGroupReq.

        是否为vdi单会话模式。

        :return: The is_vdi of this CreateServerGroupReq.
        :rtype: bool
        """
        return self._is_vdi

    @is_vdi.setter
    def is_vdi(self, is_vdi):
        r"""Sets the is_vdi of this CreateServerGroupReq.

        是否为vdi单会话模式。

        :param is_vdi: The is_vdi of this CreateServerGroupReq.
        :type is_vdi: bool
        """
        self._is_vdi = is_vdi

    @property
    def app_type(self):
        r"""Gets the app_type of this CreateServerGroupReq.

        服务器组应用类型： * `SESSION_DESKTOP_APP` - 会话桌面app * `COMMON_APP` - 普通app

        :return: The app_type of this CreateServerGroupReq.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this CreateServerGroupReq.

        服务器组应用类型： * `SESSION_DESKTOP_APP` - 会话桌面app * `COMMON_APP` - 普通app

        :param app_type: The app_type of this CreateServerGroupReq.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def extra_session_type(self):
        r"""Gets the extra_session_type of this CreateServerGroupReq.

        付费会话类型 * `GPU` - GPU规格会话 * `CPU` - 普通CPU规格会话

        :return: The extra_session_type of this CreateServerGroupReq.
        :rtype: str
        """
        return self._extra_session_type

    @extra_session_type.setter
    def extra_session_type(self, extra_session_type):
        r"""Sets the extra_session_type of this CreateServerGroupReq.

        付费会话类型 * `GPU` - GPU规格会话 * `CPU` - 普通CPU规格会话

        :param extra_session_type: The extra_session_type of this CreateServerGroupReq.
        :type extra_session_type: str
        """
        self._extra_session_type = extra_session_type

    @property
    def extra_session_size(self):
        r"""Gets the extra_session_size of this CreateServerGroupReq.

        付费会话数，单位/个。

        :return: The extra_session_size of this CreateServerGroupReq.
        :rtype: int
        """
        return self._extra_session_size

    @extra_session_size.setter
    def extra_session_size(self, extra_session_size):
        r"""Sets the extra_session_size of this CreateServerGroupReq.

        付费会话数，单位/个。

        :param extra_session_size: The extra_session_size of this CreateServerGroupReq.
        :type extra_session_size: int
        """
        self._extra_session_size = extra_session_size

    @property
    def tags(self):
        r"""Gets the tags of this CreateServerGroupReq.

        标签信息，最多包含20个key,不允许重复。

        :return: The tags of this CreateServerGroupReq.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.TmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateServerGroupReq.

        标签信息，最多包含20个key,不允许重复。

        :param tags: The tags of this CreateServerGroupReq.
        :type tags: list[:class:`huaweicloudsdkworkspaceapp.v1.TmsTag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateServerGroupReq.

        企业项目ID,仅企业项目需配置(字段为空或者0表示使用默认default企业项目)。

        :return: The enterprise_project_id of this CreateServerGroupReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateServerGroupReq.

        企业项目ID,仅企业项目需配置(字段为空或者0表示使用默认default企业项目)。

        :param enterprise_project_id: The enterprise_project_id of this CreateServerGroupReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def primary_server_group_id(self):
        r"""Gets the primary_server_group_id of this CreateServerGroupReq.

        主服务器组id,绑定主服务器组，则创建的是备服务器。

        :return: The primary_server_group_id of this CreateServerGroupReq.
        :rtype: str
        """
        return self._primary_server_group_id

    @primary_server_group_id.setter
    def primary_server_group_id(self, primary_server_group_id):
        r"""Sets the primary_server_group_id of this CreateServerGroupReq.

        主服务器组id,绑定主服务器组，则创建的是备服务器。

        :param primary_server_group_id: The primary_server_group_id of this CreateServerGroupReq.
        :type primary_server_group_id: str
        """
        self._primary_server_group_id = primary_server_group_id

    @property
    def server_group_status(self):
        r"""Gets the server_group_status of this CreateServerGroupReq.

        是否启用服务器组。

        :return: The server_group_status of this CreateServerGroupReq.
        :rtype: bool
        """
        return self._server_group_status

    @server_group_status.setter
    def server_group_status(self, server_group_status):
        r"""Sets the server_group_status of this CreateServerGroupReq.

        是否启用服务器组。

        :param server_group_status: The server_group_status of this CreateServerGroupReq.
        :type server_group_status: bool
        """
        self._server_group_status = server_group_status

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
        if not isinstance(other, CreateServerGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
