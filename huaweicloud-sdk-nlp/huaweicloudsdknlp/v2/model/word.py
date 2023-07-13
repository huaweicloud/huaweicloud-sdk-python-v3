# coding: utf-8

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
        'content': 'str',
        'pos': 'str'
    }

    attribute_map = {
        'content': 'content',
        'pos': 'pos'
    }

    def __init__(self, content=None, pos=None):
        """Word

        The model defined in huaweicloud sdk

        :param content: 词汇文本。
        :type content: str
        :param pos: 词汇对应的词性。
        :type pos: str
        """
        
        

        self._content = None
        self._pos = None
        self.discriminator = None

        self.content = content
        self.pos = pos

    @property
    def content(self):
        """Gets the content of this Word.

        词汇文本。

        :return: The content of this Word.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Word.

        词汇文本。

        :param content: The content of this Word.
        :type content: str
        """
        self._content = content

    @property
    def pos(self):
        """Gets the pos of this Word.

        词汇对应的词性。

        :return: The pos of this Word.
        :rtype: str
        """
        return self._pos

    @pos.setter
    def pos(self, pos):
        """Sets the pos of this Word.

        词汇对应的词性。

        :param pos: The pos of this Word.
        :type pos: str
        """
        self._pos = pos

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
