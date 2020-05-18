# coding: utf-8

import pprint
import re

import six


class NovaShowFloatingIpRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'floating_ip_id': 'str'
    }

    attribute_map = {
        'floating_ip_id': 'floating_ip_id'
    }

    def __init__(self, floating_ip_id=None):  # noqa: E501
        """NovaShowFloatingIpRequest - a model defined in huaweicloud sdk"""

        self._floating_ip_id = None
        self.discriminator = None

        self.floating_ip_id = floating_ip_id

    @property
    def floating_ip_id(self):
        """Gets the floating_ip_id of this NovaShowFloatingIpRequest.


        :return: The floating_ip_id of this NovaShowFloatingIpRequest.
        :rtype: str
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        """Sets the floating_ip_id of this NovaShowFloatingIpRequest.


        :param floating_ip_id: The floating_ip_id of this NovaShowFloatingIpRequest.
        :type: str
        """
        self._floating_ip_id = floating_ip_id

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
        if not isinstance(other, NovaShowFloatingIpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
