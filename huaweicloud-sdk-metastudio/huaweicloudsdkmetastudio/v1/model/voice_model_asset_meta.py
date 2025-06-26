# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VoiceModelAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order': 'int',
        'model_type': 'str',
        'sex': 'str',
        'language': 'str',
        'languages': 'list[VoiceLanguage]',
        'speed_ratio': 'float',
        'volume_ratio': 'float',
        'is_realtime_voice': 'bool',
        'style': 'str',
        'voice_capability': 'VoiceCapability',
        'external_voice_meta': 'ExternalVoiceAssetMeta',
        'is_support_vc_process': 'bool',
        'is_support_thai_auto_split': 'bool',
        'is_flexus': 'bool',
        'is_enhance_rhythm': 'bool',
        'age': 'str'
    }

    attribute_map = {
        'order': 'order',
        'model_type': 'model_type',
        'sex': 'sex',
        'language': 'language',
        'languages': 'languages',
        'speed_ratio': 'speed_ratio',
        'volume_ratio': 'volume_ratio',
        'is_realtime_voice': 'is_realtime_voice',
        'style': 'style',
        'voice_capability': 'voice_capability',
        'external_voice_meta': 'external_voice_meta',
        'is_support_vc_process': 'is_support_vc_process',
        'is_support_thai_auto_split': 'is_support_thai_auto_split',
        'is_flexus': 'is_flexus',
        'is_enhance_rhythm': 'is_enhance_rhythm',
        'age': 'age'
    }

    def __init__(self, order=None, model_type=None, sex=None, language=None, languages=None, speed_ratio=None, volume_ratio=None, is_realtime_voice=None, style=None, voice_capability=None, external_voice_meta=None, is_support_vc_process=None, is_support_thai_auto_split=None, is_flexus=None, is_enhance_rhythm=None, age=None):
        r"""VoiceModelAssetMeta

        The model defined in huaweicloud sdk

        :param order: **参数解释**： 展示顺序。 **约束限制**： 不涉及。
        :type order: int
        :param model_type: **参数解释**： 声音资产类型。 **约束限制**： 不涉及。 **取值范围**： * COMMON：通用情感模型 * CLONE：语音克隆模型
        :type model_type: str
        :param sex: **参数解释**： 声音性别。 **约束限制**： 不涉及。 **取值范围**： * UNKNOW：未知性别声音 * MALE：男性声音 * FEMALE：女性声音
        :type sex: str
        :param language: **参数解释**： 声音语言。 **约束限制**： 不涉及。 **取值范围**： * UNKNOW：未知 * CN：中文 * EN：英文 * GER：德语 * fr：法语 * Kr：韩语 * por：葡萄牙语 * JPN：日语 * Ita：意大利语 * ESP：西班牙语 * DBH：东北话 * GT：港台 * GXH：广西话 * HBH：湖北话 * SXH：陕西话 * SCH：四川话 * YY：粤语 * Russian: 俄罗斯语 * Filipino: 菲律宾语 * Dutch: 荷兰语 * Indonesian: 印尼语 * Vietnamese: 越南语 * Arabic: 阿拉伯语 * Turkish: 土耳其语 * Malay: 马来语 * Thai: 泰语 * Finnish: 芬兰语
        :type language: str
        :param languages: **参数解释**： 声音语言。 **约束限制**： 不涉及。 **取值范围**： * UNKNOW：未知 * CN：中文 * EN：英文 * GER：德语 * fr：法语 * Kr：韩语 * por：葡萄牙语 * JPN：日语 * Ita：意大利语 * ESP：西班牙语 * DBH：东北话 * GT：港台 * GXH：广西话 * HBH：湖北话 * SXH：陕西话 * SCH：四川话 * YY：粤语 * Russian: 俄罗斯语 * Filipino: 菲律宾语 * Dutch: 荷兰语 * Indonesian: 印尼语 * Vietnamese: 越南语 * Arabic: 阿拉伯语 * Turkish: 土耳其语 * Malay: 马来语 * Thai: 泰语 * Finnish: 芬兰语
        :type languages: list[:class:`huaweicloudsdkmetastudio.v1.VoiceLanguage`]
        :param speed_ratio: **参数解释**： 语速缩放比例。 **约束限制**： 不涉及
        :type speed_ratio: float
        :param volume_ratio: **参数解释**： 音量缩放比例。 **约束限制**： 不涉及
        :type volume_ratio: float
        :param is_realtime_voice: **参数解释**： 该音色是否支持实时合成。 **约束限制**： 支持实时合成的音色，可以用于直播和智能交互场景。否则只能用于视频制作。 **取值范围**： * true: 支持实时合成 * false: 不支持实时合成
        :type is_realtime_voice: bool
        :param style: 风格参考
        :type style: str
        :param voice_capability: 
        :type voice_capability: :class:`huaweicloudsdkmetastudio.v1.VoiceCapability`
        :param external_voice_meta: 
        :type external_voice_meta: :class:`huaweicloudsdkmetastudio.v1.ExternalVoiceAssetMeta`
        :param is_support_vc_process: 是否支持vc。
        :type is_support_vc_process: bool
        :param is_support_thai_auto_split: 是否支持泰语文本自动分句。
        :type is_support_thai_auto_split: bool
        :param is_flexus: 是否是Flexus版本声音。
        :type is_flexus: bool
        :param is_enhance_rhythm: 是否增强韵律
        :type is_enhance_rhythm: bool
        :param age: 音色年龄段：青年、中年、老年
        :type age: str
        """
        
        

        self._order = None
        self._model_type = None
        self._sex = None
        self._language = None
        self._languages = None
        self._speed_ratio = None
        self._volume_ratio = None
        self._is_realtime_voice = None
        self._style = None
        self._voice_capability = None
        self._external_voice_meta = None
        self._is_support_vc_process = None
        self._is_support_thai_auto_split = None
        self._is_flexus = None
        self._is_enhance_rhythm = None
        self._age = None
        self.discriminator = None

        if order is not None:
            self.order = order
        if model_type is not None:
            self.model_type = model_type
        if sex is not None:
            self.sex = sex
        if language is not None:
            self.language = language
        if languages is not None:
            self.languages = languages
        if speed_ratio is not None:
            self.speed_ratio = speed_ratio
        if volume_ratio is not None:
            self.volume_ratio = volume_ratio
        if is_realtime_voice is not None:
            self.is_realtime_voice = is_realtime_voice
        if style is not None:
            self.style = style
        if voice_capability is not None:
            self.voice_capability = voice_capability
        if external_voice_meta is not None:
            self.external_voice_meta = external_voice_meta
        if is_support_vc_process is not None:
            self.is_support_vc_process = is_support_vc_process
        if is_support_thai_auto_split is not None:
            self.is_support_thai_auto_split = is_support_thai_auto_split
        if is_flexus is not None:
            self.is_flexus = is_flexus
        if is_enhance_rhythm is not None:
            self.is_enhance_rhythm = is_enhance_rhythm
        if age is not None:
            self.age = age

    @property
    def order(self):
        r"""Gets the order of this VoiceModelAssetMeta.

        **参数解释**： 展示顺序。 **约束限制**： 不涉及。

        :return: The order of this VoiceModelAssetMeta.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this VoiceModelAssetMeta.

        **参数解释**： 展示顺序。 **约束限制**： 不涉及。

        :param order: The order of this VoiceModelAssetMeta.
        :type order: int
        """
        self._order = order

    @property
    def model_type(self):
        r"""Gets the model_type of this VoiceModelAssetMeta.

        **参数解释**： 声音资产类型。 **约束限制**： 不涉及。 **取值范围**： * COMMON：通用情感模型 * CLONE：语音克隆模型

        :return: The model_type of this VoiceModelAssetMeta.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        r"""Sets the model_type of this VoiceModelAssetMeta.

        **参数解释**： 声音资产类型。 **约束限制**： 不涉及。 **取值范围**： * COMMON：通用情感模型 * CLONE：语音克隆模型

        :param model_type: The model_type of this VoiceModelAssetMeta.
        :type model_type: str
        """
        self._model_type = model_type

    @property
    def sex(self):
        r"""Gets the sex of this VoiceModelAssetMeta.

        **参数解释**： 声音性别。 **约束限制**： 不涉及。 **取值范围**： * UNKNOW：未知性别声音 * MALE：男性声音 * FEMALE：女性声音

        :return: The sex of this VoiceModelAssetMeta.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this VoiceModelAssetMeta.

        **参数解释**： 声音性别。 **约束限制**： 不涉及。 **取值范围**： * UNKNOW：未知性别声音 * MALE：男性声音 * FEMALE：女性声音

        :param sex: The sex of this VoiceModelAssetMeta.
        :type sex: str
        """
        self._sex = sex

    @property
    def language(self):
        r"""Gets the language of this VoiceModelAssetMeta.

        **参数解释**： 声音语言。 **约束限制**： 不涉及。 **取值范围**： * UNKNOW：未知 * CN：中文 * EN：英文 * GER：德语 * fr：法语 * Kr：韩语 * por：葡萄牙语 * JPN：日语 * Ita：意大利语 * ESP：西班牙语 * DBH：东北话 * GT：港台 * GXH：广西话 * HBH：湖北话 * SXH：陕西话 * SCH：四川话 * YY：粤语 * Russian: 俄罗斯语 * Filipino: 菲律宾语 * Dutch: 荷兰语 * Indonesian: 印尼语 * Vietnamese: 越南语 * Arabic: 阿拉伯语 * Turkish: 土耳其语 * Malay: 马来语 * Thai: 泰语 * Finnish: 芬兰语

        :return: The language of this VoiceModelAssetMeta.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this VoiceModelAssetMeta.

        **参数解释**： 声音语言。 **约束限制**： 不涉及。 **取值范围**： * UNKNOW：未知 * CN：中文 * EN：英文 * GER：德语 * fr：法语 * Kr：韩语 * por：葡萄牙语 * JPN：日语 * Ita：意大利语 * ESP：西班牙语 * DBH：东北话 * GT：港台 * GXH：广西话 * HBH：湖北话 * SXH：陕西话 * SCH：四川话 * YY：粤语 * Russian: 俄罗斯语 * Filipino: 菲律宾语 * Dutch: 荷兰语 * Indonesian: 印尼语 * Vietnamese: 越南语 * Arabic: 阿拉伯语 * Turkish: 土耳其语 * Malay: 马来语 * Thai: 泰语 * Finnish: 芬兰语

        :param language: The language of this VoiceModelAssetMeta.
        :type language: str
        """
        self._language = language

    @property
    def languages(self):
        r"""Gets the languages of this VoiceModelAssetMeta.

        **参数解释**： 声音语言。 **约束限制**： 不涉及。 **取值范围**： * UNKNOW：未知 * CN：中文 * EN：英文 * GER：德语 * fr：法语 * Kr：韩语 * por：葡萄牙语 * JPN：日语 * Ita：意大利语 * ESP：西班牙语 * DBH：东北话 * GT：港台 * GXH：广西话 * HBH：湖北话 * SXH：陕西话 * SCH：四川话 * YY：粤语 * Russian: 俄罗斯语 * Filipino: 菲律宾语 * Dutch: 荷兰语 * Indonesian: 印尼语 * Vietnamese: 越南语 * Arabic: 阿拉伯语 * Turkish: 土耳其语 * Malay: 马来语 * Thai: 泰语 * Finnish: 芬兰语

        :return: The languages of this VoiceModelAssetMeta.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.VoiceLanguage`]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        r"""Sets the languages of this VoiceModelAssetMeta.

        **参数解释**： 声音语言。 **约束限制**： 不涉及。 **取值范围**： * UNKNOW：未知 * CN：中文 * EN：英文 * GER：德语 * fr：法语 * Kr：韩语 * por：葡萄牙语 * JPN：日语 * Ita：意大利语 * ESP：西班牙语 * DBH：东北话 * GT：港台 * GXH：广西话 * HBH：湖北话 * SXH：陕西话 * SCH：四川话 * YY：粤语 * Russian: 俄罗斯语 * Filipino: 菲律宾语 * Dutch: 荷兰语 * Indonesian: 印尼语 * Vietnamese: 越南语 * Arabic: 阿拉伯语 * Turkish: 土耳其语 * Malay: 马来语 * Thai: 泰语 * Finnish: 芬兰语

        :param languages: The languages of this VoiceModelAssetMeta.
        :type languages: list[:class:`huaweicloudsdkmetastudio.v1.VoiceLanguage`]
        """
        self._languages = languages

    @property
    def speed_ratio(self):
        r"""Gets the speed_ratio of this VoiceModelAssetMeta.

        **参数解释**： 语速缩放比例。 **约束限制**： 不涉及

        :return: The speed_ratio of this VoiceModelAssetMeta.
        :rtype: float
        """
        return self._speed_ratio

    @speed_ratio.setter
    def speed_ratio(self, speed_ratio):
        r"""Sets the speed_ratio of this VoiceModelAssetMeta.

        **参数解释**： 语速缩放比例。 **约束限制**： 不涉及

        :param speed_ratio: The speed_ratio of this VoiceModelAssetMeta.
        :type speed_ratio: float
        """
        self._speed_ratio = speed_ratio

    @property
    def volume_ratio(self):
        r"""Gets the volume_ratio of this VoiceModelAssetMeta.

        **参数解释**： 音量缩放比例。 **约束限制**： 不涉及

        :return: The volume_ratio of this VoiceModelAssetMeta.
        :rtype: float
        """
        return self._volume_ratio

    @volume_ratio.setter
    def volume_ratio(self, volume_ratio):
        r"""Sets the volume_ratio of this VoiceModelAssetMeta.

        **参数解释**： 音量缩放比例。 **约束限制**： 不涉及

        :param volume_ratio: The volume_ratio of this VoiceModelAssetMeta.
        :type volume_ratio: float
        """
        self._volume_ratio = volume_ratio

    @property
    def is_realtime_voice(self):
        r"""Gets the is_realtime_voice of this VoiceModelAssetMeta.

        **参数解释**： 该音色是否支持实时合成。 **约束限制**： 支持实时合成的音色，可以用于直播和智能交互场景。否则只能用于视频制作。 **取值范围**： * true: 支持实时合成 * false: 不支持实时合成

        :return: The is_realtime_voice of this VoiceModelAssetMeta.
        :rtype: bool
        """
        return self._is_realtime_voice

    @is_realtime_voice.setter
    def is_realtime_voice(self, is_realtime_voice):
        r"""Sets the is_realtime_voice of this VoiceModelAssetMeta.

        **参数解释**： 该音色是否支持实时合成。 **约束限制**： 支持实时合成的音色，可以用于直播和智能交互场景。否则只能用于视频制作。 **取值范围**： * true: 支持实时合成 * false: 不支持实时合成

        :param is_realtime_voice: The is_realtime_voice of this VoiceModelAssetMeta.
        :type is_realtime_voice: bool
        """
        self._is_realtime_voice = is_realtime_voice

    @property
    def style(self):
        r"""Gets the style of this VoiceModelAssetMeta.

        风格参考

        :return: The style of this VoiceModelAssetMeta.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style):
        r"""Sets the style of this VoiceModelAssetMeta.

        风格参考

        :param style: The style of this VoiceModelAssetMeta.
        :type style: str
        """
        self._style = style

    @property
    def voice_capability(self):
        r"""Gets the voice_capability of this VoiceModelAssetMeta.

        :return: The voice_capability of this VoiceModelAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceCapability`
        """
        return self._voice_capability

    @voice_capability.setter
    def voice_capability(self, voice_capability):
        r"""Sets the voice_capability of this VoiceModelAssetMeta.

        :param voice_capability: The voice_capability of this VoiceModelAssetMeta.
        :type voice_capability: :class:`huaweicloudsdkmetastudio.v1.VoiceCapability`
        """
        self._voice_capability = voice_capability

    @property
    def external_voice_meta(self):
        r"""Gets the external_voice_meta of this VoiceModelAssetMeta.

        :return: The external_voice_meta of this VoiceModelAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ExternalVoiceAssetMeta`
        """
        return self._external_voice_meta

    @external_voice_meta.setter
    def external_voice_meta(self, external_voice_meta):
        r"""Sets the external_voice_meta of this VoiceModelAssetMeta.

        :param external_voice_meta: The external_voice_meta of this VoiceModelAssetMeta.
        :type external_voice_meta: :class:`huaweicloudsdkmetastudio.v1.ExternalVoiceAssetMeta`
        """
        self._external_voice_meta = external_voice_meta

    @property
    def is_support_vc_process(self):
        r"""Gets the is_support_vc_process of this VoiceModelAssetMeta.

        是否支持vc。

        :return: The is_support_vc_process of this VoiceModelAssetMeta.
        :rtype: bool
        """
        return self._is_support_vc_process

    @is_support_vc_process.setter
    def is_support_vc_process(self, is_support_vc_process):
        r"""Sets the is_support_vc_process of this VoiceModelAssetMeta.

        是否支持vc。

        :param is_support_vc_process: The is_support_vc_process of this VoiceModelAssetMeta.
        :type is_support_vc_process: bool
        """
        self._is_support_vc_process = is_support_vc_process

    @property
    def is_support_thai_auto_split(self):
        r"""Gets the is_support_thai_auto_split of this VoiceModelAssetMeta.

        是否支持泰语文本自动分句。

        :return: The is_support_thai_auto_split of this VoiceModelAssetMeta.
        :rtype: bool
        """
        return self._is_support_thai_auto_split

    @is_support_thai_auto_split.setter
    def is_support_thai_auto_split(self, is_support_thai_auto_split):
        r"""Sets the is_support_thai_auto_split of this VoiceModelAssetMeta.

        是否支持泰语文本自动分句。

        :param is_support_thai_auto_split: The is_support_thai_auto_split of this VoiceModelAssetMeta.
        :type is_support_thai_auto_split: bool
        """
        self._is_support_thai_auto_split = is_support_thai_auto_split

    @property
    def is_flexus(self):
        r"""Gets the is_flexus of this VoiceModelAssetMeta.

        是否是Flexus版本声音。

        :return: The is_flexus of this VoiceModelAssetMeta.
        :rtype: bool
        """
        return self._is_flexus

    @is_flexus.setter
    def is_flexus(self, is_flexus):
        r"""Sets the is_flexus of this VoiceModelAssetMeta.

        是否是Flexus版本声音。

        :param is_flexus: The is_flexus of this VoiceModelAssetMeta.
        :type is_flexus: bool
        """
        self._is_flexus = is_flexus

    @property
    def is_enhance_rhythm(self):
        r"""Gets the is_enhance_rhythm of this VoiceModelAssetMeta.

        是否增强韵律

        :return: The is_enhance_rhythm of this VoiceModelAssetMeta.
        :rtype: bool
        """
        return self._is_enhance_rhythm

    @is_enhance_rhythm.setter
    def is_enhance_rhythm(self, is_enhance_rhythm):
        r"""Sets the is_enhance_rhythm of this VoiceModelAssetMeta.

        是否增强韵律

        :param is_enhance_rhythm: The is_enhance_rhythm of this VoiceModelAssetMeta.
        :type is_enhance_rhythm: bool
        """
        self._is_enhance_rhythm = is_enhance_rhythm

    @property
    def age(self):
        r"""Gets the age of this VoiceModelAssetMeta.

        音色年龄段：青年、中年、老年

        :return: The age of this VoiceModelAssetMeta.
        :rtype: str
        """
        return self._age

    @age.setter
    def age(self, age):
        r"""Sets the age of this VoiceModelAssetMeta.

        音色年龄段：青年、中年、老年

        :param age: The age of this VoiceModelAssetMeta.
        :type age: str
        """
        self._age = age

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
        if not isinstance(other, VoiceModelAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
