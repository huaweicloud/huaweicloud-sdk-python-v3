# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Secret:

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
        r"""Secret

        The model defined in huaweicloud sdk

        :param key: 密钥key，最大长度63个字符。不能为空，只能包含大小写字母，数字，中划线“-”，下划线“_”
        :type key: str
        :param value: 密钥value，每个值最大长度10000个字符，删除时如果value有值按照key/value删除，如果value没值，则按照key删除。不能为空，只能包含大小写字母，数字，中划线“-”，下划线“_”
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        r"""Gets the key of this Secret.

        密钥key，最大长度63个字符。不能为空，只能包含大小写字母，数字，中划线“-”，下划线“_”

        :return: The key of this Secret.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this Secret.

        密钥key，最大长度63个字符。不能为空，只能包含大小写字母，数字，中划线“-”，下划线“_”

        :param key: The key of this Secret.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this Secret.

        密钥value，每个值最大长度10000个字符，删除时如果value有值按照key/value删除，如果value没值，则按照key删除。不能为空，只能包含大小写字母，数字，中划线“-”，下划线“_”

        :return: The value of this Secret.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Secret.

        密钥value，每个值最大长度10000个字符，删除时如果value有值按照key/value删除，如果value没值，则按照key删除。不能为空，只能包含大小写字母，数字，中划线“-”，下划线“_”

        :param value: The value of this Secret.
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
        if not isinstance(other, Secret):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
