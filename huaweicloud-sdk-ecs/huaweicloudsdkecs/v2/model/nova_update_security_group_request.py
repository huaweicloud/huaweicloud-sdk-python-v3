# coding: utf-8

import pprint
import re

import six


class NovaUpdateSecurityGroupRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'security_group_id': 'str',
        'body': 'NovaUpdateSecurityGroupRequestBody'
    }

    attribute_map = {
        'security_group_id': 'security_group_id',
        'body': 'body'
    }

    def __init__(self, security_group_id=None, body=None):  # noqa: E501
        """NovaUpdateSecurityGroupRequest - a model defined in huaweicloud sdk"""

        self._security_group_id = None
        self._body = None
        self.discriminator = None

        self.security_group_id = security_group_id
        if body is not None:
            self.body = body

    @property
    def security_group_id(self):
        """Gets the security_group_id of this NovaUpdateSecurityGroupRequest.


        :return: The security_group_id of this NovaUpdateSecurityGroupRequest.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this NovaUpdateSecurityGroupRequest.


        :param security_group_id: The security_group_id of this NovaUpdateSecurityGroupRequest.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def body(self):
        """Gets the body of this NovaUpdateSecurityGroupRequest.


        :return: The body of this NovaUpdateSecurityGroupRequest.
        :rtype: NovaUpdateSecurityGroupRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this NovaUpdateSecurityGroupRequest.


        :param body: The body of this NovaUpdateSecurityGroupRequest.
        :type: NovaUpdateSecurityGroupRequestBody
        """
        self._body = body

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
        if not isinstance(other, NovaUpdateSecurityGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
