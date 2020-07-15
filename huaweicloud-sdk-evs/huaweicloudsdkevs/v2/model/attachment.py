# coding: utf-8

import pprint
import re

import six





class Attachment:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'attached_at': 'str',
        'attachment_id': 'str',
        'device': 'str',
        'host_name': 'str',
        'id': 'str',
        'server_id': 'str',
        'volume_id': 'str'
    }

    attribute_map = {
        'attached_at': 'attached_at',
        'attachment_id': 'attachment_id',
        'device': 'device',
        'host_name': 'host_name',
        'id': 'id',
        'server_id': 'server_id',
        'volume_id': 'volume_id'
    }

    def __init__(self, attached_at=None, attachment_id=None, device=None, host_name=None, id=None, server_id=None, volume_id=None):
        """Attachment - a model defined in huaweicloud sdk"""
        
        

        self._attached_at = None
        self._attachment_id = None
        self._device = None
        self._host_name = None
        self._id = None
        self._server_id = None
        self._volume_id = None
        self.discriminator = None

        self.attached_at = attached_at
        self.attachment_id = attachment_id
        self.device = device
        self.host_name = host_name
        self.id = id
        self.server_id = server_id
        self.volume_id = volume_id

    @property
    def attached_at(self):
        """Gets the attached_at of this Attachment.

        挂载的时间信息。  时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :return: The attached_at of this Attachment.
        :rtype: str
        """
        return self._attached_at

    @attached_at.setter
    def attached_at(self, attached_at):
        """Sets the attached_at of this Attachment.

        挂载的时间信息。  时间格式：UTC YYYY-MM-DDTHH:MM:SS.XXXXXX

        :param attached_at: The attached_at of this Attachment.
        :type: str
        """
        self._attached_at = attached_at

    @property
    def attachment_id(self):
        """Gets the attachment_id of this Attachment.

        挂载信息对应的ID。

        :return: The attachment_id of this Attachment.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this Attachment.

        挂载信息对应的ID。

        :param attachment_id: The attachment_id of this Attachment.
        :type: str
        """
        self._attachment_id = attachment_id

    @property
    def device(self):
        """Gets the device of this Attachment.

        挂载点。

        :return: The device of this Attachment.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this Attachment.

        挂载点。

        :param device: The device of this Attachment.
        :type: str
        """
        self._device = device

    @property
    def host_name(self):
        """Gets the host_name of this Attachment.

        云硬盘挂载到的云服务器对应的物理主机的名称。

        :return: The host_name of this Attachment.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this Attachment.

        云硬盘挂载到的云服务器对应的物理主机的名称。

        :param host_name: The host_name of this Attachment.
        :type: str
        """
        self._host_name = host_name

    @property
    def id(self):
        """Gets the id of this Attachment.

        挂载的资源ID。

        :return: The id of this Attachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Attachment.

        挂载的资源ID。

        :param id: The id of this Attachment.
        :type: str
        """
        self._id = id

    @property
    def server_id(self):
        """Gets the server_id of this Attachment.

        云硬盘挂载到的云服务器的 ID。

        :return: The server_id of this Attachment.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this Attachment.

        云硬盘挂载到的云服务器的 ID。

        :param server_id: The server_id of this Attachment.
        :type: str
        """
        self._server_id = server_id

    @property
    def volume_id(self):
        """Gets the volume_id of this Attachment.

        云硬盘ID。

        :return: The volume_id of this Attachment.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this Attachment.

        云硬盘ID。

        :param volume_id: The volume_id of this Attachment.
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
        if not isinstance(other, Attachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
