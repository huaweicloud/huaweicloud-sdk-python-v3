# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronNetwork:

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
        'status': 'str',
        'name': 'str',
        'subnets': 'list[str]',
        'routerexternal': 'bool',
        'admin_state_up': 'bool',
        'shared': 'bool',
        'tenant_id': 'str',
        'providernetwork_type': 'str',
        'availability_zone_hints': 'list[str]',
        'availability_zones': 'list[str]',
        'port_security_enabled': 'bool',
        'dns_domain': 'str',
        'project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'name': 'name',
        'subnets': 'subnets',
        'routerexternal': 'router:external',
        'admin_state_up': 'admin_state_up',
        'shared': 'shared',
        'tenant_id': 'tenant_id',
        'providernetwork_type': 'provider:network_type',
        'availability_zone_hints': 'availability_zone_hints',
        'availability_zones': 'availability_zones',
        'port_security_enabled': 'port_security_enabled',
        'dns_domain': 'dns_domain',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, status=None, name=None, subnets=None, routerexternal=None, admin_state_up=None, shared=None, tenant_id=None, providernetwork_type=None, availability_zone_hints=None, availability_zones=None, port_security_enabled=None, dns_domain=None, project_id=None, created_at=None, updated_at=None):
        """NeutronNetwork

        The model defined in huaweicloud sdk

        :param id: 网络ID
        :type id: str
        :param status: 功能说明：网络状态 取值范围：ACTIVE，DOWN，BUILD或ERROR
        :type status: str
        :param name: 功能说明：网络名称 取值范围：0-255个字符
        :type name: str
        :param subnets: 功能说明：网络关联的子网ID列表 约束：一个network仅支持关联一个 subnet。
        :type subnets: list[str]
        :param routerexternal: 功能说明：扩展属性，是否外部网络 取值范围：true、false 约束：不支持设置和更新
        :type routerexternal: bool
        :param admin_state_up: 功能说明：资源的管理状态 取值范围：true、false 约束：只支持true
        :type admin_state_up: bool
        :param shared: 功能说明：是否支持跨租户共享此资源 取值范围：true(共享)、false(非共享) 约束：不支持设置和更新
        :type shared: bool
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param providernetwork_type: 功能说明：扩展属性，网络类型（支持vxlan, geneve） 取值范围：vxlan，geneve
        :type providernetwork_type: str
        :param availability_zone_hints: 功能说明：本网络的候选可用域
        :type availability_zone_hints: list[str]
        :param availability_zones: 功能说明：本网络的可用域。 取值范围：当前region下的可用域
        :type availability_zones: list[str]
        :param port_security_enabled: 功能说明：端口安全使能标记 取值范围：true（启用）、false（禁用） 约束：如果不使能，则network下所有虚机的安全组和dhcp防欺骗不生效
        :type port_security_enabled: bool
        :param dns_domain: 功能说明：默认内网DNS域地址 约束：系统自动生成维护，不支持设置和更新
        :type dns_domain: str
        :param project_id: 项目ID
        :type project_id: str
        :param created_at: 功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._status = None
        self._name = None
        self._subnets = None
        self._routerexternal = None
        self._admin_state_up = None
        self._shared = None
        self._tenant_id = None
        self._providernetwork_type = None
        self._availability_zone_hints = None
        self._availability_zones = None
        self._port_security_enabled = None
        self._dns_domain = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.name = name
        self.subnets = subnets
        self.routerexternal = routerexternal
        self.admin_state_up = admin_state_up
        self.shared = shared
        self.tenant_id = tenant_id
        self.providernetwork_type = providernetwork_type
        self.availability_zone_hints = availability_zone_hints
        self.availability_zones = availability_zones
        self.port_security_enabled = port_security_enabled
        self.dns_domain = dns_domain
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this NeutronNetwork.

        网络ID

        :return: The id of this NeutronNetwork.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronNetwork.

        网络ID

        :param id: The id of this NeutronNetwork.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this NeutronNetwork.

        功能说明：网络状态 取值范围：ACTIVE，DOWN，BUILD或ERROR

        :return: The status of this NeutronNetwork.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NeutronNetwork.

        功能说明：网络状态 取值范围：ACTIVE，DOWN，BUILD或ERROR

        :param status: The status of this NeutronNetwork.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this NeutronNetwork.

        功能说明：网络名称 取值范围：0-255个字符

        :return: The name of this NeutronNetwork.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronNetwork.

        功能说明：网络名称 取值范围：0-255个字符

        :param name: The name of this NeutronNetwork.
        :type name: str
        """
        self._name = name

    @property
    def subnets(self):
        """Gets the subnets of this NeutronNetwork.

        功能说明：网络关联的子网ID列表 约束：一个network仅支持关联一个 subnet。

        :return: The subnets of this NeutronNetwork.
        :rtype: list[str]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this NeutronNetwork.

        功能说明：网络关联的子网ID列表 约束：一个network仅支持关联一个 subnet。

        :param subnets: The subnets of this NeutronNetwork.
        :type subnets: list[str]
        """
        self._subnets = subnets

    @property
    def routerexternal(self):
        """Gets the routerexternal of this NeutronNetwork.

        功能说明：扩展属性，是否外部网络 取值范围：true、false 约束：不支持设置和更新

        :return: The routerexternal of this NeutronNetwork.
        :rtype: bool
        """
        return self._routerexternal

    @routerexternal.setter
    def routerexternal(self, routerexternal):
        """Sets the routerexternal of this NeutronNetwork.

        功能说明：扩展属性，是否外部网络 取值范围：true、false 约束：不支持设置和更新

        :param routerexternal: The routerexternal of this NeutronNetwork.
        :type routerexternal: bool
        """
        self._routerexternal = routerexternal

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this NeutronNetwork.

        功能说明：资源的管理状态 取值范围：true、false 约束：只支持true

        :return: The admin_state_up of this NeutronNetwork.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this NeutronNetwork.

        功能说明：资源的管理状态 取值范围：true、false 约束：只支持true

        :param admin_state_up: The admin_state_up of this NeutronNetwork.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def shared(self):
        """Gets the shared of this NeutronNetwork.

        功能说明：是否支持跨租户共享此资源 取值范围：true(共享)、false(非共享) 约束：不支持设置和更新

        :return: The shared of this NeutronNetwork.
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this NeutronNetwork.

        功能说明：是否支持跨租户共享此资源 取值范围：true(共享)、false(非共享) 约束：不支持设置和更新

        :param shared: The shared of this NeutronNetwork.
        :type shared: bool
        """
        self._shared = shared

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronNetwork.

        项目ID

        :return: The tenant_id of this NeutronNetwork.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronNetwork.

        项目ID

        :param tenant_id: The tenant_id of this NeutronNetwork.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def providernetwork_type(self):
        """Gets the providernetwork_type of this NeutronNetwork.

        功能说明：扩展属性，网络类型（支持vxlan, geneve） 取值范围：vxlan，geneve

        :return: The providernetwork_type of this NeutronNetwork.
        :rtype: str
        """
        return self._providernetwork_type

    @providernetwork_type.setter
    def providernetwork_type(self, providernetwork_type):
        """Sets the providernetwork_type of this NeutronNetwork.

        功能说明：扩展属性，网络类型（支持vxlan, geneve） 取值范围：vxlan，geneve

        :param providernetwork_type: The providernetwork_type of this NeutronNetwork.
        :type providernetwork_type: str
        """
        self._providernetwork_type = providernetwork_type

    @property
    def availability_zone_hints(self):
        """Gets the availability_zone_hints of this NeutronNetwork.

        功能说明：本网络的候选可用域

        :return: The availability_zone_hints of this NeutronNetwork.
        :rtype: list[str]
        """
        return self._availability_zone_hints

    @availability_zone_hints.setter
    def availability_zone_hints(self, availability_zone_hints):
        """Sets the availability_zone_hints of this NeutronNetwork.

        功能说明：本网络的候选可用域

        :param availability_zone_hints: The availability_zone_hints of this NeutronNetwork.
        :type availability_zone_hints: list[str]
        """
        self._availability_zone_hints = availability_zone_hints

    @property
    def availability_zones(self):
        """Gets the availability_zones of this NeutronNetwork.

        功能说明：本网络的可用域。 取值范围：当前region下的可用域

        :return: The availability_zones of this NeutronNetwork.
        :rtype: list[str]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        """Sets the availability_zones of this NeutronNetwork.

        功能说明：本网络的可用域。 取值范围：当前region下的可用域

        :param availability_zones: The availability_zones of this NeutronNetwork.
        :type availability_zones: list[str]
        """
        self._availability_zones = availability_zones

    @property
    def port_security_enabled(self):
        """Gets the port_security_enabled of this NeutronNetwork.

        功能说明：端口安全使能标记 取值范围：true（启用）、false（禁用） 约束：如果不使能，则network下所有虚机的安全组和dhcp防欺骗不生效

        :return: The port_security_enabled of this NeutronNetwork.
        :rtype: bool
        """
        return self._port_security_enabled

    @port_security_enabled.setter
    def port_security_enabled(self, port_security_enabled):
        """Sets the port_security_enabled of this NeutronNetwork.

        功能说明：端口安全使能标记 取值范围：true（启用）、false（禁用） 约束：如果不使能，则network下所有虚机的安全组和dhcp防欺骗不生效

        :param port_security_enabled: The port_security_enabled of this NeutronNetwork.
        :type port_security_enabled: bool
        """
        self._port_security_enabled = port_security_enabled

    @property
    def dns_domain(self):
        """Gets the dns_domain of this NeutronNetwork.

        功能说明：默认内网DNS域地址 约束：系统自动生成维护，不支持设置和更新

        :return: The dns_domain of this NeutronNetwork.
        :rtype: str
        """
        return self._dns_domain

    @dns_domain.setter
    def dns_domain(self, dns_domain):
        """Sets the dns_domain of this NeutronNetwork.

        功能说明：默认内网DNS域地址 约束：系统自动生成维护，不支持设置和更新

        :param dns_domain: The dns_domain of this NeutronNetwork.
        :type dns_domain: str
        """
        self._dns_domain = dns_domain

    @property
    def project_id(self):
        """Gets the project_id of this NeutronNetwork.

        项目ID

        :return: The project_id of this NeutronNetwork.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NeutronNetwork.

        项目ID

        :param project_id: The project_id of this NeutronNetwork.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this NeutronNetwork.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this NeutronNetwork.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NeutronNetwork.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this NeutronNetwork.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NeutronNetwork.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this NeutronNetwork.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NeutronNetwork.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this NeutronNetwork.
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
        if not isinstance(other, NeutronNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
