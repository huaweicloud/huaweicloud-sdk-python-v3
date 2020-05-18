# coding: utf-8

import pprint
import re

import six


class NovaUpdateServerTagsRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'tags': 'list[str]'
    }

    attribute_map = {
        'tags': 'tags'
    }

    def __init__(self, tags=None):  # noqa: E501
        """NovaUpdateServerTagsRequestBody - a model defined in huaweicloud sdk"""

        self._tags = None
        self.discriminator = None

        self.tags = tags

    @property
    def tags(self):
        """Gets the tags of this NovaUpdateServerTagsRequestBody.

        云服务器tag列表。  tag个数不超过50，每个tag不超过80个字符。  只能包含数字、字母、中划线“-”、下划线“_”。

        :return: The tags of this NovaUpdateServerTagsRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this NovaUpdateServerTagsRequestBody.

        云服务器tag列表。  tag个数不超过50，每个tag不超过80个字符。  只能包含数字、字母、中划线“-”、下划线“_”。

        :param tags: The tags of this NovaUpdateServerTagsRequestBody.
        :type: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, NovaUpdateServerTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
