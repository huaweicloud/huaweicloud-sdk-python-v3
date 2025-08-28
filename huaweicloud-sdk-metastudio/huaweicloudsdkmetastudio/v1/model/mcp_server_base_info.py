# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class McpServerBaseInfo:

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
        'name': 'str'
    }

    attribute_map = {
        'mcp_server_id': 'mcp_server_id',
        'name': 'name'
    }

    def __init__(self, mcp_server_id=None, name=None):
        r"""McpServerBaseInfo

        The model defined in huaweicloud sdk

        :param mcp_server_id: MCP服务端对接配置ID。
        :type mcp_server_id: str
        :param name: MCP服务端对接配置名称。
        :type name: str
        """
        
        

        self._mcp_server_id = None
        self._name = None
        self.discriminator = None

        self.mcp_server_id = mcp_server_id
        if name is not None:
            self.name = name

    @property
    def mcp_server_id(self):
        r"""Gets the mcp_server_id of this McpServerBaseInfo.

        MCP服务端对接配置ID。

        :return: The mcp_server_id of this McpServerBaseInfo.
        :rtype: str
        """
        return self._mcp_server_id

    @mcp_server_id.setter
    def mcp_server_id(self, mcp_server_id):
        r"""Sets the mcp_server_id of this McpServerBaseInfo.

        MCP服务端对接配置ID。

        :param mcp_server_id: The mcp_server_id of this McpServerBaseInfo.
        :type mcp_server_id: str
        """
        self._mcp_server_id = mcp_server_id

    @property
    def name(self):
        r"""Gets the name of this McpServerBaseInfo.

        MCP服务端对接配置名称。

        :return: The name of this McpServerBaseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this McpServerBaseInfo.

        MCP服务端对接配置名称。

        :param name: The name of this McpServerBaseInfo.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, McpServerBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
