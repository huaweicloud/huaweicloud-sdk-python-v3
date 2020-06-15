# coding: utf-8

import pprint
import re

import six


class ListPrivateipsResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'privateips': 'list[Privateip]'
    }

    attribute_map = {
        'privateips': 'privateips'
    }

    def __init__(self, privateips=None):  # noqa: E501
        """ListPrivateipsResponse - a model defined in huaweicloud sdk"""

        self._privateips = None
        self.discriminator = None

        if privateips is not None:
            self.privateips = privateips

    @property
    def privateips(self):
        """Gets the privateips of this ListPrivateipsResponse.

        私有IP列表对象

        :return: The privateips of this ListPrivateipsResponse.
        :rtype: list[Privateip]
        """
        return self._privateips

    @privateips.setter
    def privateips(self, privateips):
        """Sets the privateips of this ListPrivateipsResponse.

        私有IP列表对象

        :param privateips: The privateips of this ListPrivateipsResponse.
        :type: list[Privateip]
        """
        self._privateips = privateips

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
        if not isinstance(other, ListPrivateipsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other