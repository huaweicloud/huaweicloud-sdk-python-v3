# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'subnet_id': 'str',
        'endpoint_service_id': 'str',
        'vpc_id': 'str',
        'enable_dns': 'bool',
        'tags': 'list[TagList]',
        'routetables': 'list[str]',
        'port_ip': 'str',
        'whitelist': 'list[str]',
        'enable_whitelist': 'bool'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'endpoint_service_id': 'endpoint_service_id',
        'vpc_id': 'vpc_id',
        'enable_dns': 'enable_dns',
        'tags': 'tags',
        'routetables': 'routetables',
        'port_ip': 'port_ip',
        'whitelist': 'whitelist',
        'enable_whitelist': 'enable_whitelist'
    }

    def __init__(self, subnet_id=None, endpoint_service_id=None, vpc_id=None, enable_dns=None, tags=None, routetables=None, port_ip=None, whitelist=None, enable_whitelist=None):
        """CreateEndpointRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._subnet_id = None
        self._endpoint_service_id = None
        self._vpc_id = None
        self._enable_dns = None
        self._tags = None
        self._routetables = None
        self._port_ip = None
        self._whitelist = None
        self._enable_whitelist = None
        self.discriminator = None

        if subnet_id is not None:
            self.subnet_id = subnet_id
        self.endpoint_service_id = endpoint_service_id
        self.vpc_id = vpc_id
        if enable_dns is not None:
            self.enable_dns = enable_dns
        if tags is not None:
            self.tags = tags
        if routetables is not None:
            self.routetables = routetables
        if port_ip is not None:
            self.port_ip = port_ip
        if whitelist is not None:
            self.whitelist = whitelist
        if enable_whitelist is not None:
            self.enable_whitelist = enable_whitelist

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateEndpointRequestBody.

        需要指定vpc_id对应VPC下已 创建的网络（network）的 ID，UUID格式。 详细内容请参考《虚拟私有云 API参考》中的“查询子 网”，详见响应消息中的 “id”字段。 创建连接Interface类型终端节 点服务的终端节点时，此参数 必选。 说明 ● VPC的子网网段不能与 198.19.128.0/20重叠 ● VPC路由表中自定义路由的目 的地址不能与 198.19.128.0/20重叠

        :return: The subnet_id of this CreateEndpointRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateEndpointRequestBody.

        需要指定vpc_id对应VPC下已 创建的网络（network）的 ID，UUID格式。 详细内容请参考《虚拟私有云 API参考》中的“查询子 网”，详见响应消息中的 “id”字段。 创建连接Interface类型终端节 点服务的终端节点时，此参数 必选。 说明 ● VPC的子网网段不能与 198.19.128.0/20重叠 ● VPC路由表中自定义路由的目 的地址不能与 198.19.128.0/20重叠

        :param subnet_id: The subnet_id of this CreateEndpointRequestBody.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def endpoint_service_id(self):
        """Gets the endpoint_service_id of this CreateEndpointRequestBody.

        终端节点服务的ID。 可以通过查询终端节点服务概 要获取要连接的终端节点服务 ID。

        :return: The endpoint_service_id of this CreateEndpointRequestBody.
        :rtype: str
        """
        return self._endpoint_service_id

    @endpoint_service_id.setter
    def endpoint_service_id(self, endpoint_service_id):
        """Sets the endpoint_service_id of this CreateEndpointRequestBody.

        终端节点服务的ID。 可以通过查询终端节点服务概 要获取要连接的终端节点服务 ID。

        :param endpoint_service_id: The endpoint_service_id of this CreateEndpointRequestBody.
        :type: str
        """
        self._endpoint_service_id = endpoint_service_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateEndpointRequestBody.

        终端节点所在的VPC的ID。 详细内容请参考《虚拟私有云 API参考》中的“查询VPC”， 详见响应消息中的“id”字 段。

        :return: The vpc_id of this CreateEndpointRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateEndpointRequestBody.

        终端节点所在的VPC的ID。 详细内容请参考《虚拟私有云 API参考》中的“查询VPC”， 详见响应消息中的“id”字 段。

        :param vpc_id: The vpc_id of this CreateEndpointRequestBody.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def enable_dns(self):
        """Gets the enable_dns of this CreateEndpointRequestBody.

        是否创建域名。 ● true：创建域名 ● false：不创建域名 默认值为false。 说明 当创建连接gateway类型终端节 点服务的终端节点时， “enable_dns”设置为true或者 false，均不创建域名。

        :return: The enable_dns of this CreateEndpointRequestBody.
        :rtype: bool
        """
        return self._enable_dns

    @enable_dns.setter
    def enable_dns(self, enable_dns):
        """Sets the enable_dns of this CreateEndpointRequestBody.

        是否创建域名。 ● true：创建域名 ● false：不创建域名 默认值为false。 说明 当创建连接gateway类型终端节 点服务的终端节点时， “enable_dns”设置为true或者 false，均不创建域名。

        :param enable_dns: The enable_dns of this CreateEndpointRequestBody.
        :type: bool
        """
        self._enable_dns = enable_dns

    @property
    def tags(self):
        """Gets the tags of this CreateEndpointRequestBody.

        标签列表，没有标签默认为空数组。

        :return: The tags of this CreateEndpointRequestBody.
        :rtype: list[TagList]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateEndpointRequestBody.

        标签列表，没有标签默认为空数组。

        :param tags: The tags of this CreateEndpointRequestBody.
        :type: list[TagList]
        """
        self._tags = tags

    @property
    def routetables(self):
        """Gets the routetables of this CreateEndpointRequestBody.

        路由表ID列表。 详细内容请参考《虚拟私有云 API参考》中的“查询VPC路 由”，详见响应消息中的 “id”字段。 创建连接gateway类型终端节 点服务的终节点时，此参数必 选。 说明 不设置此参数时，选择默认路由 表。

        :return: The routetables of this CreateEndpointRequestBody.
        :rtype: list[str]
        """
        return self._routetables

    @routetables.setter
    def routetables(self, routetables):
        """Sets the routetables of this CreateEndpointRequestBody.

        路由表ID列表。 详细内容请参考《虚拟私有云 API参考》中的“查询VPC路 由”，详见响应消息中的 “id”字段。 创建连接gateway类型终端节 点服务的终节点时，此参数必 选。 说明 不设置此参数时，选择默认路由 表。

        :param routetables: The routetables of this CreateEndpointRequestBody.
        :type: list[str]
        """
        self._routetables = routetables

    @property
    def port_ip(self):
        """Gets the port_ip of this CreateEndpointRequestBody.

        访问所连接的终端节点服务的 IP。 创建终端节点时，可以指定访 问所连接的终端节点服务的 IP，目前只支持IPv4类型 。 创建连接Interface类型终端节 点服务的终端节点时，此参数 必选。

        :return: The port_ip of this CreateEndpointRequestBody.
        :rtype: str
        """
        return self._port_ip

    @port_ip.setter
    def port_ip(self, port_ip):
        """Sets the port_ip of this CreateEndpointRequestBody.

        访问所连接的终端节点服务的 IP。 创建终端节点时，可以指定访 问所连接的终端节点服务的 IP，目前只支持IPv4类型 。 创建连接Interface类型终端节 点服务的终端节点时，此参数 必选。

        :param port_ip: The port_ip of this CreateEndpointRequestBody.
        :type: str
        """
        self._port_ip = port_ip

    @property
    def whitelist(self):
        """Gets the whitelist of this CreateEndpointRequestBody.

        添加用于控制访问终端节点的 白名单。 创建终端节点时，支持访问控 制，使用此参数可以添加IPv4 或CIDR，默认空列表。 仅当创建连接Interface类型终 端节点服务的终端节点时，支 持设置此参数。

        :return: The whitelist of this CreateEndpointRequestBody.
        :rtype: list[str]
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this CreateEndpointRequestBody.

        添加用于控制访问终端节点的 白名单。 创建终端节点时，支持访问控 制，使用此参数可以添加IPv4 或CIDR，默认空列表。 仅当创建连接Interface类型终 端节点服务的终端节点时，支 持设置此参数。

        :param whitelist: The whitelist of this CreateEndpointRequestBody.
        :type: list[str]
        """
        self._whitelist = whitelist

    @property
    def enable_whitelist(self):
        """Gets the enable_whitelist of this CreateEndpointRequestBody.

        是否开启网络ACL隔离。

        :return: The enable_whitelist of this CreateEndpointRequestBody.
        :rtype: bool
        """
        return self._enable_whitelist

    @enable_whitelist.setter
    def enable_whitelist(self, enable_whitelist):
        """Sets the enable_whitelist of this CreateEndpointRequestBody.

        是否开启网络ACL隔离。

        :param enable_whitelist: The enable_whitelist of this CreateEndpointRequestBody.
        :type: bool
        """
        self._enable_whitelist = enable_whitelist

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
        if not isinstance(other, CreateEndpointRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
