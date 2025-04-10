# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AwVariable:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'by_order': 'int',
        'current_permission': 'str',
        'description': 'str',
        'dynamic_param': 'str',
        'dynamic_param_flag': 'bool',
        'function_params': 'str',
        'function_arg': 'str',
        'function_type': 'str',
        'is_sensitive_info': 'bool',
        'is_sensitive_modified': 'bool',
        'is_out_put': 'bool',
        'name': 'str',
        'node_id': 'str',
        'node_type': 'int',
        'old_name': 'str',
        'parent_node_id': 'str',
        '_property': 'str',
        'regex': 'str',
        'sensitive_info_setter_time': 'str',
        'sensitive_info_setter_user': 'str',
        'type': 'str',
        'variable_type': 'int'
    }

    attribute_map = {
        'by_order': 'by_order',
        'current_permission': 'currentPermission',
        'description': 'description',
        'dynamic_param': 'dynamicParam',
        'dynamic_param_flag': 'dynamicParamFlag',
        'function_params': 'functionParams',
        'function_arg': 'function_arg',
        'function_type': 'function_type',
        'is_sensitive_info': 'isSensitiveInfo',
        'is_sensitive_modified': 'isSensitiveModified',
        'is_out_put': 'is_out_put',
        'name': 'name',
        'node_id': 'node_id',
        'node_type': 'node_type',
        'old_name': 'oldName',
        'parent_node_id': 'parent_node_id',
        '_property': 'property',
        'regex': 'regex',
        'sensitive_info_setter_time': 'sensitiveInfoSetterTime',
        'sensitive_info_setter_user': 'sensitiveInfoSetterUser',
        'type': 'type',
        'variable_type': 'variableType'
    }

    def __init__(self, by_order=None, current_permission=None, description=None, dynamic_param=None, dynamic_param_flag=None, function_params=None, function_arg=None, function_type=None, is_sensitive_info=None, is_sensitive_modified=None, is_out_put=None, name=None, node_id=None, node_type=None, old_name=None, parent_node_id=None, _property=None, regex=None, sensitive_info_setter_time=None, sensitive_info_setter_user=None, type=None, variable_type=None):
        r"""AwVariable

        The model defined in huaweicloud sdk

        :param by_order: 节点顺序
        :type by_order: int
        :param current_permission: 当前人员权限
        :type current_permission: str
        :param description: 参数描述
        :type description: str
        :param dynamic_param: 动态参数名称
        :type dynamic_param: str
        :param dynamic_param_flag: 动态参数标志,默认为false:true代表动态参数；false代表非动态参数
        :type dynamic_param_flag: bool
        :param function_params: 变量参数（[]:空参、[a]:一参，[a,b]:两参）
        :type function_params: str
        :param function_arg: 响应提取时要使用什么方法处理参数
        :type function_arg: str
        :param function_type: 响应提取时要使用什么方法处理参数
        :type function_type: str
        :param is_sensitive_info: 是否是敏感字段
        :type is_sensitive_info: bool
        :param is_sensitive_modified: 敏感字段是否被修改，不敏感字段不关注此值
        :type is_sensitive_modified: bool
        :param is_out_put: 是否是组合aw的输出参数，只有组合aw下awInstance的aw变量有该字段
        :type is_out_put: bool
        :param name: 参数名称
        :type name: str
        :param node_id: 节点id
        :type node_id: str
        :param node_type: 0/null-变量节点;1-目录节点
        :type node_type: int
        :param old_name: 旧名称
        :type old_name: str
        :param parent_node_id: 父节点id
        :type parent_node_id: str
        :param _property: 属性
        :type _property: str
        :param regex: 内置函数枚举
        :type regex: str
        :param sensitive_info_setter_time: 敏感参数设置时间
        :type sensitive_info_setter_time: str
        :param sensitive_info_setter_user: 敏感参数设置者名称
        :type sensitive_info_setter_user: str
        :param type: 类型
        :type type: str
        :param variable_type: 变量类型（0：text，10-16：7个内置函数）
        :type variable_type: int
        """
        
        

        self._by_order = None
        self._current_permission = None
        self._description = None
        self._dynamic_param = None
        self._dynamic_param_flag = None
        self._function_params = None
        self._function_arg = None
        self._function_type = None
        self._is_sensitive_info = None
        self._is_sensitive_modified = None
        self._is_out_put = None
        self._name = None
        self._node_id = None
        self._node_type = None
        self._old_name = None
        self._parent_node_id = None
        self.__property = None
        self._regex = None
        self._sensitive_info_setter_time = None
        self._sensitive_info_setter_user = None
        self._type = None
        self._variable_type = None
        self.discriminator = None

        if by_order is not None:
            self.by_order = by_order
        if current_permission is not None:
            self.current_permission = current_permission
        if description is not None:
            self.description = description
        if dynamic_param is not None:
            self.dynamic_param = dynamic_param
        if dynamic_param_flag is not None:
            self.dynamic_param_flag = dynamic_param_flag
        if function_params is not None:
            self.function_params = function_params
        if function_arg is not None:
            self.function_arg = function_arg
        if function_type is not None:
            self.function_type = function_type
        if is_sensitive_info is not None:
            self.is_sensitive_info = is_sensitive_info
        if is_sensitive_modified is not None:
            self.is_sensitive_modified = is_sensitive_modified
        if is_out_put is not None:
            self.is_out_put = is_out_put
        if name is not None:
            self.name = name
        if node_id is not None:
            self.node_id = node_id
        if node_type is not None:
            self.node_type = node_type
        if old_name is not None:
            self.old_name = old_name
        if parent_node_id is not None:
            self.parent_node_id = parent_node_id
        if _property is not None:
            self._property = _property
        if regex is not None:
            self.regex = regex
        if sensitive_info_setter_time is not None:
            self.sensitive_info_setter_time = sensitive_info_setter_time
        if sensitive_info_setter_user is not None:
            self.sensitive_info_setter_user = sensitive_info_setter_user
        if type is not None:
            self.type = type
        if variable_type is not None:
            self.variable_type = variable_type

    @property
    def by_order(self):
        r"""Gets the by_order of this AwVariable.

        节点顺序

        :return: The by_order of this AwVariable.
        :rtype: int
        """
        return self._by_order

    @by_order.setter
    def by_order(self, by_order):
        r"""Sets the by_order of this AwVariable.

        节点顺序

        :param by_order: The by_order of this AwVariable.
        :type by_order: int
        """
        self._by_order = by_order

    @property
    def current_permission(self):
        r"""Gets the current_permission of this AwVariable.

        当前人员权限

        :return: The current_permission of this AwVariable.
        :rtype: str
        """
        return self._current_permission

    @current_permission.setter
    def current_permission(self, current_permission):
        r"""Sets the current_permission of this AwVariable.

        当前人员权限

        :param current_permission: The current_permission of this AwVariable.
        :type current_permission: str
        """
        self._current_permission = current_permission

    @property
    def description(self):
        r"""Gets the description of this AwVariable.

        参数描述

        :return: The description of this AwVariable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AwVariable.

        参数描述

        :param description: The description of this AwVariable.
        :type description: str
        """
        self._description = description

    @property
    def dynamic_param(self):
        r"""Gets the dynamic_param of this AwVariable.

        动态参数名称

        :return: The dynamic_param of this AwVariable.
        :rtype: str
        """
        return self._dynamic_param

    @dynamic_param.setter
    def dynamic_param(self, dynamic_param):
        r"""Sets the dynamic_param of this AwVariable.

        动态参数名称

        :param dynamic_param: The dynamic_param of this AwVariable.
        :type dynamic_param: str
        """
        self._dynamic_param = dynamic_param

    @property
    def dynamic_param_flag(self):
        r"""Gets the dynamic_param_flag of this AwVariable.

        动态参数标志,默认为false:true代表动态参数；false代表非动态参数

        :return: The dynamic_param_flag of this AwVariable.
        :rtype: bool
        """
        return self._dynamic_param_flag

    @dynamic_param_flag.setter
    def dynamic_param_flag(self, dynamic_param_flag):
        r"""Sets the dynamic_param_flag of this AwVariable.

        动态参数标志,默认为false:true代表动态参数；false代表非动态参数

        :param dynamic_param_flag: The dynamic_param_flag of this AwVariable.
        :type dynamic_param_flag: bool
        """
        self._dynamic_param_flag = dynamic_param_flag

    @property
    def function_params(self):
        r"""Gets the function_params of this AwVariable.

        变量参数（[]:空参、[a]:一参，[a,b]:两参）

        :return: The function_params of this AwVariable.
        :rtype: str
        """
        return self._function_params

    @function_params.setter
    def function_params(self, function_params):
        r"""Sets the function_params of this AwVariable.

        变量参数（[]:空参、[a]:一参，[a,b]:两参）

        :param function_params: The function_params of this AwVariable.
        :type function_params: str
        """
        self._function_params = function_params

    @property
    def function_arg(self):
        r"""Gets the function_arg of this AwVariable.

        响应提取时要使用什么方法处理参数

        :return: The function_arg of this AwVariable.
        :rtype: str
        """
        return self._function_arg

    @function_arg.setter
    def function_arg(self, function_arg):
        r"""Sets the function_arg of this AwVariable.

        响应提取时要使用什么方法处理参数

        :param function_arg: The function_arg of this AwVariable.
        :type function_arg: str
        """
        self._function_arg = function_arg

    @property
    def function_type(self):
        r"""Gets the function_type of this AwVariable.

        响应提取时要使用什么方法处理参数

        :return: The function_type of this AwVariable.
        :rtype: str
        """
        return self._function_type

    @function_type.setter
    def function_type(self, function_type):
        r"""Sets the function_type of this AwVariable.

        响应提取时要使用什么方法处理参数

        :param function_type: The function_type of this AwVariable.
        :type function_type: str
        """
        self._function_type = function_type

    @property
    def is_sensitive_info(self):
        r"""Gets the is_sensitive_info of this AwVariable.

        是否是敏感字段

        :return: The is_sensitive_info of this AwVariable.
        :rtype: bool
        """
        return self._is_sensitive_info

    @is_sensitive_info.setter
    def is_sensitive_info(self, is_sensitive_info):
        r"""Sets the is_sensitive_info of this AwVariable.

        是否是敏感字段

        :param is_sensitive_info: The is_sensitive_info of this AwVariable.
        :type is_sensitive_info: bool
        """
        self._is_sensitive_info = is_sensitive_info

    @property
    def is_sensitive_modified(self):
        r"""Gets the is_sensitive_modified of this AwVariable.

        敏感字段是否被修改，不敏感字段不关注此值

        :return: The is_sensitive_modified of this AwVariable.
        :rtype: bool
        """
        return self._is_sensitive_modified

    @is_sensitive_modified.setter
    def is_sensitive_modified(self, is_sensitive_modified):
        r"""Sets the is_sensitive_modified of this AwVariable.

        敏感字段是否被修改，不敏感字段不关注此值

        :param is_sensitive_modified: The is_sensitive_modified of this AwVariable.
        :type is_sensitive_modified: bool
        """
        self._is_sensitive_modified = is_sensitive_modified

    @property
    def is_out_put(self):
        r"""Gets the is_out_put of this AwVariable.

        是否是组合aw的输出参数，只有组合aw下awInstance的aw变量有该字段

        :return: The is_out_put of this AwVariable.
        :rtype: bool
        """
        return self._is_out_put

    @is_out_put.setter
    def is_out_put(self, is_out_put):
        r"""Sets the is_out_put of this AwVariable.

        是否是组合aw的输出参数，只有组合aw下awInstance的aw变量有该字段

        :param is_out_put: The is_out_put of this AwVariable.
        :type is_out_put: bool
        """
        self._is_out_put = is_out_put

    @property
    def name(self):
        r"""Gets the name of this AwVariable.

        参数名称

        :return: The name of this AwVariable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AwVariable.

        参数名称

        :param name: The name of this AwVariable.
        :type name: str
        """
        self._name = name

    @property
    def node_id(self):
        r"""Gets the node_id of this AwVariable.

        节点id

        :return: The node_id of this AwVariable.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this AwVariable.

        节点id

        :param node_id: The node_id of this AwVariable.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_type(self):
        r"""Gets the node_type of this AwVariable.

        0/null-变量节点;1-目录节点

        :return: The node_type of this AwVariable.
        :rtype: int
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this AwVariable.

        0/null-变量节点;1-目录节点

        :param node_type: The node_type of this AwVariable.
        :type node_type: int
        """
        self._node_type = node_type

    @property
    def old_name(self):
        r"""Gets the old_name of this AwVariable.

        旧名称

        :return: The old_name of this AwVariable.
        :rtype: str
        """
        return self._old_name

    @old_name.setter
    def old_name(self, old_name):
        r"""Sets the old_name of this AwVariable.

        旧名称

        :param old_name: The old_name of this AwVariable.
        :type old_name: str
        """
        self._old_name = old_name

    @property
    def parent_node_id(self):
        r"""Gets the parent_node_id of this AwVariable.

        父节点id

        :return: The parent_node_id of this AwVariable.
        :rtype: str
        """
        return self._parent_node_id

    @parent_node_id.setter
    def parent_node_id(self, parent_node_id):
        r"""Sets the parent_node_id of this AwVariable.

        父节点id

        :param parent_node_id: The parent_node_id of this AwVariable.
        :type parent_node_id: str
        """
        self._parent_node_id = parent_node_id

    @property
    def _property(self):
        r"""Gets the _property of this AwVariable.

        属性

        :return: The _property of this AwVariable.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        r"""Sets the _property of this AwVariable.

        属性

        :param _property: The _property of this AwVariable.
        :type _property: str
        """
        self.__property = _property

    @property
    def regex(self):
        r"""Gets the regex of this AwVariable.

        内置函数枚举

        :return: The regex of this AwVariable.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        r"""Sets the regex of this AwVariable.

        内置函数枚举

        :param regex: The regex of this AwVariable.
        :type regex: str
        """
        self._regex = regex

    @property
    def sensitive_info_setter_time(self):
        r"""Gets the sensitive_info_setter_time of this AwVariable.

        敏感参数设置时间

        :return: The sensitive_info_setter_time of this AwVariable.
        :rtype: str
        """
        return self._sensitive_info_setter_time

    @sensitive_info_setter_time.setter
    def sensitive_info_setter_time(self, sensitive_info_setter_time):
        r"""Sets the sensitive_info_setter_time of this AwVariable.

        敏感参数设置时间

        :param sensitive_info_setter_time: The sensitive_info_setter_time of this AwVariable.
        :type sensitive_info_setter_time: str
        """
        self._sensitive_info_setter_time = sensitive_info_setter_time

    @property
    def sensitive_info_setter_user(self):
        r"""Gets the sensitive_info_setter_user of this AwVariable.

        敏感参数设置者名称

        :return: The sensitive_info_setter_user of this AwVariable.
        :rtype: str
        """
        return self._sensitive_info_setter_user

    @sensitive_info_setter_user.setter
    def sensitive_info_setter_user(self, sensitive_info_setter_user):
        r"""Sets the sensitive_info_setter_user of this AwVariable.

        敏感参数设置者名称

        :param sensitive_info_setter_user: The sensitive_info_setter_user of this AwVariable.
        :type sensitive_info_setter_user: str
        """
        self._sensitive_info_setter_user = sensitive_info_setter_user

    @property
    def type(self):
        r"""Gets the type of this AwVariable.

        类型

        :return: The type of this AwVariable.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AwVariable.

        类型

        :param type: The type of this AwVariable.
        :type type: str
        """
        self._type = type

    @property
    def variable_type(self):
        r"""Gets the variable_type of this AwVariable.

        变量类型（0：text，10-16：7个内置函数）

        :return: The variable_type of this AwVariable.
        :rtype: int
        """
        return self._variable_type

    @variable_type.setter
    def variable_type(self, variable_type):
        r"""Sets the variable_type of this AwVariable.

        变量类型（0：text，10-16：7个内置函数）

        :param variable_type: The variable_type of this AwVariable.
        :type variable_type: int
        """
        self._variable_type = variable_type

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
        if not isinstance(other, AwVariable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
