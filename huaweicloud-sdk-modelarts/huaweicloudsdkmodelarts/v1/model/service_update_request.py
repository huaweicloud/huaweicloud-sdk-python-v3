# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceUpdateRequest:

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
        'deploy_timeout_minutes': 'int',
        'version': 'str',
        'description': 'str',
        'group_configs': 'list[GroupConfig]',
        'runtime_config': 'RuntimeConfig',
        'upgrade_config': 'UpgradeConfig',
        'lts_strategy': 'str',
        'log_configs': 'list[LtsConfig]',
        'tags': 'str',
        'workspace_id': 'str',
        'schedule': 'list[ScheduleConfig]',
        'custom_metrics_path': 'str',
        'task_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'deploy_timeout_minutes': 'deploy_timeout_minutes',
        'version': 'version',
        'description': 'description',
        'group_configs': 'group_configs',
        'runtime_config': 'runtime_config',
        'upgrade_config': 'upgrade_config',
        'lts_strategy': 'lts_strategy',
        'log_configs': 'log_configs',
        'tags': 'tags',
        'workspace_id': 'workspace_id',
        'schedule': 'schedule',
        'custom_metrics_path': 'custom_metrics_path',
        'task_type': 'task_type'
    }

    def __init__(self, id=None, name=None, deploy_timeout_minutes=None, version=None, description=None, group_configs=None, runtime_config=None, upgrade_config=None, lts_strategy=None, log_configs=None, tags=None, workspace_id=None, schedule=None, custom_metrics_path=None, task_type=None):
        r"""ServiceUpdateRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 服务ID **约束限制：** 不涉及。 **取值范围：** 不涉及
        :type id: str
        :param name: **参数解释：** 服务名称。 **约束限制：** 不涉及。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。 **默认取值：** 不涉及。
        :type name: str
        :param deploy_timeout_minutes: **参数解释：** 服务部署超时时间，integer类型，取值在1~300（860版本该参数做保留兼容）。 **约束限制：** 不涉及。 **取值范围：** [0, 300]。 **默认取值：** 不涉及。
        :type deploy_timeout_minutes: int
        :param version: **参数解释：** 必填，填了之后，数据库中如果存在相同版本号，将会报错（仅修改描述的场景除外）。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type version: str
        :param description: **参数解释：** 非必填，仅更新描述的场景直接修改对应version的数据库字段，不新增版本号。 **约束限制：** 不涉及。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        :param group_configs: **参数解释：** 仅修改服务时不需传，兼容部署分离之前版本。 **约束限制：** group_configs的最大元素数量为1。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type group_configs: list[:class:`huaweicloudsdkmodelarts.v1.GroupConfig`]
        :param runtime_config: 
        :type runtime_config: :class:`huaweicloudsdkmodelarts.v1.RuntimeConfig`
        :param upgrade_config: 
        :type upgrade_config: :class:`huaweicloudsdkmodelarts.v1.UpgradeConfig`
        :param lts_strategy: **参数解释：** 日志策略。 **约束限制：** 不涉及。 **取值范围：** - POOL：使用资源池日志插件配置的日志流。 - AUTO_CREATE：自动创建日志流。 - DEFAULT: 由系统决定日志策略 **默认取值：** AUTO_CREATE：自动创建日志流。
        :type lts_strategy: str
        :param log_configs: **参数解释：** 日志配置，当开启LTS日志的时候，STDOUT类型为必填。 **约束限制：** 当开启LTS日志的时候，STDOUT类型为必填。 数量上限为2个。
        :type log_configs: list[:class:`huaweicloudsdkmodelarts.v1.LtsConfig`]
        :param tags: **参数解释：** 服务标签,上限20个 **约束限制：** 不涉及。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tags: str
        :param workspace_id: **参数解释：** 工作空间id，默认是“0” **约束限制：** 不涉及。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type workspace_id: str
        :param schedule: **参数解释：** 定时停止配置。 **约束限制：** 仅当body中另一个参数description为空时，此参数才生效。
        :type schedule: list[:class:`huaweicloudsdkmodelarts.v1.ScheduleConfig`]
        :param custom_metrics_path: **参数解释：** 该参数值由英文逗号隔开的协议、端口号、地址组成，其中地址长度不超过255 ，且需要与镜像给定的协议、地址、端口一致，否则指标无法上报。
        :type custom_metrics_path: str
        :param task_type: **参数解释：** 模型类型。 **取值范围：** - TEXT_GENERATION：文本生成 - IMAGE_UNDERSTANDING：图像理解 - VIDEO_GENERATION：视频生成 - IMAGE_GENERATION：图像生成 - RERANK：重排序 - VECTOR_MODEL：向量模型 - EMBEDDING：Embedding嵌入
        :type task_type: str
        """
        
        

        self._id = None
        self._name = None
        self._deploy_timeout_minutes = None
        self._version = None
        self._description = None
        self._group_configs = None
        self._runtime_config = None
        self._upgrade_config = None
        self._lts_strategy = None
        self._log_configs = None
        self._tags = None
        self._workspace_id = None
        self._schedule = None
        self._custom_metrics_path = None
        self._task_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if deploy_timeout_minutes is not None:
            self.deploy_timeout_minutes = deploy_timeout_minutes
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if group_configs is not None:
            self.group_configs = group_configs
        if runtime_config is not None:
            self.runtime_config = runtime_config
        if upgrade_config is not None:
            self.upgrade_config = upgrade_config
        if lts_strategy is not None:
            self.lts_strategy = lts_strategy
        if log_configs is not None:
            self.log_configs = log_configs
        if tags is not None:
            self.tags = tags
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if schedule is not None:
            self.schedule = schedule
        if custom_metrics_path is not None:
            self.custom_metrics_path = custom_metrics_path
        if task_type is not None:
            self.task_type = task_type

    @property
    def id(self):
        r"""Gets the id of this ServiceUpdateRequest.

        **参数解释：** 服务ID **约束限制：** 不涉及。 **取值范围：** 不涉及

        :return: The id of this ServiceUpdateRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServiceUpdateRequest.

        **参数解释：** 服务ID **约束限制：** 不涉及。 **取值范围：** 不涉及

        :param id: The id of this ServiceUpdateRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ServiceUpdateRequest.

        **参数解释：** 服务名称。 **约束限制：** 不涉及。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。 **默认取值：** 不涉及。

        :return: The name of this ServiceUpdateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServiceUpdateRequest.

        **参数解释：** 服务名称。 **约束限制：** 不涉及。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。 **默认取值：** 不涉及。

        :param name: The name of this ServiceUpdateRequest.
        :type name: str
        """
        self._name = name

    @property
    def deploy_timeout_minutes(self):
        r"""Gets the deploy_timeout_minutes of this ServiceUpdateRequest.

        **参数解释：** 服务部署超时时间，integer类型，取值在1~300（860版本该参数做保留兼容）。 **约束限制：** 不涉及。 **取值范围：** [0, 300]。 **默认取值：** 不涉及。

        :return: The deploy_timeout_minutes of this ServiceUpdateRequest.
        :rtype: int
        """
        return self._deploy_timeout_minutes

    @deploy_timeout_minutes.setter
    def deploy_timeout_minutes(self, deploy_timeout_minutes):
        r"""Sets the deploy_timeout_minutes of this ServiceUpdateRequest.

        **参数解释：** 服务部署超时时间，integer类型，取值在1~300（860版本该参数做保留兼容）。 **约束限制：** 不涉及。 **取值范围：** [0, 300]。 **默认取值：** 不涉及。

        :param deploy_timeout_minutes: The deploy_timeout_minutes of this ServiceUpdateRequest.
        :type deploy_timeout_minutes: int
        """
        self._deploy_timeout_minutes = deploy_timeout_minutes

    @property
    def version(self):
        r"""Gets the version of this ServiceUpdateRequest.

        **参数解释：** 必填，填了之后，数据库中如果存在相同版本号，将会报错（仅修改描述的场景除外）。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The version of this ServiceUpdateRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ServiceUpdateRequest.

        **参数解释：** 必填，填了之后，数据库中如果存在相同版本号，将会报错（仅修改描述的场景除外）。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param version: The version of this ServiceUpdateRequest.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        r"""Gets the description of this ServiceUpdateRequest.

        **参数解释：** 非必填，仅更新描述的场景直接修改对应version的数据库字段，不新增版本号。 **约束限制：** 不涉及。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this ServiceUpdateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ServiceUpdateRequest.

        **参数解释：** 非必填，仅更新描述的场景直接修改对应version的数据库字段，不新增版本号。 **约束限制：** 不涉及。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this ServiceUpdateRequest.
        :type description: str
        """
        self._description = description

    @property
    def group_configs(self):
        r"""Gets the group_configs of this ServiceUpdateRequest.

        **参数解释：** 仅修改服务时不需传，兼容部署分离之前版本。 **约束限制：** group_configs的最大元素数量为1。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The group_configs of this ServiceUpdateRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.GroupConfig`]
        """
        return self._group_configs

    @group_configs.setter
    def group_configs(self, group_configs):
        r"""Sets the group_configs of this ServiceUpdateRequest.

        **参数解释：** 仅修改服务时不需传，兼容部署分离之前版本。 **约束限制：** group_configs的最大元素数量为1。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param group_configs: The group_configs of this ServiceUpdateRequest.
        :type group_configs: list[:class:`huaweicloudsdkmodelarts.v1.GroupConfig`]
        """
        self._group_configs = group_configs

    @property
    def runtime_config(self):
        r"""Gets the runtime_config of this ServiceUpdateRequest.

        :return: The runtime_config of this ServiceUpdateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.RuntimeConfig`
        """
        return self._runtime_config

    @runtime_config.setter
    def runtime_config(self, runtime_config):
        r"""Sets the runtime_config of this ServiceUpdateRequest.

        :param runtime_config: The runtime_config of this ServiceUpdateRequest.
        :type runtime_config: :class:`huaweicloudsdkmodelarts.v1.RuntimeConfig`
        """
        self._runtime_config = runtime_config

    @property
    def upgrade_config(self):
        r"""Gets the upgrade_config of this ServiceUpdateRequest.

        :return: The upgrade_config of this ServiceUpdateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpgradeConfig`
        """
        return self._upgrade_config

    @upgrade_config.setter
    def upgrade_config(self, upgrade_config):
        r"""Sets the upgrade_config of this ServiceUpdateRequest.

        :param upgrade_config: The upgrade_config of this ServiceUpdateRequest.
        :type upgrade_config: :class:`huaweicloudsdkmodelarts.v1.UpgradeConfig`
        """
        self._upgrade_config = upgrade_config

    @property
    def lts_strategy(self):
        r"""Gets the lts_strategy of this ServiceUpdateRequest.

        **参数解释：** 日志策略。 **约束限制：** 不涉及。 **取值范围：** - POOL：使用资源池日志插件配置的日志流。 - AUTO_CREATE：自动创建日志流。 - DEFAULT: 由系统决定日志策略 **默认取值：** AUTO_CREATE：自动创建日志流。

        :return: The lts_strategy of this ServiceUpdateRequest.
        :rtype: str
        """
        return self._lts_strategy

    @lts_strategy.setter
    def lts_strategy(self, lts_strategy):
        r"""Sets the lts_strategy of this ServiceUpdateRequest.

        **参数解释：** 日志策略。 **约束限制：** 不涉及。 **取值范围：** - POOL：使用资源池日志插件配置的日志流。 - AUTO_CREATE：自动创建日志流。 - DEFAULT: 由系统决定日志策略 **默认取值：** AUTO_CREATE：自动创建日志流。

        :param lts_strategy: The lts_strategy of this ServiceUpdateRequest.
        :type lts_strategy: str
        """
        self._lts_strategy = lts_strategy

    @property
    def log_configs(self):
        r"""Gets the log_configs of this ServiceUpdateRequest.

        **参数解释：** 日志配置，当开启LTS日志的时候，STDOUT类型为必填。 **约束限制：** 当开启LTS日志的时候，STDOUT类型为必填。 数量上限为2个。

        :return: The log_configs of this ServiceUpdateRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.LtsConfig`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        r"""Sets the log_configs of this ServiceUpdateRequest.

        **参数解释：** 日志配置，当开启LTS日志的时候，STDOUT类型为必填。 **约束限制：** 当开启LTS日志的时候，STDOUT类型为必填。 数量上限为2个。

        :param log_configs: The log_configs of this ServiceUpdateRequest.
        :type log_configs: list[:class:`huaweicloudsdkmodelarts.v1.LtsConfig`]
        """
        self._log_configs = log_configs

    @property
    def tags(self):
        r"""Gets the tags of this ServiceUpdateRequest.

        **参数解释：** 服务标签,上限20个 **约束限制：** 不涉及。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tags of this ServiceUpdateRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ServiceUpdateRequest.

        **参数解释：** 服务标签,上限20个 **约束限制：** 不涉及。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tags: The tags of this ServiceUpdateRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ServiceUpdateRequest.

        **参数解释：** 工作空间id，默认是“0” **约束限制：** 不涉及。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The workspace_id of this ServiceUpdateRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ServiceUpdateRequest.

        **参数解释：** 工作空间id，默认是“0” **约束限制：** 不涉及。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param workspace_id: The workspace_id of this ServiceUpdateRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def schedule(self):
        r"""Gets the schedule of this ServiceUpdateRequest.

        **参数解释：** 定时停止配置。 **约束限制：** 仅当body中另一个参数description为空时，此参数才生效。

        :return: The schedule of this ServiceUpdateRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ScheduleConfig`]
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this ServiceUpdateRequest.

        **参数解释：** 定时停止配置。 **约束限制：** 仅当body中另一个参数description为空时，此参数才生效。

        :param schedule: The schedule of this ServiceUpdateRequest.
        :type schedule: list[:class:`huaweicloudsdkmodelarts.v1.ScheduleConfig`]
        """
        self._schedule = schedule

    @property
    def custom_metrics_path(self):
        r"""Gets the custom_metrics_path of this ServiceUpdateRequest.

        **参数解释：** 该参数值由英文逗号隔开的协议、端口号、地址组成，其中地址长度不超过255 ，且需要与镜像给定的协议、地址、端口一致，否则指标无法上报。

        :return: The custom_metrics_path of this ServiceUpdateRequest.
        :rtype: str
        """
        return self._custom_metrics_path

    @custom_metrics_path.setter
    def custom_metrics_path(self, custom_metrics_path):
        r"""Sets the custom_metrics_path of this ServiceUpdateRequest.

        **参数解释：** 该参数值由英文逗号隔开的协议、端口号、地址组成，其中地址长度不超过255 ，且需要与镜像给定的协议、地址、端口一致，否则指标无法上报。

        :param custom_metrics_path: The custom_metrics_path of this ServiceUpdateRequest.
        :type custom_metrics_path: str
        """
        self._custom_metrics_path = custom_metrics_path

    @property
    def task_type(self):
        r"""Gets the task_type of this ServiceUpdateRequest.

        **参数解释：** 模型类型。 **取值范围：** - TEXT_GENERATION：文本生成 - IMAGE_UNDERSTANDING：图像理解 - VIDEO_GENERATION：视频生成 - IMAGE_GENERATION：图像生成 - RERANK：重排序 - VECTOR_MODEL：向量模型 - EMBEDDING：Embedding嵌入

        :return: The task_type of this ServiceUpdateRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ServiceUpdateRequest.

        **参数解释：** 模型类型。 **取值范围：** - TEXT_GENERATION：文本生成 - IMAGE_UNDERSTANDING：图像理解 - VIDEO_GENERATION：视频生成 - IMAGE_GENERATION：图像生成 - RERANK：重排序 - VECTOR_MODEL：向量模型 - EMBEDDING：Embedding嵌入

        :param task_type: The task_type of this ServiceUpdateRequest.
        :type task_type: str
        """
        self._task_type = task_type

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
        if not isinstance(other, ServiceUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
