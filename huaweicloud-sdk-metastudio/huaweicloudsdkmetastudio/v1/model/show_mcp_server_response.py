# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMcpServerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mcp_server_id': 'str',
        'name': 'str',
        'mcp_server_url': 'str',
        'auth_header_name': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'mcp_server_id': 'mcp_server_id',
        'name': 'name',
        'mcp_server_url': 'mcp_server_url',
        'auth_header_name': 'auth_header_name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, mcp_server_id=None, name=None, mcp_server_url=None, auth_header_name=None, create_time=None, update_time=None, x_request_id=None):
        r"""ShowMcpServerResponse

        The model defined in huaweicloud sdk

        :param mcp_server_id: MCP服务端对接配置ID。
        :type mcp_server_id: str
        :param name: MCP服务端对接配置名称。
        :type name: str
        :param mcp_server_url: MCP服务端地址。
        :type mcp_server_url: str
        :param auth_header_name: 鉴权头域名称。
        :type auth_header_name: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowMcpServerResponse, self).__init__()

        self._mcp_server_id = None
        self._name = None
        self._mcp_server_url = None
        self._auth_header_name = None
        self._create_time = None
        self._update_time = None
        self._x_request_id = None
        self.discriminator = None

        if mcp_server_id is not None:
            self.mcp_server_id = mcp_server_id
        if name is not None:
            self.name = name
        if mcp_server_url is not None:
            self.mcp_server_url = mcp_server_url
        if auth_header_name is not None:
            self.auth_header_name = auth_header_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def mcp_server_id(self):
        r"""Gets the mcp_server_id of this ShowMcpServerResponse.

        MCP服务端对接配置ID。

        :return: The mcp_server_id of this ShowMcpServerResponse.
        :rtype: str
        """
        return self._mcp_server_id

    @mcp_server_id.setter
    def mcp_server_id(self, mcp_server_id):
        r"""Sets the mcp_server_id of this ShowMcpServerResponse.

        MCP服务端对接配置ID。

        :param mcp_server_id: The mcp_server_id of this ShowMcpServerResponse.
        :type mcp_server_id: str
        """
        self._mcp_server_id = mcp_server_id

    @property
    def name(self):
        r"""Gets the name of this ShowMcpServerResponse.

        MCP服务端对接配置名称。

        :return: The name of this ShowMcpServerResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowMcpServerResponse.

        MCP服务端对接配置名称。

        :param name: The name of this ShowMcpServerResponse.
        :type name: str
        """
        self._name = name

    @property
    def mcp_server_url(self):
        r"""Gets the mcp_server_url of this ShowMcpServerResponse.

        MCP服务端地址。

        :return: The mcp_server_url of this ShowMcpServerResponse.
        :rtype: str
        """
        return self._mcp_server_url

    @mcp_server_url.setter
    def mcp_server_url(self, mcp_server_url):
        r"""Sets the mcp_server_url of this ShowMcpServerResponse.

        MCP服务端地址。

        :param mcp_server_url: The mcp_server_url of this ShowMcpServerResponse.
        :type mcp_server_url: str
        """
        self._mcp_server_url = mcp_server_url

    @property
    def auth_header_name(self):
        r"""Gets the auth_header_name of this ShowMcpServerResponse.

        鉴权头域名称。

        :return: The auth_header_name of this ShowMcpServerResponse.
        :rtype: str
        """
        return self._auth_header_name

    @auth_header_name.setter
    def auth_header_name(self, auth_header_name):
        r"""Sets the auth_header_name of this ShowMcpServerResponse.

        鉴权头域名称。

        :param auth_header_name: The auth_header_name of this ShowMcpServerResponse.
        :type auth_header_name: str
        """
        self._auth_header_name = auth_header_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowMcpServerResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowMcpServerResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowMcpServerResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowMcpServerResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowMcpServerResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ShowMcpServerResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowMcpServerResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ShowMcpServerResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowMcpServerResponse.

        :return: The x_request_id of this ShowMcpServerResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowMcpServerResponse.

        :param x_request_id: The x_request_id of this ShowMcpServerResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowMcpServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
