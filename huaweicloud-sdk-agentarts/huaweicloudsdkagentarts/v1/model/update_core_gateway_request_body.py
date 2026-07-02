# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreGatewayRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'authorizer_configuration': 'CoreGatewayAuthorizerConfiguration',
        'protocol_configuration': 'CoreGatewayUpdateProtocolConfiguration',
        'log_delivery_configuration': 'CoreGatewayLogDeliveryConfigurationRequestBody',
        'tags': 'list[CoreGatewayTag]'
    }

    attribute_map = {
        'description': 'description',
        'authorizer_configuration': 'authorizer_configuration',
        'protocol_configuration': 'protocol_configuration',
        'log_delivery_configuration': 'log_delivery_configuration',
        'tags': 'tags'
    }

    def __init__(self, description=None, authorizer_configuration=None, protocol_configuration=None, log_delivery_configuration=None, tags=None):
        r"""UpdateCoreGatewayRequestBody

        The model defined in huaweicloud sdk

        :param description: 更新后的网关描述。
        :type description: str
        :param authorizer_configuration: 
        :type authorizer_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayAuthorizerConfiguration`
        :param protocol_configuration: 
        :type protocol_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayUpdateProtocolConfiguration`
        :param log_delivery_configuration: 
        :type log_delivery_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayLogDeliveryConfigurationRequestBody`
        :param tags: 资源标签列表。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        
        

        self._description = None
        self._authorizer_configuration = None
        self._protocol_configuration = None
        self._log_delivery_configuration = None
        self._tags = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if authorizer_configuration is not None:
            self.authorizer_configuration = authorizer_configuration
        if protocol_configuration is not None:
            self.protocol_configuration = protocol_configuration
        if log_delivery_configuration is not None:
            self.log_delivery_configuration = log_delivery_configuration
        if tags is not None:
            self.tags = tags

    @property
    def description(self):
        r"""Gets the description of this UpdateCoreGatewayRequestBody.

        更新后的网关描述。

        :return: The description of this UpdateCoreGatewayRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateCoreGatewayRequestBody.

        更新后的网关描述。

        :param description: The description of this UpdateCoreGatewayRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def authorizer_configuration(self):
        r"""Gets the authorizer_configuration of this UpdateCoreGatewayRequestBody.

        :return: The authorizer_configuration of this UpdateCoreGatewayRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayAuthorizerConfiguration`
        """
        return self._authorizer_configuration

    @authorizer_configuration.setter
    def authorizer_configuration(self, authorizer_configuration):
        r"""Sets the authorizer_configuration of this UpdateCoreGatewayRequestBody.

        :param authorizer_configuration: The authorizer_configuration of this UpdateCoreGatewayRequestBody.
        :type authorizer_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayAuthorizerConfiguration`
        """
        self._authorizer_configuration = authorizer_configuration

    @property
    def protocol_configuration(self):
        r"""Gets the protocol_configuration of this UpdateCoreGatewayRequestBody.

        :return: The protocol_configuration of this UpdateCoreGatewayRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayUpdateProtocolConfiguration`
        """
        return self._protocol_configuration

    @protocol_configuration.setter
    def protocol_configuration(self, protocol_configuration):
        r"""Sets the protocol_configuration of this UpdateCoreGatewayRequestBody.

        :param protocol_configuration: The protocol_configuration of this UpdateCoreGatewayRequestBody.
        :type protocol_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayUpdateProtocolConfiguration`
        """
        self._protocol_configuration = protocol_configuration

    @property
    def log_delivery_configuration(self):
        r"""Gets the log_delivery_configuration of this UpdateCoreGatewayRequestBody.

        :return: The log_delivery_configuration of this UpdateCoreGatewayRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayLogDeliveryConfigurationRequestBody`
        """
        return self._log_delivery_configuration

    @log_delivery_configuration.setter
    def log_delivery_configuration(self, log_delivery_configuration):
        r"""Sets the log_delivery_configuration of this UpdateCoreGatewayRequestBody.

        :param log_delivery_configuration: The log_delivery_configuration of this UpdateCoreGatewayRequestBody.
        :type log_delivery_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayLogDeliveryConfigurationRequestBody`
        """
        self._log_delivery_configuration = log_delivery_configuration

    @property
    def tags(self):
        r"""Gets the tags of this UpdateCoreGatewayRequestBody.

        资源标签列表。

        :return: The tags of this UpdateCoreGatewayRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateCoreGatewayRequestBody.

        资源标签列表。

        :param tags: The tags of this UpdateCoreGatewayRequestBody.
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
        if not isinstance(other, UpdateCoreGatewayRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
