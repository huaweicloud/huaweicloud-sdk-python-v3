# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PathElement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index': 'int',
        'key': 'str',
        'substring': 'Substring',
        'value': 'str'
    }

    attribute_map = {
        'index': 'index',
        'key': 'key',
        'substring': 'substring',
        'value': 'value'
    }

    def __init__(self, index=None, key=None, substring=None, value=None):
        r"""PathElement

        The model defined in huaweicloud sdk

        :param index: 数组中的索引，从0开始。
        :type index: int
        :param key: 对象中的键。
        :type key: str
        :param substring: 
        :type substring: :class:`huaweicloudsdkiamaccessanalyzer.v1.Substring`
        :param value: 与对象中给定键关联的值。
        :type value: str
        """
        
        

        self._index = None
        self._key = None
        self._substring = None
        self._value = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if key is not None:
            self.key = key
        if substring is not None:
            self.substring = substring
        if value is not None:
            self.value = value

    @property
    def index(self):
        r"""Gets the index of this PathElement.

        数组中的索引，从0开始。

        :return: The index of this PathElement.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this PathElement.

        数组中的索引，从0开始。

        :param index: The index of this PathElement.
        :type index: int
        """
        self._index = index

    @property
    def key(self):
        r"""Gets the key of this PathElement.

        对象中的键。

        :return: The key of this PathElement.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this PathElement.

        对象中的键。

        :param key: The key of this PathElement.
        :type key: str
        """
        self._key = key

    @property
    def substring(self):
        r"""Gets the substring of this PathElement.

        :return: The substring of this PathElement.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.Substring`
        """
        return self._substring

    @substring.setter
    def substring(self, substring):
        r"""Sets the substring of this PathElement.

        :param substring: The substring of this PathElement.
        :type substring: :class:`huaweicloudsdkiamaccessanalyzer.v1.Substring`
        """
        self._substring = substring

    @property
    def value(self):
        r"""Gets the value of this PathElement.

        与对象中给定键关联的值。

        :return: The value of this PathElement.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this PathElement.

        与对象中给定键关联的值。

        :param value: The value of this PathElement.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, PathElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
