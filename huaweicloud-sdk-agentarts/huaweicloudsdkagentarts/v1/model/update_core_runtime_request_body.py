# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreRuntimeRequestBody:

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
        'artifact_source': 'CoreRunArtifactSource',
        'environment_variables': 'list[CoreRunEnvironmentVariable]',
        'invoke_config': 'UpdateCoreRunInvokeConfig',
        'observability': 'CoreRunObservability',
        'storage_config': 'CoreRunStorageConfig',
        'tags': 'list[CoreRunTagItem]',
        'execution_agency_name': 'str'
    }

    attribute_map = {
        'version': 'version',
        'description': 'description',
        'artifact_source': 'artifact_source',
        'environment_variables': 'environment_variables',
        'invoke_config': 'invoke_config',
        'observability': 'observability',
        'storage_config': 'storage_config',
        'tags': 'tags',
        'execution_agency_name': 'execution_agency_name'
    }

    def __init__(self, version=None, description=None, artifact_source=None, environment_variables=None, invoke_config=None, observability=None, storage_config=None, tags=None, execution_agency_name=None):
        r"""UpdateCoreRuntimeRequestBody

        The model defined in huaweicloud sdk

        :param version: **参数解释**: 版本名称。 
        :type version: str
        :param description: **参数解释**: 版本描述信息。 
        :type description: str
        :param artifact_source: 
        :type artifact_source: :class:`huaweicloudsdkagentarts.v1.CoreRunArtifactSource`
        :param environment_variables: **参数解释**: 环境变量配置列表，用于配置运行时环境变量。 **约束限制**: 总大小约束2MB。 **取值范围**: 支持0 - 1024个元素。 **默认取值**: 不涉及。 
        :type environment_variables: list[:class:`huaweicloudsdkagentarts.v1.CoreRunEnvironmentVariable`]
        :param invoke_config: 
        :type invoke_config: :class:`huaweicloudsdkagentarts.v1.UpdateCoreRunInvokeConfig`
        :param observability: 
        :type observability: :class:`huaweicloudsdkagentarts.v1.CoreRunObservability`
        :param storage_config: 
        :type storage_config: :class:`huaweicloudsdkagentarts.v1.CoreRunStorageConfig`
        :param tags: **参数解释**: 标签配置列表。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItem`]
        :param execution_agency_name: **参数解释**： 运行时委托名称。 **取值范围**： 长度为 1 - 64 个字符。
        :type execution_agency_name: str
        """
        
        

        self._version = None
        self._description = None
        self._artifact_source = None
        self._environment_variables = None
        self._invoke_config = None
        self._observability = None
        self._storage_config = None
        self._tags = None
        self._execution_agency_name = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if artifact_source is not None:
            self.artifact_source = artifact_source
        if environment_variables is not None:
            self.environment_variables = environment_variables
        if invoke_config is not None:
            self.invoke_config = invoke_config
        if observability is not None:
            self.observability = observability
        if storage_config is not None:
            self.storage_config = storage_config
        if tags is not None:
            self.tags = tags
        if execution_agency_name is not None:
            self.execution_agency_name = execution_agency_name

    @property
    def version(self):
        r"""Gets the version of this UpdateCoreRuntimeRequestBody.

        **参数解释**: 版本名称。 

        :return: The version of this UpdateCoreRuntimeRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateCoreRuntimeRequestBody.

        **参数解释**: 版本名称。 

        :param version: The version of this UpdateCoreRuntimeRequestBody.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        r"""Gets the description of this UpdateCoreRuntimeRequestBody.

        **参数解释**: 版本描述信息。 

        :return: The description of this UpdateCoreRuntimeRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateCoreRuntimeRequestBody.

        **参数解释**: 版本描述信息。 

        :param description: The description of this UpdateCoreRuntimeRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def artifact_source(self):
        r"""Gets the artifact_source of this UpdateCoreRuntimeRequestBody.

        :return: The artifact_source of this UpdateCoreRuntimeRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunArtifactSource`
        """
        return self._artifact_source

    @artifact_source.setter
    def artifact_source(self, artifact_source):
        r"""Sets the artifact_source of this UpdateCoreRuntimeRequestBody.

        :param artifact_source: The artifact_source of this UpdateCoreRuntimeRequestBody.
        :type artifact_source: :class:`huaweicloudsdkagentarts.v1.CoreRunArtifactSource`
        """
        self._artifact_source = artifact_source

    @property
    def environment_variables(self):
        r"""Gets the environment_variables of this UpdateCoreRuntimeRequestBody.

        **参数解释**: 环境变量配置列表，用于配置运行时环境变量。 **约束限制**: 总大小约束2MB。 **取值范围**: 支持0 - 1024个元素。 **默认取值**: 不涉及。 

        :return: The environment_variables of this UpdateCoreRuntimeRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreRunEnvironmentVariable`]
        """
        return self._environment_variables

    @environment_variables.setter
    def environment_variables(self, environment_variables):
        r"""Sets the environment_variables of this UpdateCoreRuntimeRequestBody.

        **参数解释**: 环境变量配置列表，用于配置运行时环境变量。 **约束限制**: 总大小约束2MB。 **取值范围**: 支持0 - 1024个元素。 **默认取值**: 不涉及。 

        :param environment_variables: The environment_variables of this UpdateCoreRuntimeRequestBody.
        :type environment_variables: list[:class:`huaweicloudsdkagentarts.v1.CoreRunEnvironmentVariable`]
        """
        self._environment_variables = environment_variables

    @property
    def invoke_config(self):
        r"""Gets the invoke_config of this UpdateCoreRuntimeRequestBody.

        :return: The invoke_config of this UpdateCoreRuntimeRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreRunInvokeConfig`
        """
        return self._invoke_config

    @invoke_config.setter
    def invoke_config(self, invoke_config):
        r"""Sets the invoke_config of this UpdateCoreRuntimeRequestBody.

        :param invoke_config: The invoke_config of this UpdateCoreRuntimeRequestBody.
        :type invoke_config: :class:`huaweicloudsdkagentarts.v1.UpdateCoreRunInvokeConfig`
        """
        self._invoke_config = invoke_config

    @property
    def observability(self):
        r"""Gets the observability of this UpdateCoreRuntimeRequestBody.

        :return: The observability of this UpdateCoreRuntimeRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunObservability`
        """
        return self._observability

    @observability.setter
    def observability(self, observability):
        r"""Sets the observability of this UpdateCoreRuntimeRequestBody.

        :param observability: The observability of this UpdateCoreRuntimeRequestBody.
        :type observability: :class:`huaweicloudsdkagentarts.v1.CoreRunObservability`
        """
        self._observability = observability

    @property
    def storage_config(self):
        r"""Gets the storage_config of this UpdateCoreRuntimeRequestBody.

        :return: The storage_config of this UpdateCoreRuntimeRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunStorageConfig`
        """
        return self._storage_config

    @storage_config.setter
    def storage_config(self, storage_config):
        r"""Sets the storage_config of this UpdateCoreRuntimeRequestBody.

        :param storage_config: The storage_config of this UpdateCoreRuntimeRequestBody.
        :type storage_config: :class:`huaweicloudsdkagentarts.v1.CoreRunStorageConfig`
        """
        self._storage_config = storage_config

    @property
    def tags(self):
        r"""Gets the tags of this UpdateCoreRuntimeRequestBody.

        **参数解释**: 标签配置列表。 

        :return: The tags of this UpdateCoreRuntimeRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItem`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateCoreRuntimeRequestBody.

        **参数解释**: 标签配置列表。 

        :param tags: The tags of this UpdateCoreRuntimeRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItem`]
        """
        self._tags = tags

    @property
    def execution_agency_name(self):
        r"""Gets the execution_agency_name of this UpdateCoreRuntimeRequestBody.

        **参数解释**： 运行时委托名称。 **取值范围**： 长度为 1 - 64 个字符。

        :return: The execution_agency_name of this UpdateCoreRuntimeRequestBody.
        :rtype: str
        """
        return self._execution_agency_name

    @execution_agency_name.setter
    def execution_agency_name(self, execution_agency_name):
        r"""Sets the execution_agency_name of this UpdateCoreRuntimeRequestBody.

        **参数解释**： 运行时委托名称。 **取值范围**： 长度为 1 - 64 个字符。

        :param execution_agency_name: The execution_agency_name of this UpdateCoreRuntimeRequestBody.
        :type execution_agency_name: str
        """
        self._execution_agency_name = execution_agency_name

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
        if not isinstance(other, UpdateCoreRuntimeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
