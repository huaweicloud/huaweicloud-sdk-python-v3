# coding: utf-8

import pprint
import re

import six


class NovaSnapshot(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'created_at': 'datetime',
        'display_description': 'str',
        'display_name': 'str',
        'id': 'str',
        'size': 'int',
        'status': 'str',
        'volume_id': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'display_description': 'displayDescription',
        'display_name': 'displayName',
        'id': 'id',
        'size': 'size',
        'status': 'status',
        'volume_id': 'volumeId'
    }

    def __init__(self, created_at=None, display_description=None, display_name=None, id=None, size=None, status=None, volume_id=None):  # noqa: E501
        """NovaSnapshot - a model defined in huaweicloud sdk"""

        self._created_at = None
        self._display_description = None
        self._display_name = None
        self._id = None
        self._size = None
        self._status = None
        self._volume_id = None
        self.discriminator = None

        self.created_at = created_at
        if display_description is not None:
            self.display_description = display_description
        if display_name is not None:
            self.display_name = display_name
        self.id = id
        self.size = size
        self.status = status
        self.volume_id = volume_id

    @property
    def created_at(self):
        """Gets the created_at of this NovaSnapshot.

        卷快照创建时间。

        :return: The created_at of this NovaSnapshot.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NovaSnapshot.

        卷快照创建时间。

        :param created_at: The created_at of this NovaSnapshot.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def display_description(self):
        """Gets the display_description of this NovaSnapshot.

        卷快照描述信息。

        :return: The display_description of this NovaSnapshot.
        :rtype: str
        """
        return self._display_description

    @display_description.setter
    def display_description(self, display_description):
        """Sets the display_description of this NovaSnapshot.

        卷快照描述信息。

        :param display_description: The display_description of this NovaSnapshot.
        :type: str
        """
        self._display_description = display_description

    @property
    def display_name(self):
        """Gets the display_name of this NovaSnapshot.

        卷快照名称。

        :return: The display_name of this NovaSnapshot.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this NovaSnapshot.

        卷快照名称。

        :param display_name: The display_name of this NovaSnapshot.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this NovaSnapshot.

        卷快照ID，UUID格式。

        :return: The id of this NovaSnapshot.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaSnapshot.

        卷快照ID，UUID格式。

        :param id: The id of this NovaSnapshot.
        :type: str
        """
        self._id = id

    @property
    def size(self):
        """Gets the size of this NovaSnapshot.

        卷快照大小。

        :return: The size of this NovaSnapshot.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this NovaSnapshot.

        卷快照大小。

        :param size: The size of this NovaSnapshot.
        :type: int
        """
        self._size = size

    @property
    def status(self):
        """Gets the status of this NovaSnapshot.

        卷快照的状态。

        :return: The status of this NovaSnapshot.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NovaSnapshot.

        卷快照的状态。

        :param status: The status of this NovaSnapshot.
        :type: str
        """
        self._status = status

    @property
    def volume_id(self):
        """Gets the volume_id of this NovaSnapshot.

        快照所属的卷。

        :return: The volume_id of this NovaSnapshot.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this NovaSnapshot.

        快照所属的卷。

        :param volume_id: The volume_id of this NovaSnapshot.
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
        if not isinstance(other, NovaSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
