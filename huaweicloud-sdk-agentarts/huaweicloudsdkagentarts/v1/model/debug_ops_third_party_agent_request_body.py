# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugOpsThirdPartyAgentRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'description': 'str',
        'agent_name': 'str',
        'runtime_id': 'str',
        'api_config': 'OpsThirdPartyAgentApiConfig',
        'auth_config': 'OpsThirdPartyAgentAuthConfig',
        'response_config': 'OpsThirdPartyAgentResponseConfig',
        'timeout': 'int',
        'variables': 'dict(str, str)'
    }

    attribute_map = {
        'type': 'type',
        'description': 'description',
        'agent_name': 'agent_name',
        'runtime_id': 'runtime_id',
        'api_config': 'api_config',
        'auth_config': 'auth_config',
        'response_config': 'response_config',
        'timeout': 'timeout',
        'variables': 'variables'
    }

    def __init__(self, type=None, description=None, agent_name=None, runtime_id=None, api_config=None, auth_config=None, response_config=None, timeout=None, variables=None):
        r"""DebugOpsThirdPartyAgentRequestBody

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 调试对象类型，用于区分三方托管智能体和智能体运行时。 **约束限制：** 必须为枚举值之一。 **取值范围：** - third_party_agent：三方托管智能体，需配置auth_config - agent_runtime：智能体运行时，平台内部调用无需auth_config **默认取值：** 不涉及。
        :type type: str
        :param description: **参数解释：** 智能体的描述信息。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type description: str
        :param agent_name: **参数解释：** 三方智能体的名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type agent_name: str
        :param runtime_id: **参数解释：** 智能体运行时ID，type为agent_runtime时必填。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type runtime_id: str
        :param api_config: 
        :type api_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentApiConfig`
        :param auth_config: 
        :type auth_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentAuthConfig`
        :param response_config: 
        :type response_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentResponseConfig`
        :param timeout: **参数解释：** 单次调用超时时间（秒）。 **约束限制：** 整数类型，范围5到600。 **取值范围：** 5-600。 **默认取值：** 60。
        :type timeout: int
        :param variables: **参数解释：** 自定义变量键值对，将替换API配置中的{{变量名}}占位符。例如API配置Body中使用{{input}}，则variables中传入input变量即可。 **约束限制：** 键和值均为字符串类型，最多支持20个变量。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type variables: dict(str, str)
        """
        
        

        self._type = None
        self._description = None
        self._agent_name = None
        self._runtime_id = None
        self._api_config = None
        self._auth_config = None
        self._response_config = None
        self._timeout = None
        self._variables = None
        self.discriminator = None

        self.type = type
        if description is not None:
            self.description = description
        if agent_name is not None:
            self.agent_name = agent_name
        if runtime_id is not None:
            self.runtime_id = runtime_id
        self.api_config = api_config
        if auth_config is not None:
            self.auth_config = auth_config
        self.response_config = response_config
        if timeout is not None:
            self.timeout = timeout
        if variables is not None:
            self.variables = variables

    @property
    def type(self):
        r"""Gets the type of this DebugOpsThirdPartyAgentRequestBody.

        **参数解释：** 调试对象类型，用于区分三方托管智能体和智能体运行时。 **约束限制：** 必须为枚举值之一。 **取值范围：** - third_party_agent：三方托管智能体，需配置auth_config - agent_runtime：智能体运行时，平台内部调用无需auth_config **默认取值：** 不涉及。

        :return: The type of this DebugOpsThirdPartyAgentRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DebugOpsThirdPartyAgentRequestBody.

        **参数解释：** 调试对象类型，用于区分三方托管智能体和智能体运行时。 **约束限制：** 必须为枚举值之一。 **取值范围：** - third_party_agent：三方托管智能体，需配置auth_config - agent_runtime：智能体运行时，平台内部调用无需auth_config **默认取值：** 不涉及。

        :param type: The type of this DebugOpsThirdPartyAgentRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this DebugOpsThirdPartyAgentRequestBody.

        **参数解释：** 智能体的描述信息。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The description of this DebugOpsThirdPartyAgentRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DebugOpsThirdPartyAgentRequestBody.

        **参数解释：** 智能体的描述信息。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param description: The description of this DebugOpsThirdPartyAgentRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def agent_name(self):
        r"""Gets the agent_name of this DebugOpsThirdPartyAgentRequestBody.

        **参数解释：** 三方智能体的名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The agent_name of this DebugOpsThirdPartyAgentRequestBody.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        r"""Sets the agent_name of this DebugOpsThirdPartyAgentRequestBody.

        **参数解释：** 三方智能体的名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param agent_name: The agent_name of this DebugOpsThirdPartyAgentRequestBody.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def runtime_id(self):
        r"""Gets the runtime_id of this DebugOpsThirdPartyAgentRequestBody.

        **参数解释：** 智能体运行时ID，type为agent_runtime时必填。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The runtime_id of this DebugOpsThirdPartyAgentRequestBody.
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        r"""Sets the runtime_id of this DebugOpsThirdPartyAgentRequestBody.

        **参数解释：** 智能体运行时ID，type为agent_runtime时必填。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param runtime_id: The runtime_id of this DebugOpsThirdPartyAgentRequestBody.
        :type runtime_id: str
        """
        self._runtime_id = runtime_id

    @property
    def api_config(self):
        r"""Gets the api_config of this DebugOpsThirdPartyAgentRequestBody.

        :return: The api_config of this DebugOpsThirdPartyAgentRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentApiConfig`
        """
        return self._api_config

    @api_config.setter
    def api_config(self, api_config):
        r"""Sets the api_config of this DebugOpsThirdPartyAgentRequestBody.

        :param api_config: The api_config of this DebugOpsThirdPartyAgentRequestBody.
        :type api_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentApiConfig`
        """
        self._api_config = api_config

    @property
    def auth_config(self):
        r"""Gets the auth_config of this DebugOpsThirdPartyAgentRequestBody.

        :return: The auth_config of this DebugOpsThirdPartyAgentRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentAuthConfig`
        """
        return self._auth_config

    @auth_config.setter
    def auth_config(self, auth_config):
        r"""Sets the auth_config of this DebugOpsThirdPartyAgentRequestBody.

        :param auth_config: The auth_config of this DebugOpsThirdPartyAgentRequestBody.
        :type auth_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentAuthConfig`
        """
        self._auth_config = auth_config

    @property
    def response_config(self):
        r"""Gets the response_config of this DebugOpsThirdPartyAgentRequestBody.

        :return: The response_config of this DebugOpsThirdPartyAgentRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentResponseConfig`
        """
        return self._response_config

    @response_config.setter
    def response_config(self, response_config):
        r"""Sets the response_config of this DebugOpsThirdPartyAgentRequestBody.

        :param response_config: The response_config of this DebugOpsThirdPartyAgentRequestBody.
        :type response_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentResponseConfig`
        """
        self._response_config = response_config

    @property
    def timeout(self):
        r"""Gets the timeout of this DebugOpsThirdPartyAgentRequestBody.

        **参数解释：** 单次调用超时时间（秒）。 **约束限制：** 整数类型，范围5到600。 **取值范围：** 5-600。 **默认取值：** 60。

        :return: The timeout of this DebugOpsThirdPartyAgentRequestBody.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this DebugOpsThirdPartyAgentRequestBody.

        **参数解释：** 单次调用超时时间（秒）。 **约束限制：** 整数类型，范围5到600。 **取值范围：** 5-600。 **默认取值：** 60。

        :param timeout: The timeout of this DebugOpsThirdPartyAgentRequestBody.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def variables(self):
        r"""Gets the variables of this DebugOpsThirdPartyAgentRequestBody.

        **参数解释：** 自定义变量键值对，将替换API配置中的{{变量名}}占位符。例如API配置Body中使用{{input}}，则variables中传入input变量即可。 **约束限制：** 键和值均为字符串类型，最多支持20个变量。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The variables of this DebugOpsThirdPartyAgentRequestBody.
        :rtype: dict(str, str)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this DebugOpsThirdPartyAgentRequestBody.

        **参数解释：** 自定义变量键值对，将替换API配置中的{{变量名}}占位符。例如API配置Body中使用{{input}}，则variables中传入input变量即可。 **约束限制：** 键和值均为字符串类型，最多支持20个变量。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param variables: The variables of this DebugOpsThirdPartyAgentRequestBody.
        :type variables: dict(str, str)
        """
        self._variables = variables

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
        if not isinstance(other, DebugOpsThirdPartyAgentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
