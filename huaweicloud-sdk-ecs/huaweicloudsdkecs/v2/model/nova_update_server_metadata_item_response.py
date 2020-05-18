# coding: utf-8

import pprint
import re

import six


class NovaUpdateServerMetadataItemResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'meta': 'dict(str, str)'
    }

    attribute_map = {
        'meta': 'meta'
    }

    def __init__(self, meta=None):  # noqa: E501
        """NovaUpdateServerMetadataItemResponse - a model defined in huaweicloud sdk"""

        self._meta = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta

    @property
    def meta(self):
        """Gets the meta of this NovaUpdateServerMetadataItemResponse.

        用户自定义metadata键值对。  最大长度255个Unicode字符，键不能为空。键可以为大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）和小数点（.）。

        :return: The meta of this NovaUpdateServerMetadataItemResponse.
        :rtype: dict(str, str)
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this NovaUpdateServerMetadataItemResponse.

        用户自定义metadata键值对。  最大长度255个Unicode字符，键不能为空。键可以为大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）和小数点（.）。

        :param meta: The meta of this NovaUpdateServerMetadataItemResponse.
        :type: dict(str, str)
        """
        self._meta = meta

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
        if not isinstance(other, NovaUpdateServerMetadataItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
