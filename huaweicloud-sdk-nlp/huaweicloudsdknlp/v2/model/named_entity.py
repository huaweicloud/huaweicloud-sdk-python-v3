# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NamedEntity:

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
        'len': 'int'
    }

    attribute_map = {
        'word': 'word',
        'tag': 'tag',
        'offset': 'offset',
        'len': 'len'
    }

    def __init__(self, word=None, tag=None, offset=None, len=None):
        """NamedEntity

        The model defined in huaweicloud sdk

        :param word: 实体文本。
        :type word: str
        :param tag: 实体类型，枚举类型。 中文支持人名“nr”，地名“ns”，机构名“nt”，时间“t”。 英文支持人名“per”，地名“loc”，机构名“org”，时间“t”。 西班牙文支持人名“per”，地名“loc”，机构名“org”，时间“t”。
        :type tag: str
        :param offset: 实体文本在待分析文本中的起始位置。
        :type offset: int
        :param len: 实体文本长度。
        :type len: int
        """
        
        

        self._word = None
        self._tag = None
        self._offset = None
        self._len = None
        self.discriminator = None

        self.word = word
        self.tag = tag
        self.offset = offset
        self.len = len

    @property
    def word(self):
        """Gets the word of this NamedEntity.

        实体文本。

        :return: The word of this NamedEntity.
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        """Sets the word of this NamedEntity.

        实体文本。

        :param word: The word of this NamedEntity.
        :type word: str
        """
        self._word = word

    @property
    def tag(self):
        """Gets the tag of this NamedEntity.

        实体类型，枚举类型。 中文支持人名“nr”，地名“ns”，机构名“nt”，时间“t”。 英文支持人名“per”，地名“loc”，机构名“org”，时间“t”。 西班牙文支持人名“per”，地名“loc”，机构名“org”，时间“t”。

        :return: The tag of this NamedEntity.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this NamedEntity.

        实体类型，枚举类型。 中文支持人名“nr”，地名“ns”，机构名“nt”，时间“t”。 英文支持人名“per”，地名“loc”，机构名“org”，时间“t”。 西班牙文支持人名“per”，地名“loc”，机构名“org”，时间“t”。

        :param tag: The tag of this NamedEntity.
        :type tag: str
        """
        self._tag = tag

    @property
    def offset(self):
        """Gets the offset of this NamedEntity.

        实体文本在待分析文本中的起始位置。

        :return: The offset of this NamedEntity.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this NamedEntity.

        实体文本在待分析文本中的起始位置。

        :param offset: The offset of this NamedEntity.
        :type offset: int
        """
        self._offset = offset

    @property
    def len(self):
        """Gets the len of this NamedEntity.

        实体文本长度。

        :return: The len of this NamedEntity.
        :rtype: int
        """
        return self._len

    @len.setter
    def len(self, len):
        """Sets the len of this NamedEntity.

        实体文本长度。

        :param len: The len of this NamedEntity.
        :type len: int
        """
        self._len = len

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
        if not isinstance(other, NamedEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
