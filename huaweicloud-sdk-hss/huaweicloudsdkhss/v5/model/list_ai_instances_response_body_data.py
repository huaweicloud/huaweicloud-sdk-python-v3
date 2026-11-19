# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiInstancesResponseBodyData:

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
        'agent_id': 'str',
        'runtime_name': 'str',
        'runtime_id': 'str',
        'sdk_status': 'str',
        'source': 'str',
        'agent_type': 'str',
        'session_number': 'int',
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'image_url': 'str',
        'instance_create_time': 'int',
        'instance_update_time': 'int',
        'trace_alarm_number': 'int',
        'runtime_alarm_number': 'int',
        'policy_group_type': 'int',
        'policy_info_list': 'list[AiAgentPolicy]',
        'agent_runtime_env': 'str',
        'cluster_id': 'str',
        'cluster_type': 'str',
        'cluster_name': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'host_status': 'str',
        'host_id': 'str',
        'os_type': 'str',
        'os_name': 'str',
        'os_version': 'str',
        'kernel_version': 'str',
        'agent_status': 'str',
        'defender_status': 'str',
        'container_id': 'str'
    }

    attribute_map = {
        'agent_name': 'agent_name',
        'agent_id': 'agent_id',
        'runtime_name': 'runtime_name',
        'runtime_id': 'runtime_id',
        'sdk_status': 'sdk_status',
        'source': 'source',
        'agent_type': 'agent_type',
        'session_number': 'session_number',
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'image_url': 'image_url',
        'instance_create_time': 'instance_create_time',
        'instance_update_time': 'instance_update_time',
        'trace_alarm_number': 'trace_alarm_number',
        'runtime_alarm_number': 'runtime_alarm_number',
        'policy_group_type': 'policy_group_type',
        'policy_info_list': 'policy_info_list',
        'agent_runtime_env': 'agent_runtime_env',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'cluster_name': 'cluster_name',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'host_status': 'host_status',
        'host_id': 'host_id',
        'os_type': 'os_type',
        'os_name': 'os_name',
        'os_version': 'os_version',
        'kernel_version': 'kernel_version',
        'agent_status': 'agent_status',
        'defender_status': 'defender_status',
        'container_id': 'container_id'
    }

    def __init__(self, agent_name=None, agent_id=None, runtime_name=None, runtime_id=None, sdk_status=None, source=None, agent_type=None, session_number=None, project_id=None, enterprise_project_id=None, image_url=None, instance_create_time=None, instance_update_time=None, trace_alarm_number=None, runtime_alarm_number=None, policy_group_type=None, policy_info_list=None, agent_runtime_env=None, cluster_id=None, cluster_type=None, cluster_name=None, host_name=None, public_ip=None, private_ip=None, host_status=None, host_id=None, os_type=None, os_name=None, os_version=None, kernel_version=None, agent_status=None, defender_status=None, container_id=None):
        r"""ListAiInstancesResponseBodyData

        The model defined in huaweicloud sdk

        :param agent_name: **参数解释**： 智能体名字 **取值范围**： 字符长度为1-128位 
        :type agent_name: str
        :param agent_id: **参数解释**： 智能体ID **取值范围**： 字符长度为1-128位 
        :type agent_id: str
        :param runtime_name: **参数解释**： 智能体运行时名字 **取值范围**： 字符长度为1-128位 
        :type runtime_name: str
        :param runtime_id: **参数解释**： 智能体运行时ID **取值范围**： 字符长度为1-128位 
        :type runtime_id: str
        :param sdk_status: **参数解释**： SDK检测状态 **取值范围**： - open：开启 - close：关闭 
        :type sdk_status: str
        :param source: **参数解释**： 智能体的来源 **取值范围**： - AgentArts - OfficeClaw - OpenClaw 
        :type source: str
        :param agent_type: **参数解释**： 智能体类型 **取值范围**： - agent：单智能体。 - chat：工作流。 - controller：多智能体。 - teamAgent：团队智能体。 
        :type agent_type: str
        :param session_number: **参数解释**： 会话数量 **取值范围**： 0~2147483647 
        :type session_number: int
        :param project_id: **参数解释**： 项目ID **取值范围**： 字符长度为1-128位 
        :type project_id: str
        :param enterprise_project_id: **参数解释**： 企业项目ID **取值范围**： 字符长度为1-128位 
        :type enterprise_project_id: str
        :param image_url: **参数解释**： 镜像url **取值范围**： 字符长度为1-512位 
        :type image_url: str
        :param instance_create_time: **参数解释**： 智能体实例的创建时间，毫秒时间戳 **取值范围**： 0~9223372036854775807 
        :type instance_create_time: int
        :param instance_update_time: **参数解释**： 智能体实例的更新时间，毫秒时间戳 **取值范围**： 0~9223372036854775807 
        :type instance_update_time: int
        :param trace_alarm_number: **参数解释**： 行为轨迹告警数量 **取值范围**： 0~2147483647 
        :type trace_alarm_number: int
        :param runtime_alarm_number: **参数解释**： 运行时告警数量 **取值范围**： 0~2147483647 
        :type runtime_alarm_number: int
        :param policy_group_type: **参数解释**： 策略组类型 **取值范围**： - 0：Agent运行时防护-OfficeAce - 1：Agent行为轨迹检测-OfficeAce - 2：Agent角色限定 - 3：Agent运行时防护-AgentArts - 4：Agent行为轨迹检测-AgentArts - 5：Agent运行时防护-OpenClaw - 6：Agent运行时防护-其他三方Claw 
        :type policy_group_type: int
        :param policy_info_list: **参数解释**: AI策略组列表 **取值范围**: 不涉及 
        :type policy_info_list: list[:class:`huaweicloudsdkhss.v5.AiAgentPolicy`]
        :param agent_runtime_env: **参数解释**： 智能体运行环境 **取值范围**： - ECS - CCE - Others - AgentArts - OfficeClaw 
        :type agent_runtime_env: str
        :param cluster_id: **参数解释**： 集群ID，仅agent_runtime_env为CCE时返回 **取值范围**： 字符长度为1-128位 
        :type cluster_id: str
        :param cluster_type: **参数解释**： 集群类型 **取值范围**： - CCE：云容器引擎 
        :type cluster_type: str
        :param cluster_name: **参数解释**： 集群名称，仅agent_runtime_env为CCE时返回 **取值范围**： 字符长度为1-256位 
        :type cluster_name: str
        :param host_name: **参数解释**： 服务器名称 **取值范围**： 字符长度为1-256位 
        :type host_name: str
        :param public_ip: **参数解释**： 服务器公网IP地址 **取值范围**： 字符长度为1-128位 
        :type public_ip: str
        :param private_ip: **参数解释**： 服务器私有IP地址 **取值范围**： 字符长度为1-128位 
        :type private_ip: str
        :param host_status: **参数解释**： 服务器状态 **取值范围**： - ACTIVE：运行中 - SHUTOFF：已关机 - BUILD：创建中 - ERROR：异常 - DELETED：已删除 - REBOOT：重启中 
        :type host_status: str
        :param host_id: **参数解释**： 服务器ID **取值范围**： 字符长度为1-128位 
        :type host_id: str
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux - Windows 
        :type os_type: str
        :param os_name: **参数解释**： 操作系统名称 **取值范围**： - EulerOS 2.9 - CentOS 7.9 - Ubuntu 20.04 - 其他操作系统名称 
        :type os_name: str
        :param os_version: **参数解释**： 操作系统版本号 **取值范围**： 字符长度为1-64位 
        :type os_version: str
        :param kernel_version: **参数解释**： 操作系统内核版本号 **取值范围**： 字符长度为1-128位 
        :type kernel_version: str
        :param agent_status: **参数解释**： Agent状态 **取值范围**： - online：在线 - offline：离线 - not_installed：未安装 - install_failed：安装失败 - installing：安装中 
        :type agent_status: str
        :param defender_status: **参数解释**： 智能体卫士插件状态 **取值范围**： - not_installed：未安装 - install_failed：安装失败 - online：在线 - offline：离线 - installing：安装中 
        :type defender_status: str
        :param container_id: **参数解释** 容器实例id **取值范围**: 字符长度0-128位
        :type container_id: str
        """
        
        

        self._agent_name = None
        self._agent_id = None
        self._runtime_name = None
        self._runtime_id = None
        self._sdk_status = None
        self._source = None
        self._agent_type = None
        self._session_number = None
        self._project_id = None
        self._enterprise_project_id = None
        self._image_url = None
        self._instance_create_time = None
        self._instance_update_time = None
        self._trace_alarm_number = None
        self._runtime_alarm_number = None
        self._policy_group_type = None
        self._policy_info_list = None
        self._agent_runtime_env = None
        self._cluster_id = None
        self._cluster_type = None
        self._cluster_name = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._host_status = None
        self._host_id = None
        self._os_type = None
        self._os_name = None
        self._os_version = None
        self._kernel_version = None
        self._agent_status = None
        self._defender_status = None
        self._container_id = None
        self.discriminator = None

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
        if agent_type is not None:
            self.agent_type = agent_type
        if session_number is not None:
            self.session_number = session_number
        if project_id is not None:
            self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if image_url is not None:
            self.image_url = image_url
        if instance_create_time is not None:
            self.instance_create_time = instance_create_time
        if instance_update_time is not None:
            self.instance_update_time = instance_update_time
        if trace_alarm_number is not None:
            self.trace_alarm_number = trace_alarm_number
        if runtime_alarm_number is not None:
            self.runtime_alarm_number = runtime_alarm_number
        if policy_group_type is not None:
            self.policy_group_type = policy_group_type
        if policy_info_list is not None:
            self.policy_info_list = policy_info_list
        if agent_runtime_env is not None:
            self.agent_runtime_env = agent_runtime_env
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if host_status is not None:
            self.host_status = host_status
        if host_id is not None:
            self.host_id = host_id
        if os_type is not None:
            self.os_type = os_type
        if os_name is not None:
            self.os_name = os_name
        if os_version is not None:
            self.os_version = os_version
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if agent_status is not None:
            self.agent_status = agent_status
        if defender_status is not None:
            self.defender_status = defender_status
        if container_id is not None:
            self.container_id = container_id

    @property
    def agent_name(self):
        r"""Gets the agent_name of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体名字 **取值范围**： 字符长度为1-128位 

        :return: The agent_name of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        r"""Sets the agent_name of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体名字 **取值范围**： 字符长度为1-128位 

        :param agent_name: The agent_name of this ListAiInstancesResponseBodyData.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体ID **取值范围**： 字符长度为1-128位 

        :return: The agent_id of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体ID **取值范围**： 字符长度为1-128位 

        :param agent_id: The agent_id of this ListAiInstancesResponseBodyData.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def runtime_name(self):
        r"""Gets the runtime_name of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体运行时名字 **取值范围**： 字符长度为1-128位 

        :return: The runtime_name of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._runtime_name

    @runtime_name.setter
    def runtime_name(self, runtime_name):
        r"""Sets the runtime_name of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体运行时名字 **取值范围**： 字符长度为1-128位 

        :param runtime_name: The runtime_name of this ListAiInstancesResponseBodyData.
        :type runtime_name: str
        """
        self._runtime_name = runtime_name

    @property
    def runtime_id(self):
        r"""Gets the runtime_id of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体运行时ID **取值范围**： 字符长度为1-128位 

        :return: The runtime_id of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        r"""Sets the runtime_id of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体运行时ID **取值范围**： 字符长度为1-128位 

        :param runtime_id: The runtime_id of this ListAiInstancesResponseBodyData.
        :type runtime_id: str
        """
        self._runtime_id = runtime_id

    @property
    def sdk_status(self):
        r"""Gets the sdk_status of this ListAiInstancesResponseBodyData.

        **参数解释**： SDK检测状态 **取值范围**： - open：开启 - close：关闭 

        :return: The sdk_status of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._sdk_status

    @sdk_status.setter
    def sdk_status(self, sdk_status):
        r"""Sets the sdk_status of this ListAiInstancesResponseBodyData.

        **参数解释**： SDK检测状态 **取值范围**： - open：开启 - close：关闭 

        :param sdk_status: The sdk_status of this ListAiInstancesResponseBodyData.
        :type sdk_status: str
        """
        self._sdk_status = sdk_status

    @property
    def source(self):
        r"""Gets the source of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体的来源 **取值范围**： - AgentArts - OfficeClaw - OpenClaw 

        :return: The source of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体的来源 **取值范围**： - AgentArts - OfficeClaw - OpenClaw 

        :param source: The source of this ListAiInstancesResponseBodyData.
        :type source: str
        """
        self._source = source

    @property
    def agent_type(self):
        r"""Gets the agent_type of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体类型 **取值范围**： - agent：单智能体。 - chat：工作流。 - controller：多智能体。 - teamAgent：团队智能体。 

        :return: The agent_type of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体类型 **取值范围**： - agent：单智能体。 - chat：工作流。 - controller：多智能体。 - teamAgent：团队智能体。 

        :param agent_type: The agent_type of this ListAiInstancesResponseBodyData.
        :type agent_type: str
        """
        self._agent_type = agent_type

    @property
    def session_number(self):
        r"""Gets the session_number of this ListAiInstancesResponseBodyData.

        **参数解释**： 会话数量 **取值范围**： 0~2147483647 

        :return: The session_number of this ListAiInstancesResponseBodyData.
        :rtype: int
        """
        return self._session_number

    @session_number.setter
    def session_number(self, session_number):
        r"""Sets the session_number of this ListAiInstancesResponseBodyData.

        **参数解释**： 会话数量 **取值范围**： 0~2147483647 

        :param session_number: The session_number of this ListAiInstancesResponseBodyData.
        :type session_number: int
        """
        self._session_number = session_number

    @property
    def project_id(self):
        r"""Gets the project_id of this ListAiInstancesResponseBodyData.

        **参数解释**： 项目ID **取值范围**： 字符长度为1-128位 

        :return: The project_id of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListAiInstancesResponseBodyData.

        **参数解释**： 项目ID **取值范围**： 字符长度为1-128位 

        :param project_id: The project_id of this ListAiInstancesResponseBodyData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAiInstancesResponseBodyData.

        **参数解释**： 企业项目ID **取值范围**： 字符长度为1-128位 

        :return: The enterprise_project_id of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAiInstancesResponseBodyData.

        **参数解释**： 企业项目ID **取值范围**： 字符长度为1-128位 

        :param enterprise_project_id: The enterprise_project_id of this ListAiInstancesResponseBodyData.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_url(self):
        r"""Gets the image_url of this ListAiInstancesResponseBodyData.

        **参数解释**： 镜像url **取值范围**： 字符长度为1-512位 

        :return: The image_url of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this ListAiInstancesResponseBodyData.

        **参数解释**： 镜像url **取值范围**： 字符长度为1-512位 

        :param image_url: The image_url of this ListAiInstancesResponseBodyData.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def instance_create_time(self):
        r"""Gets the instance_create_time of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体实例的创建时间，毫秒时间戳 **取值范围**： 0~9223372036854775807 

        :return: The instance_create_time of this ListAiInstancesResponseBodyData.
        :rtype: int
        """
        return self._instance_create_time

    @instance_create_time.setter
    def instance_create_time(self, instance_create_time):
        r"""Sets the instance_create_time of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体实例的创建时间，毫秒时间戳 **取值范围**： 0~9223372036854775807 

        :param instance_create_time: The instance_create_time of this ListAiInstancesResponseBodyData.
        :type instance_create_time: int
        """
        self._instance_create_time = instance_create_time

    @property
    def instance_update_time(self):
        r"""Gets the instance_update_time of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体实例的更新时间，毫秒时间戳 **取值范围**： 0~9223372036854775807 

        :return: The instance_update_time of this ListAiInstancesResponseBodyData.
        :rtype: int
        """
        return self._instance_update_time

    @instance_update_time.setter
    def instance_update_time(self, instance_update_time):
        r"""Sets the instance_update_time of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体实例的更新时间，毫秒时间戳 **取值范围**： 0~9223372036854775807 

        :param instance_update_time: The instance_update_time of this ListAiInstancesResponseBodyData.
        :type instance_update_time: int
        """
        self._instance_update_time = instance_update_time

    @property
    def trace_alarm_number(self):
        r"""Gets the trace_alarm_number of this ListAiInstancesResponseBodyData.

        **参数解释**： 行为轨迹告警数量 **取值范围**： 0~2147483647 

        :return: The trace_alarm_number of this ListAiInstancesResponseBodyData.
        :rtype: int
        """
        return self._trace_alarm_number

    @trace_alarm_number.setter
    def trace_alarm_number(self, trace_alarm_number):
        r"""Sets the trace_alarm_number of this ListAiInstancesResponseBodyData.

        **参数解释**： 行为轨迹告警数量 **取值范围**： 0~2147483647 

        :param trace_alarm_number: The trace_alarm_number of this ListAiInstancesResponseBodyData.
        :type trace_alarm_number: int
        """
        self._trace_alarm_number = trace_alarm_number

    @property
    def runtime_alarm_number(self):
        r"""Gets the runtime_alarm_number of this ListAiInstancesResponseBodyData.

        **参数解释**： 运行时告警数量 **取值范围**： 0~2147483647 

        :return: The runtime_alarm_number of this ListAiInstancesResponseBodyData.
        :rtype: int
        """
        return self._runtime_alarm_number

    @runtime_alarm_number.setter
    def runtime_alarm_number(self, runtime_alarm_number):
        r"""Sets the runtime_alarm_number of this ListAiInstancesResponseBodyData.

        **参数解释**： 运行时告警数量 **取值范围**： 0~2147483647 

        :param runtime_alarm_number: The runtime_alarm_number of this ListAiInstancesResponseBodyData.
        :type runtime_alarm_number: int
        """
        self._runtime_alarm_number = runtime_alarm_number

    @property
    def policy_group_type(self):
        r"""Gets the policy_group_type of this ListAiInstancesResponseBodyData.

        **参数解释**： 策略组类型 **取值范围**： - 0：Agent运行时防护-OfficeAce - 1：Agent行为轨迹检测-OfficeAce - 2：Agent角色限定 - 3：Agent运行时防护-AgentArts - 4：Agent行为轨迹检测-AgentArts - 5：Agent运行时防护-OpenClaw - 6：Agent运行时防护-其他三方Claw 

        :return: The policy_group_type of this ListAiInstancesResponseBodyData.
        :rtype: int
        """
        return self._policy_group_type

    @policy_group_type.setter
    def policy_group_type(self, policy_group_type):
        r"""Sets the policy_group_type of this ListAiInstancesResponseBodyData.

        **参数解释**： 策略组类型 **取值范围**： - 0：Agent运行时防护-OfficeAce - 1：Agent行为轨迹检测-OfficeAce - 2：Agent角色限定 - 3：Agent运行时防护-AgentArts - 4：Agent行为轨迹检测-AgentArts - 5：Agent运行时防护-OpenClaw - 6：Agent运行时防护-其他三方Claw 

        :param policy_group_type: The policy_group_type of this ListAiInstancesResponseBodyData.
        :type policy_group_type: int
        """
        self._policy_group_type = policy_group_type

    @property
    def policy_info_list(self):
        r"""Gets the policy_info_list of this ListAiInstancesResponseBodyData.

        **参数解释**: AI策略组列表 **取值范围**: 不涉及 

        :return: The policy_info_list of this ListAiInstancesResponseBodyData.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AiAgentPolicy`]
        """
        return self._policy_info_list

    @policy_info_list.setter
    def policy_info_list(self, policy_info_list):
        r"""Sets the policy_info_list of this ListAiInstancesResponseBodyData.

        **参数解释**: AI策略组列表 **取值范围**: 不涉及 

        :param policy_info_list: The policy_info_list of this ListAiInstancesResponseBodyData.
        :type policy_info_list: list[:class:`huaweicloudsdkhss.v5.AiAgentPolicy`]
        """
        self._policy_info_list = policy_info_list

    @property
    def agent_runtime_env(self):
        r"""Gets the agent_runtime_env of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体运行环境 **取值范围**： - ECS - CCE - Others - AgentArts - OfficeClaw 

        :return: The agent_runtime_env of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._agent_runtime_env

    @agent_runtime_env.setter
    def agent_runtime_env(self, agent_runtime_env):
        r"""Sets the agent_runtime_env of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体运行环境 **取值范围**： - ECS - CCE - Others - AgentArts - OfficeClaw 

        :param agent_runtime_env: The agent_runtime_env of this ListAiInstancesResponseBodyData.
        :type agent_runtime_env: str
        """
        self._agent_runtime_env = agent_runtime_env

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListAiInstancesResponseBodyData.

        **参数解释**： 集群ID，仅agent_runtime_env为CCE时返回 **取值范围**： 字符长度为1-128位 

        :return: The cluster_id of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListAiInstancesResponseBodyData.

        **参数解释**： 集群ID，仅agent_runtime_env为CCE时返回 **取值范围**： 字符长度为1-128位 

        :param cluster_id: The cluster_id of this ListAiInstancesResponseBodyData.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ListAiInstancesResponseBodyData.

        **参数解释**： 集群类型 **取值范围**： - CCE：云容器引擎 

        :return: The cluster_type of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ListAiInstancesResponseBodyData.

        **参数解释**： 集群类型 **取值范围**： - CCE：云容器引擎 

        :param cluster_type: The cluster_type of this ListAiInstancesResponseBodyData.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListAiInstancesResponseBodyData.

        **参数解释**： 集群名称，仅agent_runtime_env为CCE时返回 **取值范围**： 字符长度为1-256位 

        :return: The cluster_name of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListAiInstancesResponseBodyData.

        **参数解释**： 集群名称，仅agent_runtime_env为CCE时返回 **取值范围**： 字符长度为1-256位 

        :param cluster_name: The cluster_name of this ListAiInstancesResponseBodyData.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ListAiInstancesResponseBodyData.

        **参数解释**： 服务器名称 **取值范围**： 字符长度为1-256位 

        :return: The host_name of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListAiInstancesResponseBodyData.

        **参数解释**： 服务器名称 **取值范围**： 字符长度为1-256位 

        :param host_name: The host_name of this ListAiInstancesResponseBodyData.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListAiInstancesResponseBodyData.

        **参数解释**： 服务器公网IP地址 **取值范围**： 字符长度为1-128位 

        :return: The public_ip of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListAiInstancesResponseBodyData.

        **参数解释**： 服务器公网IP地址 **取值范围**： 字符长度为1-128位 

        :param public_ip: The public_ip of this ListAiInstancesResponseBodyData.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListAiInstancesResponseBodyData.

        **参数解释**： 服务器私有IP地址 **取值范围**： 字符长度为1-128位 

        :return: The private_ip of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListAiInstancesResponseBodyData.

        **参数解释**： 服务器私有IP地址 **取值范围**： 字符长度为1-128位 

        :param private_ip: The private_ip of this ListAiInstancesResponseBodyData.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def host_status(self):
        r"""Gets the host_status of this ListAiInstancesResponseBodyData.

        **参数解释**： 服务器状态 **取值范围**： - ACTIVE：运行中 - SHUTOFF：已关机 - BUILD：创建中 - ERROR：异常 - DELETED：已删除 - REBOOT：重启中 

        :return: The host_status of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this ListAiInstancesResponseBodyData.

        **参数解释**： 服务器状态 **取值范围**： - ACTIVE：运行中 - SHUTOFF：已关机 - BUILD：创建中 - ERROR：异常 - DELETED：已删除 - REBOOT：重启中 

        :param host_status: The host_status of this ListAiInstancesResponseBodyData.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def host_id(self):
        r"""Gets the host_id of this ListAiInstancesResponseBodyData.

        **参数解释**： 服务器ID **取值范围**： 字符长度为1-128位 

        :return: The host_id of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListAiInstancesResponseBodyData.

        **参数解释**： 服务器ID **取值范围**： 字符长度为1-128位 

        :param host_id: The host_id of this ListAiInstancesResponseBodyData.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def os_type(self):
        r"""Gets the os_type of this ListAiInstancesResponseBodyData.

        **参数解释**： 操作系统类型 **取值范围**： - Linux - Windows 

        :return: The os_type of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListAiInstancesResponseBodyData.

        **参数解释**： 操作系统类型 **取值范围**： - Linux - Windows 

        :param os_type: The os_type of this ListAiInstancesResponseBodyData.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_name(self):
        r"""Gets the os_name of this ListAiInstancesResponseBodyData.

        **参数解释**： 操作系统名称 **取值范围**： - EulerOS 2.9 - CentOS 7.9 - Ubuntu 20.04 - 其他操作系统名称 

        :return: The os_name of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this ListAiInstancesResponseBodyData.

        **参数解释**： 操作系统名称 **取值范围**： - EulerOS 2.9 - CentOS 7.9 - Ubuntu 20.04 - 其他操作系统名称 

        :param os_name: The os_name of this ListAiInstancesResponseBodyData.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        r"""Gets the os_version of this ListAiInstancesResponseBodyData.

        **参数解释**： 操作系统版本号 **取值范围**： 字符长度为1-64位 

        :return: The os_version of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this ListAiInstancesResponseBodyData.

        **参数解释**： 操作系统版本号 **取值范围**： 字符长度为1-64位 

        :param os_version: The os_version of this ListAiInstancesResponseBodyData.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def kernel_version(self):
        r"""Gets the kernel_version of this ListAiInstancesResponseBodyData.

        **参数解释**： 操作系统内核版本号 **取值范围**： 字符长度为1-128位 

        :return: The kernel_version of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        r"""Sets the kernel_version of this ListAiInstancesResponseBodyData.

        **参数解释**： 操作系统内核版本号 **取值范围**： 字符长度为1-128位 

        :param kernel_version: The kernel_version of this ListAiInstancesResponseBodyData.
        :type kernel_version: str
        """
        self._kernel_version = kernel_version

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ListAiInstancesResponseBodyData.

        **参数解释**： Agent状态 **取值范围**： - online：在线 - offline：离线 - not_installed：未安装 - install_failed：安装失败 - installing：安装中 

        :return: The agent_status of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ListAiInstancesResponseBodyData.

        **参数解释**： Agent状态 **取值范围**： - online：在线 - offline：离线 - not_installed：未安装 - install_failed：安装失败 - installing：安装中 

        :param agent_status: The agent_status of this ListAiInstancesResponseBodyData.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def defender_status(self):
        r"""Gets the defender_status of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体卫士插件状态 **取值范围**： - not_installed：未安装 - install_failed：安装失败 - online：在线 - offline：离线 - installing：安装中 

        :return: The defender_status of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._defender_status

    @defender_status.setter
    def defender_status(self, defender_status):
        r"""Sets the defender_status of this ListAiInstancesResponseBodyData.

        **参数解释**： 智能体卫士插件状态 **取值范围**： - not_installed：未安装 - install_failed：安装失败 - online：在线 - offline：离线 - installing：安装中 

        :param defender_status: The defender_status of this ListAiInstancesResponseBodyData.
        :type defender_status: str
        """
        self._defender_status = defender_status

    @property
    def container_id(self):
        r"""Gets the container_id of this ListAiInstancesResponseBodyData.

        **参数解释** 容器实例id **取值范围**: 字符长度0-128位

        :return: The container_id of this ListAiInstancesResponseBodyData.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ListAiInstancesResponseBodyData.

        **参数解释** 容器实例id **取值范围**: 字符长度0-128位

        :param container_id: The container_id of this ListAiInstancesResponseBodyData.
        :type container_id: str
        """
        self._container_id = container_id

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
        if not isinstance(other, ListAiInstancesResponseBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
