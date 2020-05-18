# coding: utf-8

import pprint
import re

import six


class ListIpAddressGroupRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'ip_version': 'int',
        'description': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ip_version': 'ip_version',
        'description': 'description',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, id=None, name=None, ip_version=None, description=None, limit=None, marker=None):  # noqa: E501
        """ListIpAddressGroupRequest - a model defined in huaweicloud sdk"""

        self._id = None
        self._name = None
        self._ip_version = None
        self._description = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ip_version is not None:
            self.ip_version = ip_version
        if description is not None:
            self.description = description
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def id(self):
        """Gets the id of this ListIpAddressGroupRequest.


        :return: The id of this ListIpAddressGroupRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListIpAddressGroupRequest.


        :param id: The id of this ListIpAddressGroupRequest.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListIpAddressGroupRequest.


        :return: The name of this ListIpAddressGroupRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListIpAddressGroupRequest.


        :param name: The name of this ListIpAddressGroupRequest.
        :type: str
        """
        self._name = name

    @property
    def ip_version(self):
        """Gets the ip_version of this ListIpAddressGroupRequest.


        :return: The ip_version of this ListIpAddressGroupRequest.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListIpAddressGroupRequest.


        :param ip_version: The ip_version of this ListIpAddressGroupRequest.
        :type: int
        """
        self._ip_version = ip_version

    @property
    def description(self):
        """Gets the description of this ListIpAddressGroupRequest.


        :return: The description of this ListIpAddressGroupRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListIpAddressGroupRequest.


        :param description: The description of this ListIpAddressGroupRequest.
        :type: str
        """
        self._description = description

    @property
    def limit(self):
        """Gets the limit of this ListIpAddressGroupRequest.


        :return: The limit of this ListIpAddressGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIpAddressGroupRequest.


        :param limit: The limit of this ListIpAddressGroupRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListIpAddressGroupRequest.


        :return: The marker of this ListIpAddressGroupRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListIpAddressGroupRequest.


        :param marker: The marker of this ListIpAddressGroupRequest.
        :type: str
        """
        self._marker = marker

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
        if not isinstance(other, ListIpAddressGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
