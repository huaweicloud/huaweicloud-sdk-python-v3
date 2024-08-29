# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VoiceCapability:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_support_phoneme_en': 'bool',
        'is_support_phoneme': 'bool',
        'is_support_break_time': 'bool',
        'is_support_break_strength': 'bool',
        'is_support_speed': 'bool',
        'is_support_prosody': 'bool',
        'is_support_ssml_say_as': 'bool',
        'is_support_ssml_sub': 'bool',
        'is_support_word': 'bool'
    }

    attribute_map = {
        'is_support_phoneme_en': 'is_support_phoneme_en',
        'is_support_phoneme': 'is_support_phoneme',
        'is_support_break_time': 'is_support_break_time',
        'is_support_break_strength': 'is_support_break_strength',
        'is_support_speed': 'is_support_speed',
        'is_support_prosody': 'is_support_prosody',
        'is_support_ssml_say_as': 'is_support_ssml_say_as',
        'is_support_ssml_sub': 'is_support_ssml_sub',
        'is_support_word': 'is_support_word'
    }

    def __init__(self, is_support_phoneme_en=None, is_support_phoneme=None, is_support_break_time=None, is_support_break_strength=None, is_support_speed=None, is_support_prosody=None, is_support_ssml_say_as=None, is_support_ssml_sub=None, is_support_word=None):
        """VoiceCapability

        The model defined in huaweicloud sdk

        :param is_support_phoneme_en: 支持英文音标。
        :type is_support_phoneme_en: bool
        :param is_support_phoneme: 是否支持多音字。
        :type is_support_phoneme: bool
        :param is_support_break_time: 是否支持停顿。
        :type is_support_break_time: bool
        :param is_support_break_strength: 是否支持韵律。
        :type is_support_break_strength: bool
        :param is_support_speed: 是否支持全局语速。
        :type is_support_speed: bool
        :param is_support_prosody: 是否支持局部语速。
        :type is_support_prosody: bool
        :param is_support_ssml_say_as: 是否支持SSML的say-as标签。
        :type is_support_ssml_say_as: bool
        :param is_support_ssml_sub: 是否支持SSML的sub标签。
        :type is_support_ssml_sub: bool
        :param is_support_word: 是否支持连读。
        :type is_support_word: bool
        """
        
        

        self._is_support_phoneme_en = None
        self._is_support_phoneme = None
        self._is_support_break_time = None
        self._is_support_break_strength = None
        self._is_support_speed = None
        self._is_support_prosody = None
        self._is_support_ssml_say_as = None
        self._is_support_ssml_sub = None
        self._is_support_word = None
        self.discriminator = None

        if is_support_phoneme_en is not None:
            self.is_support_phoneme_en = is_support_phoneme_en
        if is_support_phoneme is not None:
            self.is_support_phoneme = is_support_phoneme
        if is_support_break_time is not None:
            self.is_support_break_time = is_support_break_time
        if is_support_break_strength is not None:
            self.is_support_break_strength = is_support_break_strength
        if is_support_speed is not None:
            self.is_support_speed = is_support_speed
        if is_support_prosody is not None:
            self.is_support_prosody = is_support_prosody
        if is_support_ssml_say_as is not None:
            self.is_support_ssml_say_as = is_support_ssml_say_as
        if is_support_ssml_sub is not None:
            self.is_support_ssml_sub = is_support_ssml_sub
        if is_support_word is not None:
            self.is_support_word = is_support_word

    @property
    def is_support_phoneme_en(self):
        """Gets the is_support_phoneme_en of this VoiceCapability.

        支持英文音标。

        :return: The is_support_phoneme_en of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_phoneme_en

    @is_support_phoneme_en.setter
    def is_support_phoneme_en(self, is_support_phoneme_en):
        """Sets the is_support_phoneme_en of this VoiceCapability.

        支持英文音标。

        :param is_support_phoneme_en: The is_support_phoneme_en of this VoiceCapability.
        :type is_support_phoneme_en: bool
        """
        self._is_support_phoneme_en = is_support_phoneme_en

    @property
    def is_support_phoneme(self):
        """Gets the is_support_phoneme of this VoiceCapability.

        是否支持多音字。

        :return: The is_support_phoneme of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_phoneme

    @is_support_phoneme.setter
    def is_support_phoneme(self, is_support_phoneme):
        """Sets the is_support_phoneme of this VoiceCapability.

        是否支持多音字。

        :param is_support_phoneme: The is_support_phoneme of this VoiceCapability.
        :type is_support_phoneme: bool
        """
        self._is_support_phoneme = is_support_phoneme

    @property
    def is_support_break_time(self):
        """Gets the is_support_break_time of this VoiceCapability.

        是否支持停顿。

        :return: The is_support_break_time of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_break_time

    @is_support_break_time.setter
    def is_support_break_time(self, is_support_break_time):
        """Sets the is_support_break_time of this VoiceCapability.

        是否支持停顿。

        :param is_support_break_time: The is_support_break_time of this VoiceCapability.
        :type is_support_break_time: bool
        """
        self._is_support_break_time = is_support_break_time

    @property
    def is_support_break_strength(self):
        """Gets the is_support_break_strength of this VoiceCapability.

        是否支持韵律。

        :return: The is_support_break_strength of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_break_strength

    @is_support_break_strength.setter
    def is_support_break_strength(self, is_support_break_strength):
        """Sets the is_support_break_strength of this VoiceCapability.

        是否支持韵律。

        :param is_support_break_strength: The is_support_break_strength of this VoiceCapability.
        :type is_support_break_strength: bool
        """
        self._is_support_break_strength = is_support_break_strength

    @property
    def is_support_speed(self):
        """Gets the is_support_speed of this VoiceCapability.

        是否支持全局语速。

        :return: The is_support_speed of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_speed

    @is_support_speed.setter
    def is_support_speed(self, is_support_speed):
        """Sets the is_support_speed of this VoiceCapability.

        是否支持全局语速。

        :param is_support_speed: The is_support_speed of this VoiceCapability.
        :type is_support_speed: bool
        """
        self._is_support_speed = is_support_speed

    @property
    def is_support_prosody(self):
        """Gets the is_support_prosody of this VoiceCapability.

        是否支持局部语速。

        :return: The is_support_prosody of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_prosody

    @is_support_prosody.setter
    def is_support_prosody(self, is_support_prosody):
        """Sets the is_support_prosody of this VoiceCapability.

        是否支持局部语速。

        :param is_support_prosody: The is_support_prosody of this VoiceCapability.
        :type is_support_prosody: bool
        """
        self._is_support_prosody = is_support_prosody

    @property
    def is_support_ssml_say_as(self):
        """Gets the is_support_ssml_say_as of this VoiceCapability.

        是否支持SSML的say-as标签。

        :return: The is_support_ssml_say_as of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_ssml_say_as

    @is_support_ssml_say_as.setter
    def is_support_ssml_say_as(self, is_support_ssml_say_as):
        """Sets the is_support_ssml_say_as of this VoiceCapability.

        是否支持SSML的say-as标签。

        :param is_support_ssml_say_as: The is_support_ssml_say_as of this VoiceCapability.
        :type is_support_ssml_say_as: bool
        """
        self._is_support_ssml_say_as = is_support_ssml_say_as

    @property
    def is_support_ssml_sub(self):
        """Gets the is_support_ssml_sub of this VoiceCapability.

        是否支持SSML的sub标签。

        :return: The is_support_ssml_sub of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_ssml_sub

    @is_support_ssml_sub.setter
    def is_support_ssml_sub(self, is_support_ssml_sub):
        """Sets the is_support_ssml_sub of this VoiceCapability.

        是否支持SSML的sub标签。

        :param is_support_ssml_sub: The is_support_ssml_sub of this VoiceCapability.
        :type is_support_ssml_sub: bool
        """
        self._is_support_ssml_sub = is_support_ssml_sub

    @property
    def is_support_word(self):
        """Gets the is_support_word of this VoiceCapability.

        是否支持连读。

        :return: The is_support_word of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_word

    @is_support_word.setter
    def is_support_word(self, is_support_word):
        """Sets the is_support_word of this VoiceCapability.

        是否支持连读。

        :param is_support_word: The is_support_word of this VoiceCapability.
        :type is_support_word: bool
        """
        self._is_support_word = is_support_word

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
        if not isinstance(other, VoiceCapability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
