# coding: utf-8

import pprint
import re

import six


class ListRouteTablesRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, limit=2000, marker=None, id=None, vpc_id=None, subnet_id=None):  # noqa: E501
        """ListRouteTablesRequest - a model defined in huaweicloud sdk"""

        self._limit = None
        self._marker = None
        self._id = None
        self._vpc_id = None
        self._subnet_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def limit(self):
        """Gets the limit of this ListRouteTablesRequest.


        :return: The limit of this ListRouteTablesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRouteTablesRequest.


        :param limit: The limit of this ListRouteTablesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListRouteTablesRequest.


        :return: The marker of this ListRouteTablesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListRouteTablesRequest.


        :param marker: The marker of this ListRouteTablesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListRouteTablesRequest.


        :return: The id of this ListRouteTablesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListRouteTablesRequest.


        :param id: The id of this ListRouteTablesRequest.
        :type: str
        """
        self._id = id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListRouteTablesRequest.


        :return: The vpc_id of this ListRouteTablesRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListRouteTablesRequest.


        :param vpc_id: The vpc_id of this ListRouteTablesRequest.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ListRouteTablesRequest.


        :return: The subnet_id of this ListRouteTablesRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ListRouteTablesRequest.


        :param subnet_id: The subnet_id of this ListRouteTablesRequest.
        :type: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, ListRouteTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
