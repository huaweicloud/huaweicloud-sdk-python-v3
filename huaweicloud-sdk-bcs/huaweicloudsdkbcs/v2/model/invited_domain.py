# coding: utf-8

import pprint
import re

import six





class InvitedDomain:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'invited_username': 'str'
    }

    attribute_map = {
        'invited_username': 'invited_username'
    }

    def __init__(self, invited_username=None):
        """InvitedDomain - a model defined in huaweicloud sdk"""
        
        

        self._invited_username = None
        self.discriminator = None

        if invited_username is not None:
            self.invited_username = invited_username

    @property
    def invited_username(self):
        """Gets the invited_username of this InvitedDomain.

        被邀请方租户名

        :return: The invited_username of this InvitedDomain.
        :rtype: str
        """
        return self._invited_username

    @invited_username.setter
    def invited_username(self, invited_username):
        """Sets the invited_username of this InvitedDomain.

        被邀请方租户名

        :param invited_username: The invited_username of this InvitedDomain.
        :type: str
        """
        self._invited_username = invited_username

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
        if not isinstance(other, InvitedDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
