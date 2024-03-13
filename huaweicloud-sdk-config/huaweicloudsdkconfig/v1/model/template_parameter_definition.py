# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateParameterDefinition:

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
        'default_value': 'object',
        'allowed_values': 'list[object]',
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
        'default_value': 'default_value',
        'allowed_values': 'allowed_values',
        'minimum': 'minimum',
        'maximum': 'maximum',
        'min_items': 'min_items',
        'max_items': 'max_items',
        'min_length': 'min_length',
        'max_length': 'max_length',
        'pattern': 'pattern',
        'type': 'type'
    }

    def __init__(self, name=None, description=None, default_value=None, allowed_values=None, minimum=None, maximum=None, min_items=None, max_items=None, min_length=None, max_length=None, pattern=None, type=None):
        """TemplateParameterDefinition

        The model defined in huaweicloud sdk

        :param name: 预定义合规包模板参数名字。
        :type name: str
        :param description: 预定义合规包模板参数描述。
        :type description: str
        :param default_value: 预定义合规包模板参数默认值。
        :type default_value: object
        :param allowed_values: 预定义合规包模板参数允许值列表。
        :type allowed_values: list[object]
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
        :param type: 预定义合规包模板参数类型。
        :type type: str
        """
        
        

        self._name = None
        self._description = None
        self._default_value = None
        self._allowed_values = None
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
        if default_value is not None:
            self.default_value = default_value
        if allowed_values is not None:
            self.allowed_values = allowed_values
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
        """Gets the name of this TemplateParameterDefinition.

        预定义合规包模板参数名字。

        :return: The name of this TemplateParameterDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateParameterDefinition.

        预定义合规包模板参数名字。

        :param name: The name of this TemplateParameterDefinition.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this TemplateParameterDefinition.

        预定义合规包模板参数描述。

        :return: The description of this TemplateParameterDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateParameterDefinition.

        预定义合规包模板参数描述。

        :param description: The description of this TemplateParameterDefinition.
        :type description: str
        """
        self._description = description

    @property
    def default_value(self):
        """Gets the default_value of this TemplateParameterDefinition.

        预定义合规包模板参数默认值。

        :return: The default_value of this TemplateParameterDefinition.
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this TemplateParameterDefinition.

        预定义合规包模板参数默认值。

        :param default_value: The default_value of this TemplateParameterDefinition.
        :type default_value: object
        """
        self._default_value = default_value

    @property
    def allowed_values(self):
        """Gets the allowed_values of this TemplateParameterDefinition.

        预定义合规包模板参数允许值列表。

        :return: The allowed_values of this TemplateParameterDefinition.
        :rtype: list[object]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """Sets the allowed_values of this TemplateParameterDefinition.

        预定义合规包模板参数允许值列表。

        :param allowed_values: The allowed_values of this TemplateParameterDefinition.
        :type allowed_values: list[object]
        """
        self._allowed_values = allowed_values

    @property
    def minimum(self):
        """Gets the minimum of this TemplateParameterDefinition.

        策略参数的最小值，当参数类型为Integer或Float时生效。

        :return: The minimum of this TemplateParameterDefinition.
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this TemplateParameterDefinition.

        策略参数的最小值，当参数类型为Integer或Float时生效。

        :param minimum: The minimum of this TemplateParameterDefinition.
        :type minimum: float
        """
        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this TemplateParameterDefinition.

        策略参数的最大值，当参数类型为Integer或Float时生效。

        :return: The maximum of this TemplateParameterDefinition.
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this TemplateParameterDefinition.

        策略参数的最大值，当参数类型为Integer或Float时生效。

        :param maximum: The maximum of this TemplateParameterDefinition.
        :type maximum: float
        """
        self._maximum = maximum

    @property
    def min_items(self):
        """Gets the min_items of this TemplateParameterDefinition.

        策略参数的最小项数，当参数类型为Array时生效。

        :return: The min_items of this TemplateParameterDefinition.
        :rtype: int
        """
        return self._min_items

    @min_items.setter
    def min_items(self, min_items):
        """Sets the min_items of this TemplateParameterDefinition.

        策略参数的最小项数，当参数类型为Array时生效。

        :param min_items: The min_items of this TemplateParameterDefinition.
        :type min_items: int
        """
        self._min_items = min_items

    @property
    def max_items(self):
        """Gets the max_items of this TemplateParameterDefinition.

        策略参数的最大项数，当参数类型为Array时生效。

        :return: The max_items of this TemplateParameterDefinition.
        :rtype: int
        """
        return self._max_items

    @max_items.setter
    def max_items(self, max_items):
        """Sets the max_items of this TemplateParameterDefinition.

        策略参数的最大项数，当参数类型为Array时生效。

        :param max_items: The max_items of this TemplateParameterDefinition.
        :type max_items: int
        """
        self._max_items = max_items

    @property
    def min_length(self):
        """Gets the min_length of this TemplateParameterDefinition.

        策略参数的最小字符串长度或每项的最小字符串长度，当参数类型为String或Array时生效。

        :return: The min_length of this TemplateParameterDefinition.
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this TemplateParameterDefinition.

        策略参数的最小字符串长度或每项的最小字符串长度，当参数类型为String或Array时生效。

        :param min_length: The min_length of this TemplateParameterDefinition.
        :type min_length: int
        """
        self._min_length = min_length

    @property
    def max_length(self):
        """Gets the max_length of this TemplateParameterDefinition.

        策略参数的最大字符串长度或每项的最大字符串长度，当参数类型为String或Array时生效。

        :return: The max_length of this TemplateParameterDefinition.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this TemplateParameterDefinition.

        策略参数的最大字符串长度或每项的最大字符串长度，当参数类型为String或Array时生效。

        :param max_length: The max_length of this TemplateParameterDefinition.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def pattern(self):
        """Gets the pattern of this TemplateParameterDefinition.

        策略参数的字符串正则要求或每项的字符串正则要求，当参数类型为String或Array时生效。

        :return: The pattern of this TemplateParameterDefinition.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this TemplateParameterDefinition.

        策略参数的字符串正则要求或每项的字符串正则要求，当参数类型为String或Array时生效。

        :param pattern: The pattern of this TemplateParameterDefinition.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def type(self):
        """Gets the type of this TemplateParameterDefinition.

        预定义合规包模板参数类型。

        :return: The type of this TemplateParameterDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TemplateParameterDefinition.

        预定义合规包模板参数类型。

        :param type: The type of this TemplateParameterDefinition.
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
        if not isinstance(other, TemplateParameterDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
