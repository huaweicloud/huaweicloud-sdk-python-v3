# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Port:

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
        'status': 'str',
        'admin_state_up': 'bool',
        'fixed_ips': 'list[FixedIp]',
        'mac_address': 'str',
        'network_id': 'str',
        'device_id': 'str',
        'device_owner': 'str',
        'security_groups': 'list[str]',
        'extra_dhcp_opts': 'list[ExtraDhcpOption]',
        'allowed_address_pairs': 'list[AllowedAddressPair]',
        'site_id': 'str',
        'dns_assignment': 'list[DnsAssignment]',
        'dns_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'admin_state_up': 'admin_state_up',
        'fixed_ips': 'fixed_ips',
        'mac_address': 'mac_address',
        'network_id': 'network_id',
        'device_id': 'device_id',
        'device_owner': 'device_owner',
        'security_groups': 'security_groups',
        'extra_dhcp_opts': 'extra_dhcp_opts',
        'allowed_address_pairs': 'allowed_address_pairs',
        'site_id': 'site_id',
        'dns_assignment': 'dns_assignment',
        'dns_name': 'dns_name'
    }

    def __init__(self, id=None, name=None, status=None, admin_state_up=None, fixed_ips=None, mac_address=None, network_id=None, device_id=None, device_owner=None, security_groups=None, extra_dhcp_opts=None, allowed_address_pairs=None, site_id=None, dns_assignment=None, dns_name=None):
        """Port

        The model defined in huaweicloud sdk

        :param id: 端口唯一标识
        :type id: str
        :param name: 端口名称  取值：默认为空，最大长度不超过255
        :type name: str
        :param status: 端口状态，Hana硬直通虚拟机端口状态总为DOWN  取值范围：ACTIVE、BUILD、DOWN
        :type status: str
        :param admin_state_up: 管理状态  约束：只支持true，默认为true
        :type admin_state_up: bool
        :param fixed_ips: 端口IP。  约束：一个端口只支持一个fixed_ip，且不支持更新。
        :type fixed_ips: list[:class:`huaweicloudsdkiec.v1.FixedIp`]
        :param mac_address: 端口MAC地址  约束：由系统分配，不支持指定
        :type mac_address: str
        :param network_id: 端口所属网络的ID  约束：必须是存在的网络ID
        :type network_id: str
        :param device_id: 端口所属设备ID  约束：不支持设置和更新，由系统自动维护
        :type device_id: str
        :param device_owner: 设备所属（DHCP/Router/ lb/Nova）  约束：不支持设置和更新，由系统自动维护 
        :type device_owner: str
        :param security_groups: 安全组的UUID(扩展属性)
        :type security_groups: list[str]
        :param extra_dhcp_opts: DHCP的扩展属性。
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkiec.v1.ExtraDhcpOption`]
        :param allowed_address_pairs: IP/Mac对列表。  约束：IP地址不允许为 “0.0.0.0/0”  建议：如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。
        :type allowed_address_pairs: list[:class:`huaweicloudsdkiec.v1.AllowedAddressPair`]
        :param site_id: 站点ID
        :type site_id: str
        :param dns_assignment: 主网卡默认内网域名信息  约束：不支持设置和更新，由系统自动维护
        :type dns_assignment: list[:class:`huaweicloudsdkiec.v1.DnsAssignment`]
        :param dns_name: 主网卡默认内网DNS名称  约束：不支持设置和更新，由系统自动维护
        :type dns_name: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._admin_state_up = None
        self._fixed_ips = None
        self._mac_address = None
        self._network_id = None
        self._device_id = None
        self._device_owner = None
        self._security_groups = None
        self._extra_dhcp_opts = None
        self._allowed_address_pairs = None
        self._site_id = None
        self._dns_assignment = None
        self._dns_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
        if mac_address is not None:
            self.mac_address = mac_address
        if network_id is not None:
            self.network_id = network_id
        if device_id is not None:
            self.device_id = device_id
        if device_owner is not None:
            self.device_owner = device_owner
        if security_groups is not None:
            self.security_groups = security_groups
        if extra_dhcp_opts is not None:
            self.extra_dhcp_opts = extra_dhcp_opts
        if allowed_address_pairs is not None:
            self.allowed_address_pairs = allowed_address_pairs
        if site_id is not None:
            self.site_id = site_id
        if dns_assignment is not None:
            self.dns_assignment = dns_assignment
        if dns_name is not None:
            self.dns_name = dns_name

    @property
    def id(self):
        """Gets the id of this Port.

        端口唯一标识

        :return: The id of this Port.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Port.

        端口唯一标识

        :param id: The id of this Port.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Port.

        端口名称  取值：默认为空，最大长度不超过255

        :return: The name of this Port.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Port.

        端口名称  取值：默认为空，最大长度不超过255

        :param name: The name of this Port.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this Port.

        端口状态，Hana硬直通虚拟机端口状态总为DOWN  取值范围：ACTIVE、BUILD、DOWN

        :return: The status of this Port.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Port.

        端口状态，Hana硬直通虚拟机端口状态总为DOWN  取值范围：ACTIVE、BUILD、DOWN

        :param status: The status of this Port.
        :type status: str
        """
        self._status = status

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this Port.

        管理状态  约束：只支持true，默认为true

        :return: The admin_state_up of this Port.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this Port.

        管理状态  约束：只支持true，默认为true

        :param admin_state_up: The admin_state_up of this Port.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this Port.

        端口IP。  约束：一个端口只支持一个fixed_ip，且不支持更新。

        :return: The fixed_ips of this Port.
        :rtype: list[:class:`huaweicloudsdkiec.v1.FixedIp`]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this Port.

        端口IP。  约束：一个端口只支持一个fixed_ip，且不支持更新。

        :param fixed_ips: The fixed_ips of this Port.
        :type fixed_ips: list[:class:`huaweicloudsdkiec.v1.FixedIp`]
        """
        self._fixed_ips = fixed_ips

    @property
    def mac_address(self):
        """Gets the mac_address of this Port.

        端口MAC地址  约束：由系统分配，不支持指定

        :return: The mac_address of this Port.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this Port.

        端口MAC地址  约束：由系统分配，不支持指定

        :param mac_address: The mac_address of this Port.
        :type mac_address: str
        """
        self._mac_address = mac_address

    @property
    def network_id(self):
        """Gets the network_id of this Port.

        端口所属网络的ID  约束：必须是存在的网络ID

        :return: The network_id of this Port.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this Port.

        端口所属网络的ID  约束：必须是存在的网络ID

        :param network_id: The network_id of this Port.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def device_id(self):
        """Gets the device_id of this Port.

        端口所属设备ID  约束：不支持设置和更新，由系统自动维护

        :return: The device_id of this Port.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Port.

        端口所属设备ID  约束：不支持设置和更新，由系统自动维护

        :param device_id: The device_id of this Port.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_owner(self):
        """Gets the device_owner of this Port.

        设备所属（DHCP/Router/ lb/Nova）  约束：不支持设置和更新，由系统自动维护 

        :return: The device_owner of this Port.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this Port.

        设备所属（DHCP/Router/ lb/Nova）  约束：不支持设置和更新，由系统自动维护 

        :param device_owner: The device_owner of this Port.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def security_groups(self):
        """Gets the security_groups of this Port.

        安全组的UUID(扩展属性)

        :return: The security_groups of this Port.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this Port.

        安全组的UUID(扩展属性)

        :param security_groups: The security_groups of this Port.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def extra_dhcp_opts(self):
        """Gets the extra_dhcp_opts of this Port.

        DHCP的扩展属性。

        :return: The extra_dhcp_opts of this Port.
        :rtype: list[:class:`huaweicloudsdkiec.v1.ExtraDhcpOption`]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        """Sets the extra_dhcp_opts of this Port.

        DHCP的扩展属性。

        :param extra_dhcp_opts: The extra_dhcp_opts of this Port.
        :type extra_dhcp_opts: list[:class:`huaweicloudsdkiec.v1.ExtraDhcpOption`]
        """
        self._extra_dhcp_opts = extra_dhcp_opts

    @property
    def allowed_address_pairs(self):
        """Gets the allowed_address_pairs of this Port.

        IP/Mac对列表。  约束：IP地址不允许为 “0.0.0.0/0”  建议：如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。

        :return: The allowed_address_pairs of this Port.
        :rtype: list[:class:`huaweicloudsdkiec.v1.AllowedAddressPair`]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        """Sets the allowed_address_pairs of this Port.

        IP/Mac对列表。  约束：IP地址不允许为 “0.0.0.0/0”  建议：如果allowed_address_pairs配置地址池较大的CIDR（掩码小于24位），建议为该port配置一个单独的安全组。

        :param allowed_address_pairs: The allowed_address_pairs of this Port.
        :type allowed_address_pairs: list[:class:`huaweicloudsdkiec.v1.AllowedAddressPair`]
        """
        self._allowed_address_pairs = allowed_address_pairs

    @property
    def site_id(self):
        """Gets the site_id of this Port.

        站点ID

        :return: The site_id of this Port.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Port.

        站点ID

        :param site_id: The site_id of this Port.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def dns_assignment(self):
        """Gets the dns_assignment of this Port.

        主网卡默认内网域名信息  约束：不支持设置和更新，由系统自动维护

        :return: The dns_assignment of this Port.
        :rtype: list[:class:`huaweicloudsdkiec.v1.DnsAssignment`]
        """
        return self._dns_assignment

    @dns_assignment.setter
    def dns_assignment(self, dns_assignment):
        """Sets the dns_assignment of this Port.

        主网卡默认内网域名信息  约束：不支持设置和更新，由系统自动维护

        :param dns_assignment: The dns_assignment of this Port.
        :type dns_assignment: list[:class:`huaweicloudsdkiec.v1.DnsAssignment`]
        """
        self._dns_assignment = dns_assignment

    @property
    def dns_name(self):
        """Gets the dns_name of this Port.

        主网卡默认内网DNS名称  约束：不支持设置和更新，由系统自动维护

        :return: The dns_name of this Port.
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """Sets the dns_name of this Port.

        主网卡默认内网DNS名称  约束：不支持设置和更新，由系统自动维护

        :param dns_name: The dns_name of this Port.
        :type dns_name: str
        """
        self._dns_name = dns_name

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
        if not isinstance(other, Port):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
