# coding: utf-8

import pprint
import re

import six





class ListMembersRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'address': 'list[str]',
        'admin_state_up': 'bool',
        'enterprise_project_id': 'list[str]',
        'id': 'list[str]',
        'limit': 'int',
        'marker': 'str',
        'name': 'list[str]',
        'operating_status': 'list[str]',
        'page_reverse': 'bool',
        'protocol_port': 'list[int]',
        'subnet_cidr_id': 'list[str]',
        'weight': 'list[int]'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'address': 'address',
        'admin_state_up': 'admin_state_up',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name',
        'operating_status': 'operating_status',
        'page_reverse': 'page_reverse',
        'protocol_port': 'protocol_port',
        'subnet_cidr_id': 'subnet_cidr_id',
        'weight': 'weight'
    }

    def __init__(self, pool_id=None, address=None, admin_state_up=None, enterprise_project_id=None, id=None, limit=None, marker=None, name=None, operating_status=None, page_reverse=None, protocol_port=None, subnet_cidr_id=None, weight=None):
        """ListMembersRequest - a model defined in huaweicloud sdk"""
        
        

        self._pool_id = None
        self._address = None
        self._admin_state_up = None
        self._enterprise_project_id = None
        self._id = None
        self._limit = None
        self._marker = None
        self._name = None
        self._operating_status = None
        self._page_reverse = None
        self._protocol_port = None
        self._subnet_cidr_id = None
        self._weight = None
        self.discriminator = None

        self.pool_id = pool_id
        if address is not None:
            self.address = address
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if operating_status is not None:
            self.operating_status = operating_status
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        if weight is not None:
            self.weight = weight

    @property
    def pool_id(self):
        """Gets the pool_id of this ListMembersRequest.


        :return: The pool_id of this ListMembersRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this ListMembersRequest.


        :param pool_id: The pool_id of this ListMembersRequest.
        :type: str
        """
        self._pool_id = pool_id

    @property
    def address(self):
        """Gets the address of this ListMembersRequest.


        :return: The address of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ListMembersRequest.


        :param address: The address of this ListMembersRequest.
        :type: list[str]
        """
        self._address = address

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListMembersRequest.


        :return: The admin_state_up of this ListMembersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListMembersRequest.


        :param admin_state_up: The admin_state_up of this ListMembersRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListMembersRequest.


        :return: The enterprise_project_id of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListMembersRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListMembersRequest.
        :type: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this ListMembersRequest.


        :return: The id of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListMembersRequest.


        :param id: The id of this ListMembersRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListMembersRequest.


        :return: The limit of this ListMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMembersRequest.


        :param limit: The limit of this ListMembersRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListMembersRequest.


        :return: The marker of this ListMembersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListMembersRequest.


        :param marker: The marker of this ListMembersRequest.
        :type: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListMembersRequest.


        :return: The name of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListMembersRequest.


        :param name: The name of this ListMembersRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def operating_status(self):
        """Gets the operating_status of this ListMembersRequest.


        :return: The operating_status of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this ListMembersRequest.


        :param operating_status: The operating_status of this ListMembersRequest.
        :type: list[str]
        """
        self._operating_status = operating_status

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListMembersRequest.


        :return: The page_reverse of this ListMembersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListMembersRequest.


        :param page_reverse: The page_reverse of this ListMembersRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def protocol_port(self):
        """Gets the protocol_port of this ListMembersRequest.


        :return: The protocol_port of this ListMembersRequest.
        :rtype: list[int]
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this ListMembersRequest.


        :param protocol_port: The protocol_port of this ListMembersRequest.
        :type: list[int]
        """
        self._protocol_port = protocol_port

    @property
    def subnet_cidr_id(self):
        """Gets the subnet_cidr_id of this ListMembersRequest.


        :return: The subnet_cidr_id of this ListMembersRequest.
        :rtype: list[str]
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        """Sets the subnet_cidr_id of this ListMembersRequest.


        :param subnet_cidr_id: The subnet_cidr_id of this ListMembersRequest.
        :type: list[str]
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def weight(self):
        """Gets the weight of this ListMembersRequest.


        :return: The weight of this ListMembersRequest.
        :rtype: list[int]
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ListMembersRequest.


        :param weight: The weight of this ListMembersRequest.
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
        if not isinstance(other, ListMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
