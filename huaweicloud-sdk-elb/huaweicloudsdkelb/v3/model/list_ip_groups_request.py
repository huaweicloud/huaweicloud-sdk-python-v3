# coding: utf-8

import pprint
import re

import six





class ListIpGroupsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'list[str]',
        'id': 'list[str]',
        'ip_list': 'list[str]',
        'limit': 'int',
        'marker': 'str',
        'name': 'list[str]',
        'page_reverse': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'ip_list': 'ip_list',
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name',
        'page_reverse': 'page_reverse'
    }

    def __init__(self, description=None, id=None, ip_list=None, limit=None, marker=None, name=None, page_reverse=None):
        """ListIpGroupsRequest - a model defined in huaweicloud sdk"""
        
        

        self._description = None
        self._id = None
        self._ip_list = None
        self._limit = None
        self._marker = None
        self._name = None
        self._page_reverse = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if ip_list is not None:
            self.ip_list = ip_list
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if page_reverse is not None:
            self.page_reverse = page_reverse

    @property
    def description(self):
        """Gets the description of this ListIpGroupsRequest.


        :return: The description of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListIpGroupsRequest.


        :param description: The description of this ListIpGroupsRequest.
        :type: list[str]
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this ListIpGroupsRequest.


        :return: The id of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListIpGroupsRequest.


        :param id: The id of this ListIpGroupsRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def ip_list(self):
        """Gets the ip_list of this ListIpGroupsRequest.


        :return: The ip_list of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this ListIpGroupsRequest.


        :param ip_list: The ip_list of this ListIpGroupsRequest.
        :type: list[str]
        """
        self._ip_list = ip_list

    @property
    def limit(self):
        """Gets the limit of this ListIpGroupsRequest.


        :return: The limit of this ListIpGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIpGroupsRequest.


        :param limit: The limit of this ListIpGroupsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListIpGroupsRequest.


        :return: The marker of this ListIpGroupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListIpGroupsRequest.


        :param marker: The marker of this ListIpGroupsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListIpGroupsRequest.


        :return: The name of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListIpGroupsRequest.


        :param name: The name of this ListIpGroupsRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListIpGroupsRequest.


        :return: The page_reverse of this ListIpGroupsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListIpGroupsRequest.


        :param page_reverse: The page_reverse of this ListIpGroupsRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

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
        if not isinstance(other, ListIpGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
