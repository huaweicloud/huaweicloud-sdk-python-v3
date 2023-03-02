# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransForm:

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
        'value': 'str',
        'template': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'template': 'template'
    }

    def __init__(self, type=None, value=None, template=None):
        """TransForm

        The model defined in huaweicloud sdk

        :param type: 转换规则类型
        :type type: str
        :param value: 常量类型规则时，字段为常量内容定义； 变量类型规则时，为变量定义，内容必须为JsonObject字符串。 变量最多支持100个，且不支持嵌套结构定义； 变量名由字母、数字、点、下划线和中划线组成，必须字母或数字开头不能以HC.开头，长度不超过64个字符； 变量值表达式支持常量或JsonPath表达式，字符串长度不超过1024个字符。
        :type value: str
        :param template: 变量类型规则时，规则内容的模板定义，支持对已定义变量的引用。
        :type template: str
        """
        
        

        self._type = None
        self._value = None
        self._template = None
        self.discriminator = None

        self.type = type
        if value is not None:
            self.value = value
        if template is not None:
            self.template = template

    @property
    def type(self):
        """Gets the type of this TransForm.

        转换规则类型

        :return: The type of this TransForm.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransForm.

        转换规则类型

        :param type: The type of this TransForm.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this TransForm.

        常量类型规则时，字段为常量内容定义； 变量类型规则时，为变量定义，内容必须为JsonObject字符串。 变量最多支持100个，且不支持嵌套结构定义； 变量名由字母、数字、点、下划线和中划线组成，必须字母或数字开头不能以HC.开头，长度不超过64个字符； 变量值表达式支持常量或JsonPath表达式，字符串长度不超过1024个字符。

        :return: The value of this TransForm.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TransForm.

        常量类型规则时，字段为常量内容定义； 变量类型规则时，为变量定义，内容必须为JsonObject字符串。 变量最多支持100个，且不支持嵌套结构定义； 变量名由字母、数字、点、下划线和中划线组成，必须字母或数字开头不能以HC.开头，长度不超过64个字符； 变量值表达式支持常量或JsonPath表达式，字符串长度不超过1024个字符。

        :param value: The value of this TransForm.
        :type value: str
        """
        self._value = value

    @property
    def template(self):
        """Gets the template of this TransForm.

        变量类型规则时，规则内容的模板定义，支持对已定义变量的引用。

        :return: The template of this TransForm.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this TransForm.

        变量类型规则时，规则内容的模板定义，支持对已定义变量的引用。

        :param template: The template of this TransForm.
        :type template: str
        """
        self._template = template

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
        if not isinstance(other, TransForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
