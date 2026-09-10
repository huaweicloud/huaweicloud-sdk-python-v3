# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemorySearchReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query': 'str',
        'strategy_type': 'str',
        'strategy_id': 'str',
        'actor_id': 'str',
        'assistant_id': 'str',
        'session_id': 'str',
        'memory_type': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'top_k': 'int',
        'min_score': 'float'
    }

    attribute_map = {
        'query': 'query',
        'strategy_type': 'strategy_type',
        'strategy_id': 'strategy_id',
        'actor_id': 'actor_id',
        'assistant_id': 'assistant_id',
        'session_id': 'session_id',
        'memory_type': 'memory_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'top_k': 'top_k',
        'min_score': 'min_score'
    }

    def __init__(self, query=None, strategy_type=None, strategy_id=None, actor_id=None, assistant_id=None, session_id=None, memory_type=None, start_time=None, end_time=None, top_k=None, min_score=None):
        r"""MemorySearchReq

        The model defined in huaweicloud sdk

        :param query: **参数解释：** 查询文本（可选，不传时仅按过滤条件检索）。 **约束限制：** 不涉及。 **取值范围：** 长度1-2000字符。 **默认取值：** 不涉及。 
        :type query: str
        :param strategy_type: **参数解释：** 按策略类型过滤。semantic（语义记忆）用于存储语义化的信息；summary（摘要记忆）用于对话总结；user_preference（用户偏好）用于存储用户偏好设置；episodic（事件记忆）用于存储特定事件；event（事件记忆）与episodic相同，用于存储特定事件；custom（自定义记忆）用于用户自定义的记忆类型。 **约束限制：** 不涉及。 **取值范围：** - semantic - summary - user_preference - episodic - event - custom **默认取值：** 不涉及。 
        :type strategy_type: str
        :param strategy_id: **参数解释：**  按策略实例 ID 过滤，仅返回指定策略实例关联的记录。策略实例 ID 可通过查询策略接口获取。 **约束限制：**  不涉及。 **取值范围：**  长度36-36字符。 **默认取值：**  不涉及。 
        :type strategy_id: str
        :param actor_id: **参数解释：**  按 Actor ID 过滤，仅返回指定 Actor 关联的记录。Actor ID 用于标识对话参与者。 **约束限制：**  不涉及。 **取值范围：** 长度0-64字符。 **默认取值：** 不涉及。 
        :type actor_id: str
        :param assistant_id: **参数解释：**  按 Assistant ID 过滤，仅返回指定 Assistant 关联的记录。Assistant ID 用于标识 AI 助手。 **约束限制：**  不涉及。 **取值范围：** 长度0-64字符。 **默认取值：** 不涉及。 
        :type assistant_id: str
        :param session_id: **参数解释：**  按 Session ID 过滤，仅返回指定 Session 关联的记录。 **约束限制：**  不涉及。 **取值范围：**  长度36-36字符。 **默认取值：**  不涉及。 
        :type session_id: str
        :param memory_type: **参数解释：**  按记忆类型过滤。 **约束限制：**  不涉及。 **取值范围：**  - memory - episode - reflection **默认取值：**  memory（一般记忆）用于存储一般的记忆信息；episode（事件记忆）用于存储特定事件；reflection（反思记忆）用于存储反思和总结。 
        :type memory_type: str
        :param start_time: **参数解释：**  按创建时间过滤的起始时间（毫秒时间戳，包含），仅返回创建时间大于等于此时间的记录。 **约束限制：**  不涉及。 **取值范围：**  0-253402300799999 **默认取值：**  0-253402300799999 
        :type start_time: int
        :param end_time: **参数解释：**  按创建时间过滤的结束时间（毫秒时间戳，包含），仅返回创建时间小于等于此时间的记录。 **约束限制：**  不涉及。 **取值范围：**  0-253402300799999 **默认取值：**  0-253402300799999 
        :type end_time: int
        :param top_k: **参数解释：** 返回相似度最高的前 K 个结果，用于控制检索返回数量。 **约束限制：** 不涉及。 **取值范围：** 1-100 **默认取值：** 10 
        :type top_k: int
        :param min_score: **参数解释：**  最小向量相似度分数阈值（基于 OpenSearch 向量检索分数过滤，Rerank 前生效）。 **约束限制：**  不涉及。 **取值范围：**  0.0-1.0 **默认取值：**  不涉及。 
        :type min_score: float
        """
        
        

        self._query = None
        self._strategy_type = None
        self._strategy_id = None
        self._actor_id = None
        self._assistant_id = None
        self._session_id = None
        self._memory_type = None
        self._start_time = None
        self._end_time = None
        self._top_k = None
        self._min_score = None
        self.discriminator = None

        if query is not None:
            self.query = query
        if strategy_type is not None:
            self.strategy_type = strategy_type
        if strategy_id is not None:
            self.strategy_id = strategy_id
        if actor_id is not None:
            self.actor_id = actor_id
        if assistant_id is not None:
            self.assistant_id = assistant_id
        if session_id is not None:
            self.session_id = session_id
        if memory_type is not None:
            self.memory_type = memory_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if top_k is not None:
            self.top_k = top_k
        if min_score is not None:
            self.min_score = min_score

    @property
    def query(self):
        r"""Gets the query of this MemorySearchReq.

        **参数解释：** 查询文本（可选，不传时仅按过滤条件检索）。 **约束限制：** 不涉及。 **取值范围：** 长度1-2000字符。 **默认取值：** 不涉及。 

        :return: The query of this MemorySearchReq.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this MemorySearchReq.

        **参数解释：** 查询文本（可选，不传时仅按过滤条件检索）。 **约束限制：** 不涉及。 **取值范围：** 长度1-2000字符。 **默认取值：** 不涉及。 

        :param query: The query of this MemorySearchReq.
        :type query: str
        """
        self._query = query

    @property
    def strategy_type(self):
        r"""Gets the strategy_type of this MemorySearchReq.

        **参数解释：** 按策略类型过滤。semantic（语义记忆）用于存储语义化的信息；summary（摘要记忆）用于对话总结；user_preference（用户偏好）用于存储用户偏好设置；episodic（事件记忆）用于存储特定事件；event（事件记忆）与episodic相同，用于存储特定事件；custom（自定义记忆）用于用户自定义的记忆类型。 **约束限制：** 不涉及。 **取值范围：** - semantic - summary - user_preference - episodic - event - custom **默认取值：** 不涉及。 

        :return: The strategy_type of this MemorySearchReq.
        :rtype: str
        """
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, strategy_type):
        r"""Sets the strategy_type of this MemorySearchReq.

        **参数解释：** 按策略类型过滤。semantic（语义记忆）用于存储语义化的信息；summary（摘要记忆）用于对话总结；user_preference（用户偏好）用于存储用户偏好设置；episodic（事件记忆）用于存储特定事件；event（事件记忆）与episodic相同，用于存储特定事件；custom（自定义记忆）用于用户自定义的记忆类型。 **约束限制：** 不涉及。 **取值范围：** - semantic - summary - user_preference - episodic - event - custom **默认取值：** 不涉及。 

        :param strategy_type: The strategy_type of this MemorySearchReq.
        :type strategy_type: str
        """
        self._strategy_type = strategy_type

    @property
    def strategy_id(self):
        r"""Gets the strategy_id of this MemorySearchReq.

        **参数解释：**  按策略实例 ID 过滤，仅返回指定策略实例关联的记录。策略实例 ID 可通过查询策略接口获取。 **约束限制：**  不涉及。 **取值范围：**  长度36-36字符。 **默认取值：**  不涉及。 

        :return: The strategy_id of this MemorySearchReq.
        :rtype: str
        """
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, strategy_id):
        r"""Sets the strategy_id of this MemorySearchReq.

        **参数解释：**  按策略实例 ID 过滤，仅返回指定策略实例关联的记录。策略实例 ID 可通过查询策略接口获取。 **约束限制：**  不涉及。 **取值范围：**  长度36-36字符。 **默认取值：**  不涉及。 

        :param strategy_id: The strategy_id of this MemorySearchReq.
        :type strategy_id: str
        """
        self._strategy_id = strategy_id

    @property
    def actor_id(self):
        r"""Gets the actor_id of this MemorySearchReq.

        **参数解释：**  按 Actor ID 过滤，仅返回指定 Actor 关联的记录。Actor ID 用于标识对话参与者。 **约束限制：**  不涉及。 **取值范围：** 长度0-64字符。 **默认取值：** 不涉及。 

        :return: The actor_id of this MemorySearchReq.
        :rtype: str
        """
        return self._actor_id

    @actor_id.setter
    def actor_id(self, actor_id):
        r"""Sets the actor_id of this MemorySearchReq.

        **参数解释：**  按 Actor ID 过滤，仅返回指定 Actor 关联的记录。Actor ID 用于标识对话参与者。 **约束限制：**  不涉及。 **取值范围：** 长度0-64字符。 **默认取值：** 不涉及。 

        :param actor_id: The actor_id of this MemorySearchReq.
        :type actor_id: str
        """
        self._actor_id = actor_id

    @property
    def assistant_id(self):
        r"""Gets the assistant_id of this MemorySearchReq.

        **参数解释：**  按 Assistant ID 过滤，仅返回指定 Assistant 关联的记录。Assistant ID 用于标识 AI 助手。 **约束限制：**  不涉及。 **取值范围：** 长度0-64字符。 **默认取值：** 不涉及。 

        :return: The assistant_id of this MemorySearchReq.
        :rtype: str
        """
        return self._assistant_id

    @assistant_id.setter
    def assistant_id(self, assistant_id):
        r"""Sets the assistant_id of this MemorySearchReq.

        **参数解释：**  按 Assistant ID 过滤，仅返回指定 Assistant 关联的记录。Assistant ID 用于标识 AI 助手。 **约束限制：**  不涉及。 **取值范围：** 长度0-64字符。 **默认取值：** 不涉及。 

        :param assistant_id: The assistant_id of this MemorySearchReq.
        :type assistant_id: str
        """
        self._assistant_id = assistant_id

    @property
    def session_id(self):
        r"""Gets the session_id of this MemorySearchReq.

        **参数解释：**  按 Session ID 过滤，仅返回指定 Session 关联的记录。 **约束限制：**  不涉及。 **取值范围：**  长度36-36字符。 **默认取值：**  不涉及。 

        :return: The session_id of this MemorySearchReq.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this MemorySearchReq.

        **参数解释：**  按 Session ID 过滤，仅返回指定 Session 关联的记录。 **约束限制：**  不涉及。 **取值范围：**  长度36-36字符。 **默认取值：**  不涉及。 

        :param session_id: The session_id of this MemorySearchReq.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def memory_type(self):
        r"""Gets the memory_type of this MemorySearchReq.

        **参数解释：**  按记忆类型过滤。 **约束限制：**  不涉及。 **取值范围：**  - memory - episode - reflection **默认取值：**  memory（一般记忆）用于存储一般的记忆信息；episode（事件记忆）用于存储特定事件；reflection（反思记忆）用于存储反思和总结。 

        :return: The memory_type of this MemorySearchReq.
        :rtype: str
        """
        return self._memory_type

    @memory_type.setter
    def memory_type(self, memory_type):
        r"""Sets the memory_type of this MemorySearchReq.

        **参数解释：**  按记忆类型过滤。 **约束限制：**  不涉及。 **取值范围：**  - memory - episode - reflection **默认取值：**  memory（一般记忆）用于存储一般的记忆信息；episode（事件记忆）用于存储特定事件；reflection（反思记忆）用于存储反思和总结。 

        :param memory_type: The memory_type of this MemorySearchReq.
        :type memory_type: str
        """
        self._memory_type = memory_type

    @property
    def start_time(self):
        r"""Gets the start_time of this MemorySearchReq.

        **参数解释：**  按创建时间过滤的起始时间（毫秒时间戳，包含），仅返回创建时间大于等于此时间的记录。 **约束限制：**  不涉及。 **取值范围：**  0-253402300799999 **默认取值：**  0-253402300799999 

        :return: The start_time of this MemorySearchReq.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this MemorySearchReq.

        **参数解释：**  按创建时间过滤的起始时间（毫秒时间戳，包含），仅返回创建时间大于等于此时间的记录。 **约束限制：**  不涉及。 **取值范围：**  0-253402300799999 **默认取值：**  0-253402300799999 

        :param start_time: The start_time of this MemorySearchReq.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this MemorySearchReq.

        **参数解释：**  按创建时间过滤的结束时间（毫秒时间戳，包含），仅返回创建时间小于等于此时间的记录。 **约束限制：**  不涉及。 **取值范围：**  0-253402300799999 **默认取值：**  0-253402300799999 

        :return: The end_time of this MemorySearchReq.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this MemorySearchReq.

        **参数解释：**  按创建时间过滤的结束时间（毫秒时间戳，包含），仅返回创建时间小于等于此时间的记录。 **约束限制：**  不涉及。 **取值范围：**  0-253402300799999 **默认取值：**  0-253402300799999 

        :param end_time: The end_time of this MemorySearchReq.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def top_k(self):
        r"""Gets the top_k of this MemorySearchReq.

        **参数解释：** 返回相似度最高的前 K 个结果，用于控制检索返回数量。 **约束限制：** 不涉及。 **取值范围：** 1-100 **默认取值：** 10 

        :return: The top_k of this MemorySearchReq.
        :rtype: int
        """
        return self._top_k

    @top_k.setter
    def top_k(self, top_k):
        r"""Sets the top_k of this MemorySearchReq.

        **参数解释：** 返回相似度最高的前 K 个结果，用于控制检索返回数量。 **约束限制：** 不涉及。 **取值范围：** 1-100 **默认取值：** 10 

        :param top_k: The top_k of this MemorySearchReq.
        :type top_k: int
        """
        self._top_k = top_k

    @property
    def min_score(self):
        r"""Gets the min_score of this MemorySearchReq.

        **参数解释：**  最小向量相似度分数阈值（基于 OpenSearch 向量检索分数过滤，Rerank 前生效）。 **约束限制：**  不涉及。 **取值范围：**  0.0-1.0 **默认取值：**  不涉及。 

        :return: The min_score of this MemorySearchReq.
        :rtype: float
        """
        return self._min_score

    @min_score.setter
    def min_score(self, min_score):
        r"""Sets the min_score of this MemorySearchReq.

        **参数解释：**  最小向量相似度分数阈值（基于 OpenSearch 向量检索分数过滤，Rerank 前生效）。 **约束限制：**  不涉及。 **取值范围：**  0.0-1.0 **默认取值：**  不涉及。 

        :param min_score: The min_score of this MemorySearchReq.
        :type min_score: float
        """
        self._min_score = min_score

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
        if not isinstance(other, MemorySearchReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
