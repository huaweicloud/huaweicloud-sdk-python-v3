# coding: utf-8

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
        'ipv6_enable': 'bool',
        'cidr': 'str',
        'cidr_v6': 'str',
        'gateway_ip': 'str',
        'gateway_ip_v6': 'str',
        'availability_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ipv6_enable': 'ipv6_enable',
        'cidr': 'cidr',
        'cidr_v6': 'cidr_v6',
        'gateway_ip': 'gateway_ip',
        'gateway_ip_v6': 'gateway_ip_v6',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, id=None, name=None, ipv6_enable=None, cidr=None, cidr_v6=None, gateway_ip=None, gateway_ip_v6=None, availability_zone=None):
        r"""Subnet

        The model defined in huaweicloud sdk

        :param id: 子网ID
        :type id: str
        :param name: 子网名字
        :type name: str
        :param ipv6_enable: 是否是IPV6子网
        :type ipv6_enable: bool
        :param cidr: 子网的CIDR信息
        :type cidr: str
        :param cidr_v6: IPV6子网的CIDR信息
        :type cidr_v6: str
        :param gateway_ip: 子网的网关
        :type gateway_ip: str
        :param gateway_ip_v6: IPV6子网的网关
        :type gateway_ip_v6: str
        :param availability_zone: 子网的可用区
        :type availability_zone: str
        """
        
        

        self._id = None
        self._name = None
        self._ipv6_enable = None
        self._cidr = None
        self._cidr_v6 = None
        self._gateway_ip = None
        self._gateway_ip_v6 = None
        self._availability_zone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if cidr is not None:
            self.cidr = cidr
        if cidr_v6 is not None:
            self.cidr_v6 = cidr_v6
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip
        if gateway_ip_v6 is not None:
            self.gateway_ip_v6 = gateway_ip_v6
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def id(self):
        r"""Gets the id of this Subnet.

        子网ID

        :return: The id of this Subnet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Subnet.

        子网ID

        :param id: The id of this Subnet.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Subnet.

        子网名字

        :return: The name of this Subnet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Subnet.

        子网名字

        :param name: The name of this Subnet.
        :type name: str
        """
        self._name = name

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this Subnet.

        是否是IPV6子网

        :return: The ipv6_enable of this Subnet.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this Subnet.

        是否是IPV6子网

        :param ipv6_enable: The ipv6_enable of this Subnet.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def cidr(self):
        r"""Gets the cidr of this Subnet.

        子网的CIDR信息

        :return: The cidr of this Subnet.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this Subnet.

        子网的CIDR信息

        :param cidr: The cidr of this Subnet.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def cidr_v6(self):
        r"""Gets the cidr_v6 of this Subnet.

        IPV6子网的CIDR信息

        :return: The cidr_v6 of this Subnet.
        :rtype: str
        """
        return self._cidr_v6

    @cidr_v6.setter
    def cidr_v6(self, cidr_v6):
        r"""Sets the cidr_v6 of this Subnet.

        IPV6子网的CIDR信息

        :param cidr_v6: The cidr_v6 of this Subnet.
        :type cidr_v6: str
        """
        self._cidr_v6 = cidr_v6

    @property
    def gateway_ip(self):
        r"""Gets the gateway_ip of this Subnet.

        子网的网关

        :return: The gateway_ip of this Subnet.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        r"""Sets the gateway_ip of this Subnet.

        子网的网关

        :param gateway_ip: The gateway_ip of this Subnet.
        :type gateway_ip: str
        """
        self._gateway_ip = gateway_ip

    @property
    def gateway_ip_v6(self):
        r"""Gets the gateway_ip_v6 of this Subnet.

        IPV6子网的网关

        :return: The gateway_ip_v6 of this Subnet.
        :rtype: str
        """
        return self._gateway_ip_v6

    @gateway_ip_v6.setter
    def gateway_ip_v6(self, gateway_ip_v6):
        r"""Sets the gateway_ip_v6 of this Subnet.

        IPV6子网的网关

        :param gateway_ip_v6: The gateway_ip_v6 of this Subnet.
        :type gateway_ip_v6: str
        """
        self._gateway_ip_v6 = gateway_ip_v6

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this Subnet.

        子网的可用区

        :return: The availability_zone of this Subnet.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this Subnet.

        子网的可用区

        :param availability_zone: The availability_zone of this Subnet.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, Subnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
