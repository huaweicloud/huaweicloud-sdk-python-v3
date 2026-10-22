# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInferDeploymentResponse(SdkResponse):

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
        'name': 'str',
        'deployment_name': 'str',
        'infer_name': 'str',
        'description': 'str',
        'pool_id': 'str',
        'framework': 'str',
        'version': 'str',
        'version_id': 'str',
        'version_count': 'int',
        'count': 'int',
        'weight': 'int',
        'priority': 'int',
        'secret_type': 'str',
        'secret_name': 'str',
        'status': 'str',
        'deploy_type': 'str',
        'workload_type': 'str',
        'high_avail_switch': 'bool',
        'system_log_dump_enable': 'bool',
        'schedule_strategy': 'str',
        'unit_configs': 'list[UnitConfig]',
        'model': 'GroupModel',
        'advanced_config': 'AdvancedConfig',
        'mirror_traffic_enable': 'bool',
        'mirror_traffic_weight': 'int',
        'user_name': 'str',
        'agency_name': 'str',
        'last_used_time': 'datetime',
        'deployment_task_limit': 'DeploymentTaskLimit',
        'frozen_infos': 'list[FrozenInfo]',
        'create_at': 'datetime',
        'update_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'deployment_name': 'deployment_name',
        'infer_name': 'infer_name',
        'description': 'description',
        'pool_id': 'pool_id',
        'framework': 'framework',
        'version': 'version',
        'version_id': 'version_id',
        'version_count': 'version_count',
        'count': 'count',
        'weight': 'weight',
        'priority': 'priority',
        'secret_type': 'secret_type',
        'secret_name': 'secret_name',
        'status': 'status',
        'deploy_type': 'deploy_type',
        'workload_type': 'workload_type',
        'high_avail_switch': 'high_avail_switch',
        'system_log_dump_enable': 'system_log_dump_enable',
        'schedule_strategy': 'schedule_strategy',
        'unit_configs': 'unit_configs',
        'model': 'model',
        'advanced_config': 'advanced_config',
        'mirror_traffic_enable': 'mirror_traffic_enable',
        'mirror_traffic_weight': 'mirror_traffic_weight',
        'user_name': 'user_name',
        'agency_name': 'agency_name',
        'last_used_time': 'last_used_time',
        'deployment_task_limit': 'deployment_task_limit',
        'frozen_infos': 'frozen_infos',
        'create_at': 'create_at',
        'update_at': 'update_at'
    }

    def __init__(self, id=None, name=None, deployment_name=None, infer_name=None, description=None, pool_id=None, framework=None, version=None, version_id=None, version_count=None, count=None, weight=None, priority=None, secret_type=None, secret_name=None, status=None, deploy_type=None, workload_type=None, high_avail_switch=None, system_log_dump_enable=None, schedule_strategy=None, unit_configs=None, model=None, advanced_config=None, mirror_traffic_enable=None, mirror_traffic_weight=None, user_name=None, agency_name=None, last_used_time=None, deployment_task_limit=None, frozen_infos=None, create_at=None, update_at=None):
        r"""UpdateInferDeploymentResponse

        The model defined in huaweicloud sdk

        :param id: 参数解释： 部署ID，在[添加部署](CreateInferDeployment.xml)时即可在返回体中获取，也可通过[查询服务部署列表](ListInferDeployments.xml)获取当前用户拥有的部署，其中deployment_id字段即为部署ID。 约束限制： 不涉及。 取值范围： 部署ID。 默认取值： 不涉及。
        :type id: str
        :param name: **参数解释：** 服务部署名字
        :type name: str
        :param deployment_name: 参数解释： 服务部署名字。
        :type deployment_name: str
        :param infer_name: 参数解释： 部署id（废弃字段）。 取值范围： 不涉及。
        :type infer_name: str
        :param description: 参数解释： 描述 取值范围： 不涉及。
        :type description: str
        :param pool_id: **参数解释：** 专属资源池ID。 **取值范围：** 不涉及。
        :type pool_id: str
        :param framework: **参数解释：** 算法框架。 **取值范围：** - COMMON： 普通在线服务。
        :type framework: str
        :param version: **参数解释：** 当前部署版本信息。
        :type version: str
        :param version_id: **参数解释：** 版本id，可通过查询version列表查询。 **取值范围：** 不涉及。
        :type version_id: str
        :param version_count: **参数解释：** 服务版本数量。 **取值范围：** 不涉及。
        :type version_count: int
        :param count: **参数解释：** 服务部署实例数。
        :type count: int
        :param weight: **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **约束限制：** 不涉及。 **取值范围：** [0, 100]。 **默认取值：** 不涉及。
        :type weight: int
        :param priority: **参数解释：** 服务优先级。 **约束限制：** 不涉及。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。
        :type priority: int
        :param secret_type: **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 不涉及。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。
        :type secret_type: str
        :param secret_name: **参数解释：** 凭证名称，用户使用dew类型凭证时可以在此处选择使用的凭证。 **取值范围：** 1-64个字符，只能包含字母、数字、连字符和下划线。
        :type secret_name: str
        :param status: **参数解释：** 服务部署状态
        :type status: str
        :param deploy_type: **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。
        :type deploy_type: str
        :param workload_type: **参数解释：** 工作负载类型。 **取值范围：** - LWS - DEPLOYMENT **默认取值：** DEPLOYMENT
        :type workload_type: str
        :param high_avail_switch: **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。 **约束限制：** 不涉及 **取值范围：** - true: 高可用开启。 - false: 高可用关闭。
        :type high_avail_switch: bool
        :param system_log_dump_enable: **参数解释：** 系统日志转储开关。 **约束限制：** 只有NPU资源池有，且逻辑池是没有的 **取值范围：** 不涉及 **默认取值：** false
        :type system_log_dump_enable: bool
        :param schedule_strategy: **参数解释：** 调度策略。 **取值范围：** 不涉及。
        :type schedule_strategy: str
        :param unit_configs: **参数解释：** 实例单元配置。 **约束限制：** 单机推理时，个数只会为1；如果是分布式推理时，根据不同框架，实例单元配置可灵活配置。
        :type unit_configs: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfig`]
        :param model: 
        :type model: :class:`huaweicloudsdkmodelarts.v1.GroupModel`
        :param advanced_config: 
        :type advanced_config: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        :param mirror_traffic_enable: **参数解释：** 是否开启镜像流量。 **取值范围：** 不涉及。
        :type mirror_traffic_enable: bool
        :param mirror_traffic_weight: **参数解释：** 镜像流量权重。 **取值范围：** 不涉及。
        :type mirror_traffic_weight: int
        :param user_name: **参数解释：** 用户名。 **取值范围：** 不涉及。
        :type user_name: str
        :param agency_name: **参数解释：** 委托名称。 **取值范围：** 不涉及。
        :type agency_name: str
        :param last_used_time: **参数解释：** 最后使用时间。 **取值范围：** 不涉及。
        :type last_used_time: datetime
        :param deployment_task_limit: 
        :type deployment_task_limit: :class:`huaweicloudsdkmodelarts.v1.DeploymentTaskLimit`
        :param frozen_infos: **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。
        :type frozen_infos: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        :param create_at: **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字
        :type create_at: datetime
        :param update_at: **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。
        :type update_at: datetime
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._deployment_name = None
        self._infer_name = None
        self._description = None
        self._pool_id = None
        self._framework = None
        self._version = None
        self._version_id = None
        self._version_count = None
        self._count = None
        self._weight = None
        self._priority = None
        self._secret_type = None
        self._secret_name = None
        self._status = None
        self._deploy_type = None
        self._workload_type = None
        self._high_avail_switch = None
        self._system_log_dump_enable = None
        self._schedule_strategy = None
        self._unit_configs = None
        self._model = None
        self._advanced_config = None
        self._mirror_traffic_enable = None
        self._mirror_traffic_weight = None
        self._user_name = None
        self._agency_name = None
        self._last_used_time = None
        self._deployment_task_limit = None
        self._frozen_infos = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if deployment_name is not None:
            self.deployment_name = deployment_name
        if infer_name is not None:
            self.infer_name = infer_name
        if description is not None:
            self.description = description
        if pool_id is not None:
            self.pool_id = pool_id
        if framework is not None:
            self.framework = framework
        if version is not None:
            self.version = version
        if version_id is not None:
            self.version_id = version_id
        if version_count is not None:
            self.version_count = version_count
        if count is not None:
            self.count = count
        if weight is not None:
            self.weight = weight
        if priority is not None:
            self.priority = priority
        if secret_type is not None:
            self.secret_type = secret_type
        if secret_name is not None:
            self.secret_name = secret_name
        if status is not None:
            self.status = status
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if workload_type is not None:
            self.workload_type = workload_type
        if high_avail_switch is not None:
            self.high_avail_switch = high_avail_switch
        if system_log_dump_enable is not None:
            self.system_log_dump_enable = system_log_dump_enable
        if schedule_strategy is not None:
            self.schedule_strategy = schedule_strategy
        if unit_configs is not None:
            self.unit_configs = unit_configs
        if model is not None:
            self.model = model
        if advanced_config is not None:
            self.advanced_config = advanced_config
        if mirror_traffic_enable is not None:
            self.mirror_traffic_enable = mirror_traffic_enable
        if mirror_traffic_weight is not None:
            self.mirror_traffic_weight = mirror_traffic_weight
        if user_name is not None:
            self.user_name = user_name
        if agency_name is not None:
            self.agency_name = agency_name
        if last_used_time is not None:
            self.last_used_time = last_used_time
        if deployment_task_limit is not None:
            self.deployment_task_limit = deployment_task_limit
        if frozen_infos is not None:
            self.frozen_infos = frozen_infos
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this UpdateInferDeploymentResponse.

        参数解释： 部署ID，在[添加部署](CreateInferDeployment.xml)时即可在返回体中获取，也可通过[查询服务部署列表](ListInferDeployments.xml)获取当前用户拥有的部署，其中deployment_id字段即为部署ID。 约束限制： 不涉及。 取值范围： 部署ID。 默认取值： 不涉及。

        :return: The id of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateInferDeploymentResponse.

        参数解释： 部署ID，在[添加部署](CreateInferDeployment.xml)时即可在返回体中获取，也可通过[查询服务部署列表](ListInferDeployments.xml)获取当前用户拥有的部署，其中deployment_id字段即为部署ID。 约束限制： 不涉及。 取值范围： 部署ID。 默认取值： 不涉及。

        :param id: The id of this UpdateInferDeploymentResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateInferDeploymentResponse.

        **参数解释：** 服务部署名字

        :return: The name of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateInferDeploymentResponse.

        **参数解释：** 服务部署名字

        :param name: The name of this UpdateInferDeploymentResponse.
        :type name: str
        """
        self._name = name

    @property
    def deployment_name(self):
        r"""Gets the deployment_name of this UpdateInferDeploymentResponse.

        参数解释： 服务部署名字。

        :return: The deployment_name of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        r"""Sets the deployment_name of this UpdateInferDeploymentResponse.

        参数解释： 服务部署名字。

        :param deployment_name: The deployment_name of this UpdateInferDeploymentResponse.
        :type deployment_name: str
        """
        self._deployment_name = deployment_name

    @property
    def infer_name(self):
        r"""Gets the infer_name of this UpdateInferDeploymentResponse.

        参数解释： 部署id（废弃字段）。 取值范围： 不涉及。

        :return: The infer_name of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._infer_name

    @infer_name.setter
    def infer_name(self, infer_name):
        r"""Sets the infer_name of this UpdateInferDeploymentResponse.

        参数解释： 部署id（废弃字段）。 取值范围： 不涉及。

        :param infer_name: The infer_name of this UpdateInferDeploymentResponse.
        :type infer_name: str
        """
        self._infer_name = infer_name

    @property
    def description(self):
        r"""Gets the description of this UpdateInferDeploymentResponse.

        参数解释： 描述 取值范围： 不涉及。

        :return: The description of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateInferDeploymentResponse.

        参数解释： 描述 取值范围： 不涉及。

        :param description: The description of this UpdateInferDeploymentResponse.
        :type description: str
        """
        self._description = description

    @property
    def pool_id(self):
        r"""Gets the pool_id of this UpdateInferDeploymentResponse.

        **参数解释：** 专属资源池ID。 **取值范围：** 不涉及。

        :return: The pool_id of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this UpdateInferDeploymentResponse.

        **参数解释：** 专属资源池ID。 **取值范围：** 不涉及。

        :param pool_id: The pool_id of this UpdateInferDeploymentResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def framework(self):
        r"""Gets the framework of this UpdateInferDeploymentResponse.

        **参数解释：** 算法框架。 **取值范围：** - COMMON： 普通在线服务。

        :return: The framework of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        r"""Sets the framework of this UpdateInferDeploymentResponse.

        **参数解释：** 算法框架。 **取值范围：** - COMMON： 普通在线服务。

        :param framework: The framework of this UpdateInferDeploymentResponse.
        :type framework: str
        """
        self._framework = framework

    @property
    def version(self):
        r"""Gets the version of this UpdateInferDeploymentResponse.

        **参数解释：** 当前部署版本信息。

        :return: The version of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateInferDeploymentResponse.

        **参数解释：** 当前部署版本信息。

        :param version: The version of this UpdateInferDeploymentResponse.
        :type version: str
        """
        self._version = version

    @property
    def version_id(self):
        r"""Gets the version_id of this UpdateInferDeploymentResponse.

        **参数解释：** 版本id，可通过查询version列表查询。 **取值范围：** 不涉及。

        :return: The version_id of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this UpdateInferDeploymentResponse.

        **参数解释：** 版本id，可通过查询version列表查询。 **取值范围：** 不涉及。

        :param version_id: The version_id of this UpdateInferDeploymentResponse.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def version_count(self):
        r"""Gets the version_count of this UpdateInferDeploymentResponse.

        **参数解释：** 服务版本数量。 **取值范围：** 不涉及。

        :return: The version_count of this UpdateInferDeploymentResponse.
        :rtype: int
        """
        return self._version_count

    @version_count.setter
    def version_count(self, version_count):
        r"""Sets the version_count of this UpdateInferDeploymentResponse.

        **参数解释：** 服务版本数量。 **取值范围：** 不涉及。

        :param version_count: The version_count of this UpdateInferDeploymentResponse.
        :type version_count: int
        """
        self._version_count = version_count

    @property
    def count(self):
        r"""Gets the count of this UpdateInferDeploymentResponse.

        **参数解释：** 服务部署实例数。

        :return: The count of this UpdateInferDeploymentResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this UpdateInferDeploymentResponse.

        **参数解释：** 服务部署实例数。

        :param count: The count of this UpdateInferDeploymentResponse.
        :type count: int
        """
        self._count = count

    @property
    def weight(self):
        r"""Gets the weight of this UpdateInferDeploymentResponse.

        **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **约束限制：** 不涉及。 **取值范围：** [0, 100]。 **默认取值：** 不涉及。

        :return: The weight of this UpdateInferDeploymentResponse.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this UpdateInferDeploymentResponse.

        **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **约束限制：** 不涉及。 **取值范围：** [0, 100]。 **默认取值：** 不涉及。

        :param weight: The weight of this UpdateInferDeploymentResponse.
        :type weight: int
        """
        self._weight = weight

    @property
    def priority(self):
        r"""Gets the priority of this UpdateInferDeploymentResponse.

        **参数解释：** 服务优先级。 **约束限制：** 不涉及。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。

        :return: The priority of this UpdateInferDeploymentResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this UpdateInferDeploymentResponse.

        **参数解释：** 服务优先级。 **约束限制：** 不涉及。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。

        :param priority: The priority of this UpdateInferDeploymentResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def secret_type(self):
        r"""Gets the secret_type of this UpdateInferDeploymentResponse.

        **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 不涉及。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。

        :return: The secret_type of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._secret_type

    @secret_type.setter
    def secret_type(self, secret_type):
        r"""Sets the secret_type of this UpdateInferDeploymentResponse.

        **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 不涉及。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。

        :param secret_type: The secret_type of this UpdateInferDeploymentResponse.
        :type secret_type: str
        """
        self._secret_type = secret_type

    @property
    def secret_name(self):
        r"""Gets the secret_name of this UpdateInferDeploymentResponse.

        **参数解释：** 凭证名称，用户使用dew类型凭证时可以在此处选择使用的凭证。 **取值范围：** 1-64个字符，只能包含字母、数字、连字符和下划线。

        :return: The secret_name of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        r"""Sets the secret_name of this UpdateInferDeploymentResponse.

        **参数解释：** 凭证名称，用户使用dew类型凭证时可以在此处选择使用的凭证。 **取值范围：** 1-64个字符，只能包含字母、数字、连字符和下划线。

        :param secret_name: The secret_name of this UpdateInferDeploymentResponse.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def status(self):
        r"""Gets the status of this UpdateInferDeploymentResponse.

        **参数解释：** 服务部署状态

        :return: The status of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateInferDeploymentResponse.

        **参数解释：** 服务部署状态

        :param status: The status of this UpdateInferDeploymentResponse.
        :type status: str
        """
        self._status = status

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this UpdateInferDeploymentResponse.

        **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。

        :return: The deploy_type of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this UpdateInferDeploymentResponse.

        **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。

        :param deploy_type: The deploy_type of this UpdateInferDeploymentResponse.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def workload_type(self):
        r"""Gets the workload_type of this UpdateInferDeploymentResponse.

        **参数解释：** 工作负载类型。 **取值范围：** - LWS - DEPLOYMENT **默认取值：** DEPLOYMENT

        :return: The workload_type of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        r"""Sets the workload_type of this UpdateInferDeploymentResponse.

        **参数解释：** 工作负载类型。 **取值范围：** - LWS - DEPLOYMENT **默认取值：** DEPLOYMENT

        :param workload_type: The workload_type of this UpdateInferDeploymentResponse.
        :type workload_type: str
        """
        self._workload_type = workload_type

    @property
    def high_avail_switch(self):
        r"""Gets the high_avail_switch of this UpdateInferDeploymentResponse.

        **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。 **约束限制：** 不涉及 **取值范围：** - true: 高可用开启。 - false: 高可用关闭。

        :return: The high_avail_switch of this UpdateInferDeploymentResponse.
        :rtype: bool
        """
        return self._high_avail_switch

    @high_avail_switch.setter
    def high_avail_switch(self, high_avail_switch):
        r"""Sets the high_avail_switch of this UpdateInferDeploymentResponse.

        **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。 **约束限制：** 不涉及 **取值范围：** - true: 高可用开启。 - false: 高可用关闭。

        :param high_avail_switch: The high_avail_switch of this UpdateInferDeploymentResponse.
        :type high_avail_switch: bool
        """
        self._high_avail_switch = high_avail_switch

    @property
    def system_log_dump_enable(self):
        r"""Gets the system_log_dump_enable of this UpdateInferDeploymentResponse.

        **参数解释：** 系统日志转储开关。 **约束限制：** 只有NPU资源池有，且逻辑池是没有的 **取值范围：** 不涉及 **默认取值：** false

        :return: The system_log_dump_enable of this UpdateInferDeploymentResponse.
        :rtype: bool
        """
        return self._system_log_dump_enable

    @system_log_dump_enable.setter
    def system_log_dump_enable(self, system_log_dump_enable):
        r"""Sets the system_log_dump_enable of this UpdateInferDeploymentResponse.

        **参数解释：** 系统日志转储开关。 **约束限制：** 只有NPU资源池有，且逻辑池是没有的 **取值范围：** 不涉及 **默认取值：** false

        :param system_log_dump_enable: The system_log_dump_enable of this UpdateInferDeploymentResponse.
        :type system_log_dump_enable: bool
        """
        self._system_log_dump_enable = system_log_dump_enable

    @property
    def schedule_strategy(self):
        r"""Gets the schedule_strategy of this UpdateInferDeploymentResponse.

        **参数解释：** 调度策略。 **取值范围：** 不涉及。

        :return: The schedule_strategy of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._schedule_strategy

    @schedule_strategy.setter
    def schedule_strategy(self, schedule_strategy):
        r"""Sets the schedule_strategy of this UpdateInferDeploymentResponse.

        **参数解释：** 调度策略。 **取值范围：** 不涉及。

        :param schedule_strategy: The schedule_strategy of this UpdateInferDeploymentResponse.
        :type schedule_strategy: str
        """
        self._schedule_strategy = schedule_strategy

    @property
    def unit_configs(self):
        r"""Gets the unit_configs of this UpdateInferDeploymentResponse.

        **参数解释：** 实例单元配置。 **约束限制：** 单机推理时，个数只会为1；如果是分布式推理时，根据不同框架，实例单元配置可灵活配置。

        :return: The unit_configs of this UpdateInferDeploymentResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfig`]
        """
        return self._unit_configs

    @unit_configs.setter
    def unit_configs(self, unit_configs):
        r"""Sets the unit_configs of this UpdateInferDeploymentResponse.

        **参数解释：** 实例单元配置。 **约束限制：** 单机推理时，个数只会为1；如果是分布式推理时，根据不同框架，实例单元配置可灵活配置。

        :param unit_configs: The unit_configs of this UpdateInferDeploymentResponse.
        :type unit_configs: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfig`]
        """
        self._unit_configs = unit_configs

    @property
    def model(self):
        r"""Gets the model of this UpdateInferDeploymentResponse.

        :return: The model of this UpdateInferDeploymentResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GroupModel`
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this UpdateInferDeploymentResponse.

        :param model: The model of this UpdateInferDeploymentResponse.
        :type model: :class:`huaweicloudsdkmodelarts.v1.GroupModel`
        """
        self._model = model

    @property
    def advanced_config(self):
        r"""Gets the advanced_config of this UpdateInferDeploymentResponse.

        :return: The advanced_config of this UpdateInferDeploymentResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        """
        return self._advanced_config

    @advanced_config.setter
    def advanced_config(self, advanced_config):
        r"""Sets the advanced_config of this UpdateInferDeploymentResponse.

        :param advanced_config: The advanced_config of this UpdateInferDeploymentResponse.
        :type advanced_config: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        """
        self._advanced_config = advanced_config

    @property
    def mirror_traffic_enable(self):
        r"""Gets the mirror_traffic_enable of this UpdateInferDeploymentResponse.

        **参数解释：** 是否开启镜像流量。 **取值范围：** 不涉及。

        :return: The mirror_traffic_enable of this UpdateInferDeploymentResponse.
        :rtype: bool
        """
        return self._mirror_traffic_enable

    @mirror_traffic_enable.setter
    def mirror_traffic_enable(self, mirror_traffic_enable):
        r"""Sets the mirror_traffic_enable of this UpdateInferDeploymentResponse.

        **参数解释：** 是否开启镜像流量。 **取值范围：** 不涉及。

        :param mirror_traffic_enable: The mirror_traffic_enable of this UpdateInferDeploymentResponse.
        :type mirror_traffic_enable: bool
        """
        self._mirror_traffic_enable = mirror_traffic_enable

    @property
    def mirror_traffic_weight(self):
        r"""Gets the mirror_traffic_weight of this UpdateInferDeploymentResponse.

        **参数解释：** 镜像流量权重。 **取值范围：** 不涉及。

        :return: The mirror_traffic_weight of this UpdateInferDeploymentResponse.
        :rtype: int
        """
        return self._mirror_traffic_weight

    @mirror_traffic_weight.setter
    def mirror_traffic_weight(self, mirror_traffic_weight):
        r"""Sets the mirror_traffic_weight of this UpdateInferDeploymentResponse.

        **参数解释：** 镜像流量权重。 **取值范围：** 不涉及。

        :param mirror_traffic_weight: The mirror_traffic_weight of this UpdateInferDeploymentResponse.
        :type mirror_traffic_weight: int
        """
        self._mirror_traffic_weight = mirror_traffic_weight

    @property
    def user_name(self):
        r"""Gets the user_name of this UpdateInferDeploymentResponse.

        **参数解释：** 用户名。 **取值范围：** 不涉及。

        :return: The user_name of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this UpdateInferDeploymentResponse.

        **参数解释：** 用户名。 **取值范围：** 不涉及。

        :param user_name: The user_name of this UpdateInferDeploymentResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this UpdateInferDeploymentResponse.

        **参数解释：** 委托名称。 **取值范围：** 不涉及。

        :return: The agency_name of this UpdateInferDeploymentResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this UpdateInferDeploymentResponse.

        **参数解释：** 委托名称。 **取值范围：** 不涉及。

        :param agency_name: The agency_name of this UpdateInferDeploymentResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def last_used_time(self):
        r"""Gets the last_used_time of this UpdateInferDeploymentResponse.

        **参数解释：** 最后使用时间。 **取值范围：** 不涉及。

        :return: The last_used_time of this UpdateInferDeploymentResponse.
        :rtype: datetime
        """
        return self._last_used_time

    @last_used_time.setter
    def last_used_time(self, last_used_time):
        r"""Sets the last_used_time of this UpdateInferDeploymentResponse.

        **参数解释：** 最后使用时间。 **取值范围：** 不涉及。

        :param last_used_time: The last_used_time of this UpdateInferDeploymentResponse.
        :type last_used_time: datetime
        """
        self._last_used_time = last_used_time

    @property
    def deployment_task_limit(self):
        r"""Gets the deployment_task_limit of this UpdateInferDeploymentResponse.

        :return: The deployment_task_limit of this UpdateInferDeploymentResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeploymentTaskLimit`
        """
        return self._deployment_task_limit

    @deployment_task_limit.setter
    def deployment_task_limit(self, deployment_task_limit):
        r"""Sets the deployment_task_limit of this UpdateInferDeploymentResponse.

        :param deployment_task_limit: The deployment_task_limit of this UpdateInferDeploymentResponse.
        :type deployment_task_limit: :class:`huaweicloudsdkmodelarts.v1.DeploymentTaskLimit`
        """
        self._deployment_task_limit = deployment_task_limit

    @property
    def frozen_infos(self):
        r"""Gets the frozen_infos of this UpdateInferDeploymentResponse.

        **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。

        :return: The frozen_infos of this UpdateInferDeploymentResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        return self._frozen_infos

    @frozen_infos.setter
    def frozen_infos(self, frozen_infos):
        r"""Sets the frozen_infos of this UpdateInferDeploymentResponse.

        **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。

        :param frozen_infos: The frozen_infos of this UpdateInferDeploymentResponse.
        :type frozen_infos: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        self._frozen_infos = frozen_infos

    @property
    def create_at(self):
        r"""Gets the create_at of this UpdateInferDeploymentResponse.

        **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字

        :return: The create_at of this UpdateInferDeploymentResponse.
        :rtype: datetime
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this UpdateInferDeploymentResponse.

        **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字

        :param create_at: The create_at of this UpdateInferDeploymentResponse.
        :type create_at: datetime
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this UpdateInferDeploymentResponse.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :return: The update_at of this UpdateInferDeploymentResponse.
        :rtype: datetime
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this UpdateInferDeploymentResponse.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :param update_at: The update_at of this UpdateInferDeploymentResponse.
        :type update_at: datetime
        """
        self._update_at = update_at

    def to_dict(self):
        import warnings
        warnings.warn("UpdateInferDeploymentResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UpdateInferDeploymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
