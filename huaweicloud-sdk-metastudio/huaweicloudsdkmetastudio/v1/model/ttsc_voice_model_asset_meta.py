# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TtscVoiceModelAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sex': 'str',
        'external_voice_meta': 'TtscExternalVoiceAssetMeta',
        'language': 'str',
        'speed_ratio': 'float',
        'volume_ratio': 'float'
    }

    attribute_map = {
        'sex': 'sex',
        'external_voice_meta': 'external_voice_meta',
        'language': 'language',
        'speed_ratio': 'speed_ratio',
        'volume_ratio': 'volume_ratio'
    }

    def __init__(self, sex=None, external_voice_meta=None, language=None, speed_ratio=None, volume_ratio=None):
        r"""TtscVoiceModelAssetMeta

        The model defined in huaweicloud sdk

        :param sex: 音色性别。 * UNKNOW：中性音色 * MALE：男性音色 * FEMALE：女性音色  默认UNKNOW。
        :type sex: str
        :param external_voice_meta: 
        :type external_voice_meta: :class:`huaweicloudsdkmetastudio.v1.TtscExternalVoiceAssetMeta`
        :param language: 音色语言。 * UNKNOW：未知 * CN：中文 * EN：英文 * GER：德语 * fr：法语 * Kr：韩语 * por：葡萄牙语 * JPN：日语 * Ita：意大利语 * ESP：西班牙语 * DBH：东北话 * GT：港台 * GXH：广西话 * HBH：湖北话 * SXH：陕西话 * SCH：四川话 * YY：粤语 * Russian: 俄罗斯语 * Filipino: 菲律宾语 * Dutch: 荷兰语 * Indonesian: 印尼语 * Vietnamese: 越南语 * Arabic: 阿拉伯语 * Turkish: 土耳其语 * Malay: 马来语 * Thai: 泰语 * Finnish: 芬兰语  默认UNKNOW。
        :type language: str
        :param speed_ratio: 语速缩放比例
        :type speed_ratio: float
        :param volume_ratio: 音量缩放比例
        :type volume_ratio: float
        """
        
        

        self._sex = None
        self._external_voice_meta = None
        self._language = None
        self._speed_ratio = None
        self._volume_ratio = None
        self.discriminator = None

        if sex is not None:
            self.sex = sex
        if external_voice_meta is not None:
            self.external_voice_meta = external_voice_meta
        if language is not None:
            self.language = language
        if speed_ratio is not None:
            self.speed_ratio = speed_ratio
        if volume_ratio is not None:
            self.volume_ratio = volume_ratio

    @property
    def sex(self):
        r"""Gets the sex of this TtscVoiceModelAssetMeta.

        音色性别。 * UNKNOW：中性音色 * MALE：男性音色 * FEMALE：女性音色  默认UNKNOW。

        :return: The sex of this TtscVoiceModelAssetMeta.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this TtscVoiceModelAssetMeta.

        音色性别。 * UNKNOW：中性音色 * MALE：男性音色 * FEMALE：女性音色  默认UNKNOW。

        :param sex: The sex of this TtscVoiceModelAssetMeta.
        :type sex: str
        """
        self._sex = sex

    @property
    def external_voice_meta(self):
        r"""Gets the external_voice_meta of this TtscVoiceModelAssetMeta.

        :return: The external_voice_meta of this TtscVoiceModelAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TtscExternalVoiceAssetMeta`
        """
        return self._external_voice_meta

    @external_voice_meta.setter
    def external_voice_meta(self, external_voice_meta):
        r"""Sets the external_voice_meta of this TtscVoiceModelAssetMeta.

        :param external_voice_meta: The external_voice_meta of this TtscVoiceModelAssetMeta.
        :type external_voice_meta: :class:`huaweicloudsdkmetastudio.v1.TtscExternalVoiceAssetMeta`
        """
        self._external_voice_meta = external_voice_meta

    @property
    def language(self):
        r"""Gets the language of this TtscVoiceModelAssetMeta.

        音色语言。 * UNKNOW：未知 * CN：中文 * EN：英文 * GER：德语 * fr：法语 * Kr：韩语 * por：葡萄牙语 * JPN：日语 * Ita：意大利语 * ESP：西班牙语 * DBH：东北话 * GT：港台 * GXH：广西话 * HBH：湖北话 * SXH：陕西话 * SCH：四川话 * YY：粤语 * Russian: 俄罗斯语 * Filipino: 菲律宾语 * Dutch: 荷兰语 * Indonesian: 印尼语 * Vietnamese: 越南语 * Arabic: 阿拉伯语 * Turkish: 土耳其语 * Malay: 马来语 * Thai: 泰语 * Finnish: 芬兰语  默认UNKNOW。

        :return: The language of this TtscVoiceModelAssetMeta.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this TtscVoiceModelAssetMeta.

        音色语言。 * UNKNOW：未知 * CN：中文 * EN：英文 * GER：德语 * fr：法语 * Kr：韩语 * por：葡萄牙语 * JPN：日语 * Ita：意大利语 * ESP：西班牙语 * DBH：东北话 * GT：港台 * GXH：广西话 * HBH：湖北话 * SXH：陕西话 * SCH：四川话 * YY：粤语 * Russian: 俄罗斯语 * Filipino: 菲律宾语 * Dutch: 荷兰语 * Indonesian: 印尼语 * Vietnamese: 越南语 * Arabic: 阿拉伯语 * Turkish: 土耳其语 * Malay: 马来语 * Thai: 泰语 * Finnish: 芬兰语  默认UNKNOW。

        :param language: The language of this TtscVoiceModelAssetMeta.
        :type language: str
        """
        self._language = language

    @property
    def speed_ratio(self):
        r"""Gets the speed_ratio of this TtscVoiceModelAssetMeta.

        语速缩放比例

        :return: The speed_ratio of this TtscVoiceModelAssetMeta.
        :rtype: float
        """
        return self._speed_ratio

    @speed_ratio.setter
    def speed_ratio(self, speed_ratio):
        r"""Sets the speed_ratio of this TtscVoiceModelAssetMeta.

        语速缩放比例

        :param speed_ratio: The speed_ratio of this TtscVoiceModelAssetMeta.
        :type speed_ratio: float
        """
        self._speed_ratio = speed_ratio

    @property
    def volume_ratio(self):
        r"""Gets the volume_ratio of this TtscVoiceModelAssetMeta.

        音量缩放比例

        :return: The volume_ratio of this TtscVoiceModelAssetMeta.
        :rtype: float
        """
        return self._volume_ratio

    @volume_ratio.setter
    def volume_ratio(self, volume_ratio):
        r"""Sets the volume_ratio of this TtscVoiceModelAssetMeta.

        音量缩放比例

        :param volume_ratio: The volume_ratio of this TtscVoiceModelAssetMeta.
        :type volume_ratio: float
        """
        self._volume_ratio = volume_ratio

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
        if not isinstance(other, TtscVoiceModelAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
