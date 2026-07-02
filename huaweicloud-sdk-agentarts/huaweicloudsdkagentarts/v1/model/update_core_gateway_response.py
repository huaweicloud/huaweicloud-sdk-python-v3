# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreGatewayResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gateway_id': 'str',
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'protocol_type': 'str',
        'protocol_configuration': 'CoreGatewayProtocolConfiguration',
        'authorizer_type': 'str',
        'agency_name': 'str',
        'endpoint_url': 'str',
        'log_delivery_configuration': 'CoreGatewayLogDeliveryConfiguration',
        'workload_identity': 'CoreGatewayWorkloadIdentity',
        'agent_gateway_id': 'str',
        'outbound_network_configuration': 'CoreGatewayOutboundNetworkConfiguration',
        'tags': 'list[CoreGatewayTag]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'protocol_type': 'protocol_type',
        'protocol_configuration': 'protocol_configuration',
        'authorizer_type': 'authorizer_type',
        'agency_name': 'agency_name',
        'endpoint_url': 'endpoint_url',
        'log_delivery_configuration': 'log_delivery_configuration',
        'workload_identity': 'workload_identity',
        'agent_gateway_id': 'agent_gateway_id',
        'outbound_network_configuration': 'outbound_network_configuration',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, gateway_id=None, name=None, description=None, status=None, protocol_type=None, protocol_configuration=None, authorizer_type=None, agency_name=None, endpoint_url=None, log_delivery_configuration=None, workload_identity=None, agent_gateway_id=None, outbound_network_configuration=None, tags=None, created_at=None, updated_at=None):
        r"""UpdateCoreGatewayResponse

        The model defined in huaweicloud sdk

        :param gateway_id: 网关的唯一标识符。
        :type gateway_id: str
        :param name: 网关名称。
        :type name: str
        :param description: 网关的详细描述。
        :type description: str
        :param status: 网关的当前状态。
        :type status: str
        :param protocol_type: 网关协议类型。
        :type protocol_type: str
        :param protocol_configuration: 
        :type protocol_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayProtocolConfiguration`
        :param authorizer_type: 入站认证类型。
        :type authorizer_type: str
        :param agency_name: 委托名称。
        :type agency_name: str
        :param endpoint_url: 访问网关的 URL 端点。
        :type endpoint_url: str
        :param log_delivery_configuration: 
        :type log_delivery_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayLogDeliveryConfiguration`
        :param workload_identity: 
        :type workload_identity: :class:`huaweicloudsdkagentarts.v1.CoreGatewayWorkloadIdentity`
        :param agent_gateway_id: AgentGateway ID。
        :type agent_gateway_id: str
        :param outbound_network_configuration: 
        :type outbound_network_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOutboundNetworkConfiguration`
        :param tags: 资源标签列表。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        :param created_at: 网关创建时间戳。
        :type created_at: datetime
        :param updated_at: 网关最后更新时间戳。
        :type updated_at: datetime
        """
        
        super().__init__()

        self._gateway_id = None
        self._name = None
        self._description = None
        self._status = None
        self._protocol_type = None
        self._protocol_configuration = None
        self._authorizer_type = None
        self._agency_name = None
        self._endpoint_url = None
        self._log_delivery_configuration = None
        self._workload_identity = None
        self._agent_gateway_id = None
        self._outbound_network_configuration = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.gateway_id = gateway_id
        self.name = name
        if description is not None:
            self.description = description
        self.status = status
        self.protocol_type = protocol_type
        if protocol_configuration is not None:
            self.protocol_configuration = protocol_configuration
        self.authorizer_type = authorizer_type
        self.agency_name = agency_name
        if endpoint_url is not None:
            self.endpoint_url = endpoint_url
        if log_delivery_configuration is not None:
            self.log_delivery_configuration = log_delivery_configuration
        if workload_identity is not None:
            self.workload_identity = workload_identity
        if agent_gateway_id is not None:
            self.agent_gateway_id = agent_gateway_id
        if outbound_network_configuration is not None:
            self.outbound_network_configuration = outbound_network_configuration
        if tags is not None:
            self.tags = tags
        self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this UpdateCoreGatewayResponse.

        网关的唯一标识符。

        :return: The gateway_id of this UpdateCoreGatewayResponse.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this UpdateCoreGatewayResponse.

        网关的唯一标识符。

        :param gateway_id: The gateway_id of this UpdateCoreGatewayResponse.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def name(self):
        r"""Gets the name of this UpdateCoreGatewayResponse.

        网关名称。

        :return: The name of this UpdateCoreGatewayResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateCoreGatewayResponse.

        网关名称。

        :param name: The name of this UpdateCoreGatewayResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateCoreGatewayResponse.

        网关的详细描述。

        :return: The description of this UpdateCoreGatewayResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateCoreGatewayResponse.

        网关的详细描述。

        :param description: The description of this UpdateCoreGatewayResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this UpdateCoreGatewayResponse.

        网关的当前状态。

        :return: The status of this UpdateCoreGatewayResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateCoreGatewayResponse.

        网关的当前状态。

        :param status: The status of this UpdateCoreGatewayResponse.
        :type status: str
        """
        self._status = status

    @property
    def protocol_type(self):
        r"""Gets the protocol_type of this UpdateCoreGatewayResponse.

        网关协议类型。

        :return: The protocol_type of this UpdateCoreGatewayResponse.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        r"""Sets the protocol_type of this UpdateCoreGatewayResponse.

        网关协议类型。

        :param protocol_type: The protocol_type of this UpdateCoreGatewayResponse.
        :type protocol_type: str
        """
        self._protocol_type = protocol_type

    @property
    def protocol_configuration(self):
        r"""Gets the protocol_configuration of this UpdateCoreGatewayResponse.

        :return: The protocol_configuration of this UpdateCoreGatewayResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayProtocolConfiguration`
        """
        return self._protocol_configuration

    @protocol_configuration.setter
    def protocol_configuration(self, protocol_configuration):
        r"""Sets the protocol_configuration of this UpdateCoreGatewayResponse.

        :param protocol_configuration: The protocol_configuration of this UpdateCoreGatewayResponse.
        :type protocol_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayProtocolConfiguration`
        """
        self._protocol_configuration = protocol_configuration

    @property
    def authorizer_type(self):
        r"""Gets the authorizer_type of this UpdateCoreGatewayResponse.

        入站认证类型。

        :return: The authorizer_type of this UpdateCoreGatewayResponse.
        :rtype: str
        """
        return self._authorizer_type

    @authorizer_type.setter
    def authorizer_type(self, authorizer_type):
        r"""Sets the authorizer_type of this UpdateCoreGatewayResponse.

        入站认证类型。

        :param authorizer_type: The authorizer_type of this UpdateCoreGatewayResponse.
        :type authorizer_type: str
        """
        self._authorizer_type = authorizer_type

    @property
    def agency_name(self):
        r"""Gets the agency_name of this UpdateCoreGatewayResponse.

        委托名称。

        :return: The agency_name of this UpdateCoreGatewayResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this UpdateCoreGatewayResponse.

        委托名称。

        :param agency_name: The agency_name of this UpdateCoreGatewayResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def endpoint_url(self):
        r"""Gets the endpoint_url of this UpdateCoreGatewayResponse.

        访问网关的 URL 端点。

        :return: The endpoint_url of this UpdateCoreGatewayResponse.
        :rtype: str
        """
        return self._endpoint_url

    @endpoint_url.setter
    def endpoint_url(self, endpoint_url):
        r"""Sets the endpoint_url of this UpdateCoreGatewayResponse.

        访问网关的 URL 端点。

        :param endpoint_url: The endpoint_url of this UpdateCoreGatewayResponse.
        :type endpoint_url: str
        """
        self._endpoint_url = endpoint_url

    @property
    def log_delivery_configuration(self):
        r"""Gets the log_delivery_configuration of this UpdateCoreGatewayResponse.

        :return: The log_delivery_configuration of this UpdateCoreGatewayResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayLogDeliveryConfiguration`
        """
        return self._log_delivery_configuration

    @log_delivery_configuration.setter
    def log_delivery_configuration(self, log_delivery_configuration):
        r"""Sets the log_delivery_configuration of this UpdateCoreGatewayResponse.

        :param log_delivery_configuration: The log_delivery_configuration of this UpdateCoreGatewayResponse.
        :type log_delivery_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayLogDeliveryConfiguration`
        """
        self._log_delivery_configuration = log_delivery_configuration

    @property
    def workload_identity(self):
        r"""Gets the workload_identity of this UpdateCoreGatewayResponse.

        :return: The workload_identity of this UpdateCoreGatewayResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayWorkloadIdentity`
        """
        return self._workload_identity

    @workload_identity.setter
    def workload_identity(self, workload_identity):
        r"""Sets the workload_identity of this UpdateCoreGatewayResponse.

        :param workload_identity: The workload_identity of this UpdateCoreGatewayResponse.
        :type workload_identity: :class:`huaweicloudsdkagentarts.v1.CoreGatewayWorkloadIdentity`
        """
        self._workload_identity = workload_identity

    @property
    def agent_gateway_id(self):
        r"""Gets the agent_gateway_id of this UpdateCoreGatewayResponse.

        AgentGateway ID。

        :return: The agent_gateway_id of this UpdateCoreGatewayResponse.
        :rtype: str
        """
        return self._agent_gateway_id

    @agent_gateway_id.setter
    def agent_gateway_id(self, agent_gateway_id):
        r"""Sets the agent_gateway_id of this UpdateCoreGatewayResponse.

        AgentGateway ID。

        :param agent_gateway_id: The agent_gateway_id of this UpdateCoreGatewayResponse.
        :type agent_gateway_id: str
        """
        self._agent_gateway_id = agent_gateway_id

    @property
    def outbound_network_configuration(self):
        r"""Gets the outbound_network_configuration of this UpdateCoreGatewayResponse.

        :return: The outbound_network_configuration of this UpdateCoreGatewayResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOutboundNetworkConfiguration`
        """
        return self._outbound_network_configuration

    @outbound_network_configuration.setter
    def outbound_network_configuration(self, outbound_network_configuration):
        r"""Sets the outbound_network_configuration of this UpdateCoreGatewayResponse.

        :param outbound_network_configuration: The outbound_network_configuration of this UpdateCoreGatewayResponse.
        :type outbound_network_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOutboundNetworkConfiguration`
        """
        self._outbound_network_configuration = outbound_network_configuration

    @property
    def tags(self):
        r"""Gets the tags of this UpdateCoreGatewayResponse.

        资源标签列表。

        :return: The tags of this UpdateCoreGatewayResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateCoreGatewayResponse.

        资源标签列表。

        :param tags: The tags of this UpdateCoreGatewayResponse.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        self._tags = tags

    @property
    def created_at(self):
        r"""Gets the created_at of this UpdateCoreGatewayResponse.

        网关创建时间戳。

        :return: The created_at of this UpdateCoreGatewayResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UpdateCoreGatewayResponse.

        网关创建时间戳。

        :param created_at: The created_at of this UpdateCoreGatewayResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UpdateCoreGatewayResponse.

        网关最后更新时间戳。

        :return: The updated_at of this UpdateCoreGatewayResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UpdateCoreGatewayResponse.

        网关最后更新时间戳。

        :param updated_at: The updated_at of this UpdateCoreGatewayResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    def to_dict(self):
        import warnings
        warnings.warn("UpdateCoreGatewayResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateCoreGatewayResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
