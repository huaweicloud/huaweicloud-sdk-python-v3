# coding: utf-8

import pprint
import re

import six





class ListServerGroupsPageInfoResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'next_marker': 'str'
    }

    attribute_map = {
        'next_marker': 'next_marker'
    }

    def __init__(self, next_marker=None):
        """ListServerGroupsPageInfoResult - a model defined in huaweicloud sdk"""
        
        

        self._next_marker = None
        self.discriminator = None

        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def next_marker(self):
        """Gets the next_marker of this ListServerGroupsPageInfoResult.

        

        :return: The next_marker of this ListServerGroupsPageInfoResult.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ListServerGroupsPageInfoResult.

        

        :param next_marker: The next_marker of this ListServerGroupsPageInfoResult.
        :type: str
        """
        self._next_marker = next_marker

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
        if not isinstance(other, ListServerGroupsPageInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
