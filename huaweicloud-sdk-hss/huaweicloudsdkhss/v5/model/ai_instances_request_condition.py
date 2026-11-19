# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiInstancesRequestCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_name': 'str',
        'detect_time': 'int',
        'security_risk_num': 'int',
        'free_health_check_total_host_num': 'int',
        'agent_id': 'str',
        'agent_id_list': 'list[str]',
        'runtime_name': 'str',
        'runtime_id': 'str',
        'image_url': 'str',
        'sdk_status': 'str',
        'exist_risk_trace': 'bool',
        'exist_risk_runtime': 'bool',
        'source': 'str',
        'agent_type': 'str'
    }

    attribute_map = {
        'agent_name': 'agent_name',
        'detect_time': 'detect_time',
        'security_risk_num': 'security_risk_num',
        'free_health_check_total_host_num': 'free_health_check_total_host_num',
        'agent_id': 'agent_id',
        'agent_id_list': 'agent_id_list',
        'runtime_name': 'runtime_name',
        'runtime_id': 'runtime_id',
        'image_url': 'image_url',
        'sdk_status': 'sdk_status',
        'exist_risk_trace': 'exist_risk_trace',
        'exist_risk_runtime': 'exist_risk_runtime',
        'source': 'source',
        'agent_type': 'agent_type'
    }

    def __init__(self, agent_name=None, detect_time=None, security_risk_num=None, free_health_check_total_host_num=None, agent_id=None, agent_id_list=None, runtime_name=None, runtime_id=None, image_url=None, sdk_status=None, exist_risk_trace=None, exist_risk_runtime=None, source=None, agent_type=None):
        r"""AiInstancesRequestCondition

        The model defined in huaweicloud sdk

        :param agent_name: 
        :type agent_name: str
        :param detect_time: **参数解释**： 最近检测时间 **取值范围**： 不涉及 
        :type detect_time: int
        :param security_risk_num: **参数解释**： 风险总数 **取值范围**： 最小值0，最大值2147483647 
        :type security_risk_num: int
        :param free_health_check_total_host_num: **参数解释**： 免费体检的服务器总数 **取值范围**： 最小值0，最大值2147483647 
        :type free_health_check_total_host_num: int
        :param agent_id: **参数解释**： 智能体ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 
        :type agent_id: str
        :param agent_id_list: **参数解释**： 智能体ID列表，支持批量查询 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type agent_id_list: list[str]
        :param runtime_name: **参数解释**： 智能体运行时名字 **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 
        :type runtime_name: str
        :param runtime_id: **参数解释**： 智能体运行时ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 
        :type runtime_id: str
        :param image_url: **参数解释**： 运行镜像地址 **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 
        :type image_url: str
        :param sdk_status: **参数解释**： SDK检测状态 **约束限制**： 不涉及 **取值范围**： - open：开启 - close：关闭  **默认取值**： 不涉及 
        :type sdk_status: str
        :param exist_risk_trace: **参数解释**： 是否存在行为轨迹检测 **约束限制**： 不涉及 **取值范围**： - true：存在 - false：不存在  **默认取值**： 不涉及 
        :type exist_risk_trace: bool
        :param exist_risk_runtime: **参数解释**： 是否存在运行时检测 **约束限制**： 不涉及 **取值范围**： - true：存在 - false：不存在  **默认取值**： 不涉及 
        :type exist_risk_runtime: bool
        :param source: **参数解释**： 智能体的来源 **约束限制**： 不涉及 **取值范围**： - AgentArts：AgentArts系统。 - OfficeClaw：OfficeClaw系统。 - OpenClaw：OpenClaw系统。  **默认取值**： 不涉及 
        :type source: str
        :param agent_type: **参数解释**： 智能体类型 **约束限制**： 不涉及 **取值范围**： - agent：单智能体。 - chat：工作流。 - controller：多智能体。 - teamAgent：团队智能体。  **默认取值**： 不涉及 
        :type agent_type: str
        """
        
        

        self._agent_name = None
        self._detect_time = None
        self._security_risk_num = None
        self._free_health_check_total_host_num = None
        self._agent_id = None
        self._agent_id_list = None
        self._runtime_name = None
        self._runtime_id = None
        self._image_url = None
        self._sdk_status = None
        self._exist_risk_trace = None
        self._exist_risk_runtime = None
        self._source = None
        self._agent_type = None
        self.discriminator = None

        if agent_name is not None:
            self.agent_name = agent_name
        if detect_time is not None:
            self.detect_time = detect_time
        if security_risk_num is not None:
            self.security_risk_num = security_risk_num
        if free_health_check_total_host_num is not None:
            self.free_health_check_total_host_num = free_health_check_total_host_num
        if agent_id is not None:
            self.agent_id = agent_id
        if agent_id_list is not None:
            self.agent_id_list = agent_id_list
        if runtime_name is not None:
            self.runtime_name = runtime_name
        if runtime_id is not None:
            self.runtime_id = runtime_id
        if image_url is not None:
            self.image_url = image_url
        if sdk_status is not None:
            self.sdk_status = sdk_status
        if exist_risk_trace is not None:
            self.exist_risk_trace = exist_risk_trace
        if exist_risk_runtime is not None:
            self.exist_risk_runtime = exist_risk_runtime
        if source is not None:
            self.source = source
        if agent_type is not None:
            self.agent_type = agent_type

    @property
    def agent_name(self):
        r"""Gets the agent_name of this AiInstancesRequestCondition.

        

        :return: The agent_name of this AiInstancesRequestCondition.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        r"""Sets the agent_name of this AiInstancesRequestCondition.

        

        :param agent_name: The agent_name of this AiInstancesRequestCondition.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def detect_time(self):
        r"""Gets the detect_time of this AiInstancesRequestCondition.

        **参数解释**： 最近检测时间 **取值范围**： 不涉及 

        :return: The detect_time of this AiInstancesRequestCondition.
        :rtype: int
        """
        return self._detect_time

    @detect_time.setter
    def detect_time(self, detect_time):
        r"""Sets the detect_time of this AiInstancesRequestCondition.

        **参数解释**： 最近检测时间 **取值范围**： 不涉及 

        :param detect_time: The detect_time of this AiInstancesRequestCondition.
        :type detect_time: int
        """
        self._detect_time = detect_time

    @property
    def security_risk_num(self):
        r"""Gets the security_risk_num of this AiInstancesRequestCondition.

        **参数解释**： 风险总数 **取值范围**： 最小值0，最大值2147483647 

        :return: The security_risk_num of this AiInstancesRequestCondition.
        :rtype: int
        """
        return self._security_risk_num

    @security_risk_num.setter
    def security_risk_num(self, security_risk_num):
        r"""Sets the security_risk_num of this AiInstancesRequestCondition.

        **参数解释**： 风险总数 **取值范围**： 最小值0，最大值2147483647 

        :param security_risk_num: The security_risk_num of this AiInstancesRequestCondition.
        :type security_risk_num: int
        """
        self._security_risk_num = security_risk_num

    @property
    def free_health_check_total_host_num(self):
        r"""Gets the free_health_check_total_host_num of this AiInstancesRequestCondition.

        **参数解释**： 免费体检的服务器总数 **取值范围**： 最小值0，最大值2147483647 

        :return: The free_health_check_total_host_num of this AiInstancesRequestCondition.
        :rtype: int
        """
        return self._free_health_check_total_host_num

    @free_health_check_total_host_num.setter
    def free_health_check_total_host_num(self, free_health_check_total_host_num):
        r"""Sets the free_health_check_total_host_num of this AiInstancesRequestCondition.

        **参数解释**： 免费体检的服务器总数 **取值范围**： 最小值0，最大值2147483647 

        :param free_health_check_total_host_num: The free_health_check_total_host_num of this AiInstancesRequestCondition.
        :type free_health_check_total_host_num: int
        """
        self._free_health_check_total_host_num = free_health_check_total_host_num

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AiInstancesRequestCondition.

        **参数解释**： 智能体ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :return: The agent_id of this AiInstancesRequestCondition.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AiInstancesRequestCondition.

        **参数解释**： 智能体ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :param agent_id: The agent_id of this AiInstancesRequestCondition.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_id_list(self):
        r"""Gets the agent_id_list of this AiInstancesRequestCondition.

        **参数解释**： 智能体ID列表，支持批量查询 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The agent_id_list of this AiInstancesRequestCondition.
        :rtype: list[str]
        """
        return self._agent_id_list

    @agent_id_list.setter
    def agent_id_list(self, agent_id_list):
        r"""Sets the agent_id_list of this AiInstancesRequestCondition.

        **参数解释**： 智能体ID列表，支持批量查询 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param agent_id_list: The agent_id_list of this AiInstancesRequestCondition.
        :type agent_id_list: list[str]
        """
        self._agent_id_list = agent_id_list

    @property
    def runtime_name(self):
        r"""Gets the runtime_name of this AiInstancesRequestCondition.

        **参数解释**： 智能体运行时名字 **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :return: The runtime_name of this AiInstancesRequestCondition.
        :rtype: str
        """
        return self._runtime_name

    @runtime_name.setter
    def runtime_name(self, runtime_name):
        r"""Sets the runtime_name of this AiInstancesRequestCondition.

        **参数解释**： 智能体运行时名字 **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :param runtime_name: The runtime_name of this AiInstancesRequestCondition.
        :type runtime_name: str
        """
        self._runtime_name = runtime_name

    @property
    def runtime_id(self):
        r"""Gets the runtime_id of this AiInstancesRequestCondition.

        **参数解释**： 智能体运行时ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :return: The runtime_id of this AiInstancesRequestCondition.
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        r"""Sets the runtime_id of this AiInstancesRequestCondition.

        **参数解释**： 智能体运行时ID **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :param runtime_id: The runtime_id of this AiInstancesRequestCondition.
        :type runtime_id: str
        """
        self._runtime_id = runtime_id

    @property
    def image_url(self):
        r"""Gets the image_url of this AiInstancesRequestCondition.

        **参数解释**： 运行镜像地址 **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :return: The image_url of this AiInstancesRequestCondition.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this AiInstancesRequestCondition.

        **参数解释**： 运行镜像地址 **约束限制**： 不涉及 **取值范围**： 字符长度为1-128位 **默认取值**： 不涉及 

        :param image_url: The image_url of this AiInstancesRequestCondition.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def sdk_status(self):
        r"""Gets the sdk_status of this AiInstancesRequestCondition.

        **参数解释**： SDK检测状态 **约束限制**： 不涉及 **取值范围**： - open：开启 - close：关闭  **默认取值**： 不涉及 

        :return: The sdk_status of this AiInstancesRequestCondition.
        :rtype: str
        """
        return self._sdk_status

    @sdk_status.setter
    def sdk_status(self, sdk_status):
        r"""Sets the sdk_status of this AiInstancesRequestCondition.

        **参数解释**： SDK检测状态 **约束限制**： 不涉及 **取值范围**： - open：开启 - close：关闭  **默认取值**： 不涉及 

        :param sdk_status: The sdk_status of this AiInstancesRequestCondition.
        :type sdk_status: str
        """
        self._sdk_status = sdk_status

    @property
    def exist_risk_trace(self):
        r"""Gets the exist_risk_trace of this AiInstancesRequestCondition.

        **参数解释**： 是否存在行为轨迹检测 **约束限制**： 不涉及 **取值范围**： - true：存在 - false：不存在  **默认取值**： 不涉及 

        :return: The exist_risk_trace of this AiInstancesRequestCondition.
        :rtype: bool
        """
        return self._exist_risk_trace

    @exist_risk_trace.setter
    def exist_risk_trace(self, exist_risk_trace):
        r"""Sets the exist_risk_trace of this AiInstancesRequestCondition.

        **参数解释**： 是否存在行为轨迹检测 **约束限制**： 不涉及 **取值范围**： - true：存在 - false：不存在  **默认取值**： 不涉及 

        :param exist_risk_trace: The exist_risk_trace of this AiInstancesRequestCondition.
        :type exist_risk_trace: bool
        """
        self._exist_risk_trace = exist_risk_trace

    @property
    def exist_risk_runtime(self):
        r"""Gets the exist_risk_runtime of this AiInstancesRequestCondition.

        **参数解释**： 是否存在运行时检测 **约束限制**： 不涉及 **取值范围**： - true：存在 - false：不存在  **默认取值**： 不涉及 

        :return: The exist_risk_runtime of this AiInstancesRequestCondition.
        :rtype: bool
        """
        return self._exist_risk_runtime

    @exist_risk_runtime.setter
    def exist_risk_runtime(self, exist_risk_runtime):
        r"""Sets the exist_risk_runtime of this AiInstancesRequestCondition.

        **参数解释**： 是否存在运行时检测 **约束限制**： 不涉及 **取值范围**： - true：存在 - false：不存在  **默认取值**： 不涉及 

        :param exist_risk_runtime: The exist_risk_runtime of this AiInstancesRequestCondition.
        :type exist_risk_runtime: bool
        """
        self._exist_risk_runtime = exist_risk_runtime

    @property
    def source(self):
        r"""Gets the source of this AiInstancesRequestCondition.

        **参数解释**： 智能体的来源 **约束限制**： 不涉及 **取值范围**： - AgentArts：AgentArts系统。 - OfficeClaw：OfficeClaw系统。 - OpenClaw：OpenClaw系统。  **默认取值**： 不涉及 

        :return: The source of this AiInstancesRequestCondition.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this AiInstancesRequestCondition.

        **参数解释**： 智能体的来源 **约束限制**： 不涉及 **取值范围**： - AgentArts：AgentArts系统。 - OfficeClaw：OfficeClaw系统。 - OpenClaw：OpenClaw系统。  **默认取值**： 不涉及 

        :param source: The source of this AiInstancesRequestCondition.
        :type source: str
        """
        self._source = source

    @property
    def agent_type(self):
        r"""Gets the agent_type of this AiInstancesRequestCondition.

        **参数解释**： 智能体类型 **约束限制**： 不涉及 **取值范围**： - agent：单智能体。 - chat：工作流。 - controller：多智能体。 - teamAgent：团队智能体。  **默认取值**： 不涉及 

        :return: The agent_type of this AiInstancesRequestCondition.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this AiInstancesRequestCondition.

        **参数解释**： 智能体类型 **约束限制**： 不涉及 **取值范围**： - agent：单智能体。 - chat：工作流。 - controller：多智能体。 - teamAgent：团队智能体。  **默认取值**： 不涉及 

        :param agent_type: The agent_type of this AiInstancesRequestCondition.
        :type agent_type: str
        """
        self._agent_type = agent_type

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
        if not isinstance(other, AiInstancesRequestCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
