# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEndpointServiceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approval_enabled': 'bool',
        'service_name': 'str',
        'ports': 'list[PortList]',
        'port_id': 'str',
        'tcp_proxy': 'str',
        'description': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'approval_enabled': 'approval_enabled',
        'service_name': 'service_name',
        'ports': 'ports',
        'port_id': 'port_id',
        'tcp_proxy': 'tcp_proxy',
        'description': 'description',
        'ip': 'ip'
    }

    def __init__(self, approval_enabled=None, service_name=None, ports=None, port_id=None, tcp_proxy=None, description=None, ip=None):
        r"""UpdateEndpointServiceRequestBody

        The model defined in huaweicloud sdk

        :param approval_enabled: 是否需要审批。  - false：不需审批，创建的终端节点连接直接为accepted状态。  - true：需审批，创建的终端节点连接需要终端节点服务所属用户审核后方可使用。 默认为true，需要审批。
        :type approval_enabled: bool
        :param service_name: 终端节点服务的名称，长度不大于16，允许传入大小写字母、数字、下划线、中划线。
        :type service_name: str
        :param ports: 服务开放的端口映射列表，同一个终端节点服务下，不允许重复的端口映射。 若多个终端节点服务共用一个port_id， 则终端节点之间服务的所有端口映射的server_port和protocol的组合不能重复， 单次最多添加200个。 该参数值将被全量更新。
        :type ports: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        :param port_id: 弹性云服务器IP地址对应的网卡ID
        :type port_id: str
        :param tcp_proxy: 用于控制将哪些信息（如客户端的源IP、源端口、marker_id等）携带到服务端。 支持携带的客户端信息包括如下两种类型：  - TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明：仅当后端资源为OBS时，支持TCP TOA类型信息携带方式。  - Proxy Protocol：表示将客户端信息插入到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置才有效。 该参数的取值包括：  - close：表示关闭代理协议。  - toa_open：表示开启代理协议“tcp_toa”。  - proxy_open：表示开启代理协议“proxy_protocol”。  - open：表示同时开启代理协议“tcp_toa”和“proxy_protocol”。 默认值为“close”。
        :type tcp_proxy: str
        :param description: 描述字段，支持中英文字母、数字等字符，不支持“&lt;”或“&gt;”字符。
        :type description: str
        :param ip: 接口型VLAN场景服务端IPv4地址或域名
        :type ip: str
        """
        
        

        self._approval_enabled = None
        self._service_name = None
        self._ports = None
        self._port_id = None
        self._tcp_proxy = None
        self._description = None
        self._ip = None
        self.discriminator = None

        if approval_enabled is not None:
            self.approval_enabled = approval_enabled
        if service_name is not None:
            self.service_name = service_name
        if ports is not None:
            self.ports = ports
        if port_id is not None:
            self.port_id = port_id
        if tcp_proxy is not None:
            self.tcp_proxy = tcp_proxy
        if description is not None:
            self.description = description
        if ip is not None:
            self.ip = ip

    @property
    def approval_enabled(self):
        r"""Gets the approval_enabled of this UpdateEndpointServiceRequestBody.

        是否需要审批。  - false：不需审批，创建的终端节点连接直接为accepted状态。  - true：需审批，创建的终端节点连接需要终端节点服务所属用户审核后方可使用。 默认为true，需要审批。

        :return: The approval_enabled of this UpdateEndpointServiceRequestBody.
        :rtype: bool
        """
        return self._approval_enabled

    @approval_enabled.setter
    def approval_enabled(self, approval_enabled):
        r"""Sets the approval_enabled of this UpdateEndpointServiceRequestBody.

        是否需要审批。  - false：不需审批，创建的终端节点连接直接为accepted状态。  - true：需审批，创建的终端节点连接需要终端节点服务所属用户审核后方可使用。 默认为true，需要审批。

        :param approval_enabled: The approval_enabled of this UpdateEndpointServiceRequestBody.
        :type approval_enabled: bool
        """
        self._approval_enabled = approval_enabled

    @property
    def service_name(self):
        r"""Gets the service_name of this UpdateEndpointServiceRequestBody.

        终端节点服务的名称，长度不大于16，允许传入大小写字母、数字、下划线、中划线。

        :return: The service_name of this UpdateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this UpdateEndpointServiceRequestBody.

        终端节点服务的名称，长度不大于16，允许传入大小写字母、数字、下划线、中划线。

        :param service_name: The service_name of this UpdateEndpointServiceRequestBody.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def ports(self):
        r"""Gets the ports of this UpdateEndpointServiceRequestBody.

        服务开放的端口映射列表，同一个终端节点服务下，不允许重复的端口映射。 若多个终端节点服务共用一个port_id， 则终端节点之间服务的所有端口映射的server_port和protocol的组合不能重复， 单次最多添加200个。 该参数值将被全量更新。

        :return: The ports of this UpdateEndpointServiceRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        r"""Sets the ports of this UpdateEndpointServiceRequestBody.

        服务开放的端口映射列表，同一个终端节点服务下，不允许重复的端口映射。 若多个终端节点服务共用一个port_id， 则终端节点之间服务的所有端口映射的server_port和protocol的组合不能重复， 单次最多添加200个。 该参数值将被全量更新。

        :param ports: The ports of this UpdateEndpointServiceRequestBody.
        :type ports: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        """
        self._ports = ports

    @property
    def port_id(self):
        r"""Gets the port_id of this UpdateEndpointServiceRequestBody.

        弹性云服务器IP地址对应的网卡ID

        :return: The port_id of this UpdateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this UpdateEndpointServiceRequestBody.

        弹性云服务器IP地址对应的网卡ID

        :param port_id: The port_id of this UpdateEndpointServiceRequestBody.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def tcp_proxy(self):
        r"""Gets the tcp_proxy of this UpdateEndpointServiceRequestBody.

        用于控制将哪些信息（如客户端的源IP、源端口、marker_id等）携带到服务端。 支持携带的客户端信息包括如下两种类型：  - TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明：仅当后端资源为OBS时，支持TCP TOA类型信息携带方式。  - Proxy Protocol：表示将客户端信息插入到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置才有效。 该参数的取值包括：  - close：表示关闭代理协议。  - toa_open：表示开启代理协议“tcp_toa”。  - proxy_open：表示开启代理协议“proxy_protocol”。  - open：表示同时开启代理协议“tcp_toa”和“proxy_protocol”。 默认值为“close”。

        :return: The tcp_proxy of this UpdateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._tcp_proxy

    @tcp_proxy.setter
    def tcp_proxy(self, tcp_proxy):
        r"""Sets the tcp_proxy of this UpdateEndpointServiceRequestBody.

        用于控制将哪些信息（如客户端的源IP、源端口、marker_id等）携带到服务端。 支持携带的客户端信息包括如下两种类型：  - TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明：仅当后端资源为OBS时，支持TCP TOA类型信息携带方式。  - Proxy Protocol：表示将客户端信息插入到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置才有效。 该参数的取值包括：  - close：表示关闭代理协议。  - toa_open：表示开启代理协议“tcp_toa”。  - proxy_open：表示开启代理协议“proxy_protocol”。  - open：表示同时开启代理协议“tcp_toa”和“proxy_protocol”。 默认值为“close”。

        :param tcp_proxy: The tcp_proxy of this UpdateEndpointServiceRequestBody.
        :type tcp_proxy: str
        """
        self._tcp_proxy = tcp_proxy

    @property
    def description(self):
        r"""Gets the description of this UpdateEndpointServiceRequestBody.

        描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。

        :return: The description of this UpdateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateEndpointServiceRequestBody.

        描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。

        :param description: The description of this UpdateEndpointServiceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def ip(self):
        r"""Gets the ip of this UpdateEndpointServiceRequestBody.

        接口型VLAN场景服务端IPv4地址或域名

        :return: The ip of this UpdateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this UpdateEndpointServiceRequestBody.

        接口型VLAN场景服务端IPv4地址或域名

        :param ip: The ip of this UpdateEndpointServiceRequestBody.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, UpdateEndpointServiceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
