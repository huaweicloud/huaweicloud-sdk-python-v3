# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiSessionsResponseBodyData:

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
        'image_url': 'str',
        'sdk_status': 'str',
        'start_time': 'int',
        'last_chat_time': 'int',
        'run_duration': 'int',
        'security_tokens': 'int',
        'source': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'agent_name': 'agent_name',
        'agent_id': 'agent_id',
        'runtime_name': 'runtime_name',
        'runtime_id': 'runtime_id',
        'image_url': 'image_url',
        'sdk_status': 'sdk_status',
        'start_time': 'start_time',
        'last_chat_time': 'last_chat_time',
        'run_duration': 'run_duration',
        'security_tokens': 'security_tokens',
        'source': 'source'
    }

    def __init__(self, session_id=None, agent_name=None, agent_id=None, runtime_name=None, runtime_id=None, image_url=None, sdk_status=None, start_time=None, last_chat_time=None, run_duration=None, security_tokens=None, source=None):
        r"""ListAiSessionsResponseBodyData

        The model defined in huaweicloud sdk

        :param session_id: **参数解释**： 会话ID **取值范围**： 字符长度为1-128位 
        :type session_id: str
        :param agent_name: **参数解释**： 智能体名字 **取值范围**： 字符长度为1-128位 
        :type agent_name: str
        :param agent_id: **参数解释**： 智能体ID **取值范围**： 字符长度为1-128位 
        :type agent_id: str
        :param runtime_name: **参数解释**： 智能体运行时名字 **取值范围**： 字符长度为1-128位 
        :type runtime_name: str
        :param runtime_id: **参数解释**： 智能体运行时ID **取值范围**： 字符长度为1-128位 
        :type runtime_id: str
        :param image_url: **参数解释**： 运行镜像地址 **取值范围**： 字符长度为1-128位 
        :type image_url: str
        :param sdk_status: **参数解释**： SDK检测状态 **取值范围**： - open：开启 - close：关闭 
        :type sdk_status: str
        :param start_time: **参数解释**： 会话开启时间，毫秒时间戳 **取值范围**： 0~9223372036854775807 
        :type start_time: int
        :param last_chat_time: **参数解释**： 会话上次对话时间，毫秒时间戳 **取值范围**： 0~9223372036854775807 
        :type last_chat_time: int
        :param run_duration: **参数解释**： 会话运行时长，单位为秒 **取值范围**： 0~2147483647 
        :type run_duration: int
        :param security_tokens: **参数解释**： 消耗的token数量 **取值范围**： 0~2147483647 
        :type security_tokens: int
        :param source: **参数解释**： 智能体的来源 **取值范围**： - AgentArts - OfficeClaw 
        :type source: str
        """
        
        

        self._session_id = None
        self._agent_name = None
        self._agent_id = None
        self._runtime_name = None
        self._runtime_id = None
        self._image_url = None
        self._sdk_status = None
        self._start_time = None
        self._last_chat_time = None
        self._run_duration = None
        self._security_tokens = None
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
        if image_url is not None:
            self.image_url = image_url
        if sdk_status is not None:
            self.sdk_status = sdk_status
        if start_time is not None:
            self.start_time = start_time
        if last_chat_time is not None:
            self.last_chat_time = last_chat_time
        if run_duration is not None:
            self.run_duration = run_duration
        if security_tokens is not None:
            self.security_tokens = security_tokens
        if source is not None:
            self.source = source

    @property
    def session_id(self):
        r"""Gets the session_id of this ListAiSessionsResponseBodyData.

        **参数解释**： 会话ID **取值范围**： 字符长度为1-128位 

        :return: The session_id of this ListAiSessionsResponseBodyData.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this ListAiSessionsResponseBodyData.

        **参数解释**： 会话ID **取值范围**： 字符长度为1-128位 

        :param session_id: The session_id of this ListAiSessionsResponseBodyData.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def agent_name(self):
        r"""Gets the agent_name of this ListAiSessionsResponseBodyData.

        **参数解释**： 智能体名字 **取值范围**： 字符长度为1-128位 

        :return: The agent_name of this ListAiSessionsResponseBodyData.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        r"""Sets the agent_name of this ListAiSessionsResponseBodyData.

        **参数解释**： 智能体名字 **取值范围**： 字符长度为1-128位 

        :param agent_name: The agent_name of this ListAiSessionsResponseBodyData.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ListAiSessionsResponseBodyData.

        **参数解释**： 智能体ID **取值范围**： 字符长度为1-128位 

        :return: The agent_id of this ListAiSessionsResponseBodyData.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ListAiSessionsResponseBodyData.

        **参数解释**： 智能体ID **取值范围**： 字符长度为1-128位 

        :param agent_id: The agent_id of this ListAiSessionsResponseBodyData.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def runtime_name(self):
        r"""Gets the runtime_name of this ListAiSessionsResponseBodyData.

        **参数解释**： 智能体运行时名字 **取值范围**： 字符长度为1-128位 

        :return: The runtime_name of this ListAiSessionsResponseBodyData.
        :rtype: str
        """
        return self._runtime_name

    @runtime_name.setter
    def runtime_name(self, runtime_name):
        r"""Sets the runtime_name of this ListAiSessionsResponseBodyData.

        **参数解释**： 智能体运行时名字 **取值范围**： 字符长度为1-128位 

        :param runtime_name: The runtime_name of this ListAiSessionsResponseBodyData.
        :type runtime_name: str
        """
        self._runtime_name = runtime_name

    @property
    def runtime_id(self):
        r"""Gets the runtime_id of this ListAiSessionsResponseBodyData.

        **参数解释**： 智能体运行时ID **取值范围**： 字符长度为1-128位 

        :return: The runtime_id of this ListAiSessionsResponseBodyData.
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        r"""Sets the runtime_id of this ListAiSessionsResponseBodyData.

        **参数解释**： 智能体运行时ID **取值范围**： 字符长度为1-128位 

        :param runtime_id: The runtime_id of this ListAiSessionsResponseBodyData.
        :type runtime_id: str
        """
        self._runtime_id = runtime_id

    @property
    def image_url(self):
        r"""Gets the image_url of this ListAiSessionsResponseBodyData.

        **参数解释**： 运行镜像地址 **取值范围**： 字符长度为1-128位 

        :return: The image_url of this ListAiSessionsResponseBodyData.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this ListAiSessionsResponseBodyData.

        **参数解释**： 运行镜像地址 **取值范围**： 字符长度为1-128位 

        :param image_url: The image_url of this ListAiSessionsResponseBodyData.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def sdk_status(self):
        r"""Gets the sdk_status of this ListAiSessionsResponseBodyData.

        **参数解释**： SDK检测状态 **取值范围**： - open：开启 - close：关闭 

        :return: The sdk_status of this ListAiSessionsResponseBodyData.
        :rtype: str
        """
        return self._sdk_status

    @sdk_status.setter
    def sdk_status(self, sdk_status):
        r"""Sets the sdk_status of this ListAiSessionsResponseBodyData.

        **参数解释**： SDK检测状态 **取值范围**： - open：开启 - close：关闭 

        :param sdk_status: The sdk_status of this ListAiSessionsResponseBodyData.
        :type sdk_status: str
        """
        self._sdk_status = sdk_status

    @property
    def start_time(self):
        r"""Gets the start_time of this ListAiSessionsResponseBodyData.

        **参数解释**： 会话开启时间，毫秒时间戳 **取值范围**： 0~9223372036854775807 

        :return: The start_time of this ListAiSessionsResponseBodyData.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListAiSessionsResponseBodyData.

        **参数解释**： 会话开启时间，毫秒时间戳 **取值范围**： 0~9223372036854775807 

        :param start_time: The start_time of this ListAiSessionsResponseBodyData.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def last_chat_time(self):
        r"""Gets the last_chat_time of this ListAiSessionsResponseBodyData.

        **参数解释**： 会话上次对话时间，毫秒时间戳 **取值范围**： 0~9223372036854775807 

        :return: The last_chat_time of this ListAiSessionsResponseBodyData.
        :rtype: int
        """
        return self._last_chat_time

    @last_chat_time.setter
    def last_chat_time(self, last_chat_time):
        r"""Sets the last_chat_time of this ListAiSessionsResponseBodyData.

        **参数解释**： 会话上次对话时间，毫秒时间戳 **取值范围**： 0~9223372036854775807 

        :param last_chat_time: The last_chat_time of this ListAiSessionsResponseBodyData.
        :type last_chat_time: int
        """
        self._last_chat_time = last_chat_time

    @property
    def run_duration(self):
        r"""Gets the run_duration of this ListAiSessionsResponseBodyData.

        **参数解释**： 会话运行时长，单位为秒 **取值范围**： 0~2147483647 

        :return: The run_duration of this ListAiSessionsResponseBodyData.
        :rtype: int
        """
        return self._run_duration

    @run_duration.setter
    def run_duration(self, run_duration):
        r"""Sets the run_duration of this ListAiSessionsResponseBodyData.

        **参数解释**： 会话运行时长，单位为秒 **取值范围**： 0~2147483647 

        :param run_duration: The run_duration of this ListAiSessionsResponseBodyData.
        :type run_duration: int
        """
        self._run_duration = run_duration

    @property
    def security_tokens(self):
        r"""Gets the security_tokens of this ListAiSessionsResponseBodyData.

        **参数解释**： 消耗的token数量 **取值范围**： 0~2147483647 

        :return: The security_tokens of this ListAiSessionsResponseBodyData.
        :rtype: int
        """
        return self._security_tokens

    @security_tokens.setter
    def security_tokens(self, security_tokens):
        r"""Sets the security_tokens of this ListAiSessionsResponseBodyData.

        **参数解释**： 消耗的token数量 **取值范围**： 0~2147483647 

        :param security_tokens: The security_tokens of this ListAiSessionsResponseBodyData.
        :type security_tokens: int
        """
        self._security_tokens = security_tokens

    @property
    def source(self):
        r"""Gets the source of this ListAiSessionsResponseBodyData.

        **参数解释**： 智能体的来源 **取值范围**： - AgentArts - OfficeClaw 

        :return: The source of this ListAiSessionsResponseBodyData.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ListAiSessionsResponseBodyData.

        **参数解释**： 智能体的来源 **取值范围**： - AgentArts - OfficeClaw 

        :param source: The source of this ListAiSessionsResponseBodyData.
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
        if not isinstance(other, ListAiSessionsResponseBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
