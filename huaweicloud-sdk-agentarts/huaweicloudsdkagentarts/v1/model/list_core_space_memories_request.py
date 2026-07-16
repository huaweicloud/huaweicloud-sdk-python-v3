# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreSpaceMemoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'space_id': 'str',
        'strategy_type': 'str',
        'strategy_id': 'str',
        'actor_id': 'str',
        'assistant_id': 'str',
        'session_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'sort_by': 'str',
        'sort_order': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'space_id': 'space_id',
        'strategy_type': 'strategy_type',
        'strategy_id': 'strategy_id',
        'actor_id': 'actor_id',
        'assistant_id': 'assistant_id',
        'session_id': 'session_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'sort_by': 'sort_by',
        'sort_order': 'sort_order',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, space_id=None, strategy_type=None, strategy_id=None, actor_id=None, assistant_id=None, session_id=None, start_time=None, end_time=None, sort_by=None, sort_order=None, limit=None, offset=None):
        r"""ListCoreSpaceMemoriesRequest

        The model defined in huaweicloud sdk

        :param space_id: **参数解释：**  记忆库 ID，唯一标识一个记忆库，可以通过AgentArts智能体记忆库控制台或者记忆库查询接口获取。 **约束限制：** 仅支持字母、数字和中划线。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type space_id: str
        :param strategy_type: **参数解释：** 按策略类型过滤。semantic（语义记忆）用于存储语义化的信息；summary（摘要记忆）用于对话总结；user_preference（用户偏好）用于存储用户偏好设置；episodic（事件记忆）用于存储特定事件；event（事件记忆）与episodic相同，用于存储特定事件；custom（自定义记忆）用于用户自定义的记忆类型。 **约束限制：** 不涉及。 **取值范围：** - semantic - summary - user_preference - episodic - event - custom **默认取值：** 不涉及。 
        :type strategy_type: str
        :param strategy_id: **参数解释：** 按策略实例 ID 过滤。 **约束限制：** 不涉及。 **取值范围：** 长度36-36字符。  **默认取值：** 不涉及。 
        :type strategy_id: str
        :param actor_id: **参数解释：**  按 Actor ID 过滤，仅返回指定 Actor 关联的记录。Actor ID 用于标识对话参与者。 **约束限制：**  不涉及。 **取值范围：** 长度范围 1-64 字符。 **默认取值：** 不涉及。 
        :type actor_id: str
        :param assistant_id: **参数解释：**  按 Assistant ID 过滤，仅返回指定 Assistant 关联的记录。Assistant ID 用于标识 AI 助手。 **约束限制：**  不涉及。 **取值范围：** 长度范围 1-64 字符。 **默认取值：** 不涉及。 
        :type assistant_id: str
        :param session_id: **参数解释：**  按 Session ID 过滤，仅返回指定 Session 关联的记录。 **约束限制：**  不涉及。 **取值范围：** 长度36-36字符。 **默认取值：** 不涉及。 
        :type session_id: str
        :param start_time: **参数解释：**  按创建时间过滤的起始时间（毫秒时间戳，包含），仅返回创建时间大于等于此时间的记录。 **约束限制：**  不涉及。 **取值范围：**  0-253402300799999 **默认取值：** 不涉及。 
        :type start_time: int
        :param end_time: **参数解释：**  按创建时间过滤的结束时间（毫秒时间戳，包含），仅返回创建时间小于等于此时间的记录。 **约束限制：**  不涉及。 **取值范围：**  0-253402300799999 **默认取值：** 不涉及。 
        :type end_time: int
        :param sort_by: **参数解释：**  排序字段，指定按哪个字段对结果进行排序。 **约束限制：**  不涉及。 **取值范围：** created_at（按创建时间排序）根据记录的创建时间进行排序；updated_at（按更新时间排序）根据记录的最近更新时间进行排序。 **默认取值：** created_at 
        :type sort_by: str
        :param sort_order: **参数解释：**  排序方向，指定按升序还是降序排列结果。 **约束限制：**  不涉及。 **取值范围：** asc（升序）按从小到大顺序排序；desc（降序）按从大到小顺序排序。 **默认取值：** desc 
        :type sort_order: str
        :param limit: **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值1000。 **默认取值：** 1000。
        :type limit: int
        :param offset: **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 
        :type offset: int
        """
        
        

        self._space_id = None
        self._strategy_type = None
        self._strategy_id = None
        self._actor_id = None
        self._assistant_id = None
        self._session_id = None
        self._start_time = None
        self._end_time = None
        self._sort_by = None
        self._sort_order = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.space_id = space_id
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
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def space_id(self):
        r"""Gets the space_id of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  记忆库 ID，唯一标识一个记忆库，可以通过AgentArts智能体记忆库控制台或者记忆库查询接口获取。 **约束限制：** 仅支持字母、数字和中划线。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The space_id of this ListCoreSpaceMemoriesRequest.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        r"""Sets the space_id of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  记忆库 ID，唯一标识一个记忆库，可以通过AgentArts智能体记忆库控制台或者记忆库查询接口获取。 **约束限制：** 仅支持字母、数字和中划线。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param space_id: The space_id of this ListCoreSpaceMemoriesRequest.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def strategy_type(self):
        r"""Gets the strategy_type of this ListCoreSpaceMemoriesRequest.

        **参数解释：** 按策略类型过滤。semantic（语义记忆）用于存储语义化的信息；summary（摘要记忆）用于对话总结；user_preference（用户偏好）用于存储用户偏好设置；episodic（事件记忆）用于存储特定事件；event（事件记忆）与episodic相同，用于存储特定事件；custom（自定义记忆）用于用户自定义的记忆类型。 **约束限制：** 不涉及。 **取值范围：** - semantic - summary - user_preference - episodic - event - custom **默认取值：** 不涉及。 

        :return: The strategy_type of this ListCoreSpaceMemoriesRequest.
        :rtype: str
        """
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, strategy_type):
        r"""Sets the strategy_type of this ListCoreSpaceMemoriesRequest.

        **参数解释：** 按策略类型过滤。semantic（语义记忆）用于存储语义化的信息；summary（摘要记忆）用于对话总结；user_preference（用户偏好）用于存储用户偏好设置；episodic（事件记忆）用于存储特定事件；event（事件记忆）与episodic相同，用于存储特定事件；custom（自定义记忆）用于用户自定义的记忆类型。 **约束限制：** 不涉及。 **取值范围：** - semantic - summary - user_preference - episodic - event - custom **默认取值：** 不涉及。 

        :param strategy_type: The strategy_type of this ListCoreSpaceMemoriesRequest.
        :type strategy_type: str
        """
        self._strategy_type = strategy_type

    @property
    def strategy_id(self):
        r"""Gets the strategy_id of this ListCoreSpaceMemoriesRequest.

        **参数解释：** 按策略实例 ID 过滤。 **约束限制：** 不涉及。 **取值范围：** 长度36-36字符。  **默认取值：** 不涉及。 

        :return: The strategy_id of this ListCoreSpaceMemoriesRequest.
        :rtype: str
        """
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, strategy_id):
        r"""Sets the strategy_id of this ListCoreSpaceMemoriesRequest.

        **参数解释：** 按策略实例 ID 过滤。 **约束限制：** 不涉及。 **取值范围：** 长度36-36字符。  **默认取值：** 不涉及。 

        :param strategy_id: The strategy_id of this ListCoreSpaceMemoriesRequest.
        :type strategy_id: str
        """
        self._strategy_id = strategy_id

    @property
    def actor_id(self):
        r"""Gets the actor_id of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  按 Actor ID 过滤，仅返回指定 Actor 关联的记录。Actor ID 用于标识对话参与者。 **约束限制：**  不涉及。 **取值范围：** 长度范围 1-64 字符。 **默认取值：** 不涉及。 

        :return: The actor_id of this ListCoreSpaceMemoriesRequest.
        :rtype: str
        """
        return self._actor_id

    @actor_id.setter
    def actor_id(self, actor_id):
        r"""Sets the actor_id of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  按 Actor ID 过滤，仅返回指定 Actor 关联的记录。Actor ID 用于标识对话参与者。 **约束限制：**  不涉及。 **取值范围：** 长度范围 1-64 字符。 **默认取值：** 不涉及。 

        :param actor_id: The actor_id of this ListCoreSpaceMemoriesRequest.
        :type actor_id: str
        """
        self._actor_id = actor_id

    @property
    def assistant_id(self):
        r"""Gets the assistant_id of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  按 Assistant ID 过滤，仅返回指定 Assistant 关联的记录。Assistant ID 用于标识 AI 助手。 **约束限制：**  不涉及。 **取值范围：** 长度范围 1-64 字符。 **默认取值：** 不涉及。 

        :return: The assistant_id of this ListCoreSpaceMemoriesRequest.
        :rtype: str
        """
        return self._assistant_id

    @assistant_id.setter
    def assistant_id(self, assistant_id):
        r"""Sets the assistant_id of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  按 Assistant ID 过滤，仅返回指定 Assistant 关联的记录。Assistant ID 用于标识 AI 助手。 **约束限制：**  不涉及。 **取值范围：** 长度范围 1-64 字符。 **默认取值：** 不涉及。 

        :param assistant_id: The assistant_id of this ListCoreSpaceMemoriesRequest.
        :type assistant_id: str
        """
        self._assistant_id = assistant_id

    @property
    def session_id(self):
        r"""Gets the session_id of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  按 Session ID 过滤，仅返回指定 Session 关联的记录。 **约束限制：**  不涉及。 **取值范围：** 长度36-36字符。 **默认取值：** 不涉及。 

        :return: The session_id of this ListCoreSpaceMemoriesRequest.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  按 Session ID 过滤，仅返回指定 Session 关联的记录。 **约束限制：**  不涉及。 **取值范围：** 长度36-36字符。 **默认取值：** 不涉及。 

        :param session_id: The session_id of this ListCoreSpaceMemoriesRequest.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  按创建时间过滤的起始时间（毫秒时间戳，包含），仅返回创建时间大于等于此时间的记录。 **约束限制：**  不涉及。 **取值范围：**  0-253402300799999 **默认取值：** 不涉及。 

        :return: The start_time of this ListCoreSpaceMemoriesRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  按创建时间过滤的起始时间（毫秒时间戳，包含），仅返回创建时间大于等于此时间的记录。 **约束限制：**  不涉及。 **取值范围：**  0-253402300799999 **默认取值：** 不涉及。 

        :param start_time: The start_time of this ListCoreSpaceMemoriesRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  按创建时间过滤的结束时间（毫秒时间戳，包含），仅返回创建时间小于等于此时间的记录。 **约束限制：**  不涉及。 **取值范围：**  0-253402300799999 **默认取值：** 不涉及。 

        :return: The end_time of this ListCoreSpaceMemoriesRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  按创建时间过滤的结束时间（毫秒时间戳，包含），仅返回创建时间小于等于此时间的记录。 **约束限制：**  不涉及。 **取值范围：**  0-253402300799999 **默认取值：** 不涉及。 

        :param end_time: The end_time of this ListCoreSpaceMemoriesRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  排序字段，指定按哪个字段对结果进行排序。 **约束限制：**  不涉及。 **取值范围：** created_at（按创建时间排序）根据记录的创建时间进行排序；updated_at（按更新时间排序）根据记录的最近更新时间进行排序。 **默认取值：** created_at 

        :return: The sort_by of this ListCoreSpaceMemoriesRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  排序字段，指定按哪个字段对结果进行排序。 **约束限制：**  不涉及。 **取值范围：** created_at（按创建时间排序）根据记录的创建时间进行排序；updated_at（按更新时间排序）根据记录的最近更新时间进行排序。 **默认取值：** created_at 

        :param sort_by: The sort_by of this ListCoreSpaceMemoriesRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def sort_order(self):
        r"""Gets the sort_order of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  排序方向，指定按升序还是降序排列结果。 **约束限制：**  不涉及。 **取值范围：** asc（升序）按从小到大顺序排序；desc（降序）按从大到小顺序排序。 **默认取值：** desc 

        :return: The sort_order of this ListCoreSpaceMemoriesRequest.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        r"""Sets the sort_order of this ListCoreSpaceMemoriesRequest.

        **参数解释：**  排序方向，指定按升序还是降序排列结果。 **约束限制：**  不涉及。 **取值范围：** asc（升序）按从小到大顺序排序；desc（降序）按从大到小顺序排序。 **默认取值：** desc 

        :param sort_order: The sort_order of this ListCoreSpaceMemoriesRequest.
        :type sort_order: str
        """
        self._sort_order = sort_order

    @property
    def limit(self):
        r"""Gets the limit of this ListCoreSpaceMemoriesRequest.

        **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值1000。 **默认取值：** 1000。

        :return: The limit of this ListCoreSpaceMemoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCoreSpaceMemoriesRequest.

        **参数解释：** 限制数量。 **约束限制：** 不涉及。 **取值范围：** 正整数，最大值1000。 **默认取值：** 1000。

        :param limit: The limit of this ListCoreSpaceMemoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCoreSpaceMemoriesRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :return: The offset of this ListCoreSpaceMemoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCoreSpaceMemoriesRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :param offset: The offset of this ListCoreSpaceMemoriesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListCoreSpaceMemoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
