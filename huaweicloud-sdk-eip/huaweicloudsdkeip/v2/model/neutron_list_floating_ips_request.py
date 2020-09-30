# coding: utf-8

import pprint
import re

import six





class NeutronListFloatingIpsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'str',
        'floating_ip_address': 'str',
        'router_id': 'str',
        'port_id': 'str',
        'fixed_ip_address': 'str',
        'tenant_id': 'str',
        'floating_network_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'floating_ip_address': 'floating_ip_address',
        'router_id': 'router_id',
        'port_id': 'port_id',
        'fixed_ip_address': 'fixed_ip_address',
        'tenant_id': 'tenant_id',
        'floating_network_id': 'floating_network_id'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, floating_ip_address=None, router_id=None, port_id=None, fixed_ip_address=None, tenant_id=None, floating_network_id=None):
        """NeutronListFloatingIpsRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._floating_ip_address = None
        self._router_id = None
        self._port_id = None
        self._fixed_ip_address = None
        self._tenant_id = None
        self._floating_network_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if floating_ip_address is not None:
            self.floating_ip_address = floating_ip_address
        if router_id is not None:
            self.router_id = router_id
        if port_id is not None:
            self.port_id = port_id
        if fixed_ip_address is not None:
            self.fixed_ip_address = fixed_ip_address
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if floating_network_id is not None:
            self.floating_network_id = floating_network_id

    @property
    def limit(self):
        """Gets the limit of this NeutronListFloatingIpsRequest.


        :return: The limit of this NeutronListFloatingIpsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NeutronListFloatingIpsRequest.


        :param limit: The limit of this NeutronListFloatingIpsRequest.
        :type: str
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NeutronListFloatingIpsRequest.


        :return: The marker of this NeutronListFloatingIpsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NeutronListFloatingIpsRequest.


        :param marker: The marker of this NeutronListFloatingIpsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this NeutronListFloatingIpsRequest.


        :return: The page_reverse of this NeutronListFloatingIpsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this NeutronListFloatingIpsRequest.


        :param page_reverse: The page_reverse of this NeutronListFloatingIpsRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this NeutronListFloatingIpsRequest.


        :return: The id of this NeutronListFloatingIpsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NeutronListFloatingIpsRequest.


        :param id: The id of this NeutronListFloatingIpsRequest.
        :type: str
        """
        self._id = id

    @property
    def floating_ip_address(self):
        """Gets the floating_ip_address of this NeutronListFloatingIpsRequest.


        :return: The floating_ip_address of this NeutronListFloatingIpsRequest.
        :rtype: str
        """
        return self._floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        """Sets the floating_ip_address of this NeutronListFloatingIpsRequest.


        :param floating_ip_address: The floating_ip_address of this NeutronListFloatingIpsRequest.
        :type: str
        """
        self._floating_ip_address = floating_ip_address

    @property
    def router_id(self):
        """Gets the router_id of this NeutronListFloatingIpsRequest.


        :return: The router_id of this NeutronListFloatingIpsRequest.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        """Sets the router_id of this NeutronListFloatingIpsRequest.


        :param router_id: The router_id of this NeutronListFloatingIpsRequest.
        :type: str
        """
        self._router_id = router_id

    @property
    def port_id(self):
        """Gets the port_id of this NeutronListFloatingIpsRequest.


        :return: The port_id of this NeutronListFloatingIpsRequest.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this NeutronListFloatingIpsRequest.


        :param port_id: The port_id of this NeutronListFloatingIpsRequest.
        :type: str
        """
        self._port_id = port_id

    @property
    def fixed_ip_address(self):
        """Gets the fixed_ip_address of this NeutronListFloatingIpsRequest.


        :return: The fixed_ip_address of this NeutronListFloatingIpsRequest.
        :rtype: str
        """
        return self._fixed_ip_address

    @fixed_ip_address.setter
    def fixed_ip_address(self, fixed_ip_address):
        """Sets the fixed_ip_address of this NeutronListFloatingIpsRequest.


        :param fixed_ip_address: The fixed_ip_address of this NeutronListFloatingIpsRequest.
        :type: str
        """
        self._fixed_ip_address = fixed_ip_address

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NeutronListFloatingIpsRequest.


        :return: The tenant_id of this NeutronListFloatingIpsRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NeutronListFloatingIpsRequest.


        :param tenant_id: The tenant_id of this NeutronListFloatingIpsRequest.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def floating_network_id(self):
        """Gets the floating_network_id of this NeutronListFloatingIpsRequest.


        :return: The floating_network_id of this NeutronListFloatingIpsRequest.
        :rtype: str
        """
        return self._floating_network_id

    @floating_network_id.setter
    def floating_network_id(self, floating_network_id):
        """Sets the floating_network_id of this NeutronListFloatingIpsRequest.


        :param floating_network_id: The floating_network_id of this NeutronListFloatingIpsRequest.
        :type: str
        """
        self._floating_network_id = floating_network_id

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
        if not isinstance(other, NeutronListFloatingIpsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
