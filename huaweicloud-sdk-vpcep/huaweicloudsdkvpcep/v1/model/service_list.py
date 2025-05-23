# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'port_id': 'str',
        'service_name': 'str',
        'server_type': 'str',
        'vpc_id': 'str',
        'approval_enabled': 'bool',
        'status': 'str',
        'service_type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'project_id': 'str',
        'domain_id': 'str',
        'ports': 'list[PortList]',
        'ip': 'str',
        'tags': 'list[TagList]',
        'connection_count': 'int',
        'tcp_proxy': 'str',
        'error': 'list[Error]',
        'description': 'str',
        'supported_editions': 'list[str]',
        'public_border_group': 'str',
        'enable_policy': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'port_id': 'port_id',
        'service_name': 'service_name',
        'server_type': 'server_type',
        'vpc_id': 'vpc_id',
        'approval_enabled': 'approval_enabled',
        'status': 'status',
        'service_type': 'service_type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'ports': 'ports',
        'ip': 'ip',
        'tags': 'tags',
        'connection_count': 'connection_count',
        'tcp_proxy': 'tcp_proxy',
        'error': 'error',
        'description': 'description',
        'supported_editions': 'supported_editions',
        'public_border_group': 'public_border_group',
        'enable_policy': 'enable_policy'
    }

    def __init__(self, id=None, port_id=None, service_name=None, server_type=None, vpc_id=None, approval_enabled=None, status=None, service_type=None, created_at=None, updated_at=None, project_id=None, domain_id=None, ports=None, ip=None, tags=None, connection_count=None, tcp_proxy=None, error=None, description=None, supported_editions=None, public_border_group=None, enable_policy=None):
        r"""ServiceList

        The model defined in huaweicloud sdk

        :param id: 终端节点服务的ID，唯一标识。
        :type id: str
        :param port_id: 标识终端节点服务后端资源的ID， 格式为通用唯一识别码（Universally Unique Identifier，下文简称UUID）。取值为：  - LB类型：负载均衡器内网IP对应的端口ID。  - VM类型：弹性云服务器IP地址对应的网卡ID。  - VIP类型：虚拟资源所在物理服务器对应的网卡ID。（该字段已废弃，请优先使用LB类型）
        :type port_id: str
        :param service_name: 终端节点服务的名称。
        :type service_name: str
        :param server_type: 资源类型。  - VM：云服务器。  - VIP：虚拟IP。  - LB：增强负载均衡型。
        :type server_type: str
        :param vpc_id: 终端节点服务对应后端资源所在的VPC的ID。
        :type vpc_id: str
        :param approval_enabled: 是否需要审批。  - false：不需要审批，创建的终端节点连接直接为accepted状态。  - true：需要审批，创建的终端节点连接为pendingAcceptance状态， 需要终端节点服务所属用户审核后方可使用。
        :type approval_enabled: bool
        :param status: 终端节点服务的状态。  - creating：创建中  - available：可连接  - failed：失败  - deleting：删除中
        :type status: str
        :param service_type: 终端节点服务类型。 终端节点服务类型包括“网关（gateway）型”和“接口（interface）型”：  - gateway：由运维人员配置。用户无需创建，可直接使用。  - interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建，用户可直接使用。 您可以通过创建终端节点创建访问Gateway和Interface类型终端节点服务的终端节点。
        :type service_type: str
        :param created_at: 终端节点服务的创建时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ
        :type created_at: datetime
        :param updated_at: 终端节点服务的更新时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ
        :type updated_at: datetime
        :param project_id: 项目ID，获取方法请参见获取项目ID。
        :type project_id: str
        :param domain_id: Domain ID
        :type domain_id: str
        :param ports: 服务开放的端口映射列表 同一个终端节点服务下，不允许重复的端口映射。 若多个终端节点服务共用一个port_id， 则终端节点服务之间的所有端口映射的server_port和protocol的组合不能重复。
        :type ports: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        :param ip: 接口型VLAN场景服务端IPv4地址或域名
        :type ip: str
        :param tags: 资源标签列表
        :type tags: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        :param connection_count: 终端节点服务下连接的状态为“创建中”或“已接受”的终端节点的个数。
        :type connection_count: int
        :param tcp_proxy: 用于控制将哪些信息（如客户端的源IP、源端口、marker_id等）携带到服务端。 支持携带的客户端信息包括如下两种类型：  - TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明：仅当后端资源为OBS时，支持TCP TOA类型信息携带方式。  - Proxy Protocol：表示将客户端信息插入到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置才有效。 该参数的取值包括：  - close：表示关闭代理协议。  - toa_open：表示开启代理协议“tcp_toa”。  - proxy_open：表示开启代理协议“proxy_protocol”。  - open：表示同时开启代理协议“tcp_toa”和“proxy_protocol”。 默认值为“close”。
        :type tcp_proxy: str
        :param error: 提交任务异常时返回的异常信息
        :type error: list[:class:`huaweicloudsdkvpcep.v1.Error`]
        :param description: 描述字段，支持中英文字母、数字等字符，不支持“&lt;”或“&gt;”字符。
        :type description: str
        :param supported_editions: 终端节点服务支持的类型，取值范围为profession-专业型，basic-基础型
        :type supported_editions: list[str]
        :param public_border_group: 终端节点服务对应Pool的Public Border Group信息
        :type public_border_group: str
        :param enable_policy: 是否允许自定义终端节点策略。  - false：不支持设置终端节点策略  - true：支持设置终端节点策略 默认为false
        :type enable_policy: bool
        """
        
        

        self._id = None
        self._port_id = None
        self._service_name = None
        self._server_type = None
        self._vpc_id = None
        self._approval_enabled = None
        self._status = None
        self._service_type = None
        self._created_at = None
        self._updated_at = None
        self._project_id = None
        self._domain_id = None
        self._ports = None
        self._ip = None
        self._tags = None
        self._connection_count = None
        self._tcp_proxy = None
        self._error = None
        self._description = None
        self._supported_editions = None
        self._public_border_group = None
        self._enable_policy = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if port_id is not None:
            self.port_id = port_id
        if service_name is not None:
            self.service_name = service_name
        if server_type is not None:
            self.server_type = server_type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if approval_enabled is not None:
            self.approval_enabled = approval_enabled
        if status is not None:
            self.status = status
        if service_type is not None:
            self.service_type = service_type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if ports is not None:
            self.ports = ports
        if ip is not None:
            self.ip = ip
        if tags is not None:
            self.tags = tags
        if connection_count is not None:
            self.connection_count = connection_count
        if tcp_proxy is not None:
            self.tcp_proxy = tcp_proxy
        if error is not None:
            self.error = error
        if description is not None:
            self.description = description
        if supported_editions is not None:
            self.supported_editions = supported_editions
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if enable_policy is not None:
            self.enable_policy = enable_policy

    @property
    def id(self):
        r"""Gets the id of this ServiceList.

        终端节点服务的ID，唯一标识。

        :return: The id of this ServiceList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServiceList.

        终端节点服务的ID，唯一标识。

        :param id: The id of this ServiceList.
        :type id: str
        """
        self._id = id

    @property
    def port_id(self):
        r"""Gets the port_id of this ServiceList.

        标识终端节点服务后端资源的ID， 格式为通用唯一识别码（Universally Unique Identifier，下文简称UUID）。取值为：  - LB类型：负载均衡器内网IP对应的端口ID。  - VM类型：弹性云服务器IP地址对应的网卡ID。  - VIP类型：虚拟资源所在物理服务器对应的网卡ID。（该字段已废弃，请优先使用LB类型）

        :return: The port_id of this ServiceList.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this ServiceList.

        标识终端节点服务后端资源的ID， 格式为通用唯一识别码（Universally Unique Identifier，下文简称UUID）。取值为：  - LB类型：负载均衡器内网IP对应的端口ID。  - VM类型：弹性云服务器IP地址对应的网卡ID。  - VIP类型：虚拟资源所在物理服务器对应的网卡ID。（该字段已废弃，请优先使用LB类型）

        :param port_id: The port_id of this ServiceList.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def service_name(self):
        r"""Gets the service_name of this ServiceList.

        终端节点服务的名称。

        :return: The service_name of this ServiceList.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ServiceList.

        终端节点服务的名称。

        :param service_name: The service_name of this ServiceList.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def server_type(self):
        r"""Gets the server_type of this ServiceList.

        资源类型。  - VM：云服务器。  - VIP：虚拟IP。  - LB：增强负载均衡型。

        :return: The server_type of this ServiceList.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ServiceList.

        资源类型。  - VM：云服务器。  - VIP：虚拟IP。  - LB：增强负载均衡型。

        :param server_type: The server_type of this ServiceList.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ServiceList.

        终端节点服务对应后端资源所在的VPC的ID。

        :return: The vpc_id of this ServiceList.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ServiceList.

        终端节点服务对应后端资源所在的VPC的ID。

        :param vpc_id: The vpc_id of this ServiceList.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def approval_enabled(self):
        r"""Gets the approval_enabled of this ServiceList.

        是否需要审批。  - false：不需要审批，创建的终端节点连接直接为accepted状态。  - true：需要审批，创建的终端节点连接为pendingAcceptance状态， 需要终端节点服务所属用户审核后方可使用。

        :return: The approval_enabled of this ServiceList.
        :rtype: bool
        """
        return self._approval_enabled

    @approval_enabled.setter
    def approval_enabled(self, approval_enabled):
        r"""Sets the approval_enabled of this ServiceList.

        是否需要审批。  - false：不需要审批，创建的终端节点连接直接为accepted状态。  - true：需要审批，创建的终端节点连接为pendingAcceptance状态， 需要终端节点服务所属用户审核后方可使用。

        :param approval_enabled: The approval_enabled of this ServiceList.
        :type approval_enabled: bool
        """
        self._approval_enabled = approval_enabled

    @property
    def status(self):
        r"""Gets the status of this ServiceList.

        终端节点服务的状态。  - creating：创建中  - available：可连接  - failed：失败  - deleting：删除中

        :return: The status of this ServiceList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServiceList.

        终端节点服务的状态。  - creating：创建中  - available：可连接  - failed：失败  - deleting：删除中

        :param status: The status of this ServiceList.
        :type status: str
        """
        self._status = status

    @property
    def service_type(self):
        r"""Gets the service_type of this ServiceList.

        终端节点服务类型。 终端节点服务类型包括“网关（gateway）型”和“接口（interface）型”：  - gateway：由运维人员配置。用户无需创建，可直接使用。  - interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建，用户可直接使用。 您可以通过创建终端节点创建访问Gateway和Interface类型终端节点服务的终端节点。

        :return: The service_type of this ServiceList.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ServiceList.

        终端节点服务类型。 终端节点服务类型包括“网关（gateway）型”和“接口（interface）型”：  - gateway：由运维人员配置。用户无需创建，可直接使用。  - interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建，用户可直接使用。 您可以通过创建终端节点创建访问Gateway和Interface类型终端节点服务的终端节点。

        :param service_type: The service_type of this ServiceList.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def created_at(self):
        r"""Gets the created_at of this ServiceList.

        终端节点服务的创建时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :return: The created_at of this ServiceList.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ServiceList.

        终端节点服务的创建时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :param created_at: The created_at of this ServiceList.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ServiceList.

        终端节点服务的更新时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :return: The updated_at of this ServiceList.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ServiceList.

        终端节点服务的更新时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :param updated_at: The updated_at of this ServiceList.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        r"""Gets the project_id of this ServiceList.

        项目ID，获取方法请参见获取项目ID。

        :return: The project_id of this ServiceList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ServiceList.

        项目ID，获取方法请参见获取项目ID。

        :param project_id: The project_id of this ServiceList.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ServiceList.

        Domain ID

        :return: The domain_id of this ServiceList.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ServiceList.

        Domain ID

        :param domain_id: The domain_id of this ServiceList.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def ports(self):
        r"""Gets the ports of this ServiceList.

        服务开放的端口映射列表 同一个终端节点服务下，不允许重复的端口映射。 若多个终端节点服务共用一个port_id， 则终端节点服务之间的所有端口映射的server_port和protocol的组合不能重复。

        :return: The ports of this ServiceList.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        r"""Sets the ports of this ServiceList.

        服务开放的端口映射列表 同一个终端节点服务下，不允许重复的端口映射。 若多个终端节点服务共用一个port_id， 则终端节点服务之间的所有端口映射的server_port和protocol的组合不能重复。

        :param ports: The ports of this ServiceList.
        :type ports: list[:class:`huaweicloudsdkvpcep.v1.PortList`]
        """
        self._ports = ports

    @property
    def ip(self):
        r"""Gets the ip of this ServiceList.

        接口型VLAN场景服务端IPv4地址或域名

        :return: The ip of this ServiceList.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ServiceList.

        接口型VLAN场景服务端IPv4地址或域名

        :param ip: The ip of this ServiceList.
        :type ip: str
        """
        self._ip = ip

    @property
    def tags(self):
        r"""Gets the tags of this ServiceList.

        资源标签列表

        :return: The tags of this ServiceList.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ServiceList.

        资源标签列表

        :param tags: The tags of this ServiceList.
        :type tags: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        """
        self._tags = tags

    @property
    def connection_count(self):
        r"""Gets the connection_count of this ServiceList.

        终端节点服务下连接的状态为“创建中”或“已接受”的终端节点的个数。

        :return: The connection_count of this ServiceList.
        :rtype: int
        """
        return self._connection_count

    @connection_count.setter
    def connection_count(self, connection_count):
        r"""Sets the connection_count of this ServiceList.

        终端节点服务下连接的状态为“创建中”或“已接受”的终端节点的个数。

        :param connection_count: The connection_count of this ServiceList.
        :type connection_count: int
        """
        self._connection_count = connection_count

    @property
    def tcp_proxy(self):
        r"""Gets the tcp_proxy of this ServiceList.

        用于控制将哪些信息（如客户端的源IP、源端口、marker_id等）携带到服务端。 支持携带的客户端信息包括如下两种类型：  - TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明：仅当后端资源为OBS时，支持TCP TOA类型信息携带方式。  - Proxy Protocol：表示将客户端信息插入到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置才有效。 该参数的取值包括：  - close：表示关闭代理协议。  - toa_open：表示开启代理协议“tcp_toa”。  - proxy_open：表示开启代理协议“proxy_protocol”。  - open：表示同时开启代理协议“tcp_toa”和“proxy_protocol”。 默认值为“close”。

        :return: The tcp_proxy of this ServiceList.
        :rtype: str
        """
        return self._tcp_proxy

    @tcp_proxy.setter
    def tcp_proxy(self, tcp_proxy):
        r"""Sets the tcp_proxy of this ServiceList.

        用于控制将哪些信息（如客户端的源IP、源端口、marker_id等）携带到服务端。 支持携带的客户端信息包括如下两种类型：  - TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明：仅当后端资源为OBS时，支持TCP TOA类型信息携带方式。  - Proxy Protocol：表示将客户端信息插入到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置才有效。 该参数的取值包括：  - close：表示关闭代理协议。  - toa_open：表示开启代理协议“tcp_toa”。  - proxy_open：表示开启代理协议“proxy_protocol”。  - open：表示同时开启代理协议“tcp_toa”和“proxy_protocol”。 默认值为“close”。

        :param tcp_proxy: The tcp_proxy of this ServiceList.
        :type tcp_proxy: str
        """
        self._tcp_proxy = tcp_proxy

    @property
    def error(self):
        r"""Gets the error of this ServiceList.

        提交任务异常时返回的异常信息

        :return: The error of this ServiceList.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.Error`]
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ServiceList.

        提交任务异常时返回的异常信息

        :param error: The error of this ServiceList.
        :type error: list[:class:`huaweicloudsdkvpcep.v1.Error`]
        """
        self._error = error

    @property
    def description(self):
        r"""Gets the description of this ServiceList.

        描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。

        :return: The description of this ServiceList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ServiceList.

        描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。

        :param description: The description of this ServiceList.
        :type description: str
        """
        self._description = description

    @property
    def supported_editions(self):
        r"""Gets the supported_editions of this ServiceList.

        终端节点服务支持的类型，取值范围为profession-专业型，basic-基础型

        :return: The supported_editions of this ServiceList.
        :rtype: list[str]
        """
        return self._supported_editions

    @supported_editions.setter
    def supported_editions(self, supported_editions):
        r"""Sets the supported_editions of this ServiceList.

        终端节点服务支持的类型，取值范围为profession-专业型，basic-基础型

        :param supported_editions: The supported_editions of this ServiceList.
        :type supported_editions: list[str]
        """
        self._supported_editions = supported_editions

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this ServiceList.

        终端节点服务对应Pool的Public Border Group信息

        :return: The public_border_group of this ServiceList.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this ServiceList.

        终端节点服务对应Pool的Public Border Group信息

        :param public_border_group: The public_border_group of this ServiceList.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def enable_policy(self):
        r"""Gets the enable_policy of this ServiceList.

        是否允许自定义终端节点策略。  - false：不支持设置终端节点策略  - true：支持设置终端节点策略 默认为false

        :return: The enable_policy of this ServiceList.
        :rtype: bool
        """
        return self._enable_policy

    @enable_policy.setter
    def enable_policy(self, enable_policy):
        r"""Sets the enable_policy of this ServiceList.

        是否允许自定义终端节点策略。  - false：不支持设置终端节点策略  - true：支持设置终端节点策略 默认为false

        :param enable_policy: The enable_policy of this ServiceList.
        :type enable_policy: bool
        """
        self._enable_policy = enable_policy

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
        if not isinstance(other, ServiceList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
