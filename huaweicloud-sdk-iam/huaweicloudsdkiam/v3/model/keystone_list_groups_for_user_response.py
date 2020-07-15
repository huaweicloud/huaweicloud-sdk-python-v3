# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class KeystoneListGroupsForUserResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'groups': 'list[KeystoneGroupResult]',
        'links': 'Links'
    }

    attribute_map = {
        'groups': 'groups',
        'links': 'links'
    }

    def __init__(self, groups=None, links=None):
        """KeystoneListGroupsForUserResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._groups = None
        self._links = None
        self.discriminator = None

        if groups is not None:
            self.groups = groups
        if links is not None:
            self.links = links

    @property
    def groups(self):
        """Gets the groups of this KeystoneListGroupsForUserResponse.

        用户组信息列表。

        :return: The groups of this KeystoneListGroupsForUserResponse.
        :rtype: list[KeystoneGroupResult]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this KeystoneListGroupsForUserResponse.

        用户组信息列表。

        :param groups: The groups of this KeystoneListGroupsForUserResponse.
        :type: list[KeystoneGroupResult]
        """
        self._groups = groups

    @property
    def links(self):
        """Gets the links of this KeystoneListGroupsForUserResponse.


        :return: The links of this KeystoneListGroupsForUserResponse.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this KeystoneListGroupsForUserResponse.


        :param links: The links of this KeystoneListGroupsForUserResponse.
        :type: Links
        """
        self._links = links

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
        if not isinstance(other, KeystoneListGroupsForUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
