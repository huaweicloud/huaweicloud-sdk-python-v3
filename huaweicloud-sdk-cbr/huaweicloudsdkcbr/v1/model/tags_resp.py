# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagsResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'values': 'str'
    }

    attribute_map = {
        'key': 'key',
        'values': 'values'
    }

    def __init__(self, key=None, values=None):
        """TagsResp

        The model defined in huaweicloud sdk

        :param key: 键。  key最大长度36个字符。  key不能为空字符串。  key只能由中文，字母，数字，“-”，“_”组成。
        :type key: str
        :param values: 值列表。  value最大长度43个字符。  value可以为空字符串。  key只能由中文，字母，数字，“-”，“_”组成。
        :type values: str
        """
        
        

        self._key = None
        self._values = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if values is not None:
            self.values = values

    @property
    def key(self):
        """Gets the key of this TagsResp.

        键。  key最大长度36个字符。  key不能为空字符串。  key只能由中文，字母，数字，“-”，“_”组成。

        :return: The key of this TagsResp.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TagsResp.

        键。  key最大长度36个字符。  key不能为空字符串。  key只能由中文，字母，数字，“-”，“_”组成。

        :param key: The key of this TagsResp.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        """Gets the values of this TagsResp.

        值列表。  value最大长度43个字符。  value可以为空字符串。  key只能由中文，字母，数字，“-”，“_”组成。

        :return: The values of this TagsResp.
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this TagsResp.

        值列表。  value最大长度43个字符。  value可以为空字符串。  key只能由中文，字母，数字，“-”，“_”组成。

        :param values: The values of this TagsResp.
        :type values: str
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
        if not isinstance(other, TagsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
