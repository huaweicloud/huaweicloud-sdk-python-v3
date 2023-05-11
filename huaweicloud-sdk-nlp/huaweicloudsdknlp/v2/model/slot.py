# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Slot:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'word': 'str',
        'tag': 'str',
        'offset': 'int',
        'length': 'int',
        'normalized_word': 'str'
    }

    attribute_map = {
        'word': 'word',
        'tag': 'tag',
        'offset': 'offset',
        'length': 'length',
        'normalized_word': 'normalized_word'
    }

    def __init__(self, word=None, tag=None, offset=None, length=None, normalized_word=None):
        """Slot

        The model defined in huaweicloud sdk

        :param word: 实体文本。
        :type word: str
        :param tag: 实体类型。对于每个意图类别所支持的实体类型分别为： weather：date(日期)，time(时间)，location(位置) time：location(位置)，timezone(时区) news：genre(风格) joke：genre(风格) translation：content(内容) notification：content(内容)，date(日期)，time(时间)，singer(歌手) alarm：date(日期)，time:(时间) music：singer(歌手)，song(歌曲)，content(内容)
        :type tag: str
        :param offset: 实体文本在待分析文本中的起始位置。
        :type offset: int
        :param length: 实体文本长度。
        :type length: int
        :param normalized_word: 同义词或者其他标准表达的词，默认为原始的word。
        :type normalized_word: str
        """
        
        

        self._word = None
        self._tag = None
        self._offset = None
        self._length = None
        self._normalized_word = None
        self.discriminator = None

        self.word = word
        self.tag = tag
        self.offset = offset
        self.length = length
        self.normalized_word = normalized_word

    @property
    def word(self):
        """Gets the word of this Slot.

        实体文本。

        :return: The word of this Slot.
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        """Sets the word of this Slot.

        实体文本。

        :param word: The word of this Slot.
        :type word: str
        """
        self._word = word

    @property
    def tag(self):
        """Gets the tag of this Slot.

        实体类型。对于每个意图类别所支持的实体类型分别为： weather：date(日期)，time(时间)，location(位置) time：location(位置)，timezone(时区) news：genre(风格) joke：genre(风格) translation：content(内容) notification：content(内容)，date(日期)，time(时间)，singer(歌手) alarm：date(日期)，time:(时间) music：singer(歌手)，song(歌曲)，content(内容)

        :return: The tag of this Slot.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Slot.

        实体类型。对于每个意图类别所支持的实体类型分别为： weather：date(日期)，time(时间)，location(位置) time：location(位置)，timezone(时区) news：genre(风格) joke：genre(风格) translation：content(内容) notification：content(内容)，date(日期)，time(时间)，singer(歌手) alarm：date(日期)，time:(时间) music：singer(歌手)，song(歌曲)，content(内容)

        :param tag: The tag of this Slot.
        :type tag: str
        """
        self._tag = tag

    @property
    def offset(self):
        """Gets the offset of this Slot.

        实体文本在待分析文本中的起始位置。

        :return: The offset of this Slot.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this Slot.

        实体文本在待分析文本中的起始位置。

        :param offset: The offset of this Slot.
        :type offset: int
        """
        self._offset = offset

    @property
    def length(self):
        """Gets the length of this Slot.

        实体文本长度。

        :return: The length of this Slot.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Slot.

        实体文本长度。

        :param length: The length of this Slot.
        :type length: int
        """
        self._length = length

    @property
    def normalized_word(self):
        """Gets the normalized_word of this Slot.

        同义词或者其他标准表达的词，默认为原始的word。

        :return: The normalized_word of this Slot.
        :rtype: str
        """
        return self._normalized_word

    @normalized_word.setter
    def normalized_word(self, normalized_word):
        """Sets the normalized_word of this Slot.

        同义词或者其他标准表达的词，默认为原始的word。

        :param normalized_word: The normalized_word of this Slot.
        :type normalized_word: str
        """
        self._normalized_word = normalized_word

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
        if not isinstance(other, Slot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
