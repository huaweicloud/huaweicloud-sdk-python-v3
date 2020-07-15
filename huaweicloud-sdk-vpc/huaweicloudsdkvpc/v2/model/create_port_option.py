# coding: utf-8

import pprint
import re

import six





class CreatePortOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'network_id': 'str',
        'fixed_ips': 'list[FixedIp]',
        'device_owner': 'str',
        'security_groups': 'list[str]',
        'admin_state_up': 'bool',
        'allowed_address_pairs': 'list[AllowedAddressPair]',
        'extra_dhcp_opts': 'list[ExtraDhcpOpt]',
        'tenant_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'network_id': 'network_id',
        'fixed_ips': 'fixed_ips',
        'device_owner': 'device_owner',
        'security_groups': 'security_groups',
        'admin_state_up': 'admin_state_up',
        'allowed_address_pairs': 'allowed_address_pairs',
        'extra_dhcp_opts': 'extra_dhcp_opts',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, name=None, network_id=None, fixed_ips=None, device_owner=None, security_groups=None, admin_state_up=None, allowed_address_pairs=None, extra_dhcp_opts=None, tenant_id=None):
        """CreatePortOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._network_id = None
        self._fixed_ips = None
        self._device_owner = None
        self._security_groups = None
        self._admin_state_up = None
        self._allowed_address_pairs = None
        self._extra_dhcp_opts = None
        self._tenant_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.network_id = network_id
        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
        if device_owner is not None:
            self.device_owner = device_owner
        if security_groups is not None:
            self.security_groups = security_groups
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if allowed_address_pairs is not None:
            self.allowed_address_pairs = allowed_address_pairs
        if extra_dhcp_opts is not None:
            self.extra_dhcp_opts = extra_dhcp_opts
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this CreatePortOption.

        功能说明：端口名称 取值范围：0~255个字符，支持中文、英文、字母、_(下划线)、-（中划线），默认为空

        :return: The name of this CreatePortOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePortOption.

        功能说明：端口名称 取值范围：0~255个字符，支持中文、英文、字母、_(下划线)、-（中划线），默认为空

        :param name: The name of this CreatePortOption.
        :type: str
        """
        self._name = name

    @property
    def network_id(self):
        """Gets the network_id of this CreatePortOption.

        功能说明：端口所属网络的ID 约束：必须是存在的网络ID

        :return: The network_id of this CreatePortOption.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this CreatePortOption.

        功能说明：端口所属网络的ID 约束：必须是存在的网络ID

        :param network_id: The network_id of this CreatePortOption.
        :type: str
        """
        self._network_id = network_id

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this CreatePortOption.

        功能说明：端口IP 例如：\"fixed_ips\": [{\"subnet_id\": \"4dc70db6-cb7f-4200-9790-a6a910776bba\", \"ip_address\": \"192.169.25.79\"}] 约束：ipv4场景下一个端口只支持一个fixed_ip，且不支持更新

        :return: The fixed_ips of this CreatePortOption.
        :rtype: list[FixedIp]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this CreatePortOption.

        功能说明：端口IP 例如：\"fixed_ips\": [{\"subnet_id\": \"4dc70db6-cb7f-4200-9790-a6a910776bba\", \"ip_address\": \"192.169.25.79\"}] 约束：ipv4场景下一个端口只支持一个fixed_ip，且不支持更新

        :param fixed_ips: The fixed_ips of this CreatePortOption.
        :type: list[FixedIp]
        """
        self._fixed_ips = fixed_ips

    @property
    def device_owner(self):
        """Gets the device_owner of this CreatePortOption.

        功能说明：端口设备所属 取值范围：目前只支持指定\"\"和\"neutron:VIP_PORT\"；neutron:VIP_PORT表示创建的是VIP

        :return: The device_owner of this CreatePortOption.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this CreatePortOption.

        功能说明：端口设备所属 取值范围：目前只支持指定\"\"和\"neutron:VIP_PORT\"；neutron:VIP_PORT表示创建的是VIP

        :param device_owner: The device_owner of this CreatePortOption.
        :type: str
        """
        self._device_owner = device_owner

    @property
    def security_groups(self):
        """Gets the security_groups of this CreatePortOption.

        功能说明：安全组的ID列表；例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"] 取值范围：默认值为系统默认安全组

        :return: The security_groups of this CreatePortOption.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this CreatePortOption.

        功能说明：安全组的ID列表；例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"] 取值范围：默认值为系统默认安全组

        :param security_groups: The security_groups of this CreatePortOption.
        :type: list[str]
        """
        self._security_groups = security_groups

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreatePortOption.

        功能说明：管理状态 取值范围：只支持true，默认为true

        :return: The admin_state_up of this CreatePortOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreatePortOption.

        功能说明：管理状态 取值范围：只支持true，默认为true

        :param admin_state_up: The admin_state_up of this CreatePortOption.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def allowed_address_pairs(self):
        """Gets the allowed_address_pairs of this CreatePortOption.

        功能说明：IP/Mac对列表 约束：IP地址不允许为 “0.0.0.0/0” 如果配置的地址池较大（CIDR掩码小于24位），建议为该port配置一个单独的安全组。

        :return: The allowed_address_pairs of this CreatePortOption.
        :rtype: list[AllowedAddressPair]
        """
        return self._allowed_address_pairs

    @allowed_address_pairs.setter
    def allowed_address_pairs(self, allowed_address_pairs):
        """Sets the allowed_address_pairs of this CreatePortOption.

        功能说明：IP/Mac对列表 约束：IP地址不允许为 “0.0.0.0/0” 如果配置的地址池较大（CIDR掩码小于24位），建议为该port配置一个单独的安全组。

        :param allowed_address_pairs: The allowed_address_pairs of this CreatePortOption.
        :type: list[AllowedAddressPair]
        """
        self._allowed_address_pairs = allowed_address_pairs

    @property
    def extra_dhcp_opts(self):
        """Gets the extra_dhcp_opts of this CreatePortOption.

        功能说明：DHCP的扩展Option(扩展属性)

        :return: The extra_dhcp_opts of this CreatePortOption.
        :rtype: list[ExtraDhcpOpt]
        """
        return self._extra_dhcp_opts

    @extra_dhcp_opts.setter
    def extra_dhcp_opts(self, extra_dhcp_opts):
        """Sets the extra_dhcp_opts of this CreatePortOption.

        功能说明：DHCP的扩展Option(扩展属性)

        :param extra_dhcp_opts: The extra_dhcp_opts of this CreatePortOption.
        :type: list[ExtraDhcpOpt]
        """
        self._extra_dhcp_opts = extra_dhcp_opts

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreatePortOption.

        功能说明：端口所属项目ID

        :return: The tenant_id of this CreatePortOption.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreatePortOption.

        功能说明：端口所属项目ID

        :param tenant_id: The tenant_id of this CreatePortOption.
        :type: str
        """
        self._tenant_id = tenant_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreatePortOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
