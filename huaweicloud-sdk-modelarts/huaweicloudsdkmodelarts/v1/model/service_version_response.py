# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceVersionResponse:

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
        'version': 'str',
        'description': 'str',
        'predict_url': 'str',
        'runtime_config': 'RuntimeConfigResponse',
        'upgrade_config': 'UpgradeConfigResponse',
        'instance_groups': 'list[GroupConfigResponse]',
        'lts_strategy': 'str',
        'lts_status': 'str',
        'lts_event_status': 'str',
        'log_configs': 'list[LogConfigResponse]',
        'deploy_timeout_minutes': 'int'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'description': 'description',
        'predict_url': 'predict_url',
        'runtime_config': 'runtime_config',
        'upgrade_config': 'upgrade_config',
        'instance_groups': 'instance_groups',
        'lts_strategy': 'lts_strategy',
        'lts_status': 'lts_status',
        'lts_event_status': 'lts_event_status',
        'log_configs': 'log_configs',
        'deploy_timeout_minutes': 'deploy_timeout_minutes'
    }

    def __init__(self, id=None, version=None, description=None, predict_url=None, runtime_config=None, upgrade_config=None, instance_groups=None, lts_strategy=None, lts_status=None, lts_event_status=None, log_configs=None, deploy_timeout_minutes=None):
        r"""ServiceVersionResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 版本id。 **取值范围：** 不涉及。
        :type id: str
        :param version: **参数解释：** 版本号。 **取值范围：** 不涉及。
        :type version: str
        :param description: **参数解释：** 描述。 **取值范围：** 不涉及。
        :type description: str
        :param predict_url: **参数解释：** 推理请求的访问地址。 **取值范围：** 不涉及。
        :type predict_url: str
        :param runtime_config: 
        :type runtime_config: :class:`huaweicloudsdkmodelarts.v1.RuntimeConfigResponse`
        :param upgrade_config: 
        :type upgrade_config: :class:`huaweicloudsdkmodelarts.v1.UpgradeConfigResponse`
        :param instance_groups: **参数解释：** 服务部署信息。
        :type instance_groups: list[:class:`huaweicloudsdkmodelarts.v1.GroupConfigResponse`]
        :param lts_strategy: **参数解释：** 日志策略。 **取值范围：** - POOL：使用资源池日志插件配置的日志流。 - AUTO_CREATE：自动创建日志流。 - DEFAULT: 由系统决定日志策略
        :type lts_strategy: str
        :param lts_status: **参数解释：** 部署对接lts状态。 **取值范围：** - ON：开启。 - OFF：关闭。
        :type lts_status: str
        :param lts_event_status: **参数解释：** 部署对接lts k8s事件状态。 **取值范围：** - ON：开启。 - OFF：关闭。
        :type lts_event_status: str
        :param log_configs: **参数解释：** 服务日志配置信息。
        :type log_configs: list[:class:`huaweicloudsdkmodelarts.v1.LogConfigResponse`]
        :param deploy_timeout_minutes: **参数解释：** 部署超时时间。 **取值范围：** 不涉及。
        :type deploy_timeout_minutes: int
        """
        
        

        self._id = None
        self._version = None
        self._description = None
        self._predict_url = None
        self._runtime_config = None
        self._upgrade_config = None
        self._instance_groups = None
        self._lts_strategy = None
        self._lts_status = None
        self._lts_event_status = None
        self._log_configs = None
        self._deploy_timeout_minutes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if predict_url is not None:
            self.predict_url = predict_url
        if runtime_config is not None:
            self.runtime_config = runtime_config
        if upgrade_config is not None:
            self.upgrade_config = upgrade_config
        if instance_groups is not None:
            self.instance_groups = instance_groups
        if lts_strategy is not None:
            self.lts_strategy = lts_strategy
        if lts_status is not None:
            self.lts_status = lts_status
        if lts_event_status is not None:
            self.lts_event_status = lts_event_status
        if log_configs is not None:
            self.log_configs = log_configs
        if deploy_timeout_minutes is not None:
            self.deploy_timeout_minutes = deploy_timeout_minutes

    @property
    def id(self):
        r"""Gets the id of this ServiceVersionResponse.

        **参数解释：** 版本id。 **取值范围：** 不涉及。

        :return: The id of this ServiceVersionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServiceVersionResponse.

        **参数解释：** 版本id。 **取值范围：** 不涉及。

        :param id: The id of this ServiceVersionResponse.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this ServiceVersionResponse.

        **参数解释：** 版本号。 **取值范围：** 不涉及。

        :return: The version of this ServiceVersionResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ServiceVersionResponse.

        **参数解释：** 版本号。 **取值范围：** 不涉及。

        :param version: The version of this ServiceVersionResponse.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        r"""Gets the description of this ServiceVersionResponse.

        **参数解释：** 描述。 **取值范围：** 不涉及。

        :return: The description of this ServiceVersionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ServiceVersionResponse.

        **参数解释：** 描述。 **取值范围：** 不涉及。

        :param description: The description of this ServiceVersionResponse.
        :type description: str
        """
        self._description = description

    @property
    def predict_url(self):
        r"""Gets the predict_url of this ServiceVersionResponse.

        **参数解释：** 推理请求的访问地址。 **取值范围：** 不涉及。

        :return: The predict_url of this ServiceVersionResponse.
        :rtype: str
        """
        return self._predict_url

    @predict_url.setter
    def predict_url(self, predict_url):
        r"""Sets the predict_url of this ServiceVersionResponse.

        **参数解释：** 推理请求的访问地址。 **取值范围：** 不涉及。

        :param predict_url: The predict_url of this ServiceVersionResponse.
        :type predict_url: str
        """
        self._predict_url = predict_url

    @property
    def runtime_config(self):
        r"""Gets the runtime_config of this ServiceVersionResponse.

        :return: The runtime_config of this ServiceVersionResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.RuntimeConfigResponse`
        """
        return self._runtime_config

    @runtime_config.setter
    def runtime_config(self, runtime_config):
        r"""Sets the runtime_config of this ServiceVersionResponse.

        :param runtime_config: The runtime_config of this ServiceVersionResponse.
        :type runtime_config: :class:`huaweicloudsdkmodelarts.v1.RuntimeConfigResponse`
        """
        self._runtime_config = runtime_config

    @property
    def upgrade_config(self):
        r"""Gets the upgrade_config of this ServiceVersionResponse.

        :return: The upgrade_config of this ServiceVersionResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.UpgradeConfigResponse`
        """
        return self._upgrade_config

    @upgrade_config.setter
    def upgrade_config(self, upgrade_config):
        r"""Sets the upgrade_config of this ServiceVersionResponse.

        :param upgrade_config: The upgrade_config of this ServiceVersionResponse.
        :type upgrade_config: :class:`huaweicloudsdkmodelarts.v1.UpgradeConfigResponse`
        """
        self._upgrade_config = upgrade_config

    @property
    def instance_groups(self):
        r"""Gets the instance_groups of this ServiceVersionResponse.

        **参数解释：** 服务部署信息。

        :return: The instance_groups of this ServiceVersionResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.GroupConfigResponse`]
        """
        return self._instance_groups

    @instance_groups.setter
    def instance_groups(self, instance_groups):
        r"""Sets the instance_groups of this ServiceVersionResponse.

        **参数解释：** 服务部署信息。

        :param instance_groups: The instance_groups of this ServiceVersionResponse.
        :type instance_groups: list[:class:`huaweicloudsdkmodelarts.v1.GroupConfigResponse`]
        """
        self._instance_groups = instance_groups

    @property
    def lts_strategy(self):
        r"""Gets the lts_strategy of this ServiceVersionResponse.

        **参数解释：** 日志策略。 **取值范围：** - POOL：使用资源池日志插件配置的日志流。 - AUTO_CREATE：自动创建日志流。 - DEFAULT: 由系统决定日志策略

        :return: The lts_strategy of this ServiceVersionResponse.
        :rtype: str
        """
        return self._lts_strategy

    @lts_strategy.setter
    def lts_strategy(self, lts_strategy):
        r"""Sets the lts_strategy of this ServiceVersionResponse.

        **参数解释：** 日志策略。 **取值范围：** - POOL：使用资源池日志插件配置的日志流。 - AUTO_CREATE：自动创建日志流。 - DEFAULT: 由系统决定日志策略

        :param lts_strategy: The lts_strategy of this ServiceVersionResponse.
        :type lts_strategy: str
        """
        self._lts_strategy = lts_strategy

    @property
    def lts_status(self):
        r"""Gets the lts_status of this ServiceVersionResponse.

        **参数解释：** 部署对接lts状态。 **取值范围：** - ON：开启。 - OFF：关闭。

        :return: The lts_status of this ServiceVersionResponse.
        :rtype: str
        """
        return self._lts_status

    @lts_status.setter
    def lts_status(self, lts_status):
        r"""Sets the lts_status of this ServiceVersionResponse.

        **参数解释：** 部署对接lts状态。 **取值范围：** - ON：开启。 - OFF：关闭。

        :param lts_status: The lts_status of this ServiceVersionResponse.
        :type lts_status: str
        """
        self._lts_status = lts_status

    @property
    def lts_event_status(self):
        r"""Gets the lts_event_status of this ServiceVersionResponse.

        **参数解释：** 部署对接lts k8s事件状态。 **取值范围：** - ON：开启。 - OFF：关闭。

        :return: The lts_event_status of this ServiceVersionResponse.
        :rtype: str
        """
        return self._lts_event_status

    @lts_event_status.setter
    def lts_event_status(self, lts_event_status):
        r"""Sets the lts_event_status of this ServiceVersionResponse.

        **参数解释：** 部署对接lts k8s事件状态。 **取值范围：** - ON：开启。 - OFF：关闭。

        :param lts_event_status: The lts_event_status of this ServiceVersionResponse.
        :type lts_event_status: str
        """
        self._lts_event_status = lts_event_status

    @property
    def log_configs(self):
        r"""Gets the log_configs of this ServiceVersionResponse.

        **参数解释：** 服务日志配置信息。

        :return: The log_configs of this ServiceVersionResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.LogConfigResponse`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        r"""Sets the log_configs of this ServiceVersionResponse.

        **参数解释：** 服务日志配置信息。

        :param log_configs: The log_configs of this ServiceVersionResponse.
        :type log_configs: list[:class:`huaweicloudsdkmodelarts.v1.LogConfigResponse`]
        """
        self._log_configs = log_configs

    @property
    def deploy_timeout_minutes(self):
        r"""Gets the deploy_timeout_minutes of this ServiceVersionResponse.

        **参数解释：** 部署超时时间。 **取值范围：** 不涉及。

        :return: The deploy_timeout_minutes of this ServiceVersionResponse.
        :rtype: int
        """
        return self._deploy_timeout_minutes

    @deploy_timeout_minutes.setter
    def deploy_timeout_minutes(self, deploy_timeout_minutes):
        r"""Sets the deploy_timeout_minutes of this ServiceVersionResponse.

        **参数解释：** 部署超时时间。 **取值范围：** 不涉及。

        :param deploy_timeout_minutes: The deploy_timeout_minutes of this ServiceVersionResponse.
        :type deploy_timeout_minutes: int
        """
        self._deploy_timeout_minutes = deploy_timeout_minutes

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
        if not isinstance(other, ServiceVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
