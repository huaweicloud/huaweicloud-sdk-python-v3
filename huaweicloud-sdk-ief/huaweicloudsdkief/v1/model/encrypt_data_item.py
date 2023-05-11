# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncryptDataItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'value': 'str',
        'is_encrypted': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'is_encrypted': 'is_encrypted'
    }

    def __init__(self, name=None, value=None, is_encrypted=None):
        """EncryptDataItem

        The model defined in huaweicloud sdk

        :param name: 加密数据项键名，小写英文字母、数字、中划线，以小写字母或数字开头，最大长度为32个字符，不能为空
        :type name: str
        :param value: 加密数据项键值
        :type value: str
        :param is_encrypted: 加密数据项键值是否已加密，默认为true
        :type is_encrypted: bool
        """
        
        

        self._name = None
        self._value = None
        self._is_encrypted = None
        self.discriminator = None

        self.name = name
        self.value = value
        if is_encrypted is not None:
            self.is_encrypted = is_encrypted

    @property
    def name(self):
        """Gets the name of this EncryptDataItem.

        加密数据项键名，小写英文字母、数字、中划线，以小写字母或数字开头，最大长度为32个字符，不能为空

        :return: The name of this EncryptDataItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EncryptDataItem.

        加密数据项键名，小写英文字母、数字、中划线，以小写字母或数字开头，最大长度为32个字符，不能为空

        :param name: The name of this EncryptDataItem.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this EncryptDataItem.

        加密数据项键值

        :return: The value of this EncryptDataItem.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EncryptDataItem.

        加密数据项键值

        :param value: The value of this EncryptDataItem.
        :type value: str
        """
        self._value = value

    @property
    def is_encrypted(self):
        """Gets the is_encrypted of this EncryptDataItem.

        加密数据项键值是否已加密，默认为true

        :return: The is_encrypted of this EncryptDataItem.
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted):
        """Sets the is_encrypted of this EncryptDataItem.

        加密数据项键值是否已加密，默认为true

        :param is_encrypted: The is_encrypted of this EncryptDataItem.
        :type is_encrypted: bool
        """
        self._is_encrypted = is_encrypted

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
        if not isinstance(other, EncryptDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
