# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCustomModelProviderGatewayDetails:

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
        'endpoint_url': 'str',
        'inbound_authorizer_type': 'str',
        'workload_identity_urn': 'str',
        'log_delivery_configuration': 'CoreGatewayLogDeliveryConfiguration',
        'agent_gateway_id': 'str',
        'description': 'str',
        'tags': 'list[CoreGatewayTag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'endpoint_url': 'endpoint_url',
        'inbound_authorizer_type': 'inbound_authorizer_type',
        'workload_identity_urn': 'workload_identity_urn',
        'log_delivery_configuration': 'log_delivery_configuration',
        'agent_gateway_id': 'agent_gateway_id',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, endpoint_url=None, inbound_authorizer_type=None, workload_identity_urn=None, log_delivery_configuration=None, agent_gateway_id=None, description=None, tags=None):
        r"""ShowCustomModelProviderGatewayDetails

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 网关的唯一标识符。 网关ID获取方式： 1. 进入AgentArts平台，在左侧导航栏选择“托管与运行 &gt; 网关”，进入网关界面。 2. 在网关列表中“网关名称/ID”处复制网关ID即可。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 
        :type id: str
        :param name: **参数解释：** 网关名称。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 
        :type name: str
        :param endpoint_url: **参数解释：** 访问网关的 URL 端点。 **取值范围：** 长度为 1-512 个字符。 - 示例：https://gateway-fo2ao8pg-beta1-gw-gu2geoldgz.cn-southwest-301.huaweicloud-agentarts.com 
        :type endpoint_url: str
        :param inbound_authorizer_type: **参数解释：** 入站认证类型。 **取值范围：** - &#x60;iam&#x60;: 使用 IAM 认证 - &#x60;api_key&#x60;: 使用 API 密钥认证 
        :type inbound_authorizer_type: str
        :param workload_identity_urn: **参数解释：** 工作负载标识的统一资源名称，格式为&#39;&#39;agentIdentity:\\&lt;region-id&gt;:\\&lt;account-id&gt;:workloadIdentity:gateway_\\&lt;gateway-name&gt;&#39;&#39;。 **取值范围：** 长度为 1-200 个字符。 
        :type workload_identity_urn: str
        :param log_delivery_configuration: 
        :type log_delivery_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayLogDeliveryConfiguration`
        :param agent_gateway_id: **参数解释：** AgentGateway ID，关联底层 AgentGateway 实例。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 
        :type agent_gateway_id: str
        :param description: **参数解释：** 详细描述。 **取值范围：** 长度为 1-1000 个字符。 
        :type description: str
        :param tags: **参数解释：** 资源标签列表。 **取值范围：** 数组长度为0-20。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        
        

        self._id = None
        self._name = None
        self._endpoint_url = None
        self._inbound_authorizer_type = None
        self._workload_identity_urn = None
        self._log_delivery_configuration = None
        self._agent_gateway_id = None
        self._description = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if endpoint_url is not None:
            self.endpoint_url = endpoint_url
        if inbound_authorizer_type is not None:
            self.inbound_authorizer_type = inbound_authorizer_type
        if workload_identity_urn is not None:
            self.workload_identity_urn = workload_identity_urn
        if log_delivery_configuration is not None:
            self.log_delivery_configuration = log_delivery_configuration
        if agent_gateway_id is not None:
            self.agent_gateway_id = agent_gateway_id
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 网关的唯一标识符。 网关ID获取方式： 1. 进入AgentArts平台，在左侧导航栏选择“托管与运行 > 网关”，进入网关界面。 2. 在网关列表中“网关名称/ID”处复制网关ID即可。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :return: The id of this ShowCustomModelProviderGatewayDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 网关的唯一标识符。 网关ID获取方式： 1. 进入AgentArts平台，在左侧导航栏选择“托管与运行 > 网关”，进入网关界面。 2. 在网关列表中“网关名称/ID”处复制网关ID即可。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :param id: The id of this ShowCustomModelProviderGatewayDetails.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 网关名称。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 

        :return: The name of this ShowCustomModelProviderGatewayDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 网关名称。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 

        :param name: The name of this ShowCustomModelProviderGatewayDetails.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_url(self):
        r"""Gets the endpoint_url of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 访问网关的 URL 端点。 **取值范围：** 长度为 1-512 个字符。 - 示例：https://gateway-fo2ao8pg-beta1-gw-gu2geoldgz.cn-southwest-301.huaweicloud-agentarts.com 

        :return: The endpoint_url of this ShowCustomModelProviderGatewayDetails.
        :rtype: str
        """
        return self._endpoint_url

    @endpoint_url.setter
    def endpoint_url(self, endpoint_url):
        r"""Sets the endpoint_url of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 访问网关的 URL 端点。 **取值范围：** 长度为 1-512 个字符。 - 示例：https://gateway-fo2ao8pg-beta1-gw-gu2geoldgz.cn-southwest-301.huaweicloud-agentarts.com 

        :param endpoint_url: The endpoint_url of this ShowCustomModelProviderGatewayDetails.
        :type endpoint_url: str
        """
        self._endpoint_url = endpoint_url

    @property
    def inbound_authorizer_type(self):
        r"""Gets the inbound_authorizer_type of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 入站认证类型。 **取值范围：** - `iam`: 使用 IAM 认证 - `api_key`: 使用 API 密钥认证 

        :return: The inbound_authorizer_type of this ShowCustomModelProviderGatewayDetails.
        :rtype: str
        """
        return self._inbound_authorizer_type

    @inbound_authorizer_type.setter
    def inbound_authorizer_type(self, inbound_authorizer_type):
        r"""Sets the inbound_authorizer_type of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 入站认证类型。 **取值范围：** - `iam`: 使用 IAM 认证 - `api_key`: 使用 API 密钥认证 

        :param inbound_authorizer_type: The inbound_authorizer_type of this ShowCustomModelProviderGatewayDetails.
        :type inbound_authorizer_type: str
        """
        self._inbound_authorizer_type = inbound_authorizer_type

    @property
    def workload_identity_urn(self):
        r"""Gets the workload_identity_urn of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 工作负载标识的统一资源名称，格式为''agentIdentity:\\<region-id>:\\<account-id>:workloadIdentity:gateway_\\<gateway-name>''。 **取值范围：** 长度为 1-200 个字符。 

        :return: The workload_identity_urn of this ShowCustomModelProviderGatewayDetails.
        :rtype: str
        """
        return self._workload_identity_urn

    @workload_identity_urn.setter
    def workload_identity_urn(self, workload_identity_urn):
        r"""Sets the workload_identity_urn of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 工作负载标识的统一资源名称，格式为''agentIdentity:\\<region-id>:\\<account-id>:workloadIdentity:gateway_\\<gateway-name>''。 **取值范围：** 长度为 1-200 个字符。 

        :param workload_identity_urn: The workload_identity_urn of this ShowCustomModelProviderGatewayDetails.
        :type workload_identity_urn: str
        """
        self._workload_identity_urn = workload_identity_urn

    @property
    def log_delivery_configuration(self):
        r"""Gets the log_delivery_configuration of this ShowCustomModelProviderGatewayDetails.

        :return: The log_delivery_configuration of this ShowCustomModelProviderGatewayDetails.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayLogDeliveryConfiguration`
        """
        return self._log_delivery_configuration

    @log_delivery_configuration.setter
    def log_delivery_configuration(self, log_delivery_configuration):
        r"""Sets the log_delivery_configuration of this ShowCustomModelProviderGatewayDetails.

        :param log_delivery_configuration: The log_delivery_configuration of this ShowCustomModelProviderGatewayDetails.
        :type log_delivery_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayLogDeliveryConfiguration`
        """
        self._log_delivery_configuration = log_delivery_configuration

    @property
    def agent_gateway_id(self):
        r"""Gets the agent_gateway_id of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** AgentGateway ID，关联底层 AgentGateway 实例。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :return: The agent_gateway_id of this ShowCustomModelProviderGatewayDetails.
        :rtype: str
        """
        return self._agent_gateway_id

    @agent_gateway_id.setter
    def agent_gateway_id(self, agent_gateway_id):
        r"""Sets the agent_gateway_id of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** AgentGateway ID，关联底层 AgentGateway 实例。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :param agent_gateway_id: The agent_gateway_id of this ShowCustomModelProviderGatewayDetails.
        :type agent_gateway_id: str
        """
        self._agent_gateway_id = agent_gateway_id

    @property
    def description(self):
        r"""Gets the description of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 详细描述。 **取值范围：** 长度为 1-1000 个字符。 

        :return: The description of this ShowCustomModelProviderGatewayDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 详细描述。 **取值范围：** 长度为 1-1000 个字符。 

        :param description: The description of this ShowCustomModelProviderGatewayDetails.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 资源标签列表。 **取值范围：** 数组长度为0-20。 

        :return: The tags of this ShowCustomModelProviderGatewayDetails.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowCustomModelProviderGatewayDetails.

        **参数解释：** 资源标签列表。 **取值范围：** 数组长度为0-20。 

        :param tags: The tags of this ShowCustomModelProviderGatewayDetails.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        self._tags = tags

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
        if not isinstance(other, ShowCustomModelProviderGatewayDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
