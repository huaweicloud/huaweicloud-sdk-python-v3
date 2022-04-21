# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SvcPort:

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
        'node_port': 'str',
        'port': 'str',
        'protocol': 'str',
        'target_port': 'str'
    }

    attribute_map = {
        'name': 'name',
        'node_port': 'node_port',
        'port': 'port',
        'protocol': 'protocol',
        'target_port': 'target_port'
    }

    def __init__(self, name=None, node_port=None, port=None, protocol=None, target_port=None):
        """SvcPort

        The model defined in huaweicloud sdk

        :param name: 服务端口必须进行命名，而且名称只允许是{protocol}-{suffix}这种格式，其中{protocol}可以是tcp、http等，IEF根据在端口上定义的协议来提供对应的路由能力。例如“name:http-0”和“name:tcp-0”是合法的端口名，“name:http2forecast”是非法的端口号。
        :type name: str
        :param node_port: 当spec.type&#x3D;NodePort时，指定映射到物理机的端口号
        :type node_port: str
        :param port: 服务监听的端口号
        :type port: str
        :param protocol: 具体的协议，比如TCP
        :type protocol: str
        :param target_port: 需要转发到后端Pod的端口号
        :type target_port: str
        """
        
        

        self._name = None
        self._node_port = None
        self._port = None
        self._protocol = None
        self._target_port = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if node_port is not None:
            self.node_port = node_port
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if target_port is not None:
            self.target_port = target_port

    @property
    def name(self):
        """Gets the name of this SvcPort.

        服务端口必须进行命名，而且名称只允许是{protocol}-{suffix}这种格式，其中{protocol}可以是tcp、http等，IEF根据在端口上定义的协议来提供对应的路由能力。例如“name:http-0”和“name:tcp-0”是合法的端口名，“name:http2forecast”是非法的端口号。

        :return: The name of this SvcPort.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SvcPort.

        服务端口必须进行命名，而且名称只允许是{protocol}-{suffix}这种格式，其中{protocol}可以是tcp、http等，IEF根据在端口上定义的协议来提供对应的路由能力。例如“name:http-0”和“name:tcp-0”是合法的端口名，“name:http2forecast”是非法的端口号。

        :param name: The name of this SvcPort.
        :type name: str
        """
        self._name = name

    @property
    def node_port(self):
        """Gets the node_port of this SvcPort.

        当spec.type=NodePort时，指定映射到物理机的端口号

        :return: The node_port of this SvcPort.
        :rtype: str
        """
        return self._node_port

    @node_port.setter
    def node_port(self, node_port):
        """Sets the node_port of this SvcPort.

        当spec.type=NodePort时，指定映射到物理机的端口号

        :param node_port: The node_port of this SvcPort.
        :type node_port: str
        """
        self._node_port = node_port

    @property
    def port(self):
        """Gets the port of this SvcPort.

        服务监听的端口号

        :return: The port of this SvcPort.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SvcPort.

        服务监听的端口号

        :param port: The port of this SvcPort.
        :type port: str
        """
        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this SvcPort.

        具体的协议，比如TCP

        :return: The protocol of this SvcPort.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SvcPort.

        具体的协议，比如TCP

        :param protocol: The protocol of this SvcPort.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def target_port(self):
        """Gets the target_port of this SvcPort.

        需要转发到后端Pod的端口号

        :return: The target_port of this SvcPort.
        :rtype: str
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port):
        """Sets the target_port of this SvcPort.

        需要转发到后端Pod的端口号

        :param target_port: The target_port of this SvcPort.
        :type target_port: str
        """
        self._target_port = target_port

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
        if not isinstance(other, SvcPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
