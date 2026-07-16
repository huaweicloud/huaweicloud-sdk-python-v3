# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupConfig:

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
        'unit_configs': 'list[UnitConfig]',
        'weight': 'int',
        'secret_type': 'str',
        'secret_name': 'str',
        'priority': 'int',
        'high_avail_switch': 'bool',
        'schedule_strategy': 'str',
        'version': 'str',
        'version_id': 'str',
        'description': 'str',
        'framework': 'str',
        'running_count': 'int',
        'deploy_type': 'str',
        'mirror_traffic_enable': 'bool',
        'mirror_traffic_weight': 'str',
        'version_count': 'int',
        'workload_type': 'str',
        'update_at': 'int',
        'model': 'ModelResource',
        'advanced_config': 'AdvancedConfig'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'pool_id': 'pool_id',
        'count': 'count',
        'system_log_dump_enable': 'system_log_dump_enable',
        'unit_configs': 'unit_configs',
        'weight': 'weight',
        'secret_type': 'secret_type',
        'secret_name': 'secret_name',
        'priority': 'priority',
        'high_avail_switch': 'high_avail_switch',
        'schedule_strategy': 'schedule_strategy',
        'version': 'version',
        'version_id': 'version_id',
        'description': 'description',
        'framework': 'framework',
        'running_count': 'running_count',
        'deploy_type': 'deploy_type',
        'mirror_traffic_enable': 'mirror_traffic_enable',
        'mirror_traffic_weight': 'mirror_traffic_weight',
        'version_count': 'version_count',
        'workload_type': 'workload_type',
        'update_at': 'update_at',
        'model': 'model',
        'advanced_config': 'advanced_config'
    }

    def __init__(self, id=None, name=None, pool_id=None, count=None, system_log_dump_enable=None, unit_configs=None, weight=None, secret_type=None, secret_name=None, priority=None, high_avail_switch=None, schedule_strategy=None, version=None, version_id=None, description=None, framework=None, running_count=None, deploy_type=None, mirror_traffic_enable=None, mirror_traffic_weight=None, version_count=None, workload_type=None, update_at=None, model=None, advanced_config=None):
        r"""GroupConfig

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 部署ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type id: str
        :param name: **参数解释：** 部署名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param pool_id: **参数解释：** 资源池ID，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type pool_id: str
        :param count: **参数解释：** 部署场景下，服务实例数量。 **约束限制：** 不涉及。 **取值范围：** [1, 128]。 **默认取值：** 不涉及。
        :type count: int
        :param system_log_dump_enable: **参数解释：** 系统日志转储开关。 **约束限制：** 只有NPU资源池有，且逻辑池是没有的。 **取值范围：** 不涉及。 **默认取值：** false。
        :type system_log_dump_enable: bool
        :param unit_configs: **参数解释：** 推理单元配置。 **约束限制：** 单机推理时，个数只会为1；如果是分布式推理时，根据不同框架，实例单元配置可灵活配置。
        :type unit_configs: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfig`]
        :param weight: **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **约束限制：** 不涉及。 **取值范围：** [0, 100]。 **默认取值：** 不涉及。
        :type weight: int
        :param secret_type: **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 1.使用临时委托凭证类型约束限制:集群已安装CCE容器存储（Everest）v2.4.204及以上版本，且集群版本为v1.28及以上且确保局点已启用IAM5服务。 2.若插件版本不足或集群不支持临时委托凭证，则需通过DEW服务挂载。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。
        :type secret_type: str
        :param secret_name: **参数解释**： 凭证名称，用户使用dew类型凭证时可以在此处选择使用的凭证。 **约束限制**： 不涉及。
        :type secret_name: str
        :param priority: **参数解释：** 服务优先级。 **约束限制：** - 如服务处于\&quot;运行中\&quot;，priority字段为必要参数，且value必须与原服务的priority值相同； - 如服务处于\&quot;停止\&quot;，priority字段为非必要参数。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。
        :type priority: int
        :param high_avail_switch: **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。（准备下线，请使用schedule_strategy字段） **约束限制：** 不涉及。 **取值范围：** - true：高可用开启。 - false：高可用关闭。 **默认取值：** true。
        :type high_avail_switch: bool
        :param schedule_strategy: **参数解释：** 调度策略。 **约束限制：** 不涉及。 **取值范围：** - HIGH_AVAILABILITY：高可用调度 - HIGH_UTILIZATION：紧凑调度 - HIGH_PERFORMANCE：高性能调度 **默认取值：** HIGH_AVAILABILITY。
        :type schedule_strategy: str
        :param version: **参数解释：** 服务版本号，以数字及点号组成，形如1.0.1。 **约束限制：** 不涉及。 **取值范围：** 1.0.0 ~ 99.99.99，长度不超过8位。 **默认取值：** 不涉及。
        :type version: str
        :param version_id: **参数解释：** 版本id，可通过查询version列表查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type version_id: str
        :param description: **参数解释：** 服务备注。 **约束限制：** 不涉及。 **取值范围：** 长度不可以超过512，不能包含大于号，小于号。 **默认取值：** 默认为空。
        :type description: str
        :param framework: **参数解释：** 服务框架。 **约束限制：** 仅支持以下枚举值：COMMON | VLLM | MINDIE。 **取值范围：** 仅支持以下枚举值：COMMON | VLLM | MINDIE。 **默认取值：** COMMON。
        :type framework: str
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
        :param workload_type: **参数解释：** 工作负载类型。 **取值范围：** - DEPLOYMENT：DEPLOYMENT类型 - LWS：LWS类型
        :type workload_type: str
        :param update_at: **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。
        :type update_at: int
        :param model: 
        :type model: :class:`huaweicloudsdkmodelarts.v1.ModelResource`
        :param advanced_config: 
        :type advanced_config: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        """
        
        

        self._id = None
        self._name = None
        self._pool_id = None
        self._count = None
        self._system_log_dump_enable = None
        self._unit_configs = None
        self._weight = None
        self._secret_type = None
        self._secret_name = None
        self._priority = None
        self._high_avail_switch = None
        self._schedule_strategy = None
        self._version = None
        self._version_id = None
        self._description = None
        self._framework = None
        self._running_count = None
        self._deploy_type = None
        self._mirror_traffic_enable = None
        self._mirror_traffic_weight = None
        self._version_count = None
        self._workload_type = None
        self._update_at = None
        self._model = None
        self._advanced_config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if pool_id is not None:
            self.pool_id = pool_id
        if count is not None:
            self.count = count
        if system_log_dump_enable is not None:
            self.system_log_dump_enable = system_log_dump_enable
        if unit_configs is not None:
            self.unit_configs = unit_configs
        self.weight = weight
        if secret_type is not None:
            self.secret_type = secret_type
        if secret_name is not None:
            self.secret_name = secret_name
        if priority is not None:
            self.priority = priority
        if high_avail_switch is not None:
            self.high_avail_switch = high_avail_switch
        if schedule_strategy is not None:
            self.schedule_strategy = schedule_strategy
        if version is not None:
            self.version = version
        if version_id is not None:
            self.version_id = version_id
        if description is not None:
            self.description = description
        if framework is not None:
            self.framework = framework
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
        if model is not None:
            self.model = model
        if advanced_config is not None:
            self.advanced_config = advanced_config

    @property
    def id(self):
        r"""Gets the id of this GroupConfig.

        **参数解释：** 部署ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The id of this GroupConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupConfig.

        **参数解释：** 部署ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param id: The id of this GroupConfig.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GroupConfig.

        **参数解释：** 部署名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this GroupConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupConfig.

        **参数解释：** 部署名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this GroupConfig.
        :type name: str
        """
        self._name = name

    @property
    def pool_id(self):
        r"""Gets the pool_id of this GroupConfig.

        **参数解释：** 资源池ID，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The pool_id of this GroupConfig.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this GroupConfig.

        **参数解释：** 资源池ID，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param pool_id: The pool_id of this GroupConfig.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def count(self):
        r"""Gets the count of this GroupConfig.

        **参数解释：** 部署场景下，服务实例数量。 **约束限制：** 不涉及。 **取值范围：** [1, 128]。 **默认取值：** 不涉及。

        :return: The count of this GroupConfig.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this GroupConfig.

        **参数解释：** 部署场景下，服务实例数量。 **约束限制：** 不涉及。 **取值范围：** [1, 128]。 **默认取值：** 不涉及。

        :param count: The count of this GroupConfig.
        :type count: int
        """
        self._count = count

    @property
    def system_log_dump_enable(self):
        r"""Gets the system_log_dump_enable of this GroupConfig.

        **参数解释：** 系统日志转储开关。 **约束限制：** 只有NPU资源池有，且逻辑池是没有的。 **取值范围：** 不涉及。 **默认取值：** false。

        :return: The system_log_dump_enable of this GroupConfig.
        :rtype: bool
        """
        return self._system_log_dump_enable

    @system_log_dump_enable.setter
    def system_log_dump_enable(self, system_log_dump_enable):
        r"""Sets the system_log_dump_enable of this GroupConfig.

        **参数解释：** 系统日志转储开关。 **约束限制：** 只有NPU资源池有，且逻辑池是没有的。 **取值范围：** 不涉及。 **默认取值：** false。

        :param system_log_dump_enable: The system_log_dump_enable of this GroupConfig.
        :type system_log_dump_enable: bool
        """
        self._system_log_dump_enable = system_log_dump_enable

    @property
    def unit_configs(self):
        r"""Gets the unit_configs of this GroupConfig.

        **参数解释：** 推理单元配置。 **约束限制：** 单机推理时，个数只会为1；如果是分布式推理时，根据不同框架，实例单元配置可灵活配置。

        :return: The unit_configs of this GroupConfig.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfig`]
        """
        return self._unit_configs

    @unit_configs.setter
    def unit_configs(self, unit_configs):
        r"""Sets the unit_configs of this GroupConfig.

        **参数解释：** 推理单元配置。 **约束限制：** 单机推理时，个数只会为1；如果是分布式推理时，根据不同框架，实例单元配置可灵活配置。

        :param unit_configs: The unit_configs of this GroupConfig.
        :type unit_configs: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfig`]
        """
        self._unit_configs = unit_configs

    @property
    def weight(self):
        r"""Gets the weight of this GroupConfig.

        **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **约束限制：** 不涉及。 **取值范围：** [0, 100]。 **默认取值：** 不涉及。

        :return: The weight of this GroupConfig.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this GroupConfig.

        **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **约束限制：** 不涉及。 **取值范围：** [0, 100]。 **默认取值：** 不涉及。

        :param weight: The weight of this GroupConfig.
        :type weight: int
        """
        self._weight = weight

    @property
    def secret_type(self):
        r"""Gets the secret_type of this GroupConfig.

        **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 1.使用临时委托凭证类型约束限制:集群已安装CCE容器存储（Everest）v2.4.204及以上版本，且集群版本为v1.28及以上且确保局点已启用IAM5服务。 2.若插件版本不足或集群不支持临时委托凭证，则需通过DEW服务挂载。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。

        :return: The secret_type of this GroupConfig.
        :rtype: str
        """
        return self._secret_type

    @secret_type.setter
    def secret_type(self, secret_type):
        r"""Sets the secret_type of this GroupConfig.

        **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 1.使用临时委托凭证类型约束限制:集群已安装CCE容器存储（Everest）v2.4.204及以上版本，且集群版本为v1.28及以上且确保局点已启用IAM5服务。 2.若插件版本不足或集群不支持临时委托凭证，则需通过DEW服务挂载。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。

        :param secret_type: The secret_type of this GroupConfig.
        :type secret_type: str
        """
        self._secret_type = secret_type

    @property
    def secret_name(self):
        r"""Gets the secret_name of this GroupConfig.

        **参数解释**： 凭证名称，用户使用dew类型凭证时可以在此处选择使用的凭证。 **约束限制**： 不涉及。

        :return: The secret_name of this GroupConfig.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        r"""Sets the secret_name of this GroupConfig.

        **参数解释**： 凭证名称，用户使用dew类型凭证时可以在此处选择使用的凭证。 **约束限制**： 不涉及。

        :param secret_name: The secret_name of this GroupConfig.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def priority(self):
        r"""Gets the priority of this GroupConfig.

        **参数解释：** 服务优先级。 **约束限制：** - 如服务处于\"运行中\"，priority字段为必要参数，且value必须与原服务的priority值相同； - 如服务处于\"停止\"，priority字段为非必要参数。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。

        :return: The priority of this GroupConfig.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this GroupConfig.

        **参数解释：** 服务优先级。 **约束限制：** - 如服务处于\"运行中\"，priority字段为必要参数，且value必须与原服务的priority值相同； - 如服务处于\"停止\"，priority字段为非必要参数。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。

        :param priority: The priority of this GroupConfig.
        :type priority: int
        """
        self._priority = priority

    @property
    def high_avail_switch(self):
        r"""Gets the high_avail_switch of this GroupConfig.

        **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。（准备下线，请使用schedule_strategy字段） **约束限制：** 不涉及。 **取值范围：** - true：高可用开启。 - false：高可用关闭。 **默认取值：** true。

        :return: The high_avail_switch of this GroupConfig.
        :rtype: bool
        """
        return self._high_avail_switch

    @high_avail_switch.setter
    def high_avail_switch(self, high_avail_switch):
        r"""Sets the high_avail_switch of this GroupConfig.

        **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。（准备下线，请使用schedule_strategy字段） **约束限制：** 不涉及。 **取值范围：** - true：高可用开启。 - false：高可用关闭。 **默认取值：** true。

        :param high_avail_switch: The high_avail_switch of this GroupConfig.
        :type high_avail_switch: bool
        """
        self._high_avail_switch = high_avail_switch

    @property
    def schedule_strategy(self):
        r"""Gets the schedule_strategy of this GroupConfig.

        **参数解释：** 调度策略。 **约束限制：** 不涉及。 **取值范围：** - HIGH_AVAILABILITY：高可用调度 - HIGH_UTILIZATION：紧凑调度 - HIGH_PERFORMANCE：高性能调度 **默认取值：** HIGH_AVAILABILITY。

        :return: The schedule_strategy of this GroupConfig.
        :rtype: str
        """
        return self._schedule_strategy

    @schedule_strategy.setter
    def schedule_strategy(self, schedule_strategy):
        r"""Sets the schedule_strategy of this GroupConfig.

        **参数解释：** 调度策略。 **约束限制：** 不涉及。 **取值范围：** - HIGH_AVAILABILITY：高可用调度 - HIGH_UTILIZATION：紧凑调度 - HIGH_PERFORMANCE：高性能调度 **默认取值：** HIGH_AVAILABILITY。

        :param schedule_strategy: The schedule_strategy of this GroupConfig.
        :type schedule_strategy: str
        """
        self._schedule_strategy = schedule_strategy

    @property
    def version(self):
        r"""Gets the version of this GroupConfig.

        **参数解释：** 服务版本号，以数字及点号组成，形如1.0.1。 **约束限制：** 不涉及。 **取值范围：** 1.0.0 ~ 99.99.99，长度不超过8位。 **默认取值：** 不涉及。

        :return: The version of this GroupConfig.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this GroupConfig.

        **参数解释：** 服务版本号，以数字及点号组成，形如1.0.1。 **约束限制：** 不涉及。 **取值范围：** 1.0.0 ~ 99.99.99，长度不超过8位。 **默认取值：** 不涉及。

        :param version: The version of this GroupConfig.
        :type version: str
        """
        self._version = version

    @property
    def version_id(self):
        r"""Gets the version_id of this GroupConfig.

        **参数解释：** 版本id，可通过查询version列表查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The version_id of this GroupConfig.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this GroupConfig.

        **参数解释：** 版本id，可通过查询version列表查询。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param version_id: The version_id of this GroupConfig.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def description(self):
        r"""Gets the description of this GroupConfig.

        **参数解释：** 服务备注。 **约束限制：** 不涉及。 **取值范围：** 长度不可以超过512，不能包含大于号，小于号。 **默认取值：** 默认为空。

        :return: The description of this GroupConfig.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this GroupConfig.

        **参数解释：** 服务备注。 **约束限制：** 不涉及。 **取值范围：** 长度不可以超过512，不能包含大于号，小于号。 **默认取值：** 默认为空。

        :param description: The description of this GroupConfig.
        :type description: str
        """
        self._description = description

    @property
    def framework(self):
        r"""Gets the framework of this GroupConfig.

        **参数解释：** 服务框架。 **约束限制：** 仅支持以下枚举值：COMMON | VLLM | MINDIE。 **取值范围：** 仅支持以下枚举值：COMMON | VLLM | MINDIE。 **默认取值：** COMMON。

        :return: The framework of this GroupConfig.
        :rtype: str
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        r"""Sets the framework of this GroupConfig.

        **参数解释：** 服务框架。 **约束限制：** 仅支持以下枚举值：COMMON | VLLM | MINDIE。 **取值范围：** 仅支持以下枚举值：COMMON | VLLM | MINDIE。 **默认取值：** COMMON。

        :param framework: The framework of this GroupConfig.
        :type framework: str
        """
        self._framework = framework

    @property
    def running_count(self):
        r"""Gets the running_count of this GroupConfig.

        **参数解释：** 部署场景下，服务运行实例数量。 **约束限制：** 不涉及。 **取值范围：** [1, 128]。 **默认取值：** 不涉及。

        :return: The running_count of this GroupConfig.
        :rtype: int
        """
        return self._running_count

    @running_count.setter
    def running_count(self, running_count):
        r"""Sets the running_count of this GroupConfig.

        **参数解释：** 部署场景下，服务运行实例数量。 **约束限制：** 不涉及。 **取值范围：** [1, 128]。 **默认取值：** 不涉及。

        :param running_count: The running_count of this GroupConfig.
        :type running_count: int
        """
        self._running_count = running_count

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this GroupConfig.

        **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。

        :return: The deploy_type of this GroupConfig.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this GroupConfig.

        **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。

        :param deploy_type: The deploy_type of this GroupConfig.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def mirror_traffic_enable(self):
        r"""Gets the mirror_traffic_enable of this GroupConfig.

        **参数解释：** 是否开启镜像流量。 **取值范围：** 不涉及。

        :return: The mirror_traffic_enable of this GroupConfig.
        :rtype: bool
        """
        return self._mirror_traffic_enable

    @mirror_traffic_enable.setter
    def mirror_traffic_enable(self, mirror_traffic_enable):
        r"""Sets the mirror_traffic_enable of this GroupConfig.

        **参数解释：** 是否开启镜像流量。 **取值范围：** 不涉及。

        :param mirror_traffic_enable: The mirror_traffic_enable of this GroupConfig.
        :type mirror_traffic_enable: bool
        """
        self._mirror_traffic_enable = mirror_traffic_enable

    @property
    def mirror_traffic_weight(self):
        r"""Gets the mirror_traffic_weight of this GroupConfig.

        **参数解释：** 镜像流量权重。 **取值范围：** 50。

        :return: The mirror_traffic_weight of this GroupConfig.
        :rtype: str
        """
        return self._mirror_traffic_weight

    @mirror_traffic_weight.setter
    def mirror_traffic_weight(self, mirror_traffic_weight):
        r"""Sets the mirror_traffic_weight of this GroupConfig.

        **参数解释：** 镜像流量权重。 **取值范围：** 50。

        :param mirror_traffic_weight: The mirror_traffic_weight of this GroupConfig.
        :type mirror_traffic_weight: str
        """
        self._mirror_traffic_weight = mirror_traffic_weight

    @property
    def version_count(self):
        r"""Gets the version_count of this GroupConfig.

        **参数解释：** 服务版本数量。 **取值范围：** 不涉及。

        :return: The version_count of this GroupConfig.
        :rtype: int
        """
        return self._version_count

    @version_count.setter
    def version_count(self, version_count):
        r"""Sets the version_count of this GroupConfig.

        **参数解释：** 服务版本数量。 **取值范围：** 不涉及。

        :param version_count: The version_count of this GroupConfig.
        :type version_count: int
        """
        self._version_count = version_count

    @property
    def workload_type(self):
        r"""Gets the workload_type of this GroupConfig.

        **参数解释：** 工作负载类型。 **取值范围：** - DEPLOYMENT：DEPLOYMENT类型 - LWS：LWS类型

        :return: The workload_type of this GroupConfig.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        r"""Sets the workload_type of this GroupConfig.

        **参数解释：** 工作负载类型。 **取值范围：** - DEPLOYMENT：DEPLOYMENT类型 - LWS：LWS类型

        :param workload_type: The workload_type of this GroupConfig.
        :type workload_type: str
        """
        self._workload_type = workload_type

    @property
    def update_at(self):
        r"""Gets the update_at of this GroupConfig.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :return: The update_at of this GroupConfig.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this GroupConfig.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :param update_at: The update_at of this GroupConfig.
        :type update_at: int
        """
        self._update_at = update_at

    @property
    def model(self):
        r"""Gets the model of this GroupConfig.

        :return: The model of this GroupConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ModelResource`
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this GroupConfig.

        :param model: The model of this GroupConfig.
        :type model: :class:`huaweicloudsdkmodelarts.v1.ModelResource`
        """
        self._model = model

    @property
    def advanced_config(self):
        r"""Gets the advanced_config of this GroupConfig.

        :return: The advanced_config of this GroupConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        """
        return self._advanced_config

    @advanced_config.setter
    def advanced_config(self, advanced_config):
        r"""Sets the advanced_config of this GroupConfig.

        :param advanced_config: The advanced_config of this GroupConfig.
        :type advanced_config: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        """
        self._advanced_config = advanced_config

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
        if not isinstance(other, GroupConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
