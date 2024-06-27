# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AwParam:

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
        'basic_value_list': 'list[AwParamBasicValue]',
        'custom_body': 'str',
        'default_value': 'str',
        'description': 'str',
        'disabled': 'bool',
        'drop_down_value': 'str',
        'enum_type': 'str',
        'enum_type_selected': 'str',
        'format': 'str',
        'in_type': 'int',
        'is_checked': 'bool',
        'is_big_field': 'bool',
        'is_body_custom': 'int',
        'is_contract_param': 'int',
        'is_sensitive': 'bool',
        'item': 'ItemParam',
        'max_items': 'int',
        'max_length': 'int',
        'maximum': 'Number',
        'min_items': 'int',
        'min_length': 'int',
        'minimum': 'Number',
        'mock': 'MockInfo',
        'name': 'str',
        'object_value': 'list[AwParam]',
        'object_value_list': 'list[list[AwParam]]',
        'pattern': 'str',
        'required': 'bool',
        'type': 'str',
        'validate_rule': 'ValidateRule',
        'value_type': 'int',
        'x_choice_value': 'str'
    }

    attribute_map = {
        'basic_value': 'basic_value',
        'basic_value_list': 'basic_value_list',
        'custom_body': 'custom_body',
        'default_value': 'defaultValue',
        'description': 'description',
        'disabled': 'disabled',
        'drop_down_value': 'drop_down_value',
        'enum_type': 'enum_type',
        'enum_type_selected': 'enum_type_selected',
        'format': 'format',
        'in_type': 'in_type',
        'is_checked': 'isChecked',
        'is_big_field': 'is_big_field',
        'is_body_custom': 'is_body_custom',
        'is_contract_param': 'is_contract_param',
        'is_sensitive': 'is_sensitive',
        'item': 'item',
        'max_items': 'maxItems',
        'max_length': 'maxLength',
        'maximum': 'maximum',
        'min_items': 'minItems',
        'min_length': 'minLength',
        'minimum': 'minimum',
        'mock': 'mock',
        'name': 'name',
        'object_value': 'object_value',
        'object_value_list': 'object_value_list',
        'pattern': 'pattern',
        'required': 'required',
        'type': 'type',
        'validate_rule': 'validate_rule',
        'value_type': 'value_type',
        'x_choice_value': 'xChoiceValue'
    }

    def __init__(self, basic_value=None, basic_value_list=None, custom_body=None, default_value=None, description=None, disabled=None, drop_down_value=None, enum_type=None, enum_type_selected=None, format=None, in_type=None, is_checked=None, is_big_field=None, is_body_custom=None, is_contract_param=None, is_sensitive=None, item=None, max_items=None, max_length=None, maximum=None, min_items=None, min_length=None, minimum=None, mock=None, name=None, object_value=None, object_value_list=None, pattern=None, required=None, type=None, validate_rule=None, value_type=None, x_choice_value=None):
        """AwParam

        The model defined in huaweicloud sdk

        :param basic_value: 
        :type basic_value: :class:`huaweicloudsdkcloudtest.v1.AwParamBasicValue`
        :param basic_value_list: valueType为1时该值有效
        :type basic_value_list: list[:class:`huaweicloudsdkcloudtest.v1.AwParamBasicValue`]
        :param custom_body: 自定义requestBody内容,inType为2且isBodyCustom为1时有效
        :type custom_body: str
        :param default_value: 默认值
        :type default_value: str
        :param description: aw参数描述
        :type description: str
        :param disabled: 是否禁用 只有非必需参数才能被禁用
        :type disabled: bool
        :param drop_down_value: 用于存储下拉菜单的值
        :type drop_down_value: str
        :param enum_type: 枚举类型
        :type enum_type: str
        :param enum_type_selected: 当前选中的枚举类型
        :type enum_type_selected: str
        :param format: num和String有效
        :type format: str
        :param in_type: rest接口输入参数类型 0-query 1-path 2-body 3-header 4-formdata 5-config
        :type in_type: int
        :param is_checked: 是否是被选中参数
        :type is_checked: bool
        :param is_big_field: 是否是大字段参数
        :type is_big_field: bool
        :param is_body_custom: requestBody是否自定义，inType为2时有效。0-非自定义，用原有逻辑；1-自定义body,requestBody直接使用字段customBody
        :type is_body_custom: int
        :param is_contract_param: 是否是契约AW 0-否；1-yes
        :type is_contract_param: int
        :param is_sensitive: 是否敏感参数，0  是，  1 不是
        :type is_sensitive: bool
        :param item: 
        :type item: :class:`huaweicloudsdkcloudtest.v1.ItemParam`
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
        :param mock: 
        :type mock: :class:`huaweicloudsdkcloudtest.v1.MockInfo`
        :param name: 参数名
        :type name: str
        :param object_value: valueType为2时该值有效。valueType为3时，该值用来表示数组中单个结构体
        :type object_value: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        :param object_value_list: valueType为3时该值有效
        :type object_value_list: list[list[AwParam]]
        :param pattern: num和String有效
        :type pattern: str
        :param required: 是否必需参数
        :type required: bool
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
        self._basic_value_list = None
        self._custom_body = None
        self._default_value = None
        self._description = None
        self._disabled = None
        self._drop_down_value = None
        self._enum_type = None
        self._enum_type_selected = None
        self._format = None
        self._in_type = None
        self._is_checked = None
        self._is_big_field = None
        self._is_body_custom = None
        self._is_contract_param = None
        self._is_sensitive = None
        self._item = None
        self._max_items = None
        self._max_length = None
        self._maximum = None
        self._min_items = None
        self._min_length = None
        self._minimum = None
        self._mock = None
        self._name = None
        self._object_value = None
        self._object_value_list = None
        self._pattern = None
        self._required = None
        self._type = None
        self._validate_rule = None
        self._value_type = None
        self._x_choice_value = None
        self.discriminator = None

        if basic_value is not None:
            self.basic_value = basic_value
        if basic_value_list is not None:
            self.basic_value_list = basic_value_list
        if custom_body is not None:
            self.custom_body = custom_body
        if default_value is not None:
            self.default_value = default_value
        if description is not None:
            self.description = description
        if disabled is not None:
            self.disabled = disabled
        if drop_down_value is not None:
            self.drop_down_value = drop_down_value
        if enum_type is not None:
            self.enum_type = enum_type
        if enum_type_selected is not None:
            self.enum_type_selected = enum_type_selected
        if format is not None:
            self.format = format
        if in_type is not None:
            self.in_type = in_type
        if is_checked is not None:
            self.is_checked = is_checked
        if is_big_field is not None:
            self.is_big_field = is_big_field
        if is_body_custom is not None:
            self.is_body_custom = is_body_custom
        if is_contract_param is not None:
            self.is_contract_param = is_contract_param
        if is_sensitive is not None:
            self.is_sensitive = is_sensitive
        if item is not None:
            self.item = item
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
        if mock is not None:
            self.mock = mock
        if name is not None:
            self.name = name
        if object_value is not None:
            self.object_value = object_value
        if object_value_list is not None:
            self.object_value_list = object_value_list
        if pattern is not None:
            self.pattern = pattern
        if required is not None:
            self.required = required
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
        """Gets the basic_value of this AwParam.

        :return: The basic_value of this AwParam.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AwParamBasicValue`
        """
        return self._basic_value

    @basic_value.setter
    def basic_value(self, basic_value):
        """Sets the basic_value of this AwParam.

        :param basic_value: The basic_value of this AwParam.
        :type basic_value: :class:`huaweicloudsdkcloudtest.v1.AwParamBasicValue`
        """
        self._basic_value = basic_value

    @property
    def basic_value_list(self):
        """Gets the basic_value_list of this AwParam.

        valueType为1时该值有效

        :return: The basic_value_list of this AwParam.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwParamBasicValue`]
        """
        return self._basic_value_list

    @basic_value_list.setter
    def basic_value_list(self, basic_value_list):
        """Sets the basic_value_list of this AwParam.

        valueType为1时该值有效

        :param basic_value_list: The basic_value_list of this AwParam.
        :type basic_value_list: list[:class:`huaweicloudsdkcloudtest.v1.AwParamBasicValue`]
        """
        self._basic_value_list = basic_value_list

    @property
    def custom_body(self):
        """Gets the custom_body of this AwParam.

        自定义requestBody内容,inType为2且isBodyCustom为1时有效

        :return: The custom_body of this AwParam.
        :rtype: str
        """
        return self._custom_body

    @custom_body.setter
    def custom_body(self, custom_body):
        """Sets the custom_body of this AwParam.

        自定义requestBody内容,inType为2且isBodyCustom为1时有效

        :param custom_body: The custom_body of this AwParam.
        :type custom_body: str
        """
        self._custom_body = custom_body

    @property
    def default_value(self):
        """Gets the default_value of this AwParam.

        默认值

        :return: The default_value of this AwParam.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this AwParam.

        默认值

        :param default_value: The default_value of this AwParam.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def description(self):
        """Gets the description of this AwParam.

        aw参数描述

        :return: The description of this AwParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AwParam.

        aw参数描述

        :param description: The description of this AwParam.
        :type description: str
        """
        self._description = description

    @property
    def disabled(self):
        """Gets the disabled of this AwParam.

        是否禁用 只有非必需参数才能被禁用

        :return: The disabled of this AwParam.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this AwParam.

        是否禁用 只有非必需参数才能被禁用

        :param disabled: The disabled of this AwParam.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def drop_down_value(self):
        """Gets the drop_down_value of this AwParam.

        用于存储下拉菜单的值

        :return: The drop_down_value of this AwParam.
        :rtype: str
        """
        return self._drop_down_value

    @drop_down_value.setter
    def drop_down_value(self, drop_down_value):
        """Sets the drop_down_value of this AwParam.

        用于存储下拉菜单的值

        :param drop_down_value: The drop_down_value of this AwParam.
        :type drop_down_value: str
        """
        self._drop_down_value = drop_down_value

    @property
    def enum_type(self):
        """Gets the enum_type of this AwParam.

        枚举类型

        :return: The enum_type of this AwParam.
        :rtype: str
        """
        return self._enum_type

    @enum_type.setter
    def enum_type(self, enum_type):
        """Sets the enum_type of this AwParam.

        枚举类型

        :param enum_type: The enum_type of this AwParam.
        :type enum_type: str
        """
        self._enum_type = enum_type

    @property
    def enum_type_selected(self):
        """Gets the enum_type_selected of this AwParam.

        当前选中的枚举类型

        :return: The enum_type_selected of this AwParam.
        :rtype: str
        """
        return self._enum_type_selected

    @enum_type_selected.setter
    def enum_type_selected(self, enum_type_selected):
        """Sets the enum_type_selected of this AwParam.

        当前选中的枚举类型

        :param enum_type_selected: The enum_type_selected of this AwParam.
        :type enum_type_selected: str
        """
        self._enum_type_selected = enum_type_selected

    @property
    def format(self):
        """Gets the format of this AwParam.

        num和String有效

        :return: The format of this AwParam.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AwParam.

        num和String有效

        :param format: The format of this AwParam.
        :type format: str
        """
        self._format = format

    @property
    def in_type(self):
        """Gets the in_type of this AwParam.

        rest接口输入参数类型 0-query 1-path 2-body 3-header 4-formdata 5-config

        :return: The in_type of this AwParam.
        :rtype: int
        """
        return self._in_type

    @in_type.setter
    def in_type(self, in_type):
        """Sets the in_type of this AwParam.

        rest接口输入参数类型 0-query 1-path 2-body 3-header 4-formdata 5-config

        :param in_type: The in_type of this AwParam.
        :type in_type: int
        """
        self._in_type = in_type

    @property
    def is_checked(self):
        """Gets the is_checked of this AwParam.

        是否是被选中参数

        :return: The is_checked of this AwParam.
        :rtype: bool
        """
        return self._is_checked

    @is_checked.setter
    def is_checked(self, is_checked):
        """Sets the is_checked of this AwParam.

        是否是被选中参数

        :param is_checked: The is_checked of this AwParam.
        :type is_checked: bool
        """
        self._is_checked = is_checked

    @property
    def is_big_field(self):
        """Gets the is_big_field of this AwParam.

        是否是大字段参数

        :return: The is_big_field of this AwParam.
        :rtype: bool
        """
        return self._is_big_field

    @is_big_field.setter
    def is_big_field(self, is_big_field):
        """Sets the is_big_field of this AwParam.

        是否是大字段参数

        :param is_big_field: The is_big_field of this AwParam.
        :type is_big_field: bool
        """
        self._is_big_field = is_big_field

    @property
    def is_body_custom(self):
        """Gets the is_body_custom of this AwParam.

        requestBody是否自定义，inType为2时有效。0-非自定义，用原有逻辑；1-自定义body,requestBody直接使用字段customBody

        :return: The is_body_custom of this AwParam.
        :rtype: int
        """
        return self._is_body_custom

    @is_body_custom.setter
    def is_body_custom(self, is_body_custom):
        """Sets the is_body_custom of this AwParam.

        requestBody是否自定义，inType为2时有效。0-非自定义，用原有逻辑；1-自定义body,requestBody直接使用字段customBody

        :param is_body_custom: The is_body_custom of this AwParam.
        :type is_body_custom: int
        """
        self._is_body_custom = is_body_custom

    @property
    def is_contract_param(self):
        """Gets the is_contract_param of this AwParam.

        是否是契约AW 0-否；1-yes

        :return: The is_contract_param of this AwParam.
        :rtype: int
        """
        return self._is_contract_param

    @is_contract_param.setter
    def is_contract_param(self, is_contract_param):
        """Sets the is_contract_param of this AwParam.

        是否是契约AW 0-否；1-yes

        :param is_contract_param: The is_contract_param of this AwParam.
        :type is_contract_param: int
        """
        self._is_contract_param = is_contract_param

    @property
    def is_sensitive(self):
        """Gets the is_sensitive of this AwParam.

        是否敏感参数，0  是，  1 不是

        :return: The is_sensitive of this AwParam.
        :rtype: bool
        """
        return self._is_sensitive

    @is_sensitive.setter
    def is_sensitive(self, is_sensitive):
        """Sets the is_sensitive of this AwParam.

        是否敏感参数，0  是，  1 不是

        :param is_sensitive: The is_sensitive of this AwParam.
        :type is_sensitive: bool
        """
        self._is_sensitive = is_sensitive

    @property
    def item(self):
        """Gets the item of this AwParam.

        :return: The item of this AwParam.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ItemParam`
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this AwParam.

        :param item: The item of this AwParam.
        :type item: :class:`huaweicloudsdkcloudtest.v1.ItemParam`
        """
        self._item = item

    @property
    def max_items(self):
        """Gets the max_items of this AwParam.

        Array类型最大元素数

        :return: The max_items of this AwParam.
        :rtype: int
        """
        return self._max_items

    @max_items.setter
    def max_items(self, max_items):
        """Sets the max_items of this AwParam.

        Array类型最大元素数

        :param max_items: The max_items of this AwParam.
        :type max_items: int
        """
        self._max_items = max_items

    @property
    def max_length(self):
        """Gets the max_length of this AwParam.

        String类型最大长度

        :return: The max_length of this AwParam.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this AwParam.

        String类型最大长度

        :param max_length: The max_length of this AwParam.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def maximum(self):
        """Gets the maximum of this AwParam.

        :return: The maximum of this AwParam.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.Number`
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this AwParam.

        :param maximum: The maximum of this AwParam.
        :type maximum: :class:`huaweicloudsdkcloudtest.v1.Number`
        """
        self._maximum = maximum

    @property
    def min_items(self):
        """Gets the min_items of this AwParam.

        Array类型最小元素数

        :return: The min_items of this AwParam.
        :rtype: int
        """
        return self._min_items

    @min_items.setter
    def min_items(self, min_items):
        """Sets the min_items of this AwParam.

        Array类型最小元素数

        :param min_items: The min_items of this AwParam.
        :type min_items: int
        """
        self._min_items = min_items

    @property
    def min_length(self):
        """Gets the min_length of this AwParam.

        String类型最小长度

        :return: The min_length of this AwParam.
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this AwParam.

        String类型最小长度

        :param min_length: The min_length of this AwParam.
        :type min_length: int
        """
        self._min_length = min_length

    @property
    def minimum(self):
        """Gets the minimum of this AwParam.

        :return: The minimum of this AwParam.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.Number`
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this AwParam.

        :param minimum: The minimum of this AwParam.
        :type minimum: :class:`huaweicloudsdkcloudtest.v1.Number`
        """
        self._minimum = minimum

    @property
    def mock(self):
        """Gets the mock of this AwParam.

        :return: The mock of this AwParam.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.MockInfo`
        """
        return self._mock

    @mock.setter
    def mock(self, mock):
        """Sets the mock of this AwParam.

        :param mock: The mock of this AwParam.
        :type mock: :class:`huaweicloudsdkcloudtest.v1.MockInfo`
        """
        self._mock = mock

    @property
    def name(self):
        """Gets the name of this AwParam.

        参数名

        :return: The name of this AwParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AwParam.

        参数名

        :param name: The name of this AwParam.
        :type name: str
        """
        self._name = name

    @property
    def object_value(self):
        """Gets the object_value of this AwParam.

        valueType为2时该值有效。valueType为3时，该值用来表示数组中单个结构体

        :return: The object_value of this AwParam.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        return self._object_value

    @object_value.setter
    def object_value(self, object_value):
        """Sets the object_value of this AwParam.

        valueType为2时该值有效。valueType为3时，该值用来表示数组中单个结构体

        :param object_value: The object_value of this AwParam.
        :type object_value: list[:class:`huaweicloudsdkcloudtest.v1.AwParam`]
        """
        self._object_value = object_value

    @property
    def object_value_list(self):
        """Gets the object_value_list of this AwParam.

        valueType为3时该值有效

        :return: The object_value_list of this AwParam.
        :rtype: list[list[AwParam]]
        """
        return self._object_value_list

    @object_value_list.setter
    def object_value_list(self, object_value_list):
        """Sets the object_value_list of this AwParam.

        valueType为3时该值有效

        :param object_value_list: The object_value_list of this AwParam.
        :type object_value_list: list[list[AwParam]]
        """
        self._object_value_list = object_value_list

    @property
    def pattern(self):
        """Gets the pattern of this AwParam.

        num和String有效

        :return: The pattern of this AwParam.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this AwParam.

        num和String有效

        :param pattern: The pattern of this AwParam.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def required(self):
        """Gets the required of this AwParam.

        是否必需参数

        :return: The required of this AwParam.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this AwParam.

        是否必需参数

        :param required: The required of this AwParam.
        :type required: bool
        """
        self._required = required

    @property
    def type(self):
        """Gets the type of this AwParam.

        参数类型

        :return: The type of this AwParam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AwParam.

        参数类型

        :param type: The type of this AwParam.
        :type type: str
        """
        self._type = type

    @property
    def validate_rule(self):
        """Gets the validate_rule of this AwParam.

        :return: The validate_rule of this AwParam.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ValidateRule`
        """
        return self._validate_rule

    @validate_rule.setter
    def validate_rule(self, validate_rule):
        """Sets the validate_rule of this AwParam.

        :param validate_rule: The validate_rule of this AwParam.
        :type validate_rule: :class:`huaweicloudsdkcloudtest.v1.ValidateRule`
        """
        self._validate_rule = validate_rule

    @property
    def value_type(self):
        """Gets the value_type of this AwParam.

        参数值类型 0-基本类型，type字段为String,Integer等基本类型 1-基本类型数组,type字段为List<String>,List<Integer>等基本类型List 2-结构体，type字段为除了基本类型以外的结构体 3-结构体数组，type字段为List<结构体> 5-前端枚举类型

        :return: The value_type of this AwParam.
        :rtype: int
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this AwParam.

        参数值类型 0-基本类型，type字段为String,Integer等基本类型 1-基本类型数组,type字段为List<String>,List<Integer>等基本类型List 2-结构体，type字段为除了基本类型以外的结构体 3-结构体数组，type字段为List<结构体> 5-前端枚举类型

        :param value_type: The value_type of this AwParam.
        :type value_type: int
        """
        self._value_type = value_type

    @property
    def x_choice_value(self):
        """Gets the x_choice_value of this AwParam.

        choice选择关系

        :return: The x_choice_value of this AwParam.
        :rtype: str
        """
        return self._x_choice_value

    @x_choice_value.setter
    def x_choice_value(self, x_choice_value):
        """Sets the x_choice_value of this AwParam.

        choice选择关系

        :param x_choice_value: The x_choice_value of this AwParam.
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
        if not isinstance(other, AwParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
