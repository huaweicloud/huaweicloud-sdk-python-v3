# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class NeutronListFloatingIpsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'floatingips': 'list[FloatingIpResp]',
        'floatingips_links': 'list[Pager]'
    }

    attribute_map = {
        'floatingips': 'floatingips',
        'floatingips_links': 'floatingips_links'
    }

    def __init__(self, floatingips=None, floatingips_links=None):
        """NeutronListFloatingIpsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._floatingips = None
        self._floatingips_links = None
        self.discriminator = None

        if floatingips is not None:
            self.floatingips = floatingips
        if floatingips_links is not None:
            self.floatingips_links = floatingips_links

    @property
    def floatingips(self):
        """Gets the floatingips of this NeutronListFloatingIpsResponse.

        floatingip对象列表

        :return: The floatingips of this NeutronListFloatingIpsResponse.
        :rtype: list[FloatingIpResp]
        """
        return self._floatingips

    @floatingips.setter
    def floatingips(self, floatingips):
        """Sets the floatingips of this NeutronListFloatingIpsResponse.

        floatingip对象列表

        :param floatingips: The floatingips of this NeutronListFloatingIpsResponse.
        :type: list[FloatingIpResp]
        """
        self._floatingips = floatingips

    @property
    def floatingips_links(self):
        """Gets the floatingips_links of this NeutronListFloatingIpsResponse.

        marker分页结构

        :return: The floatingips_links of this NeutronListFloatingIpsResponse.
        :rtype: list[Pager]
        """
        return self._floatingips_links

    @floatingips_links.setter
    def floatingips_links(self, floatingips_links):
        """Sets the floatingips_links of this NeutronListFloatingIpsResponse.

        marker分页结构

        :param floatingips_links: The floatingips_links of this NeutronListFloatingIpsResponse.
        :type: list[Pager]
        """
        self._floatingips_links = floatingips_links

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
        if not isinstance(other, NeutronListFloatingIpsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
