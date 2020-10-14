# coding: utf-8

import pprint
import re

import six





class MetaData:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'duration_ms': 'float',
        'duration': 'int',
        'format': 'str',
        'bitrate': 'int',
        'video': 'list[VideoInfo]',
        'audio': 'list[AudioInfo]'
    }

    attribute_map = {
        'size': 'size',
        'duration_ms': 'duration_ms',
        'duration': 'duration',
        'format': 'format',
        'bitrate': 'bitrate',
        'video': 'video',
        'audio': 'audio'
    }

    def __init__(self, size=None, duration_ms=None, duration=None, format=None, bitrate=None, video=None, audio=None):
        """MetaData - a model defined in huaweicloud sdk"""
        
        

        self._size = None
        self._duration_ms = None
        self._duration = None
        self._format = None
        self._bitrate = None
        self._video = None
        self._audio = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if duration_ms is not None:
            self.duration_ms = duration_ms
        if duration is not None:
            self.duration = duration
        if format is not None:
            self.format = format
        if bitrate is not None:
            self.bitrate = bitrate
        if video is not None:
            self.video = video
        if audio is not None:
            self.audio = audio

    @property
    def size(self):
        """Gets the size of this MetaData.

        文件大小。 

        :return: The size of this MetaData.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MetaData.

        文件大小。 

        :param size: The size of this MetaData.
        :type: int
        """
        self._size = size

    @property
    def duration_ms(self):
        """Gets the duration_ms of this MetaData.

        视频时长，带小数位显示。单位：秒。 

        :return: The duration_ms of this MetaData.
        :rtype: float
        """
        return self._duration_ms

    @duration_ms.setter
    def duration_ms(self, duration_ms):
        """Sets the duration_ms of this MetaData.

        视频时长，带小数位显示。单位：秒。 

        :param duration_ms: The duration_ms of this MetaData.
        :type: float
        """
        self._duration_ms = duration_ms

    @property
    def duration(self):
        """Gets the duration of this MetaData.

        视频时长。单位：秒。 

        :return: The duration of this MetaData.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this MetaData.

        视频时长。单位：秒。 

        :param duration: The duration of this MetaData.
        :type: int
        """
        self._duration = duration

    @property
    def format(self):
        """Gets the format of this MetaData.

        文件封装格式。 

        :return: The format of this MetaData.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this MetaData.

        文件封装格式。 

        :param format: The format of this MetaData.
        :type: str
        """
        self._format = format

    @property
    def bitrate(self):
        """Gets the bitrate of this MetaData.

        总码率。 

        :return: The bitrate of this MetaData.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this MetaData.

        总码率。 

        :param bitrate: The bitrate of this MetaData.
        :type: int
        """
        self._bitrate = bitrate

    @property
    def video(self):
        """Gets the video of this MetaData.

        视频流元数据。 

        :return: The video of this MetaData.
        :rtype: list[VideoInfo]
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this MetaData.

        视频流元数据。 

        :param video: The video of this MetaData.
        :type: list[VideoInfo]
        """
        self._video = video

    @property
    def audio(self):
        """Gets the audio of this MetaData.

        音频流元数据。 

        :return: The audio of this MetaData.
        :rtype: list[AudioInfo]
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this MetaData.

        音频流元数据。 

        :param audio: The audio of this MetaData.
        :type: list[AudioInfo]
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
        if not isinstance(other, MetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
