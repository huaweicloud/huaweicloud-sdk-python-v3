# coding: utf-8

import pprint
import re

import six


class NovaRemoveFloatingIpRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'remove_floating_ip': 'NovaRemoveFloatingIpOption'
    }

    attribute_map = {
        'remove_floating_ip': 'removeFloatingIp'
    }

    def __init__(self, remove_floating_ip=None):  # noqa: E501
        """NovaRemoveFloatingIpRequestBody - a model defined in huaweicloud sdk"""

        self._remove_floating_ip = None
        self.discriminator = None

        self.remove_floating_ip = remove_floating_ip

    @property
    def remove_floating_ip(self):
        """Gets the remove_floating_ip of this NovaRemoveFloatingIpRequestBody.


        :return: The remove_floating_ip of this NovaRemoveFloatingIpRequestBody.
        :rtype: NovaRemoveFloatingIpOption
        """
        return self._remove_floating_ip

    @remove_floating_ip.setter
    def remove_floating_ip(self, remove_floating_ip):
        """Sets the remove_floating_ip of this NovaRemoveFloatingIpRequestBody.


        :param remove_floating_ip: The remove_floating_ip of this NovaRemoveFloatingIpRequestBody.
        :type: NovaRemoveFloatingIpOption
        """
        self._remove_floating_ip = remove_floating_ip

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
        if not isinstance(other, NovaRemoveFloatingIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
