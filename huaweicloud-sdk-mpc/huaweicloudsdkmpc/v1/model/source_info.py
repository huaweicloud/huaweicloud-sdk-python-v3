# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceInfo:

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
        'format': 'str',
        'size': 'int',
        'manifest_name': 'str',
        'video_info': 'VideoInfo',
        'audio_info': 'list[AudioInfo]'
    }

    attribute_map = {
        'duration': 'duration',
        'duration_ms': 'duration_ms',
        'format': 'format',
        'size': 'size',
        'manifest_name': 'manifest_name',
        'video_info': 'video_info',
        'audio_info': 'audio_info'
    }

    def __init__(self, duration=None, duration_ms=None, format=None, size=None, manifest_name=None, video_info=None, audio_info=None):
        r"""SourceInfo

        The model defined in huaweicloud sdk

        :param duration: 片源时长，单位：秒
        :type duration: int
        :param duration_ms: 片源时长，单位：毫秒
        :type duration_ms: int
        :param format: 片源格式
        :type format: str
        :param size: 片源大小
        :type size: int
        :param manifest_name: 独立mpd索引文件名 
        :type manifest_name: str
        :param video_info: 
        :type video_info: :class:`huaweicloudsdkmpc.v1.VideoInfo`
        :param audio_info: 音频信息
        :type audio_info: list[:class:`huaweicloudsdkmpc.v1.AudioInfo`]
        """
        
        

        self._duration = None
        self._duration_ms = None
        self._format = None
        self._size = None
        self._manifest_name = None
        self._video_info = None
        self._audio_info = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if duration_ms is not None:
            self.duration_ms = duration_ms
        if format is not None:
            self.format = format
        if size is not None:
            self.size = size
        if manifest_name is not None:
            self.manifest_name = manifest_name
        if video_info is not None:
            self.video_info = video_info
        if audio_info is not None:
            self.audio_info = audio_info

    @property
    def duration(self):
        r"""Gets the duration of this SourceInfo.

        片源时长，单位：秒

        :return: The duration of this SourceInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this SourceInfo.

        片源时长，单位：秒

        :param duration: The duration of this SourceInfo.
        :type duration: int
        """
        self._duration = duration

    @property
    def duration_ms(self):
        r"""Gets the duration_ms of this SourceInfo.

        片源时长，单位：毫秒

        :return: The duration_ms of this SourceInfo.
        :rtype: int
        """
        return self._duration_ms

    @duration_ms.setter
    def duration_ms(self, duration_ms):
        r"""Sets the duration_ms of this SourceInfo.

        片源时长，单位：毫秒

        :param duration_ms: The duration_ms of this SourceInfo.
        :type duration_ms: int
        """
        self._duration_ms = duration_ms

    @property
    def format(self):
        r"""Gets the format of this SourceInfo.

        片源格式

        :return: The format of this SourceInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this SourceInfo.

        片源格式

        :param format: The format of this SourceInfo.
        :type format: str
        """
        self._format = format

    @property
    def size(self):
        r"""Gets the size of this SourceInfo.

        片源大小

        :return: The size of this SourceInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this SourceInfo.

        片源大小

        :param size: The size of this SourceInfo.
        :type size: int
        """
        self._size = size

    @property
    def manifest_name(self):
        r"""Gets the manifest_name of this SourceInfo.

        独立mpd索引文件名 

        :return: The manifest_name of this SourceInfo.
        :rtype: str
        """
        return self._manifest_name

    @manifest_name.setter
    def manifest_name(self, manifest_name):
        r"""Sets the manifest_name of this SourceInfo.

        独立mpd索引文件名 

        :param manifest_name: The manifest_name of this SourceInfo.
        :type manifest_name: str
        """
        self._manifest_name = manifest_name

    @property
    def video_info(self):
        r"""Gets the video_info of this SourceInfo.

        :return: The video_info of this SourceInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.VideoInfo`
        """
        return self._video_info

    @video_info.setter
    def video_info(self, video_info):
        r"""Sets the video_info of this SourceInfo.

        :param video_info: The video_info of this SourceInfo.
        :type video_info: :class:`huaweicloudsdkmpc.v1.VideoInfo`
        """
        self._video_info = video_info

    @property
    def audio_info(self):
        r"""Gets the audio_info of this SourceInfo.

        音频信息

        :return: The audio_info of this SourceInfo.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.AudioInfo`]
        """
        return self._audio_info

    @audio_info.setter
    def audio_info(self, audio_info):
        r"""Sets the audio_info of this SourceInfo.

        音频信息

        :param audio_info: The audio_info of this SourceInfo.
        :type audio_info: list[:class:`huaweicloudsdkmpc.v1.AudioInfo`]
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
        if not isinstance(other, SourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
