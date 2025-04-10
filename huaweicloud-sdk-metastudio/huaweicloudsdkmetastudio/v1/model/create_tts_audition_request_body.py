# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTtsAuditionRequestBody:

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
        'tts_text': 'str',
        'emotion': 'str',
        'speed': 'int',
        'pitch': 'int',
        'volume': 'int',
        'business_type': 'str',
        'style': 'str',
        'channels': 'int',
        'is_vocabulary_config_enable': 'bool'
    }

    attribute_map = {
        'text': 'text',
        'tts_text': 'tts_text',
        'emotion': 'emotion',
        'speed': 'speed',
        'pitch': 'pitch',
        'volume': 'volume',
        'business_type': 'business_type',
        'style': 'style',
        'channels': 'channels',
        'is_vocabulary_config_enable': 'is_vocabulary_config_enable'
    }

    def __init__(self, text=None, tts_text=None, emotion=None, speed=None, pitch=None, volume=None, business_type=None, style=None, channels=None, is_vocabulary_config_enable=None):
        r"""CreateTtsAuditionRequestBody

        The model defined in huaweicloud sdk

        :param text: 待合成文本。
        :type text: str
        :param tts_text: 发送给tts的待合成文本。
        :type tts_text: str
        :param emotion: 音色ID，获取方式详见[获取音色ID](metastudio_02_0054.xml)。
        :type emotion: str
        :param speed: 语速。 * 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。 * 50表示0.5倍语速，100表示正常语速，200表示2倍语速。
        :type speed: int
        :param pitch: 音高。
        :type pitch: int
        :param volume: 音量。
        :type volume: int
        :param business_type: 业务场景，多个入口调用试听接口时的业务场景
        :type business_type: str
        :param style: 风格情感
        :type style: str
        :param channels: 声道。（单声道|双声道） 默认值1，最小值1，最大值2。
        :type channels: int
        :param is_vocabulary_config_enable: 是否应用当前租户的读法配置
        :type is_vocabulary_config_enable: bool
        """
        
        

        self._text = None
        self._tts_text = None
        self._emotion = None
        self._speed = None
        self._pitch = None
        self._volume = None
        self._business_type = None
        self._style = None
        self._channels = None
        self._is_vocabulary_config_enable = None
        self.discriminator = None

        self.text = text
        if tts_text is not None:
            self.tts_text = tts_text
        self.emotion = emotion
        if speed is not None:
            self.speed = speed
        if pitch is not None:
            self.pitch = pitch
        if volume is not None:
            self.volume = volume
        if business_type is not None:
            self.business_type = business_type
        if style is not None:
            self.style = style
        if channels is not None:
            self.channels = channels
        if is_vocabulary_config_enable is not None:
            self.is_vocabulary_config_enable = is_vocabulary_config_enable

    @property
    def text(self):
        r"""Gets the text of this CreateTtsAuditionRequestBody.

        待合成文本。

        :return: The text of this CreateTtsAuditionRequestBody.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this CreateTtsAuditionRequestBody.

        待合成文本。

        :param text: The text of this CreateTtsAuditionRequestBody.
        :type text: str
        """
        self._text = text

    @property
    def tts_text(self):
        r"""Gets the tts_text of this CreateTtsAuditionRequestBody.

        发送给tts的待合成文本。

        :return: The tts_text of this CreateTtsAuditionRequestBody.
        :rtype: str
        """
        return self._tts_text

    @tts_text.setter
    def tts_text(self, tts_text):
        r"""Sets the tts_text of this CreateTtsAuditionRequestBody.

        发送给tts的待合成文本。

        :param tts_text: The tts_text of this CreateTtsAuditionRequestBody.
        :type tts_text: str
        """
        self._tts_text = tts_text

    @property
    def emotion(self):
        r"""Gets the emotion of this CreateTtsAuditionRequestBody.

        音色ID，获取方式详见[获取音色ID](metastudio_02_0054.xml)。

        :return: The emotion of this CreateTtsAuditionRequestBody.
        :rtype: str
        """
        return self._emotion

    @emotion.setter
    def emotion(self, emotion):
        r"""Sets the emotion of this CreateTtsAuditionRequestBody.

        音色ID，获取方式详见[获取音色ID](metastudio_02_0054.xml)。

        :param emotion: The emotion of this CreateTtsAuditionRequestBody.
        :type emotion: str
        """
        self._emotion = emotion

    @property
    def speed(self):
        r"""Gets the speed of this CreateTtsAuditionRequestBody.

        语速。 * 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。 * 50表示0.5倍语速，100表示正常语速，200表示2倍语速。

        :return: The speed of this CreateTtsAuditionRequestBody.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        r"""Sets the speed of this CreateTtsAuditionRequestBody.

        语速。 * 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。 * 50表示0.5倍语速，100表示正常语速，200表示2倍语速。

        :param speed: The speed of this CreateTtsAuditionRequestBody.
        :type speed: int
        """
        self._speed = speed

    @property
    def pitch(self):
        r"""Gets the pitch of this CreateTtsAuditionRequestBody.

        音高。

        :return: The pitch of this CreateTtsAuditionRequestBody.
        :rtype: int
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        r"""Sets the pitch of this CreateTtsAuditionRequestBody.

        音高。

        :param pitch: The pitch of this CreateTtsAuditionRequestBody.
        :type pitch: int
        """
        self._pitch = pitch

    @property
    def volume(self):
        r"""Gets the volume of this CreateTtsAuditionRequestBody.

        音量。

        :return: The volume of this CreateTtsAuditionRequestBody.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this CreateTtsAuditionRequestBody.

        音量。

        :param volume: The volume of this CreateTtsAuditionRequestBody.
        :type volume: int
        """
        self._volume = volume

    @property
    def business_type(self):
        r"""Gets the business_type of this CreateTtsAuditionRequestBody.

        业务场景，多个入口调用试听接口时的业务场景

        :return: The business_type of this CreateTtsAuditionRequestBody.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this CreateTtsAuditionRequestBody.

        业务场景，多个入口调用试听接口时的业务场景

        :param business_type: The business_type of this CreateTtsAuditionRequestBody.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def style(self):
        r"""Gets the style of this CreateTtsAuditionRequestBody.

        风格情感

        :return: The style of this CreateTtsAuditionRequestBody.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        r"""Sets the style of this CreateTtsAuditionRequestBody.

        风格情感

        :param style: The style of this CreateTtsAuditionRequestBody.
        :type style: str
        """
        self._style = style

    @property
    def channels(self):
        r"""Gets the channels of this CreateTtsAuditionRequestBody.

        声道。（单声道|双声道） 默认值1，最小值1，最大值2。

        :return: The channels of this CreateTtsAuditionRequestBody.
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        r"""Sets the channels of this CreateTtsAuditionRequestBody.

        声道。（单声道|双声道） 默认值1，最小值1，最大值2。

        :param channels: The channels of this CreateTtsAuditionRequestBody.
        :type channels: int
        """
        self._channels = channels

    @property
    def is_vocabulary_config_enable(self):
        r"""Gets the is_vocabulary_config_enable of this CreateTtsAuditionRequestBody.

        是否应用当前租户的读法配置

        :return: The is_vocabulary_config_enable of this CreateTtsAuditionRequestBody.
        :rtype: bool
        """
        return self._is_vocabulary_config_enable

    @is_vocabulary_config_enable.setter
    def is_vocabulary_config_enable(self, is_vocabulary_config_enable):
        r"""Sets the is_vocabulary_config_enable of this CreateTtsAuditionRequestBody.

        是否应用当前租户的读法配置

        :param is_vocabulary_config_enable: The is_vocabulary_config_enable of this CreateTtsAuditionRequestBody.
        :type is_vocabulary_config_enable: bool
        """
        self._is_vocabulary_config_enable = is_vocabulary_config_enable

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
        if not isinstance(other, CreateTtsAuditionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
