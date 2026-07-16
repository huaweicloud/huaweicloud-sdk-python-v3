# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayTargetConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mcp_server': 'CoreGatewayMcpServerTargetConfiguration',
        'openapi': 'CoreGatewayOpenApiTargetConfiguration'
    }

    attribute_map = {
        'mcp_server': 'mcp_server',
        'openapi': 'openapi'
    }

    def __init__(self, mcp_server=None, openapi=None):
        r"""CoreGatewayTargetConfiguration

        The model defined in huaweicloud sdk

        :param mcp_server: 
        :type mcp_server: :class:`huaweicloudsdkagentarts.v1.CoreGatewayMcpServerTargetConfiguration`
        :param openapi: 
        :type openapi: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOpenApiTargetConfiguration`
        """
        
        

        self._mcp_server = None
        self._openapi = None
        self.discriminator = None

        if mcp_server is not None:
            self.mcp_server = mcp_server
        if openapi is not None:
            self.openapi = openapi

    @property
    def mcp_server(self):
        r"""Gets the mcp_server of this CoreGatewayTargetConfiguration.

        :return: The mcp_server of this CoreGatewayTargetConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayMcpServerTargetConfiguration`
        """
        return self._mcp_server

    @mcp_server.setter
    def mcp_server(self, mcp_server):
        r"""Sets the mcp_server of this CoreGatewayTargetConfiguration.

        :param mcp_server: The mcp_server of this CoreGatewayTargetConfiguration.
        :type mcp_server: :class:`huaweicloudsdkagentarts.v1.CoreGatewayMcpServerTargetConfiguration`
        """
        self._mcp_server = mcp_server

    @property
    def openapi(self):
        r"""Gets the openapi of this CoreGatewayTargetConfiguration.

        :return: The openapi of this CoreGatewayTargetConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOpenApiTargetConfiguration`
        """
        return self._openapi

    @openapi.setter
    def openapi(self, openapi):
        r"""Sets the openapi of this CoreGatewayTargetConfiguration.

        :param openapi: The openapi of this CoreGatewayTargetConfiguration.
        :type openapi: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOpenApiTargetConfiguration`
        """
        self._openapi = openapi

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
        if not isinstance(other, CoreGatewayTargetConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
