# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubnetOption:

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
        'cidr': 'str',
        'gateway_ip': 'str',
        'dhcp_enable': 'bool',
        'primary_dns': 'str',
        'secondary_dns': 'str',
        'dns_list': 'list[str]',
        'vpc_id': 'str',
        'site_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cidr': 'cidr',
        'gateway_ip': 'gateway_ip',
        'dhcp_enable': 'dhcp_enable',
        'primary_dns': 'primary_dns',
        'secondary_dns': 'secondary_dns',
        'dns_list': 'dnsList',
        'vpc_id': 'vpc_id',
        'site_id': 'site_id'
    }

    def __init__(self, name=None, cidr=None, gateway_ip=None, dhcp_enable=None, primary_dns=None, secondary_dns=None, dns_list=None, vpc_id=None, site_id=None):
        r"""CreateSubnetOption

        The model defined in huaweicloud sdk

        :param name: 子网名称  约束：由中文字符、字母、数字、中划线和下划线和点组成，长度为1~64个字符
        :type name: str
        :param cidr: 子网的网段  取值范围：必须在vpc对应cidr范围内  约束：必须是cidr格式。掩码长度不能大于28
        :type cidr: str
        :param gateway_ip: 子网的网关  取值范围：子网网段中的IP地址  约束：必须是ip格式
        :type gateway_ip: str
        :param dhcp_enable: 子网是否开启dhcp功能  取值范围：true（开启），false（关闭）  约束：不填时默认为true。当设置为false时，会导致新创建的ECS无法获取IP地址，cloudinit无法注入账号密码，请谨慎操作。
        :type dhcp_enable: bool
        :param primary_dns: 子网dns服务器地址1  约束：ip格式，不支持IPv6地址
        :type primary_dns: str
        :param secondary_dns: 子网dns服务器地址2  约束：ip格式，不支持IPv6地址
        :type secondary_dns: str
        :param dns_list: 子网dns服务器地址的集合；如果想使用两个以上dns服务器，请使用该字段  约束：是子网dns服务器地址1跟子网dns服务器地址2的合集的父集，不支持IPv6地址。
        :type dns_list: list[str]
        :param vpc_id: 子网所在VPC的ID。
        :type vpc_id: str
        :param site_id: 子网归属的站点ID,从站点信息列表中获取。
        :type site_id: str
        """
        
        

        self._name = None
        self._cidr = None
        self._gateway_ip = None
        self._dhcp_enable = None
        self._primary_dns = None
        self._secondary_dns = None
        self._dns_list = None
        self._vpc_id = None
        self._site_id = None
        self.discriminator = None

        self.name = name
        self.cidr = cidr
        self.gateway_ip = gateway_ip
        if dhcp_enable is not None:
            self.dhcp_enable = dhcp_enable
        if primary_dns is not None:
            self.primary_dns = primary_dns
        if secondary_dns is not None:
            self.secondary_dns = secondary_dns
        if dns_list is not None:
            self.dns_list = dns_list
        self.vpc_id = vpc_id
        self.site_id = site_id

    @property
    def name(self):
        r"""Gets the name of this CreateSubnetOption.

        子网名称  约束：由中文字符、字母、数字、中划线和下划线和点组成，长度为1~64个字符

        :return: The name of this CreateSubnetOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSubnetOption.

        子网名称  约束：由中文字符、字母、数字、中划线和下划线和点组成，长度为1~64个字符

        :param name: The name of this CreateSubnetOption.
        :type name: str
        """
        self._name = name

    @property
    def cidr(self):
        r"""Gets the cidr of this CreateSubnetOption.

        子网的网段  取值范围：必须在vpc对应cidr范围内  约束：必须是cidr格式。掩码长度不能大于28

        :return: The cidr of this CreateSubnetOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this CreateSubnetOption.

        子网的网段  取值范围：必须在vpc对应cidr范围内  约束：必须是cidr格式。掩码长度不能大于28

        :param cidr: The cidr of this CreateSubnetOption.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def gateway_ip(self):
        r"""Gets the gateway_ip of this CreateSubnetOption.

        子网的网关  取值范围：子网网段中的IP地址  约束：必须是ip格式

        :return: The gateway_ip of this CreateSubnetOption.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        r"""Sets the gateway_ip of this CreateSubnetOption.

        子网的网关  取值范围：子网网段中的IP地址  约束：必须是ip格式

        :param gateway_ip: The gateway_ip of this CreateSubnetOption.
        :type gateway_ip: str
        """
        self._gateway_ip = gateway_ip

    @property
    def dhcp_enable(self):
        r"""Gets the dhcp_enable of this CreateSubnetOption.

        子网是否开启dhcp功能  取值范围：true（开启），false（关闭）  约束：不填时默认为true。当设置为false时，会导致新创建的ECS无法获取IP地址，cloudinit无法注入账号密码，请谨慎操作。

        :return: The dhcp_enable of this CreateSubnetOption.
        :rtype: bool
        """
        return self._dhcp_enable

    @dhcp_enable.setter
    def dhcp_enable(self, dhcp_enable):
        r"""Sets the dhcp_enable of this CreateSubnetOption.

        子网是否开启dhcp功能  取值范围：true（开启），false（关闭）  约束：不填时默认为true。当设置为false时，会导致新创建的ECS无法获取IP地址，cloudinit无法注入账号密码，请谨慎操作。

        :param dhcp_enable: The dhcp_enable of this CreateSubnetOption.
        :type dhcp_enable: bool
        """
        self._dhcp_enable = dhcp_enable

    @property
    def primary_dns(self):
        r"""Gets the primary_dns of this CreateSubnetOption.

        子网dns服务器地址1  约束：ip格式，不支持IPv6地址

        :return: The primary_dns of this CreateSubnetOption.
        :rtype: str
        """
        return self._primary_dns

    @primary_dns.setter
    def primary_dns(self, primary_dns):
        r"""Sets the primary_dns of this CreateSubnetOption.

        子网dns服务器地址1  约束：ip格式，不支持IPv6地址

        :param primary_dns: The primary_dns of this CreateSubnetOption.
        :type primary_dns: str
        """
        self._primary_dns = primary_dns

    @property
    def secondary_dns(self):
        r"""Gets the secondary_dns of this CreateSubnetOption.

        子网dns服务器地址2  约束：ip格式，不支持IPv6地址

        :return: The secondary_dns of this CreateSubnetOption.
        :rtype: str
        """
        return self._secondary_dns

    @secondary_dns.setter
    def secondary_dns(self, secondary_dns):
        r"""Sets the secondary_dns of this CreateSubnetOption.

        子网dns服务器地址2  约束：ip格式，不支持IPv6地址

        :param secondary_dns: The secondary_dns of this CreateSubnetOption.
        :type secondary_dns: str
        """
        self._secondary_dns = secondary_dns

    @property
    def dns_list(self):
        r"""Gets the dns_list of this CreateSubnetOption.

        子网dns服务器地址的集合；如果想使用两个以上dns服务器，请使用该字段  约束：是子网dns服务器地址1跟子网dns服务器地址2的合集的父集，不支持IPv6地址。

        :return: The dns_list of this CreateSubnetOption.
        :rtype: list[str]
        """
        return self._dns_list

    @dns_list.setter
    def dns_list(self, dns_list):
        r"""Sets the dns_list of this CreateSubnetOption.

        子网dns服务器地址的集合；如果想使用两个以上dns服务器，请使用该字段  约束：是子网dns服务器地址1跟子网dns服务器地址2的合集的父集，不支持IPv6地址。

        :param dns_list: The dns_list of this CreateSubnetOption.
        :type dns_list: list[str]
        """
        self._dns_list = dns_list

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateSubnetOption.

        子网所在VPC的ID。

        :return: The vpc_id of this CreateSubnetOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateSubnetOption.

        子网所在VPC的ID。

        :param vpc_id: The vpc_id of this CreateSubnetOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def site_id(self):
        r"""Gets the site_id of this CreateSubnetOption.

        子网归属的站点ID,从站点信息列表中获取。

        :return: The site_id of this CreateSubnetOption.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this CreateSubnetOption.

        子网归属的站点ID,从站点信息列表中获取。

        :param site_id: The site_id of this CreateSubnetOption.
        :type site_id: str
        """
        self._site_id = site_id

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
        if not isinstance(other, CreateSubnetOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
