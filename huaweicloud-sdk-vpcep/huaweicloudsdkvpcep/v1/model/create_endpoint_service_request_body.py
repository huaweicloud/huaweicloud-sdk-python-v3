# coding: utf-8

import re
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
        'vip_port_id': 'str',
        'service_name': 'str',
        'vpc_id': 'str',
        'approval_enabled': 'bool',
        'service_type': 'str',
        'server_type': 'str',
        'ports': 'list[PortList]',
        'tcp_proxy': 'str',
        'tags': 'list[TagList]',
        'description': 'str'
    }

    attribute_map = {
        'port_id': 'port_id',
        'vip_port_id': 'vip_port_id',
        'service_name': 'service_name',
        'vpc_id': 'vpc_id',
        'approval_enabled': 'approval_enabled',
        'service_type': 'service_type',
        'server_type': 'server_type',
        'ports': 'ports',
        'tcp_proxy': 'tcp_proxy',
        'tags': 'tags',
        'description': 'description'
    }

    def __init__(self, port_id=None, vip_port_id=None, service_name=None, vpc_id=None, approval_enabled=None, service_type=None, server_type=None, ports=None, tcp_proxy=None, tags=None, description=None):
        """CreateEndpointServiceRequestBody

        The model defined in huaweicloud sdk

        :param port_id: 标识终端节点服务后端资源的ID， 格式为通用唯一识别码（Universally Unique Identifier，下文简称UUID）。 取值为： ● LB类型：增强型负载均衡器内网IP对应的端口ID。 详细内容请参考《弹性负载均衡API参考》中的“查询负载均衡详情”， 详见响应消息中的“vip_port_id”字段。 ● VM类型：弹性云服务器IP地址对应的网卡ID。 详细内容请参考《弹性云服务器API参考》中的“查询云服务器网卡信息”， 详见响应消息中的“port_id”字段。 ● VIP类型：虚拟资源所在物理服务器对应的网卡ID。 说明 ● 创建终端节点服务时，VPC的子网网段不能与198.19.128.0/17重叠。 ● VPC路由表中自定义路由的目的地址不能与198.19.128.0/17重叠。
        :type port_id: str
        :param vip_port_id: 虚拟IP的网卡ID。
        :type vip_port_id: str
        :param service_name: 终端节点服务的名称，长度不大于16，允许传入大小写字母、数字、下划线、中划线。 ● 传入为空，存入值为regionName+.+serviceId ● 传入不为空并校验通过，存入值为regionName+.+serviceName+.+serviceId
        :type service_name: str
        :param vpc_id: 终端节点服务对应后端资源所在的VPC的ID。 详细内容请参考《虚拟私有云API参考》中的“查询VPC”，详见响应消息中的“id”字段。
        :type vpc_id: str
        :param approval_enabled: 是否需要审批。 ● false：不需要审批，创建的终端节点连接直接为accepted状态。 ● true：需要审批，创建的终端节点连接为pendingAcceptance状态， 需要终端节点服务所属用户审核后方可使用。 默认为true，需要审批。
        :type approval_enabled: bool
        :param service_type: 终端节点服务类型。 仅支持将用户私有服务创建为interface类型的终端节点服务。 终端节点服务类型包括“网关（gataway）型”和“接口（interface）型”： ● gataway：由运维人员配置。用户无需创建，可直接使用。 ● interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建， 用户可直接使用。 您可以通过查询公共终端节点服务列表, 查看由运维人员配置的所有用户可见且可连接的终端节点服务， 并通过创建终端节点创建访问Gateway和Interface类型终端节点服务的终端节点。
        :type service_type: str
        :param server_type: 资源类型。 ● VM：云服务器，适用于作为服务器使用。 ● VIP：虚拟IP，适用于作为虚拟资源的物理服务器使用。 ● LB：增强型负载均衡，适用于高访问量业务和对可靠性和容灾性要求较高的业务。
        :type server_type: str
        :param ports: 服务开放的端口映射列表，详细内容请参见表4-10。 同一个终端节点服务下，不允许重复的端口映射。若多个终端节点服务共用一个port_id， 则终端节点服务之间的所有端口映射的server_port和protocol的组合不能重复， 单次最多添加200个。
        :type ports: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        :param tcp_proxy: 用于控制是否将客户端的源IP、源端口、marker_id等信息携带到服务端。 信息携带支持两种方式： ● TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明 仅当后端资源为OBS时，支持TCP TOA类型信息携带方式。 ● Proxy Protocol：表示将客户端相关信息插入到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置才有效。 参数的取值包括： ● close：表示关闭代理协议。 ● toa_open：表示开启代理协议“tcp_toa”。 ● proxy_open：表示开启代理协议“proxy_protocol”。 ● open：表示同时开启代理协议“tcp_toa”和“proxy_protocol”。 默认值为“close”。
        :type tcp_proxy: str
        :param tags: 资源标签列表。同一个终端节点服务最多可添加10个标签。
        :type tags: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        :param description: 描述字段，支持中英文字母、数字等字符，不支持“&lt;”或“&gt;”字符。  描述字段，支持中英文字母、数字等字符，不支持“&lt;”或“&gt;”字符。
        :type description: str
        """
        
        

        self._port_id = None
        self._vip_port_id = None
        self._service_name = None
        self._vpc_id = None
        self._approval_enabled = None
        self._service_type = None
        self._server_type = None
        self._ports = None
        self._tcp_proxy = None
        self._tags = None
        self._description = None
        self.discriminator = None

        self.port_id = port_id
        if vip_port_id is not None:
            self.vip_port_id = vip_port_id
        if service_name is not None:
            self.service_name = service_name
        self.vpc_id = vpc_id
        if approval_enabled is not None:
            self.approval_enabled = approval_enabled
        if service_type is not None:
            self.service_type = service_type
        self.server_type = server_type
        self.ports = ports
        if tcp_proxy is not None:
            self.tcp_proxy = tcp_proxy
        if tags is not None:
            self.tags = tags
        if description is not None:
            self.description = description

    @property
    def port_id(self):
        """Gets the port_id of this CreateEndpointServiceRequestBody.

        标识终端节点服务后端资源的ID， 格式为通用唯一识别码（Universally Unique Identifier，下文简称UUID）。 取值为： ● LB类型：增强型负载均衡器内网IP对应的端口ID。 详细内容请参考《弹性负载均衡API参考》中的“查询负载均衡详情”， 详见响应消息中的“vip_port_id”字段。 ● VM类型：弹性云服务器IP地址对应的网卡ID。 详细内容请参考《弹性云服务器API参考》中的“查询云服务器网卡信息”， 详见响应消息中的“port_id”字段。 ● VIP类型：虚拟资源所在物理服务器对应的网卡ID。 说明 ● 创建终端节点服务时，VPC的子网网段不能与198.19.128.0/17重叠。 ● VPC路由表中自定义路由的目的地址不能与198.19.128.0/17重叠。

        :return: The port_id of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this CreateEndpointServiceRequestBody.

        标识终端节点服务后端资源的ID， 格式为通用唯一识别码（Universally Unique Identifier，下文简称UUID）。 取值为： ● LB类型：增强型负载均衡器内网IP对应的端口ID。 详细内容请参考《弹性负载均衡API参考》中的“查询负载均衡详情”， 详见响应消息中的“vip_port_id”字段。 ● VM类型：弹性云服务器IP地址对应的网卡ID。 详细内容请参考《弹性云服务器API参考》中的“查询云服务器网卡信息”， 详见响应消息中的“port_id”字段。 ● VIP类型：虚拟资源所在物理服务器对应的网卡ID。 说明 ● 创建终端节点服务时，VPC的子网网段不能与198.19.128.0/17重叠。 ● VPC路由表中自定义路由的目的地址不能与198.19.128.0/17重叠。

        :param port_id: The port_id of this CreateEndpointServiceRequestBody.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def vip_port_id(self):
        """Gets the vip_port_id of this CreateEndpointServiceRequestBody.

        虚拟IP的网卡ID。

        :return: The vip_port_id of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._vip_port_id

    @vip_port_id.setter
    def vip_port_id(self, vip_port_id):
        """Sets the vip_port_id of this CreateEndpointServiceRequestBody.

        虚拟IP的网卡ID。

        :param vip_port_id: The vip_port_id of this CreateEndpointServiceRequestBody.
        :type vip_port_id: str
        """
        self._vip_port_id = vip_port_id

    @property
    def service_name(self):
        """Gets the service_name of this CreateEndpointServiceRequestBody.

        终端节点服务的名称，长度不大于16，允许传入大小写字母、数字、下划线、中划线。 ● 传入为空，存入值为regionName+.+serviceId ● 传入不为空并校验通过，存入值为regionName+.+serviceName+.+serviceId

        :return: The service_name of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this CreateEndpointServiceRequestBody.

        终端节点服务的名称，长度不大于16，允许传入大小写字母、数字、下划线、中划线。 ● 传入为空，存入值为regionName+.+serviceId ● 传入不为空并校验通过，存入值为regionName+.+serviceName+.+serviceId

        :param service_name: The service_name of this CreateEndpointServiceRequestBody.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateEndpointServiceRequestBody.

        终端节点服务对应后端资源所在的VPC的ID。 详细内容请参考《虚拟私有云API参考》中的“查询VPC”，详见响应消息中的“id”字段。

        :return: The vpc_id of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateEndpointServiceRequestBody.

        终端节点服务对应后端资源所在的VPC的ID。 详细内容请参考《虚拟私有云API参考》中的“查询VPC”，详见响应消息中的“id”字段。

        :param vpc_id: The vpc_id of this CreateEndpointServiceRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def approval_enabled(self):
        """Gets the approval_enabled of this CreateEndpointServiceRequestBody.

        是否需要审批。 ● false：不需要审批，创建的终端节点连接直接为accepted状态。 ● true：需要审批，创建的终端节点连接为pendingAcceptance状态， 需要终端节点服务所属用户审核后方可使用。 默认为true，需要审批。

        :return: The approval_enabled of this CreateEndpointServiceRequestBody.
        :rtype: bool
        """
        return self._approval_enabled

    @approval_enabled.setter
    def approval_enabled(self, approval_enabled):
        """Sets the approval_enabled of this CreateEndpointServiceRequestBody.

        是否需要审批。 ● false：不需要审批，创建的终端节点连接直接为accepted状态。 ● true：需要审批，创建的终端节点连接为pendingAcceptance状态， 需要终端节点服务所属用户审核后方可使用。 默认为true，需要审批。

        :param approval_enabled: The approval_enabled of this CreateEndpointServiceRequestBody.
        :type approval_enabled: bool
        """
        self._approval_enabled = approval_enabled

    @property
    def service_type(self):
        """Gets the service_type of this CreateEndpointServiceRequestBody.

        终端节点服务类型。 仅支持将用户私有服务创建为interface类型的终端节点服务。 终端节点服务类型包括“网关（gataway）型”和“接口（interface）型”： ● gataway：由运维人员配置。用户无需创建，可直接使用。 ● interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建， 用户可直接使用。 您可以通过查询公共终端节点服务列表, 查看由运维人员配置的所有用户可见且可连接的终端节点服务， 并通过创建终端节点创建访问Gateway和Interface类型终端节点服务的终端节点。

        :return: The service_type of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this CreateEndpointServiceRequestBody.

        终端节点服务类型。 仅支持将用户私有服务创建为interface类型的终端节点服务。 终端节点服务类型包括“网关（gataway）型”和“接口（interface）型”： ● gataway：由运维人员配置。用户无需创建，可直接使用。 ● interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建， 用户可直接使用。 您可以通过查询公共终端节点服务列表, 查看由运维人员配置的所有用户可见且可连接的终端节点服务， 并通过创建终端节点创建访问Gateway和Interface类型终端节点服务的终端节点。

        :param service_type: The service_type of this CreateEndpointServiceRequestBody.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def server_type(self):
        """Gets the server_type of this CreateEndpointServiceRequestBody.

        资源类型。 ● VM：云服务器，适用于作为服务器使用。 ● VIP：虚拟IP，适用于作为虚拟资源的物理服务器使用。 ● LB：增强型负载均衡，适用于高访问量业务和对可靠性和容灾性要求较高的业务。

        :return: The server_type of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """Sets the server_type of this CreateEndpointServiceRequestBody.

        资源类型。 ● VM：云服务器，适用于作为服务器使用。 ● VIP：虚拟IP，适用于作为虚拟资源的物理服务器使用。 ● LB：增强型负载均衡，适用于高访问量业务和对可靠性和容灾性要求较高的业务。

        :param server_type: The server_type of this CreateEndpointServiceRequestBody.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def ports(self):
        """Gets the ports of this CreateEndpointServiceRequestBody.

        服务开放的端口映射列表，详细内容请参见表4-10。 同一个终端节点服务下，不允许重复的端口映射。若多个终端节点服务共用一个port_id， 则终端节点服务之间的所有端口映射的server_port和protocol的组合不能重复， 单次最多添加200个。

        :return: The ports of this CreateEndpointServiceRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this CreateEndpointServiceRequestBody.

        服务开放的端口映射列表，详细内容请参见表4-10。 同一个终端节点服务下，不允许重复的端口映射。若多个终端节点服务共用一个port_id， 则终端节点服务之间的所有端口映射的server_port和protocol的组合不能重复， 单次最多添加200个。

        :param ports: The ports of this CreateEndpointServiceRequestBody.
        :type ports: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        """
        self._ports = ports

    @property
    def tcp_proxy(self):
        """Gets the tcp_proxy of this CreateEndpointServiceRequestBody.

        用于控制是否将客户端的源IP、源端口、marker_id等信息携带到服务端。 信息携带支持两种方式： ● TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明 仅当后端资源为OBS时，支持TCP TOA类型信息携带方式。 ● Proxy Protocol：表示将客户端相关信息插入到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置才有效。 参数的取值包括： ● close：表示关闭代理协议。 ● toa_open：表示开启代理协议“tcp_toa”。 ● proxy_open：表示开启代理协议“proxy_protocol”。 ● open：表示同时开启代理协议“tcp_toa”和“proxy_protocol”。 默认值为“close”。

        :return: The tcp_proxy of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._tcp_proxy

    @tcp_proxy.setter
    def tcp_proxy(self, tcp_proxy):
        """Sets the tcp_proxy of this CreateEndpointServiceRequestBody.

        用于控制是否将客户端的源IP、源端口、marker_id等信息携带到服务端。 信息携带支持两种方式： ● TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明 仅当后端资源为OBS时，支持TCP TOA类型信息携带方式。 ● Proxy Protocol：表示将客户端相关信息插入到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置才有效。 参数的取值包括： ● close：表示关闭代理协议。 ● toa_open：表示开启代理协议“tcp_toa”。 ● proxy_open：表示开启代理协议“proxy_protocol”。 ● open：表示同时开启代理协议“tcp_toa”和“proxy_protocol”。 默认值为“close”。

        :param tcp_proxy: The tcp_proxy of this CreateEndpointServiceRequestBody.
        :type tcp_proxy: str
        """
        self._tcp_proxy = tcp_proxy

    @property
    def tags(self):
        """Gets the tags of this CreateEndpointServiceRequestBody.

        资源标签列表。同一个终端节点服务最多可添加10个标签。

        :return: The tags of this CreateEndpointServiceRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateEndpointServiceRequestBody.

        资源标签列表。同一个终端节点服务最多可添加10个标签。

        :param tags: The tags of this CreateEndpointServiceRequestBody.
        :type tags: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        """
        self._tags = tags

    @property
    def description(self):
        """Gets the description of this CreateEndpointServiceRequestBody.

        描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。  描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。

        :return: The description of this CreateEndpointServiceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEndpointServiceRequestBody.

        描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。  描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。

        :param description: The description of this CreateEndpointServiceRequestBody.
        :type description: str
        """
        self._description = description

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
