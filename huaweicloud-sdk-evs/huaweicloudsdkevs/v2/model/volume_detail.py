# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeDetail:

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
        'links': 'list[Link]',
        'name': 'str',
        'status': 'str',
        'attachments': 'list[Attachment]',
        'availability_zone': 'str',
        'os_vol_host_attrhost': 'str',
        'source_volid': 'str',
        'snapshot_id': 'str',
        'description': 'str',
        'created_at': 'str',
        'os_vol_tenant_attrtenant_id': 'str',
        'volume_image_metadata': 'dict(str, object)',
        'volume_type': 'str',
        'size': 'int',
        'consistencygroup_id': 'str',
        'bootable': 'str',
        'metadata': 'dict(str, object)',
        'updated_at': 'str',
        'encrypted': 'bool',
        'replication_status': 'str',
        'os_volume_replicationextended_status': 'str',
        'os_vol_mig_status_attrmigstat': 'str',
        'os_vol_mig_status_attrname_id': 'str',
        'shareable': 'str',
        'user_id': 'str',
        'service_type': 'str',
        'multiattach': 'bool',
        'dedicated_storage_id': 'str',
        'dedicated_storage_name': 'str',
        'tags': 'dict(str, str)',
        'wwn': 'str',
        'enterprise_project_id': 'str',
        'serial_number': 'str',
        'iops': 'Iops',
        'throughput': 'Throughput'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'name': 'name',
        'status': 'status',
        'attachments': 'attachments',
        'availability_zone': 'availability_zone',
        'os_vol_host_attrhost': 'os-vol-host-attr:host',
        'source_volid': 'source_volid',
        'snapshot_id': 'snapshot_id',
        'description': 'description',
        'created_at': 'created_at',
        'os_vol_tenant_attrtenant_id': 'os-vol-tenant-attr:tenant_id',
        'volume_image_metadata': 'volume_image_metadata',
        'volume_type': 'volume_type',
        'size': 'size',
        'consistencygroup_id': 'consistencygroup_id',
        'bootable': 'bootable',
        'metadata': 'metadata',
        'updated_at': 'updated_at',
        'encrypted': 'encrypted',
        'replication_status': 'replication_status',
        'os_volume_replicationextended_status': 'os-volume-replication:extended_status',
        'os_vol_mig_status_attrmigstat': 'os-vol-mig-status-attr:migstat',
        'os_vol_mig_status_attrname_id': 'os-vol-mig-status-attr:name_id',
        'shareable': 'shareable',
        'user_id': 'user_id',
        'service_type': 'service_type',
        'multiattach': 'multiattach',
        'dedicated_storage_id': 'dedicated_storage_id',
        'dedicated_storage_name': 'dedicated_storage_name',
        'tags': 'tags',
        'wwn': 'wwn',
        'enterprise_project_id': 'enterprise_project_id',
        'serial_number': 'serial_number',
        'iops': 'iops',
        'throughput': 'throughput'
    }

    def __init__(self, id=None, links=None, name=None, status=None, attachments=None, availability_zone=None, os_vol_host_attrhost=None, source_volid=None, snapshot_id=None, description=None, created_at=None, os_vol_tenant_attrtenant_id=None, volume_image_metadata=None, volume_type=None, size=None, consistencygroup_id=None, bootable=None, metadata=None, updated_at=None, encrypted=None, replication_status=None, os_volume_replicationextended_status=None, os_vol_mig_status_attrmigstat=None, os_vol_mig_status_attrname_id=None, shareable=None, user_id=None, service_type=None, multiattach=None, dedicated_storage_id=None, dedicated_storage_name=None, tags=None, wwn=None, enterprise_project_id=None, serial_number=None, iops=None, throughput=None):
        """VolumeDetail

        The model defined in huaweicloud sdk

        :param id: 云硬盘的ID。
        :type id: str
        :param links: 云硬盘URI自描述信息。请参见 [links参数说明](https://support.huaweicloud.com/api-evs/evs_04_2006.html#evs_04_2006__evs_04_2010_li1077125119136)。
        :type links: list[:class:`huaweicloudsdkevs.v2.Link`]
        :param name: 云硬盘名称。
        :type name: str
        :param status: 云硬盘状态，请参见[云硬盘状态](https://support.huaweicloud.com/api-evs/evs_04_0040.html)。
        :type status: str
        :param attachments: 云硬盘的挂载信息，请参见•[attachments参数说明](https://support.huaweicloud.com/api-evs/evs_04_2006.html#evs_04_2006__evs_04_2010_li12430153610291)。
        :type attachments: list[:class:`huaweicloudsdkevs.v2.Attachment`]
        :param availability_zone: 云硬盘所属的AZ信息。
        :type availability_zone: str
        :param os_vol_host_attrhost: 预留属性。
        :type os_vol_host_attrhost: str
        :param source_volid: 源云硬盘ID，如果是从源云硬盘创建，则有值。  当前云硬盘服务不支持该字段。
        :type source_volid: str
        :param snapshot_id: 快照ID，如果是从快照创建，则有值。
        :type snapshot_id: str
        :param description: 云硬盘描述。
        :type description: str
        :param created_at: 云硬盘创建时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX
        :type created_at: str
        :param os_vol_tenant_attrtenant_id: 云硬盘所属的租户ID。租户ID就是项目ID。
        :type os_vol_tenant_attrtenant_id: str
        :param volume_image_metadata: 云硬盘镜像的元数据。 &gt; 说明： &gt;  &gt; 关于“volume_image_metadata”字段的详细说明，具体请参见：\&quot;[查询镜像详情](https://support.huaweicloud.com/api-ims/ims_03_0703.html)\&quot;。
        :type volume_image_metadata: dict(str, object)
        :param volume_type: 云硬盘类型。 目前支持\&quot;SATA\&quot;，\&quot;SAS\&quot;，\&quot;GPSSD\&quot;，\&quot;SSD\&quot;，\&quot;ESSD\&quot;，\&quot;GPSSD2\&quot;,\&quot;ESSD2\&quot;七种。  - \&quot;SATA\&quot;为普通IO云硬盘 - \&quot;SAS\&quot;为高IO云硬盘 - \&quot;GPSSD\&quot;为通用型SSD云硬盘 - \&quot;SSD\&quot;为超高IO云硬盘 - \&quot;ESSD\&quot;为极速IO云硬盘 - \&quot;GPSSD2\&quot;为通用型SSD V2云硬盘 - \&quot;ESSD2\&quot;为极速型SSD V2云硬盘
        :type volume_type: str
        :param size: 云硬盘大小，单位为GB。
        :type size: int
        :param consistencygroup_id: 预留属性。
        :type consistencygroup_id: str
        :param bootable: 是否为启动云硬盘。 true：表示为启动云硬盘。 false：表示为非启动云硬盘。
        :type bootable: str
        :param metadata: 云硬盘的元数据。  __system__cmkid metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。 &gt;  &gt; 请求获取密钥ID的方法请参考：\&quot;[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)\&quot;。  __system__encrypted metadata中的表示加密功能的字段，0代表不加密，1代表加密。 不指定该字段时，云硬盘的加密属性与数据源保持一致，如果不是从数据源创建的场景，则默认不加密。  full_clone 从快照创建云硬盘时的创建方式。 * 0表示使用链接克隆方式。 * 1表示使用全量克隆方式。  hw:passthrough * true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。 * false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。 * 该字段不存在时，云硬盘默认为VBD类型。  orderID metadata中的表示云硬盘计费类型的字段。 当该字段有值时，表示该云硬盘的计费类型为包周期计费，否则计费类型为按需计费。
        :type metadata: dict(str, object)
        :param updated_at: 云硬盘更新时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX
        :type updated_at: str
        :param encrypted: 当前云硬盘服务不支持该字段。
        :type encrypted: bool
        :param replication_status: 预留属性。
        :type replication_status: str
        :param os_volume_replicationextended_status: 预留属性。
        :type os_volume_replicationextended_status: str
        :param os_vol_mig_status_attrmigstat: 预留属性。
        :type os_vol_mig_status_attrmigstat: str
        :param os_vol_mig_status_attrname_id: 预留属性。
        :type os_vol_mig_status_attrname_id: str
        :param shareable: 是否为共享云硬盘。true为共享盘，false为普通云硬盘。 该字段已经废弃，请使用multiattach。
        :type shareable: str
        :param user_id: 预留属性。
        :type user_id: str
        :param service_type: 服务类型，结果为EVS、DSS、DESS。
        :type service_type: str
        :param multiattach: 是否为共享云硬盘。
        :type multiattach: bool
        :param dedicated_storage_id: 云硬盘所属的专属存储池ID。
        :type dedicated_storage_id: str
        :param dedicated_storage_name: 云硬盘所属的专属存储池的名称。
        :type dedicated_storage_name: str
        :param tags: 云硬盘的标签。 如果云硬盘有标签，则会有该字段，否则该字段为空。
        :type tags: dict(str, str)
        :param wwn: 云硬盘挂载时的唯一标识。
        :type wwn: str
        :param enterprise_project_id: 云硬盘上绑定的企业项目ID。 &gt; 说明： &gt;  &gt; 关于企业项目ID的获取及企业项目特性的详细信息，请参见：\&quot;[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)\&quot;。
        :type enterprise_project_id: str
        :param serial_number: 云硬盘序列号。 只有SCSI类型的非双活卷才会返回该字段，用于与虚拟机中的盘做对应关系。
        :type serial_number: str
        :param iops: 
        :type iops: :class:`huaweicloudsdkevs.v2.Iops`
        :param throughput: 
        :type throughput: :class:`huaweicloudsdkevs.v2.Throughput`
        """
        
        

        self._id = None
        self._links = None
        self._name = None
        self._status = None
        self._attachments = None
        self._availability_zone = None
        self._os_vol_host_attrhost = None
        self._source_volid = None
        self._snapshot_id = None
        self._description = None
        self._created_at = None
        self._os_vol_tenant_attrtenant_id = None
        self._volume_image_metadata = None
        self._volume_type = None
        self._size = None
        self._consistencygroup_id = None
        self._bootable = None
        self._metadata = None
        self._updated_at = None
        self._encrypted = None
        self._replication_status = None
        self._os_volume_replicationextended_status = None
        self._os_vol_mig_status_attrmigstat = None
        self._os_vol_mig_status_attrname_id = None
        self._shareable = None
        self._user_id = None
        self._service_type = None
        self._multiattach = None
        self._dedicated_storage_id = None
        self._dedicated_storage_name = None
        self._tags = None
        self._wwn = None
        self._enterprise_project_id = None
        self._serial_number = None
        self._iops = None
        self._throughput = None
        self.discriminator = None

        self.id = id
        self.links = links
        self.name = name
        self.status = status
        self.attachments = attachments
        self.availability_zone = availability_zone
        self.os_vol_host_attrhost = os_vol_host_attrhost
        if source_volid is not None:
            self.source_volid = source_volid
        self.snapshot_id = snapshot_id
        self.description = description
        self.created_at = created_at
        self.os_vol_tenant_attrtenant_id = os_vol_tenant_attrtenant_id
        self.volume_image_metadata = volume_image_metadata
        self.volume_type = volume_type
        self.size = size
        if consistencygroup_id is not None:
            self.consistencygroup_id = consistencygroup_id
        self.bootable = bootable
        self.metadata = metadata
        self.updated_at = updated_at
        if encrypted is not None:
            self.encrypted = encrypted
        self.replication_status = replication_status
        self.os_volume_replicationextended_status = os_volume_replicationextended_status
        self.os_vol_mig_status_attrmigstat = os_vol_mig_status_attrmigstat
        self.os_vol_mig_status_attrname_id = os_vol_mig_status_attrname_id
        self.shareable = shareable
        self.user_id = user_id
        self.service_type = service_type
        self.multiattach = multiattach
        if dedicated_storage_id is not None:
            self.dedicated_storage_id = dedicated_storage_id
        if dedicated_storage_name is not None:
            self.dedicated_storage_name = dedicated_storage_name
        self.tags = tags
        if wwn is not None:
            self.wwn = wwn
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if serial_number is not None:
            self.serial_number = serial_number
        if iops is not None:
            self.iops = iops
        if throughput is not None:
            self.throughput = throughput

    @property
    def id(self):
        """Gets the id of this VolumeDetail.

        云硬盘的ID。

        :return: The id of this VolumeDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeDetail.

        云硬盘的ID。

        :param id: The id of this VolumeDetail.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this VolumeDetail.

        云硬盘URI自描述信息。请参见 [links参数说明](https://support.huaweicloud.com/api-evs/evs_04_2006.html#evs_04_2006__evs_04_2010_li1077125119136)。

        :return: The links of this VolumeDetail.
        :rtype: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VolumeDetail.

        云硬盘URI自描述信息。请参见 [links参数说明](https://support.huaweicloud.com/api-evs/evs_04_2006.html#evs_04_2006__evs_04_2010_li1077125119136)。

        :param links: The links of this VolumeDetail.
        :type links: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        self._links = links

    @property
    def name(self):
        """Gets the name of this VolumeDetail.

        云硬盘名称。

        :return: The name of this VolumeDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeDetail.

        云硬盘名称。

        :param name: The name of this VolumeDetail.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this VolumeDetail.

        云硬盘状态，请参见[云硬盘状态](https://support.huaweicloud.com/api-evs/evs_04_0040.html)。

        :return: The status of this VolumeDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VolumeDetail.

        云硬盘状态，请参见[云硬盘状态](https://support.huaweicloud.com/api-evs/evs_04_0040.html)。

        :param status: The status of this VolumeDetail.
        :type status: str
        """
        self._status = status

    @property
    def attachments(self):
        """Gets the attachments of this VolumeDetail.

        云硬盘的挂载信息，请参见•[attachments参数说明](https://support.huaweicloud.com/api-evs/evs_04_2006.html#evs_04_2006__evs_04_2010_li12430153610291)。

        :return: The attachments of this VolumeDetail.
        :rtype: list[:class:`huaweicloudsdkevs.v2.Attachment`]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this VolumeDetail.

        云硬盘的挂载信息，请参见•[attachments参数说明](https://support.huaweicloud.com/api-evs/evs_04_2006.html#evs_04_2006__evs_04_2010_li12430153610291)。

        :param attachments: The attachments of this VolumeDetail.
        :type attachments: list[:class:`huaweicloudsdkevs.v2.Attachment`]
        """
        self._attachments = attachments

    @property
    def availability_zone(self):
        """Gets the availability_zone of this VolumeDetail.

        云硬盘所属的AZ信息。

        :return: The availability_zone of this VolumeDetail.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this VolumeDetail.

        云硬盘所属的AZ信息。

        :param availability_zone: The availability_zone of this VolumeDetail.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def os_vol_host_attrhost(self):
        """Gets the os_vol_host_attrhost of this VolumeDetail.

        预留属性。

        :return: The os_vol_host_attrhost of this VolumeDetail.
        :rtype: str
        """
        return self._os_vol_host_attrhost

    @os_vol_host_attrhost.setter
    def os_vol_host_attrhost(self, os_vol_host_attrhost):
        """Sets the os_vol_host_attrhost of this VolumeDetail.

        预留属性。

        :param os_vol_host_attrhost: The os_vol_host_attrhost of this VolumeDetail.
        :type os_vol_host_attrhost: str
        """
        self._os_vol_host_attrhost = os_vol_host_attrhost

    @property
    def source_volid(self):
        """Gets the source_volid of this VolumeDetail.

        源云硬盘ID，如果是从源云硬盘创建，则有值。  当前云硬盘服务不支持该字段。

        :return: The source_volid of this VolumeDetail.
        :rtype: str
        """
        return self._source_volid

    @source_volid.setter
    def source_volid(self, source_volid):
        """Sets the source_volid of this VolumeDetail.

        源云硬盘ID，如果是从源云硬盘创建，则有值。  当前云硬盘服务不支持该字段。

        :param source_volid: The source_volid of this VolumeDetail.
        :type source_volid: str
        """
        self._source_volid = source_volid

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this VolumeDetail.

        快照ID，如果是从快照创建，则有值。

        :return: The snapshot_id of this VolumeDetail.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this VolumeDetail.

        快照ID，如果是从快照创建，则有值。

        :param snapshot_id: The snapshot_id of this VolumeDetail.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

    @property
    def description(self):
        """Gets the description of this VolumeDetail.

        云硬盘描述。

        :return: The description of this VolumeDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VolumeDetail.

        云硬盘描述。

        :param description: The description of this VolumeDetail.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this VolumeDetail.

        云硬盘创建时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The created_at of this VolumeDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VolumeDetail.

        云硬盘创建时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param created_at: The created_at of this VolumeDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def os_vol_tenant_attrtenant_id(self):
        """Gets the os_vol_tenant_attrtenant_id of this VolumeDetail.

        云硬盘所属的租户ID。租户ID就是项目ID。

        :return: The os_vol_tenant_attrtenant_id of this VolumeDetail.
        :rtype: str
        """
        return self._os_vol_tenant_attrtenant_id

    @os_vol_tenant_attrtenant_id.setter
    def os_vol_tenant_attrtenant_id(self, os_vol_tenant_attrtenant_id):
        """Sets the os_vol_tenant_attrtenant_id of this VolumeDetail.

        云硬盘所属的租户ID。租户ID就是项目ID。

        :param os_vol_tenant_attrtenant_id: The os_vol_tenant_attrtenant_id of this VolumeDetail.
        :type os_vol_tenant_attrtenant_id: str
        """
        self._os_vol_tenant_attrtenant_id = os_vol_tenant_attrtenant_id

    @property
    def volume_image_metadata(self):
        """Gets the volume_image_metadata of this VolumeDetail.

        云硬盘镜像的元数据。 > 说明： >  > 关于“volume_image_metadata”字段的详细说明，具体请参见：\"[查询镜像详情](https://support.huaweicloud.com/api-ims/ims_03_0703.html)\"。

        :return: The volume_image_metadata of this VolumeDetail.
        :rtype: dict(str, object)
        """
        return self._volume_image_metadata

    @volume_image_metadata.setter
    def volume_image_metadata(self, volume_image_metadata):
        """Sets the volume_image_metadata of this VolumeDetail.

        云硬盘镜像的元数据。 > 说明： >  > 关于“volume_image_metadata”字段的详细说明，具体请参见：\"[查询镜像详情](https://support.huaweicloud.com/api-ims/ims_03_0703.html)\"。

        :param volume_image_metadata: The volume_image_metadata of this VolumeDetail.
        :type volume_image_metadata: dict(str, object)
        """
        self._volume_image_metadata = volume_image_metadata

    @property
    def volume_type(self):
        """Gets the volume_type of this VolumeDetail.

        云硬盘类型。 目前支持\"SATA\"，\"SAS\"，\"GPSSD\"，\"SSD\"，\"ESSD\"，\"GPSSD2\",\"ESSD2\"七种。  - \"SATA\"为普通IO云硬盘 - \"SAS\"为高IO云硬盘 - \"GPSSD\"为通用型SSD云硬盘 - \"SSD\"为超高IO云硬盘 - \"ESSD\"为极速IO云硬盘 - \"GPSSD2\"为通用型SSD V2云硬盘 - \"ESSD2\"为极速型SSD V2云硬盘

        :return: The volume_type of this VolumeDetail.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this VolumeDetail.

        云硬盘类型。 目前支持\"SATA\"，\"SAS\"，\"GPSSD\"，\"SSD\"，\"ESSD\"，\"GPSSD2\",\"ESSD2\"七种。  - \"SATA\"为普通IO云硬盘 - \"SAS\"为高IO云硬盘 - \"GPSSD\"为通用型SSD云硬盘 - \"SSD\"为超高IO云硬盘 - \"ESSD\"为极速IO云硬盘 - \"GPSSD2\"为通用型SSD V2云硬盘 - \"ESSD2\"为极速型SSD V2云硬盘

        :param volume_type: The volume_type of this VolumeDetail.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def size(self):
        """Gets the size of this VolumeDetail.

        云硬盘大小，单位为GB。

        :return: The size of this VolumeDetail.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeDetail.

        云硬盘大小，单位为GB。

        :param size: The size of this VolumeDetail.
        :type size: int
        """
        self._size = size

    @property
    def consistencygroup_id(self):
        """Gets the consistencygroup_id of this VolumeDetail.

        预留属性。

        :return: The consistencygroup_id of this VolumeDetail.
        :rtype: str
        """
        return self._consistencygroup_id

    @consistencygroup_id.setter
    def consistencygroup_id(self, consistencygroup_id):
        """Sets the consistencygroup_id of this VolumeDetail.

        预留属性。

        :param consistencygroup_id: The consistencygroup_id of this VolumeDetail.
        :type consistencygroup_id: str
        """
        self._consistencygroup_id = consistencygroup_id

    @property
    def bootable(self):
        """Gets the bootable of this VolumeDetail.

        是否为启动云硬盘。 true：表示为启动云硬盘。 false：表示为非启动云硬盘。

        :return: The bootable of this VolumeDetail.
        :rtype: str
        """
        return self._bootable

    @bootable.setter
    def bootable(self, bootable):
        """Sets the bootable of this VolumeDetail.

        是否为启动云硬盘。 true：表示为启动云硬盘。 false：表示为非启动云硬盘。

        :param bootable: The bootable of this VolumeDetail.
        :type bootable: str
        """
        self._bootable = bootable

    @property
    def metadata(self):
        """Gets the metadata of this VolumeDetail.

        云硬盘的元数据。  __system__cmkid metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。 >  > 请求获取密钥ID的方法请参考：\"[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)\"。  __system__encrypted metadata中的表示加密功能的字段，0代表不加密，1代表加密。 不指定该字段时，云硬盘的加密属性与数据源保持一致，如果不是从数据源创建的场景，则默认不加密。  full_clone 从快照创建云硬盘时的创建方式。 * 0表示使用链接克隆方式。 * 1表示使用全量克隆方式。  hw:passthrough * true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。 * false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。 * 该字段不存在时，云硬盘默认为VBD类型。  orderID metadata中的表示云硬盘计费类型的字段。 当该字段有值时，表示该云硬盘的计费类型为包周期计费，否则计费类型为按需计费。

        :return: The metadata of this VolumeDetail.
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this VolumeDetail.

        云硬盘的元数据。  __system__cmkid metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。 >  > 请求获取密钥ID的方法请参考：\"[查询密钥列表](https://support.huaweicloud.com/api-dew/ListKeys.html)\"。  __system__encrypted metadata中的表示加密功能的字段，0代表不加密，1代表加密。 不指定该字段时，云硬盘的加密属性与数据源保持一致，如果不是从数据源创建的场景，则默认不加密。  full_clone 从快照创建云硬盘时的创建方式。 * 0表示使用链接克隆方式。 * 1表示使用全量克隆方式。  hw:passthrough * true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。 * false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。 * 该字段不存在时，云硬盘默认为VBD类型。  orderID metadata中的表示云硬盘计费类型的字段。 当该字段有值时，表示该云硬盘的计费类型为包周期计费，否则计费类型为按需计费。

        :param metadata: The metadata of this VolumeDetail.
        :type metadata: dict(str, object)
        """
        self._metadata = metadata

    @property
    def updated_at(self):
        """Gets the updated_at of this VolumeDetail.

        云硬盘更新时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The updated_at of this VolumeDetail.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VolumeDetail.

        云硬盘更新时间。 时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param updated_at: The updated_at of this VolumeDetail.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def encrypted(self):
        """Gets the encrypted of this VolumeDetail.

        当前云硬盘服务不支持该字段。

        :return: The encrypted of this VolumeDetail.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this VolumeDetail.

        当前云硬盘服务不支持该字段。

        :param encrypted: The encrypted of this VolumeDetail.
        :type encrypted: bool
        """
        self._encrypted = encrypted

    @property
    def replication_status(self):
        """Gets the replication_status of this VolumeDetail.

        预留属性。

        :return: The replication_status of this VolumeDetail.
        :rtype: str
        """
        return self._replication_status

    @replication_status.setter
    def replication_status(self, replication_status):
        """Sets the replication_status of this VolumeDetail.

        预留属性。

        :param replication_status: The replication_status of this VolumeDetail.
        :type replication_status: str
        """
        self._replication_status = replication_status

    @property
    def os_volume_replicationextended_status(self):
        """Gets the os_volume_replicationextended_status of this VolumeDetail.

        预留属性。

        :return: The os_volume_replicationextended_status of this VolumeDetail.
        :rtype: str
        """
        return self._os_volume_replicationextended_status

    @os_volume_replicationextended_status.setter
    def os_volume_replicationextended_status(self, os_volume_replicationextended_status):
        """Sets the os_volume_replicationextended_status of this VolumeDetail.

        预留属性。

        :param os_volume_replicationextended_status: The os_volume_replicationextended_status of this VolumeDetail.
        :type os_volume_replicationextended_status: str
        """
        self._os_volume_replicationextended_status = os_volume_replicationextended_status

    @property
    def os_vol_mig_status_attrmigstat(self):
        """Gets the os_vol_mig_status_attrmigstat of this VolumeDetail.

        预留属性。

        :return: The os_vol_mig_status_attrmigstat of this VolumeDetail.
        :rtype: str
        """
        return self._os_vol_mig_status_attrmigstat

    @os_vol_mig_status_attrmigstat.setter
    def os_vol_mig_status_attrmigstat(self, os_vol_mig_status_attrmigstat):
        """Sets the os_vol_mig_status_attrmigstat of this VolumeDetail.

        预留属性。

        :param os_vol_mig_status_attrmigstat: The os_vol_mig_status_attrmigstat of this VolumeDetail.
        :type os_vol_mig_status_attrmigstat: str
        """
        self._os_vol_mig_status_attrmigstat = os_vol_mig_status_attrmigstat

    @property
    def os_vol_mig_status_attrname_id(self):
        """Gets the os_vol_mig_status_attrname_id of this VolumeDetail.

        预留属性。

        :return: The os_vol_mig_status_attrname_id of this VolumeDetail.
        :rtype: str
        """
        return self._os_vol_mig_status_attrname_id

    @os_vol_mig_status_attrname_id.setter
    def os_vol_mig_status_attrname_id(self, os_vol_mig_status_attrname_id):
        """Sets the os_vol_mig_status_attrname_id of this VolumeDetail.

        预留属性。

        :param os_vol_mig_status_attrname_id: The os_vol_mig_status_attrname_id of this VolumeDetail.
        :type os_vol_mig_status_attrname_id: str
        """
        self._os_vol_mig_status_attrname_id = os_vol_mig_status_attrname_id

    @property
    def shareable(self):
        """Gets the shareable of this VolumeDetail.

        是否为共享云硬盘。true为共享盘，false为普通云硬盘。 该字段已经废弃，请使用multiattach。

        :return: The shareable of this VolumeDetail.
        :rtype: str
        """
        return self._shareable

    @shareable.setter
    def shareable(self, shareable):
        """Sets the shareable of this VolumeDetail.

        是否为共享云硬盘。true为共享盘，false为普通云硬盘。 该字段已经废弃，请使用multiattach。

        :param shareable: The shareable of this VolumeDetail.
        :type shareable: str
        """
        self._shareable = shareable

    @property
    def user_id(self):
        """Gets the user_id of this VolumeDetail.

        预留属性。

        :return: The user_id of this VolumeDetail.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this VolumeDetail.

        预留属性。

        :param user_id: The user_id of this VolumeDetail.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def service_type(self):
        """Gets the service_type of this VolumeDetail.

        服务类型，结果为EVS、DSS、DESS。

        :return: The service_type of this VolumeDetail.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this VolumeDetail.

        服务类型，结果为EVS、DSS、DESS。

        :param service_type: The service_type of this VolumeDetail.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def multiattach(self):
        """Gets the multiattach of this VolumeDetail.

        是否为共享云硬盘。

        :return: The multiattach of this VolumeDetail.
        :rtype: bool
        """
        return self._multiattach

    @multiattach.setter
    def multiattach(self, multiattach):
        """Sets the multiattach of this VolumeDetail.

        是否为共享云硬盘。

        :param multiattach: The multiattach of this VolumeDetail.
        :type multiattach: bool
        """
        self._multiattach = multiattach

    @property
    def dedicated_storage_id(self):
        """Gets the dedicated_storage_id of this VolumeDetail.

        云硬盘所属的专属存储池ID。

        :return: The dedicated_storage_id of this VolumeDetail.
        :rtype: str
        """
        return self._dedicated_storage_id

    @dedicated_storage_id.setter
    def dedicated_storage_id(self, dedicated_storage_id):
        """Sets the dedicated_storage_id of this VolumeDetail.

        云硬盘所属的专属存储池ID。

        :param dedicated_storage_id: The dedicated_storage_id of this VolumeDetail.
        :type dedicated_storage_id: str
        """
        self._dedicated_storage_id = dedicated_storage_id

    @property
    def dedicated_storage_name(self):
        """Gets the dedicated_storage_name of this VolumeDetail.

        云硬盘所属的专属存储池的名称。

        :return: The dedicated_storage_name of this VolumeDetail.
        :rtype: str
        """
        return self._dedicated_storage_name

    @dedicated_storage_name.setter
    def dedicated_storage_name(self, dedicated_storage_name):
        """Sets the dedicated_storage_name of this VolumeDetail.

        云硬盘所属的专属存储池的名称。

        :param dedicated_storage_name: The dedicated_storage_name of this VolumeDetail.
        :type dedicated_storage_name: str
        """
        self._dedicated_storage_name = dedicated_storage_name

    @property
    def tags(self):
        """Gets the tags of this VolumeDetail.

        云硬盘的标签。 如果云硬盘有标签，则会有该字段，否则该字段为空。

        :return: The tags of this VolumeDetail.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VolumeDetail.

        云硬盘的标签。 如果云硬盘有标签，则会有该字段，否则该字段为空。

        :param tags: The tags of this VolumeDetail.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def wwn(self):
        """Gets the wwn of this VolumeDetail.

        云硬盘挂载时的唯一标识。

        :return: The wwn of this VolumeDetail.
        :rtype: str
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """Sets the wwn of this VolumeDetail.

        云硬盘挂载时的唯一标识。

        :param wwn: The wwn of this VolumeDetail.
        :type wwn: str
        """
        self._wwn = wwn

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this VolumeDetail.

        云硬盘上绑定的企业项目ID。 > 说明： >  > 关于企业项目ID的获取及企业项目特性的详细信息，请参见：\"[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)\"。

        :return: The enterprise_project_id of this VolumeDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this VolumeDetail.

        云硬盘上绑定的企业项目ID。 > 说明： >  > 关于企业项目ID的获取及企业项目特性的详细信息，请参见：\"[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)\"。

        :param enterprise_project_id: The enterprise_project_id of this VolumeDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def serial_number(self):
        """Gets the serial_number of this VolumeDetail.

        云硬盘序列号。 只有SCSI类型的非双活卷才会返回该字段，用于与虚拟机中的盘做对应关系。

        :return: The serial_number of this VolumeDetail.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this VolumeDetail.

        云硬盘序列号。 只有SCSI类型的非双活卷才会返回该字段，用于与虚拟机中的盘做对应关系。

        :param serial_number: The serial_number of this VolumeDetail.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def iops(self):
        """Gets the iops of this VolumeDetail.

        :return: The iops of this VolumeDetail.
        :rtype: :class:`huaweicloudsdkevs.v2.Iops`
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this VolumeDetail.

        :param iops: The iops of this VolumeDetail.
        :type iops: :class:`huaweicloudsdkevs.v2.Iops`
        """
        self._iops = iops

    @property
    def throughput(self):
        """Gets the throughput of this VolumeDetail.

        :return: The throughput of this VolumeDetail.
        :rtype: :class:`huaweicloudsdkevs.v2.Throughput`
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """Sets the throughput of this VolumeDetail.

        :param throughput: The throughput of this VolumeDetail.
        :type throughput: :class:`huaweicloudsdkevs.v2.Throughput`
        """
        self._throughput = throughput

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
        if not isinstance(other, VolumeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
