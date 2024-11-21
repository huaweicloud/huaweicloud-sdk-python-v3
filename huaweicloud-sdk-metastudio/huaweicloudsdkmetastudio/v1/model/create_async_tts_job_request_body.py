# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAsyncTtsJobRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text': 'str',
        'voice_asset_id': 'str',
        'speed': 'int',
        'pitch': 'int',
        'volume': 'int',
        'audio_format': 'str',
        'need_timestamp': 'bool',
        'silence_flag': 'bool',
        'silence_time_ms': 'int'
    }

    attribute_map = {
        'text': 'text',
        'voice_asset_id': 'voice_asset_id',
        'speed': 'speed',
        'pitch': 'pitch',
        'volume': 'volume',
        'audio_format': 'audio_format',
        'need_timestamp': 'need_timestamp',
        'silence_flag': 'silence_flag',
        'silence_time_ms': 'silence_time_ms'
    }

    def __init__(self, text=None, voice_asset_id=None, speed=None, pitch=None, volume=None, audio_format=None, need_timestamp=None, silence_flag=None, silence_time_ms=None):
        """CreateAsyncTtsJobRequestBody

        The model defined in huaweicloud sdk

        :param text: 待合成文本
        :type text: str
        :param voice_asset_id: 音色ID
        :type voice_asset_id: str
        :param speed: 语速。 默认值100，最小值50，最大值200。 &gt; * 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。 &gt; * 50表示0.5倍语速，100表示正常语速，200表示2倍语速。
        :type speed: int
        :param pitch: 音高。 默认值100，最小值50，最大值200。
        :type pitch: int
        :param volume: 音量。 默认值140，最小值90，最大值240。
        :type volume: int
        :param audio_format: 输出音频文件格式。默认WAV。 * WAV：wav格式。 * MP3：mp3格式。
        :type audio_format: str
        :param need_timestamp: 是否需要时间戳 false不需要；true：需要返回时间戳信息；默认false
        :type need_timestamp: bool
        :param silence_flag: 异常时是否返回静默音频流
        :type silence_flag: bool
        :param silence_time_ms: 异常时返回的静默音频流时长,单位毫秒
        :type silence_time_ms: int
        """
        
        

        self._text = None
        self._voice_asset_id = None
        self._speed = None
        self._pitch = None
        self._volume = None
        self._audio_format = None
        self._need_timestamp = None
        self._silence_flag = None
        self._silence_time_ms = None
        self.discriminator = None

        self.text = text
        self.voice_asset_id = voice_asset_id
        if speed is not None:
            self.speed = speed
        if pitch is not None:
            self.pitch = pitch
        if volume is not None:
            self.volume = volume
        if audio_format is not None:
            self.audio_format = audio_format
        if need_timestamp is not None:
            self.need_timestamp = need_timestamp
        if silence_flag is not None:
            self.silence_flag = silence_flag
        if silence_time_ms is not None:
            self.silence_time_ms = silence_time_ms

    @property
    def text(self):
        """Gets the text of this CreateAsyncTtsJobRequestBody.

        待合成文本

        :return: The text of this CreateAsyncTtsJobRequestBody.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CreateAsyncTtsJobRequestBody.

        待合成文本

        :param text: The text of this CreateAsyncTtsJobRequestBody.
        :type text: str
        """
        self._text = text

    @property
    def voice_asset_id(self):
        """Gets the voice_asset_id of this CreateAsyncTtsJobRequestBody.

        音色ID

        :return: The voice_asset_id of this CreateAsyncTtsJobRequestBody.
        :rtype: str
        """
        return self._voice_asset_id

    @voice_asset_id.setter
    def voice_asset_id(self, voice_asset_id):
        """Sets the voice_asset_id of this CreateAsyncTtsJobRequestBody.

        音色ID

        :param voice_asset_id: The voice_asset_id of this CreateAsyncTtsJobRequestBody.
        :type voice_asset_id: str
        """
        self._voice_asset_id = voice_asset_id

    @property
    def speed(self):
        """Gets the speed of this CreateAsyncTtsJobRequestBody.

        语速。 默认值100，最小值50，最大值200。 > * 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。 > * 50表示0.5倍语速，100表示正常语速，200表示2倍语速。

        :return: The speed of this CreateAsyncTtsJobRequestBody.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this CreateAsyncTtsJobRequestBody.

        语速。 默认值100，最小值50，最大值200。 > * 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。 > * 50表示0.5倍语速，100表示正常语速，200表示2倍语速。

        :param speed: The speed of this CreateAsyncTtsJobRequestBody.
        :type speed: int
        """
        self._speed = speed

    @property
    def pitch(self):
        """Gets the pitch of this CreateAsyncTtsJobRequestBody.

        音高。 默认值100，最小值50，最大值200。

        :return: The pitch of this CreateAsyncTtsJobRequestBody.
        :rtype: int
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        """Sets the pitch of this CreateAsyncTtsJobRequestBody.

        音高。 默认值100，最小值50，最大值200。

        :param pitch: The pitch of this CreateAsyncTtsJobRequestBody.
        :type pitch: int
        """
        self._pitch = pitch

    @property
    def volume(self):
        """Gets the volume of this CreateAsyncTtsJobRequestBody.

        音量。 默认值140，最小值90，最大值240。

        :return: The volume of this CreateAsyncTtsJobRequestBody.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this CreateAsyncTtsJobRequestBody.

        音量。 默认值140，最小值90，最大值240。

        :param volume: The volume of this CreateAsyncTtsJobRequestBody.
        :type volume: int
        """
        self._volume = volume

    @property
    def audio_format(self):
        """Gets the audio_format of this CreateAsyncTtsJobRequestBody.

        输出音频文件格式。默认WAV。 * WAV：wav格式。 * MP3：mp3格式。

        :return: The audio_format of this CreateAsyncTtsJobRequestBody.
        :rtype: str
        """
        return self._audio_format

    @audio_format.setter
    def audio_format(self, audio_format):
        """Sets the audio_format of this CreateAsyncTtsJobRequestBody.

        输出音频文件格式。默认WAV。 * WAV：wav格式。 * MP3：mp3格式。

        :param audio_format: The audio_format of this CreateAsyncTtsJobRequestBody.
        :type audio_format: str
        """
        self._audio_format = audio_format

    @property
    def need_timestamp(self):
        """Gets the need_timestamp of this CreateAsyncTtsJobRequestBody.

        是否需要时间戳 false不需要；true：需要返回时间戳信息；默认false

        :return: The need_timestamp of this CreateAsyncTtsJobRequestBody.
        :rtype: bool
        """
        return self._need_timestamp

    @need_timestamp.setter
    def need_timestamp(self, need_timestamp):
        """Sets the need_timestamp of this CreateAsyncTtsJobRequestBody.

        是否需要时间戳 false不需要；true：需要返回时间戳信息；默认false

        :param need_timestamp: The need_timestamp of this CreateAsyncTtsJobRequestBody.
        :type need_timestamp: bool
        """
        self._need_timestamp = need_timestamp

    @property
    def silence_flag(self):
        """Gets the silence_flag of this CreateAsyncTtsJobRequestBody.

        异常时是否返回静默音频流

        :return: The silence_flag of this CreateAsyncTtsJobRequestBody.
        :rtype: bool
        """
        return self._silence_flag

    @silence_flag.setter
    def silence_flag(self, silence_flag):
        """Sets the silence_flag of this CreateAsyncTtsJobRequestBody.

        异常时是否返回静默音频流

        :param silence_flag: The silence_flag of this CreateAsyncTtsJobRequestBody.
        :type silence_flag: bool
        """
        self._silence_flag = silence_flag

    @property
    def silence_time_ms(self):
        """Gets the silence_time_ms of this CreateAsyncTtsJobRequestBody.

        异常时返回的静默音频流时长,单位毫秒

        :return: The silence_time_ms of this CreateAsyncTtsJobRequestBody.
        :rtype: int
        """
        return self._silence_time_ms

    @silence_time_ms.setter
    def silence_time_ms(self, silence_time_ms):
        """Sets the silence_time_ms of this CreateAsyncTtsJobRequestBody.

        异常时返回的静默音频流时长,单位毫秒

        :param silence_time_ms: The silence_time_ms of this CreateAsyncTtsJobRequestBody.
        :type silence_time_ms: int
        """
        self._silence_time_ms = silence_time_ms

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
        if not isinstance(other, CreateAsyncTtsJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
