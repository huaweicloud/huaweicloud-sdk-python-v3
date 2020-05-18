# coding: utf-8

import pprint
import re

import six


class NovaProjectLimits(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'rate': 'list[NovaSpaceObject]',
        'absolute': 'NovaProjectLimitsAbsolute'
    }

    attribute_map = {
        'rate': 'rate',
        'absolute': 'absolute'
    }

    def __init__(self, rate=None, absolute=None):  # noqa: E501
        """NovaProjectLimits - a model defined in huaweicloud sdk"""

        self._rate = None
        self._absolute = None
        self.discriminator = None

        if rate is not None:
            self.rate = rate
        self.absolute = absolute

    @property
    def rate(self):
        """Gets the rate of this NovaProjectLimits.

        值为空列表。

        :return: The rate of this NovaProjectLimits.
        :rtype: list[NovaSpaceObject]
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this NovaProjectLimits.

        值为空列表。

        :param rate: The rate of this NovaProjectLimits.
        :type: list[NovaSpaceObject]
        """
        self._rate = rate

    @property
    def absolute(self):
        """Gets the absolute of this NovaProjectLimits.


        :return: The absolute of this NovaProjectLimits.
        :rtype: NovaProjectLimitsAbsolute
        """
        return self._absolute

    @absolute.setter
    def absolute(self, absolute):
        """Sets the absolute of this NovaProjectLimits.


        :param absolute: The absolute of this NovaProjectLimits.
        :type: NovaProjectLimitsAbsolute
        """
        self._absolute = absolute

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
        if not isinstance(other, NovaProjectLimits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
