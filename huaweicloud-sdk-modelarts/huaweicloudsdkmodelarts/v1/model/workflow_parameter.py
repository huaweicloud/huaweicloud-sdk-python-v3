# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowParameter:

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
        'description': 'str',
        'example': 'object',
        'delay': 'bool',
        'default': 'object',
        'value': 'object',
        'enum': 'list[object]',
        'used_steps': 'list[str]',
        'format': 'str',
        'constraint': 'dict(str, object)'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'example': 'example',
        'delay': 'delay',
        'default': 'default',
        'value': 'value',
        'enum': 'enum',
        'used_steps': 'used_steps',
        'format': 'format',
        'constraint': 'constraint'
    }

    def __init__(self, name=None, type=None, description=None, example=None, delay=None, default=None, value=None, enum=None, used_steps=None, format=None, constraint=None):
        r"""WorkflowParameter

        The model defined in huaweicloud sdk

        :param name: Workflow工作流配置参数的名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。
        :type name: str
        :param type: 参数的类型，枚举值如下: - str：字符串 - int：整型 - bool：布尔类型 - float：浮点型
        :type type: str
        :param description: Workflow工作流配置参数的描述。
        :type description: str
        :param example: Workflow工作流配置参数的样例。
        :type example: object
        :param delay: 是否为延迟输入的参数，默认为否。
        :type delay: bool
        :param default: 配置参数的默认值。
        :type default: object
        :param value: 参数值。
        :type value: object
        :param enum: Workflow工作流配置参数的枚举项。
        :type enum: list[object]
        :param used_steps: 使用这个参数的工作流节点。
        :type used_steps: list[str]
        :param format: 数据格式。
        :type format: str
        :param constraint: 限制条件。
        :type constraint: dict(str, object)
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._example = None
        self._delay = None
        self._default = None
        self._value = None
        self._enum = None
        self._used_steps = None
        self._format = None
        self._constraint = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if example is not None:
            self.example = example
        if delay is not None:
            self.delay = delay
        if default is not None:
            self.default = default
        if value is not None:
            self.value = value
        if enum is not None:
            self.enum = enum
        if used_steps is not None:
            self.used_steps = used_steps
        if format is not None:
            self.format = format
        if constraint is not None:
            self.constraint = constraint

    @property
    def name(self):
        r"""Gets the name of this WorkflowParameter.

        Workflow工作流配置参数的名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :return: The name of this WorkflowParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkflowParameter.

        Workflow工作流配置参数的名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :param name: The name of this WorkflowParameter.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this WorkflowParameter.

        参数的类型，枚举值如下: - str：字符串 - int：整型 - bool：布尔类型 - float：浮点型

        :return: The type of this WorkflowParameter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this WorkflowParameter.

        参数的类型，枚举值如下: - str：字符串 - int：整型 - bool：布尔类型 - float：浮点型

        :param type: The type of this WorkflowParameter.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this WorkflowParameter.

        Workflow工作流配置参数的描述。

        :return: The description of this WorkflowParameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WorkflowParameter.

        Workflow工作流配置参数的描述。

        :param description: The description of this WorkflowParameter.
        :type description: str
        """
        self._description = description

    @property
    def example(self):
        r"""Gets the example of this WorkflowParameter.

        Workflow工作流配置参数的样例。

        :return: The example of this WorkflowParameter.
        :rtype: object
        """
        return self._example

    @example.setter
    def example(self, example):
        r"""Sets the example of this WorkflowParameter.

        Workflow工作流配置参数的样例。

        :param example: The example of this WorkflowParameter.
        :type example: object
        """
        self._example = example

    @property
    def delay(self):
        r"""Gets the delay of this WorkflowParameter.

        是否为延迟输入的参数，默认为否。

        :return: The delay of this WorkflowParameter.
        :rtype: bool
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this WorkflowParameter.

        是否为延迟输入的参数，默认为否。

        :param delay: The delay of this WorkflowParameter.
        :type delay: bool
        """
        self._delay = delay

    @property
    def default(self):
        r"""Gets the default of this WorkflowParameter.

        配置参数的默认值。

        :return: The default of this WorkflowParameter.
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this WorkflowParameter.

        配置参数的默认值。

        :param default: The default of this WorkflowParameter.
        :type default: object
        """
        self._default = default

    @property
    def value(self):
        r"""Gets the value of this WorkflowParameter.

        参数值。

        :return: The value of this WorkflowParameter.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this WorkflowParameter.

        参数值。

        :param value: The value of this WorkflowParameter.
        :type value: object
        """
        self._value = value

    @property
    def enum(self):
        r"""Gets the enum of this WorkflowParameter.

        Workflow工作流配置参数的枚举项。

        :return: The enum of this WorkflowParameter.
        :rtype: list[object]
        """
        return self._enum

    @enum.setter
    def enum(self, enum):
        r"""Sets the enum of this WorkflowParameter.

        Workflow工作流配置参数的枚举项。

        :param enum: The enum of this WorkflowParameter.
        :type enum: list[object]
        """
        self._enum = enum

    @property
    def used_steps(self):
        r"""Gets the used_steps of this WorkflowParameter.

        使用这个参数的工作流节点。

        :return: The used_steps of this WorkflowParameter.
        :rtype: list[str]
        """
        return self._used_steps

    @used_steps.setter
    def used_steps(self, used_steps):
        r"""Sets the used_steps of this WorkflowParameter.

        使用这个参数的工作流节点。

        :param used_steps: The used_steps of this WorkflowParameter.
        :type used_steps: list[str]
        """
        self._used_steps = used_steps

    @property
    def format(self):
        r"""Gets the format of this WorkflowParameter.

        数据格式。

        :return: The format of this WorkflowParameter.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this WorkflowParameter.

        数据格式。

        :param format: The format of this WorkflowParameter.
        :type format: str
        """
        self._format = format

    @property
    def constraint(self):
        r"""Gets the constraint of this WorkflowParameter.

        限制条件。

        :return: The constraint of this WorkflowParameter.
        :rtype: dict(str, object)
        """
        return self._constraint

    @constraint.setter
    def constraint(self, constraint):
        r"""Sets the constraint of this WorkflowParameter.

        限制条件。

        :param constraint: The constraint of this WorkflowParameter.
        :type constraint: dict(str, object)
        """
        self._constraint = constraint

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkflowParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
