# coding: utf-8

import pprint
import re

import six





class ListBandwidthsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'enterprise_project_id': 'str',
        'share_type': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'enterprise_project_id': 'enterprise_project_id',
        'share_type': 'share_type'
    }

    def __init__(self, marker=None, limit=None, enterprise_project_id=None, share_type=None):
        """ListBandwidthsRequest - a model defined in huaweicloud sdk"""
        
        

        self._marker = None
        self._limit = None
        self._enterprise_project_id = None
        self._share_type = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if share_type is not None:
            self.share_type = share_type

    @property
    def marker(self):
        """Gets the marker of this ListBandwidthsRequest.


        :return: The marker of this ListBandwidthsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListBandwidthsRequest.


        :param marker: The marker of this ListBandwidthsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListBandwidthsRequest.


        :return: The limit of this ListBandwidthsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBandwidthsRequest.


        :param limit: The limit of this ListBandwidthsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListBandwidthsRequest.


        :return: The enterprise_project_id of this ListBandwidthsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListBandwidthsRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListBandwidthsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def share_type(self):
        """Gets the share_type of this ListBandwidthsRequest.


        :return: The share_type of this ListBandwidthsRequest.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this ListBandwidthsRequest.


        :param share_type: The share_type of this ListBandwidthsRequest.
        :type: str
        """
        self._share_type = share_type

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
        if not isinstance(other, ListBandwidthsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
