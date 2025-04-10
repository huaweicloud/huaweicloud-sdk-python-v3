# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointInfoDetailsResponse(SdkResponse):

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
        'active_status': 'list[str]',
        'enable_status': 'str',
        'specification_name': 'str',
        'endpoint_service_name': 'str',
        'marker_id': 'int',
        'endpoint_service_id': 'str',
        'enable_dns': 'bool',
        'dns_names': 'list[str]',
        'ip': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'project_id': 'str',
        'tags': 'list[TagList]',
        'error': 'list[QueryError]',
        'whitelist': 'list[str]',
        'enable_whitelist': 'bool',
        'routetables': 'list[str]',
        'description': 'str',
        'policy_statement': 'list[PolicyStatement]',
        'policy_document': 'object',
        'endpoint_pool_id': 'str',
        'public_border_group': 'str',
        'ipv6_address': 'str'
    }

    attribute_map = {
        'id': 'id',
        'service_type': 'service_type',
        'status': 'status',
        'active_status': 'active_status',
        'enable_status': 'enable_status',
        'specification_name': 'specification_name',
        'endpoint_service_name': 'endpoint_service_name',
        'marker_id': 'marker_id',
        'endpoint_service_id': 'endpoint_service_id',
        'enable_dns': 'enable_dns',
        'dns_names': 'dns_names',
        'ip': 'ip',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'project_id': 'project_id',
        'tags': 'tags',
        'error': 'error',
        'whitelist': 'whitelist',
        'enable_whitelist': 'enable_whitelist',
        'routetables': 'routetables',
        'description': 'description',
        'policy_statement': 'policy_statement',
        'policy_document': 'policy_document',
        'endpoint_pool_id': 'endpoint_pool_id',
        'public_border_group': 'public_border_group',
        'ipv6_address': 'ipv6_address'
    }

    def __init__(self, id=None, service_type=None, status=None, active_status=None, enable_status=None, specification_name=None, endpoint_service_name=None, marker_id=None, endpoint_service_id=None, enable_dns=None, dns_names=None, ip=None, vpc_id=None, subnet_id=None, created_at=None, updated_at=None, project_id=None, tags=None, error=None, whitelist=None, enable_whitelist=None, routetables=None, description=None, policy_statement=None, policy_document=None, endpoint_pool_id=None, public_border_group=None, ipv6_address=None):
        r"""ListEndpointInfoDetailsResponse

        The model defined in huaweicloud sdk

        :param id: 终端节点的ID，唯一标识。
        :type id: str
        :param service_type: 终端节点连接的终端节点服务类型。  - gateway：由运维人员配置。用户无需创建，可直接使用。  - interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建，用户可直接使用。 您可以通过查询公共终端节点服务列表， 查看由运维人员配置的所有用户可见且可连接的终端节点服务， 并通过创建终端节点服务创建Interface类型的终端节点服务。
        :type service_type: str
        :param status: 终端节点的连接状态。  - pendingAcceptance：待接受  - creating：创建中  - accepted：已接受  - rejected：已拒绝  - failed：失败  - deleting：删除中
        :type status: str
        :param active_status: 账号状态。  - frozen：冻结  - active：解冻
        :type active_status: list[str]
        :param enable_status: 终端节点是否可用。  - enable：启用  - disable：不启用
        :type enable_status: str
        :param specification_name: 终端节点服务规格的名称。
        :type specification_name: str
        :param endpoint_service_name: 终端节点服务的名称。
        :type endpoint_service_name: str
        :param marker_id: 终端节点的报文标识。
        :type marker_id: int
        :param endpoint_service_id: 终端节点服务的ID。
        :type endpoint_service_id: str
        :param enable_dns: 是否创建域名。  - true：创建域名  - false：不创建域名 说明 当创建gateway类型终端节点服务的终端节点时， “enable_dns”设置为true或者false，均不创建域名。
        :type enable_dns: bool
        :param dns_names: 访问所连接的终端节点服务的域名。 当“enable_dns”为true时，该参数可见。
        :type dns_names: list[str]
        :param ip: 访问所连接的终端节点服务的IP。 仅当同时满足如下条件时，返回该参数：  - 当查询连接interface类型终端节点服务的终端节点时。  - 终端节点服务启用“连接审批”功能，且已经“接受”连接审批。 “status”可以是“accepted”或者“rejected（仅支持“接受”连接审批后再“拒绝”的情况）”。
        :type ip: str
        :param vpc_id: 终端节点所在的VPC的ID。
        :type vpc_id: str
        :param subnet_id: vpc_id对应VPC下已创建的网络（network）的ID，UUID格式。
        :type subnet_id: str
        :param created_at: 终端节点的创建时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ
        :type created_at: datetime
        :param updated_at: 终端节点的更新时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ
        :type updated_at: datetime
        :param project_id: 项目ID，获取方法请参见获取项目ID。
        :type project_id: str
        :param tags: 标签列表，没有标签默认为空数组。
        :type tags: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        :param error: 
        :type error: list[:class:`huaweicloudsdkvpcep.v1.QueryError`]
        :param whitelist: 控制访问终端节点的白名单。 若未创建，则返回空列表。 创建连接Interface类型终端节点服务的终端节点时，显示此参数。
        :type whitelist: list[str]
        :param enable_whitelist: 是否开启网络ACL隔离。  - true：开启网络ACL隔离  - false：不开启网络ACL隔离 若未指定，则返回false。 创建连接Interface类型终端节点服务的终端节点时，显示此参数。
        :type enable_whitelist: bool
        :param routetables: 路由表ID列表。 若未指定，返回默认VPC下路由表ID。 创建gateway类型终端节点服务的终端节点时，显示此参数。
        :type routetables: list[str]
        :param description: 描述字段，支持中英文字母、数字等字符，不支持“&lt;”或“&gt;”字符。
        :type description: str
        :param policy_statement: Gateway类型终端节点策略信息，仅限OBS、SFS的终端节点服务的enable_policy值为true时支持该参数。
        :type policy_statement: list[:class:`huaweicloudsdkvpcep.v1.PolicyStatement`]
        :param policy_document: 终端节点策略信息，仅当终端节点服务的enable_policy值为true时支持该参数，默认值为完全访问权限。（OBS、SFS的终端节点服务暂不支持该参数）
        :type policy_document: object
        :param endpoint_pool_id: 待废弃，实例相关联的集群ID
        :type endpoint_pool_id: str
        :param public_border_group: 终端节点对应Pool的Public Border Group信息
        :type public_border_group: str
        :param ipv6_address: 访问所连接的终端节点服务的IPv6的地址。  创建终端节点时，可以指定访问所连接的终端节点服务的IP，不指定的情况下，会使用系统生成的一个地址。  仅专业型终端节点支持此参数。
        :type ipv6_address: str
        """
        
        super(ListEndpointInfoDetailsResponse, self).__init__()

        self._id = None
        self._service_type = None
        self._status = None
        self._active_status = None
        self._enable_status = None
        self._specification_name = None
        self._endpoint_service_name = None
        self._marker_id = None
        self._endpoint_service_id = None
        self._enable_dns = None
        self._dns_names = None
        self._ip = None
        self._vpc_id = None
        self._subnet_id = None
        self._created_at = None
        self._updated_at = None
        self._project_id = None
        self._tags = None
        self._error = None
        self._whitelist = None
        self._enable_whitelist = None
        self._routetables = None
        self._description = None
        self._policy_statement = None
        self._policy_document = None
        self._endpoint_pool_id = None
        self._public_border_group = None
        self._ipv6_address = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if service_type is not None:
            self.service_type = service_type
        if status is not None:
            self.status = status
        if active_status is not None:
            self.active_status = active_status
        if enable_status is not None:
            self.enable_status = enable_status
        if specification_name is not None:
            self.specification_name = specification_name
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
        if ip is not None:
            self.ip = ip
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if project_id is not None:
            self.project_id = project_id
        if tags is not None:
            self.tags = tags
        if error is not None:
            self.error = error
        if whitelist is not None:
            self.whitelist = whitelist
        if enable_whitelist is not None:
            self.enable_whitelist = enable_whitelist
        if routetables is not None:
            self.routetables = routetables
        if description is not None:
            self.description = description
        if policy_statement is not None:
            self.policy_statement = policy_statement
        if policy_document is not None:
            self.policy_document = policy_document
        if endpoint_pool_id is not None:
            self.endpoint_pool_id = endpoint_pool_id
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if ipv6_address is not None:
            self.ipv6_address = ipv6_address

    @property
    def id(self):
        r"""Gets the id of this ListEndpointInfoDetailsResponse.

        终端节点的ID，唯一标识。

        :return: The id of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListEndpointInfoDetailsResponse.

        终端节点的ID，唯一标识。

        :param id: The id of this ListEndpointInfoDetailsResponse.
        :type id: str
        """
        self._id = id

    @property
    def service_type(self):
        r"""Gets the service_type of this ListEndpointInfoDetailsResponse.

        终端节点连接的终端节点服务类型。  - gateway：由运维人员配置。用户无需创建，可直接使用。  - interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建，用户可直接使用。 您可以通过查询公共终端节点服务列表， 查看由运维人员配置的所有用户可见且可连接的终端节点服务， 并通过创建终端节点服务创建Interface类型的终端节点服务。

        :return: The service_type of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ListEndpointInfoDetailsResponse.

        终端节点连接的终端节点服务类型。  - gateway：由运维人员配置。用户无需创建，可直接使用。  - interface：包括运维人员配置的云服务和用户自己创建的私有服务。 其中，运维人员配置的云服务无需创建，用户可直接使用。 您可以通过查询公共终端节点服务列表， 查看由运维人员配置的所有用户可见且可连接的终端节点服务， 并通过创建终端节点服务创建Interface类型的终端节点服务。

        :param service_type: The service_type of this ListEndpointInfoDetailsResponse.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def status(self):
        r"""Gets the status of this ListEndpointInfoDetailsResponse.

        终端节点的连接状态。  - pendingAcceptance：待接受  - creating：创建中  - accepted：已接受  - rejected：已拒绝  - failed：失败  - deleting：删除中

        :return: The status of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListEndpointInfoDetailsResponse.

        终端节点的连接状态。  - pendingAcceptance：待接受  - creating：创建中  - accepted：已接受  - rejected：已拒绝  - failed：失败  - deleting：删除中

        :param status: The status of this ListEndpointInfoDetailsResponse.
        :type status: str
        """
        self._status = status

    @property
    def active_status(self):
        r"""Gets the active_status of this ListEndpointInfoDetailsResponse.

        账号状态。  - frozen：冻结  - active：解冻

        :return: The active_status of this ListEndpointInfoDetailsResponse.
        :rtype: list[str]
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        r"""Sets the active_status of this ListEndpointInfoDetailsResponse.

        账号状态。  - frozen：冻结  - active：解冻

        :param active_status: The active_status of this ListEndpointInfoDetailsResponse.
        :type active_status: list[str]
        """
        self._active_status = active_status

    @property
    def enable_status(self):
        r"""Gets the enable_status of this ListEndpointInfoDetailsResponse.

        终端节点是否可用。  - enable：启用  - disable：不启用

        :return: The enable_status of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._enable_status

    @enable_status.setter
    def enable_status(self, enable_status):
        r"""Sets the enable_status of this ListEndpointInfoDetailsResponse.

        终端节点是否可用。  - enable：启用  - disable：不启用

        :param enable_status: The enable_status of this ListEndpointInfoDetailsResponse.
        :type enable_status: str
        """
        self._enable_status = enable_status

    @property
    def specification_name(self):
        r"""Gets the specification_name of this ListEndpointInfoDetailsResponse.

        终端节点服务规格的名称。

        :return: The specification_name of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._specification_name

    @specification_name.setter
    def specification_name(self, specification_name):
        r"""Sets the specification_name of this ListEndpointInfoDetailsResponse.

        终端节点服务规格的名称。

        :param specification_name: The specification_name of this ListEndpointInfoDetailsResponse.
        :type specification_name: str
        """
        self._specification_name = specification_name

    @property
    def endpoint_service_name(self):
        r"""Gets the endpoint_service_name of this ListEndpointInfoDetailsResponse.

        终端节点服务的名称。

        :return: The endpoint_service_name of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._endpoint_service_name

    @endpoint_service_name.setter
    def endpoint_service_name(self, endpoint_service_name):
        r"""Sets the endpoint_service_name of this ListEndpointInfoDetailsResponse.

        终端节点服务的名称。

        :param endpoint_service_name: The endpoint_service_name of this ListEndpointInfoDetailsResponse.
        :type endpoint_service_name: str
        """
        self._endpoint_service_name = endpoint_service_name

    @property
    def marker_id(self):
        r"""Gets the marker_id of this ListEndpointInfoDetailsResponse.

        终端节点的报文标识。

        :return: The marker_id of this ListEndpointInfoDetailsResponse.
        :rtype: int
        """
        return self._marker_id

    @marker_id.setter
    def marker_id(self, marker_id):
        r"""Sets the marker_id of this ListEndpointInfoDetailsResponse.

        终端节点的报文标识。

        :param marker_id: The marker_id of this ListEndpointInfoDetailsResponse.
        :type marker_id: int
        """
        self._marker_id = marker_id

    @property
    def endpoint_service_id(self):
        r"""Gets the endpoint_service_id of this ListEndpointInfoDetailsResponse.

        终端节点服务的ID。

        :return: The endpoint_service_id of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._endpoint_service_id

    @endpoint_service_id.setter
    def endpoint_service_id(self, endpoint_service_id):
        r"""Sets the endpoint_service_id of this ListEndpointInfoDetailsResponse.

        终端节点服务的ID。

        :param endpoint_service_id: The endpoint_service_id of this ListEndpointInfoDetailsResponse.
        :type endpoint_service_id: str
        """
        self._endpoint_service_id = endpoint_service_id

    @property
    def enable_dns(self):
        r"""Gets the enable_dns of this ListEndpointInfoDetailsResponse.

        是否创建域名。  - true：创建域名  - false：不创建域名 说明 当创建gateway类型终端节点服务的终端节点时， “enable_dns”设置为true或者false，均不创建域名。

        :return: The enable_dns of this ListEndpointInfoDetailsResponse.
        :rtype: bool
        """
        return self._enable_dns

    @enable_dns.setter
    def enable_dns(self, enable_dns):
        r"""Sets the enable_dns of this ListEndpointInfoDetailsResponse.

        是否创建域名。  - true：创建域名  - false：不创建域名 说明 当创建gateway类型终端节点服务的终端节点时， “enable_dns”设置为true或者false，均不创建域名。

        :param enable_dns: The enable_dns of this ListEndpointInfoDetailsResponse.
        :type enable_dns: bool
        """
        self._enable_dns = enable_dns

    @property
    def dns_names(self):
        r"""Gets the dns_names of this ListEndpointInfoDetailsResponse.

        访问所连接的终端节点服务的域名。 当“enable_dns”为true时，该参数可见。

        :return: The dns_names of this ListEndpointInfoDetailsResponse.
        :rtype: list[str]
        """
        return self._dns_names

    @dns_names.setter
    def dns_names(self, dns_names):
        r"""Sets the dns_names of this ListEndpointInfoDetailsResponse.

        访问所连接的终端节点服务的域名。 当“enable_dns”为true时，该参数可见。

        :param dns_names: The dns_names of this ListEndpointInfoDetailsResponse.
        :type dns_names: list[str]
        """
        self._dns_names = dns_names

    @property
    def ip(self):
        r"""Gets the ip of this ListEndpointInfoDetailsResponse.

        访问所连接的终端节点服务的IP。 仅当同时满足如下条件时，返回该参数：  - 当查询连接interface类型终端节点服务的终端节点时。  - 终端节点服务启用“连接审批”功能，且已经“接受”连接审批。 “status”可以是“accepted”或者“rejected（仅支持“接受”连接审批后再“拒绝”的情况）”。

        :return: The ip of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ListEndpointInfoDetailsResponse.

        访问所连接的终端节点服务的IP。 仅当同时满足如下条件时，返回该参数：  - 当查询连接interface类型终端节点服务的终端节点时。  - 终端节点服务启用“连接审批”功能，且已经“接受”连接审批。 “status”可以是“accepted”或者“rejected（仅支持“接受”连接审批后再“拒绝”的情况）”。

        :param ip: The ip of this ListEndpointInfoDetailsResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListEndpointInfoDetailsResponse.

        终端节点所在的VPC的ID。

        :return: The vpc_id of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListEndpointInfoDetailsResponse.

        终端节点所在的VPC的ID。

        :param vpc_id: The vpc_id of this ListEndpointInfoDetailsResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ListEndpointInfoDetailsResponse.

        vpc_id对应VPC下已创建的网络（network）的ID，UUID格式。

        :return: The subnet_id of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ListEndpointInfoDetailsResponse.

        vpc_id对应VPC下已创建的网络（network）的ID，UUID格式。

        :param subnet_id: The subnet_id of this ListEndpointInfoDetailsResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def created_at(self):
        r"""Gets the created_at of this ListEndpointInfoDetailsResponse.

        终端节点的创建时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :return: The created_at of this ListEndpointInfoDetailsResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ListEndpointInfoDetailsResponse.

        终端节点的创建时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :param created_at: The created_at of this ListEndpointInfoDetailsResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ListEndpointInfoDetailsResponse.

        终端节点的更新时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :return: The updated_at of this ListEndpointInfoDetailsResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ListEndpointInfoDetailsResponse.

        终端节点的更新时间。 采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :param updated_at: The updated_at of this ListEndpointInfoDetailsResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        r"""Gets the project_id of this ListEndpointInfoDetailsResponse.

        项目ID，获取方法请参见获取项目ID。

        :return: The project_id of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListEndpointInfoDetailsResponse.

        项目ID，获取方法请参见获取项目ID。

        :param project_id: The project_id of this ListEndpointInfoDetailsResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tags(self):
        r"""Gets the tags of this ListEndpointInfoDetailsResponse.

        标签列表，没有标签默认为空数组。

        :return: The tags of this ListEndpointInfoDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListEndpointInfoDetailsResponse.

        标签列表，没有标签默认为空数组。

        :param tags: The tags of this ListEndpointInfoDetailsResponse.
        :type tags: list[:class:`huaweicloudsdkvpcep.v1.TagList`]
        """
        self._tags = tags

    @property
    def error(self):
        r"""Gets the error of this ListEndpointInfoDetailsResponse.

        :return: The error of this ListEndpointInfoDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.QueryError`]
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ListEndpointInfoDetailsResponse.

        :param error: The error of this ListEndpointInfoDetailsResponse.
        :type error: list[:class:`huaweicloudsdkvpcep.v1.QueryError`]
        """
        self._error = error

    @property
    def whitelist(self):
        r"""Gets the whitelist of this ListEndpointInfoDetailsResponse.

        控制访问终端节点的白名单。 若未创建，则返回空列表。 创建连接Interface类型终端节点服务的终端节点时，显示此参数。

        :return: The whitelist of this ListEndpointInfoDetailsResponse.
        :rtype: list[str]
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        r"""Sets the whitelist of this ListEndpointInfoDetailsResponse.

        控制访问终端节点的白名单。 若未创建，则返回空列表。 创建连接Interface类型终端节点服务的终端节点时，显示此参数。

        :param whitelist: The whitelist of this ListEndpointInfoDetailsResponse.
        :type whitelist: list[str]
        """
        self._whitelist = whitelist

    @property
    def enable_whitelist(self):
        r"""Gets the enable_whitelist of this ListEndpointInfoDetailsResponse.

        是否开启网络ACL隔离。  - true：开启网络ACL隔离  - false：不开启网络ACL隔离 若未指定，则返回false。 创建连接Interface类型终端节点服务的终端节点时，显示此参数。

        :return: The enable_whitelist of this ListEndpointInfoDetailsResponse.
        :rtype: bool
        """
        return self._enable_whitelist

    @enable_whitelist.setter
    def enable_whitelist(self, enable_whitelist):
        r"""Sets the enable_whitelist of this ListEndpointInfoDetailsResponse.

        是否开启网络ACL隔离。  - true：开启网络ACL隔离  - false：不开启网络ACL隔离 若未指定，则返回false。 创建连接Interface类型终端节点服务的终端节点时，显示此参数。

        :param enable_whitelist: The enable_whitelist of this ListEndpointInfoDetailsResponse.
        :type enable_whitelist: bool
        """
        self._enable_whitelist = enable_whitelist

    @property
    def routetables(self):
        r"""Gets the routetables of this ListEndpointInfoDetailsResponse.

        路由表ID列表。 若未指定，返回默认VPC下路由表ID。 创建gateway类型终端节点服务的终端节点时，显示此参数。

        :return: The routetables of this ListEndpointInfoDetailsResponse.
        :rtype: list[str]
        """
        return self._routetables

    @routetables.setter
    def routetables(self, routetables):
        r"""Sets the routetables of this ListEndpointInfoDetailsResponse.

        路由表ID列表。 若未指定，返回默认VPC下路由表ID。 创建gateway类型终端节点服务的终端节点时，显示此参数。

        :param routetables: The routetables of this ListEndpointInfoDetailsResponse.
        :type routetables: list[str]
        """
        self._routetables = routetables

    @property
    def description(self):
        r"""Gets the description of this ListEndpointInfoDetailsResponse.

        描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。

        :return: The description of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListEndpointInfoDetailsResponse.

        描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。

        :param description: The description of this ListEndpointInfoDetailsResponse.
        :type description: str
        """
        self._description = description

    @property
    def policy_statement(self):
        r"""Gets the policy_statement of this ListEndpointInfoDetailsResponse.

        Gateway类型终端节点策略信息，仅限OBS、SFS的终端节点服务的enable_policy值为true时支持该参数。

        :return: The policy_statement of this ListEndpointInfoDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.PolicyStatement`]
        """
        return self._policy_statement

    @policy_statement.setter
    def policy_statement(self, policy_statement):
        r"""Sets the policy_statement of this ListEndpointInfoDetailsResponse.

        Gateway类型终端节点策略信息，仅限OBS、SFS的终端节点服务的enable_policy值为true时支持该参数。

        :param policy_statement: The policy_statement of this ListEndpointInfoDetailsResponse.
        :type policy_statement: list[:class:`huaweicloudsdkvpcep.v1.PolicyStatement`]
        """
        self._policy_statement = policy_statement

    @property
    def policy_document(self):
        r"""Gets the policy_document of this ListEndpointInfoDetailsResponse.

        终端节点策略信息，仅当终端节点服务的enable_policy值为true时支持该参数，默认值为完全访问权限。（OBS、SFS的终端节点服务暂不支持该参数）

        :return: The policy_document of this ListEndpointInfoDetailsResponse.
        :rtype: object
        """
        return self._policy_document

    @policy_document.setter
    def policy_document(self, policy_document):
        r"""Sets the policy_document of this ListEndpointInfoDetailsResponse.

        终端节点策略信息，仅当终端节点服务的enable_policy值为true时支持该参数，默认值为完全访问权限。（OBS、SFS的终端节点服务暂不支持该参数）

        :param policy_document: The policy_document of this ListEndpointInfoDetailsResponse.
        :type policy_document: object
        """
        self._policy_document = policy_document

    @property
    def endpoint_pool_id(self):
        r"""Gets the endpoint_pool_id of this ListEndpointInfoDetailsResponse.

        待废弃，实例相关联的集群ID

        :return: The endpoint_pool_id of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._endpoint_pool_id

    @endpoint_pool_id.setter
    def endpoint_pool_id(self, endpoint_pool_id):
        r"""Sets the endpoint_pool_id of this ListEndpointInfoDetailsResponse.

        待废弃，实例相关联的集群ID

        :param endpoint_pool_id: The endpoint_pool_id of this ListEndpointInfoDetailsResponse.
        :type endpoint_pool_id: str
        """
        self._endpoint_pool_id = endpoint_pool_id

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this ListEndpointInfoDetailsResponse.

        终端节点对应Pool的Public Border Group信息

        :return: The public_border_group of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this ListEndpointInfoDetailsResponse.

        终端节点对应Pool的Public Border Group信息

        :param public_border_group: The public_border_group of this ListEndpointInfoDetailsResponse.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def ipv6_address(self):
        r"""Gets the ipv6_address of this ListEndpointInfoDetailsResponse.

        访问所连接的终端节点服务的IPv6的地址。  创建终端节点时，可以指定访问所连接的终端节点服务的IP，不指定的情况下，会使用系统生成的一个地址。  仅专业型终端节点支持此参数。

        :return: The ipv6_address of this ListEndpointInfoDetailsResponse.
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        r"""Sets the ipv6_address of this ListEndpointInfoDetailsResponse.

        访问所连接的终端节点服务的IPv6的地址。  创建终端节点时，可以指定访问所连接的终端节点服务的IP，不指定的情况下，会使用系统生成的一个地址。  仅专业型终端节点支持此参数。

        :param ipv6_address: The ipv6_address of this ListEndpointInfoDetailsResponse.
        :type ipv6_address: str
        """
        self._ipv6_address = ipv6_address

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
        if not isinstance(other, ListEndpointInfoDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
