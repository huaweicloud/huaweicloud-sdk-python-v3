# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InsertHeaderConfig:

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
        'value_type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value_type': 'value_type',
        'value': 'value'
    }

    def __init__(self, key=None, value_type=None, value=None):
        r"""InsertHeaderConfig

        The model defined in huaweicloud sdk

        :param key: **参数解释**：请求头参数名。  **取值范围**：1-40个字符，字母a-z（不区分大小写）、数字，短划线-和下划线_。
        :type key: str
        :param value_type: **参数解释**：请求头参数类别。  **取值范围**：USER_DEFINED,REFERENCE_HEADER,SYSTEM_DEFINED。
        :type value_type: str
        :param value: **参数解释**：请求头参数的值。  **取值范围**：1-128个字符，支持ascii码值32&lt;&#x3D;ch&lt;&#x3D;127范围内可打印字符，*和英文问号?。不能以空格开头或结尾。
        :type value: str
        """
        
        

        self._key = None
        self._value_type = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value_type = value_type
        self.value = value

    @property
    def key(self):
        r"""Gets the key of this InsertHeaderConfig.

        **参数解释**：请求头参数名。  **取值范围**：1-40个字符，字母a-z（不区分大小写）、数字，短划线-和下划线_。

        :return: The key of this InsertHeaderConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this InsertHeaderConfig.

        **参数解释**：请求头参数名。  **取值范围**：1-40个字符，字母a-z（不区分大小写）、数字，短划线-和下划线_。

        :param key: The key of this InsertHeaderConfig.
        :type key: str
        """
        self._key = key

    @property
    def value_type(self):
        r"""Gets the value_type of this InsertHeaderConfig.

        **参数解释**：请求头参数类别。  **取值范围**：USER_DEFINED,REFERENCE_HEADER,SYSTEM_DEFINED。

        :return: The value_type of this InsertHeaderConfig.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        r"""Sets the value_type of this InsertHeaderConfig.

        **参数解释**：请求头参数类别。  **取值范围**：USER_DEFINED,REFERENCE_HEADER,SYSTEM_DEFINED。

        :param value_type: The value_type of this InsertHeaderConfig.
        :type value_type: str
        """
        self._value_type = value_type

    @property
    def value(self):
        r"""Gets the value of this InsertHeaderConfig.

        **参数解释**：请求头参数的值。  **取值范围**：1-128个字符，支持ascii码值32<=ch<=127范围内可打印字符，*和英文问号?。不能以空格开头或结尾。

        :return: The value of this InsertHeaderConfig.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this InsertHeaderConfig.

        **参数解释**：请求头参数的值。  **取值范围**：1-128个字符，支持ascii码值32<=ch<=127范围内可打印字符，*和英文问号?。不能以空格开头或结尾。

        :param value: The value of this InsertHeaderConfig.
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
        if not isinstance(other, InsertHeaderConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
