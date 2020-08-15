# coding: utf-8

import pprint
import re

import six





class MultiAudio:


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
        'audio_files': 'list[AudioFile]',
        'default_language': 'str'
    }

    attribute_map = {
        'tracks_info': 'tracks_info',
        'audio_files': 'audio_files',
        'default_language': 'default_language'
    }

    def __init__(self, tracks_info=None, audio_files=None, default_language=None):
        """MultiAudio - a model defined in huaweicloud sdk"""
        
        

        self._tracks_info = None
        self._audio_files = None
        self._default_language = None
        self.discriminator = None

        if tracks_info is not None:
            self.tracks_info = tracks_info
        if audio_files is not None:
            self.audio_files = audio_files
        if default_language is not None:
            self.default_language = default_language

    @property
    def tracks_info(self):
        """Gets the tracks_info of this MultiAudio.

        音轨信息

        :return: The tracks_info of this MultiAudio.
        :rtype: list[TracksInfo]
        """
        return self._tracks_info

    @tracks_info.setter
    def tracks_info(self, tracks_info):
        """Sets the tracks_info of this MultiAudio.

        音轨信息

        :param tracks_info: The tracks_info of this MultiAudio.
        :type: list[TracksInfo]
        """
        self._tracks_info = tracks_info

    @property
    def audio_files(self):
        """Gets the audio_files of this MultiAudio.

        音频文件

        :return: The audio_files of this MultiAudio.
        :rtype: list[AudioFile]
        """
        return self._audio_files

    @audio_files.setter
    def audio_files(self, audio_files):
        """Sets the audio_files of this MultiAudio.

        音频文件

        :param audio_files: The audio_files of this MultiAudio.
        :type: list[AudioFile]
        """
        self._audio_files = audio_files

    @property
    def default_language(self):
        """Gets the default_language of this MultiAudio.

        默认语言

        :return: The default_language of this MultiAudio.
        :rtype: str
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language):
        """Sets the default_language of this MultiAudio.

        默认语言

        :param default_language: The default_language of this MultiAudio.
        :type: str
        """
        self._default_language = default_language

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
        if not isinstance(other, MultiAudio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
