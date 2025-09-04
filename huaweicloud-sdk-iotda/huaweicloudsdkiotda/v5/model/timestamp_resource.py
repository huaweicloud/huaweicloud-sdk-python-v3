# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimestampResource:

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
        'pattern': 'str',
        'value': 'object'
    }

    attribute_map = {
        'type': 'type',
        'pattern': 'pattern',
        'value': 'value'
    }

    def __init__(self, type=None, pattern=None, value=None):
        r"""TimestampResource

        The model defined in huaweicloud sdk

        :param type: UNIX：表示为Unix时间戳秒级别长整数，FORMAT：表示为特定时间格式，需要在format字段中指定具体格式。
        :type type: str
        :param pattern: 时间日期格式。
        :type pattern: str
        :param value: 设备连接时具体时间戳值，可使用FunctionDefinition下的函数编程时间戳的取值，若想关闭时间戳校验则该字段值设置为空json:{}。
        :type value: object
        """
        
        

        self._type = None
        self._pattern = None
        self._value = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if pattern is not None:
            self.pattern = pattern
        if value is not None:
            self.value = value

    @property
    def type(self):
        r"""Gets the type of this TimestampResource.

        UNIX：表示为Unix时间戳秒级别长整数，FORMAT：表示为特定时间格式，需要在format字段中指定具体格式。

        :return: The type of this TimestampResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TimestampResource.

        UNIX：表示为Unix时间戳秒级别长整数，FORMAT：表示为特定时间格式，需要在format字段中指定具体格式。

        :param type: The type of this TimestampResource.
        :type type: str
        """
        self._type = type

    @property
    def pattern(self):
        r"""Gets the pattern of this TimestampResource.

        时间日期格式。

        :return: The pattern of this TimestampResource.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        r"""Sets the pattern of this TimestampResource.

        时间日期格式。

        :param pattern: The pattern of this TimestampResource.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def value(self):
        r"""Gets the value of this TimestampResource.

        设备连接时具体时间戳值，可使用FunctionDefinition下的函数编程时间戳的取值，若想关闭时间戳校验则该字段值设置为空json:{}。

        :return: The value of this TimestampResource.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this TimestampResource.

        设备连接时具体时间戳值，可使用FunctionDefinition下的函数编程时间戳的取值，若想关闭时间戳校验则该字段值设置为空json:{}。

        :param value: The value of this TimestampResource.
        :type value: object
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
        if not isinstance(other, TimestampResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
