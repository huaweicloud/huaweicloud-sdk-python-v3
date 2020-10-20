# coding: utf-8

import pprint
import re

import six





class ListMenbersRequest:


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
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'str',
        'name': 'str',
        'address': 'str',
        'protocol_port': 'int',
        'subnet_id': 'str',
        'admin_state_up': 'bool',
        'weight': 'int'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'address': 'address',
        'protocol_port': 'protocol_port',
        'subnet_id': 'subnet_id',
        'admin_state_up': 'admin_state_up',
        'weight': 'weight'
    }

    def __init__(self, pool_id=None, limit=None, marker=None, page_reverse=None, id=None, name=None, address=None, protocol_port=None, subnet_id=None, admin_state_up=None, weight=None):
        """ListMenbersRequest - a model defined in huaweicloud sdk"""
        
        

        self._pool_id = None
        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._address = None
        self._protocol_port = None
        self._subnet_id = None
        self._admin_state_up = None
        self._weight = None
        self.discriminator = None

        self.pool_id = pool_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if weight is not None:
            self.weight = weight

    @property
    def pool_id(self):
        """Gets the pool_id of this ListMenbersRequest.


        :return: The pool_id of this ListMenbersRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this ListMenbersRequest.


        :param pool_id: The pool_id of this ListMenbersRequest.
        :type: str
        """
        self._pool_id = pool_id

    @property
    def limit(self):
        """Gets the limit of this ListMenbersRequest.


        :return: The limit of this ListMenbersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMenbersRequest.


        :param limit: The limit of this ListMenbersRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListMenbersRequest.


        :return: The marker of this ListMenbersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListMenbersRequest.


        :param marker: The marker of this ListMenbersRequest.
        :type: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListMenbersRequest.


        :return: The page_reverse of this ListMenbersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListMenbersRequest.


        :param page_reverse: The page_reverse of this ListMenbersRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListMenbersRequest.


        :return: The id of this ListMenbersRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListMenbersRequest.


        :param id: The id of this ListMenbersRequest.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListMenbersRequest.


        :return: The name of this ListMenbersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListMenbersRequest.


        :param name: The name of this ListMenbersRequest.
        :type: str
        """
        self._name = name

    @property
    def address(self):
        """Gets the address of this ListMenbersRequest.


        :return: The address of this ListMenbersRequest.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ListMenbersRequest.


        :param address: The address of this ListMenbersRequest.
        :type: str
        """
        self._address = address

    @property
    def protocol_port(self):
        """Gets the protocol_port of this ListMenbersRequest.


        :return: The protocol_port of this ListMenbersRequest.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this ListMenbersRequest.


        :param protocol_port: The protocol_port of this ListMenbersRequest.
        :type: int
        """
        self._protocol_port = protocol_port

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ListMenbersRequest.


        :return: The subnet_id of this ListMenbersRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ListMenbersRequest.


        :param subnet_id: The subnet_id of this ListMenbersRequest.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListMenbersRequest.


        :return: The admin_state_up of this ListMenbersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListMenbersRequest.


        :param admin_state_up: The admin_state_up of this ListMenbersRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def weight(self):
        """Gets the weight of this ListMenbersRequest.


        :return: The weight of this ListMenbersRequest.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ListMenbersRequest.


        :param weight: The weight of this ListMenbersRequest.
        :type: int
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
        if not isinstance(other, ListMenbersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
