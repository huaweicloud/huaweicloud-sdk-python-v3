# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecognizeFlashAsrRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_property': 'str',
        'audio_format': 'str',
        'obs_bucket_name': 'str',
        'obs_object_key': 'str',
        'add_punc': 'str',
        'digit_norm': 'str',
        'need_word_info': 'str',
        'vocabulary_id': 'str',
        'first_channel_only': 'str'
    }

    attribute_map = {
        '_property': 'property',
        'audio_format': 'audio_format',
        'obs_bucket_name': 'obs_bucket_name',
        'obs_object_key': 'obs_object_key',
        'add_punc': 'add_punc',
        'digit_norm': 'digit_norm',
        'need_word_info': 'need_word_info',
        'vocabulary_id': 'vocabulary_id',
        'first_channel_only': 'first_channel_only'
    }

    def __init__(self, _property=None, audio_format=None, obs_bucket_name=None, obs_object_key=None, add_punc=None, digit_norm=None, need_word_info=None, vocabulary_id=None, first_channel_only=None):
        r"""RecognizeFlashAsrRequest

        The model defined in huaweicloud sdk

        :param _property: 所使用的模型特征串。通常是 “语种_采样率_领域”的形式。 采样率需要与音频采样率保持一致。 当前支持如下模型特征串： chinese_8k_common chinese_16k_conversation
        :type _property: str
        :param audio_format: 音频格式，audio_format取值范围： wav,mp3,m4a,aac,opus
        :type audio_format: str
        :param obs_bucket_name: obs桶名
        :type obs_bucket_name: str
        :param obs_object_key: obs对象key，经过urlencode编码，长度不超过1024个字符
        :type obs_object_key: str
        :param add_punc: 是否加标点， 可以为 yes, 默认no
        :type add_punc: str
        :param digit_norm: 是否将音频中的数字使用阿拉伯数字的形式呈现，取值为yes，no，默认为yes
        :type digit_norm: str
        :param need_word_info: 表示是否在识别结果中输出分词结果信息，取值为yes，no，默认no
        :type need_word_info: str
        :param vocabulary_id: 热词表id
        :type vocabulary_id: str
        :param first_channel_only: 表示是否在识别中只识别首个声道的音频数据，取值为“yes”和“no”，默认为“no”。
        :type first_channel_only: str
        """
        
        

        self.__property = None
        self._audio_format = None
        self._obs_bucket_name = None
        self._obs_object_key = None
        self._add_punc = None
        self._digit_norm = None
        self._need_word_info = None
        self._vocabulary_id = None
        self._first_channel_only = None
        self.discriminator = None

        self._property = _property
        self.audio_format = audio_format
        self.obs_bucket_name = obs_bucket_name
        self.obs_object_key = obs_object_key
        if add_punc is not None:
            self.add_punc = add_punc
        if digit_norm is not None:
            self.digit_norm = digit_norm
        if need_word_info is not None:
            self.need_word_info = need_word_info
        if vocabulary_id is not None:
            self.vocabulary_id = vocabulary_id
        if first_channel_only is not None:
            self.first_channel_only = first_channel_only

    @property
    def _property(self):
        r"""Gets the _property of this RecognizeFlashAsrRequest.

        所使用的模型特征串。通常是 “语种_采样率_领域”的形式。 采样率需要与音频采样率保持一致。 当前支持如下模型特征串： chinese_8k_common chinese_16k_conversation

        :return: The _property of this RecognizeFlashAsrRequest.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        r"""Sets the _property of this RecognizeFlashAsrRequest.

        所使用的模型特征串。通常是 “语种_采样率_领域”的形式。 采样率需要与音频采样率保持一致。 当前支持如下模型特征串： chinese_8k_common chinese_16k_conversation

        :param _property: The _property of this RecognizeFlashAsrRequest.
        :type _property: str
        """
        self.__property = _property

    @property
    def audio_format(self):
        r"""Gets the audio_format of this RecognizeFlashAsrRequest.

        音频格式，audio_format取值范围： wav,mp3,m4a,aac,opus

        :return: The audio_format of this RecognizeFlashAsrRequest.
        :rtype: str
        """
        return self._audio_format

    @audio_format.setter
    def audio_format(self, audio_format):
        r"""Sets the audio_format of this RecognizeFlashAsrRequest.

        音频格式，audio_format取值范围： wav,mp3,m4a,aac,opus

        :param audio_format: The audio_format of this RecognizeFlashAsrRequest.
        :type audio_format: str
        """
        self._audio_format = audio_format

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this RecognizeFlashAsrRequest.

        obs桶名

        :return: The obs_bucket_name of this RecognizeFlashAsrRequest.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this RecognizeFlashAsrRequest.

        obs桶名

        :param obs_bucket_name: The obs_bucket_name of this RecognizeFlashAsrRequest.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def obs_object_key(self):
        r"""Gets the obs_object_key of this RecognizeFlashAsrRequest.

        obs对象key，经过urlencode编码，长度不超过1024个字符

        :return: The obs_object_key of this RecognizeFlashAsrRequest.
        :rtype: str
        """
        return self._obs_object_key

    @obs_object_key.setter
    def obs_object_key(self, obs_object_key):
        r"""Sets the obs_object_key of this RecognizeFlashAsrRequest.

        obs对象key，经过urlencode编码，长度不超过1024个字符

        :param obs_object_key: The obs_object_key of this RecognizeFlashAsrRequest.
        :type obs_object_key: str
        """
        self._obs_object_key = obs_object_key

    @property
    def add_punc(self):
        r"""Gets the add_punc of this RecognizeFlashAsrRequest.

        是否加标点， 可以为 yes, 默认no

        :return: The add_punc of this RecognizeFlashAsrRequest.
        :rtype: str
        """
        return self._add_punc

    @add_punc.setter
    def add_punc(self, add_punc):
        r"""Sets the add_punc of this RecognizeFlashAsrRequest.

        是否加标点， 可以为 yes, 默认no

        :param add_punc: The add_punc of this RecognizeFlashAsrRequest.
        :type add_punc: str
        """
        self._add_punc = add_punc

    @property
    def digit_norm(self):
        r"""Gets the digit_norm of this RecognizeFlashAsrRequest.

        是否将音频中的数字使用阿拉伯数字的形式呈现，取值为yes，no，默认为yes

        :return: The digit_norm of this RecognizeFlashAsrRequest.
        :rtype: str
        """
        return self._digit_norm

    @digit_norm.setter
    def digit_norm(self, digit_norm):
        r"""Sets the digit_norm of this RecognizeFlashAsrRequest.

        是否将音频中的数字使用阿拉伯数字的形式呈现，取值为yes，no，默认为yes

        :param digit_norm: The digit_norm of this RecognizeFlashAsrRequest.
        :type digit_norm: str
        """
        self._digit_norm = digit_norm

    @property
    def need_word_info(self):
        r"""Gets the need_word_info of this RecognizeFlashAsrRequest.

        表示是否在识别结果中输出分词结果信息，取值为yes，no，默认no

        :return: The need_word_info of this RecognizeFlashAsrRequest.
        :rtype: str
        """
        return self._need_word_info

    @need_word_info.setter
    def need_word_info(self, need_word_info):
        r"""Sets the need_word_info of this RecognizeFlashAsrRequest.

        表示是否在识别结果中输出分词结果信息，取值为yes，no，默认no

        :param need_word_info: The need_word_info of this RecognizeFlashAsrRequest.
        :type need_word_info: str
        """
        self._need_word_info = need_word_info

    @property
    def vocabulary_id(self):
        r"""Gets the vocabulary_id of this RecognizeFlashAsrRequest.

        热词表id

        :return: The vocabulary_id of this RecognizeFlashAsrRequest.
        :rtype: str
        """
        return self._vocabulary_id

    @vocabulary_id.setter
    def vocabulary_id(self, vocabulary_id):
        r"""Sets the vocabulary_id of this RecognizeFlashAsrRequest.

        热词表id

        :param vocabulary_id: The vocabulary_id of this RecognizeFlashAsrRequest.
        :type vocabulary_id: str
        """
        self._vocabulary_id = vocabulary_id

    @property
    def first_channel_only(self):
        r"""Gets the first_channel_only of this RecognizeFlashAsrRequest.

        表示是否在识别中只识别首个声道的音频数据，取值为“yes”和“no”，默认为“no”。

        :return: The first_channel_only of this RecognizeFlashAsrRequest.
        :rtype: str
        """
        return self._first_channel_only

    @first_channel_only.setter
    def first_channel_only(self, first_channel_only):
        r"""Sets the first_channel_only of this RecognizeFlashAsrRequest.

        表示是否在识别中只识别首个声道的音频数据，取值为“yes”和“no”，默认为“no”。

        :param first_channel_only: The first_channel_only of this RecognizeFlashAsrRequest.
        :type first_channel_only: str
        """
        self._first_channel_only = first_channel_only

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
        if not isinstance(other, RecognizeFlashAsrRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
