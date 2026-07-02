# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCoreGatewayRequestBody:

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
        'protocol_type': 'str',
        'authorizer_type': 'str',
        'agency_name': 'str',
        'authorizer_configuration': 'CoreGatewayAuthorizerConfiguration',
        'protocol_configuration': 'CoreGatewayProtocolConfiguration',
        'log_delivery_configuration': 'CoreGatewayLogDeliveryConfigurationRequestBody',
        'agent_gateway_id': 'str',
        'outbound_network_configuration': 'CoreGatewayOutboundNetworkConfiguration',
        'tags': 'list[CoreGatewayTag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'protocol_type': 'protocol_type',
        'authorizer_type': 'authorizer_type',
        'agency_name': 'agency_name',
        'authorizer_configuration': 'authorizer_configuration',
        'protocol_configuration': 'protocol_configuration',
        'log_delivery_configuration': 'log_delivery_configuration',
        'agent_gateway_id': 'agent_gateway_id',
        'outbound_network_configuration': 'outbound_network_configuration',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, protocol_type=None, authorizer_type=None, agency_name=None, authorizer_configuration=None, protocol_configuration=None, log_delivery_configuration=None, agent_gateway_id=None, outbound_network_configuration=None, tags=None):
        r"""CreateCoreGatewayRequestBody

        The model defined in huaweicloud sdk

        :param name: 网关名称。
        :type name: str
        :param description: 网关的详细描述。
        :type description: str
        :param protocol_type: 网关协议类型。
        :type protocol_type: str
        :param authorizer_type: 授权器类型。
        :type authorizer_type: str
        :param agency_name: 委托名称。
        :type agency_name: str
        :param authorizer_configuration: 
        :type authorizer_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayAuthorizerConfiguration`
        :param protocol_configuration: 
        :type protocol_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayProtocolConfiguration`
        :param log_delivery_configuration: 
        :type log_delivery_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayLogDeliveryConfigurationRequestBody`
        :param agent_gateway_id: AgentGateway ID。
        :type agent_gateway_id: str
        :param outbound_network_configuration: 
        :type outbound_network_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOutboundNetworkConfiguration`
        :param tags: 资源标签列表。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        
        

        self._name = None
        self._description = None
        self._protocol_type = None
        self._authorizer_type = None
        self._agency_name = None
        self._authorizer_configuration = None
        self._protocol_configuration = None
        self._log_delivery_configuration = None
        self._agent_gateway_id = None
        self._outbound_network_configuration = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.protocol_type = protocol_type
        self.authorizer_type = authorizer_type
        self.agency_name = agency_name
        if authorizer_configuration is not None:
            self.authorizer_configuration = authorizer_configuration
        if protocol_configuration is not None:
            self.protocol_configuration = protocol_configuration
        if log_delivery_configuration is not None:
            self.log_delivery_configuration = log_delivery_configuration
        if agent_gateway_id is not None:
            self.agent_gateway_id = agent_gateway_id
        if outbound_network_configuration is not None:
            self.outbound_network_configuration = outbound_network_configuration
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateCoreGatewayRequestBody.

        网关名称。

        :return: The name of this CreateCoreGatewayRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCoreGatewayRequestBody.

        网关名称。

        :param name: The name of this CreateCoreGatewayRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateCoreGatewayRequestBody.

        网关的详细描述。

        :return: The description of this CreateCoreGatewayRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCoreGatewayRequestBody.

        网关的详细描述。

        :param description: The description of this CreateCoreGatewayRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def protocol_type(self):
        r"""Gets the protocol_type of this CreateCoreGatewayRequestBody.

        网关协议类型。

        :return: The protocol_type of this CreateCoreGatewayRequestBody.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        r"""Sets the protocol_type of this CreateCoreGatewayRequestBody.

        网关协议类型。

        :param protocol_type: The protocol_type of this CreateCoreGatewayRequestBody.
        :type protocol_type: str
        """
        self._protocol_type = protocol_type

    @property
    def authorizer_type(self):
        r"""Gets the authorizer_type of this CreateCoreGatewayRequestBody.

        授权器类型。

        :return: The authorizer_type of this CreateCoreGatewayRequestBody.
        :rtype: str
        """
        return self._authorizer_type

    @authorizer_type.setter
    def authorizer_type(self, authorizer_type):
        r"""Sets the authorizer_type of this CreateCoreGatewayRequestBody.

        授权器类型。

        :param authorizer_type: The authorizer_type of this CreateCoreGatewayRequestBody.
        :type authorizer_type: str
        """
        self._authorizer_type = authorizer_type

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CreateCoreGatewayRequestBody.

        委托名称。

        :return: The agency_name of this CreateCoreGatewayRequestBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CreateCoreGatewayRequestBody.

        委托名称。

        :param agency_name: The agency_name of this CreateCoreGatewayRequestBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def authorizer_configuration(self):
        r"""Gets the authorizer_configuration of this CreateCoreGatewayRequestBody.

        :return: The authorizer_configuration of this CreateCoreGatewayRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayAuthorizerConfiguration`
        """
        return self._authorizer_configuration

    @authorizer_configuration.setter
    def authorizer_configuration(self, authorizer_configuration):
        r"""Sets the authorizer_configuration of this CreateCoreGatewayRequestBody.

        :param authorizer_configuration: The authorizer_configuration of this CreateCoreGatewayRequestBody.
        :type authorizer_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayAuthorizerConfiguration`
        """
        self._authorizer_configuration = authorizer_configuration

    @property
    def protocol_configuration(self):
        r"""Gets the protocol_configuration of this CreateCoreGatewayRequestBody.

        :return: The protocol_configuration of this CreateCoreGatewayRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayProtocolConfiguration`
        """
        return self._protocol_configuration

    @protocol_configuration.setter
    def protocol_configuration(self, protocol_configuration):
        r"""Sets the protocol_configuration of this CreateCoreGatewayRequestBody.

        :param protocol_configuration: The protocol_configuration of this CreateCoreGatewayRequestBody.
        :type protocol_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayProtocolConfiguration`
        """
        self._protocol_configuration = protocol_configuration

    @property
    def log_delivery_configuration(self):
        r"""Gets the log_delivery_configuration of this CreateCoreGatewayRequestBody.

        :return: The log_delivery_configuration of this CreateCoreGatewayRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayLogDeliveryConfigurationRequestBody`
        """
        return self._log_delivery_configuration

    @log_delivery_configuration.setter
    def log_delivery_configuration(self, log_delivery_configuration):
        r"""Sets the log_delivery_configuration of this CreateCoreGatewayRequestBody.

        :param log_delivery_configuration: The log_delivery_configuration of this CreateCoreGatewayRequestBody.
        :type log_delivery_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayLogDeliveryConfigurationRequestBody`
        """
        self._log_delivery_configuration = log_delivery_configuration

    @property
    def agent_gateway_id(self):
        r"""Gets the agent_gateway_id of this CreateCoreGatewayRequestBody.

        AgentGateway ID。

        :return: The agent_gateway_id of this CreateCoreGatewayRequestBody.
        :rtype: str
        """
        return self._agent_gateway_id

    @agent_gateway_id.setter
    def agent_gateway_id(self, agent_gateway_id):
        r"""Sets the agent_gateway_id of this CreateCoreGatewayRequestBody.

        AgentGateway ID。

        :param agent_gateway_id: The agent_gateway_id of this CreateCoreGatewayRequestBody.
        :type agent_gateway_id: str
        """
        self._agent_gateway_id = agent_gateway_id

    @property
    def outbound_network_configuration(self):
        r"""Gets the outbound_network_configuration of this CreateCoreGatewayRequestBody.

        :return: The outbound_network_configuration of this CreateCoreGatewayRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOutboundNetworkConfiguration`
        """
        return self._outbound_network_configuration

    @outbound_network_configuration.setter
    def outbound_network_configuration(self, outbound_network_configuration):
        r"""Sets the outbound_network_configuration of this CreateCoreGatewayRequestBody.

        :param outbound_network_configuration: The outbound_network_configuration of this CreateCoreGatewayRequestBody.
        :type outbound_network_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOutboundNetworkConfiguration`
        """
        self._outbound_network_configuration = outbound_network_configuration

    @property
    def tags(self):
        r"""Gets the tags of this CreateCoreGatewayRequestBody.

        资源标签列表。

        :return: The tags of this CreateCoreGatewayRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateCoreGatewayRequestBody.

        资源标签列表。

        :param tags: The tags of this CreateCoreGatewayRequestBody.
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
        if not isinstance(other, CreateCoreGatewayRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
