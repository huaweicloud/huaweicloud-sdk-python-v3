# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'pack_type': 'str',
        'codec': 'str',
        'duration': 'int',
        'video_size': 'int',
        'width': 'int',
        'hight': 'int',
        'bit_rate': 'int',
        'frame_rate': 'int',
        'quality': 'str',
        'audio_channels': 'int'
    }

    attribute_map = {
        'pack_type': 'pack_type',
        'codec': 'codec',
        'duration': 'duration',
        'video_size': 'video_size',
        'width': 'width',
        'hight': 'hight',
        'bit_rate': 'bit_rate',
        'frame_rate': 'frame_rate',
        'quality': 'quality',
        'audio_channels': 'audio_channels'
    }

    def __init__(self, pack_type=None, codec=None, duration=None, video_size=None, width=None, hight=None, bit_rate=None, frame_rate=None, quality=None, audio_channels=None):
        """MetaData

        The model defined in huaweicloud sdk

        :param pack_type: 视频封装格式。  取值如下： - MP4 - TS - MOV - MXF - MPG - FLV - WMV - MP3 - WMA - APE - FLAC - AAC - AC3 - MMF - AMR - M4A - M4R - OGG - WAV - WV - MP2 - AVI - F4V - M4V - MPEG - HLS - DASH
        :type pack_type: str
        :param codec: 视频编码格式。  取值如下： - MPEG-2 - MPEG-4 - H.264 - H.265 - WMV - Vorbis - AAC - AC-3 - AMR - APE - FLAC - MP3 - MP2 - WMA - PCM - ADPCM - WavPack
        :type codec: str
        :param duration: 视频时长。  若视频的原时长为非整数，则该字段值为原时长的向上取整。
        :type duration: int
        :param video_size: 视频文件大小。  单位：字节。
        :type video_size: int
        :param width: 视频宽度（单位：像素）。 - 编码为H.264的取值范围：[32,3840]之间2的倍数。 - 编码为H.265的取值范围：[320,3840]之间4的倍数。
        :type width: int
        :param hight: 视频高度（单位：像素）。 - 编码为H.264的取值范围：[32,2160]之间2的倍数 。 - 编码为H.265的取值范围：[240,2160]之间4的倍数。
        :type hight: int
        :param bit_rate: 视频平均码率。
        :type bit_rate: int
        :param frame_rate: 帧率（单位：帧每秒）。  取值如下： - FRAMERATE_AUTO &#x3D; 1, - FRAMERATE_10 &#x3D; 2, - FRAMERATE_15 &#x3D; 3, - FRAMERATE_2397 &#x3D; 4, // 23.97 fps - FRAMERATE_24 &#x3D; 5, - FRAMERATE_25 &#x3D; 6, - FRAMERATE_2997 &#x3D; 7, // 29.97 fps - FRAMERATE_30 &#x3D; 8, - FRAMERATE_50 &#x3D; 9, - FRAMERATE_60 &#x3D; 10  默认值：1。  单位：帧每秒。
        :type frame_rate: int
        :param quality: 清晰度。  取值如下： - FULL_HD：超高清 - HD：高清 - SD：标清 - FLUENT：流畅 - AD：自适应 - 2K - 4K
        :type quality: str
        :param audio_channels: 音频的声道数。
        :type audio_channels: int
        """
        
        

        self._pack_type = None
        self._codec = None
        self._duration = None
        self._video_size = None
        self._width = None
        self._hight = None
        self._bit_rate = None
        self._frame_rate = None
        self._quality = None
        self._audio_channels = None
        self.discriminator = None

        if pack_type is not None:
            self.pack_type = pack_type
        if codec is not None:
            self.codec = codec
        if duration is not None:
            self.duration = duration
        if video_size is not None:
            self.video_size = video_size
        if width is not None:
            self.width = width
        if hight is not None:
            self.hight = hight
        if bit_rate is not None:
            self.bit_rate = bit_rate
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if quality is not None:
            self.quality = quality
        if audio_channels is not None:
            self.audio_channels = audio_channels

    @property
    def pack_type(self):
        """Gets the pack_type of this MetaData.

        视频封装格式。  取值如下： - MP4 - TS - MOV - MXF - MPG - FLV - WMV - MP3 - WMA - APE - FLAC - AAC - AC3 - MMF - AMR - M4A - M4R - OGG - WAV - WV - MP2 - AVI - F4V - M4V - MPEG - HLS - DASH

        :return: The pack_type of this MetaData.
        :rtype: str
        """
        return self._pack_type

    @pack_type.setter
    def pack_type(self, pack_type):
        """Sets the pack_type of this MetaData.

        视频封装格式。  取值如下： - MP4 - TS - MOV - MXF - MPG - FLV - WMV - MP3 - WMA - APE - FLAC - AAC - AC3 - MMF - AMR - M4A - M4R - OGG - WAV - WV - MP2 - AVI - F4V - M4V - MPEG - HLS - DASH

        :param pack_type: The pack_type of this MetaData.
        :type pack_type: str
        """
        self._pack_type = pack_type

    @property
    def codec(self):
        """Gets the codec of this MetaData.

        视频编码格式。  取值如下： - MPEG-2 - MPEG-4 - H.264 - H.265 - WMV - Vorbis - AAC - AC-3 - AMR - APE - FLAC - MP3 - MP2 - WMA - PCM - ADPCM - WavPack

        :return: The codec of this MetaData.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this MetaData.

        视频编码格式。  取值如下： - MPEG-2 - MPEG-4 - H.264 - H.265 - WMV - Vorbis - AAC - AC-3 - AMR - APE - FLAC - MP3 - MP2 - WMA - PCM - ADPCM - WavPack

        :param codec: The codec of this MetaData.
        :type codec: str
        """
        self._codec = codec

    @property
    def duration(self):
        """Gets the duration of this MetaData.

        视频时长。  若视频的原时长为非整数，则该字段值为原时长的向上取整。

        :return: The duration of this MetaData.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this MetaData.

        视频时长。  若视频的原时长为非整数，则该字段值为原时长的向上取整。

        :param duration: The duration of this MetaData.
        :type duration: int
        """
        self._duration = duration

    @property
    def video_size(self):
        """Gets the video_size of this MetaData.

        视频文件大小。  单位：字节。

        :return: The video_size of this MetaData.
        :rtype: int
        """
        return self._video_size

    @video_size.setter
    def video_size(self, video_size):
        """Sets the video_size of this MetaData.

        视频文件大小。  单位：字节。

        :param video_size: The video_size of this MetaData.
        :type video_size: int
        """
        self._video_size = video_size

    @property
    def width(self):
        """Gets the width of this MetaData.

        视频宽度（单位：像素）。 - 编码为H.264的取值范围：[32,3840]之间2的倍数。 - 编码为H.265的取值范围：[320,3840]之间4的倍数。

        :return: The width of this MetaData.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this MetaData.

        视频宽度（单位：像素）。 - 编码为H.264的取值范围：[32,3840]之间2的倍数。 - 编码为H.265的取值范围：[320,3840]之间4的倍数。

        :param width: The width of this MetaData.
        :type width: int
        """
        self._width = width

    @property
    def hight(self):
        """Gets the hight of this MetaData.

        视频高度（单位：像素）。 - 编码为H.264的取值范围：[32,2160]之间2的倍数 。 - 编码为H.265的取值范围：[240,2160]之间4的倍数。

        :return: The hight of this MetaData.
        :rtype: int
        """
        return self._hight

    @hight.setter
    def hight(self, hight):
        """Sets the hight of this MetaData.

        视频高度（单位：像素）。 - 编码为H.264的取值范围：[32,2160]之间2的倍数 。 - 编码为H.265的取值范围：[240,2160]之间4的倍数。

        :param hight: The hight of this MetaData.
        :type hight: int
        """
        self._hight = hight

    @property
    def bit_rate(self):
        """Gets the bit_rate of this MetaData.

        视频平均码率。

        :return: The bit_rate of this MetaData.
        :rtype: int
        """
        return self._bit_rate

    @bit_rate.setter
    def bit_rate(self, bit_rate):
        """Sets the bit_rate of this MetaData.

        视频平均码率。

        :param bit_rate: The bit_rate of this MetaData.
        :type bit_rate: int
        """
        self._bit_rate = bit_rate

    @property
    def frame_rate(self):
        """Gets the frame_rate of this MetaData.

        帧率（单位：帧每秒）。  取值如下： - FRAMERATE_AUTO = 1, - FRAMERATE_10 = 2, - FRAMERATE_15 = 3, - FRAMERATE_2397 = 4, // 23.97 fps - FRAMERATE_24 = 5, - FRAMERATE_25 = 6, - FRAMERATE_2997 = 7, // 29.97 fps - FRAMERATE_30 = 8, - FRAMERATE_50 = 9, - FRAMERATE_60 = 10  默认值：1。  单位：帧每秒。

        :return: The frame_rate of this MetaData.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this MetaData.

        帧率（单位：帧每秒）。  取值如下： - FRAMERATE_AUTO = 1, - FRAMERATE_10 = 2, - FRAMERATE_15 = 3, - FRAMERATE_2397 = 4, // 23.97 fps - FRAMERATE_24 = 5, - FRAMERATE_25 = 6, - FRAMERATE_2997 = 7, // 29.97 fps - FRAMERATE_30 = 8, - FRAMERATE_50 = 9, - FRAMERATE_60 = 10  默认值：1。  单位：帧每秒。

        :param frame_rate: The frame_rate of this MetaData.
        :type frame_rate: int
        """
        self._frame_rate = frame_rate

    @property
    def quality(self):
        """Gets the quality of this MetaData.

        清晰度。  取值如下： - FULL_HD：超高清 - HD：高清 - SD：标清 - FLUENT：流畅 - AD：自适应 - 2K - 4K

        :return: The quality of this MetaData.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this MetaData.

        清晰度。  取值如下： - FULL_HD：超高清 - HD：高清 - SD：标清 - FLUENT：流畅 - AD：自适应 - 2K - 4K

        :param quality: The quality of this MetaData.
        :type quality: str
        """
        self._quality = quality

    @property
    def audio_channels(self):
        """Gets the audio_channels of this MetaData.

        音频的声道数。

        :return: The audio_channels of this MetaData.
        :rtype: int
        """
        return self._audio_channels

    @audio_channels.setter
    def audio_channels(self, audio_channels):
        """Sets the audio_channels of this MetaData.

        音频的声道数。

        :param audio_channels: The audio_channels of this MetaData.
        :type audio_channels: int
        """
        self._audio_channels = audio_channels

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
        if not isinstance(other, MetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
