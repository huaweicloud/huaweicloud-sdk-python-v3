# coding: utf-8

import pprint
import re

import six





class ListPrivateipsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'subnet_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, subnet_id=None, limit=2000, marker=None):
        """ListPrivateipsRequest - a model defined in huaweicloud sdk"""
        
        

        self._subnet_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.subnet_id = subnet_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ListPrivateipsRequest.


        :return: The subnet_id of this ListPrivateipsRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ListPrivateipsRequest.


        :param subnet_id: The subnet_id of this ListPrivateipsRequest.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def limit(self):
        """Gets the limit of this ListPrivateipsRequest.


        :return: The limit of this ListPrivateipsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPrivateipsRequest.


        :param limit: The limit of this ListPrivateipsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPrivateipsRequest.


        :return: The marker of this ListPrivateipsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPrivateipsRequest.


        :param marker: The marker of this ListPrivateipsRequest.
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
        if not isinstance(other, ListPrivateipsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
