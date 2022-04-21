# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeAttachments:

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
        'server_id': 'str',
        'volume_id': 'str',
        'device': 'str'
    }

    attribute_map = {
        'id': 'id',
        'server_id': 'serverId',
        'volume_id': 'volumeId',
        'device': 'device'
    }

    def __init__(self, id=None, server_id=None, volume_id=None, device=None):
        """VolumeAttachments

        The model defined in huaweicloud sdk

        :param id: 挂载资源ID
        :type id: str
        :param server_id: 所属裸金属服务器ID
        :type server_id: str
        :param volume_id: 挂载云磁盘ID
        :type volume_id: str
        :param device: 挂载目录，例如“/dev/sdd”。
        :type device: str
        """
        
        

        self._id = None
        self._server_id = None
        self._volume_id = None
        self._device = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if server_id is not None:
            self.server_id = server_id
        if volume_id is not None:
            self.volume_id = volume_id
        if device is not None:
            self.device = device

    @property
    def id(self):
        """Gets the id of this VolumeAttachments.

        挂载资源ID

        :return: The id of this VolumeAttachments.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeAttachments.

        挂载资源ID

        :param id: The id of this VolumeAttachments.
        :type id: str
        """
        self._id = id

    @property
    def server_id(self):
        """Gets the server_id of this VolumeAttachments.

        所属裸金属服务器ID

        :return: The server_id of this VolumeAttachments.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this VolumeAttachments.

        所属裸金属服务器ID

        :param server_id: The server_id of this VolumeAttachments.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def volume_id(self):
        """Gets the volume_id of this VolumeAttachments.

        挂载云磁盘ID

        :return: The volume_id of this VolumeAttachments.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this VolumeAttachments.

        挂载云磁盘ID

        :param volume_id: The volume_id of this VolumeAttachments.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def device(self):
        """Gets the device of this VolumeAttachments.

        挂载目录，例如“/dev/sdd”。

        :return: The device of this VolumeAttachments.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this VolumeAttachments.

        挂载目录，例如“/dev/sdd”。

        :param device: The device of this VolumeAttachments.
        :type device: str
        """
        self._device = device

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
        if not isinstance(other, VolumeAttachments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
