# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlotValue:

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
        'norm_word': 'str',
        'begin_position': 'int',
        'end_position': 'int'
    }

    attribute_map = {
        'word': 'word',
        'norm_word': 'norm_word',
        'begin_position': 'begin_position',
        'end_position': 'end_position'
    }

    def __init__(self, word=None, norm_word=None, begin_position=None, end_position=None):
        r"""SlotValue

        The model defined in huaweicloud sdk

        :param word: 词。
        :type word: str
        :param norm_word: 归一化后的标准词。
        :type norm_word: str
        :param begin_position: 词的起始位置。
        :type begin_position: int
        :param end_position: 词的结束位置。
        :type end_position: int
        """
        
        

        self._word = None
        self._norm_word = None
        self._begin_position = None
        self._end_position = None
        self.discriminator = None

        self.word = word
        self.norm_word = norm_word
        self.begin_position = begin_position
        self.end_position = end_position

    @property
    def word(self):
        r"""Gets the word of this SlotValue.

        词。

        :return: The word of this SlotValue.
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        r"""Sets the word of this SlotValue.

        词。

        :param word: The word of this SlotValue.
        :type word: str
        """
        self._word = word

    @property
    def norm_word(self):
        r"""Gets the norm_word of this SlotValue.

        归一化后的标准词。

        :return: The norm_word of this SlotValue.
        :rtype: str
        """
        return self._norm_word

    @norm_word.setter
    def norm_word(self, norm_word):
        r"""Sets the norm_word of this SlotValue.

        归一化后的标准词。

        :param norm_word: The norm_word of this SlotValue.
        :type norm_word: str
        """
        self._norm_word = norm_word

    @property
    def begin_position(self):
        r"""Gets the begin_position of this SlotValue.

        词的起始位置。

        :return: The begin_position of this SlotValue.
        :rtype: int
        """
        return self._begin_position

    @begin_position.setter
    def begin_position(self, begin_position):
        r"""Sets the begin_position of this SlotValue.

        词的起始位置。

        :param begin_position: The begin_position of this SlotValue.
        :type begin_position: int
        """
        self._begin_position = begin_position

    @property
    def end_position(self):
        r"""Gets the end_position of this SlotValue.

        词的结束位置。

        :return: The end_position of this SlotValue.
        :rtype: int
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        r"""Sets the end_position of this SlotValue.

        词的结束位置。

        :param end_position: The end_position of this SlotValue.
        :type end_position: int
        """
        self._end_position = end_position

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
        if not isinstance(other, SlotValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
