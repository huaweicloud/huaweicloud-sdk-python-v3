# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Config:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_format': 'str',
        '_property': 'str',
        'add_punc': 'str',
        'vocabulary_id': 'str',
        'digit_norm': 'str',
        'need_word_info': 'str'
    }

    attribute_map = {
        'audio_format': 'audio_format',
        '_property': 'property',
        'add_punc': 'add_punc',
        'vocabulary_id': 'vocabulary_id',
        'digit_norm': 'digit_norm',
        'need_word_info': 'need_word_info'
    }

    def __init__(self, audio_format=None, _property=None, add_punc=None, vocabulary_id=None, digit_norm=None, need_word_info=None):
        """Config

        The model defined in huaweicloud sdk

        :param audio_format: 支持语音的格式。  audio_format取值范围：  pcm16k16bit  16k16bit单通道录音数据。  pcm8k16bit   8k16bit单通道录音数据。  ulaw16k8bit  16k8bit ulaw 单通道录音数据。  ulaw8k8bit   8k8bit ulaw 单通道录音数据。  alaw16k8bit  16k8bit alaw 单通道录音数据。  alaw8k8bit   8k8bit alaw 单通道录音数据。  mp3  mp3格式音频。目前仅支持单通道的音频。  aac  aac格式音频。目前仅支持单通道的音频。  wav  带wav封装头的格式，从封装头中自动确定格式，目前仅支持8k/16k采样率、单通道、pcm, alaw, ulaw三种编码格式  amr  AMR窄带(8k) 压缩录音数据。  amrwb  AMR 宽带(16k) 压缩录音数据。  auto 由引擎自动判断音频数据的格式并解码，支持自动判断wav，mp3，amr/amrwb，aac，m4a，wma格式
        :type audio_format: str
        :param _property: 所使用的模型特征串。通常是 “语种_采样率_领域”的形式。  采样率需要与音频采样率保持一致。  当前支持如下模型特征串：  chinese_16k_general  支持采样率为16k的中文普通话语音识别，同时可识别一些简单的方言。格式仅支持pcm16k16bit、mp3、wav，区域仅支持cn-north-4。  chinese_16k_travel 支持采样率为16k的中文普通话语音识别，采用新一代端到端识别算法，并针对网约车质检场景进行了优化。格式仅支持pcm16k16bit、mp3、wav和aac，区域支持cn-east-3和cn-north-4（强烈推荐使用）。  chinese_8k_common  支持采样率为8k的中文普通话语音识别。  chinese_16k_common  支持采样率为16k的中文普通话语音识别。  sichuan_16k_common  支持采样率为16k的中文普通话与四川话方言识别。区域仅支持cn-north-4。  cantonese_16k_common  支持采样率为16k的粤语方言识别。区域仅支持cn-north-4。  shanghai_16k_common  支持采样率为16k的上海话方言识别，区域仅支持cn-north-4。
        :type _property: str
        :param add_punc: 表示是否在识别结果中添加标点，取值为“yes”和“no”，缺省为“no”。
        :type add_punc: str
        :param vocabulary_id: 热词表id，不使用则不填写。
        :type vocabulary_id: str
        :param digit_norm: 表示是否将语音中的数字识别为阿拉伯数字，取值为“yes” 和 “no”，缺省为“yes”。
        :type digit_norm: str
        :param need_word_info: 表示是否在识别结果中输出分词结果信息，取值为“yes”和“no”，默认为“no”。
        :type need_word_info: str
        """
        
        

        self._audio_format = None
        self.__property = None
        self._add_punc = None
        self._vocabulary_id = None
        self._digit_norm = None
        self._need_word_info = None
        self.discriminator = None

        self.audio_format = audio_format
        self._property = _property
        if add_punc is not None:
            self.add_punc = add_punc
        if vocabulary_id is not None:
            self.vocabulary_id = vocabulary_id
        if digit_norm is not None:
            self.digit_norm = digit_norm
        if need_word_info is not None:
            self.need_word_info = need_word_info

    @property
    def audio_format(self):
        """Gets the audio_format of this Config.

        支持语音的格式。  audio_format取值范围：  pcm16k16bit  16k16bit单通道录音数据。  pcm8k16bit   8k16bit单通道录音数据。  ulaw16k8bit  16k8bit ulaw 单通道录音数据。  ulaw8k8bit   8k8bit ulaw 单通道录音数据。  alaw16k8bit  16k8bit alaw 单通道录音数据。  alaw8k8bit   8k8bit alaw 单通道录音数据。  mp3  mp3格式音频。目前仅支持单通道的音频。  aac  aac格式音频。目前仅支持单通道的音频。  wav  带wav封装头的格式，从封装头中自动确定格式，目前仅支持8k/16k采样率、单通道、pcm, alaw, ulaw三种编码格式  amr  AMR窄带(8k) 压缩录音数据。  amrwb  AMR 宽带(16k) 压缩录音数据。  auto 由引擎自动判断音频数据的格式并解码，支持自动判断wav，mp3，amr/amrwb，aac，m4a，wma格式

        :return: The audio_format of this Config.
        :rtype: str
        """
        return self._audio_format

    @audio_format.setter
    def audio_format(self, audio_format):
        """Sets the audio_format of this Config.

        支持语音的格式。  audio_format取值范围：  pcm16k16bit  16k16bit单通道录音数据。  pcm8k16bit   8k16bit单通道录音数据。  ulaw16k8bit  16k8bit ulaw 单通道录音数据。  ulaw8k8bit   8k8bit ulaw 单通道录音数据。  alaw16k8bit  16k8bit alaw 单通道录音数据。  alaw8k8bit   8k8bit alaw 单通道录音数据。  mp3  mp3格式音频。目前仅支持单通道的音频。  aac  aac格式音频。目前仅支持单通道的音频。  wav  带wav封装头的格式，从封装头中自动确定格式，目前仅支持8k/16k采样率、单通道、pcm, alaw, ulaw三种编码格式  amr  AMR窄带(8k) 压缩录音数据。  amrwb  AMR 宽带(16k) 压缩录音数据。  auto 由引擎自动判断音频数据的格式并解码，支持自动判断wav，mp3，amr/amrwb，aac，m4a，wma格式

        :param audio_format: The audio_format of this Config.
        :type audio_format: str
        """
        self._audio_format = audio_format

    @property
    def _property(self):
        """Gets the _property of this Config.

        所使用的模型特征串。通常是 “语种_采样率_领域”的形式。  采样率需要与音频采样率保持一致。  当前支持如下模型特征串：  chinese_16k_general  支持采样率为16k的中文普通话语音识别，同时可识别一些简单的方言。格式仅支持pcm16k16bit、mp3、wav，区域仅支持cn-north-4。  chinese_16k_travel 支持采样率为16k的中文普通话语音识别，采用新一代端到端识别算法，并针对网约车质检场景进行了优化。格式仅支持pcm16k16bit、mp3、wav和aac，区域支持cn-east-3和cn-north-4（强烈推荐使用）。  chinese_8k_common  支持采样率为8k的中文普通话语音识别。  chinese_16k_common  支持采样率为16k的中文普通话语音识别。  sichuan_16k_common  支持采样率为16k的中文普通话与四川话方言识别。区域仅支持cn-north-4。  cantonese_16k_common  支持采样率为16k的粤语方言识别。区域仅支持cn-north-4。  shanghai_16k_common  支持采样率为16k的上海话方言识别，区域仅支持cn-north-4。

        :return: The _property of this Config.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this Config.

        所使用的模型特征串。通常是 “语种_采样率_领域”的形式。  采样率需要与音频采样率保持一致。  当前支持如下模型特征串：  chinese_16k_general  支持采样率为16k的中文普通话语音识别，同时可识别一些简单的方言。格式仅支持pcm16k16bit、mp3、wav，区域仅支持cn-north-4。  chinese_16k_travel 支持采样率为16k的中文普通话语音识别，采用新一代端到端识别算法，并针对网约车质检场景进行了优化。格式仅支持pcm16k16bit、mp3、wav和aac，区域支持cn-east-3和cn-north-4（强烈推荐使用）。  chinese_8k_common  支持采样率为8k的中文普通话语音识别。  chinese_16k_common  支持采样率为16k的中文普通话语音识别。  sichuan_16k_common  支持采样率为16k的中文普通话与四川话方言识别。区域仅支持cn-north-4。  cantonese_16k_common  支持采样率为16k的粤语方言识别。区域仅支持cn-north-4。  shanghai_16k_common  支持采样率为16k的上海话方言识别，区域仅支持cn-north-4。

        :param _property: The _property of this Config.
        :type _property: str
        """
        self.__property = _property

    @property
    def add_punc(self):
        """Gets the add_punc of this Config.

        表示是否在识别结果中添加标点，取值为“yes”和“no”，缺省为“no”。

        :return: The add_punc of this Config.
        :rtype: str
        """
        return self._add_punc

    @add_punc.setter
    def add_punc(self, add_punc):
        """Sets the add_punc of this Config.

        表示是否在识别结果中添加标点，取值为“yes”和“no”，缺省为“no”。

        :param add_punc: The add_punc of this Config.
        :type add_punc: str
        """
        self._add_punc = add_punc

    @property
    def vocabulary_id(self):
        """Gets the vocabulary_id of this Config.

        热词表id，不使用则不填写。

        :return: The vocabulary_id of this Config.
        :rtype: str
        """
        return self._vocabulary_id

    @vocabulary_id.setter
    def vocabulary_id(self, vocabulary_id):
        """Sets the vocabulary_id of this Config.

        热词表id，不使用则不填写。

        :param vocabulary_id: The vocabulary_id of this Config.
        :type vocabulary_id: str
        """
        self._vocabulary_id = vocabulary_id

    @property
    def digit_norm(self):
        """Gets the digit_norm of this Config.

        表示是否将语音中的数字识别为阿拉伯数字，取值为“yes” 和 “no”，缺省为“yes”。

        :return: The digit_norm of this Config.
        :rtype: str
        """
        return self._digit_norm

    @digit_norm.setter
    def digit_norm(self, digit_norm):
        """Sets the digit_norm of this Config.

        表示是否将语音中的数字识别为阿拉伯数字，取值为“yes” 和 “no”，缺省为“yes”。

        :param digit_norm: The digit_norm of this Config.
        :type digit_norm: str
        """
        self._digit_norm = digit_norm

    @property
    def need_word_info(self):
        """Gets the need_word_info of this Config.

        表示是否在识别结果中输出分词结果信息，取值为“yes”和“no”，默认为“no”。

        :return: The need_word_info of this Config.
        :rtype: str
        """
        return self._need_word_info

    @need_word_info.setter
    def need_word_info(self, need_word_info):
        """Sets the need_word_info of this Config.

        表示是否在识别结果中输出分词结果信息，取值为“yes”和“no”，默认为“no”。

        :param need_word_info: The need_word_info of this Config.
        :type need_word_info: str
        """
        self._need_word_info = need_word_info

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
        if not isinstance(other, Config):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
