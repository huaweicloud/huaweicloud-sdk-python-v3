# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EmailItemDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'str',
        'type': 'str',
        'primary': 'bool'
    }

    attribute_map = {
        'value': 'value',
        'type': 'type',
        'primary': 'primary'
    }

    def __init__(self, value=None, type=None, primary=None):
        r"""EmailItemDto

        The model defined in huaweicloud sdk

        :param value: 包含电子邮箱地址的字符串
        :type value: str
        :param type: 表示电子邮箱类型的字符串
        :type type: str
        :param primary: 一个布尔值，表示这是否是用户的主电子邮箱
        :type primary: bool
        """
        
        

        self._value = None
        self._type = None
        self._primary = None
        self.discriminator = None

        self.value = value
        self.type = type
        self.primary = primary

    @property
    def value(self):
        r"""Gets the value of this EmailItemDto.

        包含电子邮箱地址的字符串

        :return: The value of this EmailItemDto.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this EmailItemDto.

        包含电子邮箱地址的字符串

        :param value: The value of this EmailItemDto.
        :type value: str
        """
        self._value = value

    @property
    def type(self):
        r"""Gets the type of this EmailItemDto.

        表示电子邮箱类型的字符串

        :return: The type of this EmailItemDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EmailItemDto.

        表示电子邮箱类型的字符串

        :param type: The type of this EmailItemDto.
        :type type: str
        """
        self._type = type

    @property
    def primary(self):
        r"""Gets the primary of this EmailItemDto.

        一个布尔值，表示这是否是用户的主电子邮箱

        :return: The primary of this EmailItemDto.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        r"""Sets the primary of this EmailItemDto.

        一个布尔值，表示这是否是用户的主电子邮箱

        :param primary: The primary of this EmailItemDto.
        :type primary: bool
        """
        self._primary = primary

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
        if not isinstance(other, EmailItemDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
