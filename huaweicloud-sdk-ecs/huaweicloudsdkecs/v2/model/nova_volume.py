# coding: utf-8

import pprint
import re

import six


class NovaVolume(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'attachments': 'list[NovaVolumeAttachment]',
        'availability_zone': 'str',
        'created_at': 'str',
        'display_description': 'str',
        'display_name': 'str',
        'id': 'str',
        'metadata': 'dict(str, str)',
        'size': 'int',
        'snapshot_id': 'str',
        'status': 'str',
        'volume_type': 'str'
    }

    attribute_map = {
        'attachments': 'attachments',
        'availability_zone': 'availabilityZone',
        'created_at': 'createdAt',
        'display_description': 'displayDescription',
        'display_name': 'displayName',
        'id': 'id',
        'metadata': 'metadata',
        'size': 'size',
        'snapshot_id': 'snapshotId',
        'status': 'status',
        'volume_type': 'volumeType'
    }

    def __init__(self, attachments=None, availability_zone=None, created_at=None, display_description=None, display_name=None, id=None, metadata=None, size=None, snapshot_id=None, status=None, volume_type=None):  # noqa: E501
        """NovaVolume - a model defined in huaweicloud sdk"""

        self._attachments = None
        self._availability_zone = None
        self._created_at = None
        self._display_description = None
        self._display_name = None
        self._id = None
        self._metadata = None
        self._size = None
        self._snapshot_id = None
        self._status = None
        self._volume_type = None
        self.discriminator = None

        if attachments is not None:
            self.attachments = attachments
        self.availability_zone = availability_zone
        self.created_at = created_at
        if display_description is not None:
            self.display_description = display_description
        if display_name is not None:
            self.display_name = display_name
        self.id = id
        self.metadata = metadata
        self.size = size
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        self.status = status
        self.volume_type = volume_type

    @property
    def attachments(self):
        """Gets the attachments of this NovaVolume.

        挂卷信息

        :return: The attachments of this NovaVolume.
        :rtype: list[NovaVolumeAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this NovaVolume.

        挂卷信息

        :param attachments: The attachments of this NovaVolume.
        :type: list[NovaVolumeAttachment]
        """
        self._attachments = attachments

    @property
    def availability_zone(self):
        """Gets the availability_zone of this NovaVolume.

        卷所属AZ

        :return: The availability_zone of this NovaVolume.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this NovaVolume.

        卷所属AZ

        :param availability_zone: The availability_zone of this NovaVolume.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def created_at(self):
        """Gets the created_at of this NovaVolume.

        创建卷的时间

        :return: The created_at of this NovaVolume.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NovaVolume.

        创建卷的时间

        :param created_at: The created_at of this NovaVolume.
        :type: str
        """
        self._created_at = created_at

    @property
    def display_description(self):
        """Gets the display_description of this NovaVolume.

        卷描述

        :return: The display_description of this NovaVolume.
        :rtype: str
        """
        return self._display_description

    @display_description.setter
    def display_description(self, display_description):
        """Sets the display_description of this NovaVolume.

        卷描述

        :param display_description: The display_description of this NovaVolume.
        :type: str
        """
        self._display_description = display_description

    @property
    def display_name(self):
        """Gets the display_name of this NovaVolume.

        卷名称

        :return: The display_name of this NovaVolume.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this NovaVolume.

        卷名称

        :param display_name: The display_name of this NovaVolume.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this NovaVolume.

        卷ID，UUID格式。

        :return: The id of this NovaVolume.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaVolume.

        卷ID，UUID格式。

        :param id: The id of this NovaVolume.
        :type: str
        """
        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this NovaVolume.

        元数据

        :return: The metadata of this NovaVolume.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NovaVolume.

        元数据

        :param metadata: The metadata of this NovaVolume.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def size(self):
        """Gets the size of this NovaVolume.

        卷大小

        :return: The size of this NovaVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this NovaVolume.

        卷大小

        :param size: The size of this NovaVolume.
        :type: int
        """
        self._size = size

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this NovaVolume.

        快照ID

        :return: The snapshot_id of this NovaVolume.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this NovaVolume.

        快照ID

        :param snapshot_id: The snapshot_id of this NovaVolume.
        :type: str
        """
        self._snapshot_id = snapshot_id

    @property
    def status(self):
        """Gets the status of this NovaVolume.

        卷状态

        :return: The status of this NovaVolume.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NovaVolume.

        卷状态

        :param status: The status of this NovaVolume.
        :type: str
        """
        self._status = status

    @property
    def volume_type(self):
        """Gets the volume_type of this NovaVolume.

        卷类型

        :return: The volume_type of this NovaVolume.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this NovaVolume.

        卷类型

        :param volume_type: The volume_type of this NovaVolume.
        :type: str
        """
        self._volume_type = volume_type

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
        if not isinstance(other, NovaVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
