# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SingleSubnetInfo:

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
        'unused': 'bool',
        'checked': 'bool',
        'vpc_id': 'str',
        'name': 'str',
        'cidr': 'str',
        'gateway_ip': 'str',
        'dhcp_enable': 'bool',
        'ipv6_enable': 'bool',
        'primary_dns': 'str',
        'secondary_dns': 'str',
        'status': 'str',
        'availability_zone': 'str',
        'neutron_subnet_id': 'str',
        'neutron_ipv6_subnet_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'unused': 'unused',
        'checked': 'checked',
        'vpc_id': 'vpc_id',
        'name': 'name',
        'cidr': 'cidr',
        'gateway_ip': 'gateway_ip',
        'dhcp_enable': 'dhcp_enable',
        'ipv6_enable': 'ipv6_enable',
        'primary_dns': 'primary_dns',
        'secondary_dns': 'secondary_dns',
        'status': 'status',
        'availability_zone': 'availability_zone',
        'neutron_subnet_id': 'neutron_subnet_id',
        'neutron_ipv6_subnet_id': 'neutron_ipv6_subnet_id',
        'description': 'description'
    }

    def __init__(self, id=None, unused=None, checked=None, vpc_id=None, name=None, cidr=None, gateway_ip=None, dhcp_enable=None, ipv6_enable=None, primary_dns=None, secondary_dns=None, status=None, availability_zone=None, neutron_subnet_id=None, neutron_ipv6_subnet_id=None, description=None):
        r"""SingleSubnetInfo

        The model defined in huaweicloud sdk

        :param id: 子网ID。
        :type id: str
        :param unused: 是否未被workspace真正使用。如果未使用，则表示可以从workspace中删除。
        :type unused: bool
        :param checked: 是否已被workspace选择使用。
        :type checked: bool
        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param name: 子网名称。
        :type name: str
        :param cidr: 子网网段。
        :type cidr: str
        :param gateway_ip: 子网网关。
        :type gateway_ip: str
        :param dhcp_enable: 是否支持DHCP。
        :type dhcp_enable: bool
        :param ipv6_enable: 是否支持IPV6。
        :type ipv6_enable: bool
        :param primary_dns: 主DNS。
        :type primary_dns: str
        :param secondary_dns: 备DNS。
        :type secondary_dns: str
        :param status: 子网状态。
        :type status: str
        :param availability_zone: 可用区。
        :type availability_zone: str
        :param neutron_subnet_id: 网络id。
        :type neutron_subnet_id: str
        :param neutron_ipv6_subnet_id: ipv6网络id。
        :type neutron_ipv6_subnet_id: str
        :param description: 描述。
        :type description: str
        """
        
        

        self._id = None
        self._unused = None
        self._checked = None
        self._vpc_id = None
        self._name = None
        self._cidr = None
        self._gateway_ip = None
        self._dhcp_enable = None
        self._ipv6_enable = None
        self._primary_dns = None
        self._secondary_dns = None
        self._status = None
        self._availability_zone = None
        self._neutron_subnet_id = None
        self._neutron_ipv6_subnet_id = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if unused is not None:
            self.unused = unused
        if checked is not None:
            self.checked = checked
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if name is not None:
            self.name = name
        if cidr is not None:
            self.cidr = cidr
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip
        if dhcp_enable is not None:
            self.dhcp_enable = dhcp_enable
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if primary_dns is not None:
            self.primary_dns = primary_dns
        if secondary_dns is not None:
            self.secondary_dns = secondary_dns
        if status is not None:
            self.status = status
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if neutron_subnet_id is not None:
            self.neutron_subnet_id = neutron_subnet_id
        if neutron_ipv6_subnet_id is not None:
            self.neutron_ipv6_subnet_id = neutron_ipv6_subnet_id
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this SingleSubnetInfo.

        子网ID。

        :return: The id of this SingleSubnetInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SingleSubnetInfo.

        子网ID。

        :param id: The id of this SingleSubnetInfo.
        :type id: str
        """
        self._id = id

    @property
    def unused(self):
        r"""Gets the unused of this SingleSubnetInfo.

        是否未被workspace真正使用。如果未使用，则表示可以从workspace中删除。

        :return: The unused of this SingleSubnetInfo.
        :rtype: bool
        """
        return self._unused

    @unused.setter
    def unused(self, unused):
        r"""Sets the unused of this SingleSubnetInfo.

        是否未被workspace真正使用。如果未使用，则表示可以从workspace中删除。

        :param unused: The unused of this SingleSubnetInfo.
        :type unused: bool
        """
        self._unused = unused

    @property
    def checked(self):
        r"""Gets the checked of this SingleSubnetInfo.

        是否已被workspace选择使用。

        :return: The checked of this SingleSubnetInfo.
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        r"""Sets the checked of this SingleSubnetInfo.

        是否已被workspace选择使用。

        :param checked: The checked of this SingleSubnetInfo.
        :type checked: bool
        """
        self._checked = checked

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this SingleSubnetInfo.

        VPC ID。

        :return: The vpc_id of this SingleSubnetInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this SingleSubnetInfo.

        VPC ID。

        :param vpc_id: The vpc_id of this SingleSubnetInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def name(self):
        r"""Gets the name of this SingleSubnetInfo.

        子网名称。

        :return: The name of this SingleSubnetInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SingleSubnetInfo.

        子网名称。

        :param name: The name of this SingleSubnetInfo.
        :type name: str
        """
        self._name = name

    @property
    def cidr(self):
        r"""Gets the cidr of this SingleSubnetInfo.

        子网网段。

        :return: The cidr of this SingleSubnetInfo.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this SingleSubnetInfo.

        子网网段。

        :param cidr: The cidr of this SingleSubnetInfo.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def gateway_ip(self):
        r"""Gets the gateway_ip of this SingleSubnetInfo.

        子网网关。

        :return: The gateway_ip of this SingleSubnetInfo.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        r"""Sets the gateway_ip of this SingleSubnetInfo.

        子网网关。

        :param gateway_ip: The gateway_ip of this SingleSubnetInfo.
        :type gateway_ip: str
        """
        self._gateway_ip = gateway_ip

    @property
    def dhcp_enable(self):
        r"""Gets the dhcp_enable of this SingleSubnetInfo.

        是否支持DHCP。

        :return: The dhcp_enable of this SingleSubnetInfo.
        :rtype: bool
        """
        return self._dhcp_enable

    @dhcp_enable.setter
    def dhcp_enable(self, dhcp_enable):
        r"""Sets the dhcp_enable of this SingleSubnetInfo.

        是否支持DHCP。

        :param dhcp_enable: The dhcp_enable of this SingleSubnetInfo.
        :type dhcp_enable: bool
        """
        self._dhcp_enable = dhcp_enable

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this SingleSubnetInfo.

        是否支持IPV6。

        :return: The ipv6_enable of this SingleSubnetInfo.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this SingleSubnetInfo.

        是否支持IPV6。

        :param ipv6_enable: The ipv6_enable of this SingleSubnetInfo.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def primary_dns(self):
        r"""Gets the primary_dns of this SingleSubnetInfo.

        主DNS。

        :return: The primary_dns of this SingleSubnetInfo.
        :rtype: str
        """
        return self._primary_dns

    @primary_dns.setter
    def primary_dns(self, primary_dns):
        r"""Sets the primary_dns of this SingleSubnetInfo.

        主DNS。

        :param primary_dns: The primary_dns of this SingleSubnetInfo.
        :type primary_dns: str
        """
        self._primary_dns = primary_dns

    @property
    def secondary_dns(self):
        r"""Gets the secondary_dns of this SingleSubnetInfo.

        备DNS。

        :return: The secondary_dns of this SingleSubnetInfo.
        :rtype: str
        """
        return self._secondary_dns

    @secondary_dns.setter
    def secondary_dns(self, secondary_dns):
        r"""Sets the secondary_dns of this SingleSubnetInfo.

        备DNS。

        :param secondary_dns: The secondary_dns of this SingleSubnetInfo.
        :type secondary_dns: str
        """
        self._secondary_dns = secondary_dns

    @property
    def status(self):
        r"""Gets the status of this SingleSubnetInfo.

        子网状态。

        :return: The status of this SingleSubnetInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SingleSubnetInfo.

        子网状态。

        :param status: The status of this SingleSubnetInfo.
        :type status: str
        """
        self._status = status

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this SingleSubnetInfo.

        可用区。

        :return: The availability_zone of this SingleSubnetInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this SingleSubnetInfo.

        可用区。

        :param availability_zone: The availability_zone of this SingleSubnetInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def neutron_subnet_id(self):
        r"""Gets the neutron_subnet_id of this SingleSubnetInfo.

        网络id。

        :return: The neutron_subnet_id of this SingleSubnetInfo.
        :rtype: str
        """
        return self._neutron_subnet_id

    @neutron_subnet_id.setter
    def neutron_subnet_id(self, neutron_subnet_id):
        r"""Sets the neutron_subnet_id of this SingleSubnetInfo.

        网络id。

        :param neutron_subnet_id: The neutron_subnet_id of this SingleSubnetInfo.
        :type neutron_subnet_id: str
        """
        self._neutron_subnet_id = neutron_subnet_id

    @property
    def neutron_ipv6_subnet_id(self):
        r"""Gets the neutron_ipv6_subnet_id of this SingleSubnetInfo.

        ipv6网络id。

        :return: The neutron_ipv6_subnet_id of this SingleSubnetInfo.
        :rtype: str
        """
        return self._neutron_ipv6_subnet_id

    @neutron_ipv6_subnet_id.setter
    def neutron_ipv6_subnet_id(self, neutron_ipv6_subnet_id):
        r"""Sets the neutron_ipv6_subnet_id of this SingleSubnetInfo.

        ipv6网络id。

        :param neutron_ipv6_subnet_id: The neutron_ipv6_subnet_id of this SingleSubnetInfo.
        :type neutron_ipv6_subnet_id: str
        """
        self._neutron_ipv6_subnet_id = neutron_ipv6_subnet_id

    @property
    def description(self):
        r"""Gets the description of this SingleSubnetInfo.

        描述。

        :return: The description of this SingleSubnetInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SingleSubnetInfo.

        描述。

        :param description: The description of this SingleSubnetInfo.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SingleSubnetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
