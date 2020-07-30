# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class NovaListServerSecurityGroupsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'security_groups': 'list[NovaSecurityGroup]'
    }

    attribute_map = {
        'security_groups': 'security_groups'
    }

    def __init__(self, security_groups=None):
        """NovaListServerSecurityGroupsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._security_groups = None
        self.discriminator = None

        if security_groups is not None:
            self.security_groups = security_groups

    @property
    def security_groups(self):
        """Gets the security_groups of this NovaListServerSecurityGroupsResponse.

        security_group列表

        :return: The security_groups of this NovaListServerSecurityGroupsResponse.
        :rtype: list[NovaSecurityGroup]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NovaListServerSecurityGroupsResponse.

        security_group列表

        :param security_groups: The security_groups of this NovaListServerSecurityGroupsResponse.
        :type: list[NovaSecurityGroup]
        """
        self._security_groups = security_groups

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
        if not isinstance(other, NovaListServerSecurityGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
