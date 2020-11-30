# coding: utf-8

import pprint
import re

import six





class ListMonitoredObjectsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dim_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'dim_name': 'dim_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, dim_name=None, offset=0, limit=10):
        """ListMonitoredObjectsRequest - a model defined in huaweicloud sdk"""
        
        

        self._dim_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.dim_name = dim_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def dim_name(self):
        """Gets the dim_name of this ListMonitoredObjectsRequest.


        :return: The dim_name of this ListMonitoredObjectsRequest.
        :rtype: str
        """
        return self._dim_name

    @dim_name.setter
    def dim_name(self, dim_name):
        """Sets the dim_name of this ListMonitoredObjectsRequest.


        :param dim_name: The dim_name of this ListMonitoredObjectsRequest.
        :type: str
        """
        self._dim_name = dim_name

    @property
    def offset(self):
        """Gets the offset of this ListMonitoredObjectsRequest.


        :return: The offset of this ListMonitoredObjectsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListMonitoredObjectsRequest.


        :param offset: The offset of this ListMonitoredObjectsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListMonitoredObjectsRequest.


        :return: The limit of this ListMonitoredObjectsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMonitoredObjectsRequest.


        :param limit: The limit of this ListMonitoredObjectsRequest.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ListMonitoredObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
