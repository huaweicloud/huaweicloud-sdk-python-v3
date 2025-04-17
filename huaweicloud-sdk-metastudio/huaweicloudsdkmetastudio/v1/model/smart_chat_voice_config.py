# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartChatVoiceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'voice_asset_id': 'str',
        'speed': 'int',
        'pitch': 'int',
        'volume': 'int',
        'provider': 'str',
        'language': 'str',
        'language_desc': 'str'
    }

    attribute_map = {
        'voice_asset_id': 'voice_asset_id',
        'speed': 'speed',
        'pitch': 'pitch',
        'volume': 'volume',
        'provider': 'provider',
        'language': 'language',
        'language_desc': 'language_desc'
    }

    def __init__(self, voice_asset_id=None, speed=None, pitch=None, volume=None, provider=None, language=None, language_desc=None):
        r"""SmartChatVoiceConfig

        The model defined in huaweicloud sdk

        :param voice_asset_id: 语音合成特征字符串
        :type voice_asset_id: str
        :param speed: 语速。默认值100，最小值50，最大值200。 &gt; 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。
        :type speed: int
        :param pitch: 音高。默认值100，最小值50，最大值200。
        :type pitch: int
        :param volume: 音量。默认值140，最小值90，最大值240。
        :type volume: int
        :param provider: 第三方TTS供应商类型。 * XIMALAYA：喜马拉雅TTS * HUAWEI_EI：EI TTS * MOBVOI：出门问问TTS
        :type provider: str
        :param language: 语言类型。默认值CN。 * CN：中文。 * EN：英文。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）
        :type language: str
        :param language_desc: 语言描述。
        :type language_desc: str
        """
        
        

        self._voice_asset_id = None
        self._speed = None
        self._pitch = None
        self._volume = None
        self._provider = None
        self._language = None
        self._language_desc = None
        self.discriminator = None

        if voice_asset_id is not None:
            self.voice_asset_id = voice_asset_id
        if speed is not None:
            self.speed = speed
        if pitch is not None:
            self.pitch = pitch
        if volume is not None:
            self.volume = volume
        if provider is not None:
            self.provider = provider
        if language is not None:
            self.language = language
        if language_desc is not None:
            self.language_desc = language_desc

    @property
    def voice_asset_id(self):
        r"""Gets the voice_asset_id of this SmartChatVoiceConfig.

        语音合成特征字符串

        :return: The voice_asset_id of this SmartChatVoiceConfig.
        :rtype: str
        """
        return self._voice_asset_id

    @voice_asset_id.setter
    def voice_asset_id(self, voice_asset_id):
        r"""Sets the voice_asset_id of this SmartChatVoiceConfig.

        语音合成特征字符串

        :param voice_asset_id: The voice_asset_id of this SmartChatVoiceConfig.
        :type voice_asset_id: str
        """
        self._voice_asset_id = voice_asset_id

    @property
    def speed(self):
        r"""Gets the speed of this SmartChatVoiceConfig.

        语速。默认值100，最小值50，最大值200。 > 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。

        :return: The speed of this SmartChatVoiceConfig.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        r"""Sets the speed of this SmartChatVoiceConfig.

        语速。默认值100，最小值50，最大值200。 > 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。

        :param speed: The speed of this SmartChatVoiceConfig.
        :type speed: int
        """
        self._speed = speed

    @property
    def pitch(self):
        r"""Gets the pitch of this SmartChatVoiceConfig.

        音高。默认值100，最小值50，最大值200。

        :return: The pitch of this SmartChatVoiceConfig.
        :rtype: int
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        r"""Sets the pitch of this SmartChatVoiceConfig.

        音高。默认值100，最小值50，最大值200。

        :param pitch: The pitch of this SmartChatVoiceConfig.
        :type pitch: int
        """
        self._pitch = pitch

    @property
    def volume(self):
        r"""Gets the volume of this SmartChatVoiceConfig.

        音量。默认值140，最小值90，最大值240。

        :return: The volume of this SmartChatVoiceConfig.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this SmartChatVoiceConfig.

        音量。默认值140，最小值90，最大值240。

        :param volume: The volume of this SmartChatVoiceConfig.
        :type volume: int
        """
        self._volume = volume

    @property
    def provider(self):
        r"""Gets the provider of this SmartChatVoiceConfig.

        第三方TTS供应商类型。 * XIMALAYA：喜马拉雅TTS * HUAWEI_EI：EI TTS * MOBVOI：出门问问TTS

        :return: The provider of this SmartChatVoiceConfig.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this SmartChatVoiceConfig.

        第三方TTS供应商类型。 * XIMALAYA：喜马拉雅TTS * HUAWEI_EI：EI TTS * MOBVOI：出门问问TTS

        :param provider: The provider of this SmartChatVoiceConfig.
        :type provider: str
        """
        self._provider = provider

    @property
    def language(self):
        r"""Gets the language of this SmartChatVoiceConfig.

        语言类型。默认值CN。 * CN：中文。 * EN：英文。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :return: The language of this SmartChatVoiceConfig.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this SmartChatVoiceConfig.

        语言类型。默认值CN。 * CN：中文。 * EN：英文。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :param language: The language of this SmartChatVoiceConfig.
        :type language: str
        """
        self._language = language

    @property
    def language_desc(self):
        r"""Gets the language_desc of this SmartChatVoiceConfig.

        语言描述。

        :return: The language_desc of this SmartChatVoiceConfig.
        :rtype: str
        """
        return self._language_desc

    @language_desc.setter
    def language_desc(self, language_desc):
        r"""Sets the language_desc of this SmartChatVoiceConfig.

        语言描述。

        :param language_desc: The language_desc of this SmartChatVoiceConfig.
        :type language_desc: str
        """
        self._language_desc = language_desc

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
        if not isinstance(other, SmartChatVoiceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
