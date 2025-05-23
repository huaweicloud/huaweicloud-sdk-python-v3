# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointServiceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port_id': 'str',
        'service_name': 'str',
        'vpc_id': 'str',
        'approval_enabled': 'bool',
        'service_type': 'str',
        'server_type': 'str',
        'ip': 'str',
        'ports': 'list[PortList]',
        'tcp_proxy': 'str',
        'tags': 'list[TagList]',
        'description': 'str',
        'ip_version': 'str',
        'snat_network_id': 'str'
    }

    attribute_map = {
        'port_id': 'port_id',
        'service_name': 'service_name',
        'vpc_id': 'vpc_id',
        'approval_enabled': 'approval_enabled',
        'service_type': 'service_type',
        'server_type': 'server_type',
        'ip': 'ip',
        'ports': 'ports',
        'tcp_proxy': 'tcp_proxy',
        'tags': 'tags',
        'description': 'description',
        'ip_version': 'ip_version',
        'snat_network_id': 'snat_network_id'
    }

    def __init__(self, port_id=None, service_name=None, vpc_id=None, approval_enabled=None, service_type=None, server_type=None, ip=None, ports=None, tcp_proxy=None, tags=None, description=None, ip_version=None, snat_network_id=None):
        r"""CreateEndpointServiceRequestBody

        The model defined in huaweicloud sdk

        :param port_id: 标识终端节点服务后端资源的ID， 格式为通用唯一识别码（Universally Unique Identifier，下文简称UUID）。 取值为： - LB类型：负载均衡器内网IP对应的端口ID。 详细内容请参考《弹性负载均衡API参考》中的“查询负载均衡详情”。 - VM类型：弹性云服务器IP地址对应的网卡ID。 详细内容请参考《弹性云服务器API参考》中的“查询云服务器网卡信息”， 详见响应消息中的“port_id”字段。 - VIP类型：虚拟IP所在虚拟机的网卡ID（VIP类型业务已不支持，该取值类型已废弃） 说明： - 创建终端节点服务时，VPC的子网网段不能与198.19.128.0/17重叠。 - VPC路由表中自定义路由的目的地址不能与198.19.128.0/17重叠。
        :type port_id: str
        :param service_name: 终端节点服务的名称，长度不大于16，允许传入大小写字母、数字、下划线、中划线。 - 传入为空，存入值为regionName+.+serviceId - 传入不为空并校验通过，存入值为regionName+.+serviceName+.+serviceId
        :type service_name: str
        :param vpc_id: 终端节点服务对应后端资源所在的VPC的ID。
        :type vpc_id: str
        :param approval_enabled: 是否需要审批。  - false：不需要审批，创建的终端节点连接直接为accepted状态。  - true：需要审批，创建的终端节点连接为pendingAcceptance状态， 需要终端节点服务所属用户审核后方可使用。 默认为true，需要审批。
        :type approval_enabled: bool
        :param service_type: 终端节点服务类型。 仅支持将用户私有服务创建为interface类型的终端节点服务。 终端节点服务类型包括“网关（gateway）型”和“接口（interface）型”：  - gateway：由运维人员配置。用户无需创建，可直接使用。  - interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建， 用户可直接使用。 您可以通过查询公共终端节点服务列表， 查看由运维人员配置的所有用户可见且可连接的终端节点服务， 并通过创建终端节点创建访问Gateway和Interface类型终端节点服务的终端节点。
        :type service_type: str
        :param server_type: 资源类型。  - VM：云服务器，适用于作为服务器使用。  - VIP：虚拟IP，适用于作为虚IP场景使用。（该字段已废弃，请优先使用LB类型）  - LB：负载均衡，适用于高访问量业务和对可靠性和容灾性要求较高的业务。
        :type server_type: str
        :param ip: 接口型VLAN场景服务端IPv4地址或域名
        :type ip: str
        :param ports: 服务开放的端口映射列表，详细内容请参见表4-10。 同一个终端节点服务下，不允许重复的端口映射。若多个终端节点服务共用一个port_id， 则终端节点服务之间的所有端口映射的server_port和protocol的组合不能重复， 单次最多添加200个。
        :type ports: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        :param tcp_proxy: 用于控制将哪些信息（如客户端的源IP、源端口、marker_id等）携带到服务端。 支持携带的客户端信息包括如下两种类型：  - TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明：仅当后端资源为OBS时，支持TCP TOA类型信息携带方式。  - Proxy Protocol：表示将客户端信息插入到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置才有效。 该参数的取值包括：  - close：表示关闭代理协议。  - toa_open：表示开启代理协议“tcp_toa”。  - proxy_open：表示开启代理协议“proxy_protocol”。  - open：表示同时开启代理协议“tcp_toa”和“proxy_protocol”。 默认值为“close”。
        :type tcp_proxy: str
        :param tags: 资源标签列表。同一个终端节点服务最多可添加20个标签。
        :type tags: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        :param description: 描述字段，支持中英文字母、数字等字符，不支持“&lt;”或“&gt;”字符。  描述字段，支持中英文字母、数字等字符，不支持“&lt;”或“&gt;”字符。
        :type description: str
        :param ip_version: 指定终端节点服务的IP版本，仅专业型终端节点服务支持此参数 ● ipv4,  IPv4 ● ipv6,  IPv6
        :type ip_version: str
        :param snat_network_id: 接口型snat的地址段，ip_version为ipv6时必选。创建服务时使用的VPC内的任意一个网络ID。当服务类型为VIP、VM、ELBV2类型时使用
        :type snat_network_id: str
        """
        
        

        self._port_id = None
        self._service_name = None
        self._vpc_id = None
        self._approval_enabled = None
        self._service_type = None
        self._server_type = None
        self._ip = None
        self._ports = None
        self._tcp_proxy = None
        self._tags = None
        self._description = None
        self._ip_version = None
        self._snat_network_id = None
        self.discriminator = None

        self.port_id = port_id
        if service_name is not None:
            self.service_name = service_name
        self.vpc_id = vpc_id
        if approval_enabled is not None:
            self.approval_enabled = approval_enabled
        if service_type is not None:
            self.service_type = service_type
        self.server_type = server_type
        if ip is not None:
            self.ip = ip
        self.ports = ports
        if tcp_proxy is not None:
            self.tcp_proxy = tcp_proxy
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description
        if ip_version is not None:
            self.ip_version = ip_version
        if snat_network_id is not None:
            self.snat_network_id = snat_network_id

    @property
    def port_id(self):
        r"""Gets the port_id of this CreateEndpointServiceRequestBody.

        标识终端节点服务后端资源的ID， 格式为通用唯一识别码（Universally Unique Identifier，下文简称UUID）。 取值为： - LB类型：负载均衡器内网IP对应的端口ID。 详细内容请参考《弹性负载均衡API参考》中的“查询负载均衡详情”。 - VM类型：弹性云服务器IP地址对应的网卡ID。 详细内容请参考《弹性云服务器API参考》中的“查询云服务器网卡信息”， 详见响应消息中的“port_id”字段。 - VIP类型：虚拟IP所在虚拟机的网卡ID（VIP类型业务已不支持，该取值类型已废弃） 说明： - 创建终端节点服务时，VPC的子网网段不能与198.19.128.0/17重叠。 - VPC路由表中自定义路由的目的地址不能与198.19.128.0/17重叠。

        :return: The port_id of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this CreateEndpointServiceRequestBody.

        标识终端节点服务后端资源的ID， 格式为通用唯一识别码（Universally Unique Identifier，下文简称UUID）。 取值为： - LB类型：负载均衡器内网IP对应的端口ID。 详细内容请参考《弹性负载均衡API参考》中的“查询负载均衡详情”。 - VM类型：弹性云服务器IP地址对应的网卡ID。 详细内容请参考《弹性云服务器API参考》中的“查询云服务器网卡信息”， 详见响应消息中的“port_id”字段。 - VIP类型：虚拟IP所在虚拟机的网卡ID（VIP类型业务已不支持，该取值类型已废弃） 说明： - 创建终端节点服务时，VPC的子网网段不能与198.19.128.0/17重叠。 - VPC路由表中自定义路由的目的地址不能与198.19.128.0/17重叠。

        :param port_id: The port_id of this CreateEndpointServiceRequestBody.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def service_name(self):
        r"""Gets the service_name of this CreateEndpointServiceRequestBody.

        终端节点服务的名称，长度不大于16，允许传入大小写字母、数字、下划线、中划线。 - 传入为空，存入值为regionName+.+serviceId - 传入不为空并校验通过，存入值为regionName+.+serviceName+.+serviceId

        :return: The service_name of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this CreateEndpointServiceRequestBody.

        终端节点服务的名称，长度不大于16，允许传入大小写字母、数字、下划线、中划线。 - 传入为空，存入值为regionName+.+serviceId - 传入不为空并校验通过，存入值为regionName+.+serviceName+.+serviceId

        :param service_name: The service_name of this CreateEndpointServiceRequestBody.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateEndpointServiceRequestBody.

        终端节点服务对应后端资源所在的VPC的ID。

        :return: The vpc_id of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateEndpointServiceRequestBody.

        终端节点服务对应后端资源所在的VPC的ID。

        :param vpc_id: The vpc_id of this CreateEndpointServiceRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def approval_enabled(self):
        r"""Gets the approval_enabled of this CreateEndpointServiceRequestBody.

        是否需要审批。  - false：不需要审批，创建的终端节点连接直接为accepted状态。  - true：需要审批，创建的终端节点连接为pendingAcceptance状态， 需要终端节点服务所属用户审核后方可使用。 默认为true，需要审批。

        :return: The approval_enabled of this CreateEndpointServiceRequestBody.
        :rtype: bool
        """
        return self._approval_enabled

    @approval_enabled.setter
    def approval_enabled(self, approval_enabled):
        r"""Sets the approval_enabled of this CreateEndpointServiceRequestBody.

        是否需要审批。  - false：不需要审批，创建的终端节点连接直接为accepted状态。  - true：需要审批，创建的终端节点连接为pendingAcceptance状态， 需要终端节点服务所属用户审核后方可使用。 默认为true，需要审批。

        :param approval_enabled: The approval_enabled of this CreateEndpointServiceRequestBody.
        :type approval_enabled: bool
        """
        self._approval_enabled = approval_enabled

    @property
    def service_type(self):
        r"""Gets the service_type of this CreateEndpointServiceRequestBody.

        终端节点服务类型。 仅支持将用户私有服务创建为interface类型的终端节点服务。 终端节点服务类型包括“网关（gateway）型”和“接口（interface）型”：  - gateway：由运维人员配置。用户无需创建，可直接使用。  - interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建， 用户可直接使用。 您可以通过查询公共终端节点服务列表， 查看由运维人员配置的所有用户可见且可连接的终端节点服务， 并通过创建终端节点创建访问Gateway和Interface类型终端节点服务的终端节点。

        :return: The service_type of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this CreateEndpointServiceRequestBody.

        终端节点服务类型。 仅支持将用户私有服务创建为interface类型的终端节点服务。 终端节点服务类型包括“网关（gateway）型”和“接口（interface）型”：  - gateway：由运维人员配置。用户无需创建，可直接使用。  - interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建， 用户可直接使用。 您可以通过查询公共终端节点服务列表， 查看由运维人员配置的所有用户可见且可连接的终端节点服务， 并通过创建终端节点创建访问Gateway和Interface类型终端节点服务的终端节点。

        :param service_type: The service_type of this CreateEndpointServiceRequestBody.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def server_type(self):
        r"""Gets the server_type of this CreateEndpointServiceRequestBody.

        资源类型。  - VM：云服务器，适用于作为服务器使用。  - VIP：虚拟IP，适用于作为虚IP场景使用。（该字段已废弃，请优先使用LB类型）  - LB：负载均衡，适用于高访问量业务和对可靠性和容灾性要求较高的业务。

        :return: The server_type of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this CreateEndpointServiceRequestBody.

        资源类型。  - VM：云服务器，适用于作为服务器使用。  - VIP：虚拟IP，适用于作为虚IP场景使用。（该字段已废弃，请优先使用LB类型）  - LB：负载均衡，适用于高访问量业务和对可靠性和容灾性要求较高的业务。

        :param server_type: The server_type of this CreateEndpointServiceRequestBody.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def ip(self):
        r"""Gets the ip of this CreateEndpointServiceRequestBody.

        接口型VLAN场景服务端IPv4地址或域名

        :return: The ip of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this CreateEndpointServiceRequestBody.

        接口型VLAN场景服务端IPv4地址或域名

        :param ip: The ip of this CreateEndpointServiceRequestBody.
        :type ip: str
        """
        self._ip = ip

    @property
    def ports(self):
        r"""Gets the ports of this CreateEndpointServiceRequestBody.

        服务开放的端口映射列表，详细内容请参见表4-10。 同一个终端节点服务下，不允许重复的端口映射。若多个终端节点服务共用一个port_id， 则终端节点服务之间的所有端口映射的server_port和protocol的组合不能重复， 单次最多添加200个。

        :return: The ports of this CreateEndpointServiceRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        r"""Sets the ports of this CreateEndpointServiceRequestBody.

        服务开放的端口映射列表，详细内容请参见表4-10。 同一个终端节点服务下，不允许重复的端口映射。若多个终端节点服务共用一个port_id， 则终端节点服务之间的所有端口映射的server_port和protocol的组合不能重复， 单次最多添加200个。

        :param ports: The ports of this CreateEndpointServiceRequestBody.
        :type ports: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        """
        self._ports = ports

    @property
    def tcp_proxy(self):
        r"""Gets the tcp_proxy of this CreateEndpointServiceRequestBody.

        用于控制将哪些信息（如客户端的源IP、源端口、marker_id等）携带到服务端。 支持携带的客户端信息包括如下两种类型：  - TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明：仅当后端资源为OBS时，支持TCP TOA类型信息携带方式。  - Proxy Protocol：表示将客户端信息插入到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置才有效。 该参数的取值包括：  - close：表示关闭代理协议。  - toa_open：表示开启代理协议“tcp_toa”。  - proxy_open：表示开启代理协议“proxy_protocol”。  - open：表示同时开启代理协议“tcp_toa”和“proxy_protocol”。 默认值为“close”。

        :return: The tcp_proxy of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._tcp_proxy

    @tcp_proxy.setter
    def tcp_proxy(self, tcp_proxy):
        r"""Sets the tcp_proxy of this CreateEndpointServiceRequestBody.

        用于控制将哪些信息（如客户端的源IP、源端口、marker_id等）携带到服务端。 支持携带的客户端信息包括如下两种类型：  - TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明：仅当后端资源为OBS时，支持TCP TOA类型信息携带方式。  - Proxy Protocol：表示将客户端信息插入到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置才有效。 该参数的取值包括：  - close：表示关闭代理协议。  - toa_open：表示开启代理协议“tcp_toa”。  - proxy_open：表示开启代理协议“proxy_protocol”。  - open：表示同时开启代理协议“tcp_toa”和“proxy_protocol”。 默认值为“close”。

        :param tcp_proxy: The tcp_proxy of this CreateEndpointServiceRequestBody.
        :type tcp_proxy: str
        """
        self._tcp_proxy = tcp_proxy

    @property
    def tags(self):
        r"""Gets the tags of this CreateEndpointServiceRequestBody.

        资源标签列表。同一个终端节点服务最多可添加20个标签。

        :return: The tags of this CreateEndpointServiceRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateEndpointServiceRequestBody.

        资源标签列表。同一个终端节点服务最多可添加20个标签。

        :param tags: The tags of this CreateEndpointServiceRequestBody.
        :type tags: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        """
        self._tags = tags

    @property
    def description(self):
        r"""Gets the description of this CreateEndpointServiceRequestBody.

        描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。  描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。

        :return: The description of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateEndpointServiceRequestBody.

        描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。  描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。

        :param description: The description of this CreateEndpointServiceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def ip_version(self):
        r"""Gets the ip_version of this CreateEndpointServiceRequestBody.

        指定终端节点服务的IP版本，仅专业型终端节点服务支持此参数 ● ipv4,  IPv4 ● ipv6,  IPv6

        :return: The ip_version of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this CreateEndpointServiceRequestBody.

        指定终端节点服务的IP版本，仅专业型终端节点服务支持此参数 ● ipv4,  IPv4 ● ipv6,  IPv6

        :param ip_version: The ip_version of this CreateEndpointServiceRequestBody.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def snat_network_id(self):
        r"""Gets the snat_network_id of this CreateEndpointServiceRequestBody.

        接口型snat的地址段，ip_version为ipv6时必选。创建服务时使用的VPC内的任意一个网络ID。当服务类型为VIP、VM、ELBV2类型时使用

        :return: The snat_network_id of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._snat_network_id

    @snat_network_id.setter
    def snat_network_id(self, snat_network_id):
        r"""Sets the snat_network_id of this CreateEndpointServiceRequestBody.

        接口型snat的地址段，ip_version为ipv6时必选。创建服务时使用的VPC内的任意一个网络ID。当服务类型为VIP、VM、ELBV2类型时使用

        :param snat_network_id: The snat_network_id of this CreateEndpointServiceRequestBody.
        :type snat_network_id: str
        """
        self._snat_network_id = snat_network_id

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
        if not isinstance(other, CreateEndpointServiceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
