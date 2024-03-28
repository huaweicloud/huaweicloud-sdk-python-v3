# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TtsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_property': 'str',
        'speed': 'float',
        'volume': 'int',
        'delay': 'float',
        'pitch': 'str',
        'audio_format': 'str',
        'sample_rate': 'str',
        'tts_source': 'int'
    }

    attribute_map = {
        '_property': 'property',
        'speed': 'speed',
        'volume': 'volume',
        'delay': 'delay',
        'pitch': 'pitch',
        'audio_format': 'audio_format',
        'sample_rate': 'sample_rate',
        'tts_source': 'tts_source'
    }

    def __init__(self, _property=None, speed=None, volume=None, delay=None, pitch=None, audio_format=None, sample_rate=None, tts_source=None):
        """TtsConfig

        The model defined in huaweicloud sdk

        :param _property: 用于设置音色
        :type _property: str
        :param speed: 用户设置音速
        :type speed: float
        :param volume: 用于设置音量
        :type volume: int
        :param delay: 段首停顿时间。 范围：0~60； 单位：秒 默认：0
        :type delay: float
        :param pitch: 音高。 取值范围： -500~500 默认值：0
        :type pitch: str
        :param audio_format: 语音格式头：wav、mp3、pcm 默认：wav
        :type audio_format: str
        :param sample_rate: 采样率：16000、8000 默认：8000
        :type sample_rate: str
        :param tts_source: tts来源： 0：huawei 1：ali 2：用户克隆声音 默认：0
        :type tts_source: int
        """
        
        

        self.__property = None
        self._speed = None
        self._volume = None
        self._delay = None
        self._pitch = None
        self._audio_format = None
        self._sample_rate = None
        self._tts_source = None
        self.discriminator = None

        self._property = _property
        self.speed = speed
        self.volume = volume
        self.delay = delay
        if pitch is not None:
            self.pitch = pitch
        if audio_format is not None:
            self.audio_format = audio_format
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if tts_source is not None:
            self.tts_source = tts_source

    @property
    def _property(self):
        """Gets the _property of this TtsConfig.

        用于设置音色

        :return: The _property of this TtsConfig.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this TtsConfig.

        用于设置音色

        :param _property: The _property of this TtsConfig.
        :type _property: str
        """
        self.__property = _property

    @property
    def speed(self):
        """Gets the speed of this TtsConfig.

        用户设置音速

        :return: The speed of this TtsConfig.
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this TtsConfig.

        用户设置音速

        :param speed: The speed of this TtsConfig.
        :type speed: float
        """
        self._speed = speed

    @property
    def volume(self):
        """Gets the volume of this TtsConfig.

        用于设置音量

        :return: The volume of this TtsConfig.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this TtsConfig.

        用于设置音量

        :param volume: The volume of this TtsConfig.
        :type volume: int
        """
        self._volume = volume

    @property
    def delay(self):
        """Gets the delay of this TtsConfig.

        段首停顿时间。 范围：0~60； 单位：秒 默认：0

        :return: The delay of this TtsConfig.
        :rtype: float
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this TtsConfig.

        段首停顿时间。 范围：0~60； 单位：秒 默认：0

        :param delay: The delay of this TtsConfig.
        :type delay: float
        """
        self._delay = delay

    @property
    def pitch(self):
        """Gets the pitch of this TtsConfig.

        音高。 取值范围： -500~500 默认值：0

        :return: The pitch of this TtsConfig.
        :rtype: str
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        """Sets the pitch of this TtsConfig.

        音高。 取值范围： -500~500 默认值：0

        :param pitch: The pitch of this TtsConfig.
        :type pitch: str
        """
        self._pitch = pitch

    @property
    def audio_format(self):
        """Gets the audio_format of this TtsConfig.

        语音格式头：wav、mp3、pcm 默认：wav

        :return: The audio_format of this TtsConfig.
        :rtype: str
        """
        return self._audio_format

    @audio_format.setter
    def audio_format(self, audio_format):
        """Sets the audio_format of this TtsConfig.

        语音格式头：wav、mp3、pcm 默认：wav

        :param audio_format: The audio_format of this TtsConfig.
        :type audio_format: str
        """
        self._audio_format = audio_format

    @property
    def sample_rate(self):
        """Gets the sample_rate of this TtsConfig.

        采样率：16000、8000 默认：8000

        :return: The sample_rate of this TtsConfig.
        :rtype: str
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this TtsConfig.

        采样率：16000、8000 默认：8000

        :param sample_rate: The sample_rate of this TtsConfig.
        :type sample_rate: str
        """
        self._sample_rate = sample_rate

    @property
    def tts_source(self):
        """Gets the tts_source of this TtsConfig.

        tts来源： 0：huawei 1：ali 2：用户克隆声音 默认：0

        :return: The tts_source of this TtsConfig.
        :rtype: int
        """
        return self._tts_source

    @tts_source.setter
    def tts_source(self, tts_source):
        """Sets the tts_source of this TtsConfig.

        tts来源： 0：huawei 1：ali 2：用户克隆声音 默认：0

        :param tts_source: The tts_source of this TtsConfig.
        :type tts_source: int
        """
        self._tts_source = tts_source

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
        if not isinstance(other, TtsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
