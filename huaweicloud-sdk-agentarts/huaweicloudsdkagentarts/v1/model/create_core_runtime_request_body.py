# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCoreRuntimeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'artifact_source': 'CoreRunArtifactSource',
        'environment_variables': 'list[CoreRunEnvironmentVariable]',
        'identity_configuration': 'CoreRunIdentityCreateReqBody',
        'execution_agency_name': 'str',
        'network_config': 'CoreRunOutboundNetwork',
        'agent_gateway_id': 'str',
        'invoke_config': 'CoreRunInvokeConfig',
        'observability': 'CoreRunObservability',
        'storage_config': 'CoreRunStorageConfig',
        'tags': 'list[CoreRunTagItem]',
        'arch': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'artifact_source': 'artifact_source',
        'environment_variables': 'environment_variables',
        'identity_configuration': 'identity_configuration',
        'execution_agency_name': 'execution_agency_name',
        'network_config': 'network_config',
        'agent_gateway_id': 'agent_gateway_id',
        'invoke_config': 'invoke_config',
        'observability': 'observability',
        'storage_config': 'storage_config',
        'tags': 'tags',
        'arch': 'arch'
    }

    def __init__(self, name=None, description=None, artifact_source=None, environment_variables=None, identity_configuration=None, execution_agency_name=None, network_config=None, agent_gateway_id=None, invoke_config=None, observability=None, storage_config=None, tags=None, arch=None):
        r"""CreateCoreRuntimeRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释**：  Agent运行时名称，用于在租户内部唯一标识一个Agent运行时。 **约束限制**: 同一账号下名称不可重复。 **取值范围**： 以小写字母开头，以小写字母或数字结尾，可以包含小写字母、数字和中划线，长度为2-48个字符。 **默认取值**: 不涉及。
        :type name: str
        :param description: **参数解释**：  描述信息，用于对Agent运行时的内容和用途进行简要说明。 **约束限制**: 不涉及。 **取值范围**： 长度为 0 - 4096 个字符。 **默认取值**: 不涉及。
        :type description: str
        :param artifact_source: 
        :type artifact_source: :class:`huaweicloudsdkagentarts.v1.CoreRunArtifactSource`
        :param environment_variables: **参数解释**: 环境变量配置列表，用于配置运行时环境变量。 **约束限制**: 总大小约束2MB。 **取值范围**: 支持0 - 1024个元素。 **默认取值**: 不涉及。 
        :type environment_variables: list[:class:`huaweicloudsdkagentarts.v1.CoreRunEnvironmentVariable`]
        :param identity_configuration: 
        :type identity_configuration: :class:`huaweicloudsdkagentarts.v1.CoreRunIdentityCreateReqBody`
        :param execution_agency_name: **参数解释**：  运行时委托名称。 **约束限制**: 必须是一个存在的信任委托名称，且该委托授权对象为安全沙箱元数据。 **取值范围**： 长度为 1 - 64 个字符。 **默认取值**: 不涉及。
        :type execution_agency_name: str
        :param network_config: 
        :type network_config: :class:`huaweicloudsdkagentarts.v1.CoreRunOutboundNetwork`
        :param agent_gateway_id: **参数解释**：  Agent网关的唯一ID，用户可以通过AgentGateway的查询网关实例列表接口来查询到对应的网关ID。 **约束限制**: 不涉及。 **取值范围**： 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值**: 不涉及。
        :type agent_gateway_id: str
        :param invoke_config: **参数解释**: 智能体调用相关配置。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type invoke_config: :class:`huaweicloudsdkagentarts.v1.CoreRunInvokeConfig`
        :param observability: 
        :type observability: :class:`huaweicloudsdkagentarts.v1.CoreRunObservability`
        :param storage_config: 
        :type storage_config: :class:`huaweicloudsdkagentarts.v1.CoreRunStorageConfig`
        :param tags: **参数解释**: 标签配置列表。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItem`]
        :param arch: **参数解释**：  Agent运行时架构，用于标明运行时需要运行在arm或者x86平台架构。 **约束限制**: 无 **取值范围**： 只允许填写arm64或者x86_64。 **默认取值**: arm64。
        :type arch: str
        """
        
        

        self._name = None
        self._description = None
        self._artifact_source = None
        self._environment_variables = None
        self._identity_configuration = None
        self._execution_agency_name = None
        self._network_config = None
        self._agent_gateway_id = None
        self._invoke_config = None
        self._observability = None
        self._storage_config = None
        self._tags = None
        self._arch = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.artifact_source = artifact_source
        if environment_variables is not None:
            self.environment_variables = environment_variables
        self.identity_configuration = identity_configuration
        if execution_agency_name is not None:
            self.execution_agency_name = execution_agency_name
        if network_config is not None:
            self.network_config = network_config
        if agent_gateway_id is not None:
            self.agent_gateway_id = agent_gateway_id
        if invoke_config is not None:
            self.invoke_config = invoke_config
        if observability is not None:
            self.observability = observability
        if storage_config is not None:
            self.storage_config = storage_config
        if tags is not None:
            self.tags = tags
        if arch is not None:
            self.arch = arch

    @property
    def name(self):
        r"""Gets the name of this CreateCoreRuntimeRequestBody.

        **参数解释**：  Agent运行时名称，用于在租户内部唯一标识一个Agent运行时。 **约束限制**: 同一账号下名称不可重复。 **取值范围**： 以小写字母开头，以小写字母或数字结尾，可以包含小写字母、数字和中划线，长度为2-48个字符。 **默认取值**: 不涉及。

        :return: The name of this CreateCoreRuntimeRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCoreRuntimeRequestBody.

        **参数解释**：  Agent运行时名称，用于在租户内部唯一标识一个Agent运行时。 **约束限制**: 同一账号下名称不可重复。 **取值范围**： 以小写字母开头，以小写字母或数字结尾，可以包含小写字母、数字和中划线，长度为2-48个字符。 **默认取值**: 不涉及。

        :param name: The name of this CreateCoreRuntimeRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateCoreRuntimeRequestBody.

        **参数解释**：  描述信息，用于对Agent运行时的内容和用途进行简要说明。 **约束限制**: 不涉及。 **取值范围**： 长度为 0 - 4096 个字符。 **默认取值**: 不涉及。

        :return: The description of this CreateCoreRuntimeRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCoreRuntimeRequestBody.

        **参数解释**：  描述信息，用于对Agent运行时的内容和用途进行简要说明。 **约束限制**: 不涉及。 **取值范围**： 长度为 0 - 4096 个字符。 **默认取值**: 不涉及。

        :param description: The description of this CreateCoreRuntimeRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def artifact_source(self):
        r"""Gets the artifact_source of this CreateCoreRuntimeRequestBody.

        :return: The artifact_source of this CreateCoreRuntimeRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunArtifactSource`
        """
        return self._artifact_source

    @artifact_source.setter
    def artifact_source(self, artifact_source):
        r"""Sets the artifact_source of this CreateCoreRuntimeRequestBody.

        :param artifact_source: The artifact_source of this CreateCoreRuntimeRequestBody.
        :type artifact_source: :class:`huaweicloudsdkagentarts.v1.CoreRunArtifactSource`
        """
        self._artifact_source = artifact_source

    @property
    def environment_variables(self):
        r"""Gets the environment_variables of this CreateCoreRuntimeRequestBody.

        **参数解释**: 环境变量配置列表，用于配置运行时环境变量。 **约束限制**: 总大小约束2MB。 **取值范围**: 支持0 - 1024个元素。 **默认取值**: 不涉及。 

        :return: The environment_variables of this CreateCoreRuntimeRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreRunEnvironmentVariable`]
        """
        return self._environment_variables

    @environment_variables.setter
    def environment_variables(self, environment_variables):
        r"""Sets the environment_variables of this CreateCoreRuntimeRequestBody.

        **参数解释**: 环境变量配置列表，用于配置运行时环境变量。 **约束限制**: 总大小约束2MB。 **取值范围**: 支持0 - 1024个元素。 **默认取值**: 不涉及。 

        :param environment_variables: The environment_variables of this CreateCoreRuntimeRequestBody.
        :type environment_variables: list[:class:`huaweicloudsdkagentarts.v1.CoreRunEnvironmentVariable`]
        """
        self._environment_variables = environment_variables

    @property
    def identity_configuration(self):
        r"""Gets the identity_configuration of this CreateCoreRuntimeRequestBody.

        :return: The identity_configuration of this CreateCoreRuntimeRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunIdentityCreateReqBody`
        """
        return self._identity_configuration

    @identity_configuration.setter
    def identity_configuration(self, identity_configuration):
        r"""Sets the identity_configuration of this CreateCoreRuntimeRequestBody.

        :param identity_configuration: The identity_configuration of this CreateCoreRuntimeRequestBody.
        :type identity_configuration: :class:`huaweicloudsdkagentarts.v1.CoreRunIdentityCreateReqBody`
        """
        self._identity_configuration = identity_configuration

    @property
    def execution_agency_name(self):
        r"""Gets the execution_agency_name of this CreateCoreRuntimeRequestBody.

        **参数解释**：  运行时委托名称。 **约束限制**: 必须是一个存在的信任委托名称，且该委托授权对象为安全沙箱元数据。 **取值范围**： 长度为 1 - 64 个字符。 **默认取值**: 不涉及。

        :return: The execution_agency_name of this CreateCoreRuntimeRequestBody.
        :rtype: str
        """
        return self._execution_agency_name

    @execution_agency_name.setter
    def execution_agency_name(self, execution_agency_name):
        r"""Sets the execution_agency_name of this CreateCoreRuntimeRequestBody.

        **参数解释**：  运行时委托名称。 **约束限制**: 必须是一个存在的信任委托名称，且该委托授权对象为安全沙箱元数据。 **取值范围**： 长度为 1 - 64 个字符。 **默认取值**: 不涉及。

        :param execution_agency_name: The execution_agency_name of this CreateCoreRuntimeRequestBody.
        :type execution_agency_name: str
        """
        self._execution_agency_name = execution_agency_name

    @property
    def network_config(self):
        r"""Gets the network_config of this CreateCoreRuntimeRequestBody.

        :return: The network_config of this CreateCoreRuntimeRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunOutboundNetwork`
        """
        return self._network_config

    @network_config.setter
    def network_config(self, network_config):
        r"""Sets the network_config of this CreateCoreRuntimeRequestBody.

        :param network_config: The network_config of this CreateCoreRuntimeRequestBody.
        :type network_config: :class:`huaweicloudsdkagentarts.v1.CoreRunOutboundNetwork`
        """
        self._network_config = network_config

    @property
    def agent_gateway_id(self):
        r"""Gets the agent_gateway_id of this CreateCoreRuntimeRequestBody.

        **参数解释**：  Agent网关的唯一ID，用户可以通过AgentGateway的查询网关实例列表接口来查询到对应的网关ID。 **约束限制**: 不涉及。 **取值范围**： 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值**: 不涉及。

        :return: The agent_gateway_id of this CreateCoreRuntimeRequestBody.
        :rtype: str
        """
        return self._agent_gateway_id

    @agent_gateway_id.setter
    def agent_gateway_id(self, agent_gateway_id):
        r"""Sets the agent_gateway_id of this CreateCoreRuntimeRequestBody.

        **参数解释**：  Agent网关的唯一ID，用户可以通过AgentGateway的查询网关实例列表接口来查询到对应的网关ID。 **约束限制**: 不涉及。 **取值范围**： 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值**: 不涉及。

        :param agent_gateway_id: The agent_gateway_id of this CreateCoreRuntimeRequestBody.
        :type agent_gateway_id: str
        """
        self._agent_gateway_id = agent_gateway_id

    @property
    def invoke_config(self):
        r"""Gets the invoke_config of this CreateCoreRuntimeRequestBody.

        **参数解释**: 智能体调用相关配置。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The invoke_config of this CreateCoreRuntimeRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunInvokeConfig`
        """
        return self._invoke_config

    @invoke_config.setter
    def invoke_config(self, invoke_config):
        r"""Sets the invoke_config of this CreateCoreRuntimeRequestBody.

        **参数解释**: 智能体调用相关配置。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param invoke_config: The invoke_config of this CreateCoreRuntimeRequestBody.
        :type invoke_config: :class:`huaweicloudsdkagentarts.v1.CoreRunInvokeConfig`
        """
        self._invoke_config = invoke_config

    @property
    def observability(self):
        r"""Gets the observability of this CreateCoreRuntimeRequestBody.

        :return: The observability of this CreateCoreRuntimeRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunObservability`
        """
        return self._observability

    @observability.setter
    def observability(self, observability):
        r"""Sets the observability of this CreateCoreRuntimeRequestBody.

        :param observability: The observability of this CreateCoreRuntimeRequestBody.
        :type observability: :class:`huaweicloudsdkagentarts.v1.CoreRunObservability`
        """
        self._observability = observability

    @property
    def storage_config(self):
        r"""Gets the storage_config of this CreateCoreRuntimeRequestBody.

        :return: The storage_config of this CreateCoreRuntimeRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunStorageConfig`
        """
        return self._storage_config

    @storage_config.setter
    def storage_config(self, storage_config):
        r"""Sets the storage_config of this CreateCoreRuntimeRequestBody.

        :param storage_config: The storage_config of this CreateCoreRuntimeRequestBody.
        :type storage_config: :class:`huaweicloudsdkagentarts.v1.CoreRunStorageConfig`
        """
        self._storage_config = storage_config

    @property
    def tags(self):
        r"""Gets the tags of this CreateCoreRuntimeRequestBody.

        **参数解释**: 标签配置列表。 

        :return: The tags of this CreateCoreRuntimeRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItem`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateCoreRuntimeRequestBody.

        **参数解释**: 标签配置列表。 

        :param tags: The tags of this CreateCoreRuntimeRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItem`]
        """
        self._tags = tags

    @property
    def arch(self):
        r"""Gets the arch of this CreateCoreRuntimeRequestBody.

        **参数解释**：  Agent运行时架构，用于标明运行时需要运行在arm或者x86平台架构。 **约束限制**: 无 **取值范围**： 只允许填写arm64或者x86_64。 **默认取值**: arm64。

        :return: The arch of this CreateCoreRuntimeRequestBody.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this CreateCoreRuntimeRequestBody.

        **参数解释**：  Agent运行时架构，用于标明运行时需要运行在arm或者x86平台架构。 **约束限制**: 无 **取值范围**： 只允许填写arm64或者x86_64。 **默认取值**: arm64。

        :param arch: The arch of this CreateCoreRuntimeRequestBody.
        :type arch: str
        """
        self._arch = arch

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
        if not isinstance(other, CreateCoreRuntimeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
