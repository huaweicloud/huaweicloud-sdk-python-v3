# coding: utf-8

import pprint
import re

import six





class ListSubNetworkInterfacesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'list[str]',
        'virsubnet_id': 'list[str]',
        'private_ip_address': 'list[str]',
        'mac_address': 'list[str]',
        'vpc_id': 'list[str]',
        'description': 'list[str]',
        'parent_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'virsubnet_id': 'virsubnet_id',
        'private_ip_address': 'private_ip_address',
        'mac_address': 'mac_address',
        'vpc_id': 'vpc_id',
        'description': 'description',
        'parent_id': 'parent_id'
    }

    def __init__(self, limit=None, marker=None, id=None, virsubnet_id=None, private_ip_address=None, mac_address=None, vpc_id=None, description=None, parent_id=None):
        """ListSubNetworkInterfacesRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._virsubnet_id = None
        self._private_ip_address = None
        self._mac_address = None
        self._vpc_id = None
        self._description = None
        self._parent_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if mac_address is not None:
            self.mac_address = mac_address
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if description is not None:
            self.description = description
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def limit(self):
        """Gets the limit of this ListSubNetworkInterfacesRequest.


        :return: The limit of this ListSubNetworkInterfacesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubNetworkInterfacesRequest.


        :param limit: The limit of this ListSubNetworkInterfacesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListSubNetworkInterfacesRequest.


        :return: The marker of this ListSubNetworkInterfacesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSubNetworkInterfacesRequest.


        :param marker: The marker of this ListSubNetworkInterfacesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListSubNetworkInterfacesRequest.


        :return: The id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListSubNetworkInterfacesRequest.


        :param id: The id of this ListSubNetworkInterfacesRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this ListSubNetworkInterfacesRequest.


        :return: The virsubnet_id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this ListSubNetworkInterfacesRequest.


        :param virsubnet_id: The virsubnet_id of this ListSubNetworkInterfacesRequest.
        :type: list[str]
        """
        self._virsubnet_id = virsubnet_id

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this ListSubNetworkInterfacesRequest.


        :return: The private_ip_address of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this ListSubNetworkInterfacesRequest.


        :param private_ip_address: The private_ip_address of this ListSubNetworkInterfacesRequest.
        :type: list[str]
        """
        self._private_ip_address = private_ip_address

    @property
    def mac_address(self):
        """Gets the mac_address of this ListSubNetworkInterfacesRequest.


        :return: The mac_address of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this ListSubNetworkInterfacesRequest.


        :param mac_address: The mac_address of this ListSubNetworkInterfacesRequest.
        :type: list[str]
        """
        self._mac_address = mac_address

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListSubNetworkInterfacesRequest.


        :return: The vpc_id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListSubNetworkInterfacesRequest.


        :param vpc_id: The vpc_id of this ListSubNetworkInterfacesRequest.
        :type: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def description(self):
        """Gets the description of this ListSubNetworkInterfacesRequest.


        :return: The description of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListSubNetworkInterfacesRequest.


        :param description: The description of this ListSubNetworkInterfacesRequest.
        :type: list[str]
        """
        self._description = description

    @property
    def parent_id(self):
        """Gets the parent_id of this ListSubNetworkInterfacesRequest.


        :return: The parent_id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ListSubNetworkInterfacesRequest.


        :param parent_id: The parent_id of this ListSubNetworkInterfacesRequest.
        :type: list[str]
        """
        self._parent_id = parent_id

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
        if not isinstance(other, ListSubNetworkInterfacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
