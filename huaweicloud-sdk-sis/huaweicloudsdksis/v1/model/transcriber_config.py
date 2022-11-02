# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TranscriberConfig:

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
        'need_analysis_info': 'AnalysisInfo',
        'vocabulary_id': 'str',
        'digit_norm': 'str',
        'callback_url': 'str',
        'need_word_info': 'str'
    }

    attribute_map = {
        'audio_format': 'audio_format',
        '_property': 'property',
        'add_punc': 'add_punc',
        'need_analysis_info': 'need_analysis_info',
        'vocabulary_id': 'vocabulary_id',
        'digit_norm': 'digit_norm',
        'callback_url': 'callback_url',
        'need_word_info': 'need_word_info'
    }

    def __init__(self, audio_format=None, _property=None, add_punc=None, need_analysis_info=None, vocabulary_id=None, digit_norm=None, callback_url=None, need_word_info=None):
        """TranscriberConfig

        The model defined in huaweicloud sdk

        :param audio_format: 支持语音的格式。  audioformat取值范围:  auto  自动判断，系统会自动判断并支持WAV（内部支持pcm/ulaw/alaw/adpcm编码格式）、MP3、M4A、ogg-speex、ogg-opus、AMR、wma等格式，相应的文件后缀名为.wav, .mp3, .m4a, .spx, .opus, .amr 和.wma, 不区分大小写。支持双声道的音频。  pcm16k16bit  16k16bit裸音频录音数据。  pcm8k16bit   8k16bit裸音频录音数据。  ulaw16k8bit  16k8bit ulaw 裸音频录音数据。  ulaw8k8bit   8k8bit ulaw 裸音频录音数据。  alaw16k8bit  16k8bit alaw 裸音频录音数据。  alaw8k8bit   8k8bit alaw 裸音频录音数据。  vox8k4bit    8k4bit vox 裸音频录音数据。  v3_8k4bit    8k4bit v3 裸音频录音数据。
        :type audio_format: str
        :param _property: 所使用的模型特征串。通常是“语种_采样率_领域”的形式，例如chinese_8k_common。  采样率需要与音频采样率保持一致。  当前支持如下模型特征串：  chinese_16k_media (音视频领域，区域仅支持cn-north-4，cn-east-3)  chinese_8k_common  chinese_16k_conversation  chinese_8k_bank（银行领域，区域仅支持cn-north-4）  chinese_8k_insurance（保险领域，区域仅支持cn-north-4）  sichuan_8k_common （四川话识别，区域支持cn-north-4，cn-east-3） 
        :type _property: str
        :param add_punc: 是否加标点， 可以为 yes, no(缺省)。
        :type add_punc: str
        :param need_analysis_info: 
        :type need_analysis_info: :class:`huaweicloudsdksis.v1.AnalysisInfo`
        :param vocabulary_id: 热词表id，不使用则不填写。
        :type vocabulary_id: str
        :param digit_norm: 表示是否将语音中的数字识别为阿拉伯数字，取值为yes 、 no，缺省为yes。
        :type digit_norm: str
        :param callback_url: 用于录音文件识表示回调 url，即用户用于接收识别结果的服务器地址，不支持IP地址方式调用，url长度小于2048字节。服务请求方法为POST。  如果用户使用回调方式获取识别结果，需填写该参数，处理成功后用户服务器需返回状态码“200”。  如果用户使用轮询方式获取识别结果，则无需填写该参数。别结果的回调url，不使用则不填写。
        :type callback_url: str
        :param need_word_info: 表示是否在识别结果中输出分词结果信息，取值为“yes”和“no”，默认为“no”。
        :type need_word_info: str
        """
        
        

        self._audio_format = None
        self.__property = None
        self._add_punc = None
        self._need_analysis_info = None
        self._vocabulary_id = None
        self._digit_norm = None
        self._callback_url = None
        self._need_word_info = None
        self.discriminator = None

        if audio_format is not None:
            self.audio_format = audio_format
        self._property = _property
        if add_punc is not None:
            self.add_punc = add_punc
        if need_analysis_info is not None:
            self.need_analysis_info = need_analysis_info
        if vocabulary_id is not None:
            self.vocabulary_id = vocabulary_id
        if digit_norm is not None:
            self.digit_norm = digit_norm
        if callback_url is not None:
            self.callback_url = callback_url
        if need_word_info is not None:
            self.need_word_info = need_word_info

    @property
    def audio_format(self):
        """Gets the audio_format of this TranscriberConfig.

        支持语音的格式。  audioformat取值范围:  auto  自动判断，系统会自动判断并支持WAV（内部支持pcm/ulaw/alaw/adpcm编码格式）、MP3、M4A、ogg-speex、ogg-opus、AMR、wma等格式，相应的文件后缀名为.wav, .mp3, .m4a, .spx, .opus, .amr 和.wma, 不区分大小写。支持双声道的音频。  pcm16k16bit  16k16bit裸音频录音数据。  pcm8k16bit   8k16bit裸音频录音数据。  ulaw16k8bit  16k8bit ulaw 裸音频录音数据。  ulaw8k8bit   8k8bit ulaw 裸音频录音数据。  alaw16k8bit  16k8bit alaw 裸音频录音数据。  alaw8k8bit   8k8bit alaw 裸音频录音数据。  vox8k4bit    8k4bit vox 裸音频录音数据。  v3_8k4bit    8k4bit v3 裸音频录音数据。

        :return: The audio_format of this TranscriberConfig.
        :rtype: str
        """
        return self._audio_format

    @audio_format.setter
    def audio_format(self, audio_format):
        """Sets the audio_format of this TranscriberConfig.

        支持语音的格式。  audioformat取值范围:  auto  自动判断，系统会自动判断并支持WAV（内部支持pcm/ulaw/alaw/adpcm编码格式）、MP3、M4A、ogg-speex、ogg-opus、AMR、wma等格式，相应的文件后缀名为.wav, .mp3, .m4a, .spx, .opus, .amr 和.wma, 不区分大小写。支持双声道的音频。  pcm16k16bit  16k16bit裸音频录音数据。  pcm8k16bit   8k16bit裸音频录音数据。  ulaw16k8bit  16k8bit ulaw 裸音频录音数据。  ulaw8k8bit   8k8bit ulaw 裸音频录音数据。  alaw16k8bit  16k8bit alaw 裸音频录音数据。  alaw8k8bit   8k8bit alaw 裸音频录音数据。  vox8k4bit    8k4bit vox 裸音频录音数据。  v3_8k4bit    8k4bit v3 裸音频录音数据。

        :param audio_format: The audio_format of this TranscriberConfig.
        :type audio_format: str
        """
        self._audio_format = audio_format

    @property
    def _property(self):
        """Gets the _property of this TranscriberConfig.

        所使用的模型特征串。通常是“语种_采样率_领域”的形式，例如chinese_8k_common。  采样率需要与音频采样率保持一致。  当前支持如下模型特征串：  chinese_16k_media (音视频领域，区域仅支持cn-north-4，cn-east-3)  chinese_8k_common  chinese_16k_conversation  chinese_8k_bank（银行领域，区域仅支持cn-north-4）  chinese_8k_insurance（保险领域，区域仅支持cn-north-4）  sichuan_8k_common （四川话识别，区域支持cn-north-4，cn-east-3） 

        :return: The _property of this TranscriberConfig.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this TranscriberConfig.

        所使用的模型特征串。通常是“语种_采样率_领域”的形式，例如chinese_8k_common。  采样率需要与音频采样率保持一致。  当前支持如下模型特征串：  chinese_16k_media (音视频领域，区域仅支持cn-north-4，cn-east-3)  chinese_8k_common  chinese_16k_conversation  chinese_8k_bank（银行领域，区域仅支持cn-north-4）  chinese_8k_insurance（保险领域，区域仅支持cn-north-4）  sichuan_8k_common （四川话识别，区域支持cn-north-4，cn-east-3） 

        :param _property: The _property of this TranscriberConfig.
        :type _property: str
        """
        self.__property = _property

    @property
    def add_punc(self):
        """Gets the add_punc of this TranscriberConfig.

        是否加标点， 可以为 yes, no(缺省)。

        :return: The add_punc of this TranscriberConfig.
        :rtype: str
        """
        return self._add_punc

    @add_punc.setter
    def add_punc(self, add_punc):
        """Sets the add_punc of this TranscriberConfig.

        是否加标点， 可以为 yes, no(缺省)。

        :param add_punc: The add_punc of this TranscriberConfig.
        :type add_punc: str
        """
        self._add_punc = add_punc

    @property
    def need_analysis_info(self):
        """Gets the need_analysis_info of this TranscriberConfig.


        :return: The need_analysis_info of this TranscriberConfig.
        :rtype: :class:`huaweicloudsdksis.v1.AnalysisInfo`
        """
        return self._need_analysis_info

    @need_analysis_info.setter
    def need_analysis_info(self, need_analysis_info):
        """Sets the need_analysis_info of this TranscriberConfig.


        :param need_analysis_info: The need_analysis_info of this TranscriberConfig.
        :type need_analysis_info: :class:`huaweicloudsdksis.v1.AnalysisInfo`
        """
        self._need_analysis_info = need_analysis_info

    @property
    def vocabulary_id(self):
        """Gets the vocabulary_id of this TranscriberConfig.

        热词表id，不使用则不填写。

        :return: The vocabulary_id of this TranscriberConfig.
        :rtype: str
        """
        return self._vocabulary_id

    @vocabulary_id.setter
    def vocabulary_id(self, vocabulary_id):
        """Sets the vocabulary_id of this TranscriberConfig.

        热词表id，不使用则不填写。

        :param vocabulary_id: The vocabulary_id of this TranscriberConfig.
        :type vocabulary_id: str
        """
        self._vocabulary_id = vocabulary_id

    @property
    def digit_norm(self):
        """Gets the digit_norm of this TranscriberConfig.

        表示是否将语音中的数字识别为阿拉伯数字，取值为yes 、 no，缺省为yes。

        :return: The digit_norm of this TranscriberConfig.
        :rtype: str
        """
        return self._digit_norm

    @digit_norm.setter
    def digit_norm(self, digit_norm):
        """Sets the digit_norm of this TranscriberConfig.

        表示是否将语音中的数字识别为阿拉伯数字，取值为yes 、 no，缺省为yes。

        :param digit_norm: The digit_norm of this TranscriberConfig.
        :type digit_norm: str
        """
        self._digit_norm = digit_norm

    @property
    def callback_url(self):
        """Gets the callback_url of this TranscriberConfig.

        用于录音文件识表示回调 url，即用户用于接收识别结果的服务器地址，不支持IP地址方式调用，url长度小于2048字节。服务请求方法为POST。  如果用户使用回调方式获取识别结果，需填写该参数，处理成功后用户服务器需返回状态码“200”。  如果用户使用轮询方式获取识别结果，则无需填写该参数。别结果的回调url，不使用则不填写。

        :return: The callback_url of this TranscriberConfig.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this TranscriberConfig.

        用于录音文件识表示回调 url，即用户用于接收识别结果的服务器地址，不支持IP地址方式调用，url长度小于2048字节。服务请求方法为POST。  如果用户使用回调方式获取识别结果，需填写该参数，处理成功后用户服务器需返回状态码“200”。  如果用户使用轮询方式获取识别结果，则无需填写该参数。别结果的回调url，不使用则不填写。

        :param callback_url: The callback_url of this TranscriberConfig.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def need_word_info(self):
        """Gets the need_word_info of this TranscriberConfig.

        表示是否在识别结果中输出分词结果信息，取值为“yes”和“no”，默认为“no”。

        :return: The need_word_info of this TranscriberConfig.
        :rtype: str
        """
        return self._need_word_info

    @need_word_info.setter
    def need_word_info(self, need_word_info):
        """Sets the need_word_info of this TranscriberConfig.

        表示是否在识别结果中输出分词结果信息，取值为“yes”和“no”，默认为“no”。

        :param need_word_info: The need_word_info of this TranscriberConfig.
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
        if not isinstance(other, TranscriberConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
