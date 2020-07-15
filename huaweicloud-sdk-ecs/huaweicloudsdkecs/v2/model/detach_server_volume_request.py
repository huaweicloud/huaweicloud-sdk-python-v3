# coding: utf-8

import pprint
import re

import six





class DetachServerVolumeRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'volume_id': 'str',
        'delete_flag': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'volume_id': 'volume_id',
        'delete_flag': 'delete_flag'
    }

    def __init__(self, server_id=None, volume_id=None, delete_flag='0'):
        """DetachServerVolumeRequest - a model defined in huaweicloud sdk"""
        
        

        self._server_id = None
        self._volume_id = None
        self._delete_flag = None
        self.discriminator = None

        self.server_id = server_id
        self.volume_id = volume_id
        if delete_flag is not None:
            self.delete_flag = delete_flag

    @property
    def server_id(self):
        """Gets the server_id of this DetachServerVolumeRequest.


        :return: The server_id of this DetachServerVolumeRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this DetachServerVolumeRequest.


        :param server_id: The server_id of this DetachServerVolumeRequest.
        :type: str
        """
        self._server_id = server_id

    @property
    def volume_id(self):
        """Gets the volume_id of this DetachServerVolumeRequest.


        :return: The volume_id of this DetachServerVolumeRequest.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this DetachServerVolumeRequest.


        :param volume_id: The volume_id of this DetachServerVolumeRequest.
        :type: str
        """
        self._volume_id = volume_id

    @property
    def delete_flag(self):
        """Gets the delete_flag of this DetachServerVolumeRequest.


        :return: The delete_flag of this DetachServerVolumeRequest.
        :rtype: str
        """
        return self._delete_flag

    @delete_flag.setter
    def delete_flag(self, delete_flag):
        """Sets the delete_flag of this DetachServerVolumeRequest.


        :param delete_flag: The delete_flag of this DetachServerVolumeRequest.
        :type: str
        """
        self._delete_flag = delete_flag

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
        if not isinstance(other, DetachServerVolumeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
