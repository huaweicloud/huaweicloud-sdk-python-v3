# coding: utf-8

import pprint
import re

import six





class CreateVolumeRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bss_param': 'BssParamForCreateVolume',
        'volume': 'CreateVolumeOption',
        'server_id': 'str'
    }

    attribute_map = {
        'bss_param': 'bssParam',
        'volume': 'volume',
        'server_id': 'server_id'
    }

    def __init__(self, bss_param=None, volume=None, server_id=None):
        """CreateVolumeRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._bss_param = None
        self._volume = None
        self._server_id = None
        self.discriminator = None

        if bss_param is not None:
            self.bss_param = bss_param
        self.volume = volume
        if server_id is not None:
            self.server_id = server_id

    @property
    def bss_param(self):
        """Gets the bss_param of this CreateVolumeRequestBody.


        :return: The bss_param of this CreateVolumeRequestBody.
        :rtype: BssParamForCreateVolume
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        """Sets the bss_param of this CreateVolumeRequestBody.


        :param bss_param: The bss_param of this CreateVolumeRequestBody.
        :type: BssParamForCreateVolume
        """
        self._bss_param = bss_param

    @property
    def volume(self):
        """Gets the volume of this CreateVolumeRequestBody.


        :return: The volume of this CreateVolumeRequestBody.
        :rtype: CreateVolumeOption
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this CreateVolumeRequestBody.


        :param volume: The volume of this CreateVolumeRequestBody.
        :type: CreateVolumeOption
        """
        self._volume = volume

    @property
    def server_id(self):
        """Gets the server_id of this CreateVolumeRequestBody.

        创建云硬盘并挂载到目标虚拟机。

        :return: The server_id of this CreateVolumeRequestBody.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this CreateVolumeRequestBody.

        创建云硬盘并挂载到目标虚拟机。

        :param server_id: The server_id of this CreateVolumeRequestBody.
        :type: str
        """
        self._server_id = server_id

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
        if not isinstance(other, CreateVolumeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
