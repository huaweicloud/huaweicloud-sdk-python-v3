# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateElbClusterPortRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'elb_id': 'str',
        'mode': 'str',
        'lb_listener_port': 'int',
        'server_port': 'int',
        'tunnel_lb_listener_port': 'int',
        'tunnel_server_port': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'elb_id': 'elb_id',
        'mode': 'mode',
        'lb_listener_port': 'lb_listener_port',
        'server_port': 'server_port',
        'tunnel_lb_listener_port': 'tunnel_lb_listener_port',
        'tunnel_server_port': 'tunnel_server_port'
    }

    def __init__(self, cluster_id=None, elb_id=None, mode=None, lb_listener_port=None, server_port=None, tunnel_lb_listener_port=None, tunnel_server_port=None):
        r"""CreateElbClusterPortRequestBody

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param elb_id: elb id。端口映射将会在该elb中创建
        :type elb_id: str
        :param mode: 新增的端口的模式。除了VPN外，其他类型的服务只支持 PROXY
        :type mode: str
        :param lb_listener_port: 将在elb中为代理通道创建的监听器的端口
        :type lb_listener_port: int
        :param server_port: 将在elb中为代理通道创建的后端服务组中后端服务器的端口。无默认值。
        :type server_port: int
        :param tunnel_lb_listener_port: 将在elb中给VPN隧道创建的监听器的端口。当mode&#x3D;TUNNEL时，必填
        :type tunnel_lb_listener_port: int
        :param tunnel_server_port: 将在elb中给VPN隧道创建的后端服务组中后端服务器的端口。 当mode&#x3D;TUNNEL时，必填，有默认值:20706。
        :type tunnel_server_port: int
        """
        
        

        self._cluster_id = None
        self._elb_id = None
        self._mode = None
        self._lb_listener_port = None
        self._server_port = None
        self._tunnel_lb_listener_port = None
        self._tunnel_server_port = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.elb_id = elb_id
        self.mode = mode
        self.lb_listener_port = lb_listener_port
        self.server_port = server_port
        if tunnel_lb_listener_port is not None:
            self.tunnel_lb_listener_port = tunnel_lb_listener_port
        if tunnel_server_port is not None:
            self.tunnel_server_port = tunnel_server_port

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CreateElbClusterPortRequestBody.

        集群id

        :return: The cluster_id of this CreateElbClusterPortRequestBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CreateElbClusterPortRequestBody.

        集群id

        :param cluster_id: The cluster_id of this CreateElbClusterPortRequestBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def elb_id(self):
        r"""Gets the elb_id of this CreateElbClusterPortRequestBody.

        elb id。端口映射将会在该elb中创建

        :return: The elb_id of this CreateElbClusterPortRequestBody.
        :rtype: str
        """
        return self._elb_id

    @elb_id.setter
    def elb_id(self, elb_id):
        r"""Sets the elb_id of this CreateElbClusterPortRequestBody.

        elb id。端口映射将会在该elb中创建

        :param elb_id: The elb_id of this CreateElbClusterPortRequestBody.
        :type elb_id: str
        """
        self._elb_id = elb_id

    @property
    def mode(self):
        r"""Gets the mode of this CreateElbClusterPortRequestBody.

        新增的端口的模式。除了VPN外，其他类型的服务只支持 PROXY

        :return: The mode of this CreateElbClusterPortRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateElbClusterPortRequestBody.

        新增的端口的模式。除了VPN外，其他类型的服务只支持 PROXY

        :param mode: The mode of this CreateElbClusterPortRequestBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def lb_listener_port(self):
        r"""Gets the lb_listener_port of this CreateElbClusterPortRequestBody.

        将在elb中为代理通道创建的监听器的端口

        :return: The lb_listener_port of this CreateElbClusterPortRequestBody.
        :rtype: int
        """
        return self._lb_listener_port

    @lb_listener_port.setter
    def lb_listener_port(self, lb_listener_port):
        r"""Sets the lb_listener_port of this CreateElbClusterPortRequestBody.

        将在elb中为代理通道创建的监听器的端口

        :param lb_listener_port: The lb_listener_port of this CreateElbClusterPortRequestBody.
        :type lb_listener_port: int
        """
        self._lb_listener_port = lb_listener_port

    @property
    def server_port(self):
        r"""Gets the server_port of this CreateElbClusterPortRequestBody.

        将在elb中为代理通道创建的后端服务组中后端服务器的端口。无默认值。

        :return: The server_port of this CreateElbClusterPortRequestBody.
        :rtype: int
        """
        return self._server_port

    @server_port.setter
    def server_port(self, server_port):
        r"""Sets the server_port of this CreateElbClusterPortRequestBody.

        将在elb中为代理通道创建的后端服务组中后端服务器的端口。无默认值。

        :param server_port: The server_port of this CreateElbClusterPortRequestBody.
        :type server_port: int
        """
        self._server_port = server_port

    @property
    def tunnel_lb_listener_port(self):
        r"""Gets the tunnel_lb_listener_port of this CreateElbClusterPortRequestBody.

        将在elb中给VPN隧道创建的监听器的端口。当mode=TUNNEL时，必填

        :return: The tunnel_lb_listener_port of this CreateElbClusterPortRequestBody.
        :rtype: int
        """
        return self._tunnel_lb_listener_port

    @tunnel_lb_listener_port.setter
    def tunnel_lb_listener_port(self, tunnel_lb_listener_port):
        r"""Sets the tunnel_lb_listener_port of this CreateElbClusterPortRequestBody.

        将在elb中给VPN隧道创建的监听器的端口。当mode=TUNNEL时，必填

        :param tunnel_lb_listener_port: The tunnel_lb_listener_port of this CreateElbClusterPortRequestBody.
        :type tunnel_lb_listener_port: int
        """
        self._tunnel_lb_listener_port = tunnel_lb_listener_port

    @property
    def tunnel_server_port(self):
        r"""Gets the tunnel_server_port of this CreateElbClusterPortRequestBody.

        将在elb中给VPN隧道创建的后端服务组中后端服务器的端口。 当mode=TUNNEL时，必填，有默认值:20706。

        :return: The tunnel_server_port of this CreateElbClusterPortRequestBody.
        :rtype: int
        """
        return self._tunnel_server_port

    @tunnel_server_port.setter
    def tunnel_server_port(self, tunnel_server_port):
        r"""Sets the tunnel_server_port of this CreateElbClusterPortRequestBody.

        将在elb中给VPN隧道创建的后端服务组中后端服务器的端口。 当mode=TUNNEL时，必填，有默认值:20706。

        :param tunnel_server_port: The tunnel_server_port of this CreateElbClusterPortRequestBody.
        :type tunnel_server_port: int
        """
        self._tunnel_server_port = tunnel_server_port

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
        if not isinstance(other, CreateElbClusterPortRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
