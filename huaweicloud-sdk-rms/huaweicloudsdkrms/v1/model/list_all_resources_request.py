# coding: utf-8

import pprint
import re

import six





class ListAllResourcesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'ep_id': 'str',
        'type': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'ep_id': 'ep_id',
        'type': 'type',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, region_id=None, ep_id=None, type=None, limit=None, marker=None):
        """ListAllResourcesRequest - a model defined in huaweicloud sdk"""
        
        

        self._region_id = None
        self._ep_id = None
        self._type = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if ep_id is not None:
            self.ep_id = ep_id
        if type is not None:
            self.type = type
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def region_id(self):
        """Gets the region_id of this ListAllResourcesRequest.


        :return: The region_id of this ListAllResourcesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListAllResourcesRequest.


        :param region_id: The region_id of this ListAllResourcesRequest.
        :type: str
        """
        self._region_id = region_id

    @property
    def ep_id(self):
        """Gets the ep_id of this ListAllResourcesRequest.


        :return: The ep_id of this ListAllResourcesRequest.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        """Sets the ep_id of this ListAllResourcesRequest.


        :param ep_id: The ep_id of this ListAllResourcesRequest.
        :type: str
        """
        self._ep_id = ep_id

    @property
    def type(self):
        """Gets the type of this ListAllResourcesRequest.


        :return: The type of this ListAllResourcesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListAllResourcesRequest.


        :param type: The type of this ListAllResourcesRequest.
        :type: str
        """
        self._type = type

    @property
    def limit(self):
        """Gets the limit of this ListAllResourcesRequest.


        :return: The limit of this ListAllResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAllResourcesRequest.


        :param limit: The limit of this ListAllResourcesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListAllResourcesRequest.


        :return: The marker of this ListAllResourcesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListAllResourcesRequest.


        :param marker: The marker of this ListAllResourcesRequest.
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
        if not isinstance(other, ListAllResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
