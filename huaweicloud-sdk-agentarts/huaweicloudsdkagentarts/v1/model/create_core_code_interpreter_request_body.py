# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCoreCodeInterpreterRequestBody:

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
        'auth_type': 'str',
        'api_key_name': 'str',
        'execution_agency_name': 'str',
        'observability': 'CoreToolsObservability',
        'network_config': 'CoreToolsOutboundNetwork',
        'agent_gateway_id': 'str',
        'tags': 'list[CoreToolsTag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'auth_type': 'auth_type',
        'api_key_name': 'api_key_name',
        'execution_agency_name': 'execution_agency_name',
        'observability': 'observability',
        'network_config': 'network_config',
        'agent_gateway_id': 'agent_gateway_id',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, auth_type=None, api_key_name=None, execution_agency_name=None, observability=None, network_config=None, agent_gateway_id=None, tags=None):
        r"""CreateCoreCodeInterpreterRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 代码解释器的名称。 **约束限制：** 该名称在您的账户中必须是唯一的。 **取值范围：** 符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$，即必须以小写字母开头，小写字母或数字结尾，中间可包含数字、小写字母、中划线，字符长度必须在2-40个字符之间。 **默认取值：** 不涉及。
        :type name: str
        :param description: **参数解释：** 代码解释器的描述。 **约束限制：** 不涉及。 **取值范围：** 任意字符（包括中文、英文字母、数字、特殊字符等），长度不能超过4096个字符。 **默认取值：** 不涉及。
        :type description: str
        :param auth_type: **参数解释：** 工具认证方式。 **约束限制：** 不涉及。 **取值范围：** &#x60;API_KEY&#x60;: 使用 API 密钥认证。 &#x60;IAM&#x60;: 使用 IAM认证。 **默认取值：** IAM。
        :type auth_type: str
        :param api_key_name: **参数解释：** API Key名称。 **约束限制：** 不涉及。 **取值范围：** 满足正则^[a-zA-Z0-9_-]{1,64}$，即只能包含数字、字母、下划线、中划线，且长度必须在1-64个字符之间。 **默认取值：** 不涉及。
        :type api_key_name: str
        :param execution_agency_name: **参数解释：** 为代码解释器提供访问云服务的权限的IAM委托名，获取方式请参见[创建委托](https://support.huaweicloud.com/usermanual-iam/iam_06_0001.html)。 **约束限制：** 必须是IAM已创建委托。 **取值范围：** IAM委托名长度必须在1-64个字符之间，字符规则以IAM服务校验规则为准。 **默认取值：** 不涉及。
        :type execution_agency_name: str
        :param observability: 
        :type observability: :class:`huaweicloudsdkagentarts.v1.CoreToolsObservability`
        :param network_config: 
        :type network_config: :class:`huaweicloudsdkagentarts.v1.CoreToolsOutboundNetwork`
        :param agent_gateway_id: **参数解释：** 代码解释器入口的AgentGateway的ID。 **约束限制：** 必须为已存在AgentGateway的ID，或者缺省为空，使用租户默认AgentGateway接入。 **取值范围：** 从AgentGateway实例获取，或默认不填。 **默认取值：** 不涉及。
        :type agent_gateway_id: str
        :param tags: **参数解释：** 资源标签。 **约束限制：** 同一个资源的标签key不能重复、标签列表最多支持20个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreToolsTag`]
        """
        
        

        self._name = None
        self._description = None
        self._auth_type = None
        self._api_key_name = None
        self._execution_agency_name = None
        self._observability = None
        self._network_config = None
        self._agent_gateway_id = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if auth_type is not None:
            self.auth_type = auth_type
        if api_key_name is not None:
            self.api_key_name = api_key_name
        if execution_agency_name is not None:
            self.execution_agency_name = execution_agency_name
        if observability is not None:
            self.observability = observability
        if network_config is not None:
            self.network_config = network_config
        if agent_gateway_id is not None:
            self.agent_gateway_id = agent_gateway_id
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** 代码解释器的名称。 **约束限制：** 该名称在您的账户中必须是唯一的。 **取值范围：** 符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$，即必须以小写字母开头，小写字母或数字结尾，中间可包含数字、小写字母、中划线，字符长度必须在2-40个字符之间。 **默认取值：** 不涉及。

        :return: The name of this CreateCoreCodeInterpreterRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** 代码解释器的名称。 **约束限制：** 该名称在您的账户中必须是唯一的。 **取值范围：** 符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$，即必须以小写字母开头，小写字母或数字结尾，中间可包含数字、小写字母、中划线，字符长度必须在2-40个字符之间。 **默认取值：** 不涉及。

        :param name: The name of this CreateCoreCodeInterpreterRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** 代码解释器的描述。 **约束限制：** 不涉及。 **取值范围：** 任意字符（包括中文、英文字母、数字、特殊字符等），长度不能超过4096个字符。 **默认取值：** 不涉及。

        :return: The description of this CreateCoreCodeInterpreterRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** 代码解释器的描述。 **约束限制：** 不涉及。 **取值范围：** 任意字符（包括中文、英文字母、数字、特殊字符等），长度不能超过4096个字符。 **默认取值：** 不涉及。

        :param description: The description of this CreateCoreCodeInterpreterRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def auth_type(self):
        r"""Gets the auth_type of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** 工具认证方式。 **约束限制：** 不涉及。 **取值范围：** `API_KEY`: 使用 API 密钥认证。 `IAM`: 使用 IAM认证。 **默认取值：** IAM。

        :return: The auth_type of this CreateCoreCodeInterpreterRequestBody.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** 工具认证方式。 **约束限制：** 不涉及。 **取值范围：** `API_KEY`: 使用 API 密钥认证。 `IAM`: 使用 IAM认证。 **默认取值：** IAM。

        :param auth_type: The auth_type of this CreateCoreCodeInterpreterRequestBody.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def api_key_name(self):
        r"""Gets the api_key_name of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** API Key名称。 **约束限制：** 不涉及。 **取值范围：** 满足正则^[a-zA-Z0-9_-]{1,64}$，即只能包含数字、字母、下划线、中划线，且长度必须在1-64个字符之间。 **默认取值：** 不涉及。

        :return: The api_key_name of this CreateCoreCodeInterpreterRequestBody.
        :rtype: str
        """
        return self._api_key_name

    @api_key_name.setter
    def api_key_name(self, api_key_name):
        r"""Sets the api_key_name of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** API Key名称。 **约束限制：** 不涉及。 **取值范围：** 满足正则^[a-zA-Z0-9_-]{1,64}$，即只能包含数字、字母、下划线、中划线，且长度必须在1-64个字符之间。 **默认取值：** 不涉及。

        :param api_key_name: The api_key_name of this CreateCoreCodeInterpreterRequestBody.
        :type api_key_name: str
        """
        self._api_key_name = api_key_name

    @property
    def execution_agency_name(self):
        r"""Gets the execution_agency_name of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** 为代码解释器提供访问云服务的权限的IAM委托名，获取方式请参见[创建委托](https://support.huaweicloud.com/usermanual-iam/iam_06_0001.html)。 **约束限制：** 必须是IAM已创建委托。 **取值范围：** IAM委托名长度必须在1-64个字符之间，字符规则以IAM服务校验规则为准。 **默认取值：** 不涉及。

        :return: The execution_agency_name of this CreateCoreCodeInterpreterRequestBody.
        :rtype: str
        """
        return self._execution_agency_name

    @execution_agency_name.setter
    def execution_agency_name(self, execution_agency_name):
        r"""Sets the execution_agency_name of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** 为代码解释器提供访问云服务的权限的IAM委托名，获取方式请参见[创建委托](https://support.huaweicloud.com/usermanual-iam/iam_06_0001.html)。 **约束限制：** 必须是IAM已创建委托。 **取值范围：** IAM委托名长度必须在1-64个字符之间，字符规则以IAM服务校验规则为准。 **默认取值：** 不涉及。

        :param execution_agency_name: The execution_agency_name of this CreateCoreCodeInterpreterRequestBody.
        :type execution_agency_name: str
        """
        self._execution_agency_name = execution_agency_name

    @property
    def observability(self):
        r"""Gets the observability of this CreateCoreCodeInterpreterRequestBody.

        :return: The observability of this CreateCoreCodeInterpreterRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreToolsObservability`
        """
        return self._observability

    @observability.setter
    def observability(self, observability):
        r"""Sets the observability of this CreateCoreCodeInterpreterRequestBody.

        :param observability: The observability of this CreateCoreCodeInterpreterRequestBody.
        :type observability: :class:`huaweicloudsdkagentarts.v1.CoreToolsObservability`
        """
        self._observability = observability

    @property
    def network_config(self):
        r"""Gets the network_config of this CreateCoreCodeInterpreterRequestBody.

        :return: The network_config of this CreateCoreCodeInterpreterRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreToolsOutboundNetwork`
        """
        return self._network_config

    @network_config.setter
    def network_config(self, network_config):
        r"""Sets the network_config of this CreateCoreCodeInterpreterRequestBody.

        :param network_config: The network_config of this CreateCoreCodeInterpreterRequestBody.
        :type network_config: :class:`huaweicloudsdkagentarts.v1.CoreToolsOutboundNetwork`
        """
        self._network_config = network_config

    @property
    def agent_gateway_id(self):
        r"""Gets the agent_gateway_id of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** 代码解释器入口的AgentGateway的ID。 **约束限制：** 必须为已存在AgentGateway的ID，或者缺省为空，使用租户默认AgentGateway接入。 **取值范围：** 从AgentGateway实例获取，或默认不填。 **默认取值：** 不涉及。

        :return: The agent_gateway_id of this CreateCoreCodeInterpreterRequestBody.
        :rtype: str
        """
        return self._agent_gateway_id

    @agent_gateway_id.setter
    def agent_gateway_id(self, agent_gateway_id):
        r"""Sets the agent_gateway_id of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** 代码解释器入口的AgentGateway的ID。 **约束限制：** 必须为已存在AgentGateway的ID，或者缺省为空，使用租户默认AgentGateway接入。 **取值范围：** 从AgentGateway实例获取，或默认不填。 **默认取值：** 不涉及。

        :param agent_gateway_id: The agent_gateway_id of this CreateCoreCodeInterpreterRequestBody.
        :type agent_gateway_id: str
        """
        self._agent_gateway_id = agent_gateway_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** 资源标签。 **约束限制：** 同一个资源的标签key不能重复、标签列表最多支持20个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tags of this CreateCoreCodeInterpreterRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreToolsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateCoreCodeInterpreterRequestBody.

        **参数解释：** 资源标签。 **约束限制：** 同一个资源的标签key不能重复、标签列表最多支持20个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tags: The tags of this CreateCoreCodeInterpreterRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreToolsTag`]
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
        if not isinstance(other, CreateCoreCodeInterpreterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
