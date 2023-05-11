# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MpeMetaData:

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
        'duration': 'float',
        'video_size': 'int',
        'width': 'int',
        'height': 'int',
        'bit_rate': 'int',
        'audio_bit_rate': 'int',
        'frame_rate': 'int',
        'codec_name': 'str',
        'audio_codec_name': 'str',
        'channels': 'int',
        'sample': 'int',
        'is_audio': 'bool'
    }

    attribute_map = {
        'pack_type': 'pack_type',
        'duration': 'duration',
        'video_size': 'video_size',
        'width': 'width',
        'height': 'height',
        'bit_rate': 'bit_rate',
        'audio_bit_rate': 'audio_bit_rate',
        'frame_rate': 'frame_rate',
        'codec_name': 'codec_name',
        'audio_codec_name': 'audio_codec_name',
        'channels': 'channels',
        'sample': 'sample',
        'is_audio': 'is_audio'
    }

    def __init__(self, pack_type=None, duration=None, video_size=None, width=None, height=None, bit_rate=None, audio_bit_rate=None, frame_rate=None, codec_name=None, audio_codec_name=None, channels=None, sample=None, is_audio=None):
        """MpeMetaData

        The model defined in huaweicloud sdk

        :param pack_type: 封装类型。
        :type pack_type: str
        :param duration: 视频时长。
        :type duration: float
        :param video_size: 视频大小。
        :type video_size: int
        :param width: 视频宽度。
        :type width: int
        :param height: 视频高度。
        :type height: int
        :param bit_rate: 码率。
        :type bit_rate: int
        :param audio_bit_rate: 音频码率。
        :type audio_bit_rate: int
        :param frame_rate: 帧率。  取值范围：0或[5,60]，0表示自适应。  单位：帧每秒。  &gt; 若设置的帧率不在取值范围内，则自动调整为0，若设置的帧率高于片源帧率，则自动调整为片源帧率。 
        :type frame_rate: int
        :param codec_name: 编码类型名称。
        :type codec_name: str
        :param audio_codec_name: 音频编码类型。
        :type audio_codec_name: str
        :param channels: 声道数。
        :type channels: int
        :param sample: 采样率。
        :type sample: int
        :param is_audio: 是否音频。
        :type is_audio: bool
        """
        
        

        self._pack_type = None
        self._duration = None
        self._video_size = None
        self._width = None
        self._height = None
        self._bit_rate = None
        self._audio_bit_rate = None
        self._frame_rate = None
        self._codec_name = None
        self._audio_codec_name = None
        self._channels = None
        self._sample = None
        self._is_audio = None
        self.discriminator = None

        if pack_type is not None:
            self.pack_type = pack_type
        if duration is not None:
            self.duration = duration
        if video_size is not None:
            self.video_size = video_size
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if bit_rate is not None:
            self.bit_rate = bit_rate
        if audio_bit_rate is not None:
            self.audio_bit_rate = audio_bit_rate
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if codec_name is not None:
            self.codec_name = codec_name
        if audio_codec_name is not None:
            self.audio_codec_name = audio_codec_name
        if channels is not None:
            self.channels = channels
        if sample is not None:
            self.sample = sample
        if is_audio is not None:
            self.is_audio = is_audio

    @property
    def pack_type(self):
        """Gets the pack_type of this MpeMetaData.

        封装类型。

        :return: The pack_type of this MpeMetaData.
        :rtype: str
        """
        return self._pack_type

    @pack_type.setter
    def pack_type(self, pack_type):
        """Sets the pack_type of this MpeMetaData.

        封装类型。

        :param pack_type: The pack_type of this MpeMetaData.
        :type pack_type: str
        """
        self._pack_type = pack_type

    @property
    def duration(self):
        """Gets the duration of this MpeMetaData.

        视频时长。

        :return: The duration of this MpeMetaData.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this MpeMetaData.

        视频时长。

        :param duration: The duration of this MpeMetaData.
        :type duration: float
        """
        self._duration = duration

    @property
    def video_size(self):
        """Gets the video_size of this MpeMetaData.

        视频大小。

        :return: The video_size of this MpeMetaData.
        :rtype: int
        """
        return self._video_size

    @video_size.setter
    def video_size(self, video_size):
        """Sets the video_size of this MpeMetaData.

        视频大小。

        :param video_size: The video_size of this MpeMetaData.
        :type video_size: int
        """
        self._video_size = video_size

    @property
    def width(self):
        """Gets the width of this MpeMetaData.

        视频宽度。

        :return: The width of this MpeMetaData.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this MpeMetaData.

        视频宽度。

        :param width: The width of this MpeMetaData.
        :type width: int
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this MpeMetaData.

        视频高度。

        :return: The height of this MpeMetaData.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this MpeMetaData.

        视频高度。

        :param height: The height of this MpeMetaData.
        :type height: int
        """
        self._height = height

    @property
    def bit_rate(self):
        """Gets the bit_rate of this MpeMetaData.

        码率。

        :return: The bit_rate of this MpeMetaData.
        :rtype: int
        """
        return self._bit_rate

    @bit_rate.setter
    def bit_rate(self, bit_rate):
        """Sets the bit_rate of this MpeMetaData.

        码率。

        :param bit_rate: The bit_rate of this MpeMetaData.
        :type bit_rate: int
        """
        self._bit_rate = bit_rate

    @property
    def audio_bit_rate(self):
        """Gets the audio_bit_rate of this MpeMetaData.

        音频码率。

        :return: The audio_bit_rate of this MpeMetaData.
        :rtype: int
        """
        return self._audio_bit_rate

    @audio_bit_rate.setter
    def audio_bit_rate(self, audio_bit_rate):
        """Sets the audio_bit_rate of this MpeMetaData.

        音频码率。

        :param audio_bit_rate: The audio_bit_rate of this MpeMetaData.
        :type audio_bit_rate: int
        """
        self._audio_bit_rate = audio_bit_rate

    @property
    def frame_rate(self):
        """Gets the frame_rate of this MpeMetaData.

        帧率。  取值范围：0或[5,60]，0表示自适应。  单位：帧每秒。  > 若设置的帧率不在取值范围内，则自动调整为0，若设置的帧率高于片源帧率，则自动调整为片源帧率。 

        :return: The frame_rate of this MpeMetaData.
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this MpeMetaData.

        帧率。  取值范围：0或[5,60]，0表示自适应。  单位：帧每秒。  > 若设置的帧率不在取值范围内，则自动调整为0，若设置的帧率高于片源帧率，则自动调整为片源帧率。 

        :param frame_rate: The frame_rate of this MpeMetaData.
        :type frame_rate: int
        """
        self._frame_rate = frame_rate

    @property
    def codec_name(self):
        """Gets the codec_name of this MpeMetaData.

        编码类型名称。

        :return: The codec_name of this MpeMetaData.
        :rtype: str
        """
        return self._codec_name

    @codec_name.setter
    def codec_name(self, codec_name):
        """Sets the codec_name of this MpeMetaData.

        编码类型名称。

        :param codec_name: The codec_name of this MpeMetaData.
        :type codec_name: str
        """
        self._codec_name = codec_name

    @property
    def audio_codec_name(self):
        """Gets the audio_codec_name of this MpeMetaData.

        音频编码类型。

        :return: The audio_codec_name of this MpeMetaData.
        :rtype: str
        """
        return self._audio_codec_name

    @audio_codec_name.setter
    def audio_codec_name(self, audio_codec_name):
        """Sets the audio_codec_name of this MpeMetaData.

        音频编码类型。

        :param audio_codec_name: The audio_codec_name of this MpeMetaData.
        :type audio_codec_name: str
        """
        self._audio_codec_name = audio_codec_name

    @property
    def channels(self):
        """Gets the channels of this MpeMetaData.

        声道数。

        :return: The channels of this MpeMetaData.
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this MpeMetaData.

        声道数。

        :param channels: The channels of this MpeMetaData.
        :type channels: int
        """
        self._channels = channels

    @property
    def sample(self):
        """Gets the sample of this MpeMetaData.

        采样率。

        :return: The sample of this MpeMetaData.
        :rtype: int
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this MpeMetaData.

        采样率。

        :param sample: The sample of this MpeMetaData.
        :type sample: int
        """
        self._sample = sample

    @property
    def is_audio(self):
        """Gets the is_audio of this MpeMetaData.

        是否音频。

        :return: The is_audio of this MpeMetaData.
        :rtype: bool
        """
        return self._is_audio

    @is_audio.setter
    def is_audio(self, is_audio):
        """Sets the is_audio of this MpeMetaData.

        是否音频。

        :param is_audio: The is_audio of this MpeMetaData.
        :type is_audio: bool
        """
        self._is_audio = is_audio

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
        if not isinstance(other, MpeMetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
