# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerVolumeAttachment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

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

    def __init__(self, device=None, id=None, server_id=None, volume_id=None):
        r"""ServerVolumeAttachment

        The model defined in huaweicloud sdk

        :param device: 云硬盘挂载盘符，即磁盘挂载点。
        :type device: str
        :param id: 挂载ID，与云硬盘ID相同，UUID格式。
        :type id: str
        :param server_id: 弹性云服务器ID，UUID格式。
        :type server_id: str
        :param volume_id: 云硬盘ID，UUID格式。
        :type volume_id: str
        """
        
        

        self._device = None
        self._id = None
        self._server_id = None
        self._volume_id = None
        self.discriminator = None

        if device is not None:
            self.device = device
        if id is not None:
            self.id = id
        if server_id is not None:
            self.server_id = server_id
        if volume_id is not None:
            self.volume_id = volume_id

    @property
    def device(self):
        r"""Gets the device of this ServerVolumeAttachment.

        云硬盘挂载盘符，即磁盘挂载点。

        :return: The device of this ServerVolumeAttachment.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        r"""Sets the device of this ServerVolumeAttachment.

        云硬盘挂载盘符，即磁盘挂载点。

        :param device: The device of this ServerVolumeAttachment.
        :type device: str
        """
        self._device = device

    @property
    def id(self):
        r"""Gets the id of this ServerVolumeAttachment.

        挂载ID，与云硬盘ID相同，UUID格式。

        :return: The id of this ServerVolumeAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServerVolumeAttachment.

        挂载ID，与云硬盘ID相同，UUID格式。

        :param id: The id of this ServerVolumeAttachment.
        :type id: str
        """
        self._id = id

    @property
    def server_id(self):
        r"""Gets the server_id of this ServerVolumeAttachment.

        弹性云服务器ID，UUID格式。

        :return: The server_id of this ServerVolumeAttachment.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ServerVolumeAttachment.

        弹性云服务器ID，UUID格式。

        :param server_id: The server_id of this ServerVolumeAttachment.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def volume_id(self):
        r"""Gets the volume_id of this ServerVolumeAttachment.

        云硬盘ID，UUID格式。

        :return: The volume_id of this ServerVolumeAttachment.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this ServerVolumeAttachment.

        云硬盘ID，UUID格式。

        :param volume_id: The volume_id of this ServerVolumeAttachment.
        :type volume_id: str
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
        if not isinstance(other, ServerVolumeAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
