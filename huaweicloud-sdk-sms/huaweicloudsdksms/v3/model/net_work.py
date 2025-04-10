# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetWork:

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
        'ip': 'str',
        'ipv6': 'str',
        'netmask': 'str',
        'gateway': 'str',
        'mtu': 'int',
        'mac': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'ip': 'ip',
        'ipv6': 'ipv6',
        'netmask': 'netmask',
        'gateway': 'gateway',
        'mtu': 'mtu',
        'mac': 'mac',
        'id': 'id'
    }

    def __init__(self, name=None, ip=None, ipv6=None, netmask=None, gateway=None, mtu=None, mac=None, id=None):
        r"""NetWork

        The model defined in huaweicloud sdk

        :param name: 网卡的名称
        :type name: str
        :param ip: 该网卡绑定的IP
        :type ip: str
        :param ipv6: IPv6地址
        :type ipv6: str
        :param netmask: 掩码
        :type netmask: str
        :param gateway: 网关
        :type gateway: str
        :param mtu: Linux必选，网卡的MTU
        :type mtu: int
        :param mac: Mac地址
        :type mac: str
        :param id: 数据库ID
        :type id: str
        """
        
        

        self._name = None
        self._ip = None
        self._ipv6 = None
        self._netmask = None
        self._gateway = None
        self._mtu = None
        self._mac = None
        self._id = None
        self.discriminator = None

        self.name = name
        self.ip = ip
        if ipv6 is not None:
            self.ipv6 = ipv6
        self.netmask = netmask
        self.gateway = gateway
        if mtu is not None:
            self.mtu = mtu
        self.mac = mac
        if id is not None:
            self.id = id

    @property
    def name(self):
        r"""Gets the name of this NetWork.

        网卡的名称

        :return: The name of this NetWork.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NetWork.

        网卡的名称

        :param name: The name of this NetWork.
        :type name: str
        """
        self._name = name

    @property
    def ip(self):
        r"""Gets the ip of this NetWork.

        该网卡绑定的IP

        :return: The ip of this NetWork.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this NetWork.

        该网卡绑定的IP

        :param ip: The ip of this NetWork.
        :type ip: str
        """
        self._ip = ip

    @property
    def ipv6(self):
        r"""Gets the ipv6 of this NetWork.

        IPv6地址

        :return: The ipv6 of this NetWork.
        :rtype: str
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        r"""Sets the ipv6 of this NetWork.

        IPv6地址

        :param ipv6: The ipv6 of this NetWork.
        :type ipv6: str
        """
        self._ipv6 = ipv6

    @property
    def netmask(self):
        r"""Gets the netmask of this NetWork.

        掩码

        :return: The netmask of this NetWork.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        r"""Sets the netmask of this NetWork.

        掩码

        :param netmask: The netmask of this NetWork.
        :type netmask: str
        """
        self._netmask = netmask

    @property
    def gateway(self):
        r"""Gets the gateway of this NetWork.

        网关

        :return: The gateway of this NetWork.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        r"""Sets the gateway of this NetWork.

        网关

        :param gateway: The gateway of this NetWork.
        :type gateway: str
        """
        self._gateway = gateway

    @property
    def mtu(self):
        r"""Gets the mtu of this NetWork.

        Linux必选，网卡的MTU

        :return: The mtu of this NetWork.
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        r"""Sets the mtu of this NetWork.

        Linux必选，网卡的MTU

        :param mtu: The mtu of this NetWork.
        :type mtu: int
        """
        self._mtu = mtu

    @property
    def mac(self):
        r"""Gets the mac of this NetWork.

        Mac地址

        :return: The mac of this NetWork.
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        r"""Sets the mac of this NetWork.

        Mac地址

        :param mac: The mac of this NetWork.
        :type mac: str
        """
        self._mac = mac

    @property
    def id(self):
        r"""Gets the id of this NetWork.

        数据库ID

        :return: The id of this NetWork.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NetWork.

        数据库ID

        :param id: The id of this NetWork.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, NetWork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
