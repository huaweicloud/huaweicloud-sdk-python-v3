# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowModelResponse(SdkResponse):

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
        'update_time': 'str',
        'groups': 'list[AttachModelGroupInfo]'
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
        'update_time': 'update_time',
        'groups': 'groups'
    }

    def __init__(self, id=None, name=None, input=None, context_window=None, max_tokens=None, reasoning=None, cost=None, compat=None, is_builtin=None, provider_model_id=None, provider_id=None, provider_name=None, description=None, priority=None, create_time=None, update_time=None, groups=None):
        r"""ShowModelResponse

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
        :param groups: 关联为默认模型的模型分组
        :type groups: list[:class:`huaweicloudsdkworkspace.v2.AttachModelGroupInfo`]
        """
        
        super().__init__()

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
        self._groups = None
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
        if groups is not None:
            self.groups = groups

    @property
    def id(self):
        r"""Gets the id of this ShowModelResponse.

        模型id。

        :return: The id of this ShowModelResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowModelResponse.

        模型id。

        :param id: The id of this ShowModelResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowModelResponse.

        模型名称。

        :return: The name of this ShowModelResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowModelResponse.

        模型名称。

        :param name: The name of this ShowModelResponse.
        :type name: str
        """
        self._name = name

    @property
    def input(self):
        r"""Gets the input of this ShowModelResponse.

        输入类型数组。

        :return: The input of this ShowModelResponse.
        :rtype: list[str]
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this ShowModelResponse.

        输入类型数组。

        :param input: The input of this ShowModelResponse.
        :type input: list[str]
        """
        self._input = input

    @property
    def context_window(self):
        r"""Gets the context_window of this ShowModelResponse.

        最大上下文窗口。

        :return: The context_window of this ShowModelResponse.
        :rtype: int
        """
        return self._context_window

    @context_window.setter
    def context_window(self, context_window):
        r"""Sets the context_window of this ShowModelResponse.

        最大上下文窗口。

        :param context_window: The context_window of this ShowModelResponse.
        :type context_window: int
        """
        self._context_window = context_window

    @property
    def max_tokens(self):
        r"""Gets the max_tokens of this ShowModelResponse.

        最大输出Token数。

        :return: The max_tokens of this ShowModelResponse.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        r"""Sets the max_tokens of this ShowModelResponse.

        最大输出Token数。

        :param max_tokens: The max_tokens of this ShowModelResponse.
        :type max_tokens: int
        """
        self._max_tokens = max_tokens

    @property
    def reasoning(self):
        r"""Gets the reasoning of this ShowModelResponse.

        是否支持推理。

        :return: The reasoning of this ShowModelResponse.
        :rtype: bool
        """
        return self._reasoning

    @reasoning.setter
    def reasoning(self, reasoning):
        r"""Sets the reasoning of this ShowModelResponse.

        是否支持推理。

        :param reasoning: The reasoning of this ShowModelResponse.
        :type reasoning: bool
        """
        self._reasoning = reasoning

    @property
    def cost(self):
        r"""Gets the cost of this ShowModelResponse.

        :return: The cost of this ShowModelResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ModelCost`
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        r"""Sets the cost of this ShowModelResponse.

        :param cost: The cost of this ShowModelResponse.
        :type cost: :class:`huaweicloudsdkworkspace.v2.ModelCost`
        """
        self._cost = cost

    @property
    def compat(self):
        r"""Gets the compat of this ShowModelResponse.

        :return: The compat of this ShowModelResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ModelCompat`
        """
        return self._compat

    @compat.setter
    def compat(self, compat):
        r"""Sets the compat of this ShowModelResponse.

        :param compat: The compat of this ShowModelResponse.
        :type compat: :class:`huaweicloudsdkworkspace.v2.ModelCompat`
        """
        self._compat = compat

    @property
    def is_builtin(self):
        r"""Gets the is_builtin of this ShowModelResponse.

        是否内置模型。

        :return: The is_builtin of this ShowModelResponse.
        :rtype: bool
        """
        return self._is_builtin

    @is_builtin.setter
    def is_builtin(self, is_builtin):
        r"""Sets the is_builtin of this ShowModelResponse.

        是否内置模型。

        :param is_builtin: The is_builtin of this ShowModelResponse.
        :type is_builtin: bool
        """
        self._is_builtin = is_builtin

    @property
    def provider_model_id(self):
        r"""Gets the provider_model_id of this ShowModelResponse.

        供应商侧模型标识。

        :return: The provider_model_id of this ShowModelResponse.
        :rtype: str
        """
        return self._provider_model_id

    @provider_model_id.setter
    def provider_model_id(self, provider_model_id):
        r"""Sets the provider_model_id of this ShowModelResponse.

        供应商侧模型标识。

        :param provider_model_id: The provider_model_id of this ShowModelResponse.
        :type provider_model_id: str
        """
        self._provider_model_id = provider_model_id

    @property
    def provider_id(self):
        r"""Gets the provider_id of this ShowModelResponse.

        供应商id。

        :return: The provider_id of this ShowModelResponse.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this ShowModelResponse.

        供应商id。

        :param provider_id: The provider_id of this ShowModelResponse.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def provider_name(self):
        r"""Gets the provider_name of this ShowModelResponse.

        供应商名称。

        :return: The provider_name of this ShowModelResponse.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        r"""Sets the provider_name of this ShowModelResponse.

        供应商名称。

        :param provider_name: The provider_name of this ShowModelResponse.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def description(self):
        r"""Gets the description of this ShowModelResponse.

        模型描述。

        :return: The description of this ShowModelResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowModelResponse.

        模型描述。

        :param description: The description of this ShowModelResponse.
        :type description: str
        """
        self._description = description

    @property
    def priority(self):
        r"""Gets the priority of this ShowModelResponse.

        组内排序优先级。

        :return: The priority of this ShowModelResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ShowModelResponse.

        组内排序优先级。

        :param priority: The priority of this ShowModelResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowModelResponse.

        创建时间。

        :return: The create_time of this ShowModelResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowModelResponse.

        创建时间。

        :param create_time: The create_time of this ShowModelResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowModelResponse.

        更新时间。

        :return: The update_time of this ShowModelResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowModelResponse.

        更新时间。

        :param update_time: The update_time of this ShowModelResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def groups(self):
        r"""Gets the groups of this ShowModelResponse.

        关联为默认模型的模型分组

        :return: The groups of this ShowModelResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachModelGroupInfo`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this ShowModelResponse.

        关联为默认模型的模型分组

        :param groups: The groups of this ShowModelResponse.
        :type groups: list[:class:`huaweicloudsdkworkspace.v2.AttachModelGroupInfo`]
        """
        self._groups = groups

    def to_dict(self):
        import warnings
        warnings.warn("ShowModelResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowModelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
