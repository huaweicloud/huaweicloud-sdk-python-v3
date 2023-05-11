# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventExtractionResponseItemArgument:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role': 'str',
        'span': 'list[int]',
        'word': 'str'
    }

    attribute_map = {
        'role': 'role',
        'span': 'span',
        'word': 'word'
    }

    def __init__(self, role=None, span=None, word=None):
        """EventExtractionResponseItemArgument

        The model defined in huaweicloud sdk

        :param role: 元素角色。元素角色指的是事件元素在事件中扮演的角色，是事件元素与事件的语义关系。
        :type role: str
        :param span: 实体文本在待分析文本中的起始和终止位置。
        :type span: list[int]
        :param word: 实体文本。
        :type word: str
        """
        
        

        self._role = None
        self._span = None
        self._word = None
        self.discriminator = None

        self.role = role
        self.span = span
        self.word = word

    @property
    def role(self):
        """Gets the role of this EventExtractionResponseItemArgument.

        元素角色。元素角色指的是事件元素在事件中扮演的角色，是事件元素与事件的语义关系。

        :return: The role of this EventExtractionResponseItemArgument.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this EventExtractionResponseItemArgument.

        元素角色。元素角色指的是事件元素在事件中扮演的角色，是事件元素与事件的语义关系。

        :param role: The role of this EventExtractionResponseItemArgument.
        :type role: str
        """
        self._role = role

    @property
    def span(self):
        """Gets the span of this EventExtractionResponseItemArgument.

        实体文本在待分析文本中的起始和终止位置。

        :return: The span of this EventExtractionResponseItemArgument.
        :rtype: list[int]
        """
        return self._span

    @span.setter
    def span(self, span):
        """Sets the span of this EventExtractionResponseItemArgument.

        实体文本在待分析文本中的起始和终止位置。

        :param span: The span of this EventExtractionResponseItemArgument.
        :type span: list[int]
        """
        self._span = span

    @property
    def word(self):
        """Gets the word of this EventExtractionResponseItemArgument.

        实体文本。

        :return: The word of this EventExtractionResponseItemArgument.
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        """Sets the word of this EventExtractionResponseItemArgument.

        实体文本。

        :param word: The word of this EventExtractionResponseItemArgument.
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
        if not isinstance(other, EventExtractionResponseItemArgument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
