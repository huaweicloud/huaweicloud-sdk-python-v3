# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Tag:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'key': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'key': 'key',
        'values': 'values'
    }

    def __init__(self, type=None, key=None, values=None):
        r"""Tag

        The model defined in huaweicloud sdk

        :param type: 标签类型: - user - system
        :type type: str
        :param key: 标签键。最大长度36个unicode字符，key不能为空。  字符集：0-9，A-Z，a-z，“_”，“-”，中文。
        :type key: str
        :param values:  标签值列表。每个标签值最大长度43个unicode字符，可以为空字符串。  字符集：0-9，A-Z，a-z，“_”，“.”，“-”，中文。
        :type values: list[str]
        """
        
        

        self._type = None
        self._key = None
        self._values = None
        self.discriminator = None

        self.type = type
        self.key = key
        self.values = values

    @property
    def type(self):
        r"""Gets the type of this Tag.

        标签类型: - user - system

        :return: The type of this Tag.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Tag.

        标签类型: - user - system

        :param type: The type of this Tag.
        :type type: str
        """
        self._type = type

    @property
    def key(self):
        r"""Gets the key of this Tag.

        标签键。最大长度36个unicode字符，key不能为空。  字符集：0-9，A-Z，a-z，“_”，“-”，中文。

        :return: The key of this Tag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this Tag.

        标签键。最大长度36个unicode字符，key不能为空。  字符集：0-9，A-Z，a-z，“_”，“-”，中文。

        :param key: The key of this Tag.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        r"""Gets the values of this Tag.

         标签值列表。每个标签值最大长度43个unicode字符，可以为空字符串。  字符集：0-9，A-Z，a-z，“_”，“.”，“-”，中文。

        :return: The values of this Tag.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this Tag.

         标签值列表。每个标签值最大长度43个unicode字符，可以为空字符串。  字符集：0-9，A-Z，a-z，“_”，“.”，“-”，中文。

        :param values: The values of this Tag.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
