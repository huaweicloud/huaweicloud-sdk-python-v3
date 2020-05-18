# coding: utf-8

import pprint
import re

import six


class NovaGetServerConsoleLogOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'length': 'int'
    }

    attribute_map = {
        'length': 'length'
    }

    def __init__(self, length=None):  # noqa: E501
        """NovaGetServerConsoleLogOption - a model defined in huaweicloud sdk"""

        self._length = None
        self.discriminator = None

        self.length = length

    @property
    def length(self):
        """Gets the length of this NovaGetServerConsoleLogOption.

        请求log行数。取值范围大于等于-1，其中-1代表不限长度输出。

        :return: The length of this NovaGetServerConsoleLogOption.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this NovaGetServerConsoleLogOption.

        请求log行数。取值范围大于等于-1，其中-1代表不限长度输出。

        :param length: The length of this NovaGetServerConsoleLogOption.
        :type: int
        """
        self._length = length

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
        if not isinstance(other, NovaGetServerConsoleLogOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
