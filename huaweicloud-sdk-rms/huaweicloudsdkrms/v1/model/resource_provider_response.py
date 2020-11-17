# coding: utf-8

import pprint
import re

import six





class ResourceProviderResponse:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'provider': 'str',
        'display_name': 'str',
        'category_display_name': 'str',
        'resource_types': 'list[ResourceTypeResponse]',
        'order': 'int'
    }

    attribute_map = {
        'provider': 'provider',
        'display_name': 'display_name',
        'category_display_name': 'category_display_name',
        'resource_types': 'resource_types',
        'order': 'order'
    }

    def __init__(self, provider=None, display_name=None, category_display_name=None, resource_types=None, order=None):
        """ResourceProviderResponse - a model defined in huaweicloud sdk"""
        
        

        self._provider = None
        self._display_name = None
        self._category_display_name = None
        self._resource_types = None
        self._order = None
        self.discriminator = None

        if provider is not None:
            self.provider = provider
        if display_name is not None:
            self.display_name = display_name
        if category_display_name is not None:
            self.category_display_name = category_display_name
        if resource_types is not None:
            self.resource_types = resource_types
        if order is not None:
            self.order = order

    @property
    def provider(self):
        """Gets the provider of this ResourceProviderResponse.

        云服务名称

        :return: The provider of this ResourceProviderResponse.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ResourceProviderResponse.

        云服务名称

        :param provider: The provider of this ResourceProviderResponse.
        :type: str
        """
        self._provider = provider

    @property
    def display_name(self):
        """Gets the display_name of this ResourceProviderResponse.

        云服务显示名称，可以通过请求Header中的'X-Language'设置语言

        :return: The display_name of this ResourceProviderResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ResourceProviderResponse.

        云服务显示名称，可以通过请求Header中的'X-Language'设置语言

        :param display_name: The display_name of this ResourceProviderResponse.
        :type: str
        """
        self._display_name = display_name

    @property
    def category_display_name(self):
        """Gets the category_display_name of this ResourceProviderResponse.

        云服务类别显示名称，可以通过请求Header中的'X-Language'设置语言

        :return: The category_display_name of this ResourceProviderResponse.
        :rtype: str
        """
        return self._category_display_name

    @category_display_name.setter
    def category_display_name(self, category_display_name):
        """Sets the category_display_name of this ResourceProviderResponse.

        云服务类别显示名称，可以通过请求Header中的'X-Language'设置语言

        :param category_display_name: The category_display_name of this ResourceProviderResponse.
        :type: str
        """
        self._category_display_name = category_display_name

    @property
    def resource_types(self):
        """Gets the resource_types of this ResourceProviderResponse.

        资源类型列表

        :return: The resource_types of this ResourceProviderResponse.
        :rtype: list[ResourceTypeResponse]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """Sets the resource_types of this ResourceProviderResponse.

        资源类型列表

        :param resource_types: The resource_types of this ResourceProviderResponse.
        :type: list[ResourceTypeResponse]
        """
        self._resource_types = resource_types

    @property
    def order(self):
        """Gets the order of this ResourceProviderResponse.

        排序序号

        :return: The order of this ResourceProviderResponse.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ResourceProviderResponse.

        排序序号

        :param order: The order of this ResourceProviderResponse.
        :type: int
        """
        self._order = order

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
        if not isinstance(other, ResourceProviderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
