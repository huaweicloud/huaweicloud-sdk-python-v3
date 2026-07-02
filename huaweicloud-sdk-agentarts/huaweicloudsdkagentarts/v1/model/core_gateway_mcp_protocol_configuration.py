# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayMcpProtocolConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_configuration': 'CoreGatewaySearchConfiguration',
        'supported_versions': 'list[str]'
    }

    attribute_map = {
        'search_configuration': 'search_configuration',
        'supported_versions': 'supported_versions'
    }

    def __init__(self, search_configuration=None, supported_versions=None):
        r"""CoreGatewayMcpProtocolConfiguration

        The model defined in huaweicloud sdk

        :param search_configuration: 
        :type search_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewaySearchConfiguration`
        :param supported_versions: MCP网关支持的协议版本列表。
        :type supported_versions: list[str]
        """
        
        

        self._search_configuration = None
        self._supported_versions = None
        self.discriminator = None

        if search_configuration is not None:
            self.search_configuration = search_configuration
        if supported_versions is not None:
            self.supported_versions = supported_versions

    @property
    def search_configuration(self):
        r"""Gets the search_configuration of this CoreGatewayMcpProtocolConfiguration.

        :return: The search_configuration of this CoreGatewayMcpProtocolConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewaySearchConfiguration`
        """
        return self._search_configuration

    @search_configuration.setter
    def search_configuration(self, search_configuration):
        r"""Sets the search_configuration of this CoreGatewayMcpProtocolConfiguration.

        :param search_configuration: The search_configuration of this CoreGatewayMcpProtocolConfiguration.
        :type search_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewaySearchConfiguration`
        """
        self._search_configuration = search_configuration

    @property
    def supported_versions(self):
        r"""Gets the supported_versions of this CoreGatewayMcpProtocolConfiguration.

        MCP网关支持的协议版本列表。

        :return: The supported_versions of this CoreGatewayMcpProtocolConfiguration.
        :rtype: list[str]
        """
        return self._supported_versions

    @supported_versions.setter
    def supported_versions(self, supported_versions):
        r"""Sets the supported_versions of this CoreGatewayMcpProtocolConfiguration.

        MCP网关支持的协议版本列表。

        :param supported_versions: The supported_versions of this CoreGatewayMcpProtocolConfiguration.
        :type supported_versions: list[str]
        """
        self._supported_versions = supported_versions

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
        if not isinstance(other, CoreGatewayMcpProtocolConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
