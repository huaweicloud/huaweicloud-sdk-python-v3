# coding: utf-8

import pprint
import re

import six


class ServerTagResource(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'resource_id': 'str',
        'resource_detail': 'str',
        'tags': 'list[ServerTag]',
        'resource_name': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_detail': 'resource_detail',
        'tags': 'tags',
        'resource_name': 'resource_name'
    }

    def __init__(self, resource_id=None, resource_detail=None, tags=None, resource_name=None):  # noqa: E501
        """ServerTagResource - a model defined in huaweicloud sdk"""

        self._resource_id = None
        self._resource_detail = None
        self._tags = None
        self._resource_name = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_detail = resource_detail
        self.tags = tags
        self.resource_name = resource_name

    @property
    def resource_id(self):
        """Gets the resource_id of this ServerTagResource.

        云服务器ID。

        :return: The resource_id of this ServerTagResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ServerTagResource.

        云服务器ID。

        :param resource_id: The resource_id of this ServerTagResource.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_detail(self):
        """Gets the resource_detail of this ServerTagResource.

        云服务器详情，对象。

        :return: The resource_detail of this ServerTagResource.
        :rtype: str
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        """Sets the resource_detail of this ServerTagResource.

        云服务器详情，对象。

        :param resource_detail: The resource_detail of this ServerTagResource.
        :type: str
        """
        self._resource_detail = resource_detail

    @property
    def tags(self):
        """Gets the tags of this ServerTagResource.

        标签列表

        :return: The tags of this ServerTagResource.
        :rtype: list[ServerTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ServerTagResource.

        标签列表

        :param tags: The tags of this ServerTagResource.
        :type: list[ServerTag]
        """
        self._tags = tags

    @property
    def resource_name(self):
        """Gets the resource_name of this ServerTagResource.

        资源名称，即弹性云服务器名称。

        :return: The resource_name of this ServerTagResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ServerTagResource.

        资源名称，即弹性云服务器名称。

        :param resource_name: The resource_name of this ServerTagResource.
        :type: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, ServerTagResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
