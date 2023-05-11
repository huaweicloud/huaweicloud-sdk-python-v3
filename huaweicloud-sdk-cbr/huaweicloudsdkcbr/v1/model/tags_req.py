# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagsReq:

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
        'values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'values': 'values'
    }

    def __init__(self, key=None, values=None):
        """TagsReq

        The model defined in huaweicloud sdk

        :param key: 键。  最大长度127个unicode字符。  不允许为空字符串。  前后的空格会被丢弃。
        :type key: str
        :param values: 值列表。  values中最多包含10个value。  每个value最大长度255个unicode字符。前后的空格会被丢弃。  values中value不允许重复。  values中多个value之间是\&quot;或\&quot;的关系。  values允许为空列表，value允许为空字符串。  values如果为空列表，表示任意值。  \\*为系统保留字符，如果value是以\\*开头表示按照\\*后面的值全模糊匹配，不能只传入“\\*”。
        :type values: list[str]
        """
        
        

        self._key = None
        self._values = None
        self.discriminator = None

        self.key = key
        self.values = values

    @property
    def key(self):
        """Gets the key of this TagsReq.

        键。  最大长度127个unicode字符。  不允许为空字符串。  前后的空格会被丢弃。

        :return: The key of this TagsReq.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TagsReq.

        键。  最大长度127个unicode字符。  不允许为空字符串。  前后的空格会被丢弃。

        :param key: The key of this TagsReq.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        """Gets the values of this TagsReq.

        值列表。  values中最多包含10个value。  每个value最大长度255个unicode字符。前后的空格会被丢弃。  values中value不允许重复。  values中多个value之间是\"或\"的关系。  values允许为空列表，value允许为空字符串。  values如果为空列表，表示任意值。  \\*为系统保留字符，如果value是以\\*开头表示按照\\*后面的值全模糊匹配，不能只传入“\\*”。

        :return: The values of this TagsReq.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this TagsReq.

        值列表。  values中最多包含10个value。  每个value最大长度255个unicode字符。前后的空格会被丢弃。  values中value不允许重复。  values中多个value之间是\"或\"的关系。  values允许为空列表，value允许为空字符串。  values如果为空列表，表示任意值。  \\*为系统保留字符，如果value是以\\*开头表示按照\\*后面的值全模糊匹配，不能只传入“\\*”。

        :param values: The values of this TagsReq.
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
        if not isinstance(other, TagsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
