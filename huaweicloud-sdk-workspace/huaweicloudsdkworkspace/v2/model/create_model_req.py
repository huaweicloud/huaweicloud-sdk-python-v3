# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateModelReq:

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
        'input': 'list[str]',
        'provider_model_id': 'str',
        'description': 'str',
        'reasoning': 'bool',
        'cost': 'ModelCost',
        'context_window': 'int',
        'max_tokens': 'int',
        'compat': 'ModelCompat'
    }

    attribute_map = {
        'name': 'name',
        'input': 'input',
        'provider_model_id': 'provider_model_id',
        'description': 'description',
        'reasoning': 'reasoning',
        'cost': 'cost',
        'context_window': 'context_window',
        'max_tokens': 'max_tokens',
        'compat': 'compat'
    }

    def __init__(self, name=None, input=None, provider_model_id=None, description=None, reasoning=None, cost=None, context_window=None, max_tokens=None, compat=None):
        r"""CreateModelReq

        The model defined in huaweicloud sdk

        :param name: 模型名称。
        :type name: str
        :param input: 输入类型数组。
        :type input: list[str]
        :param provider_model_id: 供应商侧模型标识。
        :type provider_model_id: str
        :param description: 模型描述。
        :type description: str
        :param reasoning: 是否支持推理。
        :type reasoning: bool
        :param cost: 
        :type cost: :class:`huaweicloudsdkworkspace.v2.ModelCost`
        :param context_window: 最大上下文窗口。
        :type context_window: int
        :param max_tokens: 最大输出Token数。
        :type max_tokens: int
        :param compat: 
        :type compat: :class:`huaweicloudsdkworkspace.v2.ModelCompat`
        """
        
        

        self._name = None
        self._input = None
        self._provider_model_id = None
        self._description = None
        self._reasoning = None
        self._cost = None
        self._context_window = None
        self._max_tokens = None
        self._compat = None
        self.discriminator = None

        self.name = name
        if input is not None:
            self.input = input
        self.provider_model_id = provider_model_id
        if description is not None:
            self.description = description
        if reasoning is not None:
            self.reasoning = reasoning
        if cost is not None:
            self.cost = cost
        if context_window is not None:
            self.context_window = context_window
        if max_tokens is not None:
            self.max_tokens = max_tokens
        if compat is not None:
            self.compat = compat

    @property
    def name(self):
        r"""Gets the name of this CreateModelReq.

        模型名称。

        :return: The name of this CreateModelReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateModelReq.

        模型名称。

        :param name: The name of this CreateModelReq.
        :type name: str
        """
        self._name = name

    @property
    def input(self):
        r"""Gets the input of this CreateModelReq.

        输入类型数组。

        :return: The input of this CreateModelReq.
        :rtype: list[str]
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this CreateModelReq.

        输入类型数组。

        :param input: The input of this CreateModelReq.
        :type input: list[str]
        """
        self._input = input

    @property
    def provider_model_id(self):
        r"""Gets the provider_model_id of this CreateModelReq.

        供应商侧模型标识。

        :return: The provider_model_id of this CreateModelReq.
        :rtype: str
        """
        return self._provider_model_id

    @provider_model_id.setter
    def provider_model_id(self, provider_model_id):
        r"""Sets the provider_model_id of this CreateModelReq.

        供应商侧模型标识。

        :param provider_model_id: The provider_model_id of this CreateModelReq.
        :type provider_model_id: str
        """
        self._provider_model_id = provider_model_id

    @property
    def description(self):
        r"""Gets the description of this CreateModelReq.

        模型描述。

        :return: The description of this CreateModelReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateModelReq.

        模型描述。

        :param description: The description of this CreateModelReq.
        :type description: str
        """
        self._description = description

    @property
    def reasoning(self):
        r"""Gets the reasoning of this CreateModelReq.

        是否支持推理。

        :return: The reasoning of this CreateModelReq.
        :rtype: bool
        """
        return self._reasoning

    @reasoning.setter
    def reasoning(self, reasoning):
        r"""Sets the reasoning of this CreateModelReq.

        是否支持推理。

        :param reasoning: The reasoning of this CreateModelReq.
        :type reasoning: bool
        """
        self._reasoning = reasoning

    @property
    def cost(self):
        r"""Gets the cost of this CreateModelReq.

        :return: The cost of this CreateModelReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ModelCost`
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        r"""Sets the cost of this CreateModelReq.

        :param cost: The cost of this CreateModelReq.
        :type cost: :class:`huaweicloudsdkworkspace.v2.ModelCost`
        """
        self._cost = cost

    @property
    def context_window(self):
        r"""Gets the context_window of this CreateModelReq.

        最大上下文窗口。

        :return: The context_window of this CreateModelReq.
        :rtype: int
        """
        return self._context_window

    @context_window.setter
    def context_window(self, context_window):
        r"""Sets the context_window of this CreateModelReq.

        最大上下文窗口。

        :param context_window: The context_window of this CreateModelReq.
        :type context_window: int
        """
        self._context_window = context_window

    @property
    def max_tokens(self):
        r"""Gets the max_tokens of this CreateModelReq.

        最大输出Token数。

        :return: The max_tokens of this CreateModelReq.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        r"""Sets the max_tokens of this CreateModelReq.

        最大输出Token数。

        :param max_tokens: The max_tokens of this CreateModelReq.
        :type max_tokens: int
        """
        self._max_tokens = max_tokens

    @property
    def compat(self):
        r"""Gets the compat of this CreateModelReq.

        :return: The compat of this CreateModelReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ModelCompat`
        """
        return self._compat

    @compat.setter
    def compat(self, compat):
        r"""Sets the compat of this CreateModelReq.

        :param compat: The compat of this CreateModelReq.
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
        if not isinstance(other, CreateModelReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
