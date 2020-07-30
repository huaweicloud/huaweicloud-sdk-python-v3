# coding: utf-8

import pprint
import re

import six





class NovaListKeypairsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'open_stack_api_version': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'open_stack_api_version': 'OpenStack-API-Version'
    }

    def __init__(self, limit=None, marker=None, open_stack_api_version=None):
        """NovaListKeypairsRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._marker = None
        self._open_stack_api_version = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if open_stack_api_version is not None:
            self.open_stack_api_version = open_stack_api_version

    @property
    def limit(self):
        """Gets the limit of this NovaListKeypairsRequest.


        :return: The limit of this NovaListKeypairsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NovaListKeypairsRequest.


        :param limit: The limit of this NovaListKeypairsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this NovaListKeypairsRequest.


        :return: The marker of this NovaListKeypairsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this NovaListKeypairsRequest.


        :param marker: The marker of this NovaListKeypairsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def open_stack_api_version(self):
        """Gets the open_stack_api_version of this NovaListKeypairsRequest.


        :return: The open_stack_api_version of this NovaListKeypairsRequest.
        :rtype: str
        """
        return self._open_stack_api_version

    @open_stack_api_version.setter
    def open_stack_api_version(self, open_stack_api_version):
        """Sets the open_stack_api_version of this NovaListKeypairsRequest.


        :param open_stack_api_version: The open_stack_api_version of this NovaListKeypairsRequest.
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
        if not isinstance(other, NovaListKeypairsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
