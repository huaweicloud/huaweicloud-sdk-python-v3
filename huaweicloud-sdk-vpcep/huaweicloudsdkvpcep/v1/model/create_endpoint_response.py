# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointResponse(SdkResponse):

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
        'service_type': 'str',
        'status': 'str',
        'ip': 'str',
        'active_status': 'list[str]',
        'endpoint_service_name': 'str',
        'marker_id': 'int',
        'endpoint_service_id': 'str',
        'enable_dns': 'bool',
        'dns_names': 'list[str]',
        'subnet_id': 'str',
        'vpc_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'project_id': 'str',
        'tags': 'list[TagList]',
        'whitelist': 'list[str]',
        'enable_whitelist': 'bool',
        'routetables': 'list[str]',
        'specification_name': 'str',
        'description': 'str',
        'policy_statement': 'list[str]',
        'enable_status': 'str',
        'endpoint_pool_id': 'str',
        'public_border_group': 'str'
    }

    attribute_map = {
        'id': 'id',
        'service_type': 'service_type',
        'status': 'status',
        'ip': 'ip',
        'active_status': 'active_status',
        'endpoint_service_name': 'endpoint_service_name',
        'marker_id': 'marker_id',
        'endpoint_service_id': 'endpoint_service_id',
        'enable_dns': 'enable_dns',
        'dns_names': 'dns_names',
        'subnet_id': 'subnet_id',
        'vpc_id': 'vpc_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'project_id': 'project_id',
        'tags': 'tags',
        'whitelist': 'whitelist',
        'enable_whitelist': 'enable_whitelist',
        'routetables': 'routetables',
        'specification_name': 'specification_name',
        'description': 'description',
        'policy_statement': 'policy_statement',
        'enable_status': 'enable_status',
        'endpoint_pool_id': 'endpoint_pool_id',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, id=None, service_type=None, status=None, ip=None, active_status=None, endpoint_service_name=None, marker_id=None, endpoint_service_id=None, enable_dns=None, dns_names=None, subnet_id=None, vpc_id=None, created_at=None, updated_at=None, project_id=None, tags=None, whitelist=None, enable_whitelist=None, routetables=None, specification_name=None, description=None, policy_statement=None, enable_status=None, endpoint_pool_id=None, public_border_group=None):
        """CreateEndpointResponse

        The model defined in huaweicloud sdk

        :param id: 终端节点的ID，唯一标识。
        :type id: str
        :param service_type: 终端节点连接的终端节点服务类型。 ● gataway：由运维人员配置。用户无需创建，可直接使用。 ● interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建，用户可直接使用。 您可以通过查询公共终端节点服务列表， 查看由运维人员配置的所有用户可见且可连接的终端节点服务， 并通过创建终端节点服务创建Interface类型的终端节点服务。
        :type service_type: str
        :param status: 终端节点的状态。 ● pendingAcceptance：待接受 ● creating：创建中 ● accepted：已接受 ● rejected：已拒绝 ● failed：失败 ● deleting：删除中
        :type status: str
        :param ip: 终端节点ip
        :type ip: str
        :param active_status: 帐号状态。 ● frozen：冻结 ● active：解冻
        :type active_status: list[str]
        :param endpoint_service_name: 终端节点服务的名称。
        :type endpoint_service_name: str
        :param marker_id: 终端节点的报文标识。
        :type marker_id: int
        :param endpoint_service_id: 终端节点服务的ID。
        :type endpoint_service_id: str
        :param enable_dns: 是否创建域名。 ● true：创建域名 ● false：不创建域名 说明 当创建连接gateway类型终端节点服务的终端节点时， “enable_dns”设置为true或者false，均不创建域名。
        :type enable_dns: bool
        :param dns_names: 访问所连接的终端节点服务的域名。 当“enable_dns”为true时，该参数可见。
        :type dns_names: list[str]
        :param subnet_id: vpc_id对应VPC下已创建的网络（network）的ID，UUID格式。
        :type subnet_id: str
        :param vpc_id: 终端节点所在的VPC的ID。
        :type vpc_id: str
        :param created_at: 终端节点的创建时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ
        :type created_at: str
        :param updated_at: 终端节点的更新时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ
        :type updated_at: str
        :param project_id: 项目ID，获取方法请参见获取项目ID。
        :type project_id: str
        :param tags: 标签列表，没有标签默认为空数组。
        :type tags: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        :param whitelist: 控制访问终端节点的白名单。 若未创建，则返回空列表。 创建连接Interface类型终端节点服务的终端节点时，显示此参数。
        :type whitelist: list[str]
        :param enable_whitelist: 是否开启网络ACL隔离。 ● true：开启网络ACL隔离 ● false：不开启网络ACL隔离 若未指定，则返回false。 创建连接Interface类型终端节点服务的终端节点时，显示此参数。
        :type enable_whitelist: bool
        :param routetables: 路由表ID列表。 若未指定，返回默认VPC下路由表ID。 创建连接Gateway类型终端节点服务的终端节点时，显示此参数。
        :type routetables: list[str]
        :param specification_name: 规格名称
        :type specification_name: str
        :param description: 描述
        :type description: str
        :param policy_statement: 只涉及开启双端固定的网关型终端节点，响应体展示此字段
        :type policy_statement: list[str]
        :param enable_status: 终端节点是否已停用，取值【enable/disable】
        :type enable_status: str
        :param endpoint_pool_id: 待废弃，实例相关联的集群ID
        :type endpoint_pool_id: str
        :param public_border_group: 终端节点对应Pool的Public Border Group信息
        :type public_border_group: str
        """
        
        super(CreateEndpointResponse, self).__init__()

        self._id = None
        self._service_type = None
        self._status = None
        self._ip = None
        self._active_status = None
        self._endpoint_service_name = None
        self._marker_id = None
        self._endpoint_service_id = None
        self._enable_dns = None
        self._dns_names = None
        self._subnet_id = None
        self._vpc_id = None
        self._created_at = None
        self._updated_at = None
        self._project_id = None
        self._tags = None
        self._whitelist = None
        self._enable_whitelist = None
        self._routetables = None
        self._specification_name = None
        self._description = None
        self._policy_statement = None
        self._enable_status = None
        self._endpoint_pool_id = None
        self._public_border_group = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if service_type is not None:
            self.service_type = service_type
        if status is not None:
            self.status = status
        if ip is not None:
            self.ip = ip
        if active_status is not None:
            self.active_status = active_status
        if endpoint_service_name is not None:
            self.endpoint_service_name = endpoint_service_name
        if marker_id is not None:
            self.marker_id = marker_id
        if endpoint_service_id is not None:
            self.endpoint_service_id = endpoint_service_id
        if enable_dns is not None:
            self.enable_dns = enable_dns
        if dns_names is not None:
            self.dns_names = dns_names
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if project_id is not None:
            self.project_id = project_id
        if tags is not None:
            self.tags = tags
        if whitelist is not None:
            self.whitelist = whitelist
        if enable_whitelist is not None:
            self.enable_whitelist = enable_whitelist
        if routetables is not None:
            self.routetables = routetables
        if specification_name is not None:
            self.specification_name = specification_name
        if description is not None:
            self.description = description
        if policy_statement is not None:
            self.policy_statement = policy_statement
        if enable_status is not None:
            self.enable_status = enable_status
        if endpoint_pool_id is not None:
            self.endpoint_pool_id = endpoint_pool_id
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def id(self):
        """Gets the id of this CreateEndpointResponse.

        终端节点的ID，唯一标识。

        :return: The id of this CreateEndpointResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateEndpointResponse.

        终端节点的ID，唯一标识。

        :param id: The id of this CreateEndpointResponse.
        :type id: str
        """
        self._id = id

    @property
    def service_type(self):
        """Gets the service_type of this CreateEndpointResponse.

        终端节点连接的终端节点服务类型。 ● gataway：由运维人员配置。用户无需创建，可直接使用。 ● interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建，用户可直接使用。 您可以通过查询公共终端节点服务列表， 查看由运维人员配置的所有用户可见且可连接的终端节点服务， 并通过创建终端节点服务创建Interface类型的终端节点服务。

        :return: The service_type of this CreateEndpointResponse.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this CreateEndpointResponse.

        终端节点连接的终端节点服务类型。 ● gataway：由运维人员配置。用户无需创建，可直接使用。 ● interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建，用户可直接使用。 您可以通过查询公共终端节点服务列表， 查看由运维人员配置的所有用户可见且可连接的终端节点服务， 并通过创建终端节点服务创建Interface类型的终端节点服务。

        :param service_type: The service_type of this CreateEndpointResponse.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def status(self):
        """Gets the status of this CreateEndpointResponse.

        终端节点的状态。 ● pendingAcceptance：待接受 ● creating：创建中 ● accepted：已接受 ● rejected：已拒绝 ● failed：失败 ● deleting：删除中

        :return: The status of this CreateEndpointResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateEndpointResponse.

        终端节点的状态。 ● pendingAcceptance：待接受 ● creating：创建中 ● accepted：已接受 ● rejected：已拒绝 ● failed：失败 ● deleting：删除中

        :param status: The status of this CreateEndpointResponse.
        :type status: str
        """
        self._status = status

    @property
    def ip(self):
        """Gets the ip of this CreateEndpointResponse.

        终端节点ip

        :return: The ip of this CreateEndpointResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this CreateEndpointResponse.

        终端节点ip

        :param ip: The ip of this CreateEndpointResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def active_status(self):
        """Gets the active_status of this CreateEndpointResponse.

        帐号状态。 ● frozen：冻结 ● active：解冻

        :return: The active_status of this CreateEndpointResponse.
        :rtype: list[str]
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        """Sets the active_status of this CreateEndpointResponse.

        帐号状态。 ● frozen：冻结 ● active：解冻

        :param active_status: The active_status of this CreateEndpointResponse.
        :type active_status: list[str]
        """
        self._active_status = active_status

    @property
    def endpoint_service_name(self):
        """Gets the endpoint_service_name of this CreateEndpointResponse.

        终端节点服务的名称。

        :return: The endpoint_service_name of this CreateEndpointResponse.
        :rtype: str
        """
        return self._endpoint_service_name

    @endpoint_service_name.setter
    def endpoint_service_name(self, endpoint_service_name):
        """Sets the endpoint_service_name of this CreateEndpointResponse.

        终端节点服务的名称。

        :param endpoint_service_name: The endpoint_service_name of this CreateEndpointResponse.
        :type endpoint_service_name: str
        """
        self._endpoint_service_name = endpoint_service_name

    @property
    def marker_id(self):
        """Gets the marker_id of this CreateEndpointResponse.

        终端节点的报文标识。

        :return: The marker_id of this CreateEndpointResponse.
        :rtype: int
        """
        return self._marker_id

    @marker_id.setter
    def marker_id(self, marker_id):
        """Sets the marker_id of this CreateEndpointResponse.

        终端节点的报文标识。

        :param marker_id: The marker_id of this CreateEndpointResponse.
        :type marker_id: int
        """
        self._marker_id = marker_id

    @property
    def endpoint_service_id(self):
        """Gets the endpoint_service_id of this CreateEndpointResponse.

        终端节点服务的ID。

        :return: The endpoint_service_id of this CreateEndpointResponse.
        :rtype: str
        """
        return self._endpoint_service_id

    @endpoint_service_id.setter
    def endpoint_service_id(self, endpoint_service_id):
        """Sets the endpoint_service_id of this CreateEndpointResponse.

        终端节点服务的ID。

        :param endpoint_service_id: The endpoint_service_id of this CreateEndpointResponse.
        :type endpoint_service_id: str
        """
        self._endpoint_service_id = endpoint_service_id

    @property
    def enable_dns(self):
        """Gets the enable_dns of this CreateEndpointResponse.

        是否创建域名。 ● true：创建域名 ● false：不创建域名 说明 当创建连接gateway类型终端节点服务的终端节点时， “enable_dns”设置为true或者false，均不创建域名。

        :return: The enable_dns of this CreateEndpointResponse.
        :rtype: bool
        """
        return self._enable_dns

    @enable_dns.setter
    def enable_dns(self, enable_dns):
        """Sets the enable_dns of this CreateEndpointResponse.

        是否创建域名。 ● true：创建域名 ● false：不创建域名 说明 当创建连接gateway类型终端节点服务的终端节点时， “enable_dns”设置为true或者false，均不创建域名。

        :param enable_dns: The enable_dns of this CreateEndpointResponse.
        :type enable_dns: bool
        """
        self._enable_dns = enable_dns

    @property
    def dns_names(self):
        """Gets the dns_names of this CreateEndpointResponse.

        访问所连接的终端节点服务的域名。 当“enable_dns”为true时，该参数可见。

        :return: The dns_names of this CreateEndpointResponse.
        :rtype: list[str]
        """
        return self._dns_names

    @dns_names.setter
    def dns_names(self, dns_names):
        """Sets the dns_names of this CreateEndpointResponse.

        访问所连接的终端节点服务的域名。 当“enable_dns”为true时，该参数可见。

        :param dns_names: The dns_names of this CreateEndpointResponse.
        :type dns_names: list[str]
        """
        self._dns_names = dns_names

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateEndpointResponse.

        vpc_id对应VPC下已创建的网络（network）的ID，UUID格式。

        :return: The subnet_id of this CreateEndpointResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateEndpointResponse.

        vpc_id对应VPC下已创建的网络（network）的ID，UUID格式。

        :param subnet_id: The subnet_id of this CreateEndpointResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateEndpointResponse.

        终端节点所在的VPC的ID。

        :return: The vpc_id of this CreateEndpointResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateEndpointResponse.

        终端节点所在的VPC的ID。

        :param vpc_id: The vpc_id of this CreateEndpointResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def created_at(self):
        """Gets the created_at of this CreateEndpointResponse.

        终端节点的创建时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :return: The created_at of this CreateEndpointResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateEndpointResponse.

        终端节点的创建时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :param created_at: The created_at of this CreateEndpointResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateEndpointResponse.

        终端节点的更新时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :return: The updated_at of this CreateEndpointResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateEndpointResponse.

        终端节点的更新时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :param updated_at: The updated_at of this CreateEndpointResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        """Gets the project_id of this CreateEndpointResponse.

        项目ID，获取方法请参见获取项目ID。

        :return: The project_id of this CreateEndpointResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateEndpointResponse.

        项目ID，获取方法请参见获取项目ID。

        :param project_id: The project_id of this CreateEndpointResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tags(self):
        """Gets the tags of this CreateEndpointResponse.

        标签列表，没有标签默认为空数组。

        :return: The tags of this CreateEndpointResponse.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateEndpointResponse.

        标签列表，没有标签默认为空数组。

        :param tags: The tags of this CreateEndpointResponse.
        :type tags: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        """
        self._tags = tags

    @property
    def whitelist(self):
        """Gets the whitelist of this CreateEndpointResponse.

        控制访问终端节点的白名单。 若未创建，则返回空列表。 创建连接Interface类型终端节点服务的终端节点时，显示此参数。

        :return: The whitelist of this CreateEndpointResponse.
        :rtype: list[str]
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this CreateEndpointResponse.

        控制访问终端节点的白名单。 若未创建，则返回空列表。 创建连接Interface类型终端节点服务的终端节点时，显示此参数。

        :param whitelist: The whitelist of this CreateEndpointResponse.
        :type whitelist: list[str]
        """
        self._whitelist = whitelist

    @property
    def enable_whitelist(self):
        """Gets the enable_whitelist of this CreateEndpointResponse.

        是否开启网络ACL隔离。 ● true：开启网络ACL隔离 ● false：不开启网络ACL隔离 若未指定，则返回false。 创建连接Interface类型终端节点服务的终端节点时，显示此参数。

        :return: The enable_whitelist of this CreateEndpointResponse.
        :rtype: bool
        """
        return self._enable_whitelist

    @enable_whitelist.setter
    def enable_whitelist(self, enable_whitelist):
        """Sets the enable_whitelist of this CreateEndpointResponse.

        是否开启网络ACL隔离。 ● true：开启网络ACL隔离 ● false：不开启网络ACL隔离 若未指定，则返回false。 创建连接Interface类型终端节点服务的终端节点时，显示此参数。

        :param enable_whitelist: The enable_whitelist of this CreateEndpointResponse.
        :type enable_whitelist: bool
        """
        self._enable_whitelist = enable_whitelist

    @property
    def routetables(self):
        """Gets the routetables of this CreateEndpointResponse.

        路由表ID列表。 若未指定，返回默认VPC下路由表ID。 创建连接Gateway类型终端节点服务的终端节点时，显示此参数。

        :return: The routetables of this CreateEndpointResponse.
        :rtype: list[str]
        """
        return self._routetables

    @routetables.setter
    def routetables(self, routetables):
        """Sets the routetables of this CreateEndpointResponse.

        路由表ID列表。 若未指定，返回默认VPC下路由表ID。 创建连接Gateway类型终端节点服务的终端节点时，显示此参数。

        :param routetables: The routetables of this CreateEndpointResponse.
        :type routetables: list[str]
        """
        self._routetables = routetables

    @property
    def specification_name(self):
        """Gets the specification_name of this CreateEndpointResponse.

        规格名称

        :return: The specification_name of this CreateEndpointResponse.
        :rtype: str
        """
        return self._specification_name

    @specification_name.setter
    def specification_name(self, specification_name):
        """Sets the specification_name of this CreateEndpointResponse.

        规格名称

        :param specification_name: The specification_name of this CreateEndpointResponse.
        :type specification_name: str
        """
        self._specification_name = specification_name

    @property
    def description(self):
        """Gets the description of this CreateEndpointResponse.

        描述

        :return: The description of this CreateEndpointResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEndpointResponse.

        描述

        :param description: The description of this CreateEndpointResponse.
        :type description: str
        """
        self._description = description

    @property
    def policy_statement(self):
        """Gets the policy_statement of this CreateEndpointResponse.

        只涉及开启双端固定的网关型终端节点，响应体展示此字段

        :return: The policy_statement of this CreateEndpointResponse.
        :rtype: list[str]
        """
        return self._policy_statement

    @policy_statement.setter
    def policy_statement(self, policy_statement):
        """Sets the policy_statement of this CreateEndpointResponse.

        只涉及开启双端固定的网关型终端节点，响应体展示此字段

        :param policy_statement: The policy_statement of this CreateEndpointResponse.
        :type policy_statement: list[str]
        """
        self._policy_statement = policy_statement

    @property
    def enable_status(self):
        """Gets the enable_status of this CreateEndpointResponse.

        终端节点是否已停用，取值【enable/disable】

        :return: The enable_status of this CreateEndpointResponse.
        :rtype: str
        """
        return self._enable_status

    @enable_status.setter
    def enable_status(self, enable_status):
        """Sets the enable_status of this CreateEndpointResponse.

        终端节点是否已停用，取值【enable/disable】

        :param enable_status: The enable_status of this CreateEndpointResponse.
        :type enable_status: str
        """
        self._enable_status = enable_status

    @property
    def endpoint_pool_id(self):
        """Gets the endpoint_pool_id of this CreateEndpointResponse.

        待废弃，实例相关联的集群ID

        :return: The endpoint_pool_id of this CreateEndpointResponse.
        :rtype: str
        """
        return self._endpoint_pool_id

    @endpoint_pool_id.setter
    def endpoint_pool_id(self, endpoint_pool_id):
        """Sets the endpoint_pool_id of this CreateEndpointResponse.

        待废弃，实例相关联的集群ID

        :param endpoint_pool_id: The endpoint_pool_id of this CreateEndpointResponse.
        :type endpoint_pool_id: str
        """
        self._endpoint_pool_id = endpoint_pool_id

    @property
    def public_border_group(self):
        """Gets the public_border_group of this CreateEndpointResponse.

        终端节点对应Pool的Public Border Group信息

        :return: The public_border_group of this CreateEndpointResponse.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this CreateEndpointResponse.

        终端节点对应Pool的Public Border Group信息

        :param public_border_group: The public_border_group of this CreateEndpointResponse.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

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
        if not isinstance(other, CreateEndpointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
