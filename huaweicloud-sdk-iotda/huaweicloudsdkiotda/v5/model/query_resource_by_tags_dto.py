# coding: utf-8

import pprint
import re

import six





class QueryResourceByTagsDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'tags': 'list[TagV5DTO]'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'tags': 'tags'
    }

    def __init__(self, resource_type=None, tags=None):
        """QueryResourceByTagsDTO - a model defined in huaweicloud sdk"""
        
        

        self._resource_type = None
        self._tags = None
        self.discriminator = None

        self.resource_type = resource_type
        self.tags = tags

    @property
    def resource_type(self):
        """Gets the resource_type of this QueryResourceByTagsDTO.

        要查询的资源类型，当前支持设备（device）。

        :return: The resource_type of this QueryResourceByTagsDTO.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this QueryResourceByTagsDTO.

        要查询的资源类型，当前支持设备（device）。

        :param resource_type: The resource_type of this QueryResourceByTagsDTO.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def tags(self):
        """Gets the tags of this QueryResourceByTagsDTO.

        标签列表，支持按照标签key和value组合查询，传入的多个标签之间是或的关系。

        :return: The tags of this QueryResourceByTagsDTO.
        :rtype: list[TagV5DTO]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this QueryResourceByTagsDTO.

        标签列表，支持按照标签key和value组合查询，传入的多个标签之间是或的关系。

        :param tags: The tags of this QueryResourceByTagsDTO.
        :type: list[TagV5DTO]
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
        if not isinstance(other, QueryResourceByTagsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
