# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MessageAttribute:

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
        'type': 'str',
        'value': 'object'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, name=None, type=None, value=None):
        r"""MessageAttribute

        The model defined in huaweicloud sdk

        :param name: 属性名称。属性名称只能包含小写英文字母([a-z])、数字([0-9])、下划线(_)，下划线不能出现在开始或结尾，下划线不能连续出现，长度为1到32个字符
        :type name: str
        :param type: 属性类型 STRING：字符串（String）类型 STRING_ARRAY：字符串数组（String.Array）类型 PROTOCOL：协议类型
        :type type: str
        :param value: 属性值。 当属性类型为“STRING”时，属性值只能包含中英文、数字、下划线，长度为1到32个字符。 当属性类型为“STRING_ARRAY”时，属性值为字符串数组，数组长度为1到10，数组中的元素内容不能重复，数组中的每个字符串都只能包含中英文、数字、下划线，且长度为1到32个字符。 当属性类型为“PROTOCOL”时，属性值为支持协议类型的字符串数组。
        :type value: object
        """
        
        

        self._name = None
        self._type = None
        self._value = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.value = value

    @property
    def name(self):
        r"""Gets the name of this MessageAttribute.

        属性名称。属性名称只能包含小写英文字母([a-z])、数字([0-9])、下划线(_)，下划线不能出现在开始或结尾，下划线不能连续出现，长度为1到32个字符

        :return: The name of this MessageAttribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MessageAttribute.

        属性名称。属性名称只能包含小写英文字母([a-z])、数字([0-9])、下划线(_)，下划线不能出现在开始或结尾，下划线不能连续出现，长度为1到32个字符

        :param name: The name of this MessageAttribute.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this MessageAttribute.

        属性类型 STRING：字符串（String）类型 STRING_ARRAY：字符串数组（String.Array）类型 PROTOCOL：协议类型

        :return: The type of this MessageAttribute.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MessageAttribute.

        属性类型 STRING：字符串（String）类型 STRING_ARRAY：字符串数组（String.Array）类型 PROTOCOL：协议类型

        :param type: The type of this MessageAttribute.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this MessageAttribute.

        属性值。 当属性类型为“STRING”时，属性值只能包含中英文、数字、下划线，长度为1到32个字符。 当属性类型为“STRING_ARRAY”时，属性值为字符串数组，数组长度为1到10，数组中的元素内容不能重复，数组中的每个字符串都只能包含中英文、数字、下划线，且长度为1到32个字符。 当属性类型为“PROTOCOL”时，属性值为支持协议类型的字符串数组。

        :return: The value of this MessageAttribute.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this MessageAttribute.

        属性值。 当属性类型为“STRING”时，属性值只能包含中英文、数字、下划线，长度为1到32个字符。 当属性类型为“STRING_ARRAY”时，属性值为字符串数组，数组长度为1到10，数组中的元素内容不能重复，数组中的每个字符串都只能包含中英文、数字、下划线，且长度为1到32个字符。 当属性类型为“PROTOCOL”时，属性值为支持协议类型的字符串数组。

        :param value: The value of this MessageAttribute.
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
        if not isinstance(other, MessageAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
