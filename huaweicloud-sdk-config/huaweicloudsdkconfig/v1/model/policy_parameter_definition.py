# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyParameterDefinition:

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
        'description': 'str',
        'allowed_values': 'list[object]',
        'default_value': 'str',
        'minimum': 'float',
        'maximum': 'float',
        'min_items': 'int',
        'max_items': 'int',
        'min_length': 'int',
        'max_length': 'int',
        'pattern': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'allowed_values': 'allowed_values',
        'default_value': 'default_value',
        'minimum': 'minimum',
        'maximum': 'maximum',
        'min_items': 'min_items',
        'max_items': 'max_items',
        'min_length': 'min_length',
        'max_length': 'max_length',
        'pattern': 'pattern',
        'type': 'type'
    }

    def __init__(self, name=None, description=None, allowed_values=None, default_value=None, minimum=None, maximum=None, min_items=None, max_items=None, min_length=None, max_length=None, pattern=None, type=None):
        r"""PolicyParameterDefinition

        The model defined in huaweicloud sdk

        :param name: 策略参数名字
        :type name: str
        :param description: 策略参数描述
        :type description: str
        :param allowed_values: 策略参数允许值列表
        :type allowed_values: list[object]
        :param default_value: 策略参数默认值
        :type default_value: str
        :param minimum: 策略参数的最小值，当参数类型为Integer或Float时生效。
        :type minimum: float
        :param maximum: 策略参数的最大值，当参数类型为Integer或Float时生效。
        :type maximum: float
        :param min_items: 策略参数的最小项数，当参数类型为Array时生效。
        :type min_items: int
        :param max_items: 策略参数的最大项数，当参数类型为Array时生效。
        :type max_items: int
        :param min_length: 策略参数的最小字符串长度或每项的最小字符串长度，当参数类型为String或Array时生效。
        :type min_length: int
        :param max_length: 策略参数的最大字符串长度或每项的最大字符串长度，当参数类型为String或Array时生效。
        :type max_length: int
        :param pattern: 策略参数的字符串正则要求或每项的字符串正则要求，当参数类型为String或Array时生效。
        :type pattern: str
        :param type: 策略参数类型
        :type type: str
        """
        
        

        self._name = None
        self._description = None
        self._allowed_values = None
        self._default_value = None
        self._minimum = None
        self._maximum = None
        self._min_items = None
        self._max_items = None
        self._min_length = None
        self._max_length = None
        self._pattern = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if allowed_values is not None:
            self.allowed_values = allowed_values
        if default_value is not None:
            self.default_value = default_value
        if minimum is not None:
            self.minimum = minimum
        if maximum is not None:
            self.maximum = maximum
        if min_items is not None:
            self.min_items = min_items
        if max_items is not None:
            self.max_items = max_items
        if min_length is not None:
            self.min_length = min_length
        if max_length is not None:
            self.max_length = max_length
        if pattern is not None:
            self.pattern = pattern
        if type is not None:
            self.type = type

    @property
    def name(self):
        r"""Gets the name of this PolicyParameterDefinition.

        策略参数名字

        :return: The name of this PolicyParameterDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PolicyParameterDefinition.

        策略参数名字

        :param name: The name of this PolicyParameterDefinition.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this PolicyParameterDefinition.

        策略参数描述

        :return: The description of this PolicyParameterDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PolicyParameterDefinition.

        策略参数描述

        :param description: The description of this PolicyParameterDefinition.
        :type description: str
        """
        self._description = description

    @property
    def allowed_values(self):
        r"""Gets the allowed_values of this PolicyParameterDefinition.

        策略参数允许值列表

        :return: The allowed_values of this PolicyParameterDefinition.
        :rtype: list[object]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        r"""Sets the allowed_values of this PolicyParameterDefinition.

        策略参数允许值列表

        :param allowed_values: The allowed_values of this PolicyParameterDefinition.
        :type allowed_values: list[object]
        """
        self._allowed_values = allowed_values

    @property
    def default_value(self):
        r"""Gets the default_value of this PolicyParameterDefinition.

        策略参数默认值

        :return: The default_value of this PolicyParameterDefinition.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this PolicyParameterDefinition.

        策略参数默认值

        :param default_value: The default_value of this PolicyParameterDefinition.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def minimum(self):
        r"""Gets the minimum of this PolicyParameterDefinition.

        策略参数的最小值，当参数类型为Integer或Float时生效。

        :return: The minimum of this PolicyParameterDefinition.
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        r"""Sets the minimum of this PolicyParameterDefinition.

        策略参数的最小值，当参数类型为Integer或Float时生效。

        :param minimum: The minimum of this PolicyParameterDefinition.
        :type minimum: float
        """
        self._minimum = minimum

    @property
    def maximum(self):
        r"""Gets the maximum of this PolicyParameterDefinition.

        策略参数的最大值，当参数类型为Integer或Float时生效。

        :return: The maximum of this PolicyParameterDefinition.
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        r"""Sets the maximum of this PolicyParameterDefinition.

        策略参数的最大值，当参数类型为Integer或Float时生效。

        :param maximum: The maximum of this PolicyParameterDefinition.
        :type maximum: float
        """
        self._maximum = maximum

    @property
    def min_items(self):
        r"""Gets the min_items of this PolicyParameterDefinition.

        策略参数的最小项数，当参数类型为Array时生效。

        :return: The min_items of this PolicyParameterDefinition.
        :rtype: int
        """
        return self._min_items

    @min_items.setter
    def min_items(self, min_items):
        r"""Sets the min_items of this PolicyParameterDefinition.

        策略参数的最小项数，当参数类型为Array时生效。

        :param min_items: The min_items of this PolicyParameterDefinition.
        :type min_items: int
        """
        self._min_items = min_items

    @property
    def max_items(self):
        r"""Gets the max_items of this PolicyParameterDefinition.

        策略参数的最大项数，当参数类型为Array时生效。

        :return: The max_items of this PolicyParameterDefinition.
        :rtype: int
        """
        return self._max_items

    @max_items.setter
    def max_items(self, max_items):
        r"""Sets the max_items of this PolicyParameterDefinition.

        策略参数的最大项数，当参数类型为Array时生效。

        :param max_items: The max_items of this PolicyParameterDefinition.
        :type max_items: int
        """
        self._max_items = max_items

    @property
    def min_length(self):
        r"""Gets the min_length of this PolicyParameterDefinition.

        策略参数的最小字符串长度或每项的最小字符串长度，当参数类型为String或Array时生效。

        :return: The min_length of this PolicyParameterDefinition.
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        r"""Sets the min_length of this PolicyParameterDefinition.

        策略参数的最小字符串长度或每项的最小字符串长度，当参数类型为String或Array时生效。

        :param min_length: The min_length of this PolicyParameterDefinition.
        :type min_length: int
        """
        self._min_length = min_length

    @property
    def max_length(self):
        r"""Gets the max_length of this PolicyParameterDefinition.

        策略参数的最大字符串长度或每项的最大字符串长度，当参数类型为String或Array时生效。

        :return: The max_length of this PolicyParameterDefinition.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        r"""Sets the max_length of this PolicyParameterDefinition.

        策略参数的最大字符串长度或每项的最大字符串长度，当参数类型为String或Array时生效。

        :param max_length: The max_length of this PolicyParameterDefinition.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def pattern(self):
        r"""Gets the pattern of this PolicyParameterDefinition.

        策略参数的字符串正则要求或每项的字符串正则要求，当参数类型为String或Array时生效。

        :return: The pattern of this PolicyParameterDefinition.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        r"""Sets the pattern of this PolicyParameterDefinition.

        策略参数的字符串正则要求或每项的字符串正则要求，当参数类型为String或Array时生效。

        :param pattern: The pattern of this PolicyParameterDefinition.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def type(self):
        r"""Gets the type of this PolicyParameterDefinition.

        策略参数类型

        :return: The type of this PolicyParameterDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PolicyParameterDefinition.

        策略参数类型

        :param type: The type of this PolicyParameterDefinition.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, PolicyParameterDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
