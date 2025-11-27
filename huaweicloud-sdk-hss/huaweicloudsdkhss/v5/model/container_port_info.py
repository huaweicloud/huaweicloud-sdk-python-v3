# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerPortInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container_port': 'int',
        'host_ip': 'str',
        'host_port': 'int',
        'port_name': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'container_port': 'container_port',
        'host_ip': 'host_ip',
        'host_port': 'host_port',
        'port_name': 'port_name',
        'protocol': 'protocol'
    }

    def __init__(self, container_port=None, host_ip=None, host_port=None, port_name=None, protocol=None):
        r"""ContainerPortInfo

        The model defined in huaweicloud sdk

        :param container_port: 容器端口
        :type container_port: int
        :param host_ip: 主机IP
        :type host_ip: str
        :param host_port: 主机端口
        :type host_port: int
        :param port_name: 端口名称
        :type port_name: str
        :param protocol: 端口协议，举例如下 -TCP,默认TCP -UDP
        :type protocol: str
        """
        
        

        self._container_port = None
        self._host_ip = None
        self._host_port = None
        self._port_name = None
        self._protocol = None
        self.discriminator = None

        if container_port is not None:
            self.container_port = container_port
        if host_ip is not None:
            self.host_ip = host_ip
        if host_port is not None:
            self.host_port = host_port
        if port_name is not None:
            self.port_name = port_name
        if protocol is not None:
            self.protocol = protocol

    @property
    def container_port(self):
        r"""Gets the container_port of this ContainerPortInfo.

        容器端口

        :return: The container_port of this ContainerPortInfo.
        :rtype: int
        """
        return self._container_port

    @container_port.setter
    def container_port(self, container_port):
        r"""Sets the container_port of this ContainerPortInfo.

        容器端口

        :param container_port: The container_port of this ContainerPortInfo.
        :type container_port: int
        """
        self._container_port = container_port

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ContainerPortInfo.

        主机IP

        :return: The host_ip of this ContainerPortInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ContainerPortInfo.

        主机IP

        :param host_ip: The host_ip of this ContainerPortInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_port(self):
        r"""Gets the host_port of this ContainerPortInfo.

        主机端口

        :return: The host_port of this ContainerPortInfo.
        :rtype: int
        """
        return self._host_port

    @host_port.setter
    def host_port(self, host_port):
        r"""Sets the host_port of this ContainerPortInfo.

        主机端口

        :param host_port: The host_port of this ContainerPortInfo.
        :type host_port: int
        """
        self._host_port = host_port

    @property
    def port_name(self):
        r"""Gets the port_name of this ContainerPortInfo.

        端口名称

        :return: The port_name of this ContainerPortInfo.
        :rtype: str
        """
        return self._port_name

    @port_name.setter
    def port_name(self, port_name):
        r"""Sets the port_name of this ContainerPortInfo.

        端口名称

        :param port_name: The port_name of this ContainerPortInfo.
        :type port_name: str
        """
        self._port_name = port_name

    @property
    def protocol(self):
        r"""Gets the protocol of this ContainerPortInfo.

        端口协议，举例如下 -TCP,默认TCP -UDP

        :return: The protocol of this ContainerPortInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ContainerPortInfo.

        端口协议，举例如下 -TCP,默认TCP -UDP

        :param protocol: The protocol of this ContainerPortInfo.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, ContainerPortInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
