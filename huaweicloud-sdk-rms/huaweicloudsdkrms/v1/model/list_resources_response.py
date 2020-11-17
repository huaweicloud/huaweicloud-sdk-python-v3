# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListResourcesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resources': 'list[ResourceEntity]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'resources': 'resources',
        'page_info': 'page_info'
    }

    def __init__(self, resources=None, page_info=None):
        """ListResourcesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._resources = None
        self._page_info = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if page_info is not None:
            self.page_info = page_info

    @property
    def resources(self):
        """Gets the resources of this ListResourcesResponse.

        资源列表

        :return: The resources of this ListResourcesResponse.
        :rtype: list[ResourceEntity]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListResourcesResponse.

        资源列表

        :param resources: The resources of this ListResourcesResponse.
        :type: list[ResourceEntity]
        """
        self._resources = resources

    @property
    def page_info(self):
        """Gets the page_info of this ListResourcesResponse.


        :return: The page_info of this ListResourcesResponse.
        :rtype: PageInfo
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListResourcesResponse.


        :param page_info: The page_info of this ListResourcesResponse.
        :type: PageInfo
        """
        self._page_info = page_info

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
        if not isinstance(other, ListResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
