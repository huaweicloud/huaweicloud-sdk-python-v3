# coding: utf-8

import pprint
import re

import six





class ShowImageByTagsResource:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resouce_detail': 'QueryImageByTagsResourceDetail',
        'tags': 'list[TagKeyValue]',
        'resource_name': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resouce_detail': 'resouce_detail',
        'tags': 'tags',
        'resource_name': 'resource_name'
    }

    def __init__(self, resource_id=None, resouce_detail=None, tags=None, resource_name=None):
        """ShowImageByTagsResource - a model defined in huaweicloud sdk"""
        
        

        self._resource_id = None
        self._resouce_detail = None
        self._tags = None
        self._resource_name = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resouce_detail = resouce_detail
        self.tags = tags
        self.resource_name = resource_name

    @property
    def resource_id(self):
        """Gets the resource_id of this ShowImageByTagsResource.

        镜像ID

        :return: The resource_id of this ShowImageByTagsResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ShowImageByTagsResource.

        镜像ID

        :param resource_id: The resource_id of this ShowImageByTagsResource.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resouce_detail(self):
        """Gets the resouce_detail of this ShowImageByTagsResource.


        :return: The resouce_detail of this ShowImageByTagsResource.
        :rtype: QueryImageByTagsResourceDetail
        """
        return self._resouce_detail

    @resouce_detail.setter
    def resouce_detail(self, resouce_detail):
        """Sets the resouce_detail of this ShowImageByTagsResource.


        :param resouce_detail: The resouce_detail of this ShowImageByTagsResource.
        :type: QueryImageByTagsResourceDetail
        """
        self._resouce_detail = resouce_detail

    @property
    def tags(self):
        """Gets the tags of this ShowImageByTagsResource.

        镜像的标签列表

        :return: The tags of this ShowImageByTagsResource.
        :rtype: list[TagKeyValue]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowImageByTagsResource.

        镜像的标签列表

        :param tags: The tags of this ShowImageByTagsResource.
        :type: list[TagKeyValue]
        """
        self._tags = tags

    @property
    def resource_name(self):
        """Gets the resource_name of this ShowImageByTagsResource.

        镜像名称

        :return: The resource_name of this ShowImageByTagsResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ShowImageByTagsResource.

        镜像名称

        :param resource_name: The resource_name of this ShowImageByTagsResource.
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
        if not isinstance(other, ShowImageByTagsResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
