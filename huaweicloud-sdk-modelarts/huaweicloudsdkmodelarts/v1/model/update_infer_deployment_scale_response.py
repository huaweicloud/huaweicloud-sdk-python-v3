# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInferDeploymentScaleResponse(SdkResponse):

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
        'infer_name': 'str',
        'create_at': 'datetime',
        'description': 'str',
        'pool_id': 'str',
        'framework': 'str',
        'priority': 'str',
        'secret_type': 'str',
        'status': 'str',
        'count': 'int',
        'high_avail_switch': 'str',
        'system_log_dump_enable': 'str',
        'unit_configs': 'list[UnitConfig]',
        'update_at': 'datetime',
        'version': 'str',
        'version_count': 'int',
        'weight': 'int',
        'advanced_config': 'AdvancedConfig',
        'job_id': 'str',
        'deployment_name': 'str',
        'frozen_infos': 'list[FrozenInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'infer_name': 'infer_name',
        'create_at': 'create_at',
        'description': 'description',
        'pool_id': 'pool_id',
        'framework': 'framework',
        'priority': 'priority',
        'secret_type': 'secret_type',
        'status': 'status',
        'count': 'count',
        'high_avail_switch': 'high_avail_switch',
        'system_log_dump_enable': 'system_log_dump_enable',
        'unit_configs': 'unit_configs',
        'update_at': 'update_at',
        'version': 'version',
        'version_count': 'version_count',
        'weight': 'weight',
        'advanced_config': 'advanced_config',
        'job_id': 'job_id',
        'deployment_name': 'deployment_name',
        'frozen_infos': 'frozen_infos'
    }

    def __init__(self, id=None, name=None, infer_name=None, create_at=None, description=None, pool_id=None, framework=None, priority=None, secret_type=None, status=None, count=None, high_avail_switch=None, system_log_dump_enable=None, unit_configs=None, update_at=None, version=None, version_count=None, weight=None, advanced_config=None, job_id=None, deployment_name=None, frozen_infos=None):
        r"""UpdateInferDeploymentScaleResponse

        The model defined in huaweicloud sdk

        :param id: 参数解释： 部署ID，在[添加部署](CreateInferDeployment.xml)时即可在返回体中获取，也可通过[查询服务部署列表](ListInferDeployments.xml)获取当前用户拥有的部署，其中deployment_id字段即为部署ID。 约束限制： 不涉及。 取值范围： 部署ID。 默认取值： 不涉及。
        :type id: str
        :param name: **参数解释：** 服务部署名字
        :type name: str
        :param infer_name: 参数解释： 部署id（废弃字段）。 取值范围： 不涉及。
        :type infer_name: str
        :param create_at: **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字
        :type create_at: datetime
        :param description: 参数解释： 描述 取值范围： 不涉及。
        :type description: str
        :param pool_id: **参数解释：** 专属资源池ID。 **取值范围：** 不涉及。
        :type pool_id: str
        :param framework: **参数解释：** 算法框架。 **取值范围：** - COMMON： 普通在线服务。
        :type framework: str
        :param priority: **参数解释：** 服务优先级。 **约束限制：** 不涉及。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。
        :type priority: str
        :param secret_type: **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 不涉及。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。
        :type secret_type: str
        :param status: **参数解释：** 服务部署状态
        :type status: str
        :param count: **参数解释：** 服务实例数
        :type count: int
        :param high_avail_switch: **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** true
        :type high_avail_switch: str
        :param system_log_dump_enable: **参数解释：** 系统日志转储开关。 **约束限制：** 只有NPU资源池有，且逻辑池是没有的 **取值范围：** 不涉及 **默认取值：** false
        :type system_log_dump_enable: str
        :param unit_configs: **参数解释：** 实例单元配置。 **约束限制：** 单机推理时，个数只会为1；如果是分布式推理时，根据不同框架，实例单元配置可灵活配置。
        :type unit_configs: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfig`]
        :param update_at: **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。
        :type update_at: datetime
        :param version: **参数解释：** 当前服务版本信息。
        :type version: str
        :param version_count: **参数解释：** 服务版本数量。 **取值范围：** 不涉及。
        :type version_count: int
        :param weight: **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **约束限制：** 不涉及。 **取值范围：** [0, 100]。 **默认取值：** 不涉及。
        :type weight: int
        :param advanced_config: 
        :type advanced_config: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        :param job_id: **参数解释：** 巫山工作流ID。 **取值范围：** 不涉及。
        :type job_id: str
        :param deployment_name: 参数解释： 服务部署名字。
        :type deployment_name: str
        :param frozen_infos: **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。
        :type frozen_infos: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._infer_name = None
        self._create_at = None
        self._description = None
        self._pool_id = None
        self._framework = None
        self._priority = None
        self._secret_type = None
        self._status = None
        self._count = None
        self._high_avail_switch = None
        self._system_log_dump_enable = None
        self._unit_configs = None
        self._update_at = None
        self._version = None
        self._version_count = None
        self._weight = None
        self._advanced_config = None
        self._job_id = None
        self._deployment_name = None
        self._frozen_infos = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if infer_name is not None:
            self.infer_name = infer_name
        if create_at is not None:
            self.create_at = create_at
        if description is not None:
            self.description = description
        if pool_id is not None:
            self.pool_id = pool_id
        if framework is not None:
            self.framework = framework
        if priority is not None:
            self.priority = priority
        if secret_type is not None:
            self.secret_type = secret_type
        if status is not None:
            self.status = status
        if count is not None:
            self.count = count
        if high_avail_switch is not None:
            self.high_avail_switch = high_avail_switch
        if system_log_dump_enable is not None:
            self.system_log_dump_enable = system_log_dump_enable
        if unit_configs is not None:
            self.unit_configs = unit_configs
        if update_at is not None:
            self.update_at = update_at
        if version is not None:
            self.version = version
        if version_count is not None:
            self.version_count = version_count
        if weight is not None:
            self.weight = weight
        if advanced_config is not None:
            self.advanced_config = advanced_config
        if job_id is not None:
            self.job_id = job_id
        if deployment_name is not None:
            self.deployment_name = deployment_name
        if frozen_infos is not None:
            self.frozen_infos = frozen_infos

    @property
    def id(self):
        r"""Gets the id of this UpdateInferDeploymentScaleResponse.

        参数解释： 部署ID，在[添加部署](CreateInferDeployment.xml)时即可在返回体中获取，也可通过[查询服务部署列表](ListInferDeployments.xml)获取当前用户拥有的部署，其中deployment_id字段即为部署ID。 约束限制： 不涉及。 取值范围： 部署ID。 默认取值： 不涉及。

        :return: The id of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateInferDeploymentScaleResponse.

        参数解释： 部署ID，在[添加部署](CreateInferDeployment.xml)时即可在返回体中获取，也可通过[查询服务部署列表](ListInferDeployments.xml)获取当前用户拥有的部署，其中deployment_id字段即为部署ID。 约束限制： 不涉及。 取值范围： 部署ID。 默认取值： 不涉及。

        :param id: The id of this UpdateInferDeploymentScaleResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 服务部署名字

        :return: The name of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 服务部署名字

        :param name: The name of this UpdateInferDeploymentScaleResponse.
        :type name: str
        """
        self._name = name

    @property
    def infer_name(self):
        r"""Gets the infer_name of this UpdateInferDeploymentScaleResponse.

        参数解释： 部署id（废弃字段）。 取值范围： 不涉及。

        :return: The infer_name of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._infer_name

    @infer_name.setter
    def infer_name(self, infer_name):
        r"""Sets the infer_name of this UpdateInferDeploymentScaleResponse.

        参数解释： 部署id（废弃字段）。 取值范围： 不涉及。

        :param infer_name: The infer_name of this UpdateInferDeploymentScaleResponse.
        :type infer_name: str
        """
        self._infer_name = infer_name

    @property
    def create_at(self):
        r"""Gets the create_at of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字

        :return: The create_at of this UpdateInferDeploymentScaleResponse.
        :rtype: datetime
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字

        :param create_at: The create_at of this UpdateInferDeploymentScaleResponse.
        :type create_at: datetime
        """
        self._create_at = create_at

    @property
    def description(self):
        r"""Gets the description of this UpdateInferDeploymentScaleResponse.

        参数解释： 描述 取值范围： 不涉及。

        :return: The description of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateInferDeploymentScaleResponse.

        参数解释： 描述 取值范围： 不涉及。

        :param description: The description of this UpdateInferDeploymentScaleResponse.
        :type description: str
        """
        self._description = description

    @property
    def pool_id(self):
        r"""Gets the pool_id of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 专属资源池ID。 **取值范围：** 不涉及。

        :return: The pool_id of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 专属资源池ID。 **取值范围：** 不涉及。

        :param pool_id: The pool_id of this UpdateInferDeploymentScaleResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def framework(self):
        r"""Gets the framework of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 算法框架。 **取值范围：** - COMMON： 普通在线服务。

        :return: The framework of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        r"""Sets the framework of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 算法框架。 **取值范围：** - COMMON： 普通在线服务。

        :param framework: The framework of this UpdateInferDeploymentScaleResponse.
        :type framework: str
        """
        self._framework = framework

    @property
    def priority(self):
        r"""Gets the priority of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 服务优先级。 **约束限制：** 不涉及。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。

        :return: The priority of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 服务优先级。 **约束限制：** 不涉及。 **取值范围：** [1, 3]。 **默认取值：** 不涉及。

        :param priority: The priority of this UpdateInferDeploymentScaleResponse.
        :type priority: str
        """
        self._priority = priority

    @property
    def secret_type(self):
        r"""Gets the secret_type of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 不涉及。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。

        :return: The secret_type of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._secret_type

    @secret_type.setter
    def secret_type(self, secret_type):
        r"""Sets the secret_type of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 凭证类型相关配置，用户可以在此处选择使用的凭证类型（dew，agency） **约束限制：** 不涉及。 **取值范围：** - [dew：DEW密钥。](tag:hws,hws_hk,fcs) - agency：临时委托凭证。 **默认取值：** 不涉及。

        :param secret_type: The secret_type of this UpdateInferDeploymentScaleResponse.
        :type secret_type: str
        """
        self._secret_type = secret_type

    @property
    def status(self):
        r"""Gets the status of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 服务部署状态

        :return: The status of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 服务部署状态

        :param status: The status of this UpdateInferDeploymentScaleResponse.
        :type status: str
        """
        self._status = status

    @property
    def count(self):
        r"""Gets the count of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 服务实例数

        :return: The count of this UpdateInferDeploymentScaleResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 服务实例数

        :param count: The count of this UpdateInferDeploymentScaleResponse.
        :type count: int
        """
        self._count = count

    @property
    def high_avail_switch(self):
        r"""Gets the high_avail_switch of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** true

        :return: The high_avail_switch of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._high_avail_switch

    @high_avail_switch.setter
    def high_avail_switch(self, high_avail_switch):
        r"""Sets the high_avail_switch of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 高可用开关，开启后不同实例的pod将尽量均匀分布到不同的节点上。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** true

        :param high_avail_switch: The high_avail_switch of this UpdateInferDeploymentScaleResponse.
        :type high_avail_switch: str
        """
        self._high_avail_switch = high_avail_switch

    @property
    def system_log_dump_enable(self):
        r"""Gets the system_log_dump_enable of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 系统日志转储开关。 **约束限制：** 只有NPU资源池有，且逻辑池是没有的 **取值范围：** 不涉及 **默认取值：** false

        :return: The system_log_dump_enable of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._system_log_dump_enable

    @system_log_dump_enable.setter
    def system_log_dump_enable(self, system_log_dump_enable):
        r"""Sets the system_log_dump_enable of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 系统日志转储开关。 **约束限制：** 只有NPU资源池有，且逻辑池是没有的 **取值范围：** 不涉及 **默认取值：** false

        :param system_log_dump_enable: The system_log_dump_enable of this UpdateInferDeploymentScaleResponse.
        :type system_log_dump_enable: str
        """
        self._system_log_dump_enable = system_log_dump_enable

    @property
    def unit_configs(self):
        r"""Gets the unit_configs of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 实例单元配置。 **约束限制：** 单机推理时，个数只会为1；如果是分布式推理时，根据不同框架，实例单元配置可灵活配置。

        :return: The unit_configs of this UpdateInferDeploymentScaleResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfig`]
        """
        return self._unit_configs

    @unit_configs.setter
    def unit_configs(self, unit_configs):
        r"""Sets the unit_configs of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 实例单元配置。 **约束限制：** 单机推理时，个数只会为1；如果是分布式推理时，根据不同框架，实例单元配置可灵活配置。

        :param unit_configs: The unit_configs of this UpdateInferDeploymentScaleResponse.
        :type unit_configs: list[:class:`huaweicloudsdkmodelarts.v1.UnitConfig`]
        """
        self._unit_configs = unit_configs

    @property
    def update_at(self):
        r"""Gets the update_at of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :return: The update_at of this UpdateInferDeploymentScaleResponse.
        :rtype: datetime
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 更新时间，根据更新时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字。

        :param update_at: The update_at of this UpdateInferDeploymentScaleResponse.
        :type update_at: datetime
        """
        self._update_at = update_at

    @property
    def version(self):
        r"""Gets the version of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 当前服务版本信息。

        :return: The version of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 当前服务版本信息。

        :param version: The version of this UpdateInferDeploymentScaleResponse.
        :type version: str
        """
        self._version = version

    @property
    def version_count(self):
        r"""Gets the version_count of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 服务版本数量。 **取值范围：** 不涉及。

        :return: The version_count of this UpdateInferDeploymentScaleResponse.
        :rtype: int
        """
        return self._version_count

    @version_count.setter
    def version_count(self, version_count):
        r"""Sets the version_count of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 服务版本数量。 **取值范围：** 不涉及。

        :param version_count: The version_count of this UpdateInferDeploymentScaleResponse.
        :type version_count: int
        """
        self._version_count = version_count

    @property
    def weight(self):
        r"""Gets the weight of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **约束限制：** 不涉及。 **取值范围：** [0, 100]。 **默认取值：** 不涉及。

        :return: The weight of this UpdateInferDeploymentScaleResponse.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 权重百分比，分配到此模型的流量权重，仅当模型部署为在线服务时需要配置。 **约束限制：** 不涉及。 **取值范围：** [0, 100]。 **默认取值：** 不涉及。

        :param weight: The weight of this UpdateInferDeploymentScaleResponse.
        :type weight: int
        """
        self._weight = weight

    @property
    def advanced_config(self):
        r"""Gets the advanced_config of this UpdateInferDeploymentScaleResponse.

        :return: The advanced_config of this UpdateInferDeploymentScaleResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        """
        return self._advanced_config

    @advanced_config.setter
    def advanced_config(self, advanced_config):
        r"""Sets the advanced_config of this UpdateInferDeploymentScaleResponse.

        :param advanced_config: The advanced_config of this UpdateInferDeploymentScaleResponse.
        :type advanced_config: :class:`huaweicloudsdkmodelarts.v1.AdvancedConfig`
        """
        self._advanced_config = advanced_config

    @property
    def job_id(self):
        r"""Gets the job_id of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 巫山工作流ID。 **取值范围：** 不涉及。

        :return: The job_id of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 巫山工作流ID。 **取值范围：** 不涉及。

        :param job_id: The job_id of this UpdateInferDeploymentScaleResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def deployment_name(self):
        r"""Gets the deployment_name of this UpdateInferDeploymentScaleResponse.

        参数解释： 服务部署名字。

        :return: The deployment_name of this UpdateInferDeploymentScaleResponse.
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        r"""Sets the deployment_name of this UpdateInferDeploymentScaleResponse.

        参数解释： 服务部署名字。

        :param deployment_name: The deployment_name of this UpdateInferDeploymentScaleResponse.
        :type deployment_name: str
        """
        self._deployment_name = deployment_name

    @property
    def frozen_infos(self):
        r"""Gets the frozen_infos of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。

        :return: The frozen_infos of this UpdateInferDeploymentScaleResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        return self._frozen_infos

    @frozen_infos.setter
    def frozen_infos(self, frozen_infos):
        r"""Sets the frozen_infos of this UpdateInferDeploymentScaleResponse.

        **参数解释：** 当服务或者部署被冻结时返回的冻结类型信息。

        :param frozen_infos: The frozen_infos of this UpdateInferDeploymentScaleResponse.
        :type frozen_infos: list[:class:`huaweicloudsdkmodelarts.v1.FrozenInfo`]
        """
        self._frozen_infos = frozen_infos

    def to_dict(self):
        import warnings
        warnings.warn("UpdateInferDeploymentScaleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateInferDeploymentScaleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
