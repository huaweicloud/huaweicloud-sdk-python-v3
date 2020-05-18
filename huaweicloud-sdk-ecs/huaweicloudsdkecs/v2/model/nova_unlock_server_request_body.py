# coding: utf-8

import pprint
import re

import six


class NovaUnlockServerRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'unlock': 'str'
    }

    attribute_map = {
        'unlock': 'unlock'
    }

    def __init__(self, unlock=''):  # noqa: E501
        """NovaUnlockServerRequestBody - a model defined in huaweicloud sdk"""

        self._unlock = None
        self.discriminator = None

        self.unlock = unlock

    @property
    def unlock(self):
        """Gets the unlock of this NovaUnlockServerRequestBody.

        解锁弹性云服务器

        :return: The unlock of this NovaUnlockServerRequestBody.
        :rtype: str
        """
        return self._unlock

    @unlock.setter
    def unlock(self, unlock):
        """Sets the unlock of this NovaUnlockServerRequestBody.

        解锁弹性云服务器

        :param unlock: The unlock of this NovaUnlockServerRequestBody.
        :type: str
        """
        self._unlock = unlock

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
        if not isinstance(other, NovaUnlockServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
