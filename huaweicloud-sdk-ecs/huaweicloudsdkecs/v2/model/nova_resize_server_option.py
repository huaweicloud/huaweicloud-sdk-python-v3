# coding: utf-8

import pprint
import re

import six


class NovaResizeServerOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'flavor_ref': 'str'
    }

    attribute_map = {
        'flavor_ref': 'flavorRef'
    }

    def __init__(self, flavor_ref=None):  # noqa: E501
        """NovaResizeServerOption - a model defined in huaweicloud sdk"""

        self._flavor_ref = None
        self.discriminator = None

        self.flavor_ref = flavor_ref

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this NovaResizeServerOption.

        新规格ID

        :return: The flavor_ref of this NovaResizeServerOption.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this NovaResizeServerOption.

        新规格ID

        :param flavor_ref: The flavor_ref of this NovaResizeServerOption.
        :type: str
        """
        self._flavor_ref = flavor_ref

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
        if not isinstance(other, NovaResizeServerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
