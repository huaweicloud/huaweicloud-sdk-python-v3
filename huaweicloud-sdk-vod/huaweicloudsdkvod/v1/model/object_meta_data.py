# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectMetaData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bitrate': 'int',
        'container': 'str',
        'duration': 'int',
        'video_duration': 'float',
        'audio_duration': 'float',
        'float_duration': 'float',
        'height': 'int',
        'width': 'int',
        'md5': 'str',
        'rotate': 'float',
        'size': 'int',
        'video_stream_list': 'list[MetaVideoInfo]',
        'audio_stream_list': 'list[MetaAudioInfo]'
    }

    attribute_map = {
        'bitrate': 'bitrate',
        'container': 'container',
        'duration': 'duration',
        'video_duration': 'video_duration',
        'audio_duration': 'audio_duration',
        'float_duration': 'float_duration',
        'height': 'height',
        'width': 'width',
        'md5': 'md5',
        'rotate': 'rotate',
        'size': 'size',
        'video_stream_list': 'video_stream_list',
        'audio_stream_list': 'audio_stream_list'
    }

    def __init__(self, bitrate=None, container=None, duration=None, video_duration=None, audio_duration=None, float_duration=None, height=None, width=None, md5=None, rotate=None, size=None, video_stream_list=None, audio_stream_list=None):
        r"""ObjectMetaData

        The model defined in huaweicloud sdk

        :param bitrate: 总码率，单位：bit/秒 
        :type bitrate: int
        :param container: 封装格式 
        :type container: str
        :param duration: 时长，单位：秒 
        :type duration: int
        :param video_duration: 时长，单位：秒 
        :type video_duration: float
        :param audio_duration: 时长，单位：秒 
        :type audio_duration: float
        :param float_duration: 时长，单位：秒 
        :type float_duration: float
        :param height: 视频高度 
        :type height: int
        :param width: 视频宽度 
        :type width: int
        :param md5: 视频md5 
        :type md5: str
        :param rotate: 视频拍摄角度 
        :type rotate: float
        :param size: 文件大小，单位：byte 
        :type size: int
        :param video_stream_list: 视频流元数据 
        :type video_stream_list: list[:class:`huaweicloudsdkvod.v1.MetaVideoInfo`]
        :param audio_stream_list: 音频流元数据 
        :type audio_stream_list: list[:class:`huaweicloudsdkvod.v1.MetaAudioInfo`]
        """
        
        

        self._bitrate = None
        self._container = None
        self._duration = None
        self._video_duration = None
        self._audio_duration = None
        self._float_duration = None
        self._height = None
        self._width = None
        self._md5 = None
        self._rotate = None
        self._size = None
        self._video_stream_list = None
        self._audio_stream_list = None
        self.discriminator = None

        if bitrate is not None:
            self.bitrate = bitrate
        if container is not None:
            self.container = container
        if duration is not None:
            self.duration = duration
        if video_duration is not None:
            self.video_duration = video_duration
        if audio_duration is not None:
            self.audio_duration = audio_duration
        if float_duration is not None:
            self.float_duration = float_duration
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if md5 is not None:
            self.md5 = md5
        if rotate is not None:
            self.rotate = rotate
        if size is not None:
            self.size = size
        if video_stream_list is not None:
            self.video_stream_list = video_stream_list
        if audio_stream_list is not None:
            self.audio_stream_list = audio_stream_list

    @property
    def bitrate(self):
        r"""Gets the bitrate of this ObjectMetaData.

        总码率，单位：bit/秒 

        :return: The bitrate of this ObjectMetaData.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        r"""Sets the bitrate of this ObjectMetaData.

        总码率，单位：bit/秒 

        :param bitrate: The bitrate of this ObjectMetaData.
        :type bitrate: int
        """
        self._bitrate = bitrate

    @property
    def container(self):
        r"""Gets the container of this ObjectMetaData.

        封装格式 

        :return: The container of this ObjectMetaData.
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        r"""Sets the container of this ObjectMetaData.

        封装格式 

        :param container: The container of this ObjectMetaData.
        :type container: str
        """
        self._container = container

    @property
    def duration(self):
        r"""Gets the duration of this ObjectMetaData.

        时长，单位：秒 

        :return: The duration of this ObjectMetaData.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ObjectMetaData.

        时长，单位：秒 

        :param duration: The duration of this ObjectMetaData.
        :type duration: int
        """
        self._duration = duration

    @property
    def video_duration(self):
        r"""Gets the video_duration of this ObjectMetaData.

        时长，单位：秒 

        :return: The video_duration of this ObjectMetaData.
        :rtype: float
        """
        return self._video_duration

    @video_duration.setter
    def video_duration(self, video_duration):
        r"""Sets the video_duration of this ObjectMetaData.

        时长，单位：秒 

        :param video_duration: The video_duration of this ObjectMetaData.
        :type video_duration: float
        """
        self._video_duration = video_duration

    @property
    def audio_duration(self):
        r"""Gets the audio_duration of this ObjectMetaData.

        时长，单位：秒 

        :return: The audio_duration of this ObjectMetaData.
        :rtype: float
        """
        return self._audio_duration

    @audio_duration.setter
    def audio_duration(self, audio_duration):
        r"""Sets the audio_duration of this ObjectMetaData.

        时长，单位：秒 

        :param audio_duration: The audio_duration of this ObjectMetaData.
        :type audio_duration: float
        """
        self._audio_duration = audio_duration

    @property
    def float_duration(self):
        r"""Gets the float_duration of this ObjectMetaData.

        时长，单位：秒 

        :return: The float_duration of this ObjectMetaData.
        :rtype: float
        """
        return self._float_duration

    @float_duration.setter
    def float_duration(self, float_duration):
        r"""Sets the float_duration of this ObjectMetaData.

        时长，单位：秒 

        :param float_duration: The float_duration of this ObjectMetaData.
        :type float_duration: float
        """
        self._float_duration = float_duration

    @property
    def height(self):
        r"""Gets the height of this ObjectMetaData.

        视频高度 

        :return: The height of this ObjectMetaData.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this ObjectMetaData.

        视频高度 

        :param height: The height of this ObjectMetaData.
        :type height: int
        """
        self._height = height

    @property
    def width(self):
        r"""Gets the width of this ObjectMetaData.

        视频宽度 

        :return: The width of this ObjectMetaData.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this ObjectMetaData.

        视频宽度 

        :param width: The width of this ObjectMetaData.
        :type width: int
        """
        self._width = width

    @property
    def md5(self):
        r"""Gets the md5 of this ObjectMetaData.

        视频md5 

        :return: The md5 of this ObjectMetaData.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        r"""Sets the md5 of this ObjectMetaData.

        视频md5 

        :param md5: The md5 of this ObjectMetaData.
        :type md5: str
        """
        self._md5 = md5

    @property
    def rotate(self):
        r"""Gets the rotate of this ObjectMetaData.

        视频拍摄角度 

        :return: The rotate of this ObjectMetaData.
        :rtype: float
        """
        return self._rotate

    @rotate.setter
    def rotate(self, rotate):
        r"""Sets the rotate of this ObjectMetaData.

        视频拍摄角度 

        :param rotate: The rotate of this ObjectMetaData.
        :type rotate: float
        """
        self._rotate = rotate

    @property
    def size(self):
        r"""Gets the size of this ObjectMetaData.

        文件大小，单位：byte 

        :return: The size of this ObjectMetaData.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ObjectMetaData.

        文件大小，单位：byte 

        :param size: The size of this ObjectMetaData.
        :type size: int
        """
        self._size = size

    @property
    def video_stream_list(self):
        r"""Gets the video_stream_list of this ObjectMetaData.

        视频流元数据 

        :return: The video_stream_list of this ObjectMetaData.
        :rtype: list[:class:`huaweicloudsdkvod.v1.MetaVideoInfo`]
        """
        return self._video_stream_list

    @video_stream_list.setter
    def video_stream_list(self, video_stream_list):
        r"""Sets the video_stream_list of this ObjectMetaData.

        视频流元数据 

        :param video_stream_list: The video_stream_list of this ObjectMetaData.
        :type video_stream_list: list[:class:`huaweicloudsdkvod.v1.MetaVideoInfo`]
        """
        self._video_stream_list = video_stream_list

    @property
    def audio_stream_list(self):
        r"""Gets the audio_stream_list of this ObjectMetaData.

        音频流元数据 

        :return: The audio_stream_list of this ObjectMetaData.
        :rtype: list[:class:`huaweicloudsdkvod.v1.MetaAudioInfo`]
        """
        return self._audio_stream_list

    @audio_stream_list.setter
    def audio_stream_list(self, audio_stream_list):
        r"""Sets the audio_stream_list of this ObjectMetaData.

        音频流元数据 

        :param audio_stream_list: The audio_stream_list of this ObjectMetaData.
        :type audio_stream_list: list[:class:`huaweicloudsdkvod.v1.MetaAudioInfo`]
        """
        self._audio_stream_list = audio_stream_list

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
        if not isinstance(other, ObjectMetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
