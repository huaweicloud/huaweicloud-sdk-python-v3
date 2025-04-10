# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Input:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parameter_name': 'str',
        'type': 'str',
        'value_type': 'InputParaValueType',
        'template_parameter_name': 'str',
        'parameter_value': 'str',
        'description': 'str',
        'default': 'str',
        'label': 'str',
        'constraints': 'object',
        'invisible': 'bool'
    }

    attribute_map = {
        'parameter_name': 'parameter_name',
        'type': 'type',
        'value_type': 'value_type',
        'template_parameter_name': 'template_parameter_name',
        'parameter_value': 'parameter_value',
        'description': 'description',
        'default': 'default',
        'label': 'label',
        'constraints': 'constraints',
        'invisible': 'invisible'
    }

    def __init__(self, parameter_name=None, type=None, value_type=None, template_parameter_name=None, parameter_value=None, description=None, default=None, label=None, constraints=None, invisible=None):
        r"""Input

        The model defined in huaweicloud sdk

        :param parameter_name: 输入参数名称，由小写字母、数字和中划线“-”组成
        :type parameter_name: str
        :param type: 参数类型。可为string，integer，float，boolean，list，map。type为list类型时，value_type必填
        :type type: str
        :param value_type: 
        :type value_type: :class:`huaweicloudsdkdwr.v3.InputParaValueType`
        :param template_parameter_name: 当多个相同action template在一个工作流时，增加字段做国际化。 由小写字母、数字和中划线“-”组成
        :type template_parameter_name: str
        :param parameter_value: Input结构体参数类型。支持string,integer,float,boolean,list,map
        :type parameter_value: str
        :param description: 参数项描述信息。
        :type description: str
        :param default: 默认值信息可在创建工作流实例时由外部输入替换；若未填写默认值，外部输入将必须填写这个参数的值。 注：默认值的类型和定义的参数类型必须统一。如果出现不一致，解析器可能会进行自动转换而导致出现与预期不符合的情况。
        :type default: str
        :param label: 参数的标签，此处定义的标签可在创建堆栈时进行分类展示。
        :type label: str
        :param constraints: 约束条件有以下几种，一个输入参数对每一种条件都只能定义一个规则。约束的多个条件中只要有一条不满足，即将认定参数非法。 equal：约定参数的value值必须等于特定值。 valid_values：参数的有效值，定义一个数组。 regex：参数需要满足某个正则条件，必须是字符串类型才可以进行匹配。 invalid_values：参数的无效值范围，如果参数值定义在其中，将会认为无效而报错。
        :type constraints: object
        :param invisible: 输入参数的invisible设置为true时，返回值为******。
        :type invisible: bool
        """
        
        

        self._parameter_name = None
        self._type = None
        self._value_type = None
        self._template_parameter_name = None
        self._parameter_value = None
        self._description = None
        self._default = None
        self._label = None
        self._constraints = None
        self._invisible = None
        self.discriminator = None

        self.parameter_name = parameter_name
        self.type = type
        if value_type is not None:
            self.value_type = value_type
        if template_parameter_name is not None:
            self.template_parameter_name = template_parameter_name
        if parameter_value is not None:
            self.parameter_value = parameter_value
        if description is not None:
            self.description = description
        if default is not None:
            self.default = default
        if label is not None:
            self.label = label
        if constraints is not None:
            self.constraints = constraints
        if invisible is not None:
            self.invisible = invisible

    @property
    def parameter_name(self):
        r"""Gets the parameter_name of this Input.

        输入参数名称，由小写字母、数字和中划线“-”组成

        :return: The parameter_name of this Input.
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        r"""Sets the parameter_name of this Input.

        输入参数名称，由小写字母、数字和中划线“-”组成

        :param parameter_name: The parameter_name of this Input.
        :type parameter_name: str
        """
        self._parameter_name = parameter_name

    @property
    def type(self):
        r"""Gets the type of this Input.

        参数类型。可为string，integer，float，boolean，list，map。type为list类型时，value_type必填

        :return: The type of this Input.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Input.

        参数类型。可为string，integer，float，boolean，list，map。type为list类型时，value_type必填

        :param type: The type of this Input.
        :type type: str
        """
        self._type = type

    @property
    def value_type(self):
        r"""Gets the value_type of this Input.

        :return: The value_type of this Input.
        :rtype: :class:`huaweicloudsdkdwr.v3.InputParaValueType`
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        r"""Sets the value_type of this Input.

        :param value_type: The value_type of this Input.
        :type value_type: :class:`huaweicloudsdkdwr.v3.InputParaValueType`
        """
        self._value_type = value_type

    @property
    def template_parameter_name(self):
        r"""Gets the template_parameter_name of this Input.

        当多个相同action template在一个工作流时，增加字段做国际化。 由小写字母、数字和中划线“-”组成

        :return: The template_parameter_name of this Input.
        :rtype: str
        """
        return self._template_parameter_name

    @template_parameter_name.setter
    def template_parameter_name(self, template_parameter_name):
        r"""Sets the template_parameter_name of this Input.

        当多个相同action template在一个工作流时，增加字段做国际化。 由小写字母、数字和中划线“-”组成

        :param template_parameter_name: The template_parameter_name of this Input.
        :type template_parameter_name: str
        """
        self._template_parameter_name = template_parameter_name

    @property
    def parameter_value(self):
        r"""Gets the parameter_value of this Input.

        Input结构体参数类型。支持string,integer,float,boolean,list,map

        :return: The parameter_value of this Input.
        :rtype: str
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(self, parameter_value):
        r"""Sets the parameter_value of this Input.

        Input结构体参数类型。支持string,integer,float,boolean,list,map

        :param parameter_value: The parameter_value of this Input.
        :type parameter_value: str
        """
        self._parameter_value = parameter_value

    @property
    def description(self):
        r"""Gets the description of this Input.

        参数项描述信息。

        :return: The description of this Input.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Input.

        参数项描述信息。

        :param description: The description of this Input.
        :type description: str
        """
        self._description = description

    @property
    def default(self):
        r"""Gets the default of this Input.

        默认值信息可在创建工作流实例时由外部输入替换；若未填写默认值，外部输入将必须填写这个参数的值。 注：默认值的类型和定义的参数类型必须统一。如果出现不一致，解析器可能会进行自动转换而导致出现与预期不符合的情况。

        :return: The default of this Input.
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this Input.

        默认值信息可在创建工作流实例时由外部输入替换；若未填写默认值，外部输入将必须填写这个参数的值。 注：默认值的类型和定义的参数类型必须统一。如果出现不一致，解析器可能会进行自动转换而导致出现与预期不符合的情况。

        :param default: The default of this Input.
        :type default: str
        """
        self._default = default

    @property
    def label(self):
        r"""Gets the label of this Input.

        参数的标签，此处定义的标签可在创建堆栈时进行分类展示。

        :return: The label of this Input.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this Input.

        参数的标签，此处定义的标签可在创建堆栈时进行分类展示。

        :param label: The label of this Input.
        :type label: str
        """
        self._label = label

    @property
    def constraints(self):
        r"""Gets the constraints of this Input.

        约束条件有以下几种，一个输入参数对每一种条件都只能定义一个规则。约束的多个条件中只要有一条不满足，即将认定参数非法。 equal：约定参数的value值必须等于特定值。 valid_values：参数的有效值，定义一个数组。 regex：参数需要满足某个正则条件，必须是字符串类型才可以进行匹配。 invalid_values：参数的无效值范围，如果参数值定义在其中，将会认为无效而报错。

        :return: The constraints of this Input.
        :rtype: object
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        r"""Sets the constraints of this Input.

        约束条件有以下几种，一个输入参数对每一种条件都只能定义一个规则。约束的多个条件中只要有一条不满足，即将认定参数非法。 equal：约定参数的value值必须等于特定值。 valid_values：参数的有效值，定义一个数组。 regex：参数需要满足某个正则条件，必须是字符串类型才可以进行匹配。 invalid_values：参数的无效值范围，如果参数值定义在其中，将会认为无效而报错。

        :param constraints: The constraints of this Input.
        :type constraints: object
        """
        self._constraints = constraints

    @property
    def invisible(self):
        r"""Gets the invisible of this Input.

        输入参数的invisible设置为true时，返回值为******。

        :return: The invisible of this Input.
        :rtype: bool
        """
        return self._invisible

    @invisible.setter
    def invisible(self, invisible):
        r"""Sets the invisible of this Input.

        输入参数的invisible设置为true时，返回值为******。

        :param invisible: The invisible of this Input.
        :type invisible: bool
        """
        self._invisible = invisible

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
        if not isinstance(other, Input):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
