# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FloatingIpResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fixed_ip_address': 'str',
        'floating_ip_address': 'str',
        'floating_network_id': 'str',
        'id': 'str',
        'port_id': 'str',
        'router_id': 'str',
        'status': 'str',
        'tenant_id': 'str',
        'project_id': 'str',
        'dns_name': 'str',
        'dns_domain': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'fixed_ip_address': 'fixed_ip_address',
        'floating_ip_address': 'floating_ip_address',
        'floating_network_id': 'floating_network_id',
        'id': 'id',
        'port_id': 'port_id',
        'router_id': 'router_id',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'dns_name': 'dns_name',
        'dns_domain': 'dns_domain',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, fixed_ip_address=None, floating_ip_address=None, floating_network_id=None, id=None, port_id=None, router_id=None, status=None, tenant_id=None, project_id=None, dns_name=None, dns_domain=None, created_at=None, updated_at=None):
        """FloatingIpResp

        The model defined in huaweicloud sdk

        :param fixed_ip_address: 关联端口的私有IP地址。
        :type fixed_ip_address: str
        :param floating_ip_address: 浮动IP地址。
        :type floating_ip_address: str
        :param floating_network_id: 外部网络的id。只能使用固定的外网，外部网络的信息请通过GET /v2.0/networks?router:external&#x3D;True或GET /v2.0/networks?name&#x3D;{floating_network}或neutron net-external-list方式查询。
        :type floating_network_id: str
        :param id: 浮动IP地址的id。
        :type id: str
        :param port_id: 端口id。
        :type port_id: str
        :param router_id: 所属路由器id。
        :type router_id: str
        :param status: 网络状态，可以为ACTIVE， DOWN或ERROR。  DOWN：未绑定  ACTIVE：绑定  ERROR：异常
        :type status: str
        :param tenant_id: 项目id。
        :type tenant_id: str
        :param project_id: 项目id。
        :type project_id: str
        :param dns_name: DNS名称(目前仅广州局点支持)
        :type dns_name: str
        :param dns_domain: DNS域地址(目前仅广州局点支持)
        :type dns_domain: str
        :param created_at: 资源创建时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS
        :type created_at: datetime
        :param updated_at: 资源更新时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS
        :type updated_at: datetime
        """
        
        

        self._fixed_ip_address = None
        self._floating_ip_address = None
        self._floating_network_id = None
        self._id = None
        self._port_id = None
        self._router_id = None
        self._status = None
        self._tenant_id = None
        self._project_id = None
        self._dns_name = None
        self._dns_domain = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if fixed_ip_address is not None:
            self.fixed_ip_address = fixed_ip_address
        if floating_ip_address is not None:
            self.floating_ip_address = floating_ip_address
        if floating_network_id is not None:
            self.floating_network_id = floating_network_id
        if id is not None:
            self.id = id
        if port_id is not None:
            self.port_id = port_id
        if router_id is not None:
            self.router_id = router_id
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if project_id is not None:
            self.project_id = project_id
        if dns_name is not None:
            self.dns_name = dns_name
        if dns_domain is not None:
            self.dns_domain = dns_domain
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def fixed_ip_address(self):
        """Gets the fixed_ip_address of this FloatingIpResp.

        关联端口的私有IP地址。

        :return: The fixed_ip_address of this FloatingIpResp.
        :rtype: str
        """
        return self._fixed_ip_address

    @fixed_ip_address.setter
    def fixed_ip_address(self, fixed_ip_address):
        """Sets the fixed_ip_address of this FloatingIpResp.

        关联端口的私有IP地址。

        :param fixed_ip_address: The fixed_ip_address of this FloatingIpResp.
        :type fixed_ip_address: str
        """
        self._fixed_ip_address = fixed_ip_address

    @property
    def floating_ip_address(self):
        """Gets the floating_ip_address of this FloatingIpResp.

        浮动IP地址。

        :return: The floating_ip_address of this FloatingIpResp.
        :rtype: str
        """
        return self._floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        """Sets the floating_ip_address of this FloatingIpResp.

        浮动IP地址。

        :param floating_ip_address: The floating_ip_address of this FloatingIpResp.
        :type floating_ip_address: str
        """
        self._floating_ip_address = floating_ip_address

    @property
    def floating_network_id(self):
        """Gets the floating_network_id of this FloatingIpResp.

        外部网络的id。只能使用固定的外网，外部网络的信息请通过GET /v2.0/networks?router:external=True或GET /v2.0/networks?name={floating_network}或neutron net-external-list方式查询。

        :return: The floating_network_id of this FloatingIpResp.
        :rtype: str
        """
        return self._floating_network_id

    @floating_network_id.setter
    def floating_network_id(self, floating_network_id):
        """Sets the floating_network_id of this FloatingIpResp.

        外部网络的id。只能使用固定的外网，外部网络的信息请通过GET /v2.0/networks?router:external=True或GET /v2.0/networks?name={floating_network}或neutron net-external-list方式查询。

        :param floating_network_id: The floating_network_id of this FloatingIpResp.
        :type floating_network_id: str
        """
        self._floating_network_id = floating_network_id

    @property
    def id(self):
        """Gets the id of this FloatingIpResp.

        浮动IP地址的id。

        :return: The id of this FloatingIpResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FloatingIpResp.

        浮动IP地址的id。

        :param id: The id of this FloatingIpResp.
        :type id: str
        """
        self._id = id

    @property
    def port_id(self):
        """Gets the port_id of this FloatingIpResp.

        端口id。

        :return: The port_id of this FloatingIpResp.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this FloatingIpResp.

        端口id。

        :param port_id: The port_id of this FloatingIpResp.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def router_id(self):
        """Gets the router_id of this FloatingIpResp.

        所属路由器id。

        :return: The router_id of this FloatingIpResp.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        """Sets the router_id of this FloatingIpResp.

        所属路由器id。

        :param router_id: The router_id of this FloatingIpResp.
        :type router_id: str
        """
        self._router_id = router_id

    @property
    def status(self):
        """Gets the status of this FloatingIpResp.

        网络状态，可以为ACTIVE， DOWN或ERROR。  DOWN：未绑定  ACTIVE：绑定  ERROR：异常

        :return: The status of this FloatingIpResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FloatingIpResp.

        网络状态，可以为ACTIVE， DOWN或ERROR。  DOWN：未绑定  ACTIVE：绑定  ERROR：异常

        :param status: The status of this FloatingIpResp.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this FloatingIpResp.

        项目id。

        :return: The tenant_id of this FloatingIpResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this FloatingIpResp.

        项目id。

        :param tenant_id: The tenant_id of this FloatingIpResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this FloatingIpResp.

        项目id。

        :return: The project_id of this FloatingIpResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this FloatingIpResp.

        项目id。

        :param project_id: The project_id of this FloatingIpResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def dns_name(self):
        """Gets the dns_name of this FloatingIpResp.

        DNS名称(目前仅广州局点支持)

        :return: The dns_name of this FloatingIpResp.
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """Sets the dns_name of this FloatingIpResp.

        DNS名称(目前仅广州局点支持)

        :param dns_name: The dns_name of this FloatingIpResp.
        :type dns_name: str
        """
        self._dns_name = dns_name

    @property
    def dns_domain(self):
        """Gets the dns_domain of this FloatingIpResp.

        DNS域地址(目前仅广州局点支持)

        :return: The dns_domain of this FloatingIpResp.
        :rtype: str
        """
        return self._dns_domain

    @dns_domain.setter
    def dns_domain(self, dns_domain):
        """Sets the dns_domain of this FloatingIpResp.

        DNS域地址(目前仅广州局点支持)

        :param dns_domain: The dns_domain of this FloatingIpResp.
        :type dns_domain: str
        """
        self._dns_domain = dns_domain

    @property
    def created_at(self):
        """Gets the created_at of this FloatingIpResp.

        资源创建时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS

        :return: The created_at of this FloatingIpResp.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FloatingIpResp.

        资源创建时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS

        :param created_at: The created_at of this FloatingIpResp.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this FloatingIpResp.

        资源更新时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS

        :return: The updated_at of this FloatingIpResp.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FloatingIpResp.

        资源更新时间  采用UTC时间  格式：YYYY-MM-DDTHH:MM:SS

        :param updated_at: The updated_at of this FloatingIpResp.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, FloatingIpResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
