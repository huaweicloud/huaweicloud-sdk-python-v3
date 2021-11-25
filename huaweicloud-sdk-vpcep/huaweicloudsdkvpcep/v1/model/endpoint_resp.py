# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointResp:


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
        'endpoint_service_name': 'str',
        'marker_id': 'int',
        'endpoint_service_id': 'str',
        'enable_dns': 'bool',
        'dns_names': 'list[str]',
        'ip': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'project_id': 'str',
        'tags': 'list[TagList]',
        'error': 'list[QueryError]',
        'whitelist': 'list[str]',
        'enable_whitelist': 'bool',
        'routetables': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'service_type': 'service_type',
        'status': 'status',
        'active_status': 'active_status',
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
        'routetables': 'routetables'
    }

    def __init__(self, id=None, service_type=None, status=None, active_status=None, endpoint_service_name=None, marker_id=None, endpoint_service_id=None, enable_dns=None, dns_names=None, ip=None, vpc_id=None, subnet_id=None, created_at=None, updated_at=None, project_id=None, tags=None, error=None, whitelist=None, enable_whitelist=None, routetables=None):
        """EndpointResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._service_type = None
        self._status = None
        self._active_status = None
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
        self.discriminator = None

        if id is not None:
            self.id = id
        if service_type is not None:
            self.service_type = service_type
        if status is not None:
            self.status = status
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

    @property
    def id(self):
        """Gets the id of this EndpointResp.

        终端节点的ID，唯一标识。

        :return: The id of this EndpointResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndpointResp.

        终端节点的ID，唯一标识。

        :param id: The id of this EndpointResp.
        :type: str
        """
        self._id = id

    @property
    def service_type(self):
        """Gets the service_type of this EndpointResp.

        终端节点连接的终端节点服务类 型。 ● gataway：由运维人员配置。 用户无需创建，可直接使用。 ● interface：包括运维人员配置 的云服务和用户自己创建的私 有服务。其中，运维人员配置 的云服务无需创建，用户可直 接使用。 您可以通过查询公共终端节点服 务列表查看由运维人员配置的所 有用户可见且可连接的终端节点 服务，并通过创建终端节点服务 创建Interface类型的终端节点服 务。

        :return: The service_type of this EndpointResp.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this EndpointResp.

        终端节点连接的终端节点服务类 型。 ● gataway：由运维人员配置。 用户无需创建，可直接使用。 ● interface：包括运维人员配置 的云服务和用户自己创建的私 有服务。其中，运维人员配置 的云服务无需创建，用户可直 接使用。 您可以通过查询公共终端节点服 务列表查看由运维人员配置的所 有用户可见且可连接的终端节点 服务，并通过创建终端节点服务 创建Interface类型的终端节点服 务。

        :param service_type: The service_type of this EndpointResp.
        :type: str
        """
        self._service_type = service_type

    @property
    def status(self):
        """Gets the status of this EndpointResp.

        终端节点的连接状态。 ● pendingAcceptance：待接受 ● creating：创建中 ● accepted：已接受 ● failed：失败

        :return: The status of this EndpointResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EndpointResp.

        终端节点的连接状态。 ● pendingAcceptance：待接受 ● creating：创建中 ● accepted：已接受 ● failed：失败

        :param status: The status of this EndpointResp.
        :type: str
        """
        self._status = status

    @property
    def active_status(self):
        """Gets the active_status of this EndpointResp.

        帐号状态。 ● frozen：冻结 ● active：解冻

        :return: The active_status of this EndpointResp.
        :rtype: list[str]
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        """Sets the active_status of this EndpointResp.

        帐号状态。 ● frozen：冻结 ● active：解冻

        :param active_status: The active_status of this EndpointResp.
        :type: list[str]
        """
        self._active_status = active_status

    @property
    def endpoint_service_name(self):
        """Gets the endpoint_service_name of this EndpointResp.

        终端节点服务的名称。

        :return: The endpoint_service_name of this EndpointResp.
        :rtype: str
        """
        return self._endpoint_service_name

    @endpoint_service_name.setter
    def endpoint_service_name(self, endpoint_service_name):
        """Sets the endpoint_service_name of this EndpointResp.

        终端节点服务的名称。

        :param endpoint_service_name: The endpoint_service_name of this EndpointResp.
        :type: str
        """
        self._endpoint_service_name = endpoint_service_name

    @property
    def marker_id(self):
        """Gets the marker_id of this EndpointResp.

        终端节点的报文标识。

        :return: The marker_id of this EndpointResp.
        :rtype: int
        """
        return self._marker_id

    @marker_id.setter
    def marker_id(self, marker_id):
        """Sets the marker_id of this EndpointResp.

        终端节点的报文标识。

        :param marker_id: The marker_id of this EndpointResp.
        :type: int
        """
        self._marker_id = marker_id

    @property
    def endpoint_service_id(self):
        """Gets the endpoint_service_id of this EndpointResp.

        终端节点服务的ID。

        :return: The endpoint_service_id of this EndpointResp.
        :rtype: str
        """
        return self._endpoint_service_id

    @endpoint_service_id.setter
    def endpoint_service_id(self, endpoint_service_id):
        """Sets the endpoint_service_id of this EndpointResp.

        终端节点服务的ID。

        :param endpoint_service_id: The endpoint_service_id of this EndpointResp.
        :type: str
        """
        self._endpoint_service_id = endpoint_service_id

    @property
    def enable_dns(self):
        """Gets the enable_dns of this EndpointResp.

        是否创建域名。 ● true：创建域名 ● false：不创建域名 说明 当创建连接gateway类型终端节点服 务的终端节点时，“enable_dns”设 置为true或者false，均不创建域名。

        :return: The enable_dns of this EndpointResp.
        :rtype: bool
        """
        return self._enable_dns

    @enable_dns.setter
    def enable_dns(self, enable_dns):
        """Sets the enable_dns of this EndpointResp.

        是否创建域名。 ● true：创建域名 ● false：不创建域名 说明 当创建连接gateway类型终端节点服 务的终端节点时，“enable_dns”设 置为true或者false，均不创建域名。

        :param enable_dns: The enable_dns of this EndpointResp.
        :type: bool
        """
        self._enable_dns = enable_dns

    @property
    def dns_names(self):
        """Gets the dns_names of this EndpointResp.

        访问所连接的终端节点服务的域 名。 当“enable_dns”为true时，该 参数可见。

        :return: The dns_names of this EndpointResp.
        :rtype: list[str]
        """
        return self._dns_names

    @dns_names.setter
    def dns_names(self, dns_names):
        """Sets the dns_names of this EndpointResp.

        访问所连接的终端节点服务的域 名。 当“enable_dns”为true时，该 参数可见。

        :param dns_names: The dns_names of this EndpointResp.
        :type: list[str]
        """
        self._dns_names = dns_names

    @property
    def ip(self):
        """Gets the ip of this EndpointResp.

        访问所连接的终端节点服务的IP。 仅当同时满足如下条件时，返回该参数：  当查询连接interface类型终端节点服务的终端节点时。 终端节点服务启用“连接审批”功能，且已经“接受”连接审批。 “status”可以是“accepted”或者“rejected（仅支持“接受”连接审批后再“拒绝”的情况）”。

        :return: The ip of this EndpointResp.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this EndpointResp.

        访问所连接的终端节点服务的IP。 仅当同时满足如下条件时，返回该参数：  当查询连接interface类型终端节点服务的终端节点时。 终端节点服务启用“连接审批”功能，且已经“接受”连接审批。 “status”可以是“accepted”或者“rejected（仅支持“接受”连接审批后再“拒绝”的情况）”。

        :param ip: The ip of this EndpointResp.
        :type: str
        """
        self._ip = ip

    @property
    def vpc_id(self):
        """Gets the vpc_id of this EndpointResp.

        终端节点所在的VPC的ID。

        :return: The vpc_id of this EndpointResp.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this EndpointResp.

        终端节点所在的VPC的ID。

        :param vpc_id: The vpc_id of this EndpointResp.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this EndpointResp.

        vpc_id对应VPC下已创建的网络 （network）的ID，UUID格式。

        :return: The subnet_id of this EndpointResp.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this EndpointResp.

        vpc_id对应VPC下已创建的网络 （network）的ID，UUID格式。

        :param subnet_id: The subnet_id of this EndpointResp.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def created_at(self):
        """Gets the created_at of this EndpointResp.

        终端节点的创建时间。 采用UTC时间格式，格式为： YYYY-MM-DDTHH:MM:SSZ

        :return: The created_at of this EndpointResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EndpointResp.

        终端节点的创建时间。 采用UTC时间格式，格式为： YYYY-MM-DDTHH:MM:SSZ

        :param created_at: The created_at of this EndpointResp.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EndpointResp.

        终端节点的更新时间。 采用UTC时间格式，格式为： YYYY-MM-DDTHH:MM:SSZ

        :return: The updated_at of this EndpointResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EndpointResp.

        终端节点的更新时间。 采用UTC时间格式，格式为： YYYY-MM-DDTHH:MM:SSZ

        :param updated_at: The updated_at of this EndpointResp.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        """Gets the project_id of this EndpointResp.

        项目ID，获取方法请参见获取项 目ID。

        :return: The project_id of this EndpointResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this EndpointResp.

        项目ID，获取方法请参见获取项 目ID。

        :param project_id: The project_id of this EndpointResp.
        :type: str
        """
        self._project_id = project_id

    @property
    def tags(self):
        """Gets the tags of this EndpointResp.

        标签列表，没有标签默认为空数组。

        :return: The tags of this EndpointResp.
        :rtype: list[TagList]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EndpointResp.

        标签列表，没有标签默认为空数组。

        :param tags: The tags of this EndpointResp.
        :type: list[TagList]
        """
        self._tags = tags

    @property
    def error(self):
        """Gets the error of this EndpointResp.

        错误信息。  当终端节点状态异常，即“status”的值为“failed”时，会返回该字段。

        :return: The error of this EndpointResp.
        :rtype: list[QueryError]
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EndpointResp.

        错误信息。  当终端节点状态异常，即“status”的值为“failed”时，会返回该字段。

        :param error: The error of this EndpointResp.
        :type: list[QueryError]
        """
        self._error = error

    @property
    def whitelist(self):
        """Gets the whitelist of this EndpointResp.

        控制访问终端节点的白名单。 若未创建，则返回空列表。 创建连接Interface类型终端节点 服务的终端节点时，显示此参 数。

        :return: The whitelist of this EndpointResp.
        :rtype: list[str]
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this EndpointResp.

        控制访问终端节点的白名单。 若未创建，则返回空列表。 创建连接Interface类型终端节点 服务的终端节点时，显示此参 数。

        :param whitelist: The whitelist of this EndpointResp.
        :type: list[str]
        """
        self._whitelist = whitelist

    @property
    def enable_whitelist(self):
        """Gets the enable_whitelist of this EndpointResp.

        是否开启网络ACL隔离。 ● true：开启网络ACL隔离 ● false：不开启网络ACL隔离 若未指定，则返回false。 创建连接Interface类型终端节点 服务的终端节点时，显示此参 数。

        :return: The enable_whitelist of this EndpointResp.
        :rtype: bool
        """
        return self._enable_whitelist

    @enable_whitelist.setter
    def enable_whitelist(self, enable_whitelist):
        """Sets the enable_whitelist of this EndpointResp.

        是否开启网络ACL隔离。 ● true：开启网络ACL隔离 ● false：不开启网络ACL隔离 若未指定，则返回false。 创建连接Interface类型终端节点 服务的终端节点时，显示此参 数。

        :param enable_whitelist: The enable_whitelist of this EndpointResp.
        :type: bool
        """
        self._enable_whitelist = enable_whitelist

    @property
    def routetables(self):
        """Gets the routetables of this EndpointResp.

        路由表ID列表。 若未指定，返回默认VPC下路由表 ID。 创建连接Gateway类型终端节点 服务的终端节点时，显示此参 数。

        :return: The routetables of this EndpointResp.
        :rtype: list[str]
        """
        return self._routetables

    @routetables.setter
    def routetables(self, routetables):
        """Sets the routetables of this EndpointResp.

        路由表ID列表。 若未指定，返回默认VPC下路由表 ID。 创建连接Gateway类型终端节点 服务的终端节点时，显示此参 数。

        :param routetables: The routetables of this EndpointResp.
        :type: list[str]
        """
        self._routetables = routetables

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
        if not isinstance(other, EndpointResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other