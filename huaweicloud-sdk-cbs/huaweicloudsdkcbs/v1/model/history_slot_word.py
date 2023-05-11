# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HistorySlotWord:

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
        'norm_word': 'str'
    }

    attribute_map = {
        'word': 'word',
        'norm_word': 'norm_word'
    }

    def __init__(self, word=None, norm_word=None):
        """HistorySlotWord

        The model defined in huaweicloud sdk

        :param word: 词
        :type word: str
        :param norm_word: 归一化后的词
        :type norm_word: str
        """
        
        

        self._word = None
        self._norm_word = None
        self.discriminator = None

        self.word = word
        self.norm_word = norm_word

    @property
    def word(self):
        """Gets the word of this HistorySlotWord.

        词

        :return: The word of this HistorySlotWord.
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        """Sets the word of this HistorySlotWord.

        词

        :param word: The word of this HistorySlotWord.
        :type word: str
        """
        self._word = word

    @property
    def norm_word(self):
        """Gets the norm_word of this HistorySlotWord.

        归一化后的词

        :return: The norm_word of this HistorySlotWord.
        :rtype: str
        """
        return self._norm_word

    @norm_word.setter
    def norm_word(self, norm_word):
        """Sets the norm_word of this HistorySlotWord.

        归一化后的词

        :param norm_word: The norm_word of this HistorySlotWord.
        :type norm_word: str
        """
        self._norm_word = norm_word

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
        if not isinstance(other, HistorySlotWord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
