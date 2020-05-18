# coding: utf-8

import pprint
import re

import six


class NovaAddFloatingIpRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'add_floating_ip': 'NovaAddFloatingIpOption'
    }

    attribute_map = {
        'add_floating_ip': 'addFloatingIp'
    }

    def __init__(self, add_floating_ip=None):  # noqa: E501
        """NovaAddFloatingIpRequestBody - a model defined in huaweicloud sdk"""

        self._add_floating_ip = None
        self.discriminator = None

        self.add_floating_ip = add_floating_ip

    @property
    def add_floating_ip(self):
        """Gets the add_floating_ip of this NovaAddFloatingIpRequestBody.


        :return: The add_floating_ip of this NovaAddFloatingIpRequestBody.
        :rtype: NovaAddFloatingIpOption
        """
        return self._add_floating_ip

    @add_floating_ip.setter
    def add_floating_ip(self, add_floating_ip):
        """Sets the add_floating_ip of this NovaAddFloatingIpRequestBody.


        :param add_floating_ip: The add_floating_ip of this NovaAddFloatingIpRequestBody.
        :type: NovaAddFloatingIpOption
        """
        self._add_floating_ip = add_floating_ip

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
        if not isinstance(other, NovaAddFloatingIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
