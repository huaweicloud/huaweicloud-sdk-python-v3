# coding: utf-8

import pprint
import re

import six





class ListPortsRequest:


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
        'id': 'str',
        'limit': 'int',
        'admin_state_up': 'bool',
        'network_id': 'str',
        'mac_address': 'str',
        'device_id': 'str',
        'device_owner': 'str',
        'status': 'str',
        'marker': 'str',
        'fixed_ips': 'str',
        'enterprise_project_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'limit': 'limit',
        'admin_state_up': 'admin_state_up',
        'network_id': 'network_id',
        'mac_address': 'mac_address',
        'device_id': 'device_id',
        'device_owner': 'device_owner',
        'status': 'status',
        'marker': 'marker',
        'fixed_ips': 'fixed_ips',
        'enterprise_project_id': 'enterprise_project_id',
        'zone_id': 'zone_id'
    }

    def __init__(self, name=None, id=None, limit=2000, admin_state_up=None, network_id=None, mac_address=None, device_id=None, device_owner=None, status=None, marker=None, fixed_ips=None, enterprise_project_id=None, zone_id=None):
        """ListPortsRequest - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._id = None
        self._limit = None
        self._admin_state_up = None
        self._network_id = None
        self._mac_address = None
        self._device_id = None
        self._device_owner = None
        self._status = None
        self._marker = None
        self._fixed_ips = None
        self._enterprise_project_id = None
        self._zone_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if network_id is not None:
            self.network_id = network_id
        if mac_address is not None:
            self.mac_address = mac_address
        if device_id is not None:
            self.device_id = device_id
        if device_owner is not None:
            self.device_owner = device_owner
        if status is not None:
            self.status = status
        if marker is not None:
            self.marker = marker
        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def name(self):
        """Gets the name of this ListPortsRequest.


        :return: The name of this ListPortsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPortsRequest.


        :param name: The name of this ListPortsRequest.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ListPortsRequest.


        :return: The id of this ListPortsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPortsRequest.


        :param id: The id of this ListPortsRequest.
        :type: str
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListPortsRequest.


        :return: The limit of this ListPortsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPortsRequest.


        :param limit: The limit of this ListPortsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListPortsRequest.


        :return: The admin_state_up of this ListPortsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListPortsRequest.


        :param admin_state_up: The admin_state_up of this ListPortsRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def network_id(self):
        """Gets the network_id of this ListPortsRequest.


        :return: The network_id of this ListPortsRequest.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this ListPortsRequest.


        :param network_id: The network_id of this ListPortsRequest.
        :type: str
        """
        self._network_id = network_id

    @property
    def mac_address(self):
        """Gets the mac_address of this ListPortsRequest.


        :return: The mac_address of this ListPortsRequest.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this ListPortsRequest.


        :param mac_address: The mac_address of this ListPortsRequest.
        :type: str
        """
        self._mac_address = mac_address

    @property
    def device_id(self):
        """Gets the device_id of this ListPortsRequest.


        :return: The device_id of this ListPortsRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ListPortsRequest.


        :param device_id: The device_id of this ListPortsRequest.
        :type: str
        """
        self._device_id = device_id

    @property
    def device_owner(self):
        """Gets the device_owner of this ListPortsRequest.


        :return: The device_owner of this ListPortsRequest.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this ListPortsRequest.


        :param device_owner: The device_owner of this ListPortsRequest.
        :type: str
        """
        self._device_owner = device_owner

    @property
    def status(self):
        """Gets the status of this ListPortsRequest.


        :return: The status of this ListPortsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPortsRequest.


        :param status: The status of this ListPortsRequest.
        :type: str
        """
        self._status = status

    @property
    def marker(self):
        """Gets the marker of this ListPortsRequest.


        :return: The marker of this ListPortsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPortsRequest.


        :param marker: The marker of this ListPortsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this ListPortsRequest.


        :return: The fixed_ips of this ListPortsRequest.
        :rtype: str
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this ListPortsRequest.


        :param fixed_ips: The fixed_ips of this ListPortsRequest.
        :type: str
        """
        self._fixed_ips = fixed_ips

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPortsRequest.


        :return: The enterprise_project_id of this ListPortsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPortsRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListPortsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def zone_id(self):
        """Gets the zone_id of this ListPortsRequest.


        :return: The zone_id of this ListPortsRequest.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ListPortsRequest.


        :param zone_id: The zone_id of this ListPortsRequest.
        :type: str
        """
        self._zone_id = zone_id

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
        if not isinstance(other, ListPortsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
