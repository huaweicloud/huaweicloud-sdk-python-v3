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
        'speed_ratio': 'float',
        'volume_ratio': 'float',
        'is_realtime_voice': 'bool',
        'voice_capability': 'VoiceCapability',
        'external_voice_meta': 'ExternalVoiceAssetMeta',
        'is_support_vc_process': 'bool',
        'is_flexus': 'bool'
    }

    attribute_map = {
        'order': 'order',
        'model_type': 'model_type',
        'sex': 'sex',
        'language': 'language',
        'speed_ratio': 'speed_ratio',
        'volume_ratio': 'volume_ratio',
        'is_realtime_voice': 'is_realtime_voice',
        'voice_capability': 'voice_capability',
        'external_voice_meta': 'external_voice_meta',
        'is_support_vc_process': 'is_support_vc_process',
        'is_flexus': 'is_flexus'
    }

    def __init__(self, order=None, model_type=None, sex=None, language=None, speed_ratio=None, volume_ratio=None, is_realtime_voice=None, voice_capability=None, external_voice_meta=None, is_support_vc_process=None, is_flexus=None):
        """VoiceModelAssetMeta

        The model defined in huaweicloud sdk

        :param order: 展示顺序
        :type order: int
        :param model_type: 音色资产类型。 * COMMON：通用情感模型 * CLONE：语音克隆模型
        :type model_type: str
        :param sex: 音色性别。 * UNKNOW：中性音色 * MALE：男性音色 * FEMALE：女性音色  默认UNKNOW。
        :type sex: str
        :param language: 音色语言。 * UNKNOW：未知 * CN：中文 * EN：英文 * GER：德语 * fr：法语 * Kr：韩语 * por：葡萄牙语 * JPN：日语 * Ita：意大利语 * ESP：西班牙语 * DBH：东北话 * GT：港台 * GXH：广西话 * HBH：湖北话 * SXH：陕西话 * SCH：四川话 * YY：粤语 * Russian: 俄罗斯语 * Filipino: 菲律宾语 * Dutch: 荷兰语 * Indonesian: 印尼语 * Vietnamese: 越南语 * Arabic: 阿拉伯语 * Turkish: 土耳其语 * Malay: 马来语 * Thai: 泰语 * Finnish: 芬兰语  默认UNKNOW。
        :type language: str
        :param speed_ratio: 语速缩放比例
        :type speed_ratio: float
        :param volume_ratio: 音量缩放比例
        :type volume_ratio: float
        :param is_realtime_voice: 该音色是否支持实时合成，默认是true。 &gt; * 支持实时合成的音色，可以用于直播和智能交互场景。否则只能用于视频制作。
        :type is_realtime_voice: bool
        :param voice_capability: 
        :type voice_capability: :class:`huaweicloudsdkmetastudio.v1.VoiceCapability`
        :param external_voice_meta: 
        :type external_voice_meta: :class:`huaweicloudsdkmetastudio.v1.ExternalVoiceAssetMeta`
        :param is_support_vc_process: 是否支持vc。
        :type is_support_vc_process: bool
        :param is_flexus: 是否是Flexus版本声音。
        :type is_flexus: bool
        """
        
        

        self._order = None
        self._model_type = None
        self._sex = None
        self._language = None
        self._speed_ratio = None
        self._volume_ratio = None
        self._is_realtime_voice = None
        self._voice_capability = None
        self._external_voice_meta = None
        self._is_support_vc_process = None
        self._is_flexus = None
        self.discriminator = None

        if order is not None:
            self.order = order
        if model_type is not None:
            self.model_type = model_type
        if sex is not None:
            self.sex = sex
        if language is not None:
            self.language = language
        if speed_ratio is not None:
            self.speed_ratio = speed_ratio
        if volume_ratio is not None:
            self.volume_ratio = volume_ratio
        if is_realtime_voice is not None:
            self.is_realtime_voice = is_realtime_voice
        if voice_capability is not None:
            self.voice_capability = voice_capability
        if external_voice_meta is not None:
            self.external_voice_meta = external_voice_meta
        if is_support_vc_process is not None:
            self.is_support_vc_process = is_support_vc_process
        if is_flexus is not None:
            self.is_flexus = is_flexus

    @property
    def order(self):
        """Gets the order of this VoiceModelAssetMeta.

        展示顺序

        :return: The order of this VoiceModelAssetMeta.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this VoiceModelAssetMeta.

        展示顺序

        :param order: The order of this VoiceModelAssetMeta.
        :type order: int
        """
        self._order = order

    @property
    def model_type(self):
        """Gets the model_type of this VoiceModelAssetMeta.

        音色资产类型。 * COMMON：通用情感模型 * CLONE：语音克隆模型

        :return: The model_type of this VoiceModelAssetMeta.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this VoiceModelAssetMeta.

        音色资产类型。 * COMMON：通用情感模型 * CLONE：语音克隆模型

        :param model_type: The model_type of this VoiceModelAssetMeta.
        :type model_type: str
        """
        self._model_type = model_type

    @property
    def sex(self):
        """Gets the sex of this VoiceModelAssetMeta.

        音色性别。 * UNKNOW：中性音色 * MALE：男性音色 * FEMALE：女性音色  默认UNKNOW。

        :return: The sex of this VoiceModelAssetMeta.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this VoiceModelAssetMeta.

        音色性别。 * UNKNOW：中性音色 * MALE：男性音色 * FEMALE：女性音色  默认UNKNOW。

        :param sex: The sex of this VoiceModelAssetMeta.
        :type sex: str
        """
        self._sex = sex

    @property
    def language(self):
        """Gets the language of this VoiceModelAssetMeta.

        音色语言。 * UNKNOW：未知 * CN：中文 * EN：英文 * GER：德语 * fr：法语 * Kr：韩语 * por：葡萄牙语 * JPN：日语 * Ita：意大利语 * ESP：西班牙语 * DBH：东北话 * GT：港台 * GXH：广西话 * HBH：湖北话 * SXH：陕西话 * SCH：四川话 * YY：粤语 * Russian: 俄罗斯语 * Filipino: 菲律宾语 * Dutch: 荷兰语 * Indonesian: 印尼语 * Vietnamese: 越南语 * Arabic: 阿拉伯语 * Turkish: 土耳其语 * Malay: 马来语 * Thai: 泰语 * Finnish: 芬兰语  默认UNKNOW。

        :return: The language of this VoiceModelAssetMeta.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this VoiceModelAssetMeta.

        音色语言。 * UNKNOW：未知 * CN：中文 * EN：英文 * GER：德语 * fr：法语 * Kr：韩语 * por：葡萄牙语 * JPN：日语 * Ita：意大利语 * ESP：西班牙语 * DBH：东北话 * GT：港台 * GXH：广西话 * HBH：湖北话 * SXH：陕西话 * SCH：四川话 * YY：粤语 * Russian: 俄罗斯语 * Filipino: 菲律宾语 * Dutch: 荷兰语 * Indonesian: 印尼语 * Vietnamese: 越南语 * Arabic: 阿拉伯语 * Turkish: 土耳其语 * Malay: 马来语 * Thai: 泰语 * Finnish: 芬兰语  默认UNKNOW。

        :param language: The language of this VoiceModelAssetMeta.
        :type language: str
        """
        self._language = language

    @property
    def speed_ratio(self):
        """Gets the speed_ratio of this VoiceModelAssetMeta.

        语速缩放比例

        :return: The speed_ratio of this VoiceModelAssetMeta.
        :rtype: float
        """
        return self._speed_ratio

    @speed_ratio.setter
    def speed_ratio(self, speed_ratio):
        """Sets the speed_ratio of this VoiceModelAssetMeta.

        语速缩放比例

        :param speed_ratio: The speed_ratio of this VoiceModelAssetMeta.
        :type speed_ratio: float
        """
        self._speed_ratio = speed_ratio

    @property
    def volume_ratio(self):
        """Gets the volume_ratio of this VoiceModelAssetMeta.

        音量缩放比例

        :return: The volume_ratio of this VoiceModelAssetMeta.
        :rtype: float
        """
        return self._volume_ratio

    @volume_ratio.setter
    def volume_ratio(self, volume_ratio):
        """Sets the volume_ratio of this VoiceModelAssetMeta.

        音量缩放比例

        :param volume_ratio: The volume_ratio of this VoiceModelAssetMeta.
        :type volume_ratio: float
        """
        self._volume_ratio = volume_ratio

    @property
    def is_realtime_voice(self):
        """Gets the is_realtime_voice of this VoiceModelAssetMeta.

        该音色是否支持实时合成，默认是true。 > * 支持实时合成的音色，可以用于直播和智能交互场景。否则只能用于视频制作。

        :return: The is_realtime_voice of this VoiceModelAssetMeta.
        :rtype: bool
        """
        return self._is_realtime_voice

    @is_realtime_voice.setter
    def is_realtime_voice(self, is_realtime_voice):
        """Sets the is_realtime_voice of this VoiceModelAssetMeta.

        该音色是否支持实时合成，默认是true。 > * 支持实时合成的音色，可以用于直播和智能交互场景。否则只能用于视频制作。

        :param is_realtime_voice: The is_realtime_voice of this VoiceModelAssetMeta.
        :type is_realtime_voice: bool
        """
        self._is_realtime_voice = is_realtime_voice

    @property
    def voice_capability(self):
        """Gets the voice_capability of this VoiceModelAssetMeta.

        :return: The voice_capability of this VoiceModelAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceCapability`
        """
        return self._voice_capability

    @voice_capability.setter
    def voice_capability(self, voice_capability):
        """Sets the voice_capability of this VoiceModelAssetMeta.

        :param voice_capability: The voice_capability of this VoiceModelAssetMeta.
        :type voice_capability: :class:`huaweicloudsdkmetastudio.v1.VoiceCapability`
        """
        self._voice_capability = voice_capability

    @property
    def external_voice_meta(self):
        """Gets the external_voice_meta of this VoiceModelAssetMeta.

        :return: The external_voice_meta of this VoiceModelAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ExternalVoiceAssetMeta`
        """
        return self._external_voice_meta

    @external_voice_meta.setter
    def external_voice_meta(self, external_voice_meta):
        """Sets the external_voice_meta of this VoiceModelAssetMeta.

        :param external_voice_meta: The external_voice_meta of this VoiceModelAssetMeta.
        :type external_voice_meta: :class:`huaweicloudsdkmetastudio.v1.ExternalVoiceAssetMeta`
        """
        self._external_voice_meta = external_voice_meta

    @property
    def is_support_vc_process(self):
        """Gets the is_support_vc_process of this VoiceModelAssetMeta.

        是否支持vc。

        :return: The is_support_vc_process of this VoiceModelAssetMeta.
        :rtype: bool
        """
        return self._is_support_vc_process

    @is_support_vc_process.setter
    def is_support_vc_process(self, is_support_vc_process):
        """Sets the is_support_vc_process of this VoiceModelAssetMeta.

        是否支持vc。

        :param is_support_vc_process: The is_support_vc_process of this VoiceModelAssetMeta.
        :type is_support_vc_process: bool
        """
        self._is_support_vc_process = is_support_vc_process

    @property
    def is_flexus(self):
        """Gets the is_flexus of this VoiceModelAssetMeta.

        是否是Flexus版本声音。

        :return: The is_flexus of this VoiceModelAssetMeta.
        :rtype: bool
        """
        return self._is_flexus

    @is_flexus.setter
    def is_flexus(self, is_flexus):
        """Sets the is_flexus of this VoiceModelAssetMeta.

        是否是Flexus版本声音。

        :param is_flexus: The is_flexus of this VoiceModelAssetMeta.
        :type is_flexus: bool
        """
        self._is_flexus = is_flexus

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
