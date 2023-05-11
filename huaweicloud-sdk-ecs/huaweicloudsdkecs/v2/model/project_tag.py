# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectTag:

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
        """ProjectTag

        The model defined in huaweicloud sdk

        :param key: 键。  - 最大长度36个unicode字符。  - 只能包含数字、字母、中划线“-”、下划线“_”。  - 字符集：A-Z，a-z ， 0-9，‘-’，‘_’，UNICODE字符（\\u4E00-\\u9FFF）。  - 不能包含以下ASCII非打印字符：“&#x3D;”,“*”,“&lt;”,“&gt;”,“\\”,“|”,“/”,“,”。  - 标签的键必须唯一且输入不能为空。
        :type key: str
        :param values: 值。  - 每个值最大长度43个unicode字符。  - 可以为空字符串。  - 只能包含数字、字母、中划线“-”、下划线“_”。  - 字符集：A-Z，a-z ， 0-9，‘.’，‘-’，‘_’，UNICODE字符（\\u4E00-\\u9FFF）。  - 不能包含以下ASCII非打印字符：“&#x3D;”,“*”,“&lt;”,“&gt;”,“\\”,“|”,“/”,“,”。
        :type values: list[str]
        """
        
        

        self._key = None
        self._values = None
        self.discriminator = None

        self.key = key
        if values is not None:
            self.values = values

    @property
    def key(self):
        """Gets the key of this ProjectTag.

        键。  - 最大长度36个unicode字符。  - 只能包含数字、字母、中划线“-”、下划线“_”。  - 字符集：A-Z，a-z ， 0-9，‘-’，‘_’，UNICODE字符（\\u4E00-\\u9FFF）。  - 不能包含以下ASCII非打印字符：“=”,“*”,“<”,“>”,“\\”,“|”,“/”,“,”。  - 标签的键必须唯一且输入不能为空。

        :return: The key of this ProjectTag.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ProjectTag.

        键。  - 最大长度36个unicode字符。  - 只能包含数字、字母、中划线“-”、下划线“_”。  - 字符集：A-Z，a-z ， 0-9，‘-’，‘_’，UNICODE字符（\\u4E00-\\u9FFF）。  - 不能包含以下ASCII非打印字符：“=”,“*”,“<”,“>”,“\\”,“|”,“/”,“,”。  - 标签的键必须唯一且输入不能为空。

        :param key: The key of this ProjectTag.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        """Gets the values of this ProjectTag.

        值。  - 每个值最大长度43个unicode字符。  - 可以为空字符串。  - 只能包含数字、字母、中划线“-”、下划线“_”。  - 字符集：A-Z，a-z ， 0-9，‘.’，‘-’，‘_’，UNICODE字符（\\u4E00-\\u9FFF）。  - 不能包含以下ASCII非打印字符：“=”,“*”,“<”,“>”,“\\”,“|”,“/”,“,”。

        :return: The values of this ProjectTag.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ProjectTag.

        值。  - 每个值最大长度43个unicode字符。  - 可以为空字符串。  - 只能包含数字、字母、中划线“-”、下划线“_”。  - 字符集：A-Z，a-z ， 0-9，‘.’，‘-’，‘_’，UNICODE字符（\\u4E00-\\u9FFF）。  - 不能包含以下ASCII非打印字符：“=”,“*”,“<”,“>”,“\\”,“|”,“/”,“,”。

        :param values: The values of this ProjectTag.
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
        if not isinstance(other, ProjectTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
