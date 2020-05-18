# coding: utf-8

import pprint
import re

import six


class NovaCreateVolumeOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'availability_zone': 'str',
        'display_description': 'str',
        'display_name': 'str',
        'metadata': 'dict(str, str)',
        'size': 'int',
        'snapshot_id': 'str',
        'volume_type': 'str'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'display_description': 'display_description',
        'display_name': 'display_name',
        'metadata': 'metadata',
        'size': 'size',
        'snapshot_id': 'snapshot_id',
        'volume_type': 'volume_type'
    }

    def __init__(self, availability_zone=None, display_description=None, display_name=None, metadata=None, size=None, snapshot_id=None, volume_type=None):  # noqa: E501
        """NovaCreateVolumeOption - a model defined in huaweicloud sdk"""

        self._availability_zone = None
        self._display_description = None
        self._display_name = None
        self._metadata = None
        self._size = None
        self._snapshot_id = None
        self._volume_type = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if display_description is not None:
            self.display_description = display_description
        if display_name is not None:
            self.display_name = display_name
        if metadata is not None:
            self.metadata = metadata
        self.size = size
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        if volume_type is not None:
            self.volume_type = volume_type

    @property
    def availability_zone(self):
        """Gets the availability_zone of this NovaCreateVolumeOption.

        指定要创建卷的AZ，若指定的AZ不存在，则创卷失败，卷状态为error。当前公有云需要指定AZ创建卷。

        :return: The availability_zone of this NovaCreateVolumeOption.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this NovaCreateVolumeOption.

        指定要创建卷的AZ，若指定的AZ不存在，则创卷失败，卷状态为error。当前公有云需要指定AZ创建卷。

        :param availability_zone: The availability_zone of this NovaCreateVolumeOption.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def display_description(self):
        """Gets the display_description of this NovaCreateVolumeOption.

        卷的描述。

        :return: The display_description of this NovaCreateVolumeOption.
        :rtype: str
        """
        return self._display_description

    @display_description.setter
    def display_description(self, display_description):
        """Sets the display_description of this NovaCreateVolumeOption.

        卷的描述。

        :param display_description: The display_description of this NovaCreateVolumeOption.
        :type: str
        """
        self._display_description = display_description

    @property
    def display_name(self):
        """Gets the display_name of this NovaCreateVolumeOption.

        卷名称。

        :return: The display_name of this NovaCreateVolumeOption.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this NovaCreateVolumeOption.

        卷名称。

        :param display_name: The display_name of this NovaCreateVolumeOption.
        :type: str
        """
        self._display_name = display_name

    @property
    def metadata(self):
        """Gets the metadata of this NovaCreateVolumeOption.

        卷的metadata数据。

        :return: The metadata of this NovaCreateVolumeOption.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NovaCreateVolumeOption.

        卷的metadata数据。

        :param metadata: The metadata of this NovaCreateVolumeOption.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def size(self):
        """Gets the size of this NovaCreateVolumeOption.

          卷大小。  单位为GB。

        :return: The size of this NovaCreateVolumeOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this NovaCreateVolumeOption.

          卷大小。  单位为GB。

        :param size: The size of this NovaCreateVolumeOption.
        :type: int
        """
        self._size = size

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this NovaCreateVolumeOption.

        快照ID，指定该参数表示创卷方式为从快照创建卷。

        :return: The snapshot_id of this NovaCreateVolumeOption.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this NovaCreateVolumeOption.

        快照ID，指定该参数表示创卷方式为从快照创建卷。

        :param snapshot_id: The snapshot_id of this NovaCreateVolumeOption.
        :type: str
        """
        self._snapshot_id = snapshot_id

    @property
    def volume_type(self):
        """Gets the volume_type of this NovaCreateVolumeOption.

        卷类型。

        :return: The volume_type of this NovaCreateVolumeOption.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this NovaCreateVolumeOption.

        卷类型。

        :param volume_type: The volume_type of this NovaCreateVolumeOption.
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
        if not isinstance(other, NovaCreateVolumeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
