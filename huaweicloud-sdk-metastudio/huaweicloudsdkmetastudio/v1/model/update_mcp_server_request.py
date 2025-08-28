# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMcpServerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'mcp_server_id': 'str',
        'body': 'UpdateMcpServerReq'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'mcp_server_id': 'mcp_server_id',
        'body': 'body'
    }

    def __init__(self, x_app_user_id=None, mcp_server_id=None, body=None):
        r"""UpdateMcpServerRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param mcp_server_id: MCP服务端对接配置ID。
        :type mcp_server_id: str
        :param body: Body of the UpdateMcpServerRequest
        :type body: :class:`huaweicloudsdkmetastudio.v1.UpdateMcpServerReq`
        """
        
        

        self._x_app_user_id = None
        self._mcp_server_id = None
        self._body = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.mcp_server_id = mcp_server_id
        if body is not None:
            self.body = body

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this UpdateMcpServerRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this UpdateMcpServerRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this UpdateMcpServerRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this UpdateMcpServerRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def mcp_server_id(self):
        r"""Gets the mcp_server_id of this UpdateMcpServerRequest.

        MCP服务端对接配置ID。

        :return: The mcp_server_id of this UpdateMcpServerRequest.
        :rtype: str
        """
        return self._mcp_server_id

    @mcp_server_id.setter
    def mcp_server_id(self, mcp_server_id):
        r"""Sets the mcp_server_id of this UpdateMcpServerRequest.

        MCP服务端对接配置ID。

        :param mcp_server_id: The mcp_server_id of this UpdateMcpServerRequest.
        :type mcp_server_id: str
        """
        self._mcp_server_id = mcp_server_id

    @property
    def body(self):
        r"""Gets the body of this UpdateMcpServerRequest.

        :return: The body of this UpdateMcpServerRequest.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateMcpServerReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateMcpServerRequest.

        :param body: The body of this UpdateMcpServerRequest.
        :type body: :class:`huaweicloudsdkmetastudio.v1.UpdateMcpServerReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateMcpServerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
