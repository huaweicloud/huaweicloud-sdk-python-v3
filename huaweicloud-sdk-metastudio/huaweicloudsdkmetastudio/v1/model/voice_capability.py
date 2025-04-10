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
        'is_support_word': 'bool',
        'is_support_voice_cache': 'bool',
        'conversion_rate': 'float',
        'conversion_rate_en': 'float',
        'is_support_srt': 'bool'
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
        'is_support_word': 'is_support_word',
        'is_support_voice_cache': 'is_support_voice_cache',
        'conversion_rate': 'conversion_rate',
        'conversion_rate_en': 'conversion_rate_en',
        'is_support_srt': 'is_support_srt'
    }

    def __init__(self, is_support_phoneme_en=None, is_support_phoneme=None, is_support_break_time=None, is_support_break_strength=None, is_support_speed=None, is_support_prosody=None, is_support_ssml_say_as=None, is_support_ssml_sub=None, is_support_word=None, is_support_voice_cache=None, conversion_rate=None, conversion_rate_en=None, is_support_srt=None):
        r"""VoiceCapability

        The model defined in huaweicloud sdk

        :param is_support_phoneme_en: **参数解释**： 该声音是否支持英文音标。 **约束限制**： 不涉及 **取值范围**： * true: 支持英文音标 * false: 不支持英文音标
        :type is_support_phoneme_en: bool
        :param is_support_phoneme: **参数解释**： 该声音是否支持中文多音字。 **约束限制**： 不涉及 **取值范围**： * true: 支持中文多音字 * false: 不支持中文多音字
        :type is_support_phoneme: bool
        :param is_support_break_time: **参数解释**： 该声音是否支持停顿。 **约束限制**： 不涉及 **取值范围**： * true: 支持停顿 * false: 不支持停顿
        :type is_support_break_time: bool
        :param is_support_break_strength: **参数解释**： 该声音是否支持韵律。 **约束限制**： 不涉及 **取值范围**： * true: 支持韵律 * false: 不支持韵律
        :type is_support_break_strength: bool
        :param is_support_speed: **参数解释**： 该声音是否支持全局语速。 **约束限制**： 不涉及 **取值范围**： * true: 支持全局语速 * false: 不支持全局语速
        :type is_support_speed: bool
        :param is_support_prosody: **参数解释**： 该声音是否支持局部语速。 **约束限制**： 不涉及 **取值范围**： * true: 支持局部语速 * false: 不支持局部语速
        :type is_support_prosody: bool
        :param is_support_ssml_say_as: **参数解释**： 该声音是否支持SSML的say-as标签。 **约束限制**： 不涉及 **取值范围**： * true: 支持SSML的say-as标签 * false: 不支持SSML的say-as标签
        :type is_support_ssml_say_as: bool
        :param is_support_ssml_sub: **参数解释**： 该声音是否支持SSML的sub标签。 **约束限制**： 不涉及 **取值范围**： * true: 支持SSML的sub标签 * false: 不支持SSML的sub标签
        :type is_support_ssml_sub: bool
        :param is_support_word: **参数解释**： 该声音是否支持连读。 **约束限制**： 不涉及 **取值范围**： * true: 支持连读 * false: 不支持连读
        :type is_support_word: bool
        :param is_support_voice_cache: 是否支持缓存。
        :type is_support_voice_cache: bool
        :param conversion_rate: **参数解释**： 合成率。 **约束限制**： 不涉及 **取值范围**： * 0-50
        :type conversion_rate: float
        :param conversion_rate_en: **参数解释**： 英语的合成率。 **约束限制**： 不涉及 **取值范围**： * 0-50
        :type conversion_rate_en: float
        :param is_support_srt: 是否支持生成STR字幕文件。
        :type is_support_srt: bool
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
        self._is_support_voice_cache = None
        self._conversion_rate = None
        self._conversion_rate_en = None
        self._is_support_srt = None
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
        if is_support_voice_cache is not None:
            self.is_support_voice_cache = is_support_voice_cache
        if conversion_rate is not None:
            self.conversion_rate = conversion_rate
        if conversion_rate_en is not None:
            self.conversion_rate_en = conversion_rate_en
        if is_support_srt is not None:
            self.is_support_srt = is_support_srt

    @property
    def is_support_phoneme_en(self):
        r"""Gets the is_support_phoneme_en of this VoiceCapability.

        **参数解释**： 该声音是否支持英文音标。 **约束限制**： 不涉及 **取值范围**： * true: 支持英文音标 * false: 不支持英文音标

        :return: The is_support_phoneme_en of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_phoneme_en

    @is_support_phoneme_en.setter
    def is_support_phoneme_en(self, is_support_phoneme_en):
        r"""Sets the is_support_phoneme_en of this VoiceCapability.

        **参数解释**： 该声音是否支持英文音标。 **约束限制**： 不涉及 **取值范围**： * true: 支持英文音标 * false: 不支持英文音标

        :param is_support_phoneme_en: The is_support_phoneme_en of this VoiceCapability.
        :type is_support_phoneme_en: bool
        """
        self._is_support_phoneme_en = is_support_phoneme_en

    @property
    def is_support_phoneme(self):
        r"""Gets the is_support_phoneme of this VoiceCapability.

        **参数解释**： 该声音是否支持中文多音字。 **约束限制**： 不涉及 **取值范围**： * true: 支持中文多音字 * false: 不支持中文多音字

        :return: The is_support_phoneme of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_phoneme

    @is_support_phoneme.setter
    def is_support_phoneme(self, is_support_phoneme):
        r"""Sets the is_support_phoneme of this VoiceCapability.

        **参数解释**： 该声音是否支持中文多音字。 **约束限制**： 不涉及 **取值范围**： * true: 支持中文多音字 * false: 不支持中文多音字

        :param is_support_phoneme: The is_support_phoneme of this VoiceCapability.
        :type is_support_phoneme: bool
        """
        self._is_support_phoneme = is_support_phoneme

    @property
    def is_support_break_time(self):
        r"""Gets the is_support_break_time of this VoiceCapability.

        **参数解释**： 该声音是否支持停顿。 **约束限制**： 不涉及 **取值范围**： * true: 支持停顿 * false: 不支持停顿

        :return: The is_support_break_time of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_break_time

    @is_support_break_time.setter
    def is_support_break_time(self, is_support_break_time):
        r"""Sets the is_support_break_time of this VoiceCapability.

        **参数解释**： 该声音是否支持停顿。 **约束限制**： 不涉及 **取值范围**： * true: 支持停顿 * false: 不支持停顿

        :param is_support_break_time: The is_support_break_time of this VoiceCapability.
        :type is_support_break_time: bool
        """
        self._is_support_break_time = is_support_break_time

    @property
    def is_support_break_strength(self):
        r"""Gets the is_support_break_strength of this VoiceCapability.

        **参数解释**： 该声音是否支持韵律。 **约束限制**： 不涉及 **取值范围**： * true: 支持韵律 * false: 不支持韵律

        :return: The is_support_break_strength of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_break_strength

    @is_support_break_strength.setter
    def is_support_break_strength(self, is_support_break_strength):
        r"""Sets the is_support_break_strength of this VoiceCapability.

        **参数解释**： 该声音是否支持韵律。 **约束限制**： 不涉及 **取值范围**： * true: 支持韵律 * false: 不支持韵律

        :param is_support_break_strength: The is_support_break_strength of this VoiceCapability.
        :type is_support_break_strength: bool
        """
        self._is_support_break_strength = is_support_break_strength

    @property
    def is_support_speed(self):
        r"""Gets the is_support_speed of this VoiceCapability.

        **参数解释**： 该声音是否支持全局语速。 **约束限制**： 不涉及 **取值范围**： * true: 支持全局语速 * false: 不支持全局语速

        :return: The is_support_speed of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_speed

    @is_support_speed.setter
    def is_support_speed(self, is_support_speed):
        r"""Sets the is_support_speed of this VoiceCapability.

        **参数解释**： 该声音是否支持全局语速。 **约束限制**： 不涉及 **取值范围**： * true: 支持全局语速 * false: 不支持全局语速

        :param is_support_speed: The is_support_speed of this VoiceCapability.
        :type is_support_speed: bool
        """
        self._is_support_speed = is_support_speed

    @property
    def is_support_prosody(self):
        r"""Gets the is_support_prosody of this VoiceCapability.

        **参数解释**： 该声音是否支持局部语速。 **约束限制**： 不涉及 **取值范围**： * true: 支持局部语速 * false: 不支持局部语速

        :return: The is_support_prosody of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_prosody

    @is_support_prosody.setter
    def is_support_prosody(self, is_support_prosody):
        r"""Sets the is_support_prosody of this VoiceCapability.

        **参数解释**： 该声音是否支持局部语速。 **约束限制**： 不涉及 **取值范围**： * true: 支持局部语速 * false: 不支持局部语速

        :param is_support_prosody: The is_support_prosody of this VoiceCapability.
        :type is_support_prosody: bool
        """
        self._is_support_prosody = is_support_prosody

    @property
    def is_support_ssml_say_as(self):
        r"""Gets the is_support_ssml_say_as of this VoiceCapability.

        **参数解释**： 该声音是否支持SSML的say-as标签。 **约束限制**： 不涉及 **取值范围**： * true: 支持SSML的say-as标签 * false: 不支持SSML的say-as标签

        :return: The is_support_ssml_say_as of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_ssml_say_as

    @is_support_ssml_say_as.setter
    def is_support_ssml_say_as(self, is_support_ssml_say_as):
        r"""Sets the is_support_ssml_say_as of this VoiceCapability.

        **参数解释**： 该声音是否支持SSML的say-as标签。 **约束限制**： 不涉及 **取值范围**： * true: 支持SSML的say-as标签 * false: 不支持SSML的say-as标签

        :param is_support_ssml_say_as: The is_support_ssml_say_as of this VoiceCapability.
        :type is_support_ssml_say_as: bool
        """
        self._is_support_ssml_say_as = is_support_ssml_say_as

    @property
    def is_support_ssml_sub(self):
        r"""Gets the is_support_ssml_sub of this VoiceCapability.

        **参数解释**： 该声音是否支持SSML的sub标签。 **约束限制**： 不涉及 **取值范围**： * true: 支持SSML的sub标签 * false: 不支持SSML的sub标签

        :return: The is_support_ssml_sub of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_ssml_sub

    @is_support_ssml_sub.setter
    def is_support_ssml_sub(self, is_support_ssml_sub):
        r"""Sets the is_support_ssml_sub of this VoiceCapability.

        **参数解释**： 该声音是否支持SSML的sub标签。 **约束限制**： 不涉及 **取值范围**： * true: 支持SSML的sub标签 * false: 不支持SSML的sub标签

        :param is_support_ssml_sub: The is_support_ssml_sub of this VoiceCapability.
        :type is_support_ssml_sub: bool
        """
        self._is_support_ssml_sub = is_support_ssml_sub

    @property
    def is_support_word(self):
        r"""Gets the is_support_word of this VoiceCapability.

        **参数解释**： 该声音是否支持连读。 **约束限制**： 不涉及 **取值范围**： * true: 支持连读 * false: 不支持连读

        :return: The is_support_word of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_word

    @is_support_word.setter
    def is_support_word(self, is_support_word):
        r"""Sets the is_support_word of this VoiceCapability.

        **参数解释**： 该声音是否支持连读。 **约束限制**： 不涉及 **取值范围**： * true: 支持连读 * false: 不支持连读

        :param is_support_word: The is_support_word of this VoiceCapability.
        :type is_support_word: bool
        """
        self._is_support_word = is_support_word

    @property
    def is_support_voice_cache(self):
        r"""Gets the is_support_voice_cache of this VoiceCapability.

        是否支持缓存。

        :return: The is_support_voice_cache of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_voice_cache

    @is_support_voice_cache.setter
    def is_support_voice_cache(self, is_support_voice_cache):
        r"""Sets the is_support_voice_cache of this VoiceCapability.

        是否支持缓存。

        :param is_support_voice_cache: The is_support_voice_cache of this VoiceCapability.
        :type is_support_voice_cache: bool
        """
        self._is_support_voice_cache = is_support_voice_cache

    @property
    def conversion_rate(self):
        r"""Gets the conversion_rate of this VoiceCapability.

        **参数解释**： 合成率。 **约束限制**： 不涉及 **取值范围**： * 0-50

        :return: The conversion_rate of this VoiceCapability.
        :rtype: float
        """
        return self._conversion_rate

    @conversion_rate.setter
    def conversion_rate(self, conversion_rate):
        r"""Sets the conversion_rate of this VoiceCapability.

        **参数解释**： 合成率。 **约束限制**： 不涉及 **取值范围**： * 0-50

        :param conversion_rate: The conversion_rate of this VoiceCapability.
        :type conversion_rate: float
        """
        self._conversion_rate = conversion_rate

    @property
    def conversion_rate_en(self):
        r"""Gets the conversion_rate_en of this VoiceCapability.

        **参数解释**： 英语的合成率。 **约束限制**： 不涉及 **取值范围**： * 0-50

        :return: The conversion_rate_en of this VoiceCapability.
        :rtype: float
        """
        return self._conversion_rate_en

    @conversion_rate_en.setter
    def conversion_rate_en(self, conversion_rate_en):
        r"""Sets the conversion_rate_en of this VoiceCapability.

        **参数解释**： 英语的合成率。 **约束限制**： 不涉及 **取值范围**： * 0-50

        :param conversion_rate_en: The conversion_rate_en of this VoiceCapability.
        :type conversion_rate_en: float
        """
        self._conversion_rate_en = conversion_rate_en

    @property
    def is_support_srt(self):
        r"""Gets the is_support_srt of this VoiceCapability.

        是否支持生成STR字幕文件。

        :return: The is_support_srt of this VoiceCapability.
        :rtype: bool
        """
        return self._is_support_srt

    @is_support_srt.setter
    def is_support_srt(self, is_support_srt):
        r"""Sets the is_support_srt of this VoiceCapability.

        是否支持生成STR字幕文件。

        :param is_support_srt: The is_support_srt of this VoiceCapability.
        :type is_support_srt: bool
        """
        self._is_support_srt = is_support_srt

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
