# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListResourcesByTagsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resources': 'list[ResourceDTO]',
        'page': 'Page'
    }

    attribute_map = {
        'resources': 'resources',
        'page': 'page'
    }

    def __init__(self, resources=None, page=None):
        """ListResourcesByTagsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._resources = None
        self._page = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if page is not None:
            self.page = page

    @property
    def resources(self):
        """Gets the resources of this ListResourcesByTagsResponse.

        资源列表。

        :return: The resources of this ListResourcesByTagsResponse.
        :rtype: list[ResourceDTO]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListResourcesByTagsResponse.

        资源列表。

        :param resources: The resources of this ListResourcesByTagsResponse.
        :type: list[ResourceDTO]
        """
        self._resources = resources

    @property
    def page(self):
        """Gets the page of this ListResourcesByTagsResponse.


        :return: The page of this ListResourcesByTagsResponse.
        :rtype: Page
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListResourcesByTagsResponse.


        :param page: The page of this ListResourcesByTagsResponse.
        :type: Page
        """
        self._page = page

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
        if not isinstance(other, ListResourcesByTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
