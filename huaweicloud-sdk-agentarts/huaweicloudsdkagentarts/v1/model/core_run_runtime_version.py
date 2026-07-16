# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunRuntimeVersion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'artifact_source': 'CoreRunArtifactSourceResp',
        'network_config': 'CoreRunOutboundNetworkResp',
        'environment_variables': 'list[CoreRunEnvironmentVariableResp]',
        'invoke_config': 'CoreRunInvokeConfigResp',
        'observability': 'CoreRunObservabilityResp',
        'storage_config': 'CoreRunStorageConfig',
        'health_config': 'CoreHealthCheckConfig'
    }

    attribute_map = {
        'version': 'version',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'artifact_source': 'artifact_source',
        'network_config': 'network_config',
        'environment_variables': 'environment_variables',
        'invoke_config': 'invoke_config',
        'observability': 'observability',
        'storage_config': 'storage_config',
        'health_config': 'health_config'
    }

    def __init__(self, version=None, description=None, created_at=None, updated_at=None, artifact_source=None, network_config=None, environment_variables=None, invoke_config=None, observability=None, storage_config=None, health_config=None):
        r"""CoreRunRuntimeVersion

        The model defined in huaweicloud sdk

        :param version: **参数解释**: 版本名称，默认为v1、v2自增长，用户也可自定义。 **取值范围**: 以小写字母或数字开头，以小写字母或数字结尾，可以包含小写字母、数字和中划线，长度为2-24个字符。 
        :type version: str
        :param description: **参数解释**: 版本描述（创建/更新版本时可选）。 **取值范围**: 长度为 0 - 4096 个字符。 
        :type description: str
        :param created_at: **参数解释**: 创建时间（系统自动生成，UTC时区）。 **取值范围**: 不涉及。 
        :type created_at: datetime
        :param updated_at: **参数解释**: 最近更新时间（系统自动生成，版本更新/标签修改时刷新）。 **取值范围**: 不涉及。 
        :type updated_at: datetime
        :param artifact_source: 
        :type artifact_source: :class:`huaweicloudsdkagentarts.v1.CoreRunArtifactSourceResp`
        :param network_config: 
        :type network_config: :class:`huaweicloudsdkagentarts.v1.CoreRunOutboundNetworkResp`
        :param environment_variables: **参数解释**: 环境变量配置列表，用于配置运行时环境变量。 **取值范围**: 支持0 - 1024个元素。 
        :type environment_variables: list[:class:`huaweicloudsdkagentarts.v1.CoreRunEnvironmentVariableResp`]
        :param invoke_config: 
        :type invoke_config: :class:`huaweicloudsdkagentarts.v1.CoreRunInvokeConfigResp`
        :param observability: 
        :type observability: :class:`huaweicloudsdkagentarts.v1.CoreRunObservabilityResp`
        :param storage_config: 
        :type storage_config: :class:`huaweicloudsdkagentarts.v1.CoreRunStorageConfig`
        :param health_config: 
        :type health_config: :class:`huaweicloudsdkagentarts.v1.CoreHealthCheckConfig`
        """
        
        

        self._version = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._artifact_source = None
        self._network_config = None
        self._environment_variables = None
        self._invoke_config = None
        self._observability = None
        self._storage_config = None
        self._health_config = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if artifact_source is not None:
            self.artifact_source = artifact_source
        if network_config is not None:
            self.network_config = network_config
        if environment_variables is not None:
            self.environment_variables = environment_variables
        if invoke_config is not None:
            self.invoke_config = invoke_config
        if observability is not None:
            self.observability = observability
        if storage_config is not None:
            self.storage_config = storage_config
        if health_config is not None:
            self.health_config = health_config

    @property
    def version(self):
        r"""Gets the version of this CoreRunRuntimeVersion.

        **参数解释**: 版本名称，默认为v1、v2自增长，用户也可自定义。 **取值范围**: 以小写字母或数字开头，以小写字母或数字结尾，可以包含小写字母、数字和中划线，长度为2-24个字符。 

        :return: The version of this CoreRunRuntimeVersion.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CoreRunRuntimeVersion.

        **参数解释**: 版本名称，默认为v1、v2自增长，用户也可自定义。 **取值范围**: 以小写字母或数字开头，以小写字母或数字结尾，可以包含小写字母、数字和中划线，长度为2-24个字符。 

        :param version: The version of this CoreRunRuntimeVersion.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        r"""Gets the description of this CoreRunRuntimeVersion.

        **参数解释**: 版本描述（创建/更新版本时可选）。 **取值范围**: 长度为 0 - 4096 个字符。 

        :return: The description of this CoreRunRuntimeVersion.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CoreRunRuntimeVersion.

        **参数解释**: 版本描述（创建/更新版本时可选）。 **取值范围**: 长度为 0 - 4096 个字符。 

        :param description: The description of this CoreRunRuntimeVersion.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this CoreRunRuntimeVersion.

        **参数解释**: 创建时间（系统自动生成，UTC时区）。 **取值范围**: 不涉及。 

        :return: The created_at of this CoreRunRuntimeVersion.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CoreRunRuntimeVersion.

        **参数解释**: 创建时间（系统自动生成，UTC时区）。 **取值范围**: 不涉及。 

        :param created_at: The created_at of this CoreRunRuntimeVersion.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CoreRunRuntimeVersion.

        **参数解释**: 最近更新时间（系统自动生成，版本更新/标签修改时刷新）。 **取值范围**: 不涉及。 

        :return: The updated_at of this CoreRunRuntimeVersion.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CoreRunRuntimeVersion.

        **参数解释**: 最近更新时间（系统自动生成，版本更新/标签修改时刷新）。 **取值范围**: 不涉及。 

        :param updated_at: The updated_at of this CoreRunRuntimeVersion.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def artifact_source(self):
        r"""Gets the artifact_source of this CoreRunRuntimeVersion.

        :return: The artifact_source of this CoreRunRuntimeVersion.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunArtifactSourceResp`
        """
        return self._artifact_source

    @artifact_source.setter
    def artifact_source(self, artifact_source):
        r"""Sets the artifact_source of this CoreRunRuntimeVersion.

        :param artifact_source: The artifact_source of this CoreRunRuntimeVersion.
        :type artifact_source: :class:`huaweicloudsdkagentarts.v1.CoreRunArtifactSourceResp`
        """
        self._artifact_source = artifact_source

    @property
    def network_config(self):
        r"""Gets the network_config of this CoreRunRuntimeVersion.

        :return: The network_config of this CoreRunRuntimeVersion.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunOutboundNetworkResp`
        """
        return self._network_config

    @network_config.setter
    def network_config(self, network_config):
        r"""Sets the network_config of this CoreRunRuntimeVersion.

        :param network_config: The network_config of this CoreRunRuntimeVersion.
        :type network_config: :class:`huaweicloudsdkagentarts.v1.CoreRunOutboundNetworkResp`
        """
        self._network_config = network_config

    @property
    def environment_variables(self):
        r"""Gets the environment_variables of this CoreRunRuntimeVersion.

        **参数解释**: 环境变量配置列表，用于配置运行时环境变量。 **取值范围**: 支持0 - 1024个元素。 

        :return: The environment_variables of this CoreRunRuntimeVersion.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreRunEnvironmentVariableResp`]
        """
        return self._environment_variables

    @environment_variables.setter
    def environment_variables(self, environment_variables):
        r"""Sets the environment_variables of this CoreRunRuntimeVersion.

        **参数解释**: 环境变量配置列表，用于配置运行时环境变量。 **取值范围**: 支持0 - 1024个元素。 

        :param environment_variables: The environment_variables of this CoreRunRuntimeVersion.
        :type environment_variables: list[:class:`huaweicloudsdkagentarts.v1.CoreRunEnvironmentVariableResp`]
        """
        self._environment_variables = environment_variables

    @property
    def invoke_config(self):
        r"""Gets the invoke_config of this CoreRunRuntimeVersion.

        :return: The invoke_config of this CoreRunRuntimeVersion.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunInvokeConfigResp`
        """
        return self._invoke_config

    @invoke_config.setter
    def invoke_config(self, invoke_config):
        r"""Sets the invoke_config of this CoreRunRuntimeVersion.

        :param invoke_config: The invoke_config of this CoreRunRuntimeVersion.
        :type invoke_config: :class:`huaweicloudsdkagentarts.v1.CoreRunInvokeConfigResp`
        """
        self._invoke_config = invoke_config

    @property
    def observability(self):
        r"""Gets the observability of this CoreRunRuntimeVersion.

        :return: The observability of this CoreRunRuntimeVersion.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunObservabilityResp`
        """
        return self._observability

    @observability.setter
    def observability(self, observability):
        r"""Sets the observability of this CoreRunRuntimeVersion.

        :param observability: The observability of this CoreRunRuntimeVersion.
        :type observability: :class:`huaweicloudsdkagentarts.v1.CoreRunObservabilityResp`
        """
        self._observability = observability

    @property
    def storage_config(self):
        r"""Gets the storage_config of this CoreRunRuntimeVersion.

        :return: The storage_config of this CoreRunRuntimeVersion.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunStorageConfig`
        """
        return self._storage_config

    @storage_config.setter
    def storage_config(self, storage_config):
        r"""Sets the storage_config of this CoreRunRuntimeVersion.

        :param storage_config: The storage_config of this CoreRunRuntimeVersion.
        :type storage_config: :class:`huaweicloudsdkagentarts.v1.CoreRunStorageConfig`
        """
        self._storage_config = storage_config

    @property
    def health_config(self):
        r"""Gets the health_config of this CoreRunRuntimeVersion.

        :return: The health_config of this CoreRunRuntimeVersion.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreHealthCheckConfig`
        """
        return self._health_config

    @health_config.setter
    def health_config(self, health_config):
        r"""Sets the health_config of this CoreRunRuntimeVersion.

        :param health_config: The health_config of this CoreRunRuntimeVersion.
        :type health_config: :class:`huaweicloudsdkagentarts.v1.CoreHealthCheckConfig`
        """
        self._health_config = health_config

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
        if not isinstance(other, CoreRunRuntimeVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
