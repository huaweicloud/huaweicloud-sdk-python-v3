# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Result:

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
        'score': 'float',
        'word_info': 'list[WordInfo]'
    }

    attribute_map = {
        'text': 'text',
        'score': 'score',
        'word_info': 'word_info'
    }

    def __init__(self, text=None, score=None, word_info=None):
        """Result

        The model defined in huaweicloud sdk

        :param text: 调用成功表示识别出的内容。
        :type text: str
        :param score: 调用成功表示识别出的置信度，取值范围：0~1。
        :type score: float
        :param word_info: 分词信息列表
        :type word_info: list[:class:`huaweicloudsdksis.v1.WordInfo`]
        """
        
        

        self._text = None
        self._score = None
        self._word_info = None
        self.discriminator = None

        self.text = text
        self.score = score
        if word_info is not None:
            self.word_info = word_info

    @property
    def text(self):
        """Gets the text of this Result.

        调用成功表示识别出的内容。

        :return: The text of this Result.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Result.

        调用成功表示识别出的内容。

        :param text: The text of this Result.
        :type text: str
        """
        self._text = text

    @property
    def score(self):
        """Gets the score of this Result.

        调用成功表示识别出的置信度，取值范围：0~1。

        :return: The score of this Result.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Result.

        调用成功表示识别出的置信度，取值范围：0~1。

        :param score: The score of this Result.
        :type score: float
        """
        self._score = score

    @property
    def word_info(self):
        """Gets the word_info of this Result.

        分词信息列表

        :return: The word_info of this Result.
        :rtype: list[:class:`huaweicloudsdksis.v1.WordInfo`]
        """
        return self._word_info

    @word_info.setter
    def word_info(self, word_info):
        """Sets the word_info of this Result.

        分词信息列表

        :param word_info: The word_info of this Result.
        :type word_info: list[:class:`huaweicloudsdksis.v1.WordInfo`]
        """
        self._word_info = word_info

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
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
