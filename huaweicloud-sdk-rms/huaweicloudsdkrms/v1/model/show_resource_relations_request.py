# coding: utf-8

import pprint
import re

import six





class ShowResourceRelationsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'direction': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'direction': 'direction',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, resource_id=None, direction=None, limit=None, marker=None):
        """ShowResourceRelationsRequest - a model defined in huaweicloud sdk"""
        
        

        self._resource_id = None
        self._direction = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.resource_id = resource_id
        self.direction = direction
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def resource_id(self):
        """Gets the resource_id of this ShowResourceRelationsRequest.


        :return: The resource_id of this ShowResourceRelationsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ShowResourceRelationsRequest.


        :param resource_id: The resource_id of this ShowResourceRelationsRequest.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def direction(self):
        """Gets the direction of this ShowResourceRelationsRequest.


        :return: The direction of this ShowResourceRelationsRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ShowResourceRelationsRequest.


        :param direction: The direction of this ShowResourceRelationsRequest.
        :type: str
        """
        self._direction = direction

    @property
    def limit(self):
        """Gets the limit of this ShowResourceRelationsRequest.


        :return: The limit of this ShowResourceRelationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowResourceRelationsRequest.


        :param limit: The limit of this ShowResourceRelationsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ShowResourceRelationsRequest.


        :return: The marker of this ShowResourceRelationsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ShowResourceRelationsRequest.


        :param marker: The marker of this ShowResourceRelationsRequest.
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
        if not isinstance(other, ShowResourceRelationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
