# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayMcpServerTargetConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint': 'str',
        'server_type': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'server_type': 'server_type'
    }

    def __init__(self, endpoint=None, server_type=None):
        r"""CoreGatewayMcpServerTargetConfiguration

        The model defined in huaweicloud sdk

        :param endpoint: **参数解释：** MCP服务器端点 URL。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-512个字符，匹配以 https:// 开头的任意字符串，符合正则条件https://.*。 **默认取值：** 不涉及。 
        :type endpoint: str
        :param server_type: **参数解释：** MCP 服务器类型。 **约束限制：** 不涉及。 **取值范围：** - &#x60;sse&#x60;: 使用 Server-Sent Events 长连接 - &#x60;streamable_http&#x60;: 使用可流式 HTTP 请求 **默认取值：** 不涉及。 
        :type server_type: str
        """
        
        

        self._endpoint = None
        self._server_type = None
        self.discriminator = None

        self.endpoint = endpoint
        self.server_type = server_type

    @property
    def endpoint(self):
        r"""Gets the endpoint of this CoreGatewayMcpServerTargetConfiguration.

        **参数解释：** MCP服务器端点 URL。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-512个字符，匹配以 https:// 开头的任意字符串，符合正则条件https://.*。 **默认取值：** 不涉及。 

        :return: The endpoint of this CoreGatewayMcpServerTargetConfiguration.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this CoreGatewayMcpServerTargetConfiguration.

        **参数解释：** MCP服务器端点 URL。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-512个字符，匹配以 https:// 开头的任意字符串，符合正则条件https://.*。 **默认取值：** 不涉及。 

        :param endpoint: The endpoint of this CoreGatewayMcpServerTargetConfiguration.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def server_type(self):
        r"""Gets the server_type of this CoreGatewayMcpServerTargetConfiguration.

        **参数解释：** MCP 服务器类型。 **约束限制：** 不涉及。 **取值范围：** - `sse`: 使用 Server-Sent Events 长连接 - `streamable_http`: 使用可流式 HTTP 请求 **默认取值：** 不涉及。 

        :return: The server_type of this CoreGatewayMcpServerTargetConfiguration.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this CoreGatewayMcpServerTargetConfiguration.

        **参数解释：** MCP 服务器类型。 **约束限制：** 不涉及。 **取值范围：** - `sse`: 使用 Server-Sent Events 长连接 - `streamable_http`: 使用可流式 HTTP 请求 **默认取值：** 不涉及。 

        :param server_type: The server_type of this CoreGatewayMcpServerTargetConfiguration.
        :type server_type: str
        """
        self._server_type = server_type

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
        if not isinstance(other, CoreGatewayMcpServerTargetConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
