# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateModelReq:

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
        'input': 'list[str]',
        'context_window': 'int',
        'max_tokens': 'int',
        'reasoning': 'bool',
        'cost': 'ModelCost',
        'compat': 'ModelCompat'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'input': 'input',
        'context_window': 'context_window',
        'max_tokens': 'max_tokens',
        'reasoning': 'reasoning',
        'cost': 'cost',
        'compat': 'compat'
    }

    def __init__(self, name=None, description=None, input=None, context_window=None, max_tokens=None, reasoning=None, cost=None, compat=None):
        r"""UpdateModelReq

        The model defined in huaweicloud sdk

        :param name: 模型名称。
        :type name: str
        :param description: 模型描述。
        :type description: str
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
        """
        
        

        self._name = None
        self._description = None
        self._input = None
        self._context_window = None
        self._max_tokens = None
        self._reasoning = None
        self._cost = None
        self._compat = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
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

    @property
    def name(self):
        r"""Gets the name of this UpdateModelReq.

        模型名称。

        :return: The name of this UpdateModelReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateModelReq.

        模型名称。

        :param name: The name of this UpdateModelReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateModelReq.

        模型描述。

        :return: The description of this UpdateModelReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateModelReq.

        模型描述。

        :param description: The description of this UpdateModelReq.
        :type description: str
        """
        self._description = description

    @property
    def input(self):
        r"""Gets the input of this UpdateModelReq.

        输入类型数组。

        :return: The input of this UpdateModelReq.
        :rtype: list[str]
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this UpdateModelReq.

        输入类型数组。

        :param input: The input of this UpdateModelReq.
        :type input: list[str]
        """
        self._input = input

    @property
    def context_window(self):
        r"""Gets the context_window of this UpdateModelReq.

        最大上下文窗口。

        :return: The context_window of this UpdateModelReq.
        :rtype: int
        """
        return self._context_window

    @context_window.setter
    def context_window(self, context_window):
        r"""Sets the context_window of this UpdateModelReq.

        最大上下文窗口。

        :param context_window: The context_window of this UpdateModelReq.
        :type context_window: int
        """
        self._context_window = context_window

    @property
    def max_tokens(self):
        r"""Gets the max_tokens of this UpdateModelReq.

        最大输出Token数。

        :return: The max_tokens of this UpdateModelReq.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        r"""Sets the max_tokens of this UpdateModelReq.

        最大输出Token数。

        :param max_tokens: The max_tokens of this UpdateModelReq.
        :type max_tokens: int
        """
        self._max_tokens = max_tokens

    @property
    def reasoning(self):
        r"""Gets the reasoning of this UpdateModelReq.

        是否支持推理。

        :return: The reasoning of this UpdateModelReq.
        :rtype: bool
        """
        return self._reasoning

    @reasoning.setter
    def reasoning(self, reasoning):
        r"""Sets the reasoning of this UpdateModelReq.

        是否支持推理。

        :param reasoning: The reasoning of this UpdateModelReq.
        :type reasoning: bool
        """
        self._reasoning = reasoning

    @property
    def cost(self):
        r"""Gets the cost of this UpdateModelReq.

        :return: The cost of this UpdateModelReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ModelCost`
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        r"""Sets the cost of this UpdateModelReq.

        :param cost: The cost of this UpdateModelReq.
        :type cost: :class:`huaweicloudsdkworkspace.v2.ModelCost`
        """
        self._cost = cost

    @property
    def compat(self):
        r"""Gets the compat of this UpdateModelReq.

        :return: The compat of this UpdateModelReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ModelCompat`
        """
        return self._compat

    @compat.setter
    def compat(self, compat):
        r"""Sets the compat of this UpdateModelReq.

        :param compat: The compat of this UpdateModelReq.
        :type compat: :class:`huaweicloudsdkworkspace.v2.ModelCompat`
        """
        self._compat = compat

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
        if not isinstance(other, UpdateModelReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
