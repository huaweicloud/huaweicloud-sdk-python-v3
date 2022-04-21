# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Word:

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
        'text_original': 'str',
        'text_normalised': 'list[str]',
        'out_of_vocabulary': 'bool',
        'start_time': 'float',
        'end_time': 'float',
        'score': 'float',
        'pronunciation': 'WordPronunciation',
        'fluency': 'WordFluency',
        'phonemes': 'list[Phoneme]'
    }

    attribute_map = {
        'text': 'text',
        'text_original': 'text_original',
        'text_normalised': 'text_normalised',
        'out_of_vocabulary': 'out_of_vocabulary',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'score': 'score',
        'pronunciation': 'pronunciation',
        'fluency': 'fluency',
        'phonemes': 'phonemes'
    }

    def __init__(self, text=None, text_original=None, text_normalised=None, out_of_vocabulary=None, start_time=None, end_time=None, score=None, pronunciation=None, fluency=None, phonemes=None):
        """Word

        The model defined in huaweicloud sdk

        :param text: 去除了所有标点符号后的原始文本 前端调用接口后推荐使用“​text​”来在UI 中展示结果
        :type text: str
        :param text_original: 接口接收的原始文本
        :type text_original: str
        :param text_normalised: 原始文本规范化后切分成的单词 如175 会 规范为 [\&quot;one\&quot;, \&quot;\&quot;hundred\&quot;, \&quot;and\&quot;, \&quot;seventy\&quot;, \&quot;five\&quot;]
        :type text_normalised: list[str]
        :param out_of_vocabulary: 是否命中模型发音字典 如果未命中，则表明会根据发音规律推测正确发音
        :type out_of_vocabulary: bool
        :param start_time: 起始时间
        :type start_time: float
        :param end_time: 结束时间
        :type end_time: float
        :param score: 综合评分
        :type score: float
        :param pronunciation: 
        :type pronunciation: :class:`huaweicloudsdksis.v1.WordPronunciation`
        :param fluency: 
        :type fluency: :class:`huaweicloudsdksis.v1.WordFluency`
        :param phonemes: 音节打分表
        :type phonemes: list[:class:`huaweicloudsdksis.v1.Phoneme`]
        """
        
        

        self._text = None
        self._text_original = None
        self._text_normalised = None
        self._out_of_vocabulary = None
        self._start_time = None
        self._end_time = None
        self._score = None
        self._pronunciation = None
        self._fluency = None
        self._phonemes = None
        self.discriminator = None

        self.text = text
        self.text_original = text_original
        self.text_normalised = text_normalised
        if out_of_vocabulary is not None:
            self.out_of_vocabulary = out_of_vocabulary
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if score is not None:
            self.score = score
        if pronunciation is not None:
            self.pronunciation = pronunciation
        if fluency is not None:
            self.fluency = fluency
        if phonemes is not None:
            self.phonemes = phonemes

    @property
    def text(self):
        """Gets the text of this Word.

        去除了所有标点符号后的原始文本 前端调用接口后推荐使用“​text​”来在UI 中展示结果

        :return: The text of this Word.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Word.

        去除了所有标点符号后的原始文本 前端调用接口后推荐使用“​text​”来在UI 中展示结果

        :param text: The text of this Word.
        :type text: str
        """
        self._text = text

    @property
    def text_original(self):
        """Gets the text_original of this Word.

        接口接收的原始文本

        :return: The text_original of this Word.
        :rtype: str
        """
        return self._text_original

    @text_original.setter
    def text_original(self, text_original):
        """Sets the text_original of this Word.

        接口接收的原始文本

        :param text_original: The text_original of this Word.
        :type text_original: str
        """
        self._text_original = text_original

    @property
    def text_normalised(self):
        """Gets the text_normalised of this Word.

        原始文本规范化后切分成的单词 如175 会 规范为 [\"one\", \"\"hundred\", \"and\", \"seventy\", \"five\"]

        :return: The text_normalised of this Word.
        :rtype: list[str]
        """
        return self._text_normalised

    @text_normalised.setter
    def text_normalised(self, text_normalised):
        """Sets the text_normalised of this Word.

        原始文本规范化后切分成的单词 如175 会 规范为 [\"one\", \"\"hundred\", \"and\", \"seventy\", \"five\"]

        :param text_normalised: The text_normalised of this Word.
        :type text_normalised: list[str]
        """
        self._text_normalised = text_normalised

    @property
    def out_of_vocabulary(self):
        """Gets the out_of_vocabulary of this Word.

        是否命中模型发音字典 如果未命中，则表明会根据发音规律推测正确发音

        :return: The out_of_vocabulary of this Word.
        :rtype: bool
        """
        return self._out_of_vocabulary

    @out_of_vocabulary.setter
    def out_of_vocabulary(self, out_of_vocabulary):
        """Sets the out_of_vocabulary of this Word.

        是否命中模型发音字典 如果未命中，则表明会根据发音规律推测正确发音

        :param out_of_vocabulary: The out_of_vocabulary of this Word.
        :type out_of_vocabulary: bool
        """
        self._out_of_vocabulary = out_of_vocabulary

    @property
    def start_time(self):
        """Gets the start_time of this Word.

        起始时间

        :return: The start_time of this Word.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Word.

        起始时间

        :param start_time: The start_time of this Word.
        :type start_time: float
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Word.

        结束时间

        :return: The end_time of this Word.
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Word.

        结束时间

        :param end_time: The end_time of this Word.
        :type end_time: float
        """
        self._end_time = end_time

    @property
    def score(self):
        """Gets the score of this Word.

        综合评分

        :return: The score of this Word.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Word.

        综合评分

        :param score: The score of this Word.
        :type score: float
        """
        self._score = score

    @property
    def pronunciation(self):
        """Gets the pronunciation of this Word.


        :return: The pronunciation of this Word.
        :rtype: :class:`huaweicloudsdksis.v1.WordPronunciation`
        """
        return self._pronunciation

    @pronunciation.setter
    def pronunciation(self, pronunciation):
        """Sets the pronunciation of this Word.


        :param pronunciation: The pronunciation of this Word.
        :type pronunciation: :class:`huaweicloudsdksis.v1.WordPronunciation`
        """
        self._pronunciation = pronunciation

    @property
    def fluency(self):
        """Gets the fluency of this Word.


        :return: The fluency of this Word.
        :rtype: :class:`huaweicloudsdksis.v1.WordFluency`
        """
        return self._fluency

    @fluency.setter
    def fluency(self, fluency):
        """Sets the fluency of this Word.


        :param fluency: The fluency of this Word.
        :type fluency: :class:`huaweicloudsdksis.v1.WordFluency`
        """
        self._fluency = fluency

    @property
    def phonemes(self):
        """Gets the phonemes of this Word.

        音节打分表

        :return: The phonemes of this Word.
        :rtype: list[:class:`huaweicloudsdksis.v1.Phoneme`]
        """
        return self._phonemes

    @phonemes.setter
    def phonemes(self, phonemes):
        """Sets the phonemes of this Word.

        音节打分表

        :param phonemes: The phonemes of this Word.
        :type phonemes: list[:class:`huaweicloudsdksis.v1.Phoneme`]
        """
        self._phonemes = phonemes

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
        if not isinstance(other, Word):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
