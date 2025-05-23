# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WordInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'word': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'word': 'word'
    }

    def __init__(self, start_time=None, end_time=None, word=None):
        r"""WordInfo

        The model defined in huaweicloud sdk

        :param start_time: 起始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param word: 分词
        :type word: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._word = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if word is not None:
            self.word = word

    @property
    def start_time(self):
        r"""Gets the start_time of this WordInfo.

        起始时间

        :return: The start_time of this WordInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this WordInfo.

        起始时间

        :param start_time: The start_time of this WordInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this WordInfo.

        结束时间

        :return: The end_time of this WordInfo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this WordInfo.

        结束时间

        :param end_time: The end_time of this WordInfo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def word(self):
        r"""Gets the word of this WordInfo.

        分词

        :return: The word of this WordInfo.
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        r"""Sets the word of this WordInfo.

        分词

        :param word: The word of this WordInfo.
        :type word: str
        """
        self._word = word

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
        if not isinstance(other, WordInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
