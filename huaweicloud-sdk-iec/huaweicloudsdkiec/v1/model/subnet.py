# coding: utf-8

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
        'cidr': 'str',
        'dns_list': 'list[str]',
        'gateway_ip': 'str',
        'dhcp_enable': 'bool',
        'primary_dns': 'str',
        'secondary_dns': 'str',
        'status': 'str',
        'vpc_id': 'str',
        'site_id': 'str',
        'site_info': 'str',
        'neutron_network_id': 'str',
        'neutron_subnet_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'cidr': 'cidr',
        'dns_list': 'dnsList',
        'gateway_ip': 'gateway_ip',
        'dhcp_enable': 'dhcp_enable',
        'primary_dns': 'primary_dns',
        'secondary_dns': 'secondary_dns',
        'status': 'status',
        'vpc_id': 'vpc_id',
        'site_id': 'site_id',
        'site_info': 'site_info',
        'neutron_network_id': 'neutron_network_id',
        'neutron_subnet_id': 'neutron_subnet_id'
    }

    def __init__(self, id=None, name=None, cidr=None, dns_list=None, gateway_ip=None, dhcp_enable=None, primary_dns=None, secondary_dns=None, status=None, vpc_id=None, site_id=None, site_info=None, neutron_network_id=None, neutron_subnet_id=None):
        """Subnet

        The model defined in huaweicloud sdk

        :param id: 子网的ID。
        :type id: str
        :param name: 子网名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param cidr: 子网的网段  取值范围：必须在vpc对应cidr范围内  约束：必须是cidr格式。掩码长度不能大于28
        :type cidr: str
        :param dns_list: 子网dns服务器地址列表
        :type dns_list: list[str]
        :param gateway_ip: 子网的网关  取值范围：子网网段中的IP地址  约束：必须是ip格式
        :type gateway_ip: str
        :param dhcp_enable: 子网是否开启dhcp功能
        :type dhcp_enable: bool
        :param primary_dns: 子网dns服务器地址1
        :type primary_dns: str
        :param secondary_dns: 子网dns服务器地址2
        :type secondary_dns: str
        :param status: 子网的状态  取值范围： - ACTIVE：表示子网已挂载到ROUTER上 - UNKNOWN：表示子网还未挂载到ROUTER上 - ERROR：表示子网状态故障
        :type status: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param site_id: 子网所属的站点ID。
        :type site_id: str
        :param site_info: 子网所属的站点信息。
        :type site_info: str
        :param neutron_network_id: 对应网络（OpenStack Neutron接口） id。
        :type neutron_network_id: str
        :param neutron_subnet_id: 对应子网（OpenStack Neutron接口） id。
        :type neutron_subnet_id: str
        """
        
        

        self._id = None
        self._name = None
        self._cidr = None
        self._dns_list = None
        self._gateway_ip = None
        self._dhcp_enable = None
        self._primary_dns = None
        self._secondary_dns = None
        self._status = None
        self._vpc_id = None
        self._site_id = None
        self._site_info = None
        self._neutron_network_id = None
        self._neutron_subnet_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if cidr is not None:
            self.cidr = cidr
        if dns_list is not None:
            self.dns_list = dns_list
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip
        if dhcp_enable is not None:
            self.dhcp_enable = dhcp_enable
        if primary_dns is not None:
            self.primary_dns = primary_dns
        if secondary_dns is not None:
            self.secondary_dns = secondary_dns
        if status is not None:
            self.status = status
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if site_id is not None:
            self.site_id = site_id
        if site_info is not None:
            self.site_info = site_info
        if neutron_network_id is not None:
            self.neutron_network_id = neutron_network_id
        if neutron_subnet_id is not None:
            self.neutron_subnet_id = neutron_subnet_id

    @property
    def id(self):
        """Gets the id of this Subnet.

        子网的ID。

        :return: The id of this Subnet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subnet.

        子网的ID。

        :param id: The id of this Subnet.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Subnet.

        子网名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this Subnet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Subnet.

        子网名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this Subnet.
        :type name: str
        """
        self._name = name

    @property
    def cidr(self):
        """Gets the cidr of this Subnet.

        子网的网段  取值范围：必须在vpc对应cidr范围内  约束：必须是cidr格式。掩码长度不能大于28

        :return: The cidr of this Subnet.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this Subnet.

        子网的网段  取值范围：必须在vpc对应cidr范围内  约束：必须是cidr格式。掩码长度不能大于28

        :param cidr: The cidr of this Subnet.
        :type cidr: str
        """
        self._cidr = cidr

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
    def gateway_ip(self):
        """Gets the gateway_ip of this Subnet.

        子网的网关  取值范围：子网网段中的IP地址  约束：必须是ip格式

        :return: The gateway_ip of this Subnet.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this Subnet.

        子网的网关  取值范围：子网网段中的IP地址  约束：必须是ip格式

        :param gateway_ip: The gateway_ip of this Subnet.
        :type gateway_ip: str
        """
        self._gateway_ip = gateway_ip

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
    def status(self):
        """Gets the status of this Subnet.

        子网的状态  取值范围： - ACTIVE：表示子网已挂载到ROUTER上 - UNKNOWN：表示子网还未挂载到ROUTER上 - ERROR：表示子网状态故障

        :return: The status of this Subnet.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Subnet.

        子网的状态  取值范围： - ACTIVE：表示子网已挂载到ROUTER上 - UNKNOWN：表示子网还未挂载到ROUTER上 - ERROR：表示子网状态故障

        :param status: The status of this Subnet.
        :type status: str
        """
        self._status = status

    @property
    def vpc_id(self):
        """Gets the vpc_id of this Subnet.

        虚拟私有云ID。

        :return: The vpc_id of this Subnet.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this Subnet.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this Subnet.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def site_id(self):
        """Gets the site_id of this Subnet.

        子网所属的站点ID。

        :return: The site_id of this Subnet.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Subnet.

        子网所属的站点ID。

        :param site_id: The site_id of this Subnet.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def site_info(self):
        """Gets the site_info of this Subnet.

        子网所属的站点信息。

        :return: The site_info of this Subnet.
        :rtype: str
        """
        return self._site_info

    @site_info.setter
    def site_info(self, site_info):
        """Sets the site_info of this Subnet.

        子网所属的站点信息。

        :param site_info: The site_info of this Subnet.
        :type site_info: str
        """
        self._site_info = site_info

    @property
    def neutron_network_id(self):
        """Gets the neutron_network_id of this Subnet.

        对应网络（OpenStack Neutron接口） id。

        :return: The neutron_network_id of this Subnet.
        :rtype: str
        """
        return self._neutron_network_id

    @neutron_network_id.setter
    def neutron_network_id(self, neutron_network_id):
        """Sets the neutron_network_id of this Subnet.

        对应网络（OpenStack Neutron接口） id。

        :param neutron_network_id: The neutron_network_id of this Subnet.
        :type neutron_network_id: str
        """
        self._neutron_network_id = neutron_network_id

    @property
    def neutron_subnet_id(self):
        """Gets the neutron_subnet_id of this Subnet.

        对应子网（OpenStack Neutron接口） id。

        :return: The neutron_subnet_id of this Subnet.
        :rtype: str
        """
        return self._neutron_subnet_id

    @neutron_subnet_id.setter
    def neutron_subnet_id(self, neutron_subnet_id):
        """Sets the neutron_subnet_id of this Subnet.

        对应子网（OpenStack Neutron接口） id。

        :param neutron_subnet_id: The neutron_subnet_id of this Subnet.
        :type neutron_subnet_id: str
        """
        self._neutron_subnet_id = neutron_subnet_id

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
