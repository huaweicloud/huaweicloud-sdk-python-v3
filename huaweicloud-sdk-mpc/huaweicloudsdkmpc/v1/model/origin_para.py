# coding: utf-8

import pprint
import re

import six





class OriginPara:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'duration': 'int',
        'duration_ms': 'int',
        'file_format': 'str',
        'video': 'VideoInfo',
        'audio': 'AudioInfo'
    }

    attribute_map = {
        'duration': 'duration',
        'duration_ms': 'duration_ms',
        'file_format': 'file_format',
        'video': 'video',
        'audio': 'audio'
    }

    def __init__(self, duration=None, duration_ms=None, file_format=None, video=None, audio=None):
        """OriginPara - a model defined in huaweicloud sdk"""
        
        

        self._duration = None
        self._duration_ms = None
        self._file_format = None
        self._video = None
        self._audio = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if duration_ms is not None:
            self.duration_ms = duration_ms
        if file_format is not None:
            self.file_format = file_format
        if video is not None:
            self.video = video
        if audio is not None:
            self.audio = audio

    @property
    def duration(self):
        """Gets the duration of this OriginPara.

        片源时长，单位：秒

        :return: The duration of this OriginPara.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this OriginPara.

        片源时长，单位：秒

        :param duration: The duration of this OriginPara.
        :type: int
        """
        self._duration = duration

    @property
    def duration_ms(self):
        """Gets the duration_ms of this OriginPara.

        片源时长，单位：毫秒

        :return: The duration_ms of this OriginPara.
        :rtype: int
        """
        return self._duration_ms

    @duration_ms.setter
    def duration_ms(self, duration_ms):
        """Sets the duration_ms of this OriginPara.

        片源时长，单位：毫秒

        :param duration_ms: The duration_ms of this OriginPara.
        :type: int
        """
        self._duration_ms = duration_ms

    @property
    def file_format(self):
        """Gets the file_format of this OriginPara.

        文件格式 

        :return: The file_format of this OriginPara.
        :rtype: str
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """Sets the file_format of this OriginPara.

        文件格式 

        :param file_format: The file_format of this OriginPara.
        :type: str
        """
        self._file_format = file_format

    @property
    def video(self):
        """Gets the video of this OriginPara.


        :return: The video of this OriginPara.
        :rtype: VideoInfo
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this OriginPara.


        :param video: The video of this OriginPara.
        :type: VideoInfo
        """
        self._video = video

    @property
    def audio(self):
        """Gets the audio of this OriginPara.


        :return: The audio of this OriginPara.
        :rtype: AudioInfo
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this OriginPara.


        :param audio: The audio of this OriginPara.
        :type: AudioInfo
        """
        self._audio = audio

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
        if not isinstance(other, OriginPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
