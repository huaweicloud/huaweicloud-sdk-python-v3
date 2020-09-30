# coding: utf-8

import pprint
import re

import six





class ListPublicipsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'ip_version': 'int',
        'enterprise_project_id': 'str',
        'port_id': 'list[str]',
        'public_ip_address': 'list[str]',
        'private_ip_address': 'list[str]',
        'id': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'ip_version': 'ip_version',
        'enterprise_project_id': 'enterprise_project_id',
        'port_id': 'port_id',
        'public_ip_address': 'public_ip_address',
        'private_ip_address': 'private_ip_address',
        'id': 'id'
    }

    def __init__(self, marker=None, limit=None, ip_version=None, enterprise_project_id=None, port_id=None, public_ip_address=None, private_ip_address=None, id=None):
        """ListPublicipsRequest - a model defined in huaweicloud sdk"""
        
        

        self._marker = None
        self._limit = None
        self._ip_version = None
        self._enterprise_project_id = None
        self._port_id = None
        self._public_ip_address = None
        self._private_ip_address = None
        self._id = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if ip_version is not None:
            self.ip_version = ip_version
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if port_id is not None:
            self.port_id = port_id
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if id is not None:
            self.id = id

    @property
    def marker(self):
        """Gets the marker of this ListPublicipsRequest.


        :return: The marker of this ListPublicipsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPublicipsRequest.


        :param marker: The marker of this ListPublicipsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListPublicipsRequest.


        :return: The limit of this ListPublicipsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPublicipsRequest.


        :param limit: The limit of this ListPublicipsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def ip_version(self):
        """Gets the ip_version of this ListPublicipsRequest.


        :return: The ip_version of this ListPublicipsRequest.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListPublicipsRequest.


        :param ip_version: The ip_version of this ListPublicipsRequest.
        :type: int
        """
        self._ip_version = ip_version

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPublicipsRequest.


        :return: The enterprise_project_id of this ListPublicipsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPublicipsRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListPublicipsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def port_id(self):
        """Gets the port_id of this ListPublicipsRequest.


        :return: The port_id of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this ListPublicipsRequest.


        :param port_id: The port_id of this ListPublicipsRequest.
        :type: list[str]
        """
        self._port_id = port_id

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this ListPublicipsRequest.


        :return: The public_ip_address of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this ListPublicipsRequest.


        :param public_ip_address: The public_ip_address of this ListPublicipsRequest.
        :type: list[str]
        """
        self._public_ip_address = public_ip_address

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this ListPublicipsRequest.


        :return: The private_ip_address of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this ListPublicipsRequest.


        :param private_ip_address: The private_ip_address of this ListPublicipsRequest.
        :type: list[str]
        """
        self._private_ip_address = private_ip_address

    @property
    def id(self):
        """Gets the id of this ListPublicipsRequest.


        :return: The id of this ListPublicipsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPublicipsRequest.


        :param id: The id of this ListPublicipsRequest.
        :type: list[str]
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListPublicipsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
