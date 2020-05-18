# coding: utf-8

import pprint
import re

import six


class NeutronListNetworksResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'networks': 'list[NeutronNetwork]',
        'networks_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'networks': 'networks',
        'networks_links': 'networks_links'
    }

    def __init__(self, networks=None, networks_links=None):  # noqa: E501
        """NeutronListNetworksResponse - a model defined in huaweicloud sdk"""

        self._networks = None
        self._networks_links = None
        self.discriminator = None

        if networks is not None:
            self.networks = networks
        if networks_links is not None:
            self.networks_links = networks_links

    @property
    def networks(self):
        """Gets the networks of this NeutronListNetworksResponse.

        network对象列表

        :return: The networks of this NeutronListNetworksResponse.
        :rtype: list[NeutronNetwork]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this NeutronListNetworksResponse.

        network对象列表

        :param networks: The networks of this NeutronListNetworksResponse.
        :type: list[NeutronNetwork]
        """
        self._networks = networks

    @property
    def networks_links(self):
        """Gets the networks_links of this NeutronListNetworksResponse.

        分页信息

        :return: The networks_links of this NeutronListNetworksResponse.
        :rtype: list[NeutronPageLink]
        """
        return self._networks_links

    @networks_links.setter
    def networks_links(self, networks_links):
        """Sets the networks_links of this NeutronListNetworksResponse.

        分页信息

        :param networks_links: The networks_links of this NeutronListNetworksResponse.
        :type: list[NeutronPageLink]
        """
        self._networks_links = networks_links

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
        if not isinstance(other, NeutronListNetworksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
