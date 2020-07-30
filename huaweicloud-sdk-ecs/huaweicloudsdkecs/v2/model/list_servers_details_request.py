# coding: utf-8

import pprint
import re

import six





class ListServersDetailsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'flavor': 'str',
        'ip': 'str',
        'limit': 'int',
        'name': 'str',
        'not_tags': 'str',
        'offset': 'int',
        'reservation_id': 'str',
        'status': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'flavor': 'flavor',
        'ip': 'ip',
        'limit': 'limit',
        'name': 'name',
        'not_tags': 'not-tags',
        'offset': 'offset',
        'reservation_id': 'reservation_id',
        'status': 'status',
        'tags': 'tags'
    }

    def __init__(self, enterprise_project_id=None, flavor=None, ip=None, limit=25, name=None, not_tags=None, offset=1, reservation_id=None, status=None, tags=None):
        """ListServersDetailsRequest - a model defined in huaweicloud sdk"""
        
        

        self._enterprise_project_id = None
        self._flavor = None
        self._ip = None
        self._limit = None
        self._name = None
        self._not_tags = None
        self._offset = None
        self._reservation_id = None
        self._status = None
        self._tags = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if flavor is not None:
            self.flavor = flavor
        if ip is not None:
            self.ip = ip
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if not_tags is not None:
            self.not_tags = not_tags
        if offset is not None:
            self.offset = offset
        if reservation_id is not None:
            self.reservation_id = reservation_id
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListServersDetailsRequest.


        :return: The enterprise_project_id of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListServersDetailsRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListServersDetailsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def flavor(self):
        """Gets the flavor of this ListServersDetailsRequest.


        :return: The flavor of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ListServersDetailsRequest.


        :param flavor: The flavor of this ListServersDetailsRequest.
        :type: str
        """
        self._flavor = flavor

    @property
    def ip(self):
        """Gets the ip of this ListServersDetailsRequest.


        :return: The ip of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListServersDetailsRequest.


        :param ip: The ip of this ListServersDetailsRequest.
        :type: str
        """
        self._ip = ip

    @property
    def limit(self):
        """Gets the limit of this ListServersDetailsRequest.


        :return: The limit of this ListServersDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListServersDetailsRequest.


        :param limit: The limit of this ListServersDetailsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListServersDetailsRequest.


        :return: The name of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListServersDetailsRequest.


        :param name: The name of this ListServersDetailsRequest.
        :type: str
        """
        self._name = name

    @property
    def not_tags(self):
        """Gets the not_tags of this ListServersDetailsRequest.


        :return: The not_tags of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._not_tags

    @not_tags.setter
    def not_tags(self, not_tags):
        """Sets the not_tags of this ListServersDetailsRequest.


        :param not_tags: The not_tags of this ListServersDetailsRequest.
        :type: str
        """
        self._not_tags = not_tags

    @property
    def offset(self):
        """Gets the offset of this ListServersDetailsRequest.


        :return: The offset of this ListServersDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListServersDetailsRequest.


        :param offset: The offset of this ListServersDetailsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def reservation_id(self):
        """Gets the reservation_id of this ListServersDetailsRequest.


        :return: The reservation_id of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._reservation_id

    @reservation_id.setter
    def reservation_id(self, reservation_id):
        """Sets the reservation_id of this ListServersDetailsRequest.


        :param reservation_id: The reservation_id of this ListServersDetailsRequest.
        :type: str
        """
        self._reservation_id = reservation_id

    @property
    def status(self):
        """Gets the status of this ListServersDetailsRequest.


        :return: The status of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListServersDetailsRequest.


        :param status: The status of this ListServersDetailsRequest.
        :type: str
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ListServersDetailsRequest.


        :return: The tags of this ListServersDetailsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListServersDetailsRequest.


        :param tags: The tags of this ListServersDetailsRequest.
        :type: str
        """
        self._tags = tags

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
        if not isinstance(other, ListServersDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
