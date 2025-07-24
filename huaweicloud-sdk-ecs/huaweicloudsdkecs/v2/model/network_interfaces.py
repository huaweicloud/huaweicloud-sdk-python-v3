# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkInterfaces:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port_id': 'str',
        'primary': 'bool',
        'ip_addresses': 'list[str]',
        'ipv6_addresses': 'list[str]',
        'subnet_id': 'str',
        'association': 'Association'
    }

    attribute_map = {
        'port_id': 'port_id',
        'primary': 'primary',
        'ip_addresses': 'ip_addresses',
        'ipv6_addresses': 'ipv6_addresses',
        'subnet_id': 'subnet_id',
        'association': 'association'
    }

    def __init__(self, port_id=None, primary=None, ip_addresses=None, ipv6_addresses=None, subnet_id=None, association=None):
        r"""NetworkInterfaces

        The model defined in huaweicloud sdk

        :param port_id: 网卡端口id
        :type port_id: str
        :param primary: 是否是主网卡
        :type primary: bool
        :param ip_addresses: ipv4地址
        :type ip_addresses: list[str]
        :param ipv6_addresses: ipv6地址
        :type ipv6_addresses: list[str]
        :param subnet_id: 子网id
        :type subnet_id: str
        :param association: 
        :type association: :class:`huaweicloudsdkecs.v2.Association`
        """
        
        

        self._port_id = None
        self._primary = None
        self._ip_addresses = None
        self._ipv6_addresses = None
        self._subnet_id = None
        self._association = None
        self.discriminator = None

        if port_id is not None:
            self.port_id = port_id
        if primary is not None:
            self.primary = primary
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if ipv6_addresses is not None:
            self.ipv6_addresses = ipv6_addresses
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if association is not None:
            self.association = association

    @property
    def port_id(self):
        r"""Gets the port_id of this NetworkInterfaces.

        网卡端口id

        :return: The port_id of this NetworkInterfaces.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this NetworkInterfaces.

        网卡端口id

        :param port_id: The port_id of this NetworkInterfaces.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def primary(self):
        r"""Gets the primary of this NetworkInterfaces.

        是否是主网卡

        :return: The primary of this NetworkInterfaces.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        r"""Sets the primary of this NetworkInterfaces.

        是否是主网卡

        :param primary: The primary of this NetworkInterfaces.
        :type primary: bool
        """
        self._primary = primary

    @property
    def ip_addresses(self):
        r"""Gets the ip_addresses of this NetworkInterfaces.

        ipv4地址

        :return: The ip_addresses of this NetworkInterfaces.
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        r"""Sets the ip_addresses of this NetworkInterfaces.

        ipv4地址

        :param ip_addresses: The ip_addresses of this NetworkInterfaces.
        :type ip_addresses: list[str]
        """
        self._ip_addresses = ip_addresses

    @property
    def ipv6_addresses(self):
        r"""Gets the ipv6_addresses of this NetworkInterfaces.

        ipv6地址

        :return: The ipv6_addresses of this NetworkInterfaces.
        :rtype: list[str]
        """
        return self._ipv6_addresses

    @ipv6_addresses.setter
    def ipv6_addresses(self, ipv6_addresses):
        r"""Sets the ipv6_addresses of this NetworkInterfaces.

        ipv6地址

        :param ipv6_addresses: The ipv6_addresses of this NetworkInterfaces.
        :type ipv6_addresses: list[str]
        """
        self._ipv6_addresses = ipv6_addresses

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this NetworkInterfaces.

        子网id

        :return: The subnet_id of this NetworkInterfaces.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this NetworkInterfaces.

        子网id

        :param subnet_id: The subnet_id of this NetworkInterfaces.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def association(self):
        r"""Gets the association of this NetworkInterfaces.

        :return: The association of this NetworkInterfaces.
        :rtype: :class:`huaweicloudsdkecs.v2.Association`
        """
        return self._association

    @association.setter
    def association(self, association):
        r"""Sets the association of this NetworkInterfaces.

        :param association: The association of this NetworkInterfaces.
        :type association: :class:`huaweicloudsdkecs.v2.Association`
        """
        self._association = association

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
        if not isinstance(other, NetworkInterfaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
