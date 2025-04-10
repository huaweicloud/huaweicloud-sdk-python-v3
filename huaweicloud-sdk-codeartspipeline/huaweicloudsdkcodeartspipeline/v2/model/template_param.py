# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'required': 'str',
        'visible': 'str',
        'name': 'str',
        'value': 'str',
        'description': 'str',
        'paramtype': 'str',
        'display_type': 'str',
        'display_name': 'str',
        'is_static': 'bool',
        'is_default': 'bool',
        'limits': 'list[ParamTypeLimits]',
        'constraints': 'list[Constraint]'
    }

    attribute_map = {
        'required': 'required',
        'visible': 'visible',
        'name': 'name',
        'value': 'value',
        'description': 'description',
        'paramtype': 'paramtype',
        'display_type': 'display_type',
        'display_name': 'display_name',
        'is_static': 'is_static',
        'is_default': 'is_default',
        'limits': 'limits',
        'constraints': 'constraints'
    }

    def __init__(self, required=None, visible=None, name=None, value=None, description=None, paramtype=None, display_type=None, display_name=None, is_static=None, is_default=None, limits=None, constraints=None):
        r"""TemplateParam

        The model defined in huaweicloud sdk

        :param required: 是否必须
        :type required: str
        :param visible: 是否可见
        :type visible: str
        :param name: 流水线参数名字
        :type name: str
        :param value: 流水线参数值
        :type value: str
        :param description: 流水线参数描述
        :type description: str
        :param paramtype: 流水线参数类型
        :type paramtype: str
        :param display_type: 流水线参数展示类型
        :type display_type: str
        :param display_name: 流水线参数展示名字
        :type display_name: str
        :param is_static: 是否静态参数
        :type is_static: bool
        :param is_default: 是否默认参数
        :type is_default: bool
        :param limits: array类型数据
        :type limits: list[:class:`huaweicloudsdkcodeartspipeline.v2.ParamTypeLimits`]
        :param constraints: array类型数据
        :type constraints: list[:class:`huaweicloudsdkcodeartspipeline.v2.Constraint`]
        """
        
        

        self._required = None
        self._visible = None
        self._name = None
        self._value = None
        self._description = None
        self._paramtype = None
        self._display_type = None
        self._display_name = None
        self._is_static = None
        self._is_default = None
        self._limits = None
        self._constraints = None
        self.discriminator = None

        self.required = required
        self.visible = visible
        self.name = name
        self.value = value
        self.description = description
        self.paramtype = paramtype
        self.display_type = display_type
        self.display_name = display_name
        self.is_static = is_static
        self.is_default = is_default
        self.limits = limits
        self.constraints = constraints

    @property
    def required(self):
        r"""Gets the required of this TemplateParam.

        是否必须

        :return: The required of this TemplateParam.
        :rtype: str
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this TemplateParam.

        是否必须

        :param required: The required of this TemplateParam.
        :type required: str
        """
        self._required = required

    @property
    def visible(self):
        r"""Gets the visible of this TemplateParam.

        是否可见

        :return: The visible of this TemplateParam.
        :rtype: str
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this TemplateParam.

        是否可见

        :param visible: The visible of this TemplateParam.
        :type visible: str
        """
        self._visible = visible

    @property
    def name(self):
        r"""Gets the name of this TemplateParam.

        流水线参数名字

        :return: The name of this TemplateParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TemplateParam.

        流水线参数名字

        :param name: The name of this TemplateParam.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this TemplateParam.

        流水线参数值

        :return: The value of this TemplateParam.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this TemplateParam.

        流水线参数值

        :param value: The value of this TemplateParam.
        :type value: str
        """
        self._value = value

    @property
    def description(self):
        r"""Gets the description of this TemplateParam.

        流水线参数描述

        :return: The description of this TemplateParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TemplateParam.

        流水线参数描述

        :param description: The description of this TemplateParam.
        :type description: str
        """
        self._description = description

    @property
    def paramtype(self):
        r"""Gets the paramtype of this TemplateParam.

        流水线参数类型

        :return: The paramtype of this TemplateParam.
        :rtype: str
        """
        return self._paramtype

    @paramtype.setter
    def paramtype(self, paramtype):
        r"""Sets the paramtype of this TemplateParam.

        流水线参数类型

        :param paramtype: The paramtype of this TemplateParam.
        :type paramtype: str
        """
        self._paramtype = paramtype

    @property
    def display_type(self):
        r"""Gets the display_type of this TemplateParam.

        流水线参数展示类型

        :return: The display_type of this TemplateParam.
        :rtype: str
        """
        return self._display_type

    @display_type.setter
    def display_type(self, display_type):
        r"""Sets the display_type of this TemplateParam.

        流水线参数展示类型

        :param display_type: The display_type of this TemplateParam.
        :type display_type: str
        """
        self._display_type = display_type

    @property
    def display_name(self):
        r"""Gets the display_name of this TemplateParam.

        流水线参数展示名字

        :return: The display_name of this TemplateParam.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this TemplateParam.

        流水线参数展示名字

        :param display_name: The display_name of this TemplateParam.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def is_static(self):
        r"""Gets the is_static of this TemplateParam.

        是否静态参数

        :return: The is_static of this TemplateParam.
        :rtype: bool
        """
        return self._is_static

    @is_static.setter
    def is_static(self, is_static):
        r"""Sets the is_static of this TemplateParam.

        是否静态参数

        :param is_static: The is_static of this TemplateParam.
        :type is_static: bool
        """
        self._is_static = is_static

    @property
    def is_default(self):
        r"""Gets the is_default of this TemplateParam.

        是否默认参数

        :return: The is_default of this TemplateParam.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this TemplateParam.

        是否默认参数

        :param is_default: The is_default of this TemplateParam.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def limits(self):
        r"""Gets the limits of this TemplateParam.

        array类型数据

        :return: The limits of this TemplateParam.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.ParamTypeLimits`]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        r"""Sets the limits of this TemplateParam.

        array类型数据

        :param limits: The limits of this TemplateParam.
        :type limits: list[:class:`huaweicloudsdkcodeartspipeline.v2.ParamTypeLimits`]
        """
        self._limits = limits

    @property
    def constraints(self):
        r"""Gets the constraints of this TemplateParam.

        array类型数据

        :return: The constraints of this TemplateParam.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.Constraint`]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        r"""Sets the constraints of this TemplateParam.

        array类型数据

        :param constraints: The constraints of this TemplateParam.
        :type constraints: list[:class:`huaweicloudsdkcodeartspipeline.v2.Constraint`]
        """
        self._constraints = constraints

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
        if not isinstance(other, TemplateParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
