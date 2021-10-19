# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointServiceResponse(SdkResponse):


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
        'vip_port_id': 'str',
        'service_name': 'str',
        'service_type': 'str',
        'server_type': 'str',
        'vpc_id': 'str',
        'approval_enabled': 'bool',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'project_id': 'str',
        'cidr_type': 'str',
        'ports': 'list[PortList]',
        'tcp_proxy': 'str',
        'tags': 'list[TagList]'
    }

    attribute_map = {
        'id': 'id',
        'port_id': 'port_id',
        'vip_port_id': 'vip_port_id',
        'service_name': 'service_name',
        'service_type': 'service_type',
        'server_type': 'server_type',
        'vpc_id': 'vpc_id',
        'approval_enabled': 'approval_enabled',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'project_id': 'project_id',
        'cidr_type': 'cidr_type',
        'ports': 'ports',
        'tcp_proxy': 'tcp_proxy',
        'tags': 'tags'
    }

    def __init__(self, id=None, port_id=None, vip_port_id=None, service_name=None, service_type=None, server_type=None, vpc_id=None, approval_enabled=None, status=None, created_at=None, updated_at=None, project_id=None, cidr_type=None, ports=None, tcp_proxy=None, tags=None):
        """CreateEndpointServiceResponse - a model defined in huaweicloud sdk"""
        
        super(CreateEndpointServiceResponse, self).__init__()

        self._id = None
        self._port_id = None
        self._vip_port_id = None
        self._service_name = None
        self._service_type = None
        self._server_type = None
        self._vpc_id = None
        self._approval_enabled = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._project_id = None
        self._cidr_type = None
        self._ports = None
        self._tcp_proxy = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if port_id is not None:
            self.port_id = port_id
        if vip_port_id is not None:
            self.vip_port_id = vip_port_id
        if service_name is not None:
            self.service_name = service_name
        if service_type is not None:
            self.service_type = service_type
        if server_type is not None:
            self.server_type = server_type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if approval_enabled is not None:
            self.approval_enabled = approval_enabled
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if project_id is not None:
            self.project_id = project_id
        if cidr_type is not None:
            self.cidr_type = cidr_type
        if ports is not None:
            self.ports = ports
        if tcp_proxy is not None:
            self.tcp_proxy = tcp_proxy
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this CreateEndpointServiceResponse.

        终端节点服务的ID，唯一标识。

        :return: The id of this CreateEndpointServiceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateEndpointServiceResponse.

        终端节点服务的ID，唯一标识。

        :param id: The id of this CreateEndpointServiceResponse.
        :type: str
        """
        self._id = id

    @property
    def port_id(self):
        """Gets the port_id of this CreateEndpointServiceResponse.

        标识终端节点服务后端资源的ID，格式为通用 唯一识别码（Universally Unique Identifier， 下文简称UUID）。取值为： ● LB类型：增强型负载均衡器内网IP对应的端 口ID。 ● VM类型：弹性云服务器IP地址对应的网卡 ID。 ● VIP类型：虚拟资源所在物理服务器对应的网 卡ID。

        :return: The port_id of this CreateEndpointServiceResponse.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this CreateEndpointServiceResponse.

        标识终端节点服务后端资源的ID，格式为通用 唯一识别码（Universally Unique Identifier， 下文简称UUID）。取值为： ● LB类型：增强型负载均衡器内网IP对应的端 口ID。 ● VM类型：弹性云服务器IP地址对应的网卡 ID。 ● VIP类型：虚拟资源所在物理服务器对应的网 卡ID。

        :param port_id: The port_id of this CreateEndpointServiceResponse.
        :type: str
        """
        self._port_id = port_id

    @property
    def vip_port_id(self):
        """Gets the vip_port_id of this CreateEndpointServiceResponse.

        虚拟IP的网卡ID。 仅当“port_id”为“VIP类型”时，返回该参 数。

        :return: The vip_port_id of this CreateEndpointServiceResponse.
        :rtype: str
        """
        return self._vip_port_id

    @vip_port_id.setter
    def vip_port_id(self, vip_port_id):
        """Sets the vip_port_id of this CreateEndpointServiceResponse.

        虚拟IP的网卡ID。 仅当“port_id”为“VIP类型”时，返回该参 数。

        :param vip_port_id: The vip_port_id of this CreateEndpointServiceResponse.
        :type: str
        """
        self._vip_port_id = vip_port_id

    @property
    def service_name(self):
        """Gets the service_name of this CreateEndpointServiceResponse.

        终端节点服务的名称。

        :return: The service_name of this CreateEndpointServiceResponse.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this CreateEndpointServiceResponse.

        终端节点服务的名称。

        :param service_name: The service_name of this CreateEndpointServiceResponse.
        :type: str
        """
        self._service_name = service_name

    @property
    def service_type(self):
        """Gets the service_type of this CreateEndpointServiceResponse.

        终端节点服务类型。 终端节点服务类型包括“网关（gataway）型” 和“接口（interface）型”： ● gataway：由运维人员配置。用户无需创 建，可直接使用。 ● interface：包括运维人员配置的云服务和用 户自己创建的私有服务。其中，运维人员配 置的云服务无需创建，用户可直接使用。 您可以通过创建终端节点创建访问Gateway和 Interface类型终端节点服务的终端节点。

        :return: The service_type of this CreateEndpointServiceResponse.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this CreateEndpointServiceResponse.

        终端节点服务类型。 终端节点服务类型包括“网关（gataway）型” 和“接口（interface）型”： ● gataway：由运维人员配置。用户无需创 建，可直接使用。 ● interface：包括运维人员配置的云服务和用 户自己创建的私有服务。其中，运维人员配 置的云服务无需创建，用户可直接使用。 您可以通过创建终端节点创建访问Gateway和 Interface类型终端节点服务的终端节点。

        :param service_type: The service_type of this CreateEndpointServiceResponse.
        :type: str
        """
        self._service_type = service_type

    @property
    def server_type(self):
        """Gets the server_type of this CreateEndpointServiceResponse.

        资源类型。 ● VM：云服务器。 ● VIP：虚拟IP。 ● LB：增强负载均衡型。

        :return: The server_type of this CreateEndpointServiceResponse.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """Sets the server_type of this CreateEndpointServiceResponse.

        资源类型。 ● VM：云服务器。 ● VIP：虚拟IP。 ● LB：增强负载均衡型。

        :param server_type: The server_type of this CreateEndpointServiceResponse.
        :type: str
        """
        self._server_type = server_type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateEndpointServiceResponse.

        终端节点服务对应后端资源所在的VPC的ID。

        :return: The vpc_id of this CreateEndpointServiceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateEndpointServiceResponse.

        终端节点服务对应后端资源所在的VPC的ID。

        :param vpc_id: The vpc_id of this CreateEndpointServiceResponse.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def approval_enabled(self):
        """Gets the approval_enabled of this CreateEndpointServiceResponse.

        是否需要审批。 ● false：不需要审批，创建的终端节点连接直 接为accepted状态。 ● true：需要审批，创建的终端节点连接为 pendingAcceptance状态，需要终端节点服 务所属用户审核后方可使用。

        :return: The approval_enabled of this CreateEndpointServiceResponse.
        :rtype: bool
        """
        return self._approval_enabled

    @approval_enabled.setter
    def approval_enabled(self, approval_enabled):
        """Sets the approval_enabled of this CreateEndpointServiceResponse.

        是否需要审批。 ● false：不需要审批，创建的终端节点连接直 接为accepted状态。 ● true：需要审批，创建的终端节点连接为 pendingAcceptance状态，需要终端节点服 务所属用户审核后方可使用。

        :param approval_enabled: The approval_enabled of this CreateEndpointServiceResponse.
        :type: bool
        """
        self._approval_enabled = approval_enabled

    @property
    def status(self):
        """Gets the status of this CreateEndpointServiceResponse.

        终端节点服务的状态。 ● creating：创建中 ● available：可连接 ● failed：失败

        :return: The status of this CreateEndpointServiceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateEndpointServiceResponse.

        终端节点服务的状态。 ● creating：创建中 ● available：可连接 ● failed：失败

        :param status: The status of this CreateEndpointServiceResponse.
        :type: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this CreateEndpointServiceResponse.

        终端节点服务的创建时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH: MM:SSZ

        :return: The created_at of this CreateEndpointServiceResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateEndpointServiceResponse.

        终端节点服务的创建时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH: MM:SSZ

        :param created_at: The created_at of this CreateEndpointServiceResponse.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateEndpointServiceResponse.

        终端节点服务的更新时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH: MM:SSZ

        :return: The updated_at of this CreateEndpointServiceResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateEndpointServiceResponse.

        终端节点服务的更新时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH: MM:SSZ

        :param updated_at: The updated_at of this CreateEndpointServiceResponse.
        :type: datetime
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        """Gets the project_id of this CreateEndpointServiceResponse.

        项目ID

        :return: The project_id of this CreateEndpointServiceResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateEndpointServiceResponse.

        项目ID

        :param project_id: The project_id of this CreateEndpointServiceResponse.
        :type: str
        """
        self._project_id = project_id

    @property
    def cidr_type(self):
        """Gets the cidr_type of this CreateEndpointServiceResponse.

        网段类型。 ● public：公网网段 ● internal：内网网段 默认值为internal。

        :return: The cidr_type of this CreateEndpointServiceResponse.
        :rtype: str
        """
        return self._cidr_type

    @cidr_type.setter
    def cidr_type(self, cidr_type):
        """Sets the cidr_type of this CreateEndpointServiceResponse.

        网段类型。 ● public：公网网段 ● internal：内网网段 默认值为internal。

        :param cidr_type: The cidr_type of this CreateEndpointServiceResponse.
        :type: str
        """
        self._cidr_type = cidr_type

    @property
    def ports(self):
        """Gets the ports of this CreateEndpointServiceResponse.

        服务开放的端口映射列表，详细内容请参见表 4-13 同一个终端节点服务下，不允许重复的端口映 射。若多个终端节点服务共用一个port_id，则 终端节点服务之间的所有端口映射的 server_port和protocol的组合不能重复。

        :return: The ports of this CreateEndpointServiceResponse.
        :rtype: list[PortList]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this CreateEndpointServiceResponse.

        服务开放的端口映射列表，详细内容请参见表 4-13 同一个终端节点服务下，不允许重复的端口映 射。若多个终端节点服务共用一个port_id，则 终端节点服务之间的所有端口映射的 server_port和protocol的组合不能重复。

        :param ports: The ports of this CreateEndpointServiceResponse.
        :type: list[PortList]
        """
        self._ports = ports

    @property
    def tcp_proxy(self):
        """Gets the tcp_proxy of this CreateEndpointServiceResponse.

        用于控制是否将客户端的源IP、源端口、 marker_id等信息携带到服务端。信息携带支持 两种方式： ● TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明 仅当后端资源为OBS时，支持TCP TOA类型信息 携带方式。 ● Proxy Protocol：表示将客户端相关信息插入 到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置 才有效。 参数的取值包括： ● close：表示关闭代理协议。 ● toa_open：表示开启代理协议“tcp_toa”。 ● proxy_open：表示开启代理协议 “proxy_protocol”。 ● open：表示同时开启代理协议“tcp_toa” 和“proxy_protocol”。 默认值为“close”。

        :return: The tcp_proxy of this CreateEndpointServiceResponse.
        :rtype: str
        """
        return self._tcp_proxy

    @tcp_proxy.setter
    def tcp_proxy(self, tcp_proxy):
        """Sets the tcp_proxy of this CreateEndpointServiceResponse.

        用于控制是否将客户端的源IP、源端口、 marker_id等信息携带到服务端。信息携带支持 两种方式： ● TCP TOA：表示将客户端信息插入到tcp option字段中携带至服务端。 说明 仅当后端资源为OBS时，支持TCP TOA类型信息 携带方式。 ● Proxy Protocol：表示将客户端相关信息插入 到tcp payload字段中携带至服务端。 仅当服务端支持解析上述字段时，该参数设置 才有效。 参数的取值包括： ● close：表示关闭代理协议。 ● toa_open：表示开启代理协议“tcp_toa”。 ● proxy_open：表示开启代理协议 “proxy_protocol”。 ● open：表示同时开启代理协议“tcp_toa” 和“proxy_protocol”。 默认值为“close”。

        :param tcp_proxy: The tcp_proxy of this CreateEndpointServiceResponse.
        :type: str
        """
        self._tcp_proxy = tcp_proxy

    @property
    def tags(self):
        """Gets the tags of this CreateEndpointServiceResponse.

        资源标签列表

        :return: The tags of this CreateEndpointServiceResponse.
        :rtype: list[TagList]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateEndpointServiceResponse.

        资源标签列表

        :param tags: The tags of this CreateEndpointServiceResponse.
        :type: list[TagList]
        """
        self._tags = tags

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
        if not isinstance(other, CreateEndpointServiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
