# coding: utf-8

import pprint
import re

import six





class ListResourcesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'provider': 'str',
        'type': 'str',
        'region_id': 'str',
        'ep_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'type': 'type',
        'region_id': 'region_id',
        'ep_id': 'ep_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, provider=None, type=None, region_id=None, ep_id=None, limit=None, marker=None):
        """ListResourcesRequest - a model defined in huaweicloud sdk"""
        
        

        self._provider = None
        self._type = None
        self._region_id = None
        self._ep_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.provider = provider
        self.type = type
        if region_id is not None:
            self.region_id = region_id
        if ep_id is not None:
            self.ep_id = ep_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def provider(self):
        """Gets the provider of this ListResourcesRequest.


        :return: The provider of this ListResourcesRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ListResourcesRequest.


        :param provider: The provider of this ListResourcesRequest.
        :type: str
        """
        self._provider = provider

    @property
    def type(self):
        """Gets the type of this ListResourcesRequest.


        :return: The type of this ListResourcesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListResourcesRequest.


        :param type: The type of this ListResourcesRequest.
        :type: str
        """
        self._type = type

    @property
    def region_id(self):
        """Gets the region_id of this ListResourcesRequest.


        :return: The region_id of this ListResourcesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ListResourcesRequest.


        :param region_id: The region_id of this ListResourcesRequest.
        :type: str
        """
        self._region_id = region_id

    @property
    def ep_id(self):
        """Gets the ep_id of this ListResourcesRequest.


        :return: The ep_id of this ListResourcesRequest.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        """Sets the ep_id of this ListResourcesRequest.


        :param ep_id: The ep_id of this ListResourcesRequest.
        :type: str
        """
        self._ep_id = ep_id

    @property
    def limit(self):
        """Gets the limit of this ListResourcesRequest.


        :return: The limit of this ListResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResourcesRequest.


        :param limit: The limit of this ListResourcesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListResourcesRequest.


        :return: The marker of this ListResourcesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListResourcesRequest.


        :param marker: The marker of this ListResourcesRequest.
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
        if not isinstance(other, ListResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
