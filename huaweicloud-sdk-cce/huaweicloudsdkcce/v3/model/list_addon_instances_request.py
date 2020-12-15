# coding: utf-8

import pprint
import re

import six





class ListAddonInstancesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, content_type='application/json', cluster_id=None):
        """ListAddonInstancesRequest - a model defined in huaweicloud sdk"""
        
        

        self._content_type = None
        self._cluster_id = None
        self.discriminator = None

        self.content_type = content_type
        self.cluster_id = cluster_id

    @property
    def content_type(self):
        """Gets the content_type of this ListAddonInstancesRequest.


        :return: The content_type of this ListAddonInstancesRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ListAddonInstancesRequest.


        :param content_type: The content_type of this ListAddonInstancesRequest.
        :type: str
        """
        self._content_type = content_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListAddonInstancesRequest.


        :return: The cluster_id of this ListAddonInstancesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListAddonInstancesRequest.


        :param cluster_id: The cluster_id of this ListAddonInstancesRequest.
        :type: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, ListAddonInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
