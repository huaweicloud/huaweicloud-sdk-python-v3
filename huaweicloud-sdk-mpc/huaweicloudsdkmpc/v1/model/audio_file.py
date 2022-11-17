# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioFile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tracks_info': 'list[TracksInfo]',
        'input': 'ObsObjInfo'
    }

    attribute_map = {
        'tracks_info': 'tracks_info',
        'input': 'input'
    }

    def __init__(self, tracks_info=None, input=None):
        """AudioFile

        The model defined in huaweicloud sdk

        :param tracks_info: 音轨信息
        :type tracks_info: list[:class:`huaweicloudsdkmpc.v1.TracksInfo`]
        :param input: 
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        
        

        self._tracks_info = None
        self._input = None
        self.discriminator = None

        if tracks_info is not None:
            self.tracks_info = tracks_info
        if input is not None:
            self.input = input

    @property
    def tracks_info(self):
        """Gets the tracks_info of this AudioFile.

        音轨信息

        :return: The tracks_info of this AudioFile.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.TracksInfo`]
        """
        return self._tracks_info

    @tracks_info.setter
    def tracks_info(self, tracks_info):
        """Sets the tracks_info of this AudioFile.

        音轨信息

        :param tracks_info: The tracks_info of this AudioFile.
        :type tracks_info: list[:class:`huaweicloudsdkmpc.v1.TracksInfo`]
        """
        self._tracks_info = tracks_info

    @property
    def input(self):
        """Gets the input of this AudioFile.

        :return: The input of this AudioFile.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this AudioFile.

        :param input: The input of this AudioFile.
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

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
        if not isinstance(other, AudioFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
