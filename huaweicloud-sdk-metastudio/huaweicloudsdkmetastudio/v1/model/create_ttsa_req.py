# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTTSAReq:

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
        'text': 'str',
        'speed': 'int',
        'pitch': 'int',
        'volume': 'int',
        'emotion': 'str',
        'style_id': 'str',
        'camera_position': 'str'
    }

    attribute_map = {
        'voice_asset_id': 'voice_asset_id',
        'text': 'text',
        'speed': 'speed',
        'pitch': 'pitch',
        'volume': 'volume',
        'emotion': 'emotion',
        'style_id': 'style_id',
        'camera_position': 'camera_position'
    }

    def __init__(self, voice_asset_id=None, text=None, speed=None, pitch=None, volume=None, emotion=None, style_id=None, camera_position=None):
        """CreateTTSAReq

        The model defined in huaweicloud sdk

        :param voice_asset_id: 音色模型ID
        :type voice_asset_id: str
        :param text: HTML格式的台词，可包含动作。最多2048个字符。 &gt; * HTML格式举例：\\&lt;speak&gt;大家好&lt;insert-action id&#x3D;\\\&quot;14cc7bbcde4982aab82f9d9af9e0f743\\\&quot;/&gt;，非常高兴给大家介绍MetaStudio。\\&lt;/speak&gt; &gt; * insert-action id通过查询资产列表接口获取，查询时asset_type&#x3D;ANIMATION &gt; * 多音字标签：\\&lt;phoneme ph&#x3D;\\\&quot;拼音\\\&quot;&gt;汉字\\&lt;/phoneme&gt;，南京\\&lt;phoneme ph&#x3D;\\\&quot;shi4 zhang3\\\&quot;&gt;市长\\&lt;/phoneme&gt;江大桥。 &gt; * 停顿标签：\\&lt;break/&gt;，中方一贯主张\\&lt;break/&gt;维护国家主权平等，不干涉他国内政\\&lt;break time&#x3D;\\\&quot;300ms\\\&quot;/&gt;是联合国宪章\\&lt;break time&#x3D;\\\&quot;500ms\\\&quot;/&gt;最重要的原则。
        :type text: str
        :param speed: 语速。  取值范围[50,200]   默认值：100
        :type speed: int
        :param pitch: 基频。  取值范围[50,200]  默认值：100
        :type pitch: int
        :param volume: 音量。  取值范围[90,240]   默认值：100
        :type volume: int
        :param emotion: 情感标签。 * ANGER：愤怒 * HAPPY：开心 * SAD：悲伤 * CALM：平静
        :type emotion: str
        :param style_id: 风格化ID。
        :type style_id: str
        :param camera_position: 人位置及相机位置。由如下4组浮点数组成的字符：人位置的X/Y/Z值，人角度的Pitch/Yaw/Roll值；相机位置的X/Y/Z值，相机角度的Pitch/Yaw/Roll值。
        :type camera_position: str
        """
        
        

        self._voice_asset_id = None
        self._text = None
        self._speed = None
        self._pitch = None
        self._volume = None
        self._emotion = None
        self._style_id = None
        self._camera_position = None
        self.discriminator = None

        self.voice_asset_id = voice_asset_id
        self.text = text
        if speed is not None:
            self.speed = speed
        if pitch is not None:
            self.pitch = pitch
        if volume is not None:
            self.volume = volume
        if emotion is not None:
            self.emotion = emotion
        if style_id is not None:
            self.style_id = style_id
        if camera_position is not None:
            self.camera_position = camera_position

    @property
    def voice_asset_id(self):
        """Gets the voice_asset_id of this CreateTTSAReq.

        音色模型ID

        :return: The voice_asset_id of this CreateTTSAReq.
        :rtype: str
        """
        return self._voice_asset_id

    @voice_asset_id.setter
    def voice_asset_id(self, voice_asset_id):
        """Sets the voice_asset_id of this CreateTTSAReq.

        音色模型ID

        :param voice_asset_id: The voice_asset_id of this CreateTTSAReq.
        :type voice_asset_id: str
        """
        self._voice_asset_id = voice_asset_id

    @property
    def text(self):
        """Gets the text of this CreateTTSAReq.

        HTML格式的台词，可包含动作。最多2048个字符。 > * HTML格式举例：\\<speak>大家好<insert-action id=\\\"14cc7bbcde4982aab82f9d9af9e0f743\\\"/>，非常高兴给大家介绍MetaStudio。\\</speak> > * insert-action id通过查询资产列表接口获取，查询时asset_type=ANIMATION > * 多音字标签：\\<phoneme ph=\\\"拼音\\\">汉字\\</phoneme>，南京\\<phoneme ph=\\\"shi4 zhang3\\\">市长\\</phoneme>江大桥。 > * 停顿标签：\\<break/>，中方一贯主张\\<break/>维护国家主权平等，不干涉他国内政\\<break time=\\\"300ms\\\"/>是联合国宪章\\<break time=\\\"500ms\\\"/>最重要的原则。

        :return: The text of this CreateTTSAReq.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CreateTTSAReq.

        HTML格式的台词，可包含动作。最多2048个字符。 > * HTML格式举例：\\<speak>大家好<insert-action id=\\\"14cc7bbcde4982aab82f9d9af9e0f743\\\"/>，非常高兴给大家介绍MetaStudio。\\</speak> > * insert-action id通过查询资产列表接口获取，查询时asset_type=ANIMATION > * 多音字标签：\\<phoneme ph=\\\"拼音\\\">汉字\\</phoneme>，南京\\<phoneme ph=\\\"shi4 zhang3\\\">市长\\</phoneme>江大桥。 > * 停顿标签：\\<break/>，中方一贯主张\\<break/>维护国家主权平等，不干涉他国内政\\<break time=\\\"300ms\\\"/>是联合国宪章\\<break time=\\\"500ms\\\"/>最重要的原则。

        :param text: The text of this CreateTTSAReq.
        :type text: str
        """
        self._text = text

    @property
    def speed(self):
        """Gets the speed of this CreateTTSAReq.

        语速。  取值范围[50,200]   默认值：100

        :return: The speed of this CreateTTSAReq.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this CreateTTSAReq.

        语速。  取值范围[50,200]   默认值：100

        :param speed: The speed of this CreateTTSAReq.
        :type speed: int
        """
        self._speed = speed

    @property
    def pitch(self):
        """Gets the pitch of this CreateTTSAReq.

        基频。  取值范围[50,200]  默认值：100

        :return: The pitch of this CreateTTSAReq.
        :rtype: int
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        """Sets the pitch of this CreateTTSAReq.

        基频。  取值范围[50,200]  默认值：100

        :param pitch: The pitch of this CreateTTSAReq.
        :type pitch: int
        """
        self._pitch = pitch

    @property
    def volume(self):
        """Gets the volume of this CreateTTSAReq.

        音量。  取值范围[90,240]   默认值：100

        :return: The volume of this CreateTTSAReq.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this CreateTTSAReq.

        音量。  取值范围[90,240]   默认值：100

        :param volume: The volume of this CreateTTSAReq.
        :type volume: int
        """
        self._volume = volume

    @property
    def emotion(self):
        """Gets the emotion of this CreateTTSAReq.

        情感标签。 * ANGER：愤怒 * HAPPY：开心 * SAD：悲伤 * CALM：平静

        :return: The emotion of this CreateTTSAReq.
        :rtype: str
        """
        return self._emotion

    @emotion.setter
    def emotion(self, emotion):
        """Sets the emotion of this CreateTTSAReq.

        情感标签。 * ANGER：愤怒 * HAPPY：开心 * SAD：悲伤 * CALM：平静

        :param emotion: The emotion of this CreateTTSAReq.
        :type emotion: str
        """
        self._emotion = emotion

    @property
    def style_id(self):
        """Gets the style_id of this CreateTTSAReq.

        风格化ID。

        :return: The style_id of this CreateTTSAReq.
        :rtype: str
        """
        return self._style_id

    @style_id.setter
    def style_id(self, style_id):
        """Sets the style_id of this CreateTTSAReq.

        风格化ID。

        :param style_id: The style_id of this CreateTTSAReq.
        :type style_id: str
        """
        self._style_id = style_id

    @property
    def camera_position(self):
        """Gets the camera_position of this CreateTTSAReq.

        人位置及相机位置。由如下4组浮点数组成的字符：人位置的X/Y/Z值，人角度的Pitch/Yaw/Roll值；相机位置的X/Y/Z值，相机角度的Pitch/Yaw/Roll值。

        :return: The camera_position of this CreateTTSAReq.
        :rtype: str
        """
        return self._camera_position

    @camera_position.setter
    def camera_position(self, camera_position):
        """Sets the camera_position of this CreateTTSAReq.

        人位置及相机位置。由如下4组浮点数组成的字符：人位置的X/Y/Z值，人角度的Pitch/Yaw/Roll值；相机位置的X/Y/Z值，相机角度的Pitch/Yaw/Roll值。

        :param camera_position: The camera_position of this CreateTTSAReq.
        :type camera_position: str
        """
        self._camera_position = camera_position

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
        if not isinstance(other, CreateTTSAReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
