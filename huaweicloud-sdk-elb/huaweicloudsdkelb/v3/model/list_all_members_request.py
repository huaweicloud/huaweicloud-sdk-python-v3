# coding: utf-8

import pprint
import re

import six





class ListAllMembersRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'address': 'list[str]',
        'admin_state_up': 'bool',
        'enterprise_project_id': 'list[str]',
        'id': 'list[str]',
        'ip_version': 'str',
        'limit': 'int',
        'loadbalancer_id': 'str',
        'marker': 'str',
        'name': 'list[str]',
        'operating_status': 'list[str]',
        'page_reverse': 'bool',
        'pool_id': 'str',
        'protocol_port': 'list[int]',
        'subnet_cidr_id': 'list[str]',
        'weight': 'list[int]'
    }

    attribute_map = {
        'address': 'address',
        'admin_state_up': 'admin_state_up',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'ip_version': 'ip_version',
        'limit': 'limit',
        'loadbalancer_id': 'loadbalancer_id',
        'marker': 'marker',
        'name': 'name',
        'operating_status': 'operating_status',
        'page_reverse': 'page_reverse',
        'pool_id': 'pool_id',
        'protocol_port': 'protocol_port',
        'subnet_cidr_id': 'subnet_cidr_id',
        'weight': 'weight'
    }

    def __init__(self, address=None, admin_state_up=None, enterprise_project_id=None, id=None, ip_version=None, limit=None, loadbalancer_id=None, marker=None, name=None, operating_status=None, page_reverse=None, pool_id=None, protocol_port=None, subnet_cidr_id=None, weight=None):
        """ListAllMembersRequest - a model defined in huaweicloud sdk"""
        
        

        self._address = None
        self._admin_state_up = None
        self._enterprise_project_id = None
        self._id = None
        self._ip_version = None
        self._limit = None
        self._loadbalancer_id = None
        self._marker = None
        self._name = None
        self._operating_status = None
        self._page_reverse = None
        self._pool_id = None
        self._protocol_port = None
        self._subnet_cidr_id = None
        self._weight = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        if ip_version is not None:
            self.ip_version = ip_version
        if limit is not None:
            self.limit = limit
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if operating_status is not None:
            self.operating_status = operating_status
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if pool_id is not None:
            self.pool_id = pool_id
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        if weight is not None:
            self.weight = weight

    @property
    def address(self):
        """Gets the address of this ListAllMembersRequest.


        :return: The address of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ListAllMembersRequest.


        :param address: The address of this ListAllMembersRequest.
        :type: list[str]
        """
        self._address = address

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListAllMembersRequest.


        :return: The admin_state_up of this ListAllMembersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListAllMembersRequest.


        :param admin_state_up: The admin_state_up of this ListAllMembersRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAllMembersRequest.


        :return: The enterprise_project_id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAllMembersRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListAllMembersRequest.
        :type: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this ListAllMembersRequest.


        :return: The id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListAllMembersRequest.


        :param id: The id of this ListAllMembersRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def ip_version(self):
        """Gets the ip_version of this ListAllMembersRequest.


        :return: The ip_version of this ListAllMembersRequest.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListAllMembersRequest.


        :param ip_version: The ip_version of this ListAllMembersRequest.
        :type: str
        """
        self._ip_version = ip_version

    @property
    def limit(self):
        """Gets the limit of this ListAllMembersRequest.


        :return: The limit of this ListAllMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAllMembersRequest.


        :param limit: The limit of this ListAllMembersRequest.
        :type: int
        """
        self._limit = limit

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this ListAllMembersRequest.


        :return: The loadbalancer_id of this ListAllMembersRequest.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this ListAllMembersRequest.


        :param loadbalancer_id: The loadbalancer_id of this ListAllMembersRequest.
        :type: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def marker(self):
        """Gets the marker of this ListAllMembersRequest.


        :return: The marker of this ListAllMembersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAllMembersRequest.


        :param marker: The marker of this ListAllMembersRequest.
        :type: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListAllMembersRequest.


        :return: The name of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAllMembersRequest.


        :param name: The name of this ListAllMembersRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def operating_status(self):
        """Gets the operating_status of this ListAllMembersRequest.


        :return: The operating_status of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this ListAllMembersRequest.


        :param operating_status: The operating_status of this ListAllMembersRequest.
        :type: list[str]
        """
        self._operating_status = operating_status

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListAllMembersRequest.


        :return: The page_reverse of this ListAllMembersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListAllMembersRequest.


        :param page_reverse: The page_reverse of this ListAllMembersRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def pool_id(self):
        """Gets the pool_id of this ListAllMembersRequest.


        :return: The pool_id of this ListAllMembersRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this ListAllMembersRequest.


        :param pool_id: The pool_id of this ListAllMembersRequest.
        :type: str
        """
        self._pool_id = pool_id

    @property
    def protocol_port(self):
        """Gets the protocol_port of this ListAllMembersRequest.


        :return: The protocol_port of this ListAllMembersRequest.
        :rtype: list[int]
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this ListAllMembersRequest.


        :param protocol_port: The protocol_port of this ListAllMembersRequest.
        :type: list[int]
        """
        self._protocol_port = protocol_port

    @property
    def subnet_cidr_id(self):
        """Gets the subnet_cidr_id of this ListAllMembersRequest.


        :return: The subnet_cidr_id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        """Sets the subnet_cidr_id of this ListAllMembersRequest.


        :param subnet_cidr_id: The subnet_cidr_id of this ListAllMembersRequest.
        :type: list[str]
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def weight(self):
        """Gets the weight of this ListAllMembersRequest.


        :return: The weight of this ListAllMembersRequest.
        :rtype: list[int]
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ListAllMembersRequest.


        :param weight: The weight of this ListAllMembersRequest.
        :type: list[int]
        """
        self._weight = weight

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
        if not isinstance(other, ListAllMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
