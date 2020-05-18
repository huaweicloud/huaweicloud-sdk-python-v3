# coding: utf-8

import pprint
import re

import six


class NeutronListSubnetsResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'subnets': 'list[NeutronSubnet]',
        'subnets_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'subnets': 'subnets',
        'subnets_links': 'subnets_links'
    }

    def __init__(self, subnets=None, subnets_links=None):  # noqa: E501
        """NeutronListSubnetsResponse - a model defined in huaweicloud sdk"""

        self._subnets = None
        self._subnets_links = None
        self.discriminator = None

        if subnets is not None:
            self.subnets = subnets
        if subnets_links is not None:
            self.subnets_links = subnets_links

    @property
    def subnets(self):
        """Gets the subnets of this NeutronListSubnetsResponse.

        subnet对象列表

        :return: The subnets of this NeutronListSubnetsResponse.
        :rtype: list[NeutronSubnet]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this NeutronListSubnetsResponse.

        subnet对象列表

        :param subnets: The subnets of this NeutronListSubnetsResponse.
        :type: list[NeutronSubnet]
        """
        self._subnets = subnets

    @property
    def subnets_links(self):
        """Gets the subnets_links of this NeutronListSubnetsResponse.

        分页信息

        :return: The subnets_links of this NeutronListSubnetsResponse.
        :rtype: list[NeutronPageLink]
        """
        return self._subnets_links

    @subnets_links.setter
    def subnets_links(self, subnets_links):
        """Sets the subnets_links of this NeutronListSubnetsResponse.

        分页信息

        :param subnets_links: The subnets_links of this NeutronListSubnetsResponse.
        :type: list[NeutronPageLink]
        """
        self._subnets_links = subnets_links

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
        if not isinstance(other, NeutronListSubnetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
