# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageResponse(SdkResponse):

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
        'status': 'str',
        'disk_format': 'str',
        'min_disk': 'int',
        'min_ram': 'int',
        'owner': 'str',
        'protected': 'bool',
        'visibility': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        '_self': 'str',
        'deleted': 'bool',
        'virtual_env_type': 'str',
        'deleted_at': 'str',
        'relation_job_id': 'str',
        'imagetype': 'str',
        'platform': 'str',
        'os_type': 'str',
        'os_version': 'str',
        'isregistered': 'bool',
        'support_kvm': 'str',
        'support_kvm_gpu_type': 'str',
        'support_kvm_ascend_310': 'str',
        'support_kvm_hi1822_hiovs': 'str',
        'support_arm': 'str',
        'hw_firmware_type': 'str',
        'data_source': 'str',
        'support_gpu_t4': 'str',
        'origin_region_info': 'CloudImageRegionInfo',
        'edge_region_info': 'list[EdgeImageRegionInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'disk_format': 'disk_format',
        'min_disk': 'min_disk',
        'min_ram': 'min_ram',
        'owner': 'owner',
        'protected': 'protected',
        'visibility': 'visibility',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        '_self': 'self',
        'deleted': 'deleted',
        'virtual_env_type': 'virtual_env_type',
        'deleted_at': 'deleted_at',
        'relation_job_id': 'relation_job_id',
        'imagetype': '__imagetype',
        'platform': '__platform',
        'os_type': '__os_type',
        'os_version': '__os_version',
        'isregistered': '__isregistered',
        'support_kvm': '__support_kvm',
        'support_kvm_gpu_type': '__support_kvm_gpu_type',
        'support_kvm_ascend_310': '__support_kvm_ascend_310',
        'support_kvm_hi1822_hiovs': '__support_kvm_hi1822_hiovs',
        'support_arm': '__support_arm',
        'hw_firmware_type': 'hw_firmware_type',
        'data_source': 'data_source',
        'support_gpu_t4': '__support_gpu_t4',
        'origin_region_info': 'origin_region_info',
        'edge_region_info': 'edge_region_info'
    }

    def __init__(self, id=None, name=None, status=None, disk_format=None, min_disk=None, min_ram=None, owner=None, protected=None, visibility=None, created_at=None, updated_at=None, _self=None, deleted=None, virtual_env_type=None, deleted_at=None, relation_job_id=None, imagetype=None, platform=None, os_type=None, os_version=None, isregistered=None, support_kvm=None, support_kvm_gpu_type=None, support_kvm_ascend_310=None, support_kvm_hi1822_hiovs=None, support_arm=None, hw_firmware_type=None, data_source=None, support_gpu_t4=None, origin_region_info=None, edge_region_info=None):
        r"""ShowImageResponse

        The model defined in huaweicloud sdk

        :param id: 镜像ID。
        :type id: str
        :param name: 镜像名称。
        :type name: str
        :param status: 镜像状态。
        :type status: str
        :param disk_format: 镜像格式。
        :type disk_format: str
        :param min_disk: 最小系统盘（单位：GB），取值为40～1024GB。
        :type min_disk: int
        :param min_ram: 最小内存（单位：MB），默认值为0。
        :type min_ram: int
        :param owner: 镜像所属租户ID。
        :type owner: str
        :param protected: 是否受保护。
        :type protected: bool
        :param visibility: 可见性。
        :type visibility: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        :param _self: 镜像链接信息。
        :type _self: str
        :param deleted: 是否是删除的镜像，取值为true或者false。
        :type deleted: bool
        :param virtual_env_type: 镜像使用环境类型。
        :type virtual_env_type: str
        :param deleted_at: 删除时间，格式为UTC时间。
        :type deleted_at: str
        :param relation_job_id: 镜像关联的任务ID。
        :type relation_job_id: str
        :param imagetype: 镜像类型。  取值范围： - gold：公有镜像； - private：私有镜像。
        :type imagetype: str
        :param platform: 镜像平台分类。
        :type platform: str
        :param os_type: 镜像系统类型。
        :type os_type: str
        :param os_version: 镜像的操作系统具体版本。
        :type os_version: str
        :param isregistered: 是否是注册过的镜像。
        :type isregistered: bool
        :param support_kvm: 如果镜像支持KVM，取值为true，否则无该属性。
        :type support_kvm: str
        :param support_kvm_gpu_type: 如果镜像是支持KVM虚拟化平台下的GPU类型，取值为“V100_vGPU”或者“RTX5000”，否则无该属性。
        :type support_kvm_gpu_type: str
        :param support_kvm_ascend_310: 如果镜像支持AI加速，取值为true，否则无该属性。
        :type support_kvm_ascend_310: str
        :param support_kvm_hi1822_hiovs: 如果镜像支持计算增强，取值为true，否则无该属性。
        :type support_kvm_hi1822_hiovs: str
        :param support_arm: 如果镜像为ARM架构类型，取值为true，否则无该属性。
        :type support_arm: str
        :param hw_firmware_type: 镜像启动模式，取值为uefi或bios，不指定时无该属性。
        :type hw_firmware_type: str
        :param data_source: 镜像来源。  - 来源边缘实例：instance:&lt;实例id&gt; - 来源IMS：ims:&lt;镜像id&gt;:&lt;region id&gt;
        :type data_source: str
        :param support_gpu_t4: 如果镜像支持GPU T4类型，取值为true，否则无该属性。
        :type support_gpu_t4: str
        :param origin_region_info: 
        :type origin_region_info: :class:`huaweicloudsdkiec.v1.CloudImageRegionInfo`
        :param edge_region_info: 边缘区域详情。
        :type edge_region_info: list[:class:`huaweicloudsdkiec.v1.EdgeImageRegionInfo`]
        """
        
        super(ShowImageResponse, self).__init__()

        self._id = None
        self._name = None
        self._status = None
        self._disk_format = None
        self._min_disk = None
        self._min_ram = None
        self._owner = None
        self._protected = None
        self._visibility = None
        self._created_at = None
        self._updated_at = None
        self.__self = None
        self._deleted = None
        self._virtual_env_type = None
        self._deleted_at = None
        self._relation_job_id = None
        self._imagetype = None
        self._platform = None
        self._os_type = None
        self._os_version = None
        self._isregistered = None
        self._support_kvm = None
        self._support_kvm_gpu_type = None
        self._support_kvm_ascend_310 = None
        self._support_kvm_hi1822_hiovs = None
        self._support_arm = None
        self._hw_firmware_type = None
        self._data_source = None
        self._support_gpu_t4 = None
        self._origin_region_info = None
        self._edge_region_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if disk_format is not None:
            self.disk_format = disk_format
        if min_disk is not None:
            self.min_disk = min_disk
        if min_ram is not None:
            self.min_ram = min_ram
        if owner is not None:
            self.owner = owner
        if protected is not None:
            self.protected = protected
        if visibility is not None:
            self.visibility = visibility
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if _self is not None:
            self._self = _self
        if deleted is not None:
            self.deleted = deleted
        if virtual_env_type is not None:
            self.virtual_env_type = virtual_env_type
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if relation_job_id is not None:
            self.relation_job_id = relation_job_id
        if imagetype is not None:
            self.imagetype = imagetype
        if platform is not None:
            self.platform = platform
        if os_type is not None:
            self.os_type = os_type
        if os_version is not None:
            self.os_version = os_version
        if isregistered is not None:
            self.isregistered = isregistered
        if support_kvm is not None:
            self.support_kvm = support_kvm
        if support_kvm_gpu_type is not None:
            self.support_kvm_gpu_type = support_kvm_gpu_type
        if support_kvm_ascend_310 is not None:
            self.support_kvm_ascend_310 = support_kvm_ascend_310
        if support_kvm_hi1822_hiovs is not None:
            self.support_kvm_hi1822_hiovs = support_kvm_hi1822_hiovs
        if support_arm is not None:
            self.support_arm = support_arm
        if hw_firmware_type is not None:
            self.hw_firmware_type = hw_firmware_type
        if data_source is not None:
            self.data_source = data_source
        if support_gpu_t4 is not None:
            self.support_gpu_t4 = support_gpu_t4
        if origin_region_info is not None:
            self.origin_region_info = origin_region_info
        if edge_region_info is not None:
            self.edge_region_info = edge_region_info

    @property
    def id(self):
        r"""Gets the id of this ShowImageResponse.

        镜像ID。

        :return: The id of this ShowImageResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowImageResponse.

        镜像ID。

        :param id: The id of this ShowImageResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowImageResponse.

        镜像名称。

        :return: The name of this ShowImageResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowImageResponse.

        镜像名称。

        :param name: The name of this ShowImageResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ShowImageResponse.

        镜像状态。

        :return: The status of this ShowImageResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowImageResponse.

        镜像状态。

        :param status: The status of this ShowImageResponse.
        :type status: str
        """
        self._status = status

    @property
    def disk_format(self):
        r"""Gets the disk_format of this ShowImageResponse.

        镜像格式。

        :return: The disk_format of this ShowImageResponse.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        r"""Sets the disk_format of this ShowImageResponse.

        镜像格式。

        :param disk_format: The disk_format of this ShowImageResponse.
        :type disk_format: str
        """
        self._disk_format = disk_format

    @property
    def min_disk(self):
        r"""Gets the min_disk of this ShowImageResponse.

        最小系统盘（单位：GB），取值为40～1024GB。

        :return: The min_disk of this ShowImageResponse.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        r"""Sets the min_disk of this ShowImageResponse.

        最小系统盘（单位：GB），取值为40～1024GB。

        :param min_disk: The min_disk of this ShowImageResponse.
        :type min_disk: int
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        r"""Gets the min_ram of this ShowImageResponse.

        最小内存（单位：MB），默认值为0。

        :return: The min_ram of this ShowImageResponse.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        r"""Sets the min_ram of this ShowImageResponse.

        最小内存（单位：MB），默认值为0。

        :param min_ram: The min_ram of this ShowImageResponse.
        :type min_ram: int
        """
        self._min_ram = min_ram

    @property
    def owner(self):
        r"""Gets the owner of this ShowImageResponse.

        镜像所属租户ID。

        :return: The owner of this ShowImageResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ShowImageResponse.

        镜像所属租户ID。

        :param owner: The owner of this ShowImageResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def protected(self):
        r"""Gets the protected of this ShowImageResponse.

        是否受保护。

        :return: The protected of this ShowImageResponse.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        r"""Sets the protected of this ShowImageResponse.

        是否受保护。

        :param protected: The protected of this ShowImageResponse.
        :type protected: bool
        """
        self._protected = protected

    @property
    def visibility(self):
        r"""Gets the visibility of this ShowImageResponse.

        可见性。

        :return: The visibility of this ShowImageResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ShowImageResponse.

        可见性。

        :param visibility: The visibility of this ShowImageResponse.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowImageResponse.

        创建时间。

        :return: The created_at of this ShowImageResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowImageResponse.

        创建时间。

        :param created_at: The created_at of this ShowImageResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowImageResponse.

        更新时间。

        :return: The updated_at of this ShowImageResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowImageResponse.

        更新时间。

        :param updated_at: The updated_at of this ShowImageResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def _self(self):
        r"""Gets the _self of this ShowImageResponse.

        镜像链接信息。

        :return: The _self of this ShowImageResponse.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        r"""Sets the _self of this ShowImageResponse.

        镜像链接信息。

        :param _self: The _self of this ShowImageResponse.
        :type _self: str
        """
        self.__self = _self

    @property
    def deleted(self):
        r"""Gets the deleted of this ShowImageResponse.

        是否是删除的镜像，取值为true或者false。

        :return: The deleted of this ShowImageResponse.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this ShowImageResponse.

        是否是删除的镜像，取值为true或者false。

        :param deleted: The deleted of this ShowImageResponse.
        :type deleted: bool
        """
        self._deleted = deleted

    @property
    def virtual_env_type(self):
        r"""Gets the virtual_env_type of this ShowImageResponse.

        镜像使用环境类型。

        :return: The virtual_env_type of this ShowImageResponse.
        :rtype: str
        """
        return self._virtual_env_type

    @virtual_env_type.setter
    def virtual_env_type(self, virtual_env_type):
        r"""Sets the virtual_env_type of this ShowImageResponse.

        镜像使用环境类型。

        :param virtual_env_type: The virtual_env_type of this ShowImageResponse.
        :type virtual_env_type: str
        """
        self._virtual_env_type = virtual_env_type

    @property
    def deleted_at(self):
        r"""Gets the deleted_at of this ShowImageResponse.

        删除时间，格式为UTC时间。

        :return: The deleted_at of this ShowImageResponse.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        r"""Sets the deleted_at of this ShowImageResponse.

        删除时间，格式为UTC时间。

        :param deleted_at: The deleted_at of this ShowImageResponse.
        :type deleted_at: str
        """
        self._deleted_at = deleted_at

    @property
    def relation_job_id(self):
        r"""Gets the relation_job_id of this ShowImageResponse.

        镜像关联的任务ID。

        :return: The relation_job_id of this ShowImageResponse.
        :rtype: str
        """
        return self._relation_job_id

    @relation_job_id.setter
    def relation_job_id(self, relation_job_id):
        r"""Sets the relation_job_id of this ShowImageResponse.

        镜像关联的任务ID。

        :param relation_job_id: The relation_job_id of this ShowImageResponse.
        :type relation_job_id: str
        """
        self._relation_job_id = relation_job_id

    @property
    def imagetype(self):
        r"""Gets the imagetype of this ShowImageResponse.

        镜像类型。  取值范围： - gold：公有镜像； - private：私有镜像。

        :return: The imagetype of this ShowImageResponse.
        :rtype: str
        """
        return self._imagetype

    @imagetype.setter
    def imagetype(self, imagetype):
        r"""Sets the imagetype of this ShowImageResponse.

        镜像类型。  取值范围： - gold：公有镜像； - private：私有镜像。

        :param imagetype: The imagetype of this ShowImageResponse.
        :type imagetype: str
        """
        self._imagetype = imagetype

    @property
    def platform(self):
        r"""Gets the platform of this ShowImageResponse.

        镜像平台分类。

        :return: The platform of this ShowImageResponse.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this ShowImageResponse.

        镜像平台分类。

        :param platform: The platform of this ShowImageResponse.
        :type platform: str
        """
        self._platform = platform

    @property
    def os_type(self):
        r"""Gets the os_type of this ShowImageResponse.

        镜像系统类型。

        :return: The os_type of this ShowImageResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ShowImageResponse.

        镜像系统类型。

        :param os_type: The os_type of this ShowImageResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        r"""Gets the os_version of this ShowImageResponse.

        镜像的操作系统具体版本。

        :return: The os_version of this ShowImageResponse.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this ShowImageResponse.

        镜像的操作系统具体版本。

        :param os_version: The os_version of this ShowImageResponse.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def isregistered(self):
        r"""Gets the isregistered of this ShowImageResponse.

        是否是注册过的镜像。

        :return: The isregistered of this ShowImageResponse.
        :rtype: bool
        """
        return self._isregistered

    @isregistered.setter
    def isregistered(self, isregistered):
        r"""Sets the isregistered of this ShowImageResponse.

        是否是注册过的镜像。

        :param isregistered: The isregistered of this ShowImageResponse.
        :type isregistered: bool
        """
        self._isregistered = isregistered

    @property
    def support_kvm(self):
        r"""Gets the support_kvm of this ShowImageResponse.

        如果镜像支持KVM，取值为true，否则无该属性。

        :return: The support_kvm of this ShowImageResponse.
        :rtype: str
        """
        return self._support_kvm

    @support_kvm.setter
    def support_kvm(self, support_kvm):
        r"""Sets the support_kvm of this ShowImageResponse.

        如果镜像支持KVM，取值为true，否则无该属性。

        :param support_kvm: The support_kvm of this ShowImageResponse.
        :type support_kvm: str
        """
        self._support_kvm = support_kvm

    @property
    def support_kvm_gpu_type(self):
        r"""Gets the support_kvm_gpu_type of this ShowImageResponse.

        如果镜像是支持KVM虚拟化平台下的GPU类型，取值为“V100_vGPU”或者“RTX5000”，否则无该属性。

        :return: The support_kvm_gpu_type of this ShowImageResponse.
        :rtype: str
        """
        return self._support_kvm_gpu_type

    @support_kvm_gpu_type.setter
    def support_kvm_gpu_type(self, support_kvm_gpu_type):
        r"""Sets the support_kvm_gpu_type of this ShowImageResponse.

        如果镜像是支持KVM虚拟化平台下的GPU类型，取值为“V100_vGPU”或者“RTX5000”，否则无该属性。

        :param support_kvm_gpu_type: The support_kvm_gpu_type of this ShowImageResponse.
        :type support_kvm_gpu_type: str
        """
        self._support_kvm_gpu_type = support_kvm_gpu_type

    @property
    def support_kvm_ascend_310(self):
        r"""Gets the support_kvm_ascend_310 of this ShowImageResponse.

        如果镜像支持AI加速，取值为true，否则无该属性。

        :return: The support_kvm_ascend_310 of this ShowImageResponse.
        :rtype: str
        """
        return self._support_kvm_ascend_310

    @support_kvm_ascend_310.setter
    def support_kvm_ascend_310(self, support_kvm_ascend_310):
        r"""Sets the support_kvm_ascend_310 of this ShowImageResponse.

        如果镜像支持AI加速，取值为true，否则无该属性。

        :param support_kvm_ascend_310: The support_kvm_ascend_310 of this ShowImageResponse.
        :type support_kvm_ascend_310: str
        """
        self._support_kvm_ascend_310 = support_kvm_ascend_310

    @property
    def support_kvm_hi1822_hiovs(self):
        r"""Gets the support_kvm_hi1822_hiovs of this ShowImageResponse.

        如果镜像支持计算增强，取值为true，否则无该属性。

        :return: The support_kvm_hi1822_hiovs of this ShowImageResponse.
        :rtype: str
        """
        return self._support_kvm_hi1822_hiovs

    @support_kvm_hi1822_hiovs.setter
    def support_kvm_hi1822_hiovs(self, support_kvm_hi1822_hiovs):
        r"""Sets the support_kvm_hi1822_hiovs of this ShowImageResponse.

        如果镜像支持计算增强，取值为true，否则无该属性。

        :param support_kvm_hi1822_hiovs: The support_kvm_hi1822_hiovs of this ShowImageResponse.
        :type support_kvm_hi1822_hiovs: str
        """
        self._support_kvm_hi1822_hiovs = support_kvm_hi1822_hiovs

    @property
    def support_arm(self):
        r"""Gets the support_arm of this ShowImageResponse.

        如果镜像为ARM架构类型，取值为true，否则无该属性。

        :return: The support_arm of this ShowImageResponse.
        :rtype: str
        """
        return self._support_arm

    @support_arm.setter
    def support_arm(self, support_arm):
        r"""Sets the support_arm of this ShowImageResponse.

        如果镜像为ARM架构类型，取值为true，否则无该属性。

        :param support_arm: The support_arm of this ShowImageResponse.
        :type support_arm: str
        """
        self._support_arm = support_arm

    @property
    def hw_firmware_type(self):
        r"""Gets the hw_firmware_type of this ShowImageResponse.

        镜像启动模式，取值为uefi或bios，不指定时无该属性。

        :return: The hw_firmware_type of this ShowImageResponse.
        :rtype: str
        """
        return self._hw_firmware_type

    @hw_firmware_type.setter
    def hw_firmware_type(self, hw_firmware_type):
        r"""Sets the hw_firmware_type of this ShowImageResponse.

        镜像启动模式，取值为uefi或bios，不指定时无该属性。

        :param hw_firmware_type: The hw_firmware_type of this ShowImageResponse.
        :type hw_firmware_type: str
        """
        self._hw_firmware_type = hw_firmware_type

    @property
    def data_source(self):
        r"""Gets the data_source of this ShowImageResponse.

        镜像来源。  - 来源边缘实例：instance:<实例id> - 来源IMS：ims:<镜像id>:<region id>

        :return: The data_source of this ShowImageResponse.
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        r"""Sets the data_source of this ShowImageResponse.

        镜像来源。  - 来源边缘实例：instance:<实例id> - 来源IMS：ims:<镜像id>:<region id>

        :param data_source: The data_source of this ShowImageResponse.
        :type data_source: str
        """
        self._data_source = data_source

    @property
    def support_gpu_t4(self):
        r"""Gets the support_gpu_t4 of this ShowImageResponse.

        如果镜像支持GPU T4类型，取值为true，否则无该属性。

        :return: The support_gpu_t4 of this ShowImageResponse.
        :rtype: str
        """
        return self._support_gpu_t4

    @support_gpu_t4.setter
    def support_gpu_t4(self, support_gpu_t4):
        r"""Sets the support_gpu_t4 of this ShowImageResponse.

        如果镜像支持GPU T4类型，取值为true，否则无该属性。

        :param support_gpu_t4: The support_gpu_t4 of this ShowImageResponse.
        :type support_gpu_t4: str
        """
        self._support_gpu_t4 = support_gpu_t4

    @property
    def origin_region_info(self):
        r"""Gets the origin_region_info of this ShowImageResponse.

        :return: The origin_region_info of this ShowImageResponse.
        :rtype: :class:`huaweicloudsdkiec.v1.CloudImageRegionInfo`
        """
        return self._origin_region_info

    @origin_region_info.setter
    def origin_region_info(self, origin_region_info):
        r"""Sets the origin_region_info of this ShowImageResponse.

        :param origin_region_info: The origin_region_info of this ShowImageResponse.
        :type origin_region_info: :class:`huaweicloudsdkiec.v1.CloudImageRegionInfo`
        """
        self._origin_region_info = origin_region_info

    @property
    def edge_region_info(self):
        r"""Gets the edge_region_info of this ShowImageResponse.

        边缘区域详情。

        :return: The edge_region_info of this ShowImageResponse.
        :rtype: list[:class:`huaweicloudsdkiec.v1.EdgeImageRegionInfo`]
        """
        return self._edge_region_info

    @edge_region_info.setter
    def edge_region_info(self, edge_region_info):
        r"""Sets the edge_region_info of this ShowImageResponse.

        边缘区域详情。

        :param edge_region_info: The edge_region_info of this ShowImageResponse.
        :type edge_region_info: list[:class:`huaweicloudsdkiec.v1.EdgeImageRegionInfo`]
        """
        self._edge_region_info = edge_region_info

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
        if not isinstance(other, ShowImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
