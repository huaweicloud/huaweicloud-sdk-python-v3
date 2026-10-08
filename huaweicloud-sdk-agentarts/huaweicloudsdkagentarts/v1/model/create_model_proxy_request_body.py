# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateModelProxyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_model_provider_id': 'str',
        'name': 'str',
        'description': 'str',
        'inbound_authorizer_type': 'str',
        'inbound_authorizer_configuration': 'CoreModelProxyAuthorizerConfiguration',
        'agent_gateway_id': 'str',
        'agency_name': 'str',
        'tags': 'list[CoreGatewayTagForRequest]'
    }

    attribute_map = {
        'custom_model_provider_id': 'custom_model_provider_id',
        'name': 'name',
        'description': 'description',
        'inbound_authorizer_type': 'inbound_authorizer_type',
        'inbound_authorizer_configuration': 'inbound_authorizer_configuration',
        'agent_gateway_id': 'agent_gateway_id',
        'agency_name': 'agency_name',
        'tags': 'tags'
    }

    def __init__(self, custom_model_provider_id=None, name=None, description=None, inbound_authorizer_type=None, inbound_authorizer_configuration=None, agent_gateway_id=None, agency_name=None, tags=None):
        r"""CreateModelProxyRequestBody

        The model defined in huaweicloud sdk

        :param custom_model_provider_id: **参数解释：** 模型提供商ID。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type custom_model_provider_id: str
        :param name: **参数解释：** 模型代理名称。 **约束限制：** 账户下模型代理名称唯一（不区分大小写）。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 **默认取值：** 不涉及。 
        :type name: str
        :param description: **参数解释：** 模型代理的详细描述。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-1000 个字符。 **默认取值：** 不涉及。 
        :type description: str
        :param inbound_authorizer_type: **参数解释：** 入站认证类型。 **约束限制：** 不涉及。 **取值范围：** - &#x60;iam&#x60;: 使用 IAM 认证 - &#x60;api_key&#x60;: 使用 API 密钥认证（必须携带 authorizer_configuration） **默认取值：** 不涉及。 
        :type inbound_authorizer_type: str
        :param inbound_authorizer_configuration: 
        :type inbound_authorizer_configuration: :class:`huaweicloudsdkagentarts.v1.CoreModelProxyAuthorizerConfiguration`
        :param agent_gateway_id: **参数解释：** AgentGateway ID，关联底层 AgentGateway 实例。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type agent_gateway_id: str
        :param agency_name: **参数解释：** 委托名称，用于指定模型代理使用的委托身份。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-64 个字符。 **默认取值：** 不涉及。 
        :type agency_name: str
        :param tags: **参数解释：** 资源标签列表。 **约束限制：** 不涉及。 **取值范围：** 数组长度为 0-20。 **默认取值：** 不涉及。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTagForRequest`]
        """
        
        

        self._custom_model_provider_id = None
        self._name = None
        self._description = None
        self._inbound_authorizer_type = None
        self._inbound_authorizer_configuration = None
        self._agent_gateway_id = None
        self._agency_name = None
        self._tags = None
        self.discriminator = None

        self.custom_model_provider_id = custom_model_provider_id
        self.name = name
        if description is not None:
            self.description = description
        self.inbound_authorizer_type = inbound_authorizer_type
        if inbound_authorizer_configuration is not None:
            self.inbound_authorizer_configuration = inbound_authorizer_configuration
        if agent_gateway_id is not None:
            self.agent_gateway_id = agent_gateway_id
        self.agency_name = agency_name
        if tags is not None:
            self.tags = tags

    @property
    def custom_model_provider_id(self):
        r"""Gets the custom_model_provider_id of this CreateModelProxyRequestBody.

        **参数解释：** 模型提供商ID。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The custom_model_provider_id of this CreateModelProxyRequestBody.
        :rtype: str
        """
        return self._custom_model_provider_id

    @custom_model_provider_id.setter
    def custom_model_provider_id(self, custom_model_provider_id):
        r"""Sets the custom_model_provider_id of this CreateModelProxyRequestBody.

        **参数解释：** 模型提供商ID。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param custom_model_provider_id: The custom_model_provider_id of this CreateModelProxyRequestBody.
        :type custom_model_provider_id: str
        """
        self._custom_model_provider_id = custom_model_provider_id

    @property
    def name(self):
        r"""Gets the name of this CreateModelProxyRequestBody.

        **参数解释：** 模型代理名称。 **约束限制：** 账户下模型代理名称唯一（不区分大小写）。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 **默认取值：** 不涉及。 

        :return: The name of this CreateModelProxyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateModelProxyRequestBody.

        **参数解释：** 模型代理名称。 **约束限制：** 账户下模型代理名称唯一（不区分大小写）。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 **默认取值：** 不涉及。 

        :param name: The name of this CreateModelProxyRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateModelProxyRequestBody.

        **参数解释：** 模型代理的详细描述。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-1000 个字符。 **默认取值：** 不涉及。 

        :return: The description of this CreateModelProxyRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateModelProxyRequestBody.

        **参数解释：** 模型代理的详细描述。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-1000 个字符。 **默认取值：** 不涉及。 

        :param description: The description of this CreateModelProxyRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def inbound_authorizer_type(self):
        r"""Gets the inbound_authorizer_type of this CreateModelProxyRequestBody.

        **参数解释：** 入站认证类型。 **约束限制：** 不涉及。 **取值范围：** - `iam`: 使用 IAM 认证 - `api_key`: 使用 API 密钥认证（必须携带 authorizer_configuration） **默认取值：** 不涉及。 

        :return: The inbound_authorizer_type of this CreateModelProxyRequestBody.
        :rtype: str
        """
        return self._inbound_authorizer_type

    @inbound_authorizer_type.setter
    def inbound_authorizer_type(self, inbound_authorizer_type):
        r"""Sets the inbound_authorizer_type of this CreateModelProxyRequestBody.

        **参数解释：** 入站认证类型。 **约束限制：** 不涉及。 **取值范围：** - `iam`: 使用 IAM 认证 - `api_key`: 使用 API 密钥认证（必须携带 authorizer_configuration） **默认取值：** 不涉及。 

        :param inbound_authorizer_type: The inbound_authorizer_type of this CreateModelProxyRequestBody.
        :type inbound_authorizer_type: str
        """
        self._inbound_authorizer_type = inbound_authorizer_type

    @property
    def inbound_authorizer_configuration(self):
        r"""Gets the inbound_authorizer_configuration of this CreateModelProxyRequestBody.

        :return: The inbound_authorizer_configuration of this CreateModelProxyRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreModelProxyAuthorizerConfiguration`
        """
        return self._inbound_authorizer_configuration

    @inbound_authorizer_configuration.setter
    def inbound_authorizer_configuration(self, inbound_authorizer_configuration):
        r"""Sets the inbound_authorizer_configuration of this CreateModelProxyRequestBody.

        :param inbound_authorizer_configuration: The inbound_authorizer_configuration of this CreateModelProxyRequestBody.
        :type inbound_authorizer_configuration: :class:`huaweicloudsdkagentarts.v1.CoreModelProxyAuthorizerConfiguration`
        """
        self._inbound_authorizer_configuration = inbound_authorizer_configuration

    @property
    def agent_gateway_id(self):
        r"""Gets the agent_gateway_id of this CreateModelProxyRequestBody.

        **参数解释：** AgentGateway ID，关联底层 AgentGateway 实例。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The agent_gateway_id of this CreateModelProxyRequestBody.
        :rtype: str
        """
        return self._agent_gateway_id

    @agent_gateway_id.setter
    def agent_gateway_id(self, agent_gateway_id):
        r"""Sets the agent_gateway_id of this CreateModelProxyRequestBody.

        **参数解释：** AgentGateway ID，关联底层 AgentGateway 实例。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param agent_gateway_id: The agent_gateway_id of this CreateModelProxyRequestBody.
        :type agent_gateway_id: str
        """
        self._agent_gateway_id = agent_gateway_id

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CreateModelProxyRequestBody.

        **参数解释：** 委托名称，用于指定模型代理使用的委托身份。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-64 个字符。 **默认取值：** 不涉及。 

        :return: The agency_name of this CreateModelProxyRequestBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CreateModelProxyRequestBody.

        **参数解释：** 委托名称，用于指定模型代理使用的委托身份。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-64 个字符。 **默认取值：** 不涉及。 

        :param agency_name: The agency_name of this CreateModelProxyRequestBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def tags(self):
        r"""Gets the tags of this CreateModelProxyRequestBody.

        **参数解释：** 资源标签列表。 **约束限制：** 不涉及。 **取值范围：** 数组长度为 0-20。 **默认取值：** 不涉及。 

        :return: The tags of this CreateModelProxyRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTagForRequest`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateModelProxyRequestBody.

        **参数解释：** 资源标签列表。 **约束限制：** 不涉及。 **取值范围：** 数组长度为 0-20。 **默认取值：** 不涉及。 

        :param tags: The tags of this CreateModelProxyRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTagForRequest`]
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
        if not isinstance(other, CreateModelProxyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
