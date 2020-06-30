# coding: utf-8

import pprint
import re

import six


class VolumeDetail(object):


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
        'attachments': 'list[VolumeAttachment]',
        'availability_zone': 'str',
        'source_volid': 'str',
        'snapshot_id': 'str',
        'description': 'str',
        'bootable': 'str',
        'encrypted': 'bool',
        'created_at': 'str',
        'volume_type': 'str',
        'replication_status': 'str',
        'consistencygroup_id': 'str',
        'metadata': 'VolumeMetadata',
        'size': 'int',
        'user_id': 'str',
        'updated_at': 'str',
        'shareable': 'bool',
        'multiattach': 'bool',
        'os_vol_tenant_attrtenant_id': 'str',
        'volume_image_metadata': 'str',
        'os_vol_host_attrhost': 'str',
        'os_volume_replicationextended_status': 'str',
        'os_vol_mig_status_attrmigstat': 'str',
        'os_vol_mig_status_attrname_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'name': 'name',
        'status': 'status',
        'attachments': 'attachments',
        'availability_zone': 'availability_zone',
        'source_volid': 'source_volid',
        'snapshot_id': 'snapshot_id',
        'description': 'description',
        'bootable': 'bootable',
        'encrypted': 'encrypted',
        'created_at': 'created_at',
        'volume_type': 'volume_type',
        'replication_status': 'replication_status',
        'consistencygroup_id': 'consistencygroup_id',
        'metadata': 'metadata',
        'size': 'size',
        'user_id': 'user_id',
        'updated_at': 'updated_at',
        'shareable': 'shareable',
        'multiattach': 'multiattach',
        'os_vol_tenant_attrtenant_id': 'os-vol-tenant-attr:tenant_id',
        'volume_image_metadata': 'volume_image_metadata',
        'os_vol_host_attrhost': 'os-vol-host-attr:host',
        'os_volume_replicationextended_status': 'os-volume-replication:extended_status',
        'os_vol_mig_status_attrmigstat': 'os-vol-mig-status-attr:migstat',
        'os_vol_mig_status_attrname_id': 'os-vol-mig-status-attr:name_id'
    }

    def __init__(self, id=None, links=None, name=None, status=None, attachments=None, availability_zone=None, source_volid=None, snapshot_id=None, description=None, bootable=None, encrypted=None, created_at=None, volume_type=None, replication_status=None, consistencygroup_id=None, metadata=None, size=None, user_id=None, updated_at=None, shareable=None, multiattach=None, os_vol_tenant_attrtenant_id=None, volume_image_metadata=None, os_vol_host_attrhost=None, os_volume_replicationextended_status=None, os_vol_mig_status_attrmigstat=None, os_vol_mig_status_attrname_id=None):  # noqa: E501
        """VolumeDetail - a model defined in huaweicloud sdk"""

        self._id = None
        self._links = None
        self._name = None
        self._status = None
        self._attachments = None
        self._availability_zone = None
        self._source_volid = None
        self._snapshot_id = None
        self._description = None
        self._bootable = None
        self._encrypted = None
        self._created_at = None
        self._volume_type = None
        self._replication_status = None
        self._consistencygroup_id = None
        self._metadata = None
        self._size = None
        self._user_id = None
        self._updated_at = None
        self._shareable = None
        self._multiattach = None
        self._os_vol_tenant_attrtenant_id = None
        self._volume_image_metadata = None
        self._os_vol_host_attrhost = None
        self._os_volume_replicationextended_status = None
        self._os_vol_mig_status_attrmigstat = None
        self._os_vol_mig_status_attrname_id = None
        self.discriminator = None

        self.id = id
        self.links = links
        if name is not None:
            self.name = name
        self.status = status
        if attachments is not None:
            self.attachments = attachments
        self.availability_zone = availability_zone
        if source_volid is not None:
            self.source_volid = source_volid
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        if description is not None:
            self.description = description
        if bootable is not None:
            self.bootable = bootable
        if encrypted is not None:
            self.encrypted = encrypted
        self.created_at = created_at
        self.volume_type = volume_type
        self.replication_status = replication_status
        if consistencygroup_id is not None:
            self.consistencygroup_id = consistencygroup_id
        self.metadata = metadata
        self.size = size
        self.user_id = user_id
        if updated_at is not None:
            self.updated_at = updated_at
        self.shareable = shareable
        self.multiattach = multiattach
        if os_vol_tenant_attrtenant_id is not None:
            self.os_vol_tenant_attrtenant_id = os_vol_tenant_attrtenant_id
        if volume_image_metadata is not None:
            self.volume_image_metadata = volume_image_metadata
        if os_vol_host_attrhost is not None:
            self.os_vol_host_attrhost = os_vol_host_attrhost
        if os_volume_replicationextended_status is not None:
            self.os_volume_replicationextended_status = os_volume_replicationextended_status
        if os_vol_mig_status_attrmigstat is not None:
            self.os_vol_mig_status_attrmigstat = os_vol_mig_status_attrmigstat
        if os_vol_mig_status_attrname_id is not None:
            self.os_vol_mig_status_attrname_id = os_vol_mig_status_attrname_id

    @property
    def id(self):
        """Gets the id of this VolumeDetail.

        云硬盘ID。

        :return: The id of this VolumeDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeDetail.

        云硬盘ID。

        :param id: The id of this VolumeDetail.
        :type: str
        """
        self._id = id

    @property
    def links(self):
        """Gets the links of this VolumeDetail.

        云硬盘uri自描述信息，请参见•[links参数说明](https://support.huaweicloud.com/api-evs/evs_04_2070.html#evs_04_2070__li4929184617138)。

        :return: The links of this VolumeDetail.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VolumeDetail.

        云硬盘uri自描述信息，请参见•[links参数说明](https://support.huaweicloud.com/api-evs/evs_04_2070.html#evs_04_2070__li4929184617138)。

        :param links: The links of this VolumeDetail.
        :type: list[Link]
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
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this VolumeDetail.

        云硬盘状态，具体请参见[云硬盘状态](https://support.huaweicloud.com/api-evs/evs_04_0040.html)。

        :return: The status of this VolumeDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VolumeDetail.

        云硬盘状态，具体请参见[云硬盘状态](https://support.huaweicloud.com/api-evs/evs_04_0040.html)。

        :param status: The status of this VolumeDetail.
        :type: str
        """
        self._status = status

    @property
    def attachments(self):
        """Gets the attachments of this VolumeDetail.

        是否挂载信息。

        :return: The attachments of this VolumeDetail.
        :rtype: list[VolumeAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this VolumeDetail.

        是否挂载信息。

        :param attachments: The attachments of this VolumeDetail.
        :type: list[VolumeAttachment]
        """
        self._attachments = attachments

    @property
    def availability_zone(self):
        """Gets the availability_zone of this VolumeDetail.

        云硬盘所属AZ。

        :return: The availability_zone of this VolumeDetail.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this VolumeDetail.

        云硬盘所属AZ。

        :param availability_zone: The availability_zone of this VolumeDetail.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def source_volid(self):
        """Gets the source_volid of this VolumeDetail.

        源云硬盘ID，如果是从源云硬盘创建，则有值。 当前云硬盘服务不支持该字段。

        :return: The source_volid of this VolumeDetail.
        :rtype: str
        """
        return self._source_volid

    @source_volid.setter
    def source_volid(self, source_volid):
        """Sets the source_volid of this VolumeDetail.

        源云硬盘ID，如果是从源云硬盘创建，则有值。 当前云硬盘服务不支持该字段。

        :param source_volid: The source_volid of this VolumeDetail.
        :type: str
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
        :type: str
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
        :type: str
        """
        self._description = description

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
        :type: str
        """
        self._bootable = bootable

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
        :type: bool
        """
        self._encrypted = encrypted

    @property
    def created_at(self):
        """Gets the created_at of this VolumeDetail.

        云硬盘创建时间。  时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The created_at of this VolumeDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VolumeDetail.

        云硬盘创建时间。  时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param created_at: The created_at of this VolumeDetail.
        :type: str
        """
        self._created_at = created_at

    @property
    def volume_type(self):
        """Gets the volume_type of this VolumeDetail.

        云硬盘类型。  目前支持“SSD”，“SAS”和“SATA”三种。 “SSD”为超高IO云硬盘 “SAS”为高IO云硬盘 “SATA”为普通IO云硬盘

        :return: The volume_type of this VolumeDetail.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this VolumeDetail.

        云硬盘类型。  目前支持“SSD”，“SAS”和“SATA”三种。 “SSD”为超高IO云硬盘 “SAS”为高IO云硬盘 “SATA”为普通IO云硬盘

        :param volume_type: The volume_type of this VolumeDetail.
        :type: str
        """
        self._volume_type = volume_type

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
        :type: str
        """
        self._replication_status = replication_status

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
        :type: str
        """
        self._consistencygroup_id = consistencygroup_id

    @property
    def metadata(self):
        """Gets the metadata of this VolumeDetail.


        :return: The metadata of this VolumeDetail.
        :rtype: VolumeMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this VolumeDetail.


        :param metadata: The metadata of this VolumeDetail.
        :type: VolumeMetadata
        """
        self._metadata = metadata

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
        :type: int
        """
        self._size = size

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
        :type: str
        """
        self._user_id = user_id

    @property
    def updated_at(self):
        """Gets the updated_at of this VolumeDetail.

        云硬盘更新时间。  时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The updated_at of this VolumeDetail.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VolumeDetail.

        云硬盘更新时间。  时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param updated_at: The updated_at of this VolumeDetail.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def shareable(self):
        """Gets the shareable of this VolumeDetail.

        是否为可共享云硬盘。 说明： 该字段已经废弃，请使用multiattach。

        :return: The shareable of this VolumeDetail.
        :rtype: bool
        """
        return self._shareable

    @shareable.setter
    def shareable(self, shareable):
        """Sets the shareable of this VolumeDetail.

        是否为可共享云硬盘。 说明： 该字段已经废弃，请使用multiattach。

        :param shareable: The shareable of this VolumeDetail.
        :type: bool
        """
        self._shareable = shareable

    @property
    def multiattach(self):
        """Gets the multiattach of this VolumeDetail.

        是否为可共享云硬盘。

        :return: The multiattach of this VolumeDetail.
        :rtype: bool
        """
        return self._multiattach

    @multiattach.setter
    def multiattach(self, multiattach):
        """Sets the multiattach of this VolumeDetail.

        是否为可共享云硬盘。

        :param multiattach: The multiattach of this VolumeDetail.
        :type: bool
        """
        self._multiattach = multiattach

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
        :type: str
        """
        self._os_vol_tenant_attrtenant_id = os_vol_tenant_attrtenant_id

    @property
    def volume_image_metadata(self):
        """Gets the volume_image_metadata of this VolumeDetail.

        云硬盘镜像的元数据。

        :return: The volume_image_metadata of this VolumeDetail.
        :rtype: str
        """
        return self._volume_image_metadata

    @volume_image_metadata.setter
    def volume_image_metadata(self, volume_image_metadata):
        """Sets the volume_image_metadata of this VolumeDetail.

        云硬盘镜像的元数据。

        :param volume_image_metadata: The volume_image_metadata of this VolumeDetail.
        :type: str
        """
        self._volume_image_metadata = volume_image_metadata

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
        :type: str
        """
        self._os_vol_host_attrhost = os_vol_host_attrhost

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
        :type: str
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
        :type: str
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
        :type: str
        """
        self._os_vol_mig_status_attrname_id = os_vol_mig_status_attrname_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VolumeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
