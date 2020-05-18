# coding: utf-8

import pprint
import re

import six


class NeutronListSubnetsRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'str',
        'cidr': 'str',
        'name': 'str',
        'enable_dhcp': 'bool',
        'network_id': 'str',
        'ip_version': 'int',
        'gateway_ip': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'cidr': 'cidr',
        'name': 'name',
        'enable_dhcp': 'enable_dhcp',
        'network_id': 'network_id',
        'ip_version': 'ip_version',
        'gateway_ip': 'gateway_ip',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, limit=2000, marker=None, id=None, cidr=None, name=None, enable_dhcp=None, network_id=None, ip_version=None, gateway_ip=None, tenant_id=None):  # noqa: E501
        """NeutronListSubnetsRequest - a model defined in huaweicloud sdk"""

        self._limit = None
        self._marker = None
        self._id = None
        self._cidr = None
        self._name = None
        self._enable_dhcp = None
        self._network_id = None
        self._ip_version = None
        self._gateway_ip = None
        self._tenant_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if cidr is not None:
            self.cidr = cidr
        if name is not None:
            self.name = name
        if enable_dhcp is not None:
            self.enable_dhcp = enable_dhcp
        if network_id is not None:
            self.network_id = network_id
        if ip_version is not None:
            self.ip_version = ip_version
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def limit(self):
        """Gets the limit of this NeutronListSubnetsRequest.


        :return: The limit of this NeutronListSubnetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NeutronListSubnetsRequest.


        :param limit: The limit of this NeutronListSubnetsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NeutronListSubnetsRequest.


        :return: The marker of this NeutronListSubnetsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NeutronListSubnetsRequest.


        :param marker: The marker of this NeutronListSubnetsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this NeutronListSubnetsRequest.


        :return: The id of this NeutronListSubnetsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronListSubnetsRequest.


        :param id: The id of this NeutronListSubnetsRequest.
        :type: str
        """
        self._id = id

    @property
    def cidr(self):
        """Gets the cidr of this NeutronListSubnetsRequest.


        :return: The cidr of this NeutronListSubnetsRequest.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this NeutronListSubnetsRequest.


        :param cidr: The cidr of this NeutronListSubnetsRequest.
        :type: str
        """
        self._cidr = cidr

    @property
    def name(self):
        """Gets the name of this NeutronListSubnetsRequest.


        :return: The name of this NeutronListSubnetsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NeutronListSubnetsRequest.


        :param name: The name of this NeutronListSubnetsRequest.
        :type: str
        """
        self._name = name

    @property
    def enable_dhcp(self):
        """Gets the enable_dhcp of this NeutronListSubnetsRequest.


        :return: The enable_dhcp of this NeutronListSubnetsRequest.
        :rtype: bool
        """
        return self._enable_dhcp

    @enable_dhcp.setter
    def enable_dhcp(self, enable_dhcp):
        """Sets the enable_dhcp of this NeutronListSubnetsRequest.


        :param enable_dhcp: The enable_dhcp of this NeutronListSubnetsRequest.
        :type: bool
        """
        self._enable_dhcp = enable_dhcp

    @property
    def network_id(self):
        """Gets the network_id of this NeutronListSubnetsRequest.


        :return: The network_id of this NeutronListSubnetsRequest.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this NeutronListSubnetsRequest.


        :param network_id: The network_id of this NeutronListSubnetsRequest.
        :type: str
        """
        self._network_id = network_id

    @property
    def ip_version(self):
        """Gets the ip_version of this NeutronListSubnetsRequest.


        :return: The ip_version of this NeutronListSubnetsRequest.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this NeutronListSubnetsRequest.


        :param ip_version: The ip_version of this NeutronListSubnetsRequest.
        :type: int
        """
        self._ip_version = ip_version

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this NeutronListSubnetsRequest.


        :return: The gateway_ip of this NeutronListSubnetsRequest.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this NeutronListSubnetsRequest.


        :param gateway_ip: The gateway_ip of this NeutronListSubnetsRequest.
        :type: str
        """
        self._gateway_ip = gateway_ip

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronListSubnetsRequest.


        :return: The tenant_id of this NeutronListSubnetsRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronListSubnetsRequest.


        :param tenant_id: The tenant_id of this NeutronListSubnetsRequest.
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
        if not isinstance(other, NeutronListSubnetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
