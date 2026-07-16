# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCoreSpaceRequestBody:

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
        'api_key_id': 'str',
        'message_ttl_hours': 'int',
        'memory_extract_idle_seconds': 'int',
        'memory_extract_max_tokens': 'int',
        'memory_extract_max_messages': 'int',
        'tags': 'list[CoreSpaceTag]',
        'memory_strategies_builtin': 'list[str]',
        'memory_strategies_customized': 'list[CreateCoreSpaceMemoryStrategyRequestBody]',
        'network_access': 'CreateCoreSpaceNetworkRequestBody',
        'encryption_config': 'EncryptionConfig'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'api_key_id': 'api_key_id',
        'message_ttl_hours': 'message_ttl_hours',
        'memory_extract_idle_seconds': 'memory_extract_idle_seconds',
        'memory_extract_max_tokens': 'memory_extract_max_tokens',
        'memory_extract_max_messages': 'memory_extract_max_messages',
        'tags': 'tags',
        'memory_strategies_builtin': 'memory_strategies_builtin',
        'memory_strategies_customized': 'memory_strategies_customized',
        'network_access': 'network_access',
        'encryption_config': 'encryption_config'
    }

    def __init__(self, name=None, description=None, api_key_id=None, message_ttl_hours=None, memory_extract_idle_seconds=None, memory_extract_max_tokens=None, memory_extract_max_messages=None, tags=None, memory_strategies_builtin=None, memory_strategies_customized=None, network_access=None, encryption_config=None):
        r"""CreateCoreSpaceRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 空间名称。 **约束限制：** 仅支持字母、数字和中划线。 **取值范围：** 长度1-48字符。 **默认取值：** 不涉及。 
        :type name: str
        :param description: **参数解释：**  空间描述。 **约束限制：**  不涉及。 **取值范围：**  不超过1000个字符。 **默认取值：** 不涉及。 
        :type description: str
        :param api_key_id: **参数解释：**  空间访问Key。 **约束限制：**  不涉及。 **取值范围：**  由英文字母、数字、\&quot;-\&quot;组成的字符串。 **默认取值：** 不涉及。 
        :type api_key_id: str
        :param message_ttl_hours: **参数解释：** 过期时间（小时）。 **约束限制：** 不涉及。 **取值范围：** 1-8760 h。 **默认取值：** 168。 
        :type message_ttl_hours: int
        :param memory_extract_idle_seconds: **参数解释：** 触发记忆抽取的空闲时间（秒)。 **约束限制：** 不涉及。 **取值范围：** 10-86400 s。 **默认取值：** 不涉及。 
        :type memory_extract_idle_seconds: int
        :param memory_extract_max_tokens: **参数解释：** 触发记忆抽取最大累计token数。 **约束限制：** 不涉及。 **取值范围：** 1000-1073741824 tokens。 **默认取值：** 不涉及。 
        :type memory_extract_max_tokens: int
        :param memory_extract_max_messages: **参数解释：** 触发记忆抽取最大累计message数。 **约束限制：** 不涉及。 **取值范围：** 3-10000 条。 **默认取值：** 不涉及。 
        :type memory_extract_max_messages: int
        :param tags: **参数解释：** 库标签列表。 **约束限制：** 数组长度0-20个；键最大长度36字符，不允许为空；值最大长度43字符，可以为空。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceTag`]
        :param memory_strategies_builtin: **参数解释：** 内置策略类型列表，与memory_strategies_customized至少选填一项。 **约束限制：** 数组长度0-10个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type memory_strategies_builtin: list[str]
        :param memory_strategies_customized: **参数解释：** 长期记忆自定义策略。 **约束限制：** 与memory_strategies_builtin至少选填一项；单个记忆库最多配置10个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type memory_strategies_customized: list[:class:`huaweicloudsdkagentarts.v1.CreateCoreSpaceMemoryStrategyRequestBody`]
        :param network_access: 
        :type network_access: :class:`huaweicloudsdkagentarts.v1.CreateCoreSpaceNetworkRequestBody`
        :param encryption_config: 
        :type encryption_config: :class:`huaweicloudsdkagentarts.v1.EncryptionConfig`
        """
        
        

        self._name = None
        self._description = None
        self._api_key_id = None
        self._message_ttl_hours = None
        self._memory_extract_idle_seconds = None
        self._memory_extract_max_tokens = None
        self._memory_extract_max_messages = None
        self._tags = None
        self._memory_strategies_builtin = None
        self._memory_strategies_customized = None
        self._network_access = None
        self._encryption_config = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.api_key_id = api_key_id
        self.message_ttl_hours = message_ttl_hours
        if memory_extract_idle_seconds is not None:
            self.memory_extract_idle_seconds = memory_extract_idle_seconds
        if memory_extract_max_tokens is not None:
            self.memory_extract_max_tokens = memory_extract_max_tokens
        if memory_extract_max_messages is not None:
            self.memory_extract_max_messages = memory_extract_max_messages
        if tags is not None:
            self.tags = tags
        if memory_strategies_builtin is not None:
            self.memory_strategies_builtin = memory_strategies_builtin
        if memory_strategies_customized is not None:
            self.memory_strategies_customized = memory_strategies_customized
        if network_access is not None:
            self.network_access = network_access
        if encryption_config is not None:
            self.encryption_config = encryption_config

    @property
    def name(self):
        r"""Gets the name of this CreateCoreSpaceRequestBody.

        **参数解释：** 空间名称。 **约束限制：** 仅支持字母、数字和中划线。 **取值范围：** 长度1-48字符。 **默认取值：** 不涉及。 

        :return: The name of this CreateCoreSpaceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCoreSpaceRequestBody.

        **参数解释：** 空间名称。 **约束限制：** 仅支持字母、数字和中划线。 **取值范围：** 长度1-48字符。 **默认取值：** 不涉及。 

        :param name: The name of this CreateCoreSpaceRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateCoreSpaceRequestBody.

        **参数解释：**  空间描述。 **约束限制：**  不涉及。 **取值范围：**  不超过1000个字符。 **默认取值：** 不涉及。 

        :return: The description of this CreateCoreSpaceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCoreSpaceRequestBody.

        **参数解释：**  空间描述。 **约束限制：**  不涉及。 **取值范围：**  不超过1000个字符。 **默认取值：** 不涉及。 

        :param description: The description of this CreateCoreSpaceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def api_key_id(self):
        r"""Gets the api_key_id of this CreateCoreSpaceRequestBody.

        **参数解释：**  空间访问Key。 **约束限制：**  不涉及。 **取值范围：**  由英文字母、数字、\"-\"组成的字符串。 **默认取值：** 不涉及。 

        :return: The api_key_id of this CreateCoreSpaceRequestBody.
        :rtype: str
        """
        return self._api_key_id

    @api_key_id.setter
    def api_key_id(self, api_key_id):
        r"""Sets the api_key_id of this CreateCoreSpaceRequestBody.

        **参数解释：**  空间访问Key。 **约束限制：**  不涉及。 **取值范围：**  由英文字母、数字、\"-\"组成的字符串。 **默认取值：** 不涉及。 

        :param api_key_id: The api_key_id of this CreateCoreSpaceRequestBody.
        :type api_key_id: str
        """
        self._api_key_id = api_key_id

    @property
    def message_ttl_hours(self):
        r"""Gets the message_ttl_hours of this CreateCoreSpaceRequestBody.

        **参数解释：** 过期时间（小时）。 **约束限制：** 不涉及。 **取值范围：** 1-8760 h。 **默认取值：** 168。 

        :return: The message_ttl_hours of this CreateCoreSpaceRequestBody.
        :rtype: int
        """
        return self._message_ttl_hours

    @message_ttl_hours.setter
    def message_ttl_hours(self, message_ttl_hours):
        r"""Sets the message_ttl_hours of this CreateCoreSpaceRequestBody.

        **参数解释：** 过期时间（小时）。 **约束限制：** 不涉及。 **取值范围：** 1-8760 h。 **默认取值：** 168。 

        :param message_ttl_hours: The message_ttl_hours of this CreateCoreSpaceRequestBody.
        :type message_ttl_hours: int
        """
        self._message_ttl_hours = message_ttl_hours

    @property
    def memory_extract_idle_seconds(self):
        r"""Gets the memory_extract_idle_seconds of this CreateCoreSpaceRequestBody.

        **参数解释：** 触发记忆抽取的空闲时间（秒)。 **约束限制：** 不涉及。 **取值范围：** 10-86400 s。 **默认取值：** 不涉及。 

        :return: The memory_extract_idle_seconds of this CreateCoreSpaceRequestBody.
        :rtype: int
        """
        return self._memory_extract_idle_seconds

    @memory_extract_idle_seconds.setter
    def memory_extract_idle_seconds(self, memory_extract_idle_seconds):
        r"""Sets the memory_extract_idle_seconds of this CreateCoreSpaceRequestBody.

        **参数解释：** 触发记忆抽取的空闲时间（秒)。 **约束限制：** 不涉及。 **取值范围：** 10-86400 s。 **默认取值：** 不涉及。 

        :param memory_extract_idle_seconds: The memory_extract_idle_seconds of this CreateCoreSpaceRequestBody.
        :type memory_extract_idle_seconds: int
        """
        self._memory_extract_idle_seconds = memory_extract_idle_seconds

    @property
    def memory_extract_max_tokens(self):
        r"""Gets the memory_extract_max_tokens of this CreateCoreSpaceRequestBody.

        **参数解释：** 触发记忆抽取最大累计token数。 **约束限制：** 不涉及。 **取值范围：** 1000-1073741824 tokens。 **默认取值：** 不涉及。 

        :return: The memory_extract_max_tokens of this CreateCoreSpaceRequestBody.
        :rtype: int
        """
        return self._memory_extract_max_tokens

    @memory_extract_max_tokens.setter
    def memory_extract_max_tokens(self, memory_extract_max_tokens):
        r"""Sets the memory_extract_max_tokens of this CreateCoreSpaceRequestBody.

        **参数解释：** 触发记忆抽取最大累计token数。 **约束限制：** 不涉及。 **取值范围：** 1000-1073741824 tokens。 **默认取值：** 不涉及。 

        :param memory_extract_max_tokens: The memory_extract_max_tokens of this CreateCoreSpaceRequestBody.
        :type memory_extract_max_tokens: int
        """
        self._memory_extract_max_tokens = memory_extract_max_tokens

    @property
    def memory_extract_max_messages(self):
        r"""Gets the memory_extract_max_messages of this CreateCoreSpaceRequestBody.

        **参数解释：** 触发记忆抽取最大累计message数。 **约束限制：** 不涉及。 **取值范围：** 3-10000 条。 **默认取值：** 不涉及。 

        :return: The memory_extract_max_messages of this CreateCoreSpaceRequestBody.
        :rtype: int
        """
        return self._memory_extract_max_messages

    @memory_extract_max_messages.setter
    def memory_extract_max_messages(self, memory_extract_max_messages):
        r"""Sets the memory_extract_max_messages of this CreateCoreSpaceRequestBody.

        **参数解释：** 触发记忆抽取最大累计message数。 **约束限制：** 不涉及。 **取值范围：** 3-10000 条。 **默认取值：** 不涉及。 

        :param memory_extract_max_messages: The memory_extract_max_messages of this CreateCoreSpaceRequestBody.
        :type memory_extract_max_messages: int
        """
        self._memory_extract_max_messages = memory_extract_max_messages

    @property
    def tags(self):
        r"""Gets the tags of this CreateCoreSpaceRequestBody.

        **参数解释：** 库标签列表。 **约束限制：** 数组长度0-20个；键最大长度36字符，不允许为空；值最大长度43字符，可以为空。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The tags of this CreateCoreSpaceRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateCoreSpaceRequestBody.

        **参数解释：** 库标签列表。 **约束限制：** 数组长度0-20个；键最大长度36字符，不允许为空；值最大长度43字符，可以为空。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param tags: The tags of this CreateCoreSpaceRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceTag`]
        """
        self._tags = tags

    @property
    def memory_strategies_builtin(self):
        r"""Gets the memory_strategies_builtin of this CreateCoreSpaceRequestBody.

        **参数解释：** 内置策略类型列表，与memory_strategies_customized至少选填一项。 **约束限制：** 数组长度0-10个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The memory_strategies_builtin of this CreateCoreSpaceRequestBody.
        :rtype: list[str]
        """
        return self._memory_strategies_builtin

    @memory_strategies_builtin.setter
    def memory_strategies_builtin(self, memory_strategies_builtin):
        r"""Sets the memory_strategies_builtin of this CreateCoreSpaceRequestBody.

        **参数解释：** 内置策略类型列表，与memory_strategies_customized至少选填一项。 **约束限制：** 数组长度0-10个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param memory_strategies_builtin: The memory_strategies_builtin of this CreateCoreSpaceRequestBody.
        :type memory_strategies_builtin: list[str]
        """
        self._memory_strategies_builtin = memory_strategies_builtin

    @property
    def memory_strategies_customized(self):
        r"""Gets the memory_strategies_customized of this CreateCoreSpaceRequestBody.

        **参数解释：** 长期记忆自定义策略。 **约束限制：** 与memory_strategies_builtin至少选填一项；单个记忆库最多配置10个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The memory_strategies_customized of this CreateCoreSpaceRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CreateCoreSpaceMemoryStrategyRequestBody`]
        """
        return self._memory_strategies_customized

    @memory_strategies_customized.setter
    def memory_strategies_customized(self, memory_strategies_customized):
        r"""Sets the memory_strategies_customized of this CreateCoreSpaceRequestBody.

        **参数解释：** 长期记忆自定义策略。 **约束限制：** 与memory_strategies_builtin至少选填一项；单个记忆库最多配置10个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param memory_strategies_customized: The memory_strategies_customized of this CreateCoreSpaceRequestBody.
        :type memory_strategies_customized: list[:class:`huaweicloudsdkagentarts.v1.CreateCoreSpaceMemoryStrategyRequestBody`]
        """
        self._memory_strategies_customized = memory_strategies_customized

    @property
    def network_access(self):
        r"""Gets the network_access of this CreateCoreSpaceRequestBody.

        :return: The network_access of this CreateCoreSpaceRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CreateCoreSpaceNetworkRequestBody`
        """
        return self._network_access

    @network_access.setter
    def network_access(self, network_access):
        r"""Sets the network_access of this CreateCoreSpaceRequestBody.

        :param network_access: The network_access of this CreateCoreSpaceRequestBody.
        :type network_access: :class:`huaweicloudsdkagentarts.v1.CreateCoreSpaceNetworkRequestBody`
        """
        self._network_access = network_access

    @property
    def encryption_config(self):
        r"""Gets the encryption_config of this CreateCoreSpaceRequestBody.

        :return: The encryption_config of this CreateCoreSpaceRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EncryptionConfig`
        """
        return self._encryption_config

    @encryption_config.setter
    def encryption_config(self, encryption_config):
        r"""Sets the encryption_config of this CreateCoreSpaceRequestBody.

        :param encryption_config: The encryption_config of this CreateCoreSpaceRequestBody.
        :type encryption_config: :class:`huaweicloudsdkagentarts.v1.EncryptionConfig`
        """
        self._encryption_config = encryption_config

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
        if not isinstance(other, CreateCoreSpaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
