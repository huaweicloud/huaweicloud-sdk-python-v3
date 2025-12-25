# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Message:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role': 'str',
        'content': 'str',
        'create_time': 'int',
        'name': 'object',
        'function_call': 'object',
        'tool_calls': 'object',
        'tool_call_id': 'object',
        'enable_history': 'bool',
        'intent': 'list[str]',
        'execution_id': 'str',
        'node_id': 'str',
        'agent_id': 'str',
        'rating': 'int',
        'files': 'list[object]',
        'reason': 'FeedbackReason'
    }

    attribute_map = {
        'role': 'role',
        'content': 'content',
        'create_time': 'create_time',
        'name': 'name',
        'function_call': 'function_call',
        'tool_calls': 'tool_calls',
        'tool_call_id': 'tool_call_id',
        'enable_history': 'enable_history',
        'intent': 'intent',
        'execution_id': 'execution_id',
        'node_id': 'node_id',
        'agent_id': 'agent_id',
        'rating': 'rating',
        'files': 'files',
        'reason': 'reason'
    }

    def __init__(self, role=None, content=None, create_time=None, name=None, function_call=None, tool_calls=None, tool_call_id=None, enable_history=None, intent=None, execution_id=None, node_id=None, agent_id=None, rating=None, files=None, reason=None):
        r"""Message

        The model defined in huaweicloud sdk

        :param role: 角色
        :type role: str
        :param content: 内容
        :type content: str
        :param create_time: 时间戳
        :type create_time: int
        :param name: 工具名称
        :type name: object
        :param function_call: 工具调用信息
        :type function_call: object
        :param tool_calls: 工具调用信息
        :type tool_calls: object
        :param tool_call_id: 工具调用ID信息
        :type tool_call_id: object
        :param enable_history: 是否开启会话历史
        :type enable_history: bool
        :param intent: 
        :type intent: list[str]
        :param execution_id: 对话ID
        :type execution_id: str
        :param node_id: 节点ID
        :type node_id: str
        :param agent_id: agent id
        :type agent_id: str
        :param rating: 评分，-1（点赞）、1（点踩）
        :type rating: int
        :param files: 多模态文件列表
        :type files: list[object]
        :param reason: 
        :type reason: :class:`huaweicloudsdkversatile.v1.FeedbackReason`
        """
        
        

        self._role = None
        self._content = None
        self._create_time = None
        self._name = None
        self._function_call = None
        self._tool_calls = None
        self._tool_call_id = None
        self._enable_history = None
        self._intent = None
        self._execution_id = None
        self._node_id = None
        self._agent_id = None
        self._rating = None
        self._files = None
        self._reason = None
        self.discriminator = None

        if role is not None:
            self.role = role
        if content is not None:
            self.content = content
        if create_time is not None:
            self.create_time = create_time
        if name is not None:
            self.name = name
        if function_call is not None:
            self.function_call = function_call
        if tool_calls is not None:
            self.tool_calls = tool_calls
        if tool_call_id is not None:
            self.tool_call_id = tool_call_id
        if enable_history is not None:
            self.enable_history = enable_history
        if intent is not None:
            self.intent = intent
        if execution_id is not None:
            self.execution_id = execution_id
        if node_id is not None:
            self.node_id = node_id
        if agent_id is not None:
            self.agent_id = agent_id
        if rating is not None:
            self.rating = rating
        if files is not None:
            self.files = files
        if reason is not None:
            self.reason = reason

    @property
    def role(self):
        r"""Gets the role of this Message.

        角色

        :return: The role of this Message.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this Message.

        角色

        :param role: The role of this Message.
        :type role: str
        """
        self._role = role

    @property
    def content(self):
        r"""Gets the content of this Message.

        内容

        :return: The content of this Message.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this Message.

        内容

        :param content: The content of this Message.
        :type content: str
        """
        self._content = content

    @property
    def create_time(self):
        r"""Gets the create_time of this Message.

        时间戳

        :return: The create_time of this Message.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Message.

        时间戳

        :param create_time: The create_time of this Message.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this Message.

        工具名称

        :return: The name of this Message.
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Message.

        工具名称

        :param name: The name of this Message.
        :type name: object
        """
        self._name = name

    @property
    def function_call(self):
        r"""Gets the function_call of this Message.

        工具调用信息

        :return: The function_call of this Message.
        :rtype: object
        """
        return self._function_call

    @function_call.setter
    def function_call(self, function_call):
        r"""Sets the function_call of this Message.

        工具调用信息

        :param function_call: The function_call of this Message.
        :type function_call: object
        """
        self._function_call = function_call

    @property
    def tool_calls(self):
        r"""Gets the tool_calls of this Message.

        工具调用信息

        :return: The tool_calls of this Message.
        :rtype: object
        """
        return self._tool_calls

    @tool_calls.setter
    def tool_calls(self, tool_calls):
        r"""Sets the tool_calls of this Message.

        工具调用信息

        :param tool_calls: The tool_calls of this Message.
        :type tool_calls: object
        """
        self._tool_calls = tool_calls

    @property
    def tool_call_id(self):
        r"""Gets the tool_call_id of this Message.

        工具调用ID信息

        :return: The tool_call_id of this Message.
        :rtype: object
        """
        return self._tool_call_id

    @tool_call_id.setter
    def tool_call_id(self, tool_call_id):
        r"""Sets the tool_call_id of this Message.

        工具调用ID信息

        :param tool_call_id: The tool_call_id of this Message.
        :type tool_call_id: object
        """
        self._tool_call_id = tool_call_id

    @property
    def enable_history(self):
        r"""Gets the enable_history of this Message.

        是否开启会话历史

        :return: The enable_history of this Message.
        :rtype: bool
        """
        return self._enable_history

    @enable_history.setter
    def enable_history(self, enable_history):
        r"""Sets the enable_history of this Message.

        是否开启会话历史

        :param enable_history: The enable_history of this Message.
        :type enable_history: bool
        """
        self._enable_history = enable_history

    @property
    def intent(self):
        r"""Gets the intent of this Message.

        :return: The intent of this Message.
        :rtype: list[str]
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        r"""Sets the intent of this Message.

        :param intent: The intent of this Message.
        :type intent: list[str]
        """
        self._intent = intent

    @property
    def execution_id(self):
        r"""Gets the execution_id of this Message.

        对话ID

        :return: The execution_id of this Message.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this Message.

        对话ID

        :param execution_id: The execution_id of this Message.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def node_id(self):
        r"""Gets the node_id of this Message.

        节点ID

        :return: The node_id of this Message.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this Message.

        节点ID

        :param node_id: The node_id of this Message.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def agent_id(self):
        r"""Gets the agent_id of this Message.

        agent id

        :return: The agent_id of this Message.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this Message.

        agent id

        :param agent_id: The agent_id of this Message.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def rating(self):
        r"""Gets the rating of this Message.

        评分，-1（点赞）、1（点踩）

        :return: The rating of this Message.
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        r"""Sets the rating of this Message.

        评分，-1（点赞）、1（点踩）

        :param rating: The rating of this Message.
        :type rating: int
        """
        self._rating = rating

    @property
    def files(self):
        r"""Gets the files of this Message.

        多模态文件列表

        :return: The files of this Message.
        :rtype: list[object]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this Message.

        多模态文件列表

        :param files: The files of this Message.
        :type files: list[object]
        """
        self._files = files

    @property
    def reason(self):
        r"""Gets the reason of this Message.

        :return: The reason of this Message.
        :rtype: :class:`huaweicloudsdkversatile.v1.FeedbackReason`
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this Message.

        :param reason: The reason of this Message.
        :type reason: :class:`huaweicloudsdkversatile.v1.FeedbackReason`
        """
        self._reason = reason

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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
