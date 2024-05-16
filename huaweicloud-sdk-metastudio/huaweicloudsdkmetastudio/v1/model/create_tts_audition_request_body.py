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
        'emotion': 'str',
        'speed': 'int',
        'pitch': 'int',
        'volume': 'int'
    }

    attribute_map = {
        'text': 'text',
        'emotion': 'emotion',
        'speed': 'speed',
        'pitch': 'pitch',
        'volume': 'volume'
    }

    def __init__(self, text=None, emotion=None, speed=None, pitch=None, volume=None):
        """CreateTtsAuditionRequestBody

        The model defined in huaweicloud sdk

        :param text: 待合成文本。
        :type text: str
        :param emotion: 音色ID。
        :type emotion: str
        :param speed: 语速。 默认值100，最小值50，最大值200。 &gt; * 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。 &gt; * 50表示0.5倍语速，100表示正常语速，200表示2倍语速。
        :type speed: int
        :param pitch: 音高。 默认值100，最小值50，最大值200。
        :type pitch: int
        :param volume: 音量。 默认值140，最小值90，最大值240。
        :type volume: int
        """
        
        

        self._text = None
        self._emotion = None
        self._speed = None
        self._pitch = None
        self._volume = None
        self.discriminator = None

        self.text = text
        self.emotion = emotion
        if speed is not None:
            self.speed = speed
        if pitch is not None:
            self.pitch = pitch
        if volume is not None:
            self.volume = volume

    @property
    def text(self):
        """Gets the text of this CreateTtsAuditionRequestBody.

        待合成文本。

        :return: The text of this CreateTtsAuditionRequestBody.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CreateTtsAuditionRequestBody.

        待合成文本。

        :param text: The text of this CreateTtsAuditionRequestBody.
        :type text: str
        """
        self._text = text

    @property
    def emotion(self):
        """Gets the emotion of this CreateTtsAuditionRequestBody.

        音色ID。

        :return: The emotion of this CreateTtsAuditionRequestBody.
        :rtype: str
        """
        return self._emotion

    @emotion.setter
    def emotion(self, emotion):
        """Sets the emotion of this CreateTtsAuditionRequestBody.

        音色ID。

        :param emotion: The emotion of this CreateTtsAuditionRequestBody.
        :type emotion: str
        """
        self._emotion = emotion

    @property
    def speed(self):
        """Gets the speed of this CreateTtsAuditionRequestBody.

        语速。 默认值100，最小值50，最大值200。 > * 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。 > * 50表示0.5倍语速，100表示正常语速，200表示2倍语速。

        :return: The speed of this CreateTtsAuditionRequestBody.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this CreateTtsAuditionRequestBody.

        语速。 默认值100，最小值50，最大值200。 > * 当取值为“100”时，表示一个成年人正常的语速，约为250字/分钟。 > * 50表示0.5倍语速，100表示正常语速，200表示2倍语速。

        :param speed: The speed of this CreateTtsAuditionRequestBody.
        :type speed: int
        """
        self._speed = speed

    @property
    def pitch(self):
        """Gets the pitch of this CreateTtsAuditionRequestBody.

        音高。 默认值100，最小值50，最大值200。

        :return: The pitch of this CreateTtsAuditionRequestBody.
        :rtype: int
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        """Sets the pitch of this CreateTtsAuditionRequestBody.

        音高。 默认值100，最小值50，最大值200。

        :param pitch: The pitch of this CreateTtsAuditionRequestBody.
        :type pitch: int
        """
        self._pitch = pitch

    @property
    def volume(self):
        """Gets the volume of this CreateTtsAuditionRequestBody.

        音量。 默认值140，最小值90，最大值240。

        :return: The volume of this CreateTtsAuditionRequestBody.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this CreateTtsAuditionRequestBody.

        音量。 默认值140，最小值90，最大值240。

        :param volume: The volume of this CreateTtsAuditionRequestBody.
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
        if not isinstance(other, CreateTtsAuditionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
