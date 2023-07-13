# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TmsKeyValue:

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
        """TmsKeyValue

        The model defined in huaweicloud sdk

        :param key: 键。  支持可用 UTF-8 格式表示的字母(包含中文)、数字和空格，以及以下字符： _ . : &#x3D; + - @； \\_sys\\_开头属于系统标签，租户不能输入
        :type key: str
        :param value: 值。  支持可用 UTF-8 格式表示的字母(包含中文)、数字和空格，以及以下字符： _ . : / &#x3D; + - @
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def key(self):
        """Gets the key of this TmsKeyValue.

        键。  支持可用 UTF-8 格式表示的字母(包含中文)、数字和空格，以及以下字符： _ . : = + - @； \\_sys\\_开头属于系统标签，租户不能输入

        :return: The key of this TmsKeyValue.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TmsKeyValue.

        键。  支持可用 UTF-8 格式表示的字母(包含中文)、数字和空格，以及以下字符： _ . : = + - @； \\_sys\\_开头属于系统标签，租户不能输入

        :param key: The key of this TmsKeyValue.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this TmsKeyValue.

        值。  支持可用 UTF-8 格式表示的字母(包含中文)、数字和空格，以及以下字符： _ . : / = + - @

        :return: The value of this TmsKeyValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TmsKeyValue.

        值。  支持可用 UTF-8 格式表示的字母(包含中文)、数字和空格，以及以下字符： _ . : / = + - @

        :param value: The value of this TmsKeyValue.
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
        if not isinstance(other, TmsKeyValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
