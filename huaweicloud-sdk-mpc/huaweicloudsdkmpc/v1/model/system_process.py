# coding: utf-8

import pprint
import re

import six





class SystemProcess:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'append_type': 'str',
        'hls_index': 'ObsObjInfo',
        'dash_index': 'ObsObjInfo'
    }

    attribute_map = {
        'append_type': 'append_type',
        'hls_index': 'hls_index',
        'dash_index': 'dash_index'
    }

    def __init__(self, append_type=None, hls_index=None, dash_index=None):
        """SystemProcess - a model defined in huaweicloud sdk"""
        
        

        self._append_type = None
        self._hls_index = None
        self._dash_index = None
        self.discriminator = None

        if append_type is not None:
            self.append_type = append_type
        if hls_index is not None:
            self.hls_index = hls_index
        if dash_index is not None:
            self.dash_index = dash_index

    @property
    def append_type(self):
        """Gets the append_type of this SystemProcess.

        追加转码类型。  取值如下： - SUBTITLE：追加字幕 - AUDIO：追加音频 - VIDEO：追加视频（原有追加新分辨率视频） 

        :return: The append_type of this SystemProcess.
        :rtype: str
        """
        return self._append_type

    @append_type.setter
    def append_type(self, append_type):
        """Sets the append_type of this SystemProcess.

        追加转码类型。  取值如下： - SUBTITLE：追加字幕 - AUDIO：追加音频 - VIDEO：追加视频（原有追加新分辨率视频） 

        :param append_type: The append_type of this SystemProcess.
        :type: str
        """
        self._append_type = append_type

    @property
    def hls_index(self):
        """Gets the hls_index of this SystemProcess.


        :return: The hls_index of this SystemProcess.
        :rtype: ObsObjInfo
        """
        return self._hls_index

    @hls_index.setter
    def hls_index(self, hls_index):
        """Sets the hls_index of this SystemProcess.


        :param hls_index: The hls_index of this SystemProcess.
        :type: ObsObjInfo
        """
        self._hls_index = hls_index

    @property
    def dash_index(self):
        """Gets the dash_index of this SystemProcess.


        :return: The dash_index of this SystemProcess.
        :rtype: ObsObjInfo
        """
        return self._dash_index

    @dash_index.setter
    def dash_index(self, dash_index):
        """Sets the dash_index of this SystemProcess.


        :param dash_index: The dash_index of this SystemProcess.
        :type: ObsObjInfo
        """
        self._dash_index = dash_index

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
        if not isinstance(other, SystemProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
