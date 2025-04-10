# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VoiceConfig:

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
        'volume': 'int'
    }

    attribute_map = {
        'voice_asset_id': 'voice_asset_id',
        'speed': 'speed',
        'pitch': 'pitch',
        'volume': 'volume'
    }

    def __init__(self, voice_asset_id=None, speed=None, pitch=None, volume=None):
        r"""VoiceConfig

        The model defined in huaweicloud sdk

        :param voice_asset_id: **参数解释**： 音色资产ID，可以从资产库中查询。 音色ID的查询操作，详见[查询预置音色ID](metastudio_02_0054.xml)。 **约束限制**： 不涉及。 **取值范围**： 字符长度1-256位。 **默认取值**： 不涉及。
        :type voice_asset_id: str
        :param speed: **参数解释**： 语速。50表示0.5倍语速，100表示正常语速，200表示2倍语速。 当取值为“100”时，表示一个成年人的正常语速，约为250字/分钟。  **约束限制**： 不涉及。
        :type speed: int
        :param pitch: **参数解释**： 音高。 **约束限制**： 不涉及。
        :type pitch: int
        :param volume: **参数解释**： 音量。 **约束限制**： 不涉及。
        :type volume: int
        """
        
        

        self._voice_asset_id = None
        self._speed = None
        self._pitch = None
        self._volume = None
        self.discriminator = None

        self.voice_asset_id = voice_asset_id
        if speed is not None:
            self.speed = speed
        if pitch is not None:
            self.pitch = pitch
        if volume is not None:
            self.volume = volume

    @property
    def voice_asset_id(self):
        r"""Gets the voice_asset_id of this VoiceConfig.

        **参数解释**： 音色资产ID，可以从资产库中查询。 音色ID的查询操作，详见[查询预置音色ID](metastudio_02_0054.xml)。 **约束限制**： 不涉及。 **取值范围**： 字符长度1-256位。 **默认取值**： 不涉及。

        :return: The voice_asset_id of this VoiceConfig.
        :rtype: str
        """
        return self._voice_asset_id

    @voice_asset_id.setter
    def voice_asset_id(self, voice_asset_id):
        r"""Sets the voice_asset_id of this VoiceConfig.

        **参数解释**： 音色资产ID，可以从资产库中查询。 音色ID的查询操作，详见[查询预置音色ID](metastudio_02_0054.xml)。 **约束限制**： 不涉及。 **取值范围**： 字符长度1-256位。 **默认取值**： 不涉及。

        :param voice_asset_id: The voice_asset_id of this VoiceConfig.
        :type voice_asset_id: str
        """
        self._voice_asset_id = voice_asset_id

    @property
    def speed(self):
        r"""Gets the speed of this VoiceConfig.

        **参数解释**： 语速。50表示0.5倍语速，100表示正常语速，200表示2倍语速。 当取值为“100”时，表示一个成年人的正常语速，约为250字/分钟。  **约束限制**： 不涉及。

        :return: The speed of this VoiceConfig.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        r"""Sets the speed of this VoiceConfig.

        **参数解释**： 语速。50表示0.5倍语速，100表示正常语速，200表示2倍语速。 当取值为“100”时，表示一个成年人的正常语速，约为250字/分钟。  **约束限制**： 不涉及。

        :param speed: The speed of this VoiceConfig.
        :type speed: int
        """
        self._speed = speed

    @property
    def pitch(self):
        r"""Gets the pitch of this VoiceConfig.

        **参数解释**： 音高。 **约束限制**： 不涉及。

        :return: The pitch of this VoiceConfig.
        :rtype: int
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        r"""Sets the pitch of this VoiceConfig.

        **参数解释**： 音高。 **约束限制**： 不涉及。

        :param pitch: The pitch of this VoiceConfig.
        :type pitch: int
        """
        self._pitch = pitch

    @property
    def volume(self):
        r"""Gets the volume of this VoiceConfig.

        **参数解释**： 音量。 **约束限制**： 不涉及。

        :return: The volume of this VoiceConfig.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this VoiceConfig.

        **参数解释**： 音量。 **约束限制**： 不涉及。

        :param volume: The volume of this VoiceConfig.
        :type volume: int
        """
        self._volume = volume

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
        if not isinstance(other, VoiceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
