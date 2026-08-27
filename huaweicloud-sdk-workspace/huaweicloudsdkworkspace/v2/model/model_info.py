# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelInfo:

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
        'provider_model_id': 'str',
        'input': 'list[str]',
        'reasoning': 'bool',
        'update_time': 'str',
        'context_window': 'int',
        'max_tokens': 'int',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'provider_model_id': 'provider_model_id',
        'input': 'input',
        'reasoning': 'reasoning',
        'update_time': 'update_time',
        'context_window': 'context_window',
        'max_tokens': 'max_tokens',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, provider_model_id=None, input=None, reasoning=None, update_time=None, context_window=None, max_tokens=None, type=None):
        r"""ModelInfo

        The model defined in huaweicloud sdk

        :param id: 模型 ID（业务主键）。
        :type id: str
        :param name: 模型名称。
        :type name: str
        :param provider_model_id: 供应商侧模型 ID。
        :type provider_model_id: str
        :param input: 输入类型数组。
        :type input: list[str]
        :param reasoning: 是否支持推理。
        :type reasoning: bool
        :param update_time: 模型更新时间。
        :type update_time: str
        :param context_window: 上下文窗口。
        :type context_window: int
        :param max_tokens: 最大输出 token 数。
        :type max_tokens: int
        :param type: 纳管类型（BACKEND_MANAGE后台管理/CUSTOM自定义）,业务下发的都是BACKEND_MANAGE。
        :type type: str
        """
        
        

        self._id = None
        self._name = None
        self._provider_model_id = None
        self._input = None
        self._reasoning = None
        self._update_time = None
        self._context_window = None
        self._max_tokens = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if provider_model_id is not None:
            self.provider_model_id = provider_model_id
        if input is not None:
            self.input = input
        if reasoning is not None:
            self.reasoning = reasoning
        if update_time is not None:
            self.update_time = update_time
        if context_window is not None:
            self.context_window = context_window
        if max_tokens is not None:
            self.max_tokens = max_tokens
        if type is not None:
            self.type = type

    @property
    def id(self):
        r"""Gets the id of this ModelInfo.

        模型 ID（业务主键）。

        :return: The id of this ModelInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModelInfo.

        模型 ID（业务主键）。

        :param id: The id of this ModelInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ModelInfo.

        模型名称。

        :return: The name of this ModelInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModelInfo.

        模型名称。

        :param name: The name of this ModelInfo.
        :type name: str
        """
        self._name = name

    @property
    def provider_model_id(self):
        r"""Gets the provider_model_id of this ModelInfo.

        供应商侧模型 ID。

        :return: The provider_model_id of this ModelInfo.
        :rtype: str
        """
        return self._provider_model_id

    @provider_model_id.setter
    def provider_model_id(self, provider_model_id):
        r"""Sets the provider_model_id of this ModelInfo.

        供应商侧模型 ID。

        :param provider_model_id: The provider_model_id of this ModelInfo.
        :type provider_model_id: str
        """
        self._provider_model_id = provider_model_id

    @property
    def input(self):
        r"""Gets the input of this ModelInfo.

        输入类型数组。

        :return: The input of this ModelInfo.
        :rtype: list[str]
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this ModelInfo.

        输入类型数组。

        :param input: The input of this ModelInfo.
        :type input: list[str]
        """
        self._input = input

    @property
    def reasoning(self):
        r"""Gets the reasoning of this ModelInfo.

        是否支持推理。

        :return: The reasoning of this ModelInfo.
        :rtype: bool
        """
        return self._reasoning

    @reasoning.setter
    def reasoning(self, reasoning):
        r"""Sets the reasoning of this ModelInfo.

        是否支持推理。

        :param reasoning: The reasoning of this ModelInfo.
        :type reasoning: bool
        """
        self._reasoning = reasoning

    @property
    def update_time(self):
        r"""Gets the update_time of this ModelInfo.

        模型更新时间。

        :return: The update_time of this ModelInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ModelInfo.

        模型更新时间。

        :param update_time: The update_time of this ModelInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def context_window(self):
        r"""Gets the context_window of this ModelInfo.

        上下文窗口。

        :return: The context_window of this ModelInfo.
        :rtype: int
        """
        return self._context_window

    @context_window.setter
    def context_window(self, context_window):
        r"""Sets the context_window of this ModelInfo.

        上下文窗口。

        :param context_window: The context_window of this ModelInfo.
        :type context_window: int
        """
        self._context_window = context_window

    @property
    def max_tokens(self):
        r"""Gets the max_tokens of this ModelInfo.

        最大输出 token 数。

        :return: The max_tokens of this ModelInfo.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        r"""Sets the max_tokens of this ModelInfo.

        最大输出 token 数。

        :param max_tokens: The max_tokens of this ModelInfo.
        :type max_tokens: int
        """
        self._max_tokens = max_tokens

    @property
    def type(self):
        r"""Gets the type of this ModelInfo.

        纳管类型（BACKEND_MANAGE后台管理/CUSTOM自定义）,业务下发的都是BACKEND_MANAGE。

        :return: The type of this ModelInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ModelInfo.

        纳管类型（BACKEND_MANAGE后台管理/CUSTOM自定义）,业务下发的都是BACKEND_MANAGE。

        :param type: The type of this ModelInfo.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ModelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
