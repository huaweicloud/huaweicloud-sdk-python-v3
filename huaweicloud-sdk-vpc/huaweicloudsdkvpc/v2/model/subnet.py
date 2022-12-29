# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Subnet:

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
        'name': 'str',
        'description': 'str',
        'cidr': 'str',
        'gateway_ip': 'str',
        'ipv6_enable': 'bool',
        'cidr_v6': 'str',
        'gateway_ip_v6': 'str',
        'dhcp_enable': 'bool',
        'primary_dns': 'str',
        'secondary_dns': 'str',
        'dns_list': 'list[str]',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'status': 'str',
        'neutron_network_id': 'str',
        'neutron_subnet_id': 'str',
        'neutron_subnet_id_v6': 'str',
        'extra_dhcp_opts': 'list[ExtraDhcpOption]',
        'scope': 'str',
        'tenant_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'cidr': 'cidr',
        'gateway_ip': 'gateway_ip',
        'ipv6_enable': 'ipv6_enable',
        'cidr_v6': 'cidr_v6',
        'gateway_ip_v6': 'gateway_ip_v6',
        'dhcp_enable': 'dhcp_enable',
        'primary_dns': 'primary_dns',
        'secondary_dns': 'secondary_dns',
        'dns_list': 'dnsList',
        'availability_zone': 'availability_zone',
        'vpc_id': 'vpc_id',
        'status': 'status',
        'neutron_network_id': 'neutron_network_id',
        'neutron_subnet_id': 'neutron_subnet_id',
        'neutron_subnet_id_v6': 'neutron_subnet_id_v6',
        'extra_dhcp_opts': 'extra_dhcp_opts',
        'scope': 'scope',
        'tenant_id': 'tenant_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, cidr=None, gateway_ip=None, ipv6_enable=None, cidr_v6=None, gateway_ip_v6=None, dhcp_enable=None, primary_dns=None, secondary_dns=None, dns_list=None, availability_zone=None, vpc_id=None, status=None, neutron_network_id=None, neutron_subnet_id=None, neutron_subnet_id_v6=None, extra_dhcp_opts=None, scope=None, tenant_id=None, created_at=None, updated_at=None):
        """Subnet

        The model defined in huaweicloud sdk

        :param id: 子网ID
        :type id: str
        :param name: 功能说明：子网名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：子网描述 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param cidr: 功能说明：子网的网段 取值范围：必须在vpc对应cidr范围内 约束：必须是cidr格式。掩码长度不能大于28
        :type cidr: str
        :param gateway_ip: 功能说明：子网的网关 取值范围：子网网段中的IP地址 约束：必须是ip格式
        :type gateway_ip: str
        :param ipv6_enable: 功能说明：是否创建cidr_v6 取值范围：true（开启），false（关闭）
        :type ipv6_enable: bool
        :param cidr_v6: IPv6子网的网段，如果子网为IPv4子网，则不返回此参数
        :type cidr_v6: str
        :param gateway_ip_v6: IPv6子网的网关，如果子网为IPv4子网，则不返回此参数
        :type gateway_ip_v6: str
        :param dhcp_enable: 子网是否开启dhcp功能
        :type dhcp_enable: bool
        :param primary_dns: 子网dns服务器地址1
        :type primary_dns: str
        :param secondary_dns: 子网dns服务器地址2
        :type secondary_dns: str
        :param dns_list: 子网dns服务器地址列表
        :type dns_list: list[str]
        :param availability_zone: 子网所在的可用区标识
        :type availability_zone: str
        :param vpc_id: 子网所在VPC标识
        :type vpc_id: str
        :param status: 功能说明：子网的状态 取值范围： - ACTIVE：表示子网已挂载到ROUTER上 - UNKNOWN：表示子网还未挂载到ROUTER上 - ERROR：表示子网状态故障
        :type status: str
        :param neutron_network_id: 对应网络（OpenStack Neutron接口）id
        :type neutron_network_id: str
        :param neutron_subnet_id: 对应子网（OpenStack Neutron接口）id
        :type neutron_subnet_id: str
        :param neutron_subnet_id_v6: 对应IPv6子网（OpenStack Neutron接口）id，如果子网为IPv4子网，则不返回此参数
        :type neutron_subnet_id_v6: str
        :param extra_dhcp_opts: 子网配置的NTP地址或DHCP租约时间
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOption`]
        :param scope: 功能说明：子网作用域 取值范围：center-表示作用域为中心；{azId}表示作用域为具体的AZ
        :type scope: str
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param created_at: 功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._cidr = None
        self._gateway_ip = None
        self._ipv6_enable = None
        self._cidr_v6 = None
        self._gateway_ip_v6 = None
        self._dhcp_enable = None
        self._primary_dns = None
        self._secondary_dns = None
        self._dns_list = None
        self._availability_zone = None
        self._vpc_id = None
        self._status = None
        self._neutron_network_id = None
        self._neutron_subnet_id = None
        self._neutron_subnet_id_v6 = None
        self._extra_dhcp_opts = None
        self._scope = None
        self._tenant_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.cidr = cidr
        self.gateway_ip = gateway_ip
        self.ipv6_enable = ipv6_enable
        self.cidr_v6 = cidr_v6
        self.gateway_ip_v6 = gateway_ip_v6
        self.dhcp_enable = dhcp_enable
        self.primary_dns = primary_dns
        self.secondary_dns = secondary_dns
        self.dns_list = dns_list
        self.availability_zone = availability_zone
        self.vpc_id = vpc_id
        self.status = status
        self.neutron_network_id = neutron_network_id
        self.neutron_subnet_id = neutron_subnet_id
        self.neutron_subnet_id_v6 = neutron_subnet_id_v6
        self.extra_dhcp_opts = extra_dhcp_opts
        if scope is not None:
            self.scope = scope
        self.tenant_id = tenant_id
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Subnet.

        子网ID

        :return: The id of this Subnet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subnet.

        子网ID

        :param id: The id of this Subnet.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Subnet.

        功能说明：子网名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this Subnet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Subnet.

        功能说明：子网名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this Subnet.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Subnet.

        功能说明：子网描述 取值范围：0-255个字符，不能包含“<”和“>”。

        :return: The description of this Subnet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Subnet.

        功能说明：子网描述 取值范围：0-255个字符，不能包含“<”和“>”。

        :param description: The description of this Subnet.
        :type description: str
        """
        self._description = description

    @property
    def cidr(self):
        """Gets the cidr of this Subnet.

        功能说明：子网的网段 取值范围：必须在vpc对应cidr范围内 约束：必须是cidr格式。掩码长度不能大于28

        :return: The cidr of this Subnet.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this Subnet.

        功能说明：子网的网段 取值范围：必须在vpc对应cidr范围内 约束：必须是cidr格式。掩码长度不能大于28

        :param cidr: The cidr of this Subnet.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this Subnet.

        功能说明：子网的网关 取值范围：子网网段中的IP地址 约束：必须是ip格式

        :return: The gateway_ip of this Subnet.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this Subnet.

        功能说明：子网的网关 取值范围：子网网段中的IP地址 约束：必须是ip格式

        :param gateway_ip: The gateway_ip of this Subnet.
        :type gateway_ip: str
        """
        self._gateway_ip = gateway_ip

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this Subnet.

        功能说明：是否创建cidr_v6 取值范围：true（开启），false（关闭）

        :return: The ipv6_enable of this Subnet.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this Subnet.

        功能说明：是否创建cidr_v6 取值范围：true（开启），false（关闭）

        :param ipv6_enable: The ipv6_enable of this Subnet.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def cidr_v6(self):
        """Gets the cidr_v6 of this Subnet.

        IPv6子网的网段，如果子网为IPv4子网，则不返回此参数

        :return: The cidr_v6 of this Subnet.
        :rtype: str
        """
        return self._cidr_v6

    @cidr_v6.setter
    def cidr_v6(self, cidr_v6):
        """Sets the cidr_v6 of this Subnet.

        IPv6子网的网段，如果子网为IPv4子网，则不返回此参数

        :param cidr_v6: The cidr_v6 of this Subnet.
        :type cidr_v6: str
        """
        self._cidr_v6 = cidr_v6

    @property
    def gateway_ip_v6(self):
        """Gets the gateway_ip_v6 of this Subnet.

        IPv6子网的网关，如果子网为IPv4子网，则不返回此参数

        :return: The gateway_ip_v6 of this Subnet.
        :rtype: str
        """
        return self._gateway_ip_v6

    @gateway_ip_v6.setter
    def gateway_ip_v6(self, gateway_ip_v6):
        """Sets the gateway_ip_v6 of this Subnet.

        IPv6子网的网关，如果子网为IPv4子网，则不返回此参数

        :param gateway_ip_v6: The gateway_ip_v6 of this Subnet.
        :type gateway_ip_v6: str
        """
        self._gateway_ip_v6 = gateway_ip_v6

    @property
    def dhcp_enable(self):
        """Gets the dhcp_enable of this Subnet.

        子网是否开启dhcp功能

        :return: The dhcp_enable of this Subnet.
        :rtype: bool
        """
        return self._dhcp_enable

    @dhcp_enable.setter
    def dhcp_enable(self, dhcp_enable):
        """Sets the dhcp_enable of this Subnet.

        子网是否开启dhcp功能

        :param dhcp_enable: The dhcp_enable of this Subnet.
        :type dhcp_enable: bool
        """
        self._dhcp_enable = dhcp_enable

    @property
    def primary_dns(self):
        """Gets the primary_dns of this Subnet.

        子网dns服务器地址1

        :return: The primary_dns of this Subnet.
        :rtype: str
        """
        return self._primary_dns

    @primary_dns.setter
    def primary_dns(self, primary_dns):
        """Sets the primary_dns of this Subnet.

        子网dns服务器地址1

        :param primary_dns: The primary_dns of this Subnet.
        :type primary_dns: str
        """
        self._primary_dns = primary_dns

    @property
    def secondary_dns(self):
        """Gets the secondary_dns of this Subnet.

        子网dns服务器地址2

        :return: The secondary_dns of this Subnet.
        :rtype: str
        """
        return self._secondary_dns

    @secondary_dns.setter
    def secondary_dns(self, secondary_dns):
        """Sets the secondary_dns of this Subnet.

        子网dns服务器地址2

        :param secondary_dns: The secondary_dns of this Subnet.
        :type secondary_dns: str
        """
        self._secondary_dns = secondary_dns

    @property
    def dns_list(self):
        """Gets the dns_list of this Subnet.

        子网dns服务器地址列表

        :return: The dns_list of this Subnet.
        :rtype: list[str]
        """
        return self._dns_list

    @dns_list.setter
    def dns_list(self, dns_list):
        """Sets the dns_list of this Subnet.

        子网dns服务器地址列表

        :param dns_list: The dns_list of this Subnet.
        :type dns_list: list[str]
        """
        self._dns_list = dns_list

    @property
    def availability_zone(self):
        """Gets the availability_zone of this Subnet.

        子网所在的可用区标识

        :return: The availability_zone of this Subnet.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this Subnet.

        子网所在的可用区标识

        :param availability_zone: The availability_zone of this Subnet.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this Subnet.

        子网所在VPC标识

        :return: The vpc_id of this Subnet.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this Subnet.

        子网所在VPC标识

        :param vpc_id: The vpc_id of this Subnet.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def status(self):
        """Gets the status of this Subnet.

        功能说明：子网的状态 取值范围： - ACTIVE：表示子网已挂载到ROUTER上 - UNKNOWN：表示子网还未挂载到ROUTER上 - ERROR：表示子网状态故障

        :return: The status of this Subnet.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Subnet.

        功能说明：子网的状态 取值范围： - ACTIVE：表示子网已挂载到ROUTER上 - UNKNOWN：表示子网还未挂载到ROUTER上 - ERROR：表示子网状态故障

        :param status: The status of this Subnet.
        :type status: str
        """
        self._status = status

    @property
    def neutron_network_id(self):
        """Gets the neutron_network_id of this Subnet.

        对应网络（OpenStack Neutron接口）id

        :return: The neutron_network_id of this Subnet.
        :rtype: str
        """
        return self._neutron_network_id

    @neutron_network_id.setter
    def neutron_network_id(self, neutron_network_id):
        """Sets the neutron_network_id of this Subnet.

        对应网络（OpenStack Neutron接口）id

        :param neutron_network_id: The neutron_network_id of this Subnet.
        :type neutron_network_id: str
        """
        self._neutron_network_id = neutron_network_id

    @property
    def neutron_subnet_id(self):
        """Gets the neutron_subnet_id of this Subnet.

        对应子网（OpenStack Neutron接口）id

        :return: The neutron_subnet_id of this Subnet.
        :rtype: str
        """
        return self._neutron_subnet_id

    @neutron_subnet_id.setter
    def neutron_subnet_id(self, neutron_subnet_id):
        """Sets the neutron_subnet_id of this Subnet.

        对应子网（OpenStack Neutron接口）id

        :param neutron_subnet_id: The neutron_subnet_id of this Subnet.
        :type neutron_subnet_id: str
        """
        self._neutron_subnet_id = neutron_subnet_id

    @property
    def neutron_subnet_id_v6(self):
        """Gets the neutron_subnet_id_v6 of this Subnet.

        对应IPv6子网（OpenStack Neutron接口）id，如果子网为IPv4子网，则不返回此参数

        :return: The neutron_subnet_id_v6 of this Subnet.
        :rtype: str
        """
        return self._neutron_subnet_id_v6

    @neutron_subnet_id_v6.setter
    def neutron_subnet_id_v6(self, neutron_subnet_id_v6):
        """Sets the neutron_subnet_id_v6 of this Subnet.

        对应IPv6子网（OpenStack Neutron接口）id，如果子网为IPv4子网，则不返回此参数

        :param neutron_subnet_id_v6: The neutron_subnet_id_v6 of this Subnet.
        :type neutron_subnet_id_v6: str
        """
        self._neutron_subnet_id_v6 = neutron_subnet_id_v6

    @property
    def extra_dhcp_opts(self):
        """Gets the extra_dhcp_opts of this Subnet.

        子网配置的NTP地址或DHCP租约时间

        :return: The extra_dhcp_opts of this Subnet.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOption`]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        """Sets the extra_dhcp_opts of this Subnet.

        子网配置的NTP地址或DHCP租约时间

        :param extra_dhcp_opts: The extra_dhcp_opts of this Subnet.
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkvpc.v2.ExtraDhcpOption`]
        """
        self._extra_dhcp_opts = extra_dhcp_opts

    @property
    def scope(self):
        """Gets the scope of this Subnet.

        功能说明：子网作用域 取值范围：center-表示作用域为中心；{azId}表示作用域为具体的AZ

        :return: The scope of this Subnet.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Subnet.

        功能说明：子网作用域 取值范围：center-表示作用域为中心；{azId}表示作用域为具体的AZ

        :param scope: The scope of this Subnet.
        :type scope: str
        """
        self._scope = scope

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Subnet.

        项目ID

        :return: The tenant_id of this Subnet.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Subnet.

        项目ID

        :param tenant_id: The tenant_id of this Subnet.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def created_at(self):
        """Gets the created_at of this Subnet.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this Subnet.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Subnet.

        功能说明：资源创建UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this Subnet.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Subnet.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this Subnet.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Subnet.

        功能说明：资源更新UTC时间 格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this Subnet.
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
        if not isinstance(other, Subnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
