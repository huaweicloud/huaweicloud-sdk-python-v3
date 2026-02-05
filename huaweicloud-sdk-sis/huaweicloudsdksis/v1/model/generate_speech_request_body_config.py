# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenerateSpeechRequestBodyConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_format': 'str',
        'sample_rate': 'str',
        'voice_name': 'str',
        'speed': 'int',
        'pitch': 'int',
        'volume': 'int'
    }

    attribute_map = {
        'audio_format': 'audio_format',
        'sample_rate': 'sample_rate',
        'voice_name': 'voice_name',
        'speed': 'speed',
        'pitch': 'pitch',
        'volume': 'volume'
    }

    def __init__(self, audio_format=None, sample_rate=None, voice_name=None, speed=None, pitch=None, volume=None):
        r"""GenerateSpeechRequestBodyConfig

        The model defined in huaweicloud sdk

        :param audio_format: 语音格式头：wav、mp3、pcm。 默认：wav
        :type audio_format: str
        :param sample_rate: 采样率：8kHz、16kHz、24kHz。 默认：24kHz
        :type sample_rate: str
        :param voice_name: 音色名称。
        :type voice_name: str
        :param speed: 语速：-500~500。 默认：0
        :type speed: int
        :param pitch: 音高：-500~500。 默认：0
        :type pitch: int
        :param volume: 音量：0~100。 默认：50
        :type volume: int
        """
        
        

        self._audio_format = None
        self._sample_rate = None
        self._voice_name = None
        self._speed = None
        self._pitch = None
        self._volume = None
        self.discriminator = None

        if audio_format is not None:
            self.audio_format = audio_format
        if sample_rate is not None:
            self.sample_rate = sample_rate
        self.voice_name = voice_name
        if speed is not None:
            self.speed = speed
        if pitch is not None:
            self.pitch = pitch
        if volume is not None:
            self.volume = volume

    @property
    def audio_format(self):
        r"""Gets the audio_format of this GenerateSpeechRequestBodyConfig.

        语音格式头：wav、mp3、pcm。 默认：wav

        :return: The audio_format of this GenerateSpeechRequestBodyConfig.
        :rtype: str
        """
        return self._audio_format

    @audio_format.setter
    def audio_format(self, audio_format):
        r"""Sets the audio_format of this GenerateSpeechRequestBodyConfig.

        语音格式头：wav、mp3、pcm。 默认：wav

        :param audio_format: The audio_format of this GenerateSpeechRequestBodyConfig.
        :type audio_format: str
        """
        self._audio_format = audio_format

    @property
    def sample_rate(self):
        r"""Gets the sample_rate of this GenerateSpeechRequestBodyConfig.

        采样率：8kHz、16kHz、24kHz。 默认：24kHz

        :return: The sample_rate of this GenerateSpeechRequestBodyConfig.
        :rtype: str
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        r"""Sets the sample_rate of this GenerateSpeechRequestBodyConfig.

        采样率：8kHz、16kHz、24kHz。 默认：24kHz

        :param sample_rate: The sample_rate of this GenerateSpeechRequestBodyConfig.
        :type sample_rate: str
        """
        self._sample_rate = sample_rate

    @property
    def voice_name(self):
        r"""Gets the voice_name of this GenerateSpeechRequestBodyConfig.

        音色名称。

        :return: The voice_name of this GenerateSpeechRequestBodyConfig.
        :rtype: str
        """
        return self._voice_name

    @voice_name.setter
    def voice_name(self, voice_name):
        r"""Sets the voice_name of this GenerateSpeechRequestBodyConfig.

        音色名称。

        :param voice_name: The voice_name of this GenerateSpeechRequestBodyConfig.
        :type voice_name: str
        """
        self._voice_name = voice_name

    @property
    def speed(self):
        r"""Gets the speed of this GenerateSpeechRequestBodyConfig.

        语速：-500~500。 默认：0

        :return: The speed of this GenerateSpeechRequestBodyConfig.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        r"""Sets the speed of this GenerateSpeechRequestBodyConfig.

        语速：-500~500。 默认：0

        :param speed: The speed of this GenerateSpeechRequestBodyConfig.
        :type speed: int
        """
        self._speed = speed

    @property
    def pitch(self):
        r"""Gets the pitch of this GenerateSpeechRequestBodyConfig.

        音高：-500~500。 默认：0

        :return: The pitch of this GenerateSpeechRequestBodyConfig.
        :rtype: int
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        r"""Sets the pitch of this GenerateSpeechRequestBodyConfig.

        音高：-500~500。 默认：0

        :param pitch: The pitch of this GenerateSpeechRequestBodyConfig.
        :type pitch: int
        """
        self._pitch = pitch

    @property
    def volume(self):
        r"""Gets the volume of this GenerateSpeechRequestBodyConfig.

        音量：0~100。 默认：50

        :return: The volume of this GenerateSpeechRequestBodyConfig.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this GenerateSpeechRequestBodyConfig.

        音量：0~100。 默认：50

        :param volume: The volume of this GenerateSpeechRequestBodyConfig.
        :type volume: int
        """
        self._volume = volume

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GenerateSpeechRequestBodyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
