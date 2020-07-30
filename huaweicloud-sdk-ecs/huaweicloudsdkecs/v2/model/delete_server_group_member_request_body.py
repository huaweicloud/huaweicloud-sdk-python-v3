# coding: utf-8

import pprint
import re

import six





class DeleteServerGroupMemberRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'remove_member': 'ServerGroupMember'
    }

    attribute_map = {
        'remove_member': 'remove_member'
    }

    def __init__(self, remove_member=None):
        """DeleteServerGroupMemberRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._remove_member = None
        self.discriminator = None

        self.remove_member = remove_member

    @property
    def remove_member(self):
        """Gets the remove_member of this DeleteServerGroupMemberRequestBody.


        :return: The remove_member of this DeleteServerGroupMemberRequestBody.
        :rtype: ServerGroupMember
        """
        return self._remove_member

    @remove_member.setter
    def remove_member(self, remove_member):
        """Sets the remove_member of this DeleteServerGroupMemberRequestBody.


        :param remove_member: The remove_member of this DeleteServerGroupMemberRequestBody.
        :type: ServerGroupMember
        """
        self._remove_member = remove_member

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
        if not isinstance(other, DeleteServerGroupMemberRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
