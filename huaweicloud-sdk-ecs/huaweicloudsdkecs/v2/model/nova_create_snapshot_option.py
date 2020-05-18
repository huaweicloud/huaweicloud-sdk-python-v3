# coding: utf-8

import pprint
import re

import six


class NovaCreateSnapshotOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'display_description': 'str',
        'display_name': 'str',
        'force': 'bool',
        'volume_id': 'str'
    }

    attribute_map = {
        'display_description': 'display_description',
        'display_name': 'display_name',
        'force': 'force',
        'volume_id': 'volume_id'
    }

    def __init__(self, display_description=None, display_name=None, force=None, volume_id=None):  # noqa: E501
        """NovaCreateSnapshotOption - a model defined in huaweicloud sdk"""

        self._display_description = None
        self._display_name = None
        self._force = None
        self._volume_id = None
        self.discriminator = None

        if display_description is not None:
            self.display_description = display_description
        if display_name is not None:
            self.display_name = display_name
        if force is not None:
            self.force = force
        self.volume_id = volume_id

    @property
    def display_description(self):
        """Gets the display_description of this NovaCreateSnapshotOption.

        快照的描述。

        :return: The display_description of this NovaCreateSnapshotOption.
        :rtype: str
        """
        return self._display_description

    @display_description.setter
    def display_description(self, display_description):
        """Sets the display_description of this NovaCreateSnapshotOption.

        快照的描述。

        :param display_description: The display_description of this NovaCreateSnapshotOption.
        :type: str
        """
        self._display_description = display_description

    @property
    def display_name(self):
        """Gets the display_name of this NovaCreateSnapshotOption.

        云硬盘快照名称。  最大支持255个字节。   > 说明：  - 通过VBS对云硬盘创建备份时，同时会创建以autobk_snapshot_为名称前缀的快照，云硬盘控制台对此类快照会有操作限制。因此，建议您不要创建以autobk_snapshot_为名称前缀的快照，避免影响快照的正常使用。

        :return: The display_name of this NovaCreateSnapshotOption.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this NovaCreateSnapshotOption.

        云硬盘快照名称。  最大支持255个字节。   > 说明：  - 通过VBS对云硬盘创建备份时，同时会创建以autobk_snapshot_为名称前缀的快照，云硬盘控制台对此类快照会有操作限制。因此，建议您不要创建以autobk_snapshot_为名称前缀的快照，避免影响快照的正常使用。

        :param display_name: The display_name of this NovaCreateSnapshotOption.
        :type: str
        """
        self._display_name = display_name

    @property
    def force(self):
        """Gets the force of this NovaCreateSnapshotOption.

        是否执行强制创建。force为true时，支持卷在in-use状态时创建快照。

        :return: The force of this NovaCreateSnapshotOption.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this NovaCreateSnapshotOption.

        是否执行强制创建。force为true时，支持卷在in-use状态时创建快照。

        :param force: The force of this NovaCreateSnapshotOption.
        :type: bool
        """
        self._force = force

    @property
    def volume_id(self):
        """Gets the volume_id of this NovaCreateSnapshotOption.

        卷ID。

        :return: The volume_id of this NovaCreateSnapshotOption.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this NovaCreateSnapshotOption.

        卷ID。

        :param volume_id: The volume_id of this NovaCreateSnapshotOption.
        :type: str
        """
        self._volume_id = volume_id

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
        if not isinstance(other, NovaCreateSnapshotOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
