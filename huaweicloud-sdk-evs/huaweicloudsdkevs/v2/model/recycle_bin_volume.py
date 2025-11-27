# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecycleBinVolume:

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
        'status': 'str',
        'attachments': 'list[Attachment]',
        'multiattach': 'bool',
        'size': 'int',
        'metadata': 'dict(str, object)',
        'bootable': 'str',
        'tags': 'dict(str, str)',
        'availability_zone': 'str',
        'created_at': 'str',
        'service_type': 'str',
        'updated_at': 'str',
        'volume_type': 'str',
        'enterprise_project_id': 'str',
        'plan_delete_at': 'str',
        'pre_deleted_at': 'str',
        'dedicated_storage_id': 'str',
        'dedicated_storage_name': 'str',
        'volume_image_metadata': 'dict(str, object)',
        'wwn': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'attachments': 'attachments',
        'multiattach': 'multiattach',
        'size': 'size',
        'metadata': 'metadata',
        'bootable': 'bootable',
        'tags': 'tags',
        'availability_zone': 'availability_zone',
        'created_at': 'created_at',
        'service_type': 'service_type',
        'updated_at': 'updated_at',
        'volume_type': 'volume_type',
        'enterprise_project_id': 'enterprise_project_id',
        'plan_delete_at': 'plan_delete_at',
        'pre_deleted_at': 'pre_deleted_at',
        'dedicated_storage_id': 'dedicated_storage_id',
        'dedicated_storage_name': 'dedicated_storage_name',
        'volume_image_metadata': 'volume_image_metadata',
        'wwn': 'wwn'
    }

    def __init__(self, id=None, name=None, description=None, status=None, attachments=None, multiattach=None, size=None, metadata=None, bootable=None, tags=None, availability_zone=None, created_at=None, service_type=None, updated_at=None, volume_type=None, enterprise_project_id=None, plan_delete_at=None, pre_deleted_at=None, dedicated_storage_id=None, dedicated_storage_name=None, volume_image_metadata=None, wwn=None):
        r"""RecycleBinVolume

        The model defined in huaweicloud sdk

        :param id: **参数解释** 云硬盘ID。 **取值范围** 不涉及。
        :type id: str
        :param name: **参数解释** 云硬盘名称。 **取值范围** 不涉及。
        :type name: str
        :param description: **参数解释** 云硬盘描述。 **取值范围** 不涉及。
        :type description: str
        :param status: **参数解释** 云硬盘状态，具体请参见[云硬盘状态](evs_04_0040.xml)。 **取值范围** 不涉及。
        :type status: str
        :param attachments: **参数解释** 云硬盘的挂载信息。 **取值范围** 不涉及。
        :type attachments: list[:class:`huaweicloudsdkevs.v2.Attachment`]
        :param multiattach: **参数解释** 云硬盘是否共享。 **取值范围** - true：表示为共享云硬盘。 - false：表示为普通云硬盘。
        :type multiattach: bool
        :param size: **参数解释** 云硬盘大小，单位为GiB。 **取值范围** 不涉及。
        :type size: int
        :param metadata: **参数解释** 云硬盘的metadata信息 ，调用方可以添加或删除metadata信息。 **取值范围** 当前部分key在EVS服务中有业务场景含义，这部分key的描述如下： - __system__cmkid    metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。    请求获取密钥ID的方法请参考：\&quot;[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)\&quot;。      - __system__encrypted    metadata中的表示加密功能的字段，0代表不加密，1代表加密。    不指定该字段时，云硬盘的加密属性与数据源保持一致，如果不是从数据源创建的场景，则默认不加密。   - hw:passthrough    - true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。    - false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。    - 该字段不存在时，云硬盘默认为VBD类型。
        :type metadata: dict(str, object)
        :param bootable: **参数解释** 云硬盘是否为启动盘。 **取值范围** - true：表示为启动云硬盘。 - false：表示为非启动云硬盘。
        :type bootable: str
        :param tags: **参数解释** 云硬盘标签。 **取值范围** 不涉及。
        :type tags: dict(str, str)
        :param availability_zone: **参数解释** 云硬盘所属可用区。 **取值范围** 不涉及。
        :type availability_zone: str
        :param created_at: **参数解释** 云硬盘创建时间。 **取值范围** 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX
        :type created_at: str
        :param service_type: **参数解释** 云硬盘所属的服务类型。 **取值范围** - EVS：云硬盘。 - DSS：专属分布式存储服务。
        :type service_type: str
        :param updated_at: **参数解释** 云硬盘信息被更新的时间。 **取值范围** 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX
        :type updated_at: str
        :param volume_type: **参数解释** 云硬盘类型。 **取值范围** 目前支持\&quot;SATA\&quot;，\&quot;SAS\&quot;，\&quot;GPSSD\&quot;，\&quot;SSD\&quot;，\&quot;ESSD\&quot;，\&quot;GPSSD2\&quot;，\&quot;ESSD2\&quot;七种。   - \&quot;SATA\&quot;为普通IO云硬盘(已售罄) - \&quot;SAS\&quot;为高IO云硬盘 - \&quot;GPSSD\&quot;为通用型SSD云硬盘 - \&quot;SSD\&quot;为超高IO云硬盘 - \&quot;ESSD\&quot;为极速型SSD云硬盘 - \&quot;GPSSD2\&quot;为通用型SSD V2云硬盘 - \&quot;ESSD2\&quot;为极速型SSD V2云硬盘
        :type volume_type: str
        :param enterprise_project_id: **参数解释** 企业项目ID。 **取值范围** 不涉及。
        :type enterprise_project_id: str
        :param plan_delete_at: **参数解释** 预计到期清理的时间。 **取值范围** 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX
        :type plan_delete_at: str
        :param pre_deleted_at: **参数解释** 放入回收站的时间。 **取值范围** 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX
        :type pre_deleted_at: str
        :param dedicated_storage_id: **参数解释** 云硬盘所属的专属存储池ID。 **取值范围** 不涉及。
        :type dedicated_storage_id: str
        :param dedicated_storage_name: **参数解释** 云硬盘所属的专属存储池的名称。 **取值范围** 不涉及。
        :type dedicated_storage_name: str
        :param volume_image_metadata: **参数解释** 云硬盘镜像的元数据。 关于“volume_image_metadata”字段的详细说明，具体请参见：\&quot;[查询镜像详情](https://support.huaweicloud.com/api-ims/ims_03_0703.html)\&quot;。  **取值范围** 不涉及。
        :type volume_image_metadata: dict(str, object)
        :param wwn: **参数解释** 云硬盘的唯一标识。 **取值范围** 不涉及。
        :type wwn: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._attachments = None
        self._multiattach = None
        self._size = None
        self._metadata = None
        self._bootable = None
        self._tags = None
        self._availability_zone = None
        self._created_at = None
        self._service_type = None
        self._updated_at = None
        self._volume_type = None
        self._enterprise_project_id = None
        self._plan_delete_at = None
        self._pre_deleted_at = None
        self._dedicated_storage_id = None
        self._dedicated_storage_name = None
        self._volume_image_metadata = None
        self._wwn = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if attachments is not None:
            self.attachments = attachments
        if multiattach is not None:
            self.multiattach = multiattach
        if size is not None:
            self.size = size
        if metadata is not None:
            self.metadata = metadata
        if bootable is not None:
            self.bootable = bootable
        if tags is not None:
            self.tags = tags
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if created_at is not None:
            self.created_at = created_at
        if service_type is not None:
            self.service_type = service_type
        if updated_at is not None:
            self.updated_at = updated_at
        if volume_type is not None:
            self.volume_type = volume_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if plan_delete_at is not None:
            self.plan_delete_at = plan_delete_at
        if pre_deleted_at is not None:
            self.pre_deleted_at = pre_deleted_at
        if dedicated_storage_id is not None:
            self.dedicated_storage_id = dedicated_storage_id
        if dedicated_storage_name is not None:
            self.dedicated_storage_name = dedicated_storage_name
        if volume_image_metadata is not None:
            self.volume_image_metadata = volume_image_metadata
        if wwn is not None:
            self.wwn = wwn

    @property
    def id(self):
        r"""Gets the id of this RecycleBinVolume.

        **参数解释** 云硬盘ID。 **取值范围** 不涉及。

        :return: The id of this RecycleBinVolume.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RecycleBinVolume.

        **参数解释** 云硬盘ID。 **取值范围** 不涉及。

        :param id: The id of this RecycleBinVolume.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RecycleBinVolume.

        **参数解释** 云硬盘名称。 **取值范围** 不涉及。

        :return: The name of this RecycleBinVolume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RecycleBinVolume.

        **参数解释** 云硬盘名称。 **取值范围** 不涉及。

        :param name: The name of this RecycleBinVolume.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this RecycleBinVolume.

        **参数解释** 云硬盘描述。 **取值范围** 不涉及。

        :return: The description of this RecycleBinVolume.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RecycleBinVolume.

        **参数解释** 云硬盘描述。 **取值范围** 不涉及。

        :param description: The description of this RecycleBinVolume.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this RecycleBinVolume.

        **参数解释** 云硬盘状态，具体请参见[云硬盘状态](evs_04_0040.xml)。 **取值范围** 不涉及。

        :return: The status of this RecycleBinVolume.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RecycleBinVolume.

        **参数解释** 云硬盘状态，具体请参见[云硬盘状态](evs_04_0040.xml)。 **取值范围** 不涉及。

        :param status: The status of this RecycleBinVolume.
        :type status: str
        """
        self._status = status

    @property
    def attachments(self):
        r"""Gets the attachments of this RecycleBinVolume.

        **参数解释** 云硬盘的挂载信息。 **取值范围** 不涉及。

        :return: The attachments of this RecycleBinVolume.
        :rtype: list[:class:`huaweicloudsdkevs.v2.Attachment`]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        r"""Sets the attachments of this RecycleBinVolume.

        **参数解释** 云硬盘的挂载信息。 **取值范围** 不涉及。

        :param attachments: The attachments of this RecycleBinVolume.
        :type attachments: list[:class:`huaweicloudsdkevs.v2.Attachment`]
        """
        self._attachments = attachments

    @property
    def multiattach(self):
        r"""Gets the multiattach of this RecycleBinVolume.

        **参数解释** 云硬盘是否共享。 **取值范围** - true：表示为共享云硬盘。 - false：表示为普通云硬盘。

        :return: The multiattach of this RecycleBinVolume.
        :rtype: bool
        """
        return self._multiattach

    @multiattach.setter
    def multiattach(self, multiattach):
        r"""Sets the multiattach of this RecycleBinVolume.

        **参数解释** 云硬盘是否共享。 **取值范围** - true：表示为共享云硬盘。 - false：表示为普通云硬盘。

        :param multiattach: The multiattach of this RecycleBinVolume.
        :type multiattach: bool
        """
        self._multiattach = multiattach

    @property
    def size(self):
        r"""Gets the size of this RecycleBinVolume.

        **参数解释** 云硬盘大小，单位为GiB。 **取值范围** 不涉及。

        :return: The size of this RecycleBinVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this RecycleBinVolume.

        **参数解释** 云硬盘大小，单位为GiB。 **取值范围** 不涉及。

        :param size: The size of this RecycleBinVolume.
        :type size: int
        """
        self._size = size

    @property
    def metadata(self):
        r"""Gets the metadata of this RecycleBinVolume.

        **参数解释** 云硬盘的metadata信息 ，调用方可以添加或删除metadata信息。 **取值范围** 当前部分key在EVS服务中有业务场景含义，这部分key的描述如下： - __system__cmkid    metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。    请求获取密钥ID的方法请参考：\"[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)\"。      - __system__encrypted    metadata中的表示加密功能的字段，0代表不加密，1代表加密。    不指定该字段时，云硬盘的加密属性与数据源保持一致，如果不是从数据源创建的场景，则默认不加密。   - hw:passthrough    - true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。    - false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。    - 该字段不存在时，云硬盘默认为VBD类型。

        :return: The metadata of this RecycleBinVolume.
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this RecycleBinVolume.

        **参数解释** 云硬盘的metadata信息 ，调用方可以添加或删除metadata信息。 **取值范围** 当前部分key在EVS服务中有业务场景含义，这部分key的描述如下： - __system__cmkid    metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。    请求获取密钥ID的方法请参考：\"[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)\"。      - __system__encrypted    metadata中的表示加密功能的字段，0代表不加密，1代表加密。    不指定该字段时，云硬盘的加密属性与数据源保持一致，如果不是从数据源创建的场景，则默认不加密。   - hw:passthrough    - true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。    - false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。    - 该字段不存在时，云硬盘默认为VBD类型。

        :param metadata: The metadata of this RecycleBinVolume.
        :type metadata: dict(str, object)
        """
        self._metadata = metadata

    @property
    def bootable(self):
        r"""Gets the bootable of this RecycleBinVolume.

        **参数解释** 云硬盘是否为启动盘。 **取值范围** - true：表示为启动云硬盘。 - false：表示为非启动云硬盘。

        :return: The bootable of this RecycleBinVolume.
        :rtype: str
        """
        return self._bootable

    @bootable.setter
    def bootable(self, bootable):
        r"""Sets the bootable of this RecycleBinVolume.

        **参数解释** 云硬盘是否为启动盘。 **取值范围** - true：表示为启动云硬盘。 - false：表示为非启动云硬盘。

        :param bootable: The bootable of this RecycleBinVolume.
        :type bootable: str
        """
        self._bootable = bootable

    @property
    def tags(self):
        r"""Gets the tags of this RecycleBinVolume.

        **参数解释** 云硬盘标签。 **取值范围** 不涉及。

        :return: The tags of this RecycleBinVolume.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this RecycleBinVolume.

        **参数解释** 云硬盘标签。 **取值范围** 不涉及。

        :param tags: The tags of this RecycleBinVolume.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this RecycleBinVolume.

        **参数解释** 云硬盘所属可用区。 **取值范围** 不涉及。

        :return: The availability_zone of this RecycleBinVolume.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this RecycleBinVolume.

        **参数解释** 云硬盘所属可用区。 **取值范围** 不涉及。

        :param availability_zone: The availability_zone of this RecycleBinVolume.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def created_at(self):
        r"""Gets the created_at of this RecycleBinVolume.

        **参数解释** 云硬盘创建时间。 **取值范围** 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The created_at of this RecycleBinVolume.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RecycleBinVolume.

        **参数解释** 云硬盘创建时间。 **取值范围** 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param created_at: The created_at of this RecycleBinVolume.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def service_type(self):
        r"""Gets the service_type of this RecycleBinVolume.

        **参数解释** 云硬盘所属的服务类型。 **取值范围** - EVS：云硬盘。 - DSS：专属分布式存储服务。

        :return: The service_type of this RecycleBinVolume.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this RecycleBinVolume.

        **参数解释** 云硬盘所属的服务类型。 **取值范围** - EVS：云硬盘。 - DSS：专属分布式存储服务。

        :param service_type: The service_type of this RecycleBinVolume.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def updated_at(self):
        r"""Gets the updated_at of this RecycleBinVolume.

        **参数解释** 云硬盘信息被更新的时间。 **取值范围** 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The updated_at of this RecycleBinVolume.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this RecycleBinVolume.

        **参数解释** 云硬盘信息被更新的时间。 **取值范围** 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param updated_at: The updated_at of this RecycleBinVolume.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def volume_type(self):
        r"""Gets the volume_type of this RecycleBinVolume.

        **参数解释** 云硬盘类型。 **取值范围** 目前支持\"SATA\"，\"SAS\"，\"GPSSD\"，\"SSD\"，\"ESSD\"，\"GPSSD2\"，\"ESSD2\"七种。   - \"SATA\"为普通IO云硬盘(已售罄) - \"SAS\"为高IO云硬盘 - \"GPSSD\"为通用型SSD云硬盘 - \"SSD\"为超高IO云硬盘 - \"ESSD\"为极速型SSD云硬盘 - \"GPSSD2\"为通用型SSD V2云硬盘 - \"ESSD2\"为极速型SSD V2云硬盘

        :return: The volume_type of this RecycleBinVolume.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this RecycleBinVolume.

        **参数解释** 云硬盘类型。 **取值范围** 目前支持\"SATA\"，\"SAS\"，\"GPSSD\"，\"SSD\"，\"ESSD\"，\"GPSSD2\"，\"ESSD2\"七种。   - \"SATA\"为普通IO云硬盘(已售罄) - \"SAS\"为高IO云硬盘 - \"GPSSD\"为通用型SSD云硬盘 - \"SSD\"为超高IO云硬盘 - \"ESSD\"为极速型SSD云硬盘 - \"GPSSD2\"为通用型SSD V2云硬盘 - \"ESSD2\"为极速型SSD V2云硬盘

        :param volume_type: The volume_type of this RecycleBinVolume.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this RecycleBinVolume.

        **参数解释** 企业项目ID。 **取值范围** 不涉及。

        :return: The enterprise_project_id of this RecycleBinVolume.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this RecycleBinVolume.

        **参数解释** 企业项目ID。 **取值范围** 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this RecycleBinVolume.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def plan_delete_at(self):
        r"""Gets the plan_delete_at of this RecycleBinVolume.

        **参数解释** 预计到期清理的时间。 **取值范围** 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The plan_delete_at of this RecycleBinVolume.
        :rtype: str
        """
        return self._plan_delete_at

    @plan_delete_at.setter
    def plan_delete_at(self, plan_delete_at):
        r"""Sets the plan_delete_at of this RecycleBinVolume.

        **参数解释** 预计到期清理的时间。 **取值范围** 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param plan_delete_at: The plan_delete_at of this RecycleBinVolume.
        :type plan_delete_at: str
        """
        self._plan_delete_at = plan_delete_at

    @property
    def pre_deleted_at(self):
        r"""Gets the pre_deleted_at of this RecycleBinVolume.

        **参数解释** 放入回收站的时间。 **取值范围** 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The pre_deleted_at of this RecycleBinVolume.
        :rtype: str
        """
        return self._pre_deleted_at

    @pre_deleted_at.setter
    def pre_deleted_at(self, pre_deleted_at):
        r"""Sets the pre_deleted_at of this RecycleBinVolume.

        **参数解释** 放入回收站的时间。 **取值范围** 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param pre_deleted_at: The pre_deleted_at of this RecycleBinVolume.
        :type pre_deleted_at: str
        """
        self._pre_deleted_at = pre_deleted_at

    @property
    def dedicated_storage_id(self):
        r"""Gets the dedicated_storage_id of this RecycleBinVolume.

        **参数解释** 云硬盘所属的专属存储池ID。 **取值范围** 不涉及。

        :return: The dedicated_storage_id of this RecycleBinVolume.
        :rtype: str
        """
        return self._dedicated_storage_id

    @dedicated_storage_id.setter
    def dedicated_storage_id(self, dedicated_storage_id):
        r"""Sets the dedicated_storage_id of this RecycleBinVolume.

        **参数解释** 云硬盘所属的专属存储池ID。 **取值范围** 不涉及。

        :param dedicated_storage_id: The dedicated_storage_id of this RecycleBinVolume.
        :type dedicated_storage_id: str
        """
        self._dedicated_storage_id = dedicated_storage_id

    @property
    def dedicated_storage_name(self):
        r"""Gets the dedicated_storage_name of this RecycleBinVolume.

        **参数解释** 云硬盘所属的专属存储池的名称。 **取值范围** 不涉及。

        :return: The dedicated_storage_name of this RecycleBinVolume.
        :rtype: str
        """
        return self._dedicated_storage_name

    @dedicated_storage_name.setter
    def dedicated_storage_name(self, dedicated_storage_name):
        r"""Sets the dedicated_storage_name of this RecycleBinVolume.

        **参数解释** 云硬盘所属的专属存储池的名称。 **取值范围** 不涉及。

        :param dedicated_storage_name: The dedicated_storage_name of this RecycleBinVolume.
        :type dedicated_storage_name: str
        """
        self._dedicated_storage_name = dedicated_storage_name

    @property
    def volume_image_metadata(self):
        r"""Gets the volume_image_metadata of this RecycleBinVolume.

        **参数解释** 云硬盘镜像的元数据。 关于“volume_image_metadata”字段的详细说明，具体请参见：\"[查询镜像详情](https://support.huaweicloud.com/api-ims/ims_03_0703.html)\"。  **取值范围** 不涉及。

        :return: The volume_image_metadata of this RecycleBinVolume.
        :rtype: dict(str, object)
        """
        return self._volume_image_metadata

    @volume_image_metadata.setter
    def volume_image_metadata(self, volume_image_metadata):
        r"""Sets the volume_image_metadata of this RecycleBinVolume.

        **参数解释** 云硬盘镜像的元数据。 关于“volume_image_metadata”字段的详细说明，具体请参见：\"[查询镜像详情](https://support.huaweicloud.com/api-ims/ims_03_0703.html)\"。  **取值范围** 不涉及。

        :param volume_image_metadata: The volume_image_metadata of this RecycleBinVolume.
        :type volume_image_metadata: dict(str, object)
        """
        self._volume_image_metadata = volume_image_metadata

    @property
    def wwn(self):
        r"""Gets the wwn of this RecycleBinVolume.

        **参数解释** 云硬盘的唯一标识。 **取值范围** 不涉及。

        :return: The wwn of this RecycleBinVolume.
        :rtype: str
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        r"""Sets the wwn of this RecycleBinVolume.

        **参数解释** 云硬盘的唯一标识。 **取值范围** 不涉及。

        :param wwn: The wwn of this RecycleBinVolume.
        :type wwn: str
        """
        self._wwn = wwn

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
        if not isinstance(other, RecycleBinVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
