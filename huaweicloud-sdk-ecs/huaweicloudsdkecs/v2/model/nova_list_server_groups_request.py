# coding: utf-8

import pprint
import re

import six


class NovaListServerGroupsRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'all_projects': 'bool',
        'limit': 'int',
        'marker': 'str',
        'open_stack_api_version': 'str'
    }

    attribute_map = {
        'all_projects': 'all_projects',
        'limit': 'limit',
        'marker': 'marker',
        'open_stack_api_version': 'OpenStack-API-Version'
    }

    def __init__(self, all_projects=None, limit=None, marker=None, open_stack_api_version='compute 2.13'):  # noqa: E501
        """NovaListServerGroupsRequest - a model defined in huaweicloud sdk"""

        self._all_projects = None
        self._limit = None
        self._marker = None
        self._open_stack_api_version = None
        self.discriminator = None

        if all_projects is not None:
            self.all_projects = all_projects
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if open_stack_api_version is not None:
            self.open_stack_api_version = open_stack_api_version

    @property
    def all_projects(self):
        """Gets the all_projects of this NovaListServerGroupsRequest.


        :return: The all_projects of this NovaListServerGroupsRequest.
        :rtype: bool
        """
        return self._all_projects

    @all_projects.setter
    def all_projects(self, all_projects):
        """Sets the all_projects of this NovaListServerGroupsRequest.


        :param all_projects: The all_projects of this NovaListServerGroupsRequest.
        :type: bool
        """
        self._all_projects = all_projects

    @property
    def limit(self):
        """Gets the limit of this NovaListServerGroupsRequest.


        :return: The limit of this NovaListServerGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NovaListServerGroupsRequest.


        :param limit: The limit of this NovaListServerGroupsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NovaListServerGroupsRequest.


        :return: The marker of this NovaListServerGroupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NovaListServerGroupsRequest.


        :param marker: The marker of this NovaListServerGroupsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def open_stack_api_version(self):
        """Gets the open_stack_api_version of this NovaListServerGroupsRequest.


        :return: The open_stack_api_version of this NovaListServerGroupsRequest.
        :rtype: str
        """
        return self._open_stack_api_version

    @open_stack_api_version.setter
    def open_stack_api_version(self, open_stack_api_version):
        """Sets the open_stack_api_version of this NovaListServerGroupsRequest.


        :param open_stack_api_version: The open_stack_api_version of this NovaListServerGroupsRequest.
        :type: str
        """
        self._open_stack_api_version = open_stack_api_version

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
        if not isinstance(other, NovaListServerGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
