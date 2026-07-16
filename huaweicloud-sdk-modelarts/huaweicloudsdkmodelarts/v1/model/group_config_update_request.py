# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupConfigUpdateRequest:

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
        'framework': 'str',
        'count': 'int',
        'deploy_type': 'str',
        'system_log_dump_enable': 'bool',
        'unit_configs': 'list[UnitConfig]',
        'weight': 'int',
        'secret_type': 'str',
        'secret_name': 'str',
        'priority': 'int',
        'high_avail_switch': 'bool',
        'description': 'str',
        'advanced_config': 'AdvancedConfig',
        'model': 'GroupModel',
        'mirror_traffic_enable': 'bool',
        'mirror_traffic_weight': 'int',
        'status': 'str',
        'deployment_task_limit': 'DeploymentTaskLimit',
        'schedule_strategy': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'pool_id': 'pool_id',
        'framework': 'framework',
        'count': 'count',
        'deploy_type': 'deploy_type',
        'system_log_dump_enable': 'system_log_dump_enable',
        'unit_configs': 'unit_configs',
        'weight': 'weight',
        'secret_type': 'secret_type',
        'secret_name': 'secret_name',
        'priority': 'priority',
        'high_avail_switch': 'high_avail_switch',
        'description': 'description',
        'advanced_config': 'advanced_config',
        'model': 'model',
        'mirror_traffic_enable': 'mirror_traffic_enable',
        'mirror_traffic_weight': 'mirror_traffic_weight',
        'status': 'status',
        'deployment_task_limit': 'deployment_task_limit',
        'schedule_strategy': 'schedule_strategy'
    }

    def __init__(self, id=None, name=None, pool_id=None, framework=None, count=None, deploy_type=None, system_log_dump_enable=None, unit_configs=None, weight=None, secret_type=None, secret_name=None, priority=None, high_avail_switch=None, description=None, advanced_config=None, model=None, mirror_traffic_enable=None, mirror_traffic_weight=None, status=None, deployment_task_limit=None, schedule_strategy=None):
        r"""GroupConfigUpdateRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 部署ID。 **约束限制：** 不填保留原有值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type id: str
        :param name: **参数解释：** 部署名称。 **约束限制：** 必填参数，不填不保留原有值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param pool_id: **参数解释：** 资源池ID，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **约束限制：** 不填保留原有值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type pool_id: str
        :param framework: **参数解释：** 框架类型。 **约束限制：** 不填则为默认值。 **取值范围：** - COMMON：普通在线服务 - VLLM：VLLM框架 - MINDIE：MINDIE框架 **默认取值：** COMMON
        :type framework: str
        :param count: **参数解释：** 部署场景下，服务实例数量。 **约束限制：** 不填则为默认值。 **取值范围：** [1, 128]。 **默认取值：** 1
        :type count: int
        :param deploy_type: **参数解释：** 部署类型。 **约束限制：** 不填保留原有值。 **取值范围：** - SINGLE：常规部署 - MULTI：分布式部署 **默认取值：** 不涉及
        :type deploy_type: str
        :param system_log_dump_enable: **参数解释：** 系统日志转储开关。 **约束限制：** 不填则为默认值。 **取值范围：** 不涉及 **默认取值：** false
        :type system_log_dump_enable: bool
        :param unit_configs: **参数解释：** 实例单元配置。 **约束限制：** - 单机推理时，个数只会为1；如果是分布式推理时，根据不同框架，实例单元配置可灵活配置。 - 必填字段。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type unit_configs: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfig`]
        :param weight: **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **约束限制：** 不填保留原有值。 **取值范围：** [0, 100]。 **默认取值：** 不涉及
        :type weight: int
        :param secret_type: **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 1.使用临时委托凭证类型约束限制:集群已安装CCE容器存储（Everest）v2.4.204及以上版本，且集群版本为v1.28及以上且确保局点已启用IAM5服务。 2.若插件版本不足或集群不支持临时委托凭证，则需通过DEW服务挂载。 3.不填保留原有值。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。
        :type secret_type: str
        :param secret_name: **参数解释**： 认证凭证名称，用户使用dew类型凭证时可以在此处选择使用的凭证。 **约束限制**： secret_type是dew时必填，不填保留原有值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type secret_name: str
        :param priority: **参数解释：** 服务优先级。 **约束限制：** - 如服务处于“运行中”，priority字段为必要参数，且value必须为原版的值； - 如服务处于“停止”，priority字段为非必要参数。 - 不填保留原有值。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。
        :type priority: int
        :param high_avail_switch: **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。 **约束限制：** 不填则为默认值 **取值范围：** 不涉及 **默认取值：** true
        :type high_avail_switch: bool
        :param description: **参数解释：** 部署备注。 **约束限制：** 不填则将部署描述清空。 **取值范围：** 长度不可以超过512，不能包含大于号，小于号。 **默认取值：** 默认为空。
        :type description: str
        :param advanced_config: 
        :type advanced_config: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        :param model: 
        :type model: :class:`huaweicloudsdkmodelarts.v1.GroupModel`
        :param mirror_traffic_enable: **参数解释：** 镜像流量开关。 **约束限制：** 不填保留原有值 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type mirror_traffic_enable: bool
        :param mirror_traffic_weight: **参数解释：** 镜像流量权重。 **约束限制：** 不填保留原有值。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type mirror_traffic_weight: int
        :param status: **参数解释：** 部署状态。 **约束限制：** 不填保留原有值。 **取值范围：** - DEPLOYING：部署中 - FAILED：失败 - STOPPED：停止 - RUNNING：运行中 - DELETING：删除中 - STOPPING：停止中 - CONCERNING：存在潜在问题 - DELETED：删除 - RESTARTING：重启中 - UPGRADING：更新中 - ERROR：错误 - INTERRUPTING：中断中 **默认取值：** 不涉及
        :type status: str
        :param deployment_task_limit: 
        :type deployment_task_limit: :class:`huaweicloudsdkmodelarts.v1.DeploymentTaskLimit`
        :param schedule_strategy: **参数解释：** 调度策略。 **约束限制：** 不涉及。 **取值范围：** - HIGH_AVAILABILITY：高可用调度 - HIGH_UTILIZATION：紧凑调度 - HIGH_PERFORMANCE：高性能调度 **默认取值：** HIGH_AVAILABILITY。
        :type schedule_strategy: str
        """
        
        

        self._id = None
        self._name = None
        self._pool_id = None
        self._framework = None
        self._count = None
        self._deploy_type = None
        self._system_log_dump_enable = None
        self._unit_configs = None
        self._weight = None
        self._secret_type = None
        self._secret_name = None
        self._priority = None
        self._high_avail_switch = None
        self._description = None
        self._advanced_config = None
        self._model = None
        self._mirror_traffic_enable = None
        self._mirror_traffic_weight = None
        self._status = None
        self._deployment_task_limit = None
        self._schedule_strategy = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if pool_id is not None:
            self.pool_id = pool_id
        if framework is not None:
            self.framework = framework
        if count is not None:
            self.count = count
        if deploy_type is not None:
            self.deploy_type = deploy_type
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
        if description is not None:
            self.description = description
        self.advanced_config = advanced_config
        if model is not None:
            self.model = model
        if mirror_traffic_enable is not None:
            self.mirror_traffic_enable = mirror_traffic_enable
        if mirror_traffic_weight is not None:
            self.mirror_traffic_weight = mirror_traffic_weight
        if status is not None:
            self.status = status
        if deployment_task_limit is not None:
            self.deployment_task_limit = deployment_task_limit
        if schedule_strategy is not None:
            self.schedule_strategy = schedule_strategy

    @property
    def id(self):
        r"""Gets the id of this GroupConfigUpdateRequest.

        **参数解释：** 部署ID。 **约束限制：** 不填保留原有值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The id of this GroupConfigUpdateRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupConfigUpdateRequest.

        **参数解释：** 部署ID。 **约束限制：** 不填保留原有值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param id: The id of this GroupConfigUpdateRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GroupConfigUpdateRequest.

        **参数解释：** 部署名称。 **约束限制：** 必填参数，不填不保留原有值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this GroupConfigUpdateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupConfigUpdateRequest.

        **参数解释：** 部署名称。 **约束限制：** 必填参数，不填不保留原有值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this GroupConfigUpdateRequest.
        :type name: str
        """
        self._name = name

    @property
    def pool_id(self):
        r"""Gets the pool_id of this GroupConfigUpdateRequest.

        **参数解释：** 资源池ID，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **约束限制：** 不填保留原有值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The pool_id of this GroupConfigUpdateRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this GroupConfigUpdateRequest.

        **参数解释：** 资源池ID，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **约束限制：** 不填保留原有值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param pool_id: The pool_id of this GroupConfigUpdateRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def framework(self):
        r"""Gets the framework of this GroupConfigUpdateRequest.

        **参数解释：** 框架类型。 **约束限制：** 不填则为默认值。 **取值范围：** - COMMON：普通在线服务 - VLLM：VLLM框架 - MINDIE：MINDIE框架 **默认取值：** COMMON

        :return: The framework of this GroupConfigUpdateRequest.
        :rtype: str
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        r"""Sets the framework of this GroupConfigUpdateRequest.

        **参数解释：** 框架类型。 **约束限制：** 不填则为默认值。 **取值范围：** - COMMON：普通在线服务 - VLLM：VLLM框架 - MINDIE：MINDIE框架 **默认取值：** COMMON

        :param framework: The framework of this GroupConfigUpdateRequest.
        :type framework: str
        """
        self._framework = framework

    @property
    def count(self):
        r"""Gets the count of this GroupConfigUpdateRequest.

        **参数解释：** 部署场景下，服务实例数量。 **约束限制：** 不填则为默认值。 **取值范围：** [1, 128]。 **默认取值：** 1

        :return: The count of this GroupConfigUpdateRequest.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this GroupConfigUpdateRequest.

        **参数解释：** 部署场景下，服务实例数量。 **约束限制：** 不填则为默认值。 **取值范围：** [1, 128]。 **默认取值：** 1

        :param count: The count of this GroupConfigUpdateRequest.
        :type count: int
        """
        self._count = count

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this GroupConfigUpdateRequest.

        **参数解释：** 部署类型。 **约束限制：** 不填保留原有值。 **取值范围：** - SINGLE：常规部署 - MULTI：分布式部署 **默认取值：** 不涉及

        :return: The deploy_type of this GroupConfigUpdateRequest.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this GroupConfigUpdateRequest.

        **参数解释：** 部署类型。 **约束限制：** 不填保留原有值。 **取值范围：** - SINGLE：常规部署 - MULTI：分布式部署 **默认取值：** 不涉及

        :param deploy_type: The deploy_type of this GroupConfigUpdateRequest.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def system_log_dump_enable(self):
        r"""Gets the system_log_dump_enable of this GroupConfigUpdateRequest.

        **参数解释：** 系统日志转储开关。 **约束限制：** 不填则为默认值。 **取值范围：** 不涉及 **默认取值：** false

        :return: The system_log_dump_enable of this GroupConfigUpdateRequest.
        :rtype: bool
        """
        return self._system_log_dump_enable

    @system_log_dump_enable.setter
    def system_log_dump_enable(self, system_log_dump_enable):
        r"""Sets the system_log_dump_enable of this GroupConfigUpdateRequest.

        **参数解释：** 系统日志转储开关。 **约束限制：** 不填则为默认值。 **取值范围：** 不涉及 **默认取值：** false

        :param system_log_dump_enable: The system_log_dump_enable of this GroupConfigUpdateRequest.
        :type system_log_dump_enable: bool
        """
        self._system_log_dump_enable = system_log_dump_enable

    @property
    def unit_configs(self):
        r"""Gets the unit_configs of this GroupConfigUpdateRequest.

        **参数解释：** 实例单元配置。 **约束限制：** - 单机推理时，个数只会为1；如果是分布式推理时，根据不同框架，实例单元配置可灵活配置。 - 必填字段。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The unit_configs of this GroupConfigUpdateRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfig`]
        """
        return self._unit_configs

    @unit_configs.setter
    def unit_configs(self, unit_configs):
        r"""Sets the unit_configs of this GroupConfigUpdateRequest.

        **参数解释：** 实例单元配置。 **约束限制：** - 单机推理时，个数只会为1；如果是分布式推理时，根据不同框架，实例单元配置可灵活配置。 - 必填字段。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param unit_configs: The unit_configs of this GroupConfigUpdateRequest.
        :type unit_configs: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfig`]
        """
        self._unit_configs = unit_configs

    @property
    def weight(self):
        r"""Gets the weight of this GroupConfigUpdateRequest.

        **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **约束限制：** 不填保留原有值。 **取值范围：** [0, 100]。 **默认取值：** 不涉及

        :return: The weight of this GroupConfigUpdateRequest.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this GroupConfigUpdateRequest.

        **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **约束限制：** 不填保留原有值。 **取值范围：** [0, 100]。 **默认取值：** 不涉及

        :param weight: The weight of this GroupConfigUpdateRequest.
        :type weight: int
        """
        self._weight = weight

    @property
    def secret_type(self):
        r"""Gets the secret_type of this GroupConfigUpdateRequest.

        **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 1.使用临时委托凭证类型约束限制:集群已安装CCE容器存储（Everest）v2.4.204及以上版本，且集群版本为v1.28及以上且确保局点已启用IAM5服务。 2.若插件版本不足或集群不支持临时委托凭证，则需通过DEW服务挂载。 3.不填保留原有值。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。

        :return: The secret_type of this GroupConfigUpdateRequest.
        :rtype: str
        """
        return self._secret_type

    @secret_type.setter
    def secret_type(self, secret_type):
        r"""Sets the secret_type of this GroupConfigUpdateRequest.

        **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 1.使用临时委托凭证类型约束限制:集群已安装CCE容器存储（Everest）v2.4.204及以上版本，且集群版本为v1.28及以上且确保局点已启用IAM5服务。 2.若插件版本不足或集群不支持临时委托凭证，则需通过DEW服务挂载。 3.不填保留原有值。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。

        :param secret_type: The secret_type of this GroupConfigUpdateRequest.
        :type secret_type: str
        """
        self._secret_type = secret_type

    @property
    def secret_name(self):
        r"""Gets the secret_name of this GroupConfigUpdateRequest.

        **参数解释**： 认证凭证名称，用户使用dew类型凭证时可以在此处选择使用的凭证。 **约束限制**： secret_type是dew时必填，不填保留原有值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The secret_name of this GroupConfigUpdateRequest.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        r"""Sets the secret_name of this GroupConfigUpdateRequest.

        **参数解释**： 认证凭证名称，用户使用dew类型凭证时可以在此处选择使用的凭证。 **约束限制**： secret_type是dew时必填，不填保留原有值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param secret_name: The secret_name of this GroupConfigUpdateRequest.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def priority(self):
        r"""Gets the priority of this GroupConfigUpdateRequest.

        **参数解释：** 服务优先级。 **约束限制：** - 如服务处于“运行中”，priority字段为必要参数，且value必须为原版的值； - 如服务处于“停止”，priority字段为非必要参数。 - 不填保留原有值。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。

        :return: The priority of this GroupConfigUpdateRequest.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this GroupConfigUpdateRequest.

        **参数解释：** 服务优先级。 **约束限制：** - 如服务处于“运行中”，priority字段为必要参数，且value必须为原版的值； - 如服务处于“停止”，priority字段为非必要参数。 - 不填保留原有值。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。

        :param priority: The priority of this GroupConfigUpdateRequest.
        :type priority: int
        """
        self._priority = priority

    @property
    def high_avail_switch(self):
        r"""Gets the high_avail_switch of this GroupConfigUpdateRequest.

        **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。 **约束限制：** 不填则为默认值 **取值范围：** 不涉及 **默认取值：** true

        :return: The high_avail_switch of this GroupConfigUpdateRequest.
        :rtype: bool
        """
        return self._high_avail_switch

    @high_avail_switch.setter
    def high_avail_switch(self, high_avail_switch):
        r"""Sets the high_avail_switch of this GroupConfigUpdateRequest.

        **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。 **约束限制：** 不填则为默认值 **取值范围：** 不涉及 **默认取值：** true

        :param high_avail_switch: The high_avail_switch of this GroupConfigUpdateRequest.
        :type high_avail_switch: bool
        """
        self._high_avail_switch = high_avail_switch

    @property
    def description(self):
        r"""Gets the description of this GroupConfigUpdateRequest.

        **参数解释：** 部署备注。 **约束限制：** 不填则将部署描述清空。 **取值范围：** 长度不可以超过512，不能包含大于号，小于号。 **默认取值：** 默认为空。

        :return: The description of this GroupConfigUpdateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this GroupConfigUpdateRequest.

        **参数解释：** 部署备注。 **约束限制：** 不填则将部署描述清空。 **取值范围：** 长度不可以超过512，不能包含大于号，小于号。 **默认取值：** 默认为空。

        :param description: The description of this GroupConfigUpdateRequest.
        :type description: str
        """
        self._description = description

    @property
    def advanced_config(self):
        r"""Gets the advanced_config of this GroupConfigUpdateRequest.

        :return: The advanced_config of this GroupConfigUpdateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        """
        return self._advanced_config

    @advanced_config.setter
    def advanced_config(self, advanced_config):
        r"""Sets the advanced_config of this GroupConfigUpdateRequest.

        :param advanced_config: The advanced_config of this GroupConfigUpdateRequest.
        :type advanced_config: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        """
        self._advanced_config = advanced_config

    @property
    def model(self):
        r"""Gets the model of this GroupConfigUpdateRequest.

        :return: The model of this GroupConfigUpdateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.GroupModel`
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this GroupConfigUpdateRequest.

        :param model: The model of this GroupConfigUpdateRequest.
        :type model: :class:`huaweicloudsdkmodelarts.v1.GroupModel`
        """
        self._model = model

    @property
    def mirror_traffic_enable(self):
        r"""Gets the mirror_traffic_enable of this GroupConfigUpdateRequest.

        **参数解释：** 镜像流量开关。 **约束限制：** 不填保留原有值 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The mirror_traffic_enable of this GroupConfigUpdateRequest.
        :rtype: bool
        """
        return self._mirror_traffic_enable

    @mirror_traffic_enable.setter
    def mirror_traffic_enable(self, mirror_traffic_enable):
        r"""Sets the mirror_traffic_enable of this GroupConfigUpdateRequest.

        **参数解释：** 镜像流量开关。 **约束限制：** 不填保留原有值 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param mirror_traffic_enable: The mirror_traffic_enable of this GroupConfigUpdateRequest.
        :type mirror_traffic_enable: bool
        """
        self._mirror_traffic_enable = mirror_traffic_enable

    @property
    def mirror_traffic_weight(self):
        r"""Gets the mirror_traffic_weight of this GroupConfigUpdateRequest.

        **参数解释：** 镜像流量权重。 **约束限制：** 不填保留原有值。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The mirror_traffic_weight of this GroupConfigUpdateRequest.
        :rtype: int
        """
        return self._mirror_traffic_weight

    @mirror_traffic_weight.setter
    def mirror_traffic_weight(self, mirror_traffic_weight):
        r"""Sets the mirror_traffic_weight of this GroupConfigUpdateRequest.

        **参数解释：** 镜像流量权重。 **约束限制：** 不填保留原有值。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param mirror_traffic_weight: The mirror_traffic_weight of this GroupConfigUpdateRequest.
        :type mirror_traffic_weight: int
        """
        self._mirror_traffic_weight = mirror_traffic_weight

    @property
    def status(self):
        r"""Gets the status of this GroupConfigUpdateRequest.

        **参数解释：** 部署状态。 **约束限制：** 不填保留原有值。 **取值范围：** - DEPLOYING：部署中 - FAILED：失败 - STOPPED：停止 - RUNNING：运行中 - DELETING：删除中 - STOPPING：停止中 - CONCERNING：存在潜在问题 - DELETED：删除 - RESTARTING：重启中 - UPGRADING：更新中 - ERROR：错误 - INTERRUPTING：中断中 **默认取值：** 不涉及

        :return: The status of this GroupConfigUpdateRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GroupConfigUpdateRequest.

        **参数解释：** 部署状态。 **约束限制：** 不填保留原有值。 **取值范围：** - DEPLOYING：部署中 - FAILED：失败 - STOPPED：停止 - RUNNING：运行中 - DELETING：删除中 - STOPPING：停止中 - CONCERNING：存在潜在问题 - DELETED：删除 - RESTARTING：重启中 - UPGRADING：更新中 - ERROR：错误 - INTERRUPTING：中断中 **默认取值：** 不涉及

        :param status: The status of this GroupConfigUpdateRequest.
        :type status: str
        """
        self._status = status

    @property
    def deployment_task_limit(self):
        r"""Gets the deployment_task_limit of this GroupConfigUpdateRequest.

        :return: The deployment_task_limit of this GroupConfigUpdateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.DeploymentTaskLimit`
        """
        return self._deployment_task_limit

    @deployment_task_limit.setter
    def deployment_task_limit(self, deployment_task_limit):
        r"""Sets the deployment_task_limit of this GroupConfigUpdateRequest.

        :param deployment_task_limit: The deployment_task_limit of this GroupConfigUpdateRequest.
        :type deployment_task_limit: :class:`huaweicloudsdkmodelarts.v1.DeploymentTaskLimit`
        """
        self._deployment_task_limit = deployment_task_limit

    @property
    def schedule_strategy(self):
        r"""Gets the schedule_strategy of this GroupConfigUpdateRequest.

        **参数解释：** 调度策略。 **约束限制：** 不涉及。 **取值范围：** - HIGH_AVAILABILITY：高可用调度 - HIGH_UTILIZATION：紧凑调度 - HIGH_PERFORMANCE：高性能调度 **默认取值：** HIGH_AVAILABILITY。

        :return: The schedule_strategy of this GroupConfigUpdateRequest.
        :rtype: str
        """
        return self._schedule_strategy

    @schedule_strategy.setter
    def schedule_strategy(self, schedule_strategy):
        r"""Sets the schedule_strategy of this GroupConfigUpdateRequest.

        **参数解释：** 调度策略。 **约束限制：** 不涉及。 **取值范围：** - HIGH_AVAILABILITY：高可用调度 - HIGH_UTILIZATION：紧凑调度 - HIGH_PERFORMANCE：高性能调度 **默认取值：** HIGH_AVAILABILITY。

        :param schedule_strategy: The schedule_strategy of this GroupConfigUpdateRequest.
        :type schedule_strategy: str
        """
        self._schedule_strategy = schedule_strategy

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
        if not isinstance(other, GroupConfigUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
