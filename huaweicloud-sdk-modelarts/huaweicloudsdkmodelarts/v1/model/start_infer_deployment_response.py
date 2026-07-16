# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartInferDeploymentResponse(SdkResponse):

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
        'pool_id': 'str',
        'count': 'int',
        'system_log_dump_enable': 'bool',
        'unit_configs': 'list[UnitConfigResponse]',
        'weight': 'int',
        'traffic_ratio': 'str',
        'secret_type': 'str',
        'secret_name': 'str',
        'priority': 'int',
        'high_avail_switch': 'bool',
        'framework': 'str',
        'version': 'str',
        'version_id': 'str',
        'status': 'str',
        'running_count': 'int',
        'deploy_type': 'str',
        'mirror_traffic_enable': 'bool',
        'mirror_traffic_weight': 'str',
        'version_count': 'int',
        'workload_type': 'str',
        'update_at': 'int',
        'lts_state': 'str',
        'infer_name': 'str',
        'model': 'InferModelResponse',
        'advanced_config': 'AdvancedConfig',
        'description': 'str',
        'create_at': 'str',
        'schedule_strategy': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'pool_id': 'pool_id',
        'count': 'count',
        'system_log_dump_enable': 'system_log_dump_enable',
        'unit_configs': 'unit_configs',
        'weight': 'weight',
        'traffic_ratio': 'traffic_ratio',
        'secret_type': 'secret_type',
        'secret_name': 'secret_name',
        'priority': 'priority',
        'high_avail_switch': 'high_avail_switch',
        'framework': 'framework',
        'version': 'version',
        'version_id': 'version_id',
        'status': 'status',
        'running_count': 'running_count',
        'deploy_type': 'deploy_type',
        'mirror_traffic_enable': 'mirror_traffic_enable',
        'mirror_traffic_weight': 'mirror_traffic_weight',
        'version_count': 'version_count',
        'workload_type': 'workload_type',
        'update_at': 'update_at',
        'lts_state': 'lts_state',
        'infer_name': 'infer_name',
        'model': 'model',
        'advanced_config': 'advanced_config',
        'description': 'description',
        'create_at': 'create_at',
        'schedule_strategy': 'schedule_strategy'
    }

    def __init__(self, id=None, name=None, pool_id=None, count=None, system_log_dump_enable=None, unit_configs=None, weight=None, traffic_ratio=None, secret_type=None, secret_name=None, priority=None, high_avail_switch=None, framework=None, version=None, version_id=None, status=None, running_count=None, deploy_type=None, mirror_traffic_enable=None, mirror_traffic_weight=None, version_count=None, workload_type=None, update_at=None, lts_state=None, infer_name=None, model=None, advanced_config=None, description=None, create_at=None, schedule_strategy=None):
        r"""StartInferDeploymentResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 部署ID。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 部署名称。 **取值范围：** 不涉及。
        :type name: str
        :param pool_id: **参数解释：** 资源池ID，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **取值范围：** 不涉及。
        :type pool_id: str
        :param count: **参数解释：** 部署场景下，服务实例数量。 **约束限制：** 不涉及。 **取值范围：** [1, 128]。 **默认取值：** 不涉及。
        :type count: int
        :param system_log_dump_enable: **参数解释：** 系统日志转储开关。 **约束限制：** 只有NPU资源池有，且逻辑池是没有的。 **取值范围：** 不涉及。 **默认取值：** false。
        :type system_log_dump_enable: bool
        :param unit_configs: **参数解释：** 推理单元配置。
        :type unit_configs: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfigResponse`]
        :param weight: **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **取值范围：** [0, 100]。
        :type weight: int
        :param traffic_ratio: **参数解释：** 流量比例，单个部署实例预期接收用户的流量与总流量比值，是由流量权重配置和部署状态计算所得的值。 **取值范围：** 0.00%~100.00%。
        :type traffic_ratio: str
        :param secret_type: **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 不涉及。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。
        :type secret_type: str
        :param secret_name: **参数解释：** 凭证名称，用户使用dew类型凭证时可以在此处选择使用的凭证。 **约束限制：** 不涉及。
        :type secret_name: str
        :param priority: **参数解释：** 服务优先级。 **约束限制：** 不涉及。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。
        :type priority: int
        :param high_avail_switch: **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。（准备下线，请使用schedule_strategy字段） **取值范围：** - true: 高可用开启 - false: 高可用关闭。
        :type high_avail_switch: bool
        :param framework: **参数解释：** 算法框架。 **取值范围：** - COMMON： 普通在线服务。
        :type framework: str
        :param version: **参数解释：** 服务版本号，以数字及点号组成，形如1.0.1。 **约束限制：** 不涉及。 **取值范围：** 1.0.0 ~ 99.99.99，长度不超过8位。 **默认取值：** 不涉及。
        :type version: str
        :param version_id: **参数解释：** 版本id，可通过查询version列表查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type version_id: str
        :param status: **参数解释：** 服务当前状态。 **取值范围：** - DEPLOYING：部署中。 - FAILED：失败。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中。 - STOPPING：停止中。 - CONCERNING：告警。 - DELETED: 已删除。 - RESTARTING: 重启中。 - UPGRADING：升级中。 - ERROR：异常。 - INTERRUPTING：中断中。
        :type status: str
        :param running_count: **参数解释：** 部署场景下，服务运行实例数量。 **约束限制：** 不涉及。 **取值范围：** [1, 128]。 **默认取值：** 不涉及。
        :type running_count: int
        :param deploy_type: **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。
        :type deploy_type: str
        :param mirror_traffic_enable: **参数解释：** 是否开启镜像流量。 **取值范围：** 不涉及。
        :type mirror_traffic_enable: bool
        :param mirror_traffic_weight: **参数解释：** 镜像流量权重。 **取值范围：** 50。
        :type mirror_traffic_weight: str
        :param version_count: **参数解释：** 服务版本数量。 **取值范围：** 不涉及。
        :type version_count: int
        :param workload_type: **参数解释：** 工作负载类型。 **取值范围：** 不涉及。
        :type workload_type: str
        :param update_at: **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。
        :type update_at: int
        :param lts_state: **参数解释：** 部署对接lts状态。 **取值范围：** - ON：开启。 - OFF：关闭。
        :type lts_state: str
        :param infer_name: **参数解释：** 部署ID。
        :type infer_name: str
        :param model: 
        :type model: :class:`huaweicloudsdkmodelarts.v1.InferModelResponse`
        :param advanced_config: 
        :type advanced_config: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        :param description: **参数解释：** 部署描述。
        :type description: str
        :param create_at: 参数解释： 创建时间，根据创建时的当前时间自动生成。 取值范围： 毫秒级时间戳，13位数字，如1609459200000。
        :type create_at: str
        :param schedule_strategy: **参数解释：** 调度策略。 **取值范围：** - HIGH_AVAILABILITY：高可用调度 - HIGH_UTILIZATION：紧凑调度 - HIGH_PERFORMANCE：高性能调度
        :type schedule_strategy: str
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._pool_id = None
        self._count = None
        self._system_log_dump_enable = None
        self._unit_configs = None
        self._weight = None
        self._traffic_ratio = None
        self._secret_type = None
        self._secret_name = None
        self._priority = None
        self._high_avail_switch = None
        self._framework = None
        self._version = None
        self._version_id = None
        self._status = None
        self._running_count = None
        self._deploy_type = None
        self._mirror_traffic_enable = None
        self._mirror_traffic_weight = None
        self._version_count = None
        self._workload_type = None
        self._update_at = None
        self._lts_state = None
        self._infer_name = None
        self._model = None
        self._advanced_config = None
        self._description = None
        self._create_at = None
        self._schedule_strategy = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if pool_id is not None:
            self.pool_id = pool_id
        if count is not None:
            self.count = count
        if system_log_dump_enable is not None:
            self.system_log_dump_enable = system_log_dump_enable
        if unit_configs is not None:
            self.unit_configs = unit_configs
        if weight is not None:
            self.weight = weight
        if traffic_ratio is not None:
            self.traffic_ratio = traffic_ratio
        if secret_type is not None:
            self.secret_type = secret_type
        if secret_name is not None:
            self.secret_name = secret_name
        if priority is not None:
            self.priority = priority
        if high_avail_switch is not None:
            self.high_avail_switch = high_avail_switch
        if framework is not None:
            self.framework = framework
        if version is not None:
            self.version = version
        if version_id is not None:
            self.version_id = version_id
        if status is not None:
            self.status = status
        if running_count is not None:
            self.running_count = running_count
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if mirror_traffic_enable is not None:
            self.mirror_traffic_enable = mirror_traffic_enable
        if mirror_traffic_weight is not None:
            self.mirror_traffic_weight = mirror_traffic_weight
        if version_count is not None:
            self.version_count = version_count
        if workload_type is not None:
            self.workload_type = workload_type
        if update_at is not None:
            self.update_at = update_at
        if lts_state is not None:
            self.lts_state = lts_state
        if infer_name is not None:
            self.infer_name = infer_name
        if model is not None:
            self.model = model
        if advanced_config is not None:
            self.advanced_config = advanced_config
        if description is not None:
            self.description = description
        if create_at is not None:
            self.create_at = create_at
        if schedule_strategy is not None:
            self.schedule_strategy = schedule_strategy

    @property
    def id(self):
        r"""Gets the id of this StartInferDeploymentResponse.

        **参数解释：** 部署ID。 **取值范围：** 不涉及。

        :return: The id of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this StartInferDeploymentResponse.

        **参数解释：** 部署ID。 **取值范围：** 不涉及。

        :param id: The id of this StartInferDeploymentResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this StartInferDeploymentResponse.

        **参数解释：** 部署名称。 **取值范围：** 不涉及。

        :return: The name of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StartInferDeploymentResponse.

        **参数解释：** 部署名称。 **取值范围：** 不涉及。

        :param name: The name of this StartInferDeploymentResponse.
        :type name: str
        """
        self._name = name

    @property
    def pool_id(self):
        r"""Gets the pool_id of this StartInferDeploymentResponse.

        **参数解释：** 资源池ID，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **取值范围：** 不涉及。

        :return: The pool_id of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this StartInferDeploymentResponse.

        **参数解释：** 资源池ID，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **取值范围：** 不涉及。

        :param pool_id: The pool_id of this StartInferDeploymentResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def count(self):
        r"""Gets the count of this StartInferDeploymentResponse.

        **参数解释：** 部署场景下，服务实例数量。 **约束限制：** 不涉及。 **取值范围：** [1, 128]。 **默认取值：** 不涉及。

        :return: The count of this StartInferDeploymentResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this StartInferDeploymentResponse.

        **参数解释：** 部署场景下，服务实例数量。 **约束限制：** 不涉及。 **取值范围：** [1, 128]。 **默认取值：** 不涉及。

        :param count: The count of this StartInferDeploymentResponse.
        :type count: int
        """
        self._count = count

    @property
    def system_log_dump_enable(self):
        r"""Gets the system_log_dump_enable of this StartInferDeploymentResponse.

        **参数解释：** 系统日志转储开关。 **约束限制：** 只有NPU资源池有，且逻辑池是没有的。 **取值范围：** 不涉及。 **默认取值：** false。

        :return: The system_log_dump_enable of this StartInferDeploymentResponse.
        :rtype: bool
        """
        return self._system_log_dump_enable

    @system_log_dump_enable.setter
    def system_log_dump_enable(self, system_log_dump_enable):
        r"""Sets the system_log_dump_enable of this StartInferDeploymentResponse.

        **参数解释：** 系统日志转储开关。 **约束限制：** 只有NPU资源池有，且逻辑池是没有的。 **取值范围：** 不涉及。 **默认取值：** false。

        :param system_log_dump_enable: The system_log_dump_enable of this StartInferDeploymentResponse.
        :type system_log_dump_enable: bool
        """
        self._system_log_dump_enable = system_log_dump_enable

    @property
    def unit_configs(self):
        r"""Gets the unit_configs of this StartInferDeploymentResponse.

        **参数解释：** 推理单元配置。

        :return: The unit_configs of this StartInferDeploymentResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfigResponse`]
        """
        return self._unit_configs

    @unit_configs.setter
    def unit_configs(self, unit_configs):
        r"""Sets the unit_configs of this StartInferDeploymentResponse.

        **参数解释：** 推理单元配置。

        :param unit_configs: The unit_configs of this StartInferDeploymentResponse.
        :type unit_configs: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfigResponse`]
        """
        self._unit_configs = unit_configs

    @property
    def weight(self):
        r"""Gets the weight of this StartInferDeploymentResponse.

        **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **取值范围：** [0, 100]。

        :return: The weight of this StartInferDeploymentResponse.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this StartInferDeploymentResponse.

        **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **取值范围：** [0, 100]。

        :param weight: The weight of this StartInferDeploymentResponse.
        :type weight: int
        """
        self._weight = weight

    @property
    def traffic_ratio(self):
        r"""Gets the traffic_ratio of this StartInferDeploymentResponse.

        **参数解释：** 流量比例，单个部署实例预期接收用户的流量与总流量比值，是由流量权重配置和部署状态计算所得的值。 **取值范围：** 0.00%~100.00%。

        :return: The traffic_ratio of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._traffic_ratio

    @traffic_ratio.setter
    def traffic_ratio(self, traffic_ratio):
        r"""Sets the traffic_ratio of this StartInferDeploymentResponse.

        **参数解释：** 流量比例，单个部署实例预期接收用户的流量与总流量比值，是由流量权重配置和部署状态计算所得的值。 **取值范围：** 0.00%~100.00%。

        :param traffic_ratio: The traffic_ratio of this StartInferDeploymentResponse.
        :type traffic_ratio: str
        """
        self._traffic_ratio = traffic_ratio

    @property
    def secret_type(self):
        r"""Gets the secret_type of this StartInferDeploymentResponse.

        **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 不涉及。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。

        :return: The secret_type of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._secret_type

    @secret_type.setter
    def secret_type(self, secret_type):
        r"""Sets the secret_type of this StartInferDeploymentResponse.

        **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 不涉及。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。

        :param secret_type: The secret_type of this StartInferDeploymentResponse.
        :type secret_type: str
        """
        self._secret_type = secret_type

    @property
    def secret_name(self):
        r"""Gets the secret_name of this StartInferDeploymentResponse.

        **参数解释：** 凭证名称，用户使用dew类型凭证时可以在此处选择使用的凭证。 **约束限制：** 不涉及。

        :return: The secret_name of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        r"""Sets the secret_name of this StartInferDeploymentResponse.

        **参数解释：** 凭证名称，用户使用dew类型凭证时可以在此处选择使用的凭证。 **约束限制：** 不涉及。

        :param secret_name: The secret_name of this StartInferDeploymentResponse.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def priority(self):
        r"""Gets the priority of this StartInferDeploymentResponse.

        **参数解释：** 服务优先级。 **约束限制：** 不涉及。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。

        :return: The priority of this StartInferDeploymentResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this StartInferDeploymentResponse.

        **参数解释：** 服务优先级。 **约束限制：** 不涉及。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。

        :param priority: The priority of this StartInferDeploymentResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def high_avail_switch(self):
        r"""Gets the high_avail_switch of this StartInferDeploymentResponse.

        **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。（准备下线，请使用schedule_strategy字段） **取值范围：** - true: 高可用开启 - false: 高可用关闭。

        :return: The high_avail_switch of this StartInferDeploymentResponse.
        :rtype: bool
        """
        return self._high_avail_switch

    @high_avail_switch.setter
    def high_avail_switch(self, high_avail_switch):
        r"""Sets the high_avail_switch of this StartInferDeploymentResponse.

        **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。（准备下线，请使用schedule_strategy字段） **取值范围：** - true: 高可用开启 - false: 高可用关闭。

        :param high_avail_switch: The high_avail_switch of this StartInferDeploymentResponse.
        :type high_avail_switch: bool
        """
        self._high_avail_switch = high_avail_switch

    @property
    def framework(self):
        r"""Gets the framework of this StartInferDeploymentResponse.

        **参数解释：** 算法框架。 **取值范围：** - COMMON： 普通在线服务。

        :return: The framework of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        r"""Sets the framework of this StartInferDeploymentResponse.

        **参数解释：** 算法框架。 **取值范围：** - COMMON： 普通在线服务。

        :param framework: The framework of this StartInferDeploymentResponse.
        :type framework: str
        """
        self._framework = framework

    @property
    def version(self):
        r"""Gets the version of this StartInferDeploymentResponse.

        **参数解释：** 服务版本号，以数字及点号组成，形如1.0.1。 **约束限制：** 不涉及。 **取值范围：** 1.0.0 ~ 99.99.99，长度不超过8位。 **默认取值：** 不涉及。

        :return: The version of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this StartInferDeploymentResponse.

        **参数解释：** 服务版本号，以数字及点号组成，形如1.0.1。 **约束限制：** 不涉及。 **取值范围：** 1.0.0 ~ 99.99.99，长度不超过8位。 **默认取值：** 不涉及。

        :param version: The version of this StartInferDeploymentResponse.
        :type version: str
        """
        self._version = version

    @property
    def version_id(self):
        r"""Gets the version_id of this StartInferDeploymentResponse.

        **参数解释：** 版本id，可通过查询version列表查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The version_id of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this StartInferDeploymentResponse.

        **参数解释：** 版本id，可通过查询version列表查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param version_id: The version_id of this StartInferDeploymentResponse.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def status(self):
        r"""Gets the status of this StartInferDeploymentResponse.

        **参数解释：** 服务当前状态。 **取值范围：** - DEPLOYING：部署中。 - FAILED：失败。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中。 - STOPPING：停止中。 - CONCERNING：告警。 - DELETED: 已删除。 - RESTARTING: 重启中。 - UPGRADING：升级中。 - ERROR：异常。 - INTERRUPTING：中断中。

        :return: The status of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StartInferDeploymentResponse.

        **参数解释：** 服务当前状态。 **取值范围：** - DEPLOYING：部署中。 - FAILED：失败。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中。 - STOPPING：停止中。 - CONCERNING：告警。 - DELETED: 已删除。 - RESTARTING: 重启中。 - UPGRADING：升级中。 - ERROR：异常。 - INTERRUPTING：中断中。

        :param status: The status of this StartInferDeploymentResponse.
        :type status: str
        """
        self._status = status

    @property
    def running_count(self):
        r"""Gets the running_count of this StartInferDeploymentResponse.

        **参数解释：** 部署场景下，服务运行实例数量。 **约束限制：** 不涉及。 **取值范围：** [1, 128]。 **默认取值：** 不涉及。

        :return: The running_count of this StartInferDeploymentResponse.
        :rtype: int
        """
        return self._running_count

    @running_count.setter
    def running_count(self, running_count):
        r"""Sets the running_count of this StartInferDeploymentResponse.

        **参数解释：** 部署场景下，服务运行实例数量。 **约束限制：** 不涉及。 **取值范围：** [1, 128]。 **默认取值：** 不涉及。

        :param running_count: The running_count of this StartInferDeploymentResponse.
        :type running_count: int
        """
        self._running_count = running_count

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this StartInferDeploymentResponse.

        **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。

        :return: The deploy_type of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this StartInferDeploymentResponse.

        **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。

        :param deploy_type: The deploy_type of this StartInferDeploymentResponse.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def mirror_traffic_enable(self):
        r"""Gets the mirror_traffic_enable of this StartInferDeploymentResponse.

        **参数解释：** 是否开启镜像流量。 **取值范围：** 不涉及。

        :return: The mirror_traffic_enable of this StartInferDeploymentResponse.
        :rtype: bool
        """
        return self._mirror_traffic_enable

    @mirror_traffic_enable.setter
    def mirror_traffic_enable(self, mirror_traffic_enable):
        r"""Sets the mirror_traffic_enable of this StartInferDeploymentResponse.

        **参数解释：** 是否开启镜像流量。 **取值范围：** 不涉及。

        :param mirror_traffic_enable: The mirror_traffic_enable of this StartInferDeploymentResponse.
        :type mirror_traffic_enable: bool
        """
        self._mirror_traffic_enable = mirror_traffic_enable

    @property
    def mirror_traffic_weight(self):
        r"""Gets the mirror_traffic_weight of this StartInferDeploymentResponse.

        **参数解释：** 镜像流量权重。 **取值范围：** 50。

        :return: The mirror_traffic_weight of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._mirror_traffic_weight

    @mirror_traffic_weight.setter
    def mirror_traffic_weight(self, mirror_traffic_weight):
        r"""Sets the mirror_traffic_weight of this StartInferDeploymentResponse.

        **参数解释：** 镜像流量权重。 **取值范围：** 50。

        :param mirror_traffic_weight: The mirror_traffic_weight of this StartInferDeploymentResponse.
        :type mirror_traffic_weight: str
        """
        self._mirror_traffic_weight = mirror_traffic_weight

    @property
    def version_count(self):
        r"""Gets the version_count of this StartInferDeploymentResponse.

        **参数解释：** 服务版本数量。 **取值范围：** 不涉及。

        :return: The version_count of this StartInferDeploymentResponse.
        :rtype: int
        """
        return self._version_count

    @version_count.setter
    def version_count(self, version_count):
        r"""Sets the version_count of this StartInferDeploymentResponse.

        **参数解释：** 服务版本数量。 **取值范围：** 不涉及。

        :param version_count: The version_count of this StartInferDeploymentResponse.
        :type version_count: int
        """
        self._version_count = version_count

    @property
    def workload_type(self):
        r"""Gets the workload_type of this StartInferDeploymentResponse.

        **参数解释：** 工作负载类型。 **取值范围：** 不涉及。

        :return: The workload_type of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        r"""Sets the workload_type of this StartInferDeploymentResponse.

        **参数解释：** 工作负载类型。 **取值范围：** 不涉及。

        :param workload_type: The workload_type of this StartInferDeploymentResponse.
        :type workload_type: str
        """
        self._workload_type = workload_type

    @property
    def update_at(self):
        r"""Gets the update_at of this StartInferDeploymentResponse.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :return: The update_at of this StartInferDeploymentResponse.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this StartInferDeploymentResponse.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :param update_at: The update_at of this StartInferDeploymentResponse.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def lts_state(self):
        r"""Gets the lts_state of this StartInferDeploymentResponse.

        **参数解释：** 部署对接lts状态。 **取值范围：** - ON：开启。 - OFF：关闭。

        :return: The lts_state of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._lts_state

    @lts_state.setter
    def lts_state(self, lts_state):
        r"""Sets the lts_state of this StartInferDeploymentResponse.

        **参数解释：** 部署对接lts状态。 **取值范围：** - ON：开启。 - OFF：关闭。

        :param lts_state: The lts_state of this StartInferDeploymentResponse.
        :type lts_state: str
        """
        self._lts_state = lts_state

    @property
    def infer_name(self):
        r"""Gets the infer_name of this StartInferDeploymentResponse.

        **参数解释：** 部署ID。

        :return: The infer_name of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._infer_name

    @infer_name.setter
    def infer_name(self, infer_name):
        r"""Sets the infer_name of this StartInferDeploymentResponse.

        **参数解释：** 部署ID。

        :param infer_name: The infer_name of this StartInferDeploymentResponse.
        :type infer_name: str
        """
        self._infer_name = infer_name

    @property
    def model(self):
        r"""Gets the model of this StartInferDeploymentResponse.

        :return: The model of this StartInferDeploymentResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.InferModelResponse`
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this StartInferDeploymentResponse.

        :param model: The model of this StartInferDeploymentResponse.
        :type model: :class:`huaweicloudsdkmodelarts.v1.InferModelResponse`
        """
        self._model = model

    @property
    def advanced_config(self):
        r"""Gets the advanced_config of this StartInferDeploymentResponse.

        :return: The advanced_config of this StartInferDeploymentResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        """
        return self._advanced_config

    @advanced_config.setter
    def advanced_config(self, advanced_config):
        r"""Sets the advanced_config of this StartInferDeploymentResponse.

        :param advanced_config: The advanced_config of this StartInferDeploymentResponse.
        :type advanced_config: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        """
        self._advanced_config = advanced_config

    @property
    def description(self):
        r"""Gets the description of this StartInferDeploymentResponse.

        **参数解释：** 部署描述。

        :return: The description of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this StartInferDeploymentResponse.

        **参数解释：** 部署描述。

        :param description: The description of this StartInferDeploymentResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_at(self):
        r"""Gets the create_at of this StartInferDeploymentResponse.

        参数解释： 创建时间，根据创建时的当前时间自动生成。 取值范围： 毫秒级时间戳，13位数字，如1609459200000。

        :return: The create_at of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this StartInferDeploymentResponse.

        参数解释： 创建时间，根据创建时的当前时间自动生成。 取值范围： 毫秒级时间戳，13位数字，如1609459200000。

        :param create_at: The create_at of this StartInferDeploymentResponse.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def schedule_strategy(self):
        r"""Gets the schedule_strategy of this StartInferDeploymentResponse.

        **参数解释：** 调度策略。 **取值范围：** - HIGH_AVAILABILITY：高可用调度 - HIGH_UTILIZATION：紧凑调度 - HIGH_PERFORMANCE：高性能调度

        :return: The schedule_strategy of this StartInferDeploymentResponse.
        :rtype: str
        """
        return self._schedule_strategy

    @schedule_strategy.setter
    def schedule_strategy(self, schedule_strategy):
        r"""Sets the schedule_strategy of this StartInferDeploymentResponse.

        **参数解释：** 调度策略。 **取值范围：** - HIGH_AVAILABILITY：高可用调度 - HIGH_UTILIZATION：紧凑调度 - HIGH_PERFORMANCE：高性能调度

        :param schedule_strategy: The schedule_strategy of this StartInferDeploymentResponse.
        :type schedule_strategy: str
        """
        self._schedule_strategy = schedule_strategy

    def to_dict(self):
        import warnings
        warnings.warn("StartInferDeploymentResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, StartInferDeploymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
