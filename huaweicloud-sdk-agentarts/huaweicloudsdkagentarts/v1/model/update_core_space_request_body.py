# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreSpaceRequestBody:

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
        'message_ttl_hours': 'int',
        'memory_extract_enabled': 'bool',
        'memory_extract_idle_seconds': 'int',
        'memory_extract_max_tokens': 'int',
        'memory_extract_max_messages': 'int',
        'tags': 'list[CoreSpaceTag]',
        'memory_strategies_builtin': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'message_ttl_hours': 'message_ttl_hours',
        'memory_extract_enabled': 'memory_extract_enabled',
        'memory_extract_idle_seconds': 'memory_extract_idle_seconds',
        'memory_extract_max_tokens': 'memory_extract_max_tokens',
        'memory_extract_max_messages': 'memory_extract_max_messages',
        'tags': 'tags',
        'memory_strategies_builtin': 'memory_strategies_builtin'
    }

    def __init__(self, name=None, description=None, message_ttl_hours=None, memory_extract_enabled=None, memory_extract_idle_seconds=None, memory_extract_max_tokens=None, memory_extract_max_messages=None, tags=None, memory_strategies_builtin=None):
        r"""UpdateCoreSpaceRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：**  记忆库名称。 **约束限制：**  支持字母、数字和中划线。 **取值范围：**  长度1-48字符。 **默认取值：** 不涉及。 
        :type name: str
        :param description: **参数解释：**  记忆库描述。 **约束限制：**  不涉及。 **取值范围：** 不超过1000长度的字符串。 **默认取值：** 不涉及。 
        :type description: str
        :param message_ttl_hours: **参数解释：** Message过期时间（小时）。 **约束限制：** 最大8760个小时（365天）。 **取值范围：** 1-8760 **默认取值：** 不涉及。 
        :type message_ttl_hours: int
        :param memory_extract_enabled: **参数解释：** 是否开启记忆抽取。 **约束限制：** 不涉及。 **取值范围：** - true: 开启记忆抽取 - false: 关闭记忆抽取 **默认取值：** 不涉及。 
        :type memory_extract_enabled: bool
        :param memory_extract_idle_seconds: **参数解释：**  触发记忆抽取空闲时间（秒）。 **约束限制：**  不涉及。 **取值范围：**  10-86400（24小时） **默认取值：** 不涉及。 
        :type memory_extract_idle_seconds: int
        :param memory_extract_max_tokens: **参数解释：** 触发记忆抽取最大累计 token 数。 **约束限制：** 不涉及。 **取值范围：** 1000-1073741824 **默认取值：** 不涉及。 
        :type memory_extract_max_tokens: int
        :param memory_extract_max_messages: **参数解释：**  触发记忆抽取最大累计 message 数。 **约束限制：**  不涉及。 **取值范围：** 3-10000 **默认取值：** 不涉及。 
        :type memory_extract_max_messages: int
        :param tags: **参数解释：** 库标签列表。 **约束限制：** 数组长度0-20个；键最大长度36字符，不允许为空；值最大长度43字符，可以为空。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceTag`]
        :param memory_strategies_builtin: **参数解释：** 内置策略类型列表。 **约束限制：** 数组长度0-10个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type memory_strategies_builtin: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._message_ttl_hours = None
        self._memory_extract_enabled = None
        self._memory_extract_idle_seconds = None
        self._memory_extract_max_tokens = None
        self._memory_extract_max_messages = None
        self._tags = None
        self._memory_strategies_builtin = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if message_ttl_hours is not None:
            self.message_ttl_hours = message_ttl_hours
        if memory_extract_enabled is not None:
            self.memory_extract_enabled = memory_extract_enabled
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

    @property
    def name(self):
        r"""Gets the name of this UpdateCoreSpaceRequestBody.

        **参数解释：**  记忆库名称。 **约束限制：**  支持字母、数字和中划线。 **取值范围：**  长度1-48字符。 **默认取值：** 不涉及。 

        :return: The name of this UpdateCoreSpaceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateCoreSpaceRequestBody.

        **参数解释：**  记忆库名称。 **约束限制：**  支持字母、数字和中划线。 **取值范围：**  长度1-48字符。 **默认取值：** 不涉及。 

        :param name: The name of this UpdateCoreSpaceRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateCoreSpaceRequestBody.

        **参数解释：**  记忆库描述。 **约束限制：**  不涉及。 **取值范围：** 不超过1000长度的字符串。 **默认取值：** 不涉及。 

        :return: The description of this UpdateCoreSpaceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateCoreSpaceRequestBody.

        **参数解释：**  记忆库描述。 **约束限制：**  不涉及。 **取值范围：** 不超过1000长度的字符串。 **默认取值：** 不涉及。 

        :param description: The description of this UpdateCoreSpaceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def message_ttl_hours(self):
        r"""Gets the message_ttl_hours of this UpdateCoreSpaceRequestBody.

        **参数解释：** Message过期时间（小时）。 **约束限制：** 最大8760个小时（365天）。 **取值范围：** 1-8760 **默认取值：** 不涉及。 

        :return: The message_ttl_hours of this UpdateCoreSpaceRequestBody.
        :rtype: int
        """
        return self._message_ttl_hours

    @message_ttl_hours.setter
    def message_ttl_hours(self, message_ttl_hours):
        r"""Sets the message_ttl_hours of this UpdateCoreSpaceRequestBody.

        **参数解释：** Message过期时间（小时）。 **约束限制：** 最大8760个小时（365天）。 **取值范围：** 1-8760 **默认取值：** 不涉及。 

        :param message_ttl_hours: The message_ttl_hours of this UpdateCoreSpaceRequestBody.
        :type message_ttl_hours: int
        """
        self._message_ttl_hours = message_ttl_hours

    @property
    def memory_extract_enabled(self):
        r"""Gets the memory_extract_enabled of this UpdateCoreSpaceRequestBody.

        **参数解释：** 是否开启记忆抽取。 **约束限制：** 不涉及。 **取值范围：** - true: 开启记忆抽取 - false: 关闭记忆抽取 **默认取值：** 不涉及。 

        :return: The memory_extract_enabled of this UpdateCoreSpaceRequestBody.
        :rtype: bool
        """
        return self._memory_extract_enabled

    @memory_extract_enabled.setter
    def memory_extract_enabled(self, memory_extract_enabled):
        r"""Sets the memory_extract_enabled of this UpdateCoreSpaceRequestBody.

        **参数解释：** 是否开启记忆抽取。 **约束限制：** 不涉及。 **取值范围：** - true: 开启记忆抽取 - false: 关闭记忆抽取 **默认取值：** 不涉及。 

        :param memory_extract_enabled: The memory_extract_enabled of this UpdateCoreSpaceRequestBody.
        :type memory_extract_enabled: bool
        """
        self._memory_extract_enabled = memory_extract_enabled

    @property
    def memory_extract_idle_seconds(self):
        r"""Gets the memory_extract_idle_seconds of this UpdateCoreSpaceRequestBody.

        **参数解释：**  触发记忆抽取空闲时间（秒）。 **约束限制：**  不涉及。 **取值范围：**  10-86400（24小时） **默认取值：** 不涉及。 

        :return: The memory_extract_idle_seconds of this UpdateCoreSpaceRequestBody.
        :rtype: int
        """
        return self._memory_extract_idle_seconds

    @memory_extract_idle_seconds.setter
    def memory_extract_idle_seconds(self, memory_extract_idle_seconds):
        r"""Sets the memory_extract_idle_seconds of this UpdateCoreSpaceRequestBody.

        **参数解释：**  触发记忆抽取空闲时间（秒）。 **约束限制：**  不涉及。 **取值范围：**  10-86400（24小时） **默认取值：** 不涉及。 

        :param memory_extract_idle_seconds: The memory_extract_idle_seconds of this UpdateCoreSpaceRequestBody.
        :type memory_extract_idle_seconds: int
        """
        self._memory_extract_idle_seconds = memory_extract_idle_seconds

    @property
    def memory_extract_max_tokens(self):
        r"""Gets the memory_extract_max_tokens of this UpdateCoreSpaceRequestBody.

        **参数解释：** 触发记忆抽取最大累计 token 数。 **约束限制：** 不涉及。 **取值范围：** 1000-1073741824 **默认取值：** 不涉及。 

        :return: The memory_extract_max_tokens of this UpdateCoreSpaceRequestBody.
        :rtype: int
        """
        return self._memory_extract_max_tokens

    @memory_extract_max_tokens.setter
    def memory_extract_max_tokens(self, memory_extract_max_tokens):
        r"""Sets the memory_extract_max_tokens of this UpdateCoreSpaceRequestBody.

        **参数解释：** 触发记忆抽取最大累计 token 数。 **约束限制：** 不涉及。 **取值范围：** 1000-1073741824 **默认取值：** 不涉及。 

        :param memory_extract_max_tokens: The memory_extract_max_tokens of this UpdateCoreSpaceRequestBody.
        :type memory_extract_max_tokens: int
        """
        self._memory_extract_max_tokens = memory_extract_max_tokens

    @property
    def memory_extract_max_messages(self):
        r"""Gets the memory_extract_max_messages of this UpdateCoreSpaceRequestBody.

        **参数解释：**  触发记忆抽取最大累计 message 数。 **约束限制：**  不涉及。 **取值范围：** 3-10000 **默认取值：** 不涉及。 

        :return: The memory_extract_max_messages of this UpdateCoreSpaceRequestBody.
        :rtype: int
        """
        return self._memory_extract_max_messages

    @memory_extract_max_messages.setter
    def memory_extract_max_messages(self, memory_extract_max_messages):
        r"""Sets the memory_extract_max_messages of this UpdateCoreSpaceRequestBody.

        **参数解释：**  触发记忆抽取最大累计 message 数。 **约束限制：**  不涉及。 **取值范围：** 3-10000 **默认取值：** 不涉及。 

        :param memory_extract_max_messages: The memory_extract_max_messages of this UpdateCoreSpaceRequestBody.
        :type memory_extract_max_messages: int
        """
        self._memory_extract_max_messages = memory_extract_max_messages

    @property
    def tags(self):
        r"""Gets the tags of this UpdateCoreSpaceRequestBody.

        **参数解释：** 库标签列表。 **约束限制：** 数组长度0-20个；键最大长度36字符，不允许为空；值最大长度43字符，可以为空。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The tags of this UpdateCoreSpaceRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateCoreSpaceRequestBody.

        **参数解释：** 库标签列表。 **约束限制：** 数组长度0-20个；键最大长度36字符，不允许为空；值最大长度43字符，可以为空。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param tags: The tags of this UpdateCoreSpaceRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceTag`]
        """
        self._tags = tags

    @property
    def memory_strategies_builtin(self):
        r"""Gets the memory_strategies_builtin of this UpdateCoreSpaceRequestBody.

        **参数解释：** 内置策略类型列表。 **约束限制：** 数组长度0-10个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The memory_strategies_builtin of this UpdateCoreSpaceRequestBody.
        :rtype: list[str]
        """
        return self._memory_strategies_builtin

    @memory_strategies_builtin.setter
    def memory_strategies_builtin(self, memory_strategies_builtin):
        r"""Sets the memory_strategies_builtin of this UpdateCoreSpaceRequestBody.

        **参数解释：** 内置策略类型列表。 **约束限制：** 数组长度0-10个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param memory_strategies_builtin: The memory_strategies_builtin of this UpdateCoreSpaceRequestBody.
        :type memory_strategies_builtin: list[str]
        """
        self._memory_strategies_builtin = memory_strategies_builtin

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
        if not isinstance(other, UpdateCoreSpaceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
