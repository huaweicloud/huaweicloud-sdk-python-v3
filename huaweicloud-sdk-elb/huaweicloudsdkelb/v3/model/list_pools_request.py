# coding: utf-8

import pprint
import re

import six





class ListPoolsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'description': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'healthmonitor_id': 'list[str]',
        'id': 'list[str]',
        'ip_version': 'list[str]',
        'lb_algorithm': 'list[str]',
        'limit': 'int',
        'loadbalancer_id': 'list[str]',
        'marker': 'str',
        'member_address': 'list[str]',
        'member_deletion_protection_enable': 'bool',
        'member_device_id': 'list[str]',
        'name': 'list[str]',
        'page_reverse': 'bool',
        'protocol': 'list[str]'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'healthmonitor_id': 'healthmonitor_id',
        'id': 'id',
        'ip_version': 'ip_version',
        'lb_algorithm': 'lb_algorithm',
        'limit': 'limit',
        'loadbalancer_id': 'loadbalancer_id',
        'marker': 'marker',
        'member_address': 'member_address',
        'member_deletion_protection_enable': 'member_deletion_protection_enable',
        'member_device_id': 'member_device_id',
        'name': 'name',
        'page_reverse': 'page_reverse',
        'protocol': 'protocol'
    }

    def __init__(self, admin_state_up=None, description=None, enterprise_project_id=None, healthmonitor_id=None, id=None, ip_version=None, lb_algorithm=None, limit=None, loadbalancer_id=None, marker=None, member_address=None, member_deletion_protection_enable=None, member_device_id=None, name=None, page_reverse=None, protocol=None):
        """ListPoolsRequest - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._description = None
        self._enterprise_project_id = None
        self._healthmonitor_id = None
        self._id = None
        self._ip_version = None
        self._lb_algorithm = None
        self._limit = None
        self._loadbalancer_id = None
        self._marker = None
        self._member_address = None
        self._member_deletion_protection_enable = None
        self._member_device_id = None
        self._name = None
        self._page_reverse = None
        self._protocol = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if healthmonitor_id is not None:
            self.healthmonitor_id = healthmonitor_id
        if id is not None:
            self.id = id
        if ip_version is not None:
            self.ip_version = ip_version
        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if limit is not None:
            self.limit = limit
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if marker is not None:
            self.marker = marker
        if member_address is not None:
            self.member_address = member_address
        if member_deletion_protection_enable is not None:
            self.member_deletion_protection_enable = member_deletion_protection_enable
        if member_device_id is not None:
            self.member_device_id = member_device_id
        if name is not None:
            self.name = name
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if protocol is not None:
            self.protocol = protocol

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListPoolsRequest.


        :return: The admin_state_up of this ListPoolsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListPoolsRequest.


        :param admin_state_up: The admin_state_up of this ListPoolsRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this ListPoolsRequest.


        :return: The description of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListPoolsRequest.


        :param description: The description of this ListPoolsRequest.
        :type: list[str]
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPoolsRequest.


        :return: The enterprise_project_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPoolsRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListPoolsRequest.
        :type: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def healthmonitor_id(self):
        """Gets the healthmonitor_id of this ListPoolsRequest.


        :return: The healthmonitor_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._healthmonitor_id

    @healthmonitor_id.setter
    def healthmonitor_id(self, healthmonitor_id):
        """Sets the healthmonitor_id of this ListPoolsRequest.


        :param healthmonitor_id: The healthmonitor_id of this ListPoolsRequest.
        :type: list[str]
        """
        self._healthmonitor_id = healthmonitor_id

    @property
    def id(self):
        """Gets the id of this ListPoolsRequest.


        :return: The id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPoolsRequest.


        :param id: The id of this ListPoolsRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def ip_version(self):
        """Gets the ip_version of this ListPoolsRequest.


        :return: The ip_version of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListPoolsRequest.


        :param ip_version: The ip_version of this ListPoolsRequest.
        :type: list[str]
        """
        self._ip_version = ip_version

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this ListPoolsRequest.


        :return: The lb_algorithm of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this ListPoolsRequest.


        :param lb_algorithm: The lb_algorithm of this ListPoolsRequest.
        :type: list[str]
        """
        self._lb_algorithm = lb_algorithm

    @property
    def limit(self):
        """Gets the limit of this ListPoolsRequest.


        :return: The limit of this ListPoolsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPoolsRequest.


        :param limit: The limit of this ListPoolsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this ListPoolsRequest.


        :return: The loadbalancer_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this ListPoolsRequest.


        :param loadbalancer_id: The loadbalancer_id of this ListPoolsRequest.
        :type: list[str]
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def marker(self):
        """Gets the marker of this ListPoolsRequest.


        :return: The marker of this ListPoolsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPoolsRequest.


        :param marker: The marker of this ListPoolsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def member_address(self):
        """Gets the member_address of this ListPoolsRequest.


        :return: The member_address of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        """Sets the member_address of this ListPoolsRequest.


        :param member_address: The member_address of this ListPoolsRequest.
        :type: list[str]
        """
        self._member_address = member_address

    @property
    def member_deletion_protection_enable(self):
        """Gets the member_deletion_protection_enable of this ListPoolsRequest.


        :return: The member_deletion_protection_enable of this ListPoolsRequest.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        """Sets the member_deletion_protection_enable of this ListPoolsRequest.


        :param member_deletion_protection_enable: The member_deletion_protection_enable of this ListPoolsRequest.
        :type: bool
        """
        self._member_deletion_protection_enable = member_deletion_protection_enable

    @property
    def member_device_id(self):
        """Gets the member_device_id of this ListPoolsRequest.


        :return: The member_device_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        """Sets the member_device_id of this ListPoolsRequest.


        :param member_device_id: The member_device_id of this ListPoolsRequest.
        :type: list[str]
        """
        self._member_device_id = member_device_id

    @property
    def name(self):
        """Gets the name of this ListPoolsRequest.


        :return: The name of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPoolsRequest.


        :param name: The name of this ListPoolsRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListPoolsRequest.


        :return: The page_reverse of this ListPoolsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListPoolsRequest.


        :param page_reverse: The page_reverse of this ListPoolsRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def protocol(self):
        """Gets the protocol of this ListPoolsRequest.


        :return: The protocol of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListPoolsRequest.


        :param protocol: The protocol of this ListPoolsRequest.
        :type: list[str]
        """
        self._protocol = protocol

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
        if not isinstance(other, ListPoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
