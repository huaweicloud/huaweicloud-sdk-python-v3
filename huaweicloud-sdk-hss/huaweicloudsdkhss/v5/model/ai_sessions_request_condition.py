# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiSessionsRequestCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'agent_name': 'str',
        'agent_id': 'str',
        'runtime_name': 'str',
        'runtime_id': 'str',
        'sdk_status': 'str',
        'source': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'agent_name': 'agent_name',
        'agent_id': 'agent_id',
        'runtime_name': 'runtime_name',
        'runtime_id': 'runtime_id',
        'sdk_status': 'sdk_status',
        'source': 'source'
    }

    def __init__(self, session_id=None, agent_name=None, agent_id=None, runtime_name=None, runtime_id=None, sdk_status=None, source=None):
        r"""AiSessionsRequestCondition

        The model defined in huaweicloud sdk

        :param session_id: **参数解释**： 会话ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 
        :type session_id: str
        :param agent_name: **参数解释**： 智能体名字 **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 
        :type agent_name: str
        :param agent_id: **参数解释**： 智能体ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 
        :type agent_id: str
        :param runtime_name: **参数解释**： 智能体运行时名字 **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 
        :type runtime_name: str
        :param runtime_id: **参数解释**： 智能体运行时ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 
        :type runtime_id: str
        :param sdk_status: **参数解释**： SDK检测状态 **约束限制**： 不涉及 **取值范围**： - open：开启 - close：关闭  **默认取值**： 不涉及 
        :type sdk_status: str
        :param source: **参数解释**： 智能体的来源 **约束限制**： 不涉及 **取值范围**： - AgentArts：AgentArts。 - OfficeClaw：OfficeClaw。  **默认取值**： 不涉及 
        :type source: str
        """
        
        

        self._session_id = None
        self._agent_name = None
        self._agent_id = None
        self._runtime_name = None
        self._runtime_id = None
        self._sdk_status = None
        self._source = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if agent_name is not None:
            self.agent_name = agent_name
        if agent_id is not None:
            self.agent_id = agent_id
        if runtime_name is not None:
            self.runtime_name = runtime_name
        if runtime_id is not None:
            self.runtime_id = runtime_id
        if sdk_status is not None:
            self.sdk_status = sdk_status
        if source is not None:
            self.source = source

    @property
    def session_id(self):
        r"""Gets the session_id of this AiSessionsRequestCondition.

        **参数解释**： 会话ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :return: The session_id of this AiSessionsRequestCondition.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this AiSessionsRequestCondition.

        **参数解释**： 会话ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :param session_id: The session_id of this AiSessionsRequestCondition.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def agent_name(self):
        r"""Gets the agent_name of this AiSessionsRequestCondition.

        **参数解释**： 智能体名字 **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :return: The agent_name of this AiSessionsRequestCondition.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        r"""Sets the agent_name of this AiSessionsRequestCondition.

        **参数解释**： 智能体名字 **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :param agent_name: The agent_name of this AiSessionsRequestCondition.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AiSessionsRequestCondition.

        **参数解释**： 智能体ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :return: The agent_id of this AiSessionsRequestCondition.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AiSessionsRequestCondition.

        **参数解释**： 智能体ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :param agent_id: The agent_id of this AiSessionsRequestCondition.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def runtime_name(self):
        r"""Gets the runtime_name of this AiSessionsRequestCondition.

        **参数解释**： 智能体运行时名字 **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :return: The runtime_name of this AiSessionsRequestCondition.
        :rtype: str
        """
        return self._runtime_name

    @runtime_name.setter
    def runtime_name(self, runtime_name):
        r"""Sets the runtime_name of this AiSessionsRequestCondition.

        **参数解释**： 智能体运行时名字 **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :param runtime_name: The runtime_name of this AiSessionsRequestCondition.
        :type runtime_name: str
        """
        self._runtime_name = runtime_name

    @property
    def runtime_id(self):
        r"""Gets the runtime_id of this AiSessionsRequestCondition.

        **参数解释**： 智能体运行时ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :return: The runtime_id of this AiSessionsRequestCondition.
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        r"""Sets the runtime_id of this AiSessionsRequestCondition.

        **参数解释**： 智能体运行时ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :param runtime_id: The runtime_id of this AiSessionsRequestCondition.
        :type runtime_id: str
        """
        self._runtime_id = runtime_id

    @property
    def sdk_status(self):
        r"""Gets the sdk_status of this AiSessionsRequestCondition.

        **参数解释**： SDK检测状态 **约束限制**： 不涉及 **取值范围**： - open：开启 - close：关闭  **默认取值**： 不涉及 

        :return: The sdk_status of this AiSessionsRequestCondition.
        :rtype: str
        """
        return self._sdk_status

    @sdk_status.setter
    def sdk_status(self, sdk_status):
        r"""Sets the sdk_status of this AiSessionsRequestCondition.

        **参数解释**： SDK检测状态 **约束限制**： 不涉及 **取值范围**： - open：开启 - close：关闭  **默认取值**： 不涉及 

        :param sdk_status: The sdk_status of this AiSessionsRequestCondition.
        :type sdk_status: str
        """
        self._sdk_status = sdk_status

    @property
    def source(self):
        r"""Gets the source of this AiSessionsRequestCondition.

        **参数解释**： 智能体的来源 **约束限制**： 不涉及 **取值范围**： - AgentArts：AgentArts。 - OfficeClaw：OfficeClaw。  **默认取值**： 不涉及 

        :return: The source of this AiSessionsRequestCondition.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this AiSessionsRequestCondition.

        **参数解释**： 智能体的来源 **约束限制**： 不涉及 **取值范围**： - AgentArts：AgentArts。 - OfficeClaw：OfficeClaw。  **默认取值**： 不涉及 

        :param source: The source of this AiSessionsRequestCondition.
        :type source: str
        """
        self._source = source

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
        if not isinstance(other, AiSessionsRequestCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
