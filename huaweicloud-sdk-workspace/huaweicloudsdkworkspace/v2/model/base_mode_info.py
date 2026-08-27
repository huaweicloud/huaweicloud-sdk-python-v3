# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseModeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'input': 'list[str]',
        'context_window': 'int',
        'max_tokens': 'int',
        'reasoning': 'bool',
        'cost': 'ModelCost',
        'compat': 'ModelCompat',
        'is_builtin': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'input': 'input',
        'context_window': 'context_window',
        'max_tokens': 'max_tokens',
        'reasoning': 'reasoning',
        'cost': 'cost',
        'compat': 'compat',
        'is_builtin': 'is_builtin'
    }

    def __init__(self, id=None, name=None, input=None, context_window=None, max_tokens=None, reasoning=None, cost=None, compat=None, is_builtin=None):
        r"""BaseModeInfo

        The model defined in huaweicloud sdk

        :param id: 模型id。
        :type id: str
        :param name: 模型名称。
        :type name: str
        :param input: 输入类型数组。
        :type input: list[str]
        :param context_window: 最大上下文窗口。
        :type context_window: int
        :param max_tokens: 最大输出Token数。
        :type max_tokens: int
        :param reasoning: 是否支持推理。
        :type reasoning: bool
        :param cost: 
        :type cost: :class:`huaweicloudsdkworkspace.v2.ModelCost`
        :param compat: 
        :type compat: :class:`huaweicloudsdkworkspace.v2.ModelCompat`
        :param is_builtin: 是否内置模型。
        :type is_builtin: bool
        """
        
        

        self._id = None
        self._name = None
        self._input = None
        self._context_window = None
        self._max_tokens = None
        self._reasoning = None
        self._cost = None
        self._compat = None
        self._is_builtin = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if input is not None:
            self.input = input
        if context_window is not None:
            self.context_window = context_window
        if max_tokens is not None:
            self.max_tokens = max_tokens
        if reasoning is not None:
            self.reasoning = reasoning
        if cost is not None:
            self.cost = cost
        if compat is not None:
            self.compat = compat
        if is_builtin is not None:
            self.is_builtin = is_builtin

    @property
    def id(self):
        r"""Gets the id of this BaseModeInfo.

        模型id。

        :return: The id of this BaseModeInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BaseModeInfo.

        模型id。

        :param id: The id of this BaseModeInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BaseModeInfo.

        模型名称。

        :return: The name of this BaseModeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BaseModeInfo.

        模型名称。

        :param name: The name of this BaseModeInfo.
        :type name: str
        """
        self._name = name

    @property
    def input(self):
        r"""Gets the input of this BaseModeInfo.

        输入类型数组。

        :return: The input of this BaseModeInfo.
        :rtype: list[str]
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this BaseModeInfo.

        输入类型数组。

        :param input: The input of this BaseModeInfo.
        :type input: list[str]
        """
        self._input = input

    @property
    def context_window(self):
        r"""Gets the context_window of this BaseModeInfo.

        最大上下文窗口。

        :return: The context_window of this BaseModeInfo.
        :rtype: int
        """
        return self._context_window

    @context_window.setter
    def context_window(self, context_window):
        r"""Sets the context_window of this BaseModeInfo.

        最大上下文窗口。

        :param context_window: The context_window of this BaseModeInfo.
        :type context_window: int
        """
        self._context_window = context_window

    @property
    def max_tokens(self):
        r"""Gets the max_tokens of this BaseModeInfo.

        最大输出Token数。

        :return: The max_tokens of this BaseModeInfo.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        r"""Sets the max_tokens of this BaseModeInfo.

        最大输出Token数。

        :param max_tokens: The max_tokens of this BaseModeInfo.
        :type max_tokens: int
        """
        self._max_tokens = max_tokens

    @property
    def reasoning(self):
        r"""Gets the reasoning of this BaseModeInfo.

        是否支持推理。

        :return: The reasoning of this BaseModeInfo.
        :rtype: bool
        """
        return self._reasoning

    @reasoning.setter
    def reasoning(self, reasoning):
        r"""Sets the reasoning of this BaseModeInfo.

        是否支持推理。

        :param reasoning: The reasoning of this BaseModeInfo.
        :type reasoning: bool
        """
        self._reasoning = reasoning

    @property
    def cost(self):
        r"""Gets the cost of this BaseModeInfo.

        :return: The cost of this BaseModeInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ModelCost`
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        r"""Sets the cost of this BaseModeInfo.

        :param cost: The cost of this BaseModeInfo.
        :type cost: :class:`huaweicloudsdkworkspace.v2.ModelCost`
        """
        self._cost = cost

    @property
    def compat(self):
        r"""Gets the compat of this BaseModeInfo.

        :return: The compat of this BaseModeInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ModelCompat`
        """
        return self._compat

    @compat.setter
    def compat(self, compat):
        r"""Sets the compat of this BaseModeInfo.

        :param compat: The compat of this BaseModeInfo.
        :type compat: :class:`huaweicloudsdkworkspace.v2.ModelCompat`
        """
        self._compat = compat

    @property
    def is_builtin(self):
        r"""Gets the is_builtin of this BaseModeInfo.

        是否内置模型。

        :return: The is_builtin of this BaseModeInfo.
        :rtype: bool
        """
        return self._is_builtin

    @is_builtin.setter
    def is_builtin(self, is_builtin):
        r"""Sets the is_builtin of this BaseModeInfo.

        是否内置模型。

        :param is_builtin: The is_builtin of this BaseModeInfo.
        :type is_builtin: bool
        """
        self._is_builtin = is_builtin

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
        if not isinstance(other, BaseModeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
