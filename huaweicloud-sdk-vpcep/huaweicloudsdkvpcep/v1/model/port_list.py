# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_port': 'int',
        'server_port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'client_port': 'client_port',
        'server_port': 'server_port',
        'protocol': 'protocol'
    }

    def __init__(self, client_port=None, server_port=None, protocol=None):
        """PortList

        The model defined in huaweicloud sdk

        :param client_port: 终端节点访问的端口。 终端节点提供给用户，作为访问终端节点服务的端口，范围1-65535。
        :type client_port: int
        :param server_port: 终端节点服务的端口。 终端节点服务绑定了后端资源，作为提供服务的端口，范围1-65535。
        :type server_port: int
        :param protocol: 端口映射协议，支持TCP。
        :type protocol: str
        """
        
        

        self._client_port = None
        self._server_port = None
        self._protocol = None
        self.discriminator = None

        if client_port is not None:
            self.client_port = client_port
        if server_port is not None:
            self.server_port = server_port
        if protocol is not None:
            self.protocol = protocol

    @property
    def client_port(self):
        """Gets the client_port of this PortList.

        终端节点访问的端口。 终端节点提供给用户，作为访问终端节点服务的端口，范围1-65535。

        :return: The client_port of this PortList.
        :rtype: int
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        """Sets the client_port of this PortList.

        终端节点访问的端口。 终端节点提供给用户，作为访问终端节点服务的端口，范围1-65535。

        :param client_port: The client_port of this PortList.
        :type client_port: int
        """
        self._client_port = client_port

    @property
    def server_port(self):
        """Gets the server_port of this PortList.

        终端节点服务的端口。 终端节点服务绑定了后端资源，作为提供服务的端口，范围1-65535。

        :return: The server_port of this PortList.
        :rtype: int
        """
        return self._server_port

    @server_port.setter
    def server_port(self, server_port):
        """Sets the server_port of this PortList.

        终端节点服务的端口。 终端节点服务绑定了后端资源，作为提供服务的端口，范围1-65535。

        :param server_port: The server_port of this PortList.
        :type server_port: int
        """
        self._server_port = server_port

    @property
    def protocol(self):
        """Gets the protocol of this PortList.

        端口映射协议，支持TCP。

        :return: The protocol of this PortList.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PortList.

        端口映射协议，支持TCP。

        :param protocol: The protocol of this PortList.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, PortList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
