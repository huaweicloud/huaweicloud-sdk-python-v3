# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVolumeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attachments': 'list[Attachment]',
        'availability_zone': 'str',
        'bootable': 'str',
        'created_at': 'str',
        'id': 'str',
        'links': 'list[Link]',
        'metadata': 'VolumeMetadata',
        'multiattach': 'bool',
        'name': 'str',
        'os_vol_host_attrhost': 'str',
        'os_vol_tenant_attrtenant_id': 'str',
        'shareable': 'str',
        'size': 'int',
        'snapshot_id': 'str',
        'source_volid': 'str',
        'status': 'str',
        'volume_image_metadata': 'object',
        'volume_type': 'str',
        'description': 'str',
        'os_volume_replicationextended_status': 'str'
    }

    attribute_map = {
        'attachments': 'attachments',
        'availability_zone': 'availability_zone',
        'bootable': 'bootable',
        'created_at': 'created_at',
        'id': 'id',
        'links': 'links',
        'metadata': 'metadata',
        'multiattach': 'multiattach',
        'name': 'name',
        'os_vol_host_attrhost': 'os-vol-host-attr:host',
        'os_vol_tenant_attrtenant_id': 'os-vol-tenant-attr:tenant_id',
        'shareable': 'shareable',
        'size': 'size',
        'snapshot_id': 'snapshot_id',
        'source_volid': 'source_volid',
        'status': 'status',
        'volume_image_metadata': 'volume_image_metadata',
        'volume_type': 'volume_type',
        'description': 'description',
        'os_volume_replicationextended_status': 'os-volume-replication:extended_status'
    }

    def __init__(self, attachments=None, availability_zone=None, bootable=None, created_at=None, id=None, links=None, metadata=None, multiattach=None, name=None, os_vol_host_attrhost=None, os_vol_tenant_attrtenant_id=None, shareable=None, size=None, snapshot_id=None, source_volid=None, status=None, volume_image_metadata=None, volume_type=None, description=None, os_volume_replicationextended_status=None):
        """UpdateVolumeResponse

        The model defined in huaweicloud sdk

        :param attachments: 是否挂载信息。
        :type attachments: list[:class:`huaweicloudsdkevs.v2.Attachment`]
        :param availability_zone: 云硬盘所属AZ。
        :type availability_zone: str
        :param bootable: 是否为可启动云硬盘。
        :type bootable: str
        :param created_at: 创建云硬盘的时间。
        :type created_at: str
        :param id: 云硬盘ID。
        :type id: str
        :param links: 云硬盘uri自描述信息
        :type links: list[:class:`huaweicloudsdkevs.v2.Link`]
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkevs.v2.VolumeMetadata`
        :param multiattach: 是否为可共享云硬盘。
        :type multiattach: bool
        :param name: 云硬盘名称
        :type name: str
        :param os_vol_host_attrhost: 预留属性。
        :type os_vol_host_attrhost: str
        :param os_vol_tenant_attrtenant_id: 云硬盘所属的项目ID。
        :type os_vol_tenant_attrtenant_id: str
        :param shareable: 是否为共享云硬盘。
        :type shareable: str
        :param size: 云硬盘大小。
        :type size: int
        :param snapshot_id: 快照ID。
        :type snapshot_id: str
        :param source_volid: 预留字段。
        :type source_volid: str
        :param status: 云硬盘状态。
        :type status: str
        :param volume_image_metadata: 云硬盘镜像的元数据。 &gt; 说明： &gt;  &gt; 关于“volume_image_metadata”字段的详细说明，具体请参见：\&quot;[查询镜像详情](https://support.huaweicloud.com/api-ims/ims_03_0703.html)\&quot;。
        :type volume_image_metadata: object
        :param volume_type: 云硬盘类型。
        :type volume_type: str
        :param description: 云硬盘描述。
        :type description: str
        :param os_volume_replicationextended_status: 预留属性。
        :type os_volume_replicationextended_status: str
        """
        
        super(UpdateVolumeResponse, self).__init__()

        self._attachments = None
        self._availability_zone = None
        self._bootable = None
        self._created_at = None
        self._id = None
        self._links = None
        self._metadata = None
        self._multiattach = None
        self._name = None
        self._os_vol_host_attrhost = None
        self._os_vol_tenant_attrtenant_id = None
        self._shareable = None
        self._size = None
        self._snapshot_id = None
        self._source_volid = None
        self._status = None
        self._volume_image_metadata = None
        self._volume_type = None
        self._description = None
        self._os_volume_replicationextended_status = None
        self.discriminator = None

        if attachments is not None:
            self.attachments = attachments
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if bootable is not None:
            self.bootable = bootable
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if metadata is not None:
            self.metadata = metadata
        if multiattach is not None:
            self.multiattach = multiattach
        if name is not None:
            self.name = name
        if os_vol_host_attrhost is not None:
            self.os_vol_host_attrhost = os_vol_host_attrhost
        if os_vol_tenant_attrtenant_id is not None:
            self.os_vol_tenant_attrtenant_id = os_vol_tenant_attrtenant_id
        if shareable is not None:
            self.shareable = shareable
        if size is not None:
            self.size = size
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        if source_volid is not None:
            self.source_volid = source_volid
        if status is not None:
            self.status = status
        if volume_image_metadata is not None:
            self.volume_image_metadata = volume_image_metadata
        if volume_type is not None:
            self.volume_type = volume_type
        if description is not None:
            self.description = description
        if os_volume_replicationextended_status is not None:
            self.os_volume_replicationextended_status = os_volume_replicationextended_status

    @property
    def attachments(self):
        """Gets the attachments of this UpdateVolumeResponse.

        是否挂载信息。

        :return: The attachments of this UpdateVolumeResponse.
        :rtype: list[:class:`huaweicloudsdkevs.v2.Attachment`]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this UpdateVolumeResponse.

        是否挂载信息。

        :param attachments: The attachments of this UpdateVolumeResponse.
        :type attachments: list[:class:`huaweicloudsdkevs.v2.Attachment`]
        """
        self._attachments = attachments

    @property
    def availability_zone(self):
        """Gets the availability_zone of this UpdateVolumeResponse.

        云硬盘所属AZ。

        :return: The availability_zone of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this UpdateVolumeResponse.

        云硬盘所属AZ。

        :param availability_zone: The availability_zone of this UpdateVolumeResponse.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def bootable(self):
        """Gets the bootable of this UpdateVolumeResponse.

        是否为可启动云硬盘。

        :return: The bootable of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._bootable

    @bootable.setter
    def bootable(self, bootable):
        """Sets the bootable of this UpdateVolumeResponse.

        是否为可启动云硬盘。

        :param bootable: The bootable of this UpdateVolumeResponse.
        :type bootable: str
        """
        self._bootable = bootable

    @property
    def created_at(self):
        """Gets the created_at of this UpdateVolumeResponse.

        创建云硬盘的时间。

        :return: The created_at of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UpdateVolumeResponse.

        创建云硬盘的时间。

        :param created_at: The created_at of this UpdateVolumeResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this UpdateVolumeResponse.

        云硬盘ID。

        :return: The id of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateVolumeResponse.

        云硬盘ID。

        :param id: The id of this UpdateVolumeResponse.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this UpdateVolumeResponse.

        云硬盘uri自描述信息

        :return: The links of this UpdateVolumeResponse.
        :rtype: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UpdateVolumeResponse.

        云硬盘uri自描述信息

        :param links: The links of this UpdateVolumeResponse.
        :type links: list[:class:`huaweicloudsdkevs.v2.Link`]
        """
        self._links = links

    @property
    def metadata(self):
        """Gets the metadata of this UpdateVolumeResponse.

        :return: The metadata of this UpdateVolumeResponse.
        :rtype: :class:`huaweicloudsdkevs.v2.VolumeMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UpdateVolumeResponse.

        :param metadata: The metadata of this UpdateVolumeResponse.
        :type metadata: :class:`huaweicloudsdkevs.v2.VolumeMetadata`
        """
        self._metadata = metadata

    @property
    def multiattach(self):
        """Gets the multiattach of this UpdateVolumeResponse.

        是否为可共享云硬盘。

        :return: The multiattach of this UpdateVolumeResponse.
        :rtype: bool
        """
        return self._multiattach

    @multiattach.setter
    def multiattach(self, multiattach):
        """Sets the multiattach of this UpdateVolumeResponse.

        是否为可共享云硬盘。

        :param multiattach: The multiattach of this UpdateVolumeResponse.
        :type multiattach: bool
        """
        self._multiattach = multiattach

    @property
    def name(self):
        """Gets the name of this UpdateVolumeResponse.

        云硬盘名称

        :return: The name of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateVolumeResponse.

        云硬盘名称

        :param name: The name of this UpdateVolumeResponse.
        :type name: str
        """
        self._name = name

    @property
    def os_vol_host_attrhost(self):
        """Gets the os_vol_host_attrhost of this UpdateVolumeResponse.

        预留属性。

        :return: The os_vol_host_attrhost of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._os_vol_host_attrhost

    @os_vol_host_attrhost.setter
    def os_vol_host_attrhost(self, os_vol_host_attrhost):
        """Sets the os_vol_host_attrhost of this UpdateVolumeResponse.

        预留属性。

        :param os_vol_host_attrhost: The os_vol_host_attrhost of this UpdateVolumeResponse.
        :type os_vol_host_attrhost: str
        """
        self._os_vol_host_attrhost = os_vol_host_attrhost

    @property
    def os_vol_tenant_attrtenant_id(self):
        """Gets the os_vol_tenant_attrtenant_id of this UpdateVolumeResponse.

        云硬盘所属的项目ID。

        :return: The os_vol_tenant_attrtenant_id of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._os_vol_tenant_attrtenant_id

    @os_vol_tenant_attrtenant_id.setter
    def os_vol_tenant_attrtenant_id(self, os_vol_tenant_attrtenant_id):
        """Sets the os_vol_tenant_attrtenant_id of this UpdateVolumeResponse.

        云硬盘所属的项目ID。

        :param os_vol_tenant_attrtenant_id: The os_vol_tenant_attrtenant_id of this UpdateVolumeResponse.
        :type os_vol_tenant_attrtenant_id: str
        """
        self._os_vol_tenant_attrtenant_id = os_vol_tenant_attrtenant_id

    @property
    def shareable(self):
        """Gets the shareable of this UpdateVolumeResponse.

        是否为共享云硬盘。

        :return: The shareable of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._shareable

    @shareable.setter
    def shareable(self, shareable):
        """Sets the shareable of this UpdateVolumeResponse.

        是否为共享云硬盘。

        :param shareable: The shareable of this UpdateVolumeResponse.
        :type shareable: str
        """
        self._shareable = shareable

    @property
    def size(self):
        """Gets the size of this UpdateVolumeResponse.

        云硬盘大小。

        :return: The size of this UpdateVolumeResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this UpdateVolumeResponse.

        云硬盘大小。

        :param size: The size of this UpdateVolumeResponse.
        :type size: int
        """
        self._size = size

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this UpdateVolumeResponse.

        快照ID。

        :return: The snapshot_id of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this UpdateVolumeResponse.

        快照ID。

        :param snapshot_id: The snapshot_id of this UpdateVolumeResponse.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

    @property
    def source_volid(self):
        """Gets the source_volid of this UpdateVolumeResponse.

        预留字段。

        :return: The source_volid of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._source_volid

    @source_volid.setter
    def source_volid(self, source_volid):
        """Sets the source_volid of this UpdateVolumeResponse.

        预留字段。

        :param source_volid: The source_volid of this UpdateVolumeResponse.
        :type source_volid: str
        """
        self._source_volid = source_volid

    @property
    def status(self):
        """Gets the status of this UpdateVolumeResponse.

        云硬盘状态。

        :return: The status of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateVolumeResponse.

        云硬盘状态。

        :param status: The status of this UpdateVolumeResponse.
        :type status: str
        """
        self._status = status

    @property
    def volume_image_metadata(self):
        """Gets the volume_image_metadata of this UpdateVolumeResponse.

        云硬盘镜像的元数据。 > 说明： >  > 关于“volume_image_metadata”字段的详细说明，具体请参见：\"[查询镜像详情](https://support.huaweicloud.com/api-ims/ims_03_0703.html)\"。

        :return: The volume_image_metadata of this UpdateVolumeResponse.
        :rtype: object
        """
        return self._volume_image_metadata

    @volume_image_metadata.setter
    def volume_image_metadata(self, volume_image_metadata):
        """Sets the volume_image_metadata of this UpdateVolumeResponse.

        云硬盘镜像的元数据。 > 说明： >  > 关于“volume_image_metadata”字段的详细说明，具体请参见：\"[查询镜像详情](https://support.huaweicloud.com/api-ims/ims_03_0703.html)\"。

        :param volume_image_metadata: The volume_image_metadata of this UpdateVolumeResponse.
        :type volume_image_metadata: object
        """
        self._volume_image_metadata = volume_image_metadata

    @property
    def volume_type(self):
        """Gets the volume_type of this UpdateVolumeResponse.

        云硬盘类型。

        :return: The volume_type of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this UpdateVolumeResponse.

        云硬盘类型。

        :param volume_type: The volume_type of this UpdateVolumeResponse.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def description(self):
        """Gets the description of this UpdateVolumeResponse.

        云硬盘描述。

        :return: The description of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateVolumeResponse.

        云硬盘描述。

        :param description: The description of this UpdateVolumeResponse.
        :type description: str
        """
        self._description = description

    @property
    def os_volume_replicationextended_status(self):
        """Gets the os_volume_replicationextended_status of this UpdateVolumeResponse.

        预留属性。

        :return: The os_volume_replicationextended_status of this UpdateVolumeResponse.
        :rtype: str
        """
        return self._os_volume_replicationextended_status

    @os_volume_replicationextended_status.setter
    def os_volume_replicationextended_status(self, os_volume_replicationextended_status):
        """Sets the os_volume_replicationextended_status of this UpdateVolumeResponse.

        预留属性。

        :param os_volume_replicationextended_status: The os_volume_replicationextended_status of this UpdateVolumeResponse.
        :type os_volume_replicationextended_status: str
        """
        self._os_volume_replicationextended_status = os_volume_replicationextended_status

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
        if not isinstance(other, UpdateVolumeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
