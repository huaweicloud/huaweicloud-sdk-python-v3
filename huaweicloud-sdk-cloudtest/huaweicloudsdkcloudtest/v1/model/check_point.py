# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckPoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'comparison': 'str',
        'description': 'str',
        'function_arg': 'str',
        'function_type': 'str',
        '_property': 'str',
        'value': 'str'
    }

    attribute_map = {
        'comparison': 'comparison',
        'description': 'description',
        'function_arg': 'function_arg',
        'function_type': 'function_type',
        '_property': 'property',
        'value': 'value'
    }

    def __init__(self, comparison=None, description=None, function_arg=None, function_type=None, _property=None, value=None):
        r"""CheckPoint

        The model defined in huaweicloud sdk

        :param comparison: 运算符
        :type comparison: str
        :param description: 描述信息
        :type description: str
        :param function_arg: 响应提取时要使用什么方法处理参数
        :type function_arg: str
        :param function_type: 响应提取时要使用什么方法处理参数
        :type function_type: str
        :param _property: 属性名称
        :type _property: str
        :param value: 值
        :type value: str
        """
        
        

        self._comparison = None
        self._description = None
        self._function_arg = None
        self._function_type = None
        self.__property = None
        self._value = None
        self.discriminator = None

        if comparison is not None:
            self.comparison = comparison
        if description is not None:
            self.description = description
        if function_arg is not None:
            self.function_arg = function_arg
        if function_type is not None:
            self.function_type = function_type
        if _property is not None:
            self._property = _property
        if value is not None:
            self.value = value

    @property
    def comparison(self):
        r"""Gets the comparison of this CheckPoint.

        运算符

        :return: The comparison of this CheckPoint.
        :rtype: str
        """
        return self._comparison

    @comparison.setter
    def comparison(self, comparison):
        r"""Sets the comparison of this CheckPoint.

        运算符

        :param comparison: The comparison of this CheckPoint.
        :type comparison: str
        """
        self._comparison = comparison

    @property
    def description(self):
        r"""Gets the description of this CheckPoint.

        描述信息

        :return: The description of this CheckPoint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CheckPoint.

        描述信息

        :param description: The description of this CheckPoint.
        :type description: str
        """
        self._description = description

    @property
    def function_arg(self):
        r"""Gets the function_arg of this CheckPoint.

        响应提取时要使用什么方法处理参数

        :return: The function_arg of this CheckPoint.
        :rtype: str
        """
        return self._function_arg

    @function_arg.setter
    def function_arg(self, function_arg):
        r"""Sets the function_arg of this CheckPoint.

        响应提取时要使用什么方法处理参数

        :param function_arg: The function_arg of this CheckPoint.
        :type function_arg: str
        """
        self._function_arg = function_arg

    @property
    def function_type(self):
        r"""Gets the function_type of this CheckPoint.

        响应提取时要使用什么方法处理参数

        :return: The function_type of this CheckPoint.
        :rtype: str
        """
        return self._function_type

    @function_type.setter
    def function_type(self, function_type):
        r"""Sets the function_type of this CheckPoint.

        响应提取时要使用什么方法处理参数

        :param function_type: The function_type of this CheckPoint.
        :type function_type: str
        """
        self._function_type = function_type

    @property
    def _property(self):
        r"""Gets the _property of this CheckPoint.

        属性名称

        :return: The _property of this CheckPoint.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        r"""Sets the _property of this CheckPoint.

        属性名称

        :param _property: The _property of this CheckPoint.
        :type _property: str
        """
        self.__property = _property

    @property
    def value(self):
        r"""Gets the value of this CheckPoint.

        值

        :return: The value of this CheckPoint.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CheckPoint.

        值

        :param value: The value of this CheckPoint.
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
        if not isinstance(other, CheckPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
