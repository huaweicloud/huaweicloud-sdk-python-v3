# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Tags:

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
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):
        """Tags

        The model defined in huaweicloud sdk

        :param key: 键。输入标签键的最大长度为36个unicode字符，不能为空字符串，且首尾字符不能为空格。 不能包含“&#x3D;”,“*”,“&lt;”,“&gt;”,“\\\\”,“,”,“|”,“/”。 只能包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）和特殊字符（中划线-、下划线_）以及中文字符。
        :type key: str
        :param value: 值。输入标签值的最大长度为43个字符，首尾字符不能为空格，可以为空字符串。 不能包含“&#x3D;”,“*”,“&lt;”,“&gt;”,“\\\\”,“,”,“|”,“/”。 只能包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）和特殊字符（中划线-、下划线_）以及中文字符。
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        """Gets the key of this Tags.

        键。输入标签键的最大长度为36个unicode字符，不能为空字符串，且首尾字符不能为空格。 不能包含“=”,“*”,“<”,“>”,“\\\\”,“,”,“|”,“/”。 只能包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）和特殊字符（中划线-、下划线_）以及中文字符。

        :return: The key of this Tags.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Tags.

        键。输入标签键的最大长度为36个unicode字符，不能为空字符串，且首尾字符不能为空格。 不能包含“=”,“*”,“<”,“>”,“\\\\”,“,”,“|”,“/”。 只能包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）和特殊字符（中划线-、下划线_）以及中文字符。

        :param key: The key of this Tags.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this Tags.

        值。输入标签值的最大长度为43个字符，首尾字符不能为空格，可以为空字符串。 不能包含“=”,“*”,“<”,“>”,“\\\\”,“,”,“|”,“/”。 只能包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）和特殊字符（中划线-、下划线_）以及中文字符。

        :return: The value of this Tags.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Tags.

        值。输入标签值的最大长度为43个字符，首尾字符不能为空格，可以为空字符串。 不能包含“=”,“*”,“<”,“>”,“\\\\”,“,”,“|”,“/”。 只能包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）和特殊字符（中划线-、下划线_）以及中文字符。

        :param value: The value of this Tags.
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
        if not isinstance(other, Tags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
