# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlanceCreateImageMetadataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'visibility': 'str',
        'name': 'str',
        'protected': 'bool',
        'container_format': 'str',
        'disk_format': 'str',
        'tags': 'list[str]',
        'min_ram': 'int',
        'min_disk': 'int',
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        '_self': 'str',
        'id': 'str',
        'file': 'str',
        'schema': 'str',
        'image_source_type': 'str',
        'image_size': 'str',
        'isregistered': 'str',
        'os_version': 'str',
        'os_type': 'str',
        'platform': 'str',
        'os_bit': 'str',
        'imagetype': 'str',
        'virtual_env_type': 'str',
        'owner': 'str',
        'virtual_size': 'int',
        'properties': 'object',
        'root_origin': 'str',
        'checksum': 'str',
        'size': 'int'
    }

    attribute_map = {
        'visibility': 'visibility',
        'name': 'name',
        'protected': 'protected',
        'container_format': 'container_format',
        'disk_format': 'disk_format',
        'tags': 'tags',
        'min_ram': 'min_ram',
        'min_disk': 'min_disk',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        '_self': 'self',
        'id': 'id',
        'file': 'file',
        'schema': 'schema',
        'image_source_type': '__image_source_type',
        'image_size': '__image_size',
        'isregistered': '__isregistered',
        'os_version': '__os_version',
        'os_type': '__os_type',
        'platform': '__platform',
        'os_bit': '__os_bit',
        'imagetype': '__imagetype',
        'virtual_env_type': 'virtual_env_type',
        'owner': 'owner',
        'virtual_size': 'virtual_size',
        'properties': 'properties',
        'root_origin': '__root_origin',
        'checksum': 'checksum',
        'size': 'size'
    }

    def __init__(self, visibility=None, name=None, protected=None, container_format=None, disk_format=None, tags=None, min_ram=None, min_disk=None, status=None, created_at=None, updated_at=None, _self=None, id=None, file=None, schema=None, image_source_type=None, image_size=None, isregistered=None, os_version=None, os_type=None, platform=None, os_bit=None, imagetype=None, virtual_env_type=None, owner=None, virtual_size=None, properties=None, root_origin=None, checksum=None, size=None):
        r"""GlanceCreateImageMetadataResponse

        The model defined in huaweicloud sdk

        :param visibility: 其他租户是否可见。取值为private。
        :type visibility: str
        :param name: 镜像名称，如果未指定name的取值，则默认为空，但是使用该镜像创建虚拟机会失败。名称的长度为1～128位。
        :type name: str
        :param protected: 镜像是否被保护，保护后的镜像不可删除。取值为false
        :type protected: bool
        :param container_format: 容器格式。取值为bare。
        :type container_format: str
        :param disk_format: 镜像文件格式。目前支持vhd、zvhd、raw、qcow2。默认值是vhd。
        :type disk_format: str
        :param tags: 镜像标签列表。长度为1～255位。
        :type tags: list[str]
        :param min_ram: 镜像运行最小内存，单位为MB。取值参考ECS规格限制，一般设置为0。云服务器的规格限制，请参见规格清单。
        :type min_ram: int
        :param min_disk: 镜像运行需要的最小磁盘容量，单位为GB 。取值为40～1024GB。必须大于镜像系统盘容量，否则创建云主机云服务器可能失败。
        :type min_disk: int
        :param status: 镜像状态。取值如下：queued：表示镜像元数据已经创建成功，等待上传镜像文件。saving：表示镜像正在上传文件到后端存储。deleted：表示镜像已经删除。killed：表示镜像上传错误。active：表示镜像可以正常使用。
        :type status: str
        :param created_at: 创建时间。格式为UTC时间。
        :type created_at: str
        :param updated_at: 更新时间。格式为UTC时间。
        :type updated_at: str
        :param _self: 本镜像链接。
        :type _self: str
        :param id: 镜像ID，用户调用创建镜像接口后，需保存该镜像的ID，用来调用上传镜像接口完成镜像上传。
        :type id: str
        :param file: 上传下载镜像文件的地址链接。
        :type file: str
        :param schema: 视图链接。
        :type schema: str
        :param image_source_type: 镜像后端存储类型，目前支持uds。
        :type image_source_type: str
        :param image_size: 镜像大小。单位为字节。
        :type image_size: str
        :param isregistered: 镜像是否注册。只有已注册的镜像才能在Portal界面上查询到。取值为true。
        :type isregistered: str
        :param os_version: 镜像的操作系统具体版本。
        :type os_version: str
        :param os_type: 镜像的操作系统类型，取值由__os_version确定。支持Windows、Linux和other。
        :type os_type: str
        :param platform: 表示镜像支持的操作系统平台。取值由__os_version确定
        :type platform: str
        :param os_bit: 表示操作系统位数。取值由__os_version确定，取值为32或64。
        :type os_bit: str
        :param imagetype: 镜像类型。取值为private，表示私有镜像。
        :type imagetype: str
        :param virtual_env_type: 平台类型。镜像使用环境类型：FusionCompute、Ironic、DataImage。如果是云主机云服务器镜像，则取值为FusionCompute。如果是数据卷镜像则取值是DataImage。如果是物理机裸金属服务器镜像，则取值是Ironic。
        :type virtual_env_type: str
        :param owner: 镜像所属项目ID。
        :type owner: str
        :param virtual_size: 镜像虚拟大小。单位为字节。
        :type virtual_size: int
        :param properties: 镜像属性的集合，不表示具体的镜像属性
        :type properties: object
        :param root_origin: 表示当前镜像来源是从外部导入。取值：file
        :type root_origin: str
        :param checksum: 镜像文件md5值。
        :type checksum: str
        :param size: 目前暂时不使用。
        :type size: int
        """
        
        super(GlanceCreateImageMetadataResponse, self).__init__()

        self._visibility = None
        self._name = None
        self._protected = None
        self._container_format = None
        self._disk_format = None
        self._tags = None
        self._min_ram = None
        self._min_disk = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.__self = None
        self._id = None
        self._file = None
        self._schema = None
        self._image_source_type = None
        self._image_size = None
        self._isregistered = None
        self._os_version = None
        self._os_type = None
        self._platform = None
        self._os_bit = None
        self._imagetype = None
        self._virtual_env_type = None
        self._owner = None
        self._virtual_size = None
        self._properties = None
        self._root_origin = None
        self._checksum = None
        self._size = None
        self.discriminator = None

        if visibility is not None:
            self.visibility = visibility
        if name is not None:
            self.name = name
        if protected is not None:
            self.protected = protected
        if container_format is not None:
            self.container_format = container_format
        if disk_format is not None:
            self.disk_format = disk_format
        if tags is not None:
            self.tags = tags
        if min_ram is not None:
            self.min_ram = min_ram
        if min_disk is not None:
            self.min_disk = min_disk
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if _self is not None:
            self._self = _self
        if id is not None:
            self.id = id
        if file is not None:
            self.file = file
        if schema is not None:
            self.schema = schema
        if image_source_type is not None:
            self.image_source_type = image_source_type
        if image_size is not None:
            self.image_size = image_size
        if isregistered is not None:
            self.isregistered = isregistered
        if os_version is not None:
            self.os_version = os_version
        if os_type is not None:
            self.os_type = os_type
        if platform is not None:
            self.platform = platform
        if os_bit is not None:
            self.os_bit = os_bit
        if imagetype is not None:
            self.imagetype = imagetype
        if virtual_env_type is not None:
            self.virtual_env_type = virtual_env_type
        if owner is not None:
            self.owner = owner
        if virtual_size is not None:
            self.virtual_size = virtual_size
        if properties is not None:
            self.properties = properties
        if root_origin is not None:
            self.root_origin = root_origin
        if checksum is not None:
            self.checksum = checksum
        if size is not None:
            self.size = size

    @property
    def visibility(self):
        r"""Gets the visibility of this GlanceCreateImageMetadataResponse.

        其他租户是否可见。取值为private。

        :return: The visibility of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this GlanceCreateImageMetadataResponse.

        其他租户是否可见。取值为private。

        :param visibility: The visibility of this GlanceCreateImageMetadataResponse.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def name(self):
        r"""Gets the name of this GlanceCreateImageMetadataResponse.

        镜像名称，如果未指定name的取值，则默认为空，但是使用该镜像创建虚拟机会失败。名称的长度为1～128位。

        :return: The name of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GlanceCreateImageMetadataResponse.

        镜像名称，如果未指定name的取值，则默认为空，但是使用该镜像创建虚拟机会失败。名称的长度为1～128位。

        :param name: The name of this GlanceCreateImageMetadataResponse.
        :type name: str
        """
        self._name = name

    @property
    def protected(self):
        r"""Gets the protected of this GlanceCreateImageMetadataResponse.

        镜像是否被保护，保护后的镜像不可删除。取值为false

        :return: The protected of this GlanceCreateImageMetadataResponse.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        r"""Sets the protected of this GlanceCreateImageMetadataResponse.

        镜像是否被保护，保护后的镜像不可删除。取值为false

        :param protected: The protected of this GlanceCreateImageMetadataResponse.
        :type protected: bool
        """
        self._protected = protected

    @property
    def container_format(self):
        r"""Gets the container_format of this GlanceCreateImageMetadataResponse.

        容器格式。取值为bare。

        :return: The container_format of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        r"""Sets the container_format of this GlanceCreateImageMetadataResponse.

        容器格式。取值为bare。

        :param container_format: The container_format of this GlanceCreateImageMetadataResponse.
        :type container_format: str
        """
        self._container_format = container_format

    @property
    def disk_format(self):
        r"""Gets the disk_format of this GlanceCreateImageMetadataResponse.

        镜像文件格式。目前支持vhd、zvhd、raw、qcow2。默认值是vhd。

        :return: The disk_format of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        r"""Sets the disk_format of this GlanceCreateImageMetadataResponse.

        镜像文件格式。目前支持vhd、zvhd、raw、qcow2。默认值是vhd。

        :param disk_format: The disk_format of this GlanceCreateImageMetadataResponse.
        :type disk_format: str
        """
        self._disk_format = disk_format

    @property
    def tags(self):
        r"""Gets the tags of this GlanceCreateImageMetadataResponse.

        镜像标签列表。长度为1～255位。

        :return: The tags of this GlanceCreateImageMetadataResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this GlanceCreateImageMetadataResponse.

        镜像标签列表。长度为1～255位。

        :param tags: The tags of this GlanceCreateImageMetadataResponse.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def min_ram(self):
        r"""Gets the min_ram of this GlanceCreateImageMetadataResponse.

        镜像运行最小内存，单位为MB。取值参考ECS规格限制，一般设置为0。云服务器的规格限制，请参见规格清单。

        :return: The min_ram of this GlanceCreateImageMetadataResponse.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        r"""Sets the min_ram of this GlanceCreateImageMetadataResponse.

        镜像运行最小内存，单位为MB。取值参考ECS规格限制，一般设置为0。云服务器的规格限制，请参见规格清单。

        :param min_ram: The min_ram of this GlanceCreateImageMetadataResponse.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def min_disk(self):
        r"""Gets the min_disk of this GlanceCreateImageMetadataResponse.

        镜像运行需要的最小磁盘容量，单位为GB 。取值为40～1024GB。必须大于镜像系统盘容量，否则创建云主机云服务器可能失败。

        :return: The min_disk of this GlanceCreateImageMetadataResponse.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        r"""Sets the min_disk of this GlanceCreateImageMetadataResponse.

        镜像运行需要的最小磁盘容量，单位为GB 。取值为40～1024GB。必须大于镜像系统盘容量，否则创建云主机云服务器可能失败。

        :param min_disk: The min_disk of this GlanceCreateImageMetadataResponse.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def status(self):
        r"""Gets the status of this GlanceCreateImageMetadataResponse.

        镜像状态。取值如下：queued：表示镜像元数据已经创建成功，等待上传镜像文件。saving：表示镜像正在上传文件到后端存储。deleted：表示镜像已经删除。killed：表示镜像上传错误。active：表示镜像可以正常使用。

        :return: The status of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GlanceCreateImageMetadataResponse.

        镜像状态。取值如下：queued：表示镜像元数据已经创建成功，等待上传镜像文件。saving：表示镜像正在上传文件到后端存储。deleted：表示镜像已经删除。killed：表示镜像上传错误。active：表示镜像可以正常使用。

        :param status: The status of this GlanceCreateImageMetadataResponse.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this GlanceCreateImageMetadataResponse.

        创建时间。格式为UTC时间。

        :return: The created_at of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this GlanceCreateImageMetadataResponse.

        创建时间。格式为UTC时间。

        :param created_at: The created_at of this GlanceCreateImageMetadataResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this GlanceCreateImageMetadataResponse.

        更新时间。格式为UTC时间。

        :return: The updated_at of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this GlanceCreateImageMetadataResponse.

        更新时间。格式为UTC时间。

        :param updated_at: The updated_at of this GlanceCreateImageMetadataResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def _self(self):
        r"""Gets the _self of this GlanceCreateImageMetadataResponse.

        本镜像链接。

        :return: The _self of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        r"""Sets the _self of this GlanceCreateImageMetadataResponse.

        本镜像链接。

        :param _self: The _self of this GlanceCreateImageMetadataResponse.
        :type _self: str
        """
        self.__self = _self

    @property
    def id(self):
        r"""Gets the id of this GlanceCreateImageMetadataResponse.

        镜像ID，用户调用创建镜像接口后，需保存该镜像的ID，用来调用上传镜像接口完成镜像上传。

        :return: The id of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GlanceCreateImageMetadataResponse.

        镜像ID，用户调用创建镜像接口后，需保存该镜像的ID，用来调用上传镜像接口完成镜像上传。

        :param id: The id of this GlanceCreateImageMetadataResponse.
        :type id: str
        """
        self._id = id

    @property
    def file(self):
        r"""Gets the file of this GlanceCreateImageMetadataResponse.

        上传下载镜像文件的地址链接。

        :return: The file of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this GlanceCreateImageMetadataResponse.

        上传下载镜像文件的地址链接。

        :param file: The file of this GlanceCreateImageMetadataResponse.
        :type file: str
        """
        self._file = file

    @property
    def schema(self):
        r"""Gets the schema of this GlanceCreateImageMetadataResponse.

        视图链接。

        :return: The schema of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this GlanceCreateImageMetadataResponse.

        视图链接。

        :param schema: The schema of this GlanceCreateImageMetadataResponse.
        :type schema: str
        """
        self._schema = schema

    @property
    def image_source_type(self):
        r"""Gets the image_source_type of this GlanceCreateImageMetadataResponse.

        镜像后端存储类型，目前支持uds。

        :return: The image_source_type of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._image_source_type

    @image_source_type.setter
    def image_source_type(self, image_source_type):
        r"""Sets the image_source_type of this GlanceCreateImageMetadataResponse.

        镜像后端存储类型，目前支持uds。

        :param image_source_type: The image_source_type of this GlanceCreateImageMetadataResponse.
        :type image_source_type: str
        """
        self._image_source_type = image_source_type

    @property
    def image_size(self):
        r"""Gets the image_size of this GlanceCreateImageMetadataResponse.

        镜像大小。单位为字节。

        :return: The image_size of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        r"""Sets the image_size of this GlanceCreateImageMetadataResponse.

        镜像大小。单位为字节。

        :param image_size: The image_size of this GlanceCreateImageMetadataResponse.
        :type image_size: str
        """
        self._image_size = image_size

    @property
    def isregistered(self):
        r"""Gets the isregistered of this GlanceCreateImageMetadataResponse.

        镜像是否注册。只有已注册的镜像才能在Portal界面上查询到。取值为true。

        :return: The isregistered of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._isregistered

    @isregistered.setter
    def isregistered(self, isregistered):
        r"""Sets the isregistered of this GlanceCreateImageMetadataResponse.

        镜像是否注册。只有已注册的镜像才能在Portal界面上查询到。取值为true。

        :param isregistered: The isregistered of this GlanceCreateImageMetadataResponse.
        :type isregistered: str
        """
        self._isregistered = isregistered

    @property
    def os_version(self):
        r"""Gets the os_version of this GlanceCreateImageMetadataResponse.

        镜像的操作系统具体版本。

        :return: The os_version of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this GlanceCreateImageMetadataResponse.

        镜像的操作系统具体版本。

        :param os_version: The os_version of this GlanceCreateImageMetadataResponse.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def os_type(self):
        r"""Gets the os_type of this GlanceCreateImageMetadataResponse.

        镜像的操作系统类型，取值由__os_version确定。支持Windows、Linux和other。

        :return: The os_type of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this GlanceCreateImageMetadataResponse.

        镜像的操作系统类型，取值由__os_version确定。支持Windows、Linux和other。

        :param os_type: The os_type of this GlanceCreateImageMetadataResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def platform(self):
        r"""Gets the platform of this GlanceCreateImageMetadataResponse.

        表示镜像支持的操作系统平台。取值由__os_version确定

        :return: The platform of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this GlanceCreateImageMetadataResponse.

        表示镜像支持的操作系统平台。取值由__os_version确定

        :param platform: The platform of this GlanceCreateImageMetadataResponse.
        :type platform: str
        """
        self._platform = platform

    @property
    def os_bit(self):
        r"""Gets the os_bit of this GlanceCreateImageMetadataResponse.

        表示操作系统位数。取值由__os_version确定，取值为32或64。

        :return: The os_bit of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        r"""Sets the os_bit of this GlanceCreateImageMetadataResponse.

        表示操作系统位数。取值由__os_version确定，取值为32或64。

        :param os_bit: The os_bit of this GlanceCreateImageMetadataResponse.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def imagetype(self):
        r"""Gets the imagetype of this GlanceCreateImageMetadataResponse.

        镜像类型。取值为private，表示私有镜像。

        :return: The imagetype of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._imagetype

    @imagetype.setter
    def imagetype(self, imagetype):
        r"""Sets the imagetype of this GlanceCreateImageMetadataResponse.

        镜像类型。取值为private，表示私有镜像。

        :param imagetype: The imagetype of this GlanceCreateImageMetadataResponse.
        :type imagetype: str
        """
        self._imagetype = imagetype

    @property
    def virtual_env_type(self):
        r"""Gets the virtual_env_type of this GlanceCreateImageMetadataResponse.

        平台类型。镜像使用环境类型：FusionCompute、Ironic、DataImage。如果是云主机云服务器镜像，则取值为FusionCompute。如果是数据卷镜像则取值是DataImage。如果是物理机裸金属服务器镜像，则取值是Ironic。

        :return: The virtual_env_type of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._virtual_env_type

    @virtual_env_type.setter
    def virtual_env_type(self, virtual_env_type):
        r"""Sets the virtual_env_type of this GlanceCreateImageMetadataResponse.

        平台类型。镜像使用环境类型：FusionCompute、Ironic、DataImage。如果是云主机云服务器镜像，则取值为FusionCompute。如果是数据卷镜像则取值是DataImage。如果是物理机裸金属服务器镜像，则取值是Ironic。

        :param virtual_env_type: The virtual_env_type of this GlanceCreateImageMetadataResponse.
        :type virtual_env_type: str
        """
        self._virtual_env_type = virtual_env_type

    @property
    def owner(self):
        r"""Gets the owner of this GlanceCreateImageMetadataResponse.

        镜像所属项目ID。

        :return: The owner of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this GlanceCreateImageMetadataResponse.

        镜像所属项目ID。

        :param owner: The owner of this GlanceCreateImageMetadataResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def virtual_size(self):
        r"""Gets the virtual_size of this GlanceCreateImageMetadataResponse.

        镜像虚拟大小。单位为字节。

        :return: The virtual_size of this GlanceCreateImageMetadataResponse.
        :rtype: int
        """
        return self._virtual_size

    @virtual_size.setter
    def virtual_size(self, virtual_size):
        r"""Sets the virtual_size of this GlanceCreateImageMetadataResponse.

        镜像虚拟大小。单位为字节。

        :param virtual_size: The virtual_size of this GlanceCreateImageMetadataResponse.
        :type virtual_size: int
        """
        self._virtual_size = virtual_size

    @property
    def properties(self):
        r"""Gets the properties of this GlanceCreateImageMetadataResponse.

        镜像属性的集合，不表示具体的镜像属性

        :return: The properties of this GlanceCreateImageMetadataResponse.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this GlanceCreateImageMetadataResponse.

        镜像属性的集合，不表示具体的镜像属性

        :param properties: The properties of this GlanceCreateImageMetadataResponse.
        :type properties: object
        """
        self._properties = properties

    @property
    def root_origin(self):
        r"""Gets the root_origin of this GlanceCreateImageMetadataResponse.

        表示当前镜像来源是从外部导入。取值：file

        :return: The root_origin of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._root_origin

    @root_origin.setter
    def root_origin(self, root_origin):
        r"""Sets the root_origin of this GlanceCreateImageMetadataResponse.

        表示当前镜像来源是从外部导入。取值：file

        :param root_origin: The root_origin of this GlanceCreateImageMetadataResponse.
        :type root_origin: str
        """
        self._root_origin = root_origin

    @property
    def checksum(self):
        r"""Gets the checksum of this GlanceCreateImageMetadataResponse.

        镜像文件md5值。

        :return: The checksum of this GlanceCreateImageMetadataResponse.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        r"""Sets the checksum of this GlanceCreateImageMetadataResponse.

        镜像文件md5值。

        :param checksum: The checksum of this GlanceCreateImageMetadataResponse.
        :type checksum: str
        """
        self._checksum = checksum

    @property
    def size(self):
        r"""Gets the size of this GlanceCreateImageMetadataResponse.

        目前暂时不使用。

        :return: The size of this GlanceCreateImageMetadataResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this GlanceCreateImageMetadataResponse.

        目前暂时不使用。

        :param size: The size of this GlanceCreateImageMetadataResponse.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, GlanceCreateImageMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
