# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListCustomPoliciesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'links': 'Links',
        'roles': 'list[PolicyRoleResult]',
        'total_number': 'int'
    }

    attribute_map = {
        'links': 'links',
        'roles': 'roles',
        'total_number': 'total_number'
    }

    def __init__(self, links=None, roles=None, total_number=None):
        """ListCustomPoliciesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._links = None
        self._roles = None
        self._total_number = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if roles is not None:
            self.roles = roles
        if total_number is not None:
            self.total_number = total_number

    @property
    def links(self):
        """Gets the links of this ListCustomPoliciesResponse.


        :return: The links of this ListCustomPoliciesResponse.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ListCustomPoliciesResponse.


        :param links: The links of this ListCustomPoliciesResponse.
        :type: Links
        """
        self._links = links

    @property
    def roles(self):
        """Gets the roles of this ListCustomPoliciesResponse.

        自定义策略信息列表。

        :return: The roles of this ListCustomPoliciesResponse.
        :rtype: list[PolicyRoleResult]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this ListCustomPoliciesResponse.

        自定义策略信息列表。

        :param roles: The roles of this ListCustomPoliciesResponse.
        :type: list[PolicyRoleResult]
        """
        self._roles = roles

    @property
    def total_number(self):
        """Gets the total_number of this ListCustomPoliciesResponse.

        返回自定义策略的总条数

        :return: The total_number of this ListCustomPoliciesResponse.
        :rtype: int
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        """Sets the total_number of this ListCustomPoliciesResponse.

        返回自定义策略的总条数

        :param total_number: The total_number of this ListCustomPoliciesResponse.
        :type: int
        """
        self._total_number = total_number

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
        if not isinstance(other, ListCustomPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
