# coding: utf-8

import pprint
import re

import six


class NovaStartServerRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'os_start': 'str'
    }

    attribute_map = {
        'os_start': 'os-start'
    }

    def __init__(self, os_start=''):  # noqa: E501
        """NovaStartServerRequestBody - a model defined in huaweicloud sdk"""

        self._os_start = None
        self.discriminator = None

        self.os_start = os_start

    @property
    def os_start(self):
        """Gets the os_start of this NovaStartServerRequestBody.

        标记为启动云服务器操作，数据结构为空。

        :return: The os_start of this NovaStartServerRequestBody.
        :rtype: str
        """
        return self._os_start

    @os_start.setter
    def os_start(self, os_start):
        """Sets the os_start of this NovaStartServerRequestBody.

        标记为启动云服务器操作，数据结构为空。

        :param os_start: The os_start of this NovaStartServerRequestBody.
        :type: str
        """
        self._os_start = os_start

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
        if not isinstance(other, NovaStartServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
