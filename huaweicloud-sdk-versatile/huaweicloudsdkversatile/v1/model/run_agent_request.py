# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunAgentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'conversation_id': 'str',
        'workspace_id': 'str',
        'version': 'str',
        'type': 'str',
        'stream': 'bool',
        'body': 'AgentRunReq'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'conversation_id': 'conversation_id',
        'workspace_id': 'workspace_id',
        'version': 'version',
        'type': 'type',
        'stream': 'stream',
        'body': 'body'
    }

    def __init__(self, agent_id=None, conversation_id=None, workspace_id=None, version=None, type=None, stream=None, body=None):
        r"""RunAgentRequest

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释**： 智能体ID  **取值范围**： 由英文，数字，“-”，“_”组成，不超过64位字符。
        :type agent_id: str
        :param conversation_id: **参数解释**： 会话ID，历史对话记忆功能基于同一个会话  **取值范围**： 由英文，数字，“-”，“_”组成，不超过64位字符。
        :type conversation_id: str
        :param workspace_id: **参数解释**： 空间ID，当前资源所属工作空间  **取值范围**： 由英文，数字，“-”，“_”组成，不超过64位字符。
        :type workspace_id: str
        :param version: **参数解释**： 运行的智能体/工作流的发布版本号，默认运行最新发布版本  **取值范围**： 不涉及
        :type version: str
        :param type: **参数解释**： 指定运行的智能体是单智能体还是多智能体，默认 agent  **取值范围**： agent, controller
        :type type: str
        :param stream: **参数解释**： 是否流式响应  **取值范围**： true,false（不传默认 true，支持流式）
        :type stream: bool
        :param body: Body of the RunAgentRequest
        :type body: :class:`huaweicloudsdkversatile.v1.AgentRunReq`
        """
        
        

        self._agent_id = None
        self._conversation_id = None
        self._workspace_id = None
        self._version = None
        self._type = None
        self._stream = None
        self._body = None
        self.discriminator = None

        self.agent_id = agent_id
        self.conversation_id = conversation_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if version is not None:
            self.version = version
        if type is not None:
            self.type = type
        if stream is not None:
            self.stream = stream
        if body is not None:
            self.body = body

    @property
    def agent_id(self):
        r"""Gets the agent_id of this RunAgentRequest.

        **参数解释**： 智能体ID  **取值范围**： 由英文，数字，“-”，“_”组成，不超过64位字符。

        :return: The agent_id of this RunAgentRequest.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this RunAgentRequest.

        **参数解释**： 智能体ID  **取值范围**： 由英文，数字，“-”，“_”组成，不超过64位字符。

        :param agent_id: The agent_id of this RunAgentRequest.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def conversation_id(self):
        r"""Gets the conversation_id of this RunAgentRequest.

        **参数解释**： 会话ID，历史对话记忆功能基于同一个会话  **取值范围**： 由英文，数字，“-”，“_”组成，不超过64位字符。

        :return: The conversation_id of this RunAgentRequest.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        r"""Sets the conversation_id of this RunAgentRequest.

        **参数解释**： 会话ID，历史对话记忆功能基于同一个会话  **取值范围**： 由英文，数字，“-”，“_”组成，不超过64位字符。

        :param conversation_id: The conversation_id of this RunAgentRequest.
        :type conversation_id: str
        """
        self._conversation_id = conversation_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this RunAgentRequest.

        **参数解释**： 空间ID，当前资源所属工作空间  **取值范围**： 由英文，数字，“-”，“_”组成，不超过64位字符。

        :return: The workspace_id of this RunAgentRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this RunAgentRequest.

        **参数解释**： 空间ID，当前资源所属工作空间  **取值范围**： 由英文，数字，“-”，“_”组成，不超过64位字符。

        :param workspace_id: The workspace_id of this RunAgentRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def version(self):
        r"""Gets the version of this RunAgentRequest.

        **参数解释**： 运行的智能体/工作流的发布版本号，默认运行最新发布版本  **取值范围**： 不涉及

        :return: The version of this RunAgentRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this RunAgentRequest.

        **参数解释**： 运行的智能体/工作流的发布版本号，默认运行最新发布版本  **取值范围**： 不涉及

        :param version: The version of this RunAgentRequest.
        :type version: str
        """
        self._version = version

    @property
    def type(self):
        r"""Gets the type of this RunAgentRequest.

        **参数解释**： 指定运行的智能体是单智能体还是多智能体，默认 agent  **取值范围**： agent, controller

        :return: The type of this RunAgentRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RunAgentRequest.

        **参数解释**： 指定运行的智能体是单智能体还是多智能体，默认 agent  **取值范围**： agent, controller

        :param type: The type of this RunAgentRequest.
        :type type: str
        """
        self._type = type

    @property
    def stream(self):
        r"""Gets the stream of this RunAgentRequest.

        **参数解释**： 是否流式响应  **取值范围**： true,false（不传默认 true，支持流式）

        :return: The stream of this RunAgentRequest.
        :rtype: bool
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this RunAgentRequest.

        **参数解释**： 是否流式响应  **取值范围**： true,false（不传默认 true，支持流式）

        :param stream: The stream of this RunAgentRequest.
        :type stream: bool
        """
        self._stream = stream

    @property
    def body(self):
        r"""Gets the body of this RunAgentRequest.

        :return: The body of this RunAgentRequest.
        :rtype: :class:`huaweicloudsdkversatile.v1.AgentRunReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this RunAgentRequest.

        :param body: The body of this RunAgentRequest.
        :type body: :class:`huaweicloudsdkversatile.v1.AgentRunReq`
        """
        self._body = body

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
        if not isinstance(other, RunAgentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
