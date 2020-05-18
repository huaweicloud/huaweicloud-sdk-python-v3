# coding: utf-8

import pprint
import re

import six


class NovaVolumeAttachment(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'device': 'str',
        'id': 'str',
        'server_id': 'str',
        'volume_id': 'str'
    }

    attribute_map = {
        'device': 'device',
        'id': 'id',
        'server_id': 'serverId',
        'volume_id': 'volumeId'
    }

    def __init__(self, device=None, id=None, server_id=None, volume_id=None):  # noqa: E501
        """NovaVolumeAttachment - a model defined in huaweicloud sdk"""

        self._device = None
        self._id = None
        self._server_id = None
        self._volume_id = None
        self.discriminator = None

        self.device = device
        if id is not None:
            self.id = id
        self.server_id = server_id
        self.volume_id = volume_id

    @property
    def device(self):
        """Gets the device of this NovaVolumeAttachment.

        挂载目录。

        :return: The device of this NovaVolumeAttachment.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this NovaVolumeAttachment.

        挂载目录。

        :param device: The device of this NovaVolumeAttachment.
        :type: str
        """
        self._device = device

    @property
    def id(self):
        """Gets the id of this NovaVolumeAttachment.

        挂载资源ID。

        :return: The id of this NovaVolumeAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaVolumeAttachment.

        挂载资源ID。

        :param id: The id of this NovaVolumeAttachment.
        :type: str
        """
        self._id = id

    @property
    def server_id(self):
        """Gets the server_id of this NovaVolumeAttachment.

        所属云服务器ID。

        :return: The server_id of this NovaVolumeAttachment.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this NovaVolumeAttachment.

        所属云服务器ID。

        :param server_id: The server_id of this NovaVolumeAttachment.
        :type: str
        """
        self._server_id = server_id

    @property
    def volume_id(self):
        """Gets the volume_id of this NovaVolumeAttachment.

        挂载云磁盘ID。

        :return: The volume_id of this NovaVolumeAttachment.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this NovaVolumeAttachment.

        挂载云磁盘ID。

        :param volume_id: The volume_id of this NovaVolumeAttachment.
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
        if not isinstance(other, NovaVolumeAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
