# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelInfoForResp:

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
        'is_builtin': 'bool',
        'provider_model_id': 'str',
        'provider_id': 'str',
        'provider_name': 'str',
        'description': 'str',
        'priority': 'int',
        'create_time': 'str',
        'update_time': 'str'
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
        'is_builtin': 'is_builtin',
        'provider_model_id': 'provider_model_id',
        'provider_id': 'provider_id',
        'provider_name': 'provider_name',
        'description': 'description',
        'priority': 'priority',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, input=None, context_window=None, max_tokens=None, reasoning=None, cost=None, compat=None, is_builtin=None, provider_model_id=None, provider_id=None, provider_name=None, description=None, priority=None, create_time=None, update_time=None):
        r"""ModelInfoForResp

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
        :param provider_model_id: 供应商侧模型标识。
        :type provider_model_id: str
        :param provider_id: 供应商id。
        :type provider_id: str
        :param provider_name: 供应商名称。
        :type provider_name: str
        :param description: 模型描述。
        :type description: str
        :param priority: 组内排序优先级。
        :type priority: int
        :param create_time: 创建时间。
        :type create_time: str
        :param update_time: 更新时间。
        :type update_time: str
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
        self._provider_model_id = None
        self._provider_id = None
        self._provider_name = None
        self._description = None
        self._priority = None
        self._create_time = None
        self._update_time = None
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
        if provider_model_id is not None:
            self.provider_model_id = provider_model_id
        if provider_id is not None:
            self.provider_id = provider_id
        if provider_name is not None:
            self.provider_name = provider_name
        if description is not None:
            self.description = description
        if priority is not None:
            self.priority = priority
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ModelInfoForResp.

        模型id。

        :return: The id of this ModelInfoForResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModelInfoForResp.

        模型id。

        :param id: The id of this ModelInfoForResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ModelInfoForResp.

        模型名称。

        :return: The name of this ModelInfoForResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModelInfoForResp.

        模型名称。

        :param name: The name of this ModelInfoForResp.
        :type name: str
        """
        self._name = name

    @property
    def input(self):
        r"""Gets the input of this ModelInfoForResp.

        输入类型数组。

        :return: The input of this ModelInfoForResp.
        :rtype: list[str]
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this ModelInfoForResp.

        输入类型数组。

        :param input: The input of this ModelInfoForResp.
        :type input: list[str]
        """
        self._input = input

    @property
    def context_window(self):
        r"""Gets the context_window of this ModelInfoForResp.

        最大上下文窗口。

        :return: The context_window of this ModelInfoForResp.
        :rtype: int
        """
        return self._context_window

    @context_window.setter
    def context_window(self, context_window):
        r"""Sets the context_window of this ModelInfoForResp.

        最大上下文窗口。

        :param context_window: The context_window of this ModelInfoForResp.
        :type context_window: int
        """
        self._context_window = context_window

    @property
    def max_tokens(self):
        r"""Gets the max_tokens of this ModelInfoForResp.

        最大输出Token数。

        :return: The max_tokens of this ModelInfoForResp.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        r"""Sets the max_tokens of this ModelInfoForResp.

        最大输出Token数。

        :param max_tokens: The max_tokens of this ModelInfoForResp.
        :type max_tokens: int
        """
        self._max_tokens = max_tokens

    @property
    def reasoning(self):
        r"""Gets the reasoning of this ModelInfoForResp.

        是否支持推理。

        :return: The reasoning of this ModelInfoForResp.
        :rtype: bool
        """
        return self._reasoning

    @reasoning.setter
    def reasoning(self, reasoning):
        r"""Sets the reasoning of this ModelInfoForResp.

        是否支持推理。

        :param reasoning: The reasoning of this ModelInfoForResp.
        :type reasoning: bool
        """
        self._reasoning = reasoning

    @property
    def cost(self):
        r"""Gets the cost of this ModelInfoForResp.

        :return: The cost of this ModelInfoForResp.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ModelCost`
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        r"""Sets the cost of this ModelInfoForResp.

        :param cost: The cost of this ModelInfoForResp.
        :type cost: :class:`huaweicloudsdkworkspace.v2.ModelCost`
        """
        self._cost = cost

    @property
    def compat(self):
        r"""Gets the compat of this ModelInfoForResp.

        :return: The compat of this ModelInfoForResp.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ModelCompat`
        """
        return self._compat

    @compat.setter
    def compat(self, compat):
        r"""Sets the compat of this ModelInfoForResp.

        :param compat: The compat of this ModelInfoForResp.
        :type compat: :class:`huaweicloudsdkworkspace.v2.ModelCompat`
        """
        self._compat = compat

    @property
    def is_builtin(self):
        r"""Gets the is_builtin of this ModelInfoForResp.

        是否内置模型。

        :return: The is_builtin of this ModelInfoForResp.
        :rtype: bool
        """
        return self._is_builtin

    @is_builtin.setter
    def is_builtin(self, is_builtin):
        r"""Sets the is_builtin of this ModelInfoForResp.

        是否内置模型。

        :param is_builtin: The is_builtin of this ModelInfoForResp.
        :type is_builtin: bool
        """
        self._is_builtin = is_builtin

    @property
    def provider_model_id(self):
        r"""Gets the provider_model_id of this ModelInfoForResp.

        供应商侧模型标识。

        :return: The provider_model_id of this ModelInfoForResp.
        :rtype: str
        """
        return self._provider_model_id

    @provider_model_id.setter
    def provider_model_id(self, provider_model_id):
        r"""Sets the provider_model_id of this ModelInfoForResp.

        供应商侧模型标识。

        :param provider_model_id: The provider_model_id of this ModelInfoForResp.
        :type provider_model_id: str
        """
        self._provider_model_id = provider_model_id

    @property
    def provider_id(self):
        r"""Gets the provider_id of this ModelInfoForResp.

        供应商id。

        :return: The provider_id of this ModelInfoForResp.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this ModelInfoForResp.

        供应商id。

        :param provider_id: The provider_id of this ModelInfoForResp.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def provider_name(self):
        r"""Gets the provider_name of this ModelInfoForResp.

        供应商名称。

        :return: The provider_name of this ModelInfoForResp.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        r"""Sets the provider_name of this ModelInfoForResp.

        供应商名称。

        :param provider_name: The provider_name of this ModelInfoForResp.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def description(self):
        r"""Gets the description of this ModelInfoForResp.

        模型描述。

        :return: The description of this ModelInfoForResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModelInfoForResp.

        模型描述。

        :param description: The description of this ModelInfoForResp.
        :type description: str
        """
        self._description = description

    @property
    def priority(self):
        r"""Gets the priority of this ModelInfoForResp.

        组内排序优先级。

        :return: The priority of this ModelInfoForResp.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ModelInfoForResp.

        组内排序优先级。

        :param priority: The priority of this ModelInfoForResp.
        :type priority: int
        """
        self._priority = priority

    @property
    def create_time(self):
        r"""Gets the create_time of this ModelInfoForResp.

        创建时间。

        :return: The create_time of this ModelInfoForResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ModelInfoForResp.

        创建时间。

        :param create_time: The create_time of this ModelInfoForResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ModelInfoForResp.

        更新时间。

        :return: The update_time of this ModelInfoForResp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ModelInfoForResp.

        更新时间。

        :param update_time: The update_time of this ModelInfoForResp.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, ModelInfoForResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
