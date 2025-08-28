# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMcpServerReq:

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
        'mcp_server_url': 'str',
        'auth_header_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'mcp_server_url': 'mcp_server_url',
        'auth_header_name': 'auth_header_name'
    }

    def __init__(self, name=None, mcp_server_url=None, auth_header_name=None):
        r"""CreateMcpServerReq

        The model defined in huaweicloud sdk

        :param name: MCP服务端对接配置名称。
        :type name: str
        :param mcp_server_url: MCP服务端地址。
        :type mcp_server_url: str
        :param auth_header_name: 鉴权头域名称。
        :type auth_header_name: str
        """
        
        

        self._name = None
        self._mcp_server_url = None
        self._auth_header_name = None
        self.discriminator = None

        self.name = name
        self.mcp_server_url = mcp_server_url
        if auth_header_name is not None:
            self.auth_header_name = auth_header_name

    @property
    def name(self):
        r"""Gets the name of this CreateMcpServerReq.

        MCP服务端对接配置名称。

        :return: The name of this CreateMcpServerReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateMcpServerReq.

        MCP服务端对接配置名称。

        :param name: The name of this CreateMcpServerReq.
        :type name: str
        """
        self._name = name

    @property
    def mcp_server_url(self):
        r"""Gets the mcp_server_url of this CreateMcpServerReq.

        MCP服务端地址。

        :return: The mcp_server_url of this CreateMcpServerReq.
        :rtype: str
        """
        return self._mcp_server_url

    @mcp_server_url.setter
    def mcp_server_url(self, mcp_server_url):
        r"""Sets the mcp_server_url of this CreateMcpServerReq.

        MCP服务端地址。

        :param mcp_server_url: The mcp_server_url of this CreateMcpServerReq.
        :type mcp_server_url: str
        """
        self._mcp_server_url = mcp_server_url

    @property
    def auth_header_name(self):
        r"""Gets the auth_header_name of this CreateMcpServerReq.

        鉴权头域名称。

        :return: The auth_header_name of this CreateMcpServerReq.
        :rtype: str
        """
        return self._auth_header_name

    @auth_header_name.setter
    def auth_header_name(self, auth_header_name):
        r"""Sets the auth_header_name of this CreateMcpServerReq.

        鉴权头域名称。

        :param auth_header_name: The auth_header_name of this CreateMcpServerReq.
        :type auth_header_name: str
        """
        self._auth_header_name = auth_header_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateMcpServerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
