# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemoryRecord:

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
        'space_id': 'str',
        'strategy_id': 'str',
        'strategy_type': 'str',
        'actor_id': 'str',
        'assistant_id': 'str',
        'session_id': 'str',
        'content': 'str',
        'memory_type': 'str',
        'isolation_level': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'space_id': 'space_id',
        'strategy_id': 'strategy_id',
        'strategy_type': 'strategy_type',
        'actor_id': 'actor_id',
        'assistant_id': 'assistant_id',
        'session_id': 'session_id',
        'content': 'content',
        'memory_type': 'memory_type',
        'isolation_level': 'isolation_level',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, space_id=None, strategy_id=None, strategy_type=None, actor_id=None, assistant_id=None, session_id=None, content=None, memory_type=None, isolation_level=None, created_at=None, updated_at=None):
        r"""MemoryRecord

        The model defined in huaweicloud sdk

        :param id: **参数解释：**  记忆记录 ID，唯一标识一条记忆记录，创建记忆时由系统自动生成。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 
        :type id: str
        :param space_id: **参数解释：**  所属 Space ID，标识该记录所属的记忆库。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 
        :type space_id: str
        :param strategy_id: **参数解释：**  来源策略 ID，标识该记忆记录由哪个策略生成，可通过查询策略接口获取。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 
        :type strategy_id: str
        :param strategy_type: **参数解释：**  策略类型，决定记忆的存储和使用方式。 **取值范围：**  semantic（语义记忆）用于存储语义化的信息；summary（摘要记忆）用于对话总结；user_preference（用户偏好）用于存储用户偏好设置；episodic（事件记忆）用于存储特定事件；event（事件记忆）与episodic相同，用于存储特定事件；custom（自定义记忆）用于用户自定义的记忆类型。 **默认取值：** 不涉及。 
        :type strategy_type: str
        :param actor_id: **参数解释：**  归属 Actor ID，标识该记忆记录所属的 Actor，实现 Actor 级记忆隔离。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 
        :type actor_id: str
        :param assistant_id: **参数解释：**  归属 Assistant ID，标识该记录所属的 AI 助手。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 
        :type assistant_id: str
        :param session_id: **参数解释：**  来源会话 ID，标识该记忆记录关联的会话，实现 Session 级记忆隔离。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 
        :type session_id: str
        :param content: **参数解释：**  记忆内容，存储具体的记忆信息文本，如用户偏好、重要事实等。 **取值范围：** 1-10000 字符。 **默认取值：** 不涉及。 
        :type content: str
        :param memory_type: **参数解释：**  记忆类型，标识记忆的存储形式。 **取值范围：** memory（一般记忆）用于存储一般的记忆信息；episode（事件记忆）用于存储特定事件；reflection（反思记忆）用于存储反思和总结。 
        :type memory_type: str
        :param isolation_level: **参数解释：**  记忆隔离级别，控制记忆的可见范围。 **取值范围：**  actor（Actor 隔离）记忆只能在 Actor 内部共享；session（Session 隔离）记忆只能在 Session 内部共享。 不涉及。 
        :type isolation_level: str
        :param created_at: **参数解释：**  记录的创建时间，由系统自动生成，格式为 ISO 8601。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 
        :type created_at: datetime
        :param updated_at: **参数解释：**  记录的最近更新时间，由系统自动更新，格式为 ISO 8601。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._space_id = None
        self._strategy_id = None
        self._strategy_type = None
        self._actor_id = None
        self._assistant_id = None
        self._session_id = None
        self._content = None
        self._memory_type = None
        self._isolation_level = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.space_id = space_id
        self.strategy_id = strategy_id
        self.strategy_type = strategy_type
        if actor_id is not None:
            self.actor_id = actor_id
        if assistant_id is not None:
            self.assistant_id = assistant_id
        if session_id is not None:
            self.session_id = session_id
        self.content = content
        if memory_type is not None:
            self.memory_type = memory_type
        if isolation_level is not None:
            self.isolation_level = isolation_level
        self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this MemoryRecord.

        **参数解释：**  记忆记录 ID，唯一标识一条记忆记录，创建记忆时由系统自动生成。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :return: The id of this MemoryRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MemoryRecord.

        **参数解释：**  记忆记录 ID，唯一标识一条记忆记录，创建记忆时由系统自动生成。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :param id: The id of this MemoryRecord.
        :type id: str
        """
        self._id = id

    @property
    def space_id(self):
        r"""Gets the space_id of this MemoryRecord.

        **参数解释：**  所属 Space ID，标识该记录所属的记忆库。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :return: The space_id of this MemoryRecord.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        r"""Sets the space_id of this MemoryRecord.

        **参数解释：**  所属 Space ID，标识该记录所属的记忆库。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :param space_id: The space_id of this MemoryRecord.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def strategy_id(self):
        r"""Gets the strategy_id of this MemoryRecord.

        **参数解释：**  来源策略 ID，标识该记忆记录由哪个策略生成，可通过查询策略接口获取。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :return: The strategy_id of this MemoryRecord.
        :rtype: str
        """
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, strategy_id):
        r"""Sets the strategy_id of this MemoryRecord.

        **参数解释：**  来源策略 ID，标识该记忆记录由哪个策略生成，可通过查询策略接口获取。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :param strategy_id: The strategy_id of this MemoryRecord.
        :type strategy_id: str
        """
        self._strategy_id = strategy_id

    @property
    def strategy_type(self):
        r"""Gets the strategy_type of this MemoryRecord.

        **参数解释：**  策略类型，决定记忆的存储和使用方式。 **取值范围：**  semantic（语义记忆）用于存储语义化的信息；summary（摘要记忆）用于对话总结；user_preference（用户偏好）用于存储用户偏好设置；episodic（事件记忆）用于存储特定事件；event（事件记忆）与episodic相同，用于存储特定事件；custom（自定义记忆）用于用户自定义的记忆类型。 **默认取值：** 不涉及。 

        :return: The strategy_type of this MemoryRecord.
        :rtype: str
        """
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, strategy_type):
        r"""Sets the strategy_type of this MemoryRecord.

        **参数解释：**  策略类型，决定记忆的存储和使用方式。 **取值范围：**  semantic（语义记忆）用于存储语义化的信息；summary（摘要记忆）用于对话总结；user_preference（用户偏好）用于存储用户偏好设置；episodic（事件记忆）用于存储特定事件；event（事件记忆）与episodic相同，用于存储特定事件；custom（自定义记忆）用于用户自定义的记忆类型。 **默认取值：** 不涉及。 

        :param strategy_type: The strategy_type of this MemoryRecord.
        :type strategy_type: str
        """
        self._strategy_type = strategy_type

    @property
    def actor_id(self):
        r"""Gets the actor_id of this MemoryRecord.

        **参数解释：**  归属 Actor ID，标识该记忆记录所属的 Actor，实现 Actor 级记忆隔离。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :return: The actor_id of this MemoryRecord.
        :rtype: str
        """
        return self._actor_id

    @actor_id.setter
    def actor_id(self, actor_id):
        r"""Sets the actor_id of this MemoryRecord.

        **参数解释：**  归属 Actor ID，标识该记忆记录所属的 Actor，实现 Actor 级记忆隔离。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :param actor_id: The actor_id of this MemoryRecord.
        :type actor_id: str
        """
        self._actor_id = actor_id

    @property
    def assistant_id(self):
        r"""Gets the assistant_id of this MemoryRecord.

        **参数解释：**  归属 Assistant ID，标识该记录所属的 AI 助手。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :return: The assistant_id of this MemoryRecord.
        :rtype: str
        """
        return self._assistant_id

    @assistant_id.setter
    def assistant_id(self, assistant_id):
        r"""Sets the assistant_id of this MemoryRecord.

        **参数解释：**  归属 Assistant ID，标识该记录所属的 AI 助手。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :param assistant_id: The assistant_id of this MemoryRecord.
        :type assistant_id: str
        """
        self._assistant_id = assistant_id

    @property
    def session_id(self):
        r"""Gets the session_id of this MemoryRecord.

        **参数解释：**  来源会话 ID，标识该记忆记录关联的会话，实现 Session 级记忆隔离。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :return: The session_id of this MemoryRecord.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this MemoryRecord.

        **参数解释：**  来源会话 ID，标识该记忆记录关联的会话，实现 Session 级记忆隔离。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :param session_id: The session_id of this MemoryRecord.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def content(self):
        r"""Gets the content of this MemoryRecord.

        **参数解释：**  记忆内容，存储具体的记忆信息文本，如用户偏好、重要事实等。 **取值范围：** 1-10000 字符。 **默认取值：** 不涉及。 

        :return: The content of this MemoryRecord.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this MemoryRecord.

        **参数解释：**  记忆内容，存储具体的记忆信息文本，如用户偏好、重要事实等。 **取值范围：** 1-10000 字符。 **默认取值：** 不涉及。 

        :param content: The content of this MemoryRecord.
        :type content: str
        """
        self._content = content

    @property
    def memory_type(self):
        r"""Gets the memory_type of this MemoryRecord.

        **参数解释：**  记忆类型，标识记忆的存储形式。 **取值范围：** memory（一般记忆）用于存储一般的记忆信息；episode（事件记忆）用于存储特定事件；reflection（反思记忆）用于存储反思和总结。 

        :return: The memory_type of this MemoryRecord.
        :rtype: str
        """
        return self._memory_type

    @memory_type.setter
    def memory_type(self, memory_type):
        r"""Sets the memory_type of this MemoryRecord.

        **参数解释：**  记忆类型，标识记忆的存储形式。 **取值范围：** memory（一般记忆）用于存储一般的记忆信息；episode（事件记忆）用于存储特定事件；reflection（反思记忆）用于存储反思和总结。 

        :param memory_type: The memory_type of this MemoryRecord.
        :type memory_type: str
        """
        self._memory_type = memory_type

    @property
    def isolation_level(self):
        r"""Gets the isolation_level of this MemoryRecord.

        **参数解释：**  记忆隔离级别，控制记忆的可见范围。 **取值范围：**  actor（Actor 隔离）记忆只能在 Actor 内部共享；session（Session 隔离）记忆只能在 Session 内部共享。 不涉及。 

        :return: The isolation_level of this MemoryRecord.
        :rtype: str
        """
        return self._isolation_level

    @isolation_level.setter
    def isolation_level(self, isolation_level):
        r"""Sets the isolation_level of this MemoryRecord.

        **参数解释：**  记忆隔离级别，控制记忆的可见范围。 **取值范围：**  actor（Actor 隔离）记忆只能在 Actor 内部共享；session（Session 隔离）记忆只能在 Session 内部共享。 不涉及。 

        :param isolation_level: The isolation_level of this MemoryRecord.
        :type isolation_level: str
        """
        self._isolation_level = isolation_level

    @property
    def created_at(self):
        r"""Gets the created_at of this MemoryRecord.

        **参数解释：**  记录的创建时间，由系统自动生成，格式为 ISO 8601。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :return: The created_at of this MemoryRecord.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MemoryRecord.

        **参数解释：**  记录的创建时间，由系统自动生成，格式为 ISO 8601。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :param created_at: The created_at of this MemoryRecord.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this MemoryRecord.

        **参数解释：**  记录的最近更新时间，由系统自动更新，格式为 ISO 8601。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :return: The updated_at of this MemoryRecord.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this MemoryRecord.

        **参数解释：**  记录的最近更新时间，由系统自动更新，格式为 ISO 8601。 **取值范围：**  不涉及。 **默认取值：** 不涉及。 

        :param updated_at: The updated_at of this MemoryRecord.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, MemoryRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
