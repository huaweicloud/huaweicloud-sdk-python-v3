# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerlessInstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_name': 'str',
        'instance_name': 'str',
        'instance_id': 'str',
        'instance_ip': 'str',
        'instance_status': 'str',
        'namespace_name': 'str',
        'agent_status': 'str',
        'agent_id': 'str',
        'create_time': 'int',
        'subscribe_time': 'int',
        'cpu_request': 'str',
        'cpu_limit': 'str',
        'protect_status': 'str',
        'policy_group_name': 'str',
        'labels': 'list[LabelInfo]',
        'cluster_name': 'str',
        'workload_name': 'str',
        'cluster_id': 'str',
        'container_info': 'list[ProtectionContainerInfo]',
        'is_support_protect': 'bool',
        'reason': 'str',
        'vul_num': 'int',
        'app_vul_num': 'int',
        'linux_vul_num': 'int',
        'security_num': 'int',
        'event_num': 'int'
    }

    attribute_map = {
        'enterprise_project_name': 'enterprise_project_name',
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'instance_ip': 'instance_ip',
        'instance_status': 'instance_status',
        'namespace_name': 'namespace_name',
        'agent_status': 'agent_status',
        'agent_id': 'agent_id',
        'create_time': 'create_time',
        'subscribe_time': 'subscribe_time',
        'cpu_request': 'cpu_request',
        'cpu_limit': 'cpu_limit',
        'protect_status': 'protect_status',
        'policy_group_name': 'policy_group_name',
        'labels': 'labels',
        'cluster_name': 'cluster_name',
        'workload_name': 'workload_name',
        'cluster_id': 'cluster_id',
        'container_info': 'container_info',
        'is_support_protect': 'is_support_protect',
        'reason': 'reason',
        'vul_num': 'vul_num',
        'app_vul_num': 'app_vul_num',
        'linux_vul_num': 'linux_vul_num',
        'security_num': 'security_num',
        'event_num': 'event_num'
    }

    def __init__(self, enterprise_project_name=None, instance_name=None, instance_id=None, instance_ip=None, instance_status=None, namespace_name=None, agent_status=None, agent_id=None, create_time=None, subscribe_time=None, cpu_request=None, cpu_limit=None, protect_status=None, policy_group_name=None, labels=None, cluster_name=None, workload_name=None, cluster_id=None, container_info=None, is_support_protect=None, reason=None, vul_num=None, app_vul_num=None, linux_vul_num=None, security_num=None, event_num=None):
        r"""ServerlessInstanceInfo

        The model defined in huaweicloud sdk

        :param enterprise_project_name: **参数解释**: 所属企业项目名称 **取值范围**: 字符长度0-65535位 
        :type enterprise_project_name: str
        :param instance_name: **参数解释**: 实例名称 **取值范围**: 字符长度0-65535位 
        :type instance_name: str
        :param instance_id: **参数解释**: 实例ID **取值范围**: 字符长度0-65535位 
        :type instance_id: str
        :param instance_ip: **参数解释**: 实例IP **取值范围**: 字符长度0-65535位 
        :type instance_ip: str
        :param instance_status: **参数解释**: 实例状态 **取值范围**: 字符长度0-65535位 
        :type instance_status: str
        :param namespace_name: **参数解释**: 命名空间名称 **取值范围**: 字符长度0-256位 
        :type namespace_name: str
        :param agent_status: **参数解释**: agent状态 **取值范围**: 字符长度0-65535位 
        :type agent_status: str
        :param agent_id: **参数解释**: agentID标识 **取值范围**: 字符长度0-65535位 
        :type agent_id: str
        :param create_time: **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type create_time: int
        :param subscribe_time: **参数解释**: 开通防护时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type subscribe_time: int
        :param cpu_request: **参数解释**: cpu申请值 **取值范围**: 字符长度0-65535位 
        :type cpu_request: str
        :param cpu_limit: **参数解释**: cpu限制值 **取值范围**: 字符长度0-65535位 
        :type cpu_limit: str
        :param protect_status: **参数解释**: 防护状态 **取值范围**: 字符长度0-65535位 
        :type protect_status: str
        :param policy_group_name: **参数解释**: 策略组名称 **取值范围**: 字符长度0-65535位 
        :type policy_group_name: str
        :param labels: **参数解释**: 标签 **取值范围**: 最小值0，最大值65535 
        :type labels: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        :param cluster_name: **参数解释**: 所属集群名称 **取值范围**: 字符长度0-65535位 
        :type cluster_name: str
        :param workload_name: **参数解释**: 所属工作负载名称 **取值范围**: 字符长度0-65535位 
        :type workload_name: str
        :param cluster_id: **参数解释**: 所属集群ID **取值范围**: 字符长度0-65535位 
        :type cluster_id: str
        :param container_info: **参数解释**: 容器列表 **取值范围**: 最小值0，最大值65535 
        :type container_info: list[:class:`huaweicloudsdkhss.v5.ProtectionContainerInfo`]
        :param is_support_protect: **参数解释**: 实例是否支持开关防护 **取值范围**: - true：是。 - false：否。 
        :type is_support_protect: bool
        :param reason: **参数解释**: 实例不支持开关防护的原因 **取值范围**: 字符长度0-65535位 
        :type reason: str
        :param vul_num: **参数解释**: 实例漏洞风险数 **取值范围**: 最小值0，最大值9223372036854775807 
        :type vul_num: int
        :param app_vul_num: **参数解释**: 实例应用漏洞风险数 **取值范围**: 最小值0，最大值9223372036854775807 
        :type app_vul_num: int
        :param linux_vul_num: **参数解释**: 实例系统漏洞风险数 **取值范围**: 最小值0，最大值9223372036854775807 
        :type linux_vul_num: int
        :param security_num: **参数解释**: 实例基线检查数 **取值范围**: 最小值0，最大值9223372036854775807 
        :type security_num: int
        :param event_num: **参数解释**: 实例入侵风险数 **取值范围**: 最小值0，最大值9223372036854775807 
        :type event_num: int
        """
        
        

        self._enterprise_project_name = None
        self._instance_name = None
        self._instance_id = None
        self._instance_ip = None
        self._instance_status = None
        self._namespace_name = None
        self._agent_status = None
        self._agent_id = None
        self._create_time = None
        self._subscribe_time = None
        self._cpu_request = None
        self._cpu_limit = None
        self._protect_status = None
        self._policy_group_name = None
        self._labels = None
        self._cluster_name = None
        self._workload_name = None
        self._cluster_id = None
        self._container_info = None
        self._is_support_protect = None
        self._reason = None
        self._vul_num = None
        self._app_vul_num = None
        self._linux_vul_num = None
        self._security_num = None
        self._event_num = None
        self.discriminator = None

        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_ip is not None:
            self.instance_ip = instance_ip
        if instance_status is not None:
            self.instance_status = instance_status
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if agent_status is not None:
            self.agent_status = agent_status
        if agent_id is not None:
            self.agent_id = agent_id
        if create_time is not None:
            self.create_time = create_time
        if subscribe_time is not None:
            self.subscribe_time = subscribe_time
        if cpu_request is not None:
            self.cpu_request = cpu_request
        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if protect_status is not None:
            self.protect_status = protect_status
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if labels is not None:
            self.labels = labels
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if workload_name is not None:
            self.workload_name = workload_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if container_info is not None:
            self.container_info = container_info
        if is_support_protect is not None:
            self.is_support_protect = is_support_protect
        if reason is not None:
            self.reason = reason
        if vul_num is not None:
            self.vul_num = vul_num
        if app_vul_num is not None:
            self.app_vul_num = app_vul_num
        if linux_vul_num is not None:
            self.linux_vul_num = linux_vul_num
        if security_num is not None:
            self.security_num = security_num
        if event_num is not None:
            self.event_num = event_num

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this ServerlessInstanceInfo.

        **参数解释**: 所属企业项目名称 **取值范围**: 字符长度0-65535位 

        :return: The enterprise_project_name of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this ServerlessInstanceInfo.

        **参数解释**: 所属企业项目名称 **取值范围**: 字符长度0-65535位 

        :param enterprise_project_name: The enterprise_project_name of this ServerlessInstanceInfo.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ServerlessInstanceInfo.

        **参数解释**: 实例名称 **取值范围**: 字符长度0-65535位 

        :return: The instance_name of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ServerlessInstanceInfo.

        **参数解释**: 实例名称 **取值范围**: 字符长度0-65535位 

        :param instance_name: The instance_name of this ServerlessInstanceInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ServerlessInstanceInfo.

        **参数解释**: 实例ID **取值范围**: 字符长度0-65535位 

        :return: The instance_id of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ServerlessInstanceInfo.

        **参数解释**: 实例ID **取值范围**: 字符长度0-65535位 

        :param instance_id: The instance_id of this ServerlessInstanceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_ip(self):
        r"""Gets the instance_ip of this ServerlessInstanceInfo.

        **参数解释**: 实例IP **取值范围**: 字符长度0-65535位 

        :return: The instance_ip of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._instance_ip

    @instance_ip.setter
    def instance_ip(self, instance_ip):
        r"""Sets the instance_ip of this ServerlessInstanceInfo.

        **参数解释**: 实例IP **取值范围**: 字符长度0-65535位 

        :param instance_ip: The instance_ip of this ServerlessInstanceInfo.
        :type instance_ip: str
        """
        self._instance_ip = instance_ip

    @property
    def instance_status(self):
        r"""Gets the instance_status of this ServerlessInstanceInfo.

        **参数解释**: 实例状态 **取值范围**: 字符长度0-65535位 

        :return: The instance_status of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this ServerlessInstanceInfo.

        **参数解释**: 实例状态 **取值范围**: 字符长度0-65535位 

        :param instance_status: The instance_status of this ServerlessInstanceInfo.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ServerlessInstanceInfo.

        **参数解释**: 命名空间名称 **取值范围**: 字符长度0-256位 

        :return: The namespace_name of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ServerlessInstanceInfo.

        **参数解释**: 命名空间名称 **取值范围**: 字符长度0-256位 

        :param namespace_name: The namespace_name of this ServerlessInstanceInfo.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ServerlessInstanceInfo.

        **参数解释**: agent状态 **取值范围**: 字符长度0-65535位 

        :return: The agent_status of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ServerlessInstanceInfo.

        **参数解释**: agent状态 **取值范围**: 字符长度0-65535位 

        :param agent_status: The agent_status of this ServerlessInstanceInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ServerlessInstanceInfo.

        **参数解释**: agentID标识 **取值范围**: 字符长度0-65535位 

        :return: The agent_id of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ServerlessInstanceInfo.

        **参数解释**: agentID标识 **取值范围**: 字符长度0-65535位 

        :param agent_id: The agent_id of this ServerlessInstanceInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ServerlessInstanceInfo.

        **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The create_time of this ServerlessInstanceInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ServerlessInstanceInfo.

        **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param create_time: The create_time of this ServerlessInstanceInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def subscribe_time(self):
        r"""Gets the subscribe_time of this ServerlessInstanceInfo.

        **参数解释**: 开通防护时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The subscribe_time of this ServerlessInstanceInfo.
        :rtype: int
        """
        return self._subscribe_time

    @subscribe_time.setter
    def subscribe_time(self, subscribe_time):
        r"""Sets the subscribe_time of this ServerlessInstanceInfo.

        **参数解释**: 开通防护时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param subscribe_time: The subscribe_time of this ServerlessInstanceInfo.
        :type subscribe_time: int
        """
        self._subscribe_time = subscribe_time

    @property
    def cpu_request(self):
        r"""Gets the cpu_request of this ServerlessInstanceInfo.

        **参数解释**: cpu申请值 **取值范围**: 字符长度0-65535位 

        :return: The cpu_request of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._cpu_request

    @cpu_request.setter
    def cpu_request(self, cpu_request):
        r"""Sets the cpu_request of this ServerlessInstanceInfo.

        **参数解释**: cpu申请值 **取值范围**: 字符长度0-65535位 

        :param cpu_request: The cpu_request of this ServerlessInstanceInfo.
        :type cpu_request: str
        """
        self._cpu_request = cpu_request

    @property
    def cpu_limit(self):
        r"""Gets the cpu_limit of this ServerlessInstanceInfo.

        **参数解释**: cpu限制值 **取值范围**: 字符长度0-65535位 

        :return: The cpu_limit of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        r"""Sets the cpu_limit of this ServerlessInstanceInfo.

        **参数解释**: cpu限制值 **取值范围**: 字符长度0-65535位 

        :param cpu_limit: The cpu_limit of this ServerlessInstanceInfo.
        :type cpu_limit: str
        """
        self._cpu_limit = cpu_limit

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ServerlessInstanceInfo.

        **参数解释**: 防护状态 **取值范围**: 字符长度0-65535位 

        :return: The protect_status of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ServerlessInstanceInfo.

        **参数解释**: 防护状态 **取值范围**: 字符长度0-65535位 

        :param protect_status: The protect_status of this ServerlessInstanceInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def policy_group_name(self):
        r"""Gets the policy_group_name of this ServerlessInstanceInfo.

        **参数解释**: 策略组名称 **取值范围**: 字符长度0-65535位 

        :return: The policy_group_name of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        r"""Sets the policy_group_name of this ServerlessInstanceInfo.

        **参数解释**: 策略组名称 **取值范围**: 字符长度0-65535位 

        :param policy_group_name: The policy_group_name of this ServerlessInstanceInfo.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def labels(self):
        r"""Gets the labels of this ServerlessInstanceInfo.

        **参数解释**: 标签 **取值范围**: 最小值0，最大值65535 

        :return: The labels of this ServerlessInstanceInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ServerlessInstanceInfo.

        **参数解释**: 标签 **取值范围**: 最小值0，最大值65535 

        :param labels: The labels of this ServerlessInstanceInfo.
        :type labels: list[:class:`huaweicloudsdkhss.v5.LabelInfo`]
        """
        self._labels = labels

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ServerlessInstanceInfo.

        **参数解释**: 所属集群名称 **取值范围**: 字符长度0-65535位 

        :return: The cluster_name of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ServerlessInstanceInfo.

        **参数解释**: 所属集群名称 **取值范围**: 字符长度0-65535位 

        :param cluster_name: The cluster_name of this ServerlessInstanceInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def workload_name(self):
        r"""Gets the workload_name of this ServerlessInstanceInfo.

        **参数解释**: 所属工作负载名称 **取值范围**: 字符长度0-65535位 

        :return: The workload_name of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._workload_name

    @workload_name.setter
    def workload_name(self, workload_name):
        r"""Sets the workload_name of this ServerlessInstanceInfo.

        **参数解释**: 所属工作负载名称 **取值范围**: 字符长度0-65535位 

        :param workload_name: The workload_name of this ServerlessInstanceInfo.
        :type workload_name: str
        """
        self._workload_name = workload_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ServerlessInstanceInfo.

        **参数解释**: 所属集群ID **取值范围**: 字符长度0-65535位 

        :return: The cluster_id of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ServerlessInstanceInfo.

        **参数解释**: 所属集群ID **取值范围**: 字符长度0-65535位 

        :param cluster_id: The cluster_id of this ServerlessInstanceInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def container_info(self):
        r"""Gets the container_info of this ServerlessInstanceInfo.

        **参数解释**: 容器列表 **取值范围**: 最小值0，最大值65535 

        :return: The container_info of this ServerlessInstanceInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ProtectionContainerInfo`]
        """
        return self._container_info

    @container_info.setter
    def container_info(self, container_info):
        r"""Sets the container_info of this ServerlessInstanceInfo.

        **参数解释**: 容器列表 **取值范围**: 最小值0，最大值65535 

        :param container_info: The container_info of this ServerlessInstanceInfo.
        :type container_info: list[:class:`huaweicloudsdkhss.v5.ProtectionContainerInfo`]
        """
        self._container_info = container_info

    @property
    def is_support_protect(self):
        r"""Gets the is_support_protect of this ServerlessInstanceInfo.

        **参数解释**: 实例是否支持开关防护 **取值范围**: - true：是。 - false：否。 

        :return: The is_support_protect of this ServerlessInstanceInfo.
        :rtype: bool
        """
        return self._is_support_protect

    @is_support_protect.setter
    def is_support_protect(self, is_support_protect):
        r"""Sets the is_support_protect of this ServerlessInstanceInfo.

        **参数解释**: 实例是否支持开关防护 **取值范围**: - true：是。 - false：否。 

        :param is_support_protect: The is_support_protect of this ServerlessInstanceInfo.
        :type is_support_protect: bool
        """
        self._is_support_protect = is_support_protect

    @property
    def reason(self):
        r"""Gets the reason of this ServerlessInstanceInfo.

        **参数解释**: 实例不支持开关防护的原因 **取值范围**: 字符长度0-65535位 

        :return: The reason of this ServerlessInstanceInfo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ServerlessInstanceInfo.

        **参数解释**: 实例不支持开关防护的原因 **取值范围**: 字符长度0-65535位 

        :param reason: The reason of this ServerlessInstanceInfo.
        :type reason: str
        """
        self._reason = reason

    @property
    def vul_num(self):
        r"""Gets the vul_num of this ServerlessInstanceInfo.

        **参数解释**: 实例漏洞风险数 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The vul_num of this ServerlessInstanceInfo.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this ServerlessInstanceInfo.

        **参数解释**: 实例漏洞风险数 **取值范围**: 最小值0，最大值9223372036854775807 

        :param vul_num: The vul_num of this ServerlessInstanceInfo.
        :type vul_num: int
        """
        self._vul_num = vul_num

    @property
    def app_vul_num(self):
        r"""Gets the app_vul_num of this ServerlessInstanceInfo.

        **参数解释**: 实例应用漏洞风险数 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The app_vul_num of this ServerlessInstanceInfo.
        :rtype: int
        """
        return self._app_vul_num

    @app_vul_num.setter
    def app_vul_num(self, app_vul_num):
        r"""Sets the app_vul_num of this ServerlessInstanceInfo.

        **参数解释**: 实例应用漏洞风险数 **取值范围**: 最小值0，最大值9223372036854775807 

        :param app_vul_num: The app_vul_num of this ServerlessInstanceInfo.
        :type app_vul_num: int
        """
        self._app_vul_num = app_vul_num

    @property
    def linux_vul_num(self):
        r"""Gets the linux_vul_num of this ServerlessInstanceInfo.

        **参数解释**: 实例系统漏洞风险数 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The linux_vul_num of this ServerlessInstanceInfo.
        :rtype: int
        """
        return self._linux_vul_num

    @linux_vul_num.setter
    def linux_vul_num(self, linux_vul_num):
        r"""Sets the linux_vul_num of this ServerlessInstanceInfo.

        **参数解释**: 实例系统漏洞风险数 **取值范围**: 最小值0，最大值9223372036854775807 

        :param linux_vul_num: The linux_vul_num of this ServerlessInstanceInfo.
        :type linux_vul_num: int
        """
        self._linux_vul_num = linux_vul_num

    @property
    def security_num(self):
        r"""Gets the security_num of this ServerlessInstanceInfo.

        **参数解释**: 实例基线检查数 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The security_num of this ServerlessInstanceInfo.
        :rtype: int
        """
        return self._security_num

    @security_num.setter
    def security_num(self, security_num):
        r"""Sets the security_num of this ServerlessInstanceInfo.

        **参数解释**: 实例基线检查数 **取值范围**: 最小值0，最大值9223372036854775807 

        :param security_num: The security_num of this ServerlessInstanceInfo.
        :type security_num: int
        """
        self._security_num = security_num

    @property
    def event_num(self):
        r"""Gets the event_num of this ServerlessInstanceInfo.

        **参数解释**: 实例入侵风险数 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The event_num of this ServerlessInstanceInfo.
        :rtype: int
        """
        return self._event_num

    @event_num.setter
    def event_num(self, event_num):
        r"""Sets the event_num of this ServerlessInstanceInfo.

        **参数解释**: 实例入侵风险数 **取值范围**: 最小值0，最大值9223372036854775807 

        :param event_num: The event_num of this ServerlessInstanceInfo.
        :type event_num: int
        """
        self._event_num = event_num

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
        if not isinstance(other, ServerlessInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
