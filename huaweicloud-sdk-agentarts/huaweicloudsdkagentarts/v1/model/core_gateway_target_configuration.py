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
        'openapi': 'CoreGatewayOpenApiTargetConfiguration',
        'dedicated_gateway_api': 'CoreGatewayDedicatedGatewayApiTargetConfiguration',
        'cloud_service_open_api': 'CoreGatewayCloudServiceApiTargetConfiguration',
        'inference': 'CoreGatewayTargetInferenceConfiguration'
    }

    attribute_map = {
        'mcp_server': 'mcp_server',
        'openapi': 'openapi',
        'dedicated_gateway_api': 'dedicated_gateway_api',
        'cloud_service_open_api': 'cloud_service_open_api',
        'inference': 'inference'
    }

    def __init__(self, mcp_server=None, openapi=None, dedicated_gateway_api=None, cloud_service_open_api=None, inference=None):
        r"""CoreGatewayTargetConfiguration

        The model defined in huaweicloud sdk

        :param mcp_server: 
        :type mcp_server: :class:`huaweicloudsdkagentarts.v1.CoreGatewayMcpServerTargetConfiguration`
        :param openapi: 
        :type openapi: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOpenApiTargetConfiguration`
        :param dedicated_gateway_api: 
        :type dedicated_gateway_api: :class:`huaweicloudsdkagentarts.v1.CoreGatewayDedicatedGatewayApiTargetConfiguration`
        :param cloud_service_open_api: 
        :type cloud_service_open_api: :class:`huaweicloudsdkagentarts.v1.CoreGatewayCloudServiceApiTargetConfiguration`
        :param inference: 
        :type inference: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetInferenceConfiguration`
        """
        
        

        self._mcp_server = None
        self._openapi = None
        self._dedicated_gateway_api = None
        self._cloud_service_open_api = None
        self._inference = None
        self.discriminator = None

        if mcp_server is not None:
            self.mcp_server = mcp_server
        if openapi is not None:
            self.openapi = openapi
        if dedicated_gateway_api is not None:
            self.dedicated_gateway_api = dedicated_gateway_api
        if cloud_service_open_api is not None:
            self.cloud_service_open_api = cloud_service_open_api
        if inference is not None:
            self.inference = inference

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

    @property
    def dedicated_gateway_api(self):
        r"""Gets the dedicated_gateway_api of this CoreGatewayTargetConfiguration.

        :return: The dedicated_gateway_api of this CoreGatewayTargetConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayDedicatedGatewayApiTargetConfiguration`
        """
        return self._dedicated_gateway_api

    @dedicated_gateway_api.setter
    def dedicated_gateway_api(self, dedicated_gateway_api):
        r"""Sets the dedicated_gateway_api of this CoreGatewayTargetConfiguration.

        :param dedicated_gateway_api: The dedicated_gateway_api of this CoreGatewayTargetConfiguration.
        :type dedicated_gateway_api: :class:`huaweicloudsdkagentarts.v1.CoreGatewayDedicatedGatewayApiTargetConfiguration`
        """
        self._dedicated_gateway_api = dedicated_gateway_api

    @property
    def cloud_service_open_api(self):
        r"""Gets the cloud_service_open_api of this CoreGatewayTargetConfiguration.

        :return: The cloud_service_open_api of this CoreGatewayTargetConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayCloudServiceApiTargetConfiguration`
        """
        return self._cloud_service_open_api

    @cloud_service_open_api.setter
    def cloud_service_open_api(self, cloud_service_open_api):
        r"""Sets the cloud_service_open_api of this CoreGatewayTargetConfiguration.

        :param cloud_service_open_api: The cloud_service_open_api of this CoreGatewayTargetConfiguration.
        :type cloud_service_open_api: :class:`huaweicloudsdkagentarts.v1.CoreGatewayCloudServiceApiTargetConfiguration`
        """
        self._cloud_service_open_api = cloud_service_open_api

    @property
    def inference(self):
        r"""Gets the inference of this CoreGatewayTargetConfiguration.

        :return: The inference of this CoreGatewayTargetConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetInferenceConfiguration`
        """
        return self._inference

    @inference.setter
    def inference(self, inference):
        r"""Sets the inference of this CoreGatewayTargetConfiguration.

        :param inference: The inference of this CoreGatewayTargetConfiguration.
        :type inference: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetInferenceConfiguration`
        """
        self._inference = inference

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
