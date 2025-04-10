# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SealWordsBlockList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'words': 'str',
        'words_confidence': 'float'
    }

    attribute_map = {
        'words': 'words',
        'words_confidence': 'words_confidence'
    }

    def __init__(self, words=None, words_confidence=None):
        r"""SealWordsBlockList

        The model defined in huaweicloud sdk

        :param words: 印章文本块。
        :type words: str
        :param words_confidence: 印章文本块的置信度。
        :type words_confidence: float
        """
        
        

        self._words = None
        self._words_confidence = None
        self.discriminator = None

        if words is not None:
            self.words = words
        if words_confidence is not None:
            self.words_confidence = words_confidence

    @property
    def words(self):
        r"""Gets the words of this SealWordsBlockList.

        印章文本块。

        :return: The words of this SealWordsBlockList.
        :rtype: str
        """
        return self._words

    @words.setter
    def words(self, words):
        r"""Sets the words of this SealWordsBlockList.

        印章文本块。

        :param words: The words of this SealWordsBlockList.
        :type words: str
        """
        self._words = words

    @property
    def words_confidence(self):
        r"""Gets the words_confidence of this SealWordsBlockList.

        印章文本块的置信度。

        :return: The words_confidence of this SealWordsBlockList.
        :rtype: float
        """
        return self._words_confidence

    @words_confidence.setter
    def words_confidence(self, words_confidence):
        r"""Sets the words_confidence of this SealWordsBlockList.

        印章文本块的置信度。

        :param words_confidence: The words_confidence of this SealWordsBlockList.
        :type words_confidence: float
        """
        self._words_confidence = words_confidence

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
        if not isinstance(other, SealWordsBlockList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
