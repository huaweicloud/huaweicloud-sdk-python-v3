# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditingOutputFileInfo:

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
        'format': 'str',
        'size': 'int',
        'size_byte': 'int',
        'video_info': 'EditingVideoInfo',
        'audio_info': 'list[EditingAudioInfo]'
    }

    attribute_map = {
        'duration': 'duration',
        'format': 'format',
        'size': 'size',
        'size_byte': 'size_byte',
        'video_info': 'video_info',
        'audio_info': 'audio_info'
    }

    def __init__(self, duration=None, format=None, size=None, size_byte=None, video_info=None, audio_info=None):
        """EditingOutputFileInfo

        The model defined in huaweicloud sdk

        :param duration: 输出片源时长 单位秒 
        :type duration: int
        :param format: 输出封装格式 
        :type format: str
        :param size: 媒体文件大小，单位：KByte。 
        :type size: int
        :param size_byte: 媒体文件大小，单位：Byte。 
        :type size_byte: int
        :param video_info: 
        :type video_info: :class:`huaweicloudsdkmpc.v1.EditingVideoInfo`
        :param audio_info: 音频信息
        :type audio_info: list[:class:`huaweicloudsdkmpc.v1.EditingAudioInfo`]
        """
        
        

        self._duration = None
        self._format = None
        self._size = None
        self._size_byte = None
        self._video_info = None
        self._audio_info = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if format is not None:
            self.format = format
        if size is not None:
            self.size = size
        if size_byte is not None:
            self.size_byte = size_byte
        if video_info is not None:
            self.video_info = video_info
        if audio_info is not None:
            self.audio_info = audio_info

    @property
    def duration(self):
        """Gets the duration of this EditingOutputFileInfo.

        输出片源时长 单位秒 

        :return: The duration of this EditingOutputFileInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this EditingOutputFileInfo.

        输出片源时长 单位秒 

        :param duration: The duration of this EditingOutputFileInfo.
        :type duration: int
        """
        self._duration = duration

    @property
    def format(self):
        """Gets the format of this EditingOutputFileInfo.

        输出封装格式 

        :return: The format of this EditingOutputFileInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this EditingOutputFileInfo.

        输出封装格式 

        :param format: The format of this EditingOutputFileInfo.
        :type format: str
        """
        self._format = format

    @property
    def size(self):
        """Gets the size of this EditingOutputFileInfo.

        媒体文件大小，单位：KByte。 

        :return: The size of this EditingOutputFileInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this EditingOutputFileInfo.

        媒体文件大小，单位：KByte。 

        :param size: The size of this EditingOutputFileInfo.
        :type size: int
        """
        self._size = size

    @property
    def size_byte(self):
        """Gets the size_byte of this EditingOutputFileInfo.

        媒体文件大小，单位：Byte。 

        :return: The size_byte of this EditingOutputFileInfo.
        :rtype: int
        """
        return self._size_byte

    @size_byte.setter
    def size_byte(self, size_byte):
        """Sets the size_byte of this EditingOutputFileInfo.

        媒体文件大小，单位：Byte。 

        :param size_byte: The size_byte of this EditingOutputFileInfo.
        :type size_byte: int
        """
        self._size_byte = size_byte

    @property
    def video_info(self):
        """Gets the video_info of this EditingOutputFileInfo.

        :return: The video_info of this EditingOutputFileInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.EditingVideoInfo`
        """
        return self._video_info

    @video_info.setter
    def video_info(self, video_info):
        """Sets the video_info of this EditingOutputFileInfo.

        :param video_info: The video_info of this EditingOutputFileInfo.
        :type video_info: :class:`huaweicloudsdkmpc.v1.EditingVideoInfo`
        """
        self._video_info = video_info

    @property
    def audio_info(self):
        """Gets the audio_info of this EditingOutputFileInfo.

        音频信息

        :return: The audio_info of this EditingOutputFileInfo.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.EditingAudioInfo`]
        """
        return self._audio_info

    @audio_info.setter
    def audio_info(self, audio_info):
        """Sets the audio_info of this EditingOutputFileInfo.

        音频信息

        :param audio_info: The audio_info of this EditingOutputFileInfo.
        :type audio_info: list[:class:`huaweicloudsdkmpc.v1.EditingAudioInfo`]
        """
        self._audio_info = audio_info

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
        if not isinstance(other, EditingOutputFileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
