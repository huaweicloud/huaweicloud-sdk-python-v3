# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ItemParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_value': 'AwParamBasicValue',
        'default_value': 'str',
        'enum_type': 'str',
        'enum_type_selected': 'str',
        'format': 'str',
        'is_big_field': 'bool',
        'max_items': 'int',
        'max_length': 'int',
        'maximum': 'Number',
        'min_items': 'int',
        'min_length': 'int',
        'minimum': 'Number',
        'pattern': 'str',
        'type': 'str',
        'validate_rule': 'ValidateRule',
        'value_type': 'int',
        'x_choice_value': 'str'
    }

    attribute_map = {
        'basic_value': 'basic_value',
        'default_value': 'defaultValue',
        'enum_type': 'enum_type',
        'enum_type_selected': 'enum_type_selected',
        'format': 'format',
        'is_big_field': 'is_big_field',
        'max_items': 'maxItems',
        'max_length': 'maxLength',
        'maximum': 'maximum',
        'min_items': 'minItems',
        'min_length': 'minLength',
        'minimum': 'minimum',
        'pattern': 'pattern',
        'type': 'type',
        'validate_rule': 'validate_rule',
        'value_type': 'value_type',
        'x_choice_value': 'xChoiceValue'
    }

    def __init__(self, basic_value=None, default_value=None, enum_type=None, enum_type_selected=None, format=None, is_big_field=None, max_items=None, max_length=None, maximum=None, min_items=None, min_length=None, minimum=None, pattern=None, type=None, validate_rule=None, value_type=None, x_choice_value=None):
        """ItemParam

        The model defined in huaweicloud sdk

        :param basic_value: 
        :type basic_value: :class:`huaweicloudsdkcloudtest.v1.AwParamBasicValue`
        :param default_value: 默认值
        :type default_value: str
        :param enum_type: 枚举类型
        :type enum_type: str
        :param enum_type_selected: 当前选中的枚举类型
        :type enum_type_selected: str
        :param format: num和String有效
        :type format: str
        :param is_big_field: 是否是大字段参数
        :type is_big_field: bool
        :param max_items: Array类型最大元素数
        :type max_items: int
        :param max_length: String类型最大长度
        :type max_length: int
        :param maximum: 
        :type maximum: :class:`huaweicloudsdkcloudtest.v1.Number`
        :param min_items: Array类型最小元素数
        :type min_items: int
        :param min_length: String类型最小长度
        :type min_length: int
        :param minimum: 
        :type minimum: :class:`huaweicloudsdkcloudtest.v1.Number`
        :param pattern: num和String有效
        :type pattern: str
        :param type: 参数类型
        :type type: str
        :param validate_rule: 
        :type validate_rule: :class:`huaweicloudsdkcloudtest.v1.ValidateRule`
        :param value_type: 参数值类型 0-基本类型，type字段为String,Integer等基本类型 1-基本类型数组,type字段为List&lt;String&gt;,List&lt;Integer&gt;等基本类型List 2-结构体，type字段为除了基本类型以外的结构体 3-结构体数组，type字段为List&lt;结构体&gt; 5-前端枚举类型
        :type value_type: int
        :param x_choice_value: choice选择关系
        :type x_choice_value: str
        """
        
        

        self._basic_value = None
        self._default_value = None
        self._enum_type = None
        self._enum_type_selected = None
        self._format = None
        self._is_big_field = None
        self._max_items = None
        self._max_length = None
        self._maximum = None
        self._min_items = None
        self._min_length = None
        self._minimum = None
        self._pattern = None
        self._type = None
        self._validate_rule = None
        self._value_type = None
        self._x_choice_value = None
        self.discriminator = None

        if basic_value is not None:
            self.basic_value = basic_value
        if default_value is not None:
            self.default_value = default_value
        if enum_type is not None:
            self.enum_type = enum_type
        if enum_type_selected is not None:
            self.enum_type_selected = enum_type_selected
        if format is not None:
            self.format = format
        if is_big_field is not None:
            self.is_big_field = is_big_field
        if max_items is not None:
            self.max_items = max_items
        if max_length is not None:
            self.max_length = max_length
        if maximum is not None:
            self.maximum = maximum
        if min_items is not None:
            self.min_items = min_items
        if min_length is not None:
            self.min_length = min_length
        if minimum is not None:
            self.minimum = minimum
        if pattern is not None:
            self.pattern = pattern
        if type is not None:
            self.type = type
        if validate_rule is not None:
            self.validate_rule = validate_rule
        if value_type is not None:
            self.value_type = value_type
        if x_choice_value is not None:
            self.x_choice_value = x_choice_value

    @property
    def basic_value(self):
        """Gets the basic_value of this ItemParam.

        :return: The basic_value of this ItemParam.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AwParamBasicValue`
        """
        return self._basic_value

    @basic_value.setter
    def basic_value(self, basic_value):
        """Sets the basic_value of this ItemParam.

        :param basic_value: The basic_value of this ItemParam.
        :type basic_value: :class:`huaweicloudsdkcloudtest.v1.AwParamBasicValue`
        """
        self._basic_value = basic_value

    @property
    def default_value(self):
        """Gets the default_value of this ItemParam.

        默认值

        :return: The default_value of this ItemParam.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this ItemParam.

        默认值

        :param default_value: The default_value of this ItemParam.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def enum_type(self):
        """Gets the enum_type of this ItemParam.

        枚举类型

        :return: The enum_type of this ItemParam.
        :rtype: str
        """
        return self._enum_type

    @enum_type.setter
    def enum_type(self, enum_type):
        """Sets the enum_type of this ItemParam.

        枚举类型

        :param enum_type: The enum_type of this ItemParam.
        :type enum_type: str
        """
        self._enum_type = enum_type

    @property
    def enum_type_selected(self):
        """Gets the enum_type_selected of this ItemParam.

        当前选中的枚举类型

        :return: The enum_type_selected of this ItemParam.
        :rtype: str
        """
        return self._enum_type_selected

    @enum_type_selected.setter
    def enum_type_selected(self, enum_type_selected):
        """Sets the enum_type_selected of this ItemParam.

        当前选中的枚举类型

        :param enum_type_selected: The enum_type_selected of this ItemParam.
        :type enum_type_selected: str
        """
        self._enum_type_selected = enum_type_selected

    @property
    def format(self):
        """Gets the format of this ItemParam.

        num和String有效

        :return: The format of this ItemParam.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ItemParam.

        num和String有效

        :param format: The format of this ItemParam.
        :type format: str
        """
        self._format = format

    @property
    def is_big_field(self):
        """Gets the is_big_field of this ItemParam.

        是否是大字段参数

        :return: The is_big_field of this ItemParam.
        :rtype: bool
        """
        return self._is_big_field

    @is_big_field.setter
    def is_big_field(self, is_big_field):
        """Sets the is_big_field of this ItemParam.

        是否是大字段参数

        :param is_big_field: The is_big_field of this ItemParam.
        :type is_big_field: bool
        """
        self._is_big_field = is_big_field

    @property
    def max_items(self):
        """Gets the max_items of this ItemParam.

        Array类型最大元素数

        :return: The max_items of this ItemParam.
        :rtype: int
        """
        return self._max_items

    @max_items.setter
    def max_items(self, max_items):
        """Sets the max_items of this ItemParam.

        Array类型最大元素数

        :param max_items: The max_items of this ItemParam.
        :type max_items: int
        """
        self._max_items = max_items

    @property
    def max_length(self):
        """Gets the max_length of this ItemParam.

        String类型最大长度

        :return: The max_length of this ItemParam.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this ItemParam.

        String类型最大长度

        :param max_length: The max_length of this ItemParam.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def maximum(self):
        """Gets the maximum of this ItemParam.

        :return: The maximum of this ItemParam.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.Number`
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this ItemParam.

        :param maximum: The maximum of this ItemParam.
        :type maximum: :class:`huaweicloudsdkcloudtest.v1.Number`
        """
        self._maximum = maximum

    @property
    def min_items(self):
        """Gets the min_items of this ItemParam.

        Array类型最小元素数

        :return: The min_items of this ItemParam.
        :rtype: int
        """
        return self._min_items

    @min_items.setter
    def min_items(self, min_items):
        """Sets the min_items of this ItemParam.

        Array类型最小元素数

        :param min_items: The min_items of this ItemParam.
        :type min_items: int
        """
        self._min_items = min_items

    @property
    def min_length(self):
        """Gets the min_length of this ItemParam.

        String类型最小长度

        :return: The min_length of this ItemParam.
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this ItemParam.

        String类型最小长度

        :param min_length: The min_length of this ItemParam.
        :type min_length: int
        """
        self._min_length = min_length

    @property
    def minimum(self):
        """Gets the minimum of this ItemParam.

        :return: The minimum of this ItemParam.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.Number`
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this ItemParam.

        :param minimum: The minimum of this ItemParam.
        :type minimum: :class:`huaweicloudsdkcloudtest.v1.Number`
        """
        self._minimum = minimum

    @property
    def pattern(self):
        """Gets the pattern of this ItemParam.

        num和String有效

        :return: The pattern of this ItemParam.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this ItemParam.

        num和String有效

        :param pattern: The pattern of this ItemParam.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def type(self):
        """Gets the type of this ItemParam.

        参数类型

        :return: The type of this ItemParam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ItemParam.

        参数类型

        :param type: The type of this ItemParam.
        :type type: str
        """
        self._type = type

    @property
    def validate_rule(self):
        """Gets the validate_rule of this ItemParam.

        :return: The validate_rule of this ItemParam.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ValidateRule`
        """
        return self._validate_rule

    @validate_rule.setter
    def validate_rule(self, validate_rule):
        """Sets the validate_rule of this ItemParam.

        :param validate_rule: The validate_rule of this ItemParam.
        :type validate_rule: :class:`huaweicloudsdkcloudtest.v1.ValidateRule`
        """
        self._validate_rule = validate_rule

    @property
    def value_type(self):
        """Gets the value_type of this ItemParam.

        参数值类型 0-基本类型，type字段为String,Integer等基本类型 1-基本类型数组,type字段为List<String>,List<Integer>等基本类型List 2-结构体，type字段为除了基本类型以外的结构体 3-结构体数组，type字段为List<结构体> 5-前端枚举类型

        :return: The value_type of this ItemParam.
        :rtype: int
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this ItemParam.

        参数值类型 0-基本类型，type字段为String,Integer等基本类型 1-基本类型数组,type字段为List<String>,List<Integer>等基本类型List 2-结构体，type字段为除了基本类型以外的结构体 3-结构体数组，type字段为List<结构体> 5-前端枚举类型

        :param value_type: The value_type of this ItemParam.
        :type value_type: int
        """
        self._value_type = value_type

    @property
    def x_choice_value(self):
        """Gets the x_choice_value of this ItemParam.

        choice选择关系

        :return: The x_choice_value of this ItemParam.
        :rtype: str
        """
        return self._x_choice_value

    @x_choice_value.setter
    def x_choice_value(self, x_choice_value):
        """Sets the x_choice_value of this ItemParam.

        choice选择关系

        :param x_choice_value: The x_choice_value of this ItemParam.
        :type x_choice_value: str
        """
        self._x_choice_value = x_choice_value

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
        if not isinstance(other, ItemParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
