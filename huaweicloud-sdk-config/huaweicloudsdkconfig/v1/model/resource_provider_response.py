# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'resource_types': 'list[ResourceTypeResponse]'
    }

    attribute_map = {
        'provider': 'provider',
        'display_name': 'display_name',
        'category_display_name': 'category_display_name',
        'resource_types': 'resource_types'
    }

    def __init__(self, provider=None, display_name=None, category_display_name=None, resource_types=None):
        r"""ResourceProviderResponse

        The model defined in huaweicloud sdk

        :param provider: 云服务名称
        :type provider: str
        :param display_name: 云服务显示名称，可以通过请求Header中的&#39;X-Language&#39;设置语言
        :type display_name: str
        :param category_display_name: 云服务类别显示名称，可以通过请求Header中的&#39;X-Language&#39;设置语言
        :type category_display_name: str
        :param resource_types: 资源类型列表
        :type resource_types: list[:class:`huaweicloudsdkconfig.v1.ResourceTypeResponse`]
        """
        
        

        self._provider = None
        self._display_name = None
        self._category_display_name = None
        self._resource_types = None
        self.discriminator = None

        if provider is not None:
            self.provider = provider
        if display_name is not None:
            self.display_name = display_name
        if category_display_name is not None:
            self.category_display_name = category_display_name
        if resource_types is not None:
            self.resource_types = resource_types

    @property
    def provider(self):
        r"""Gets the provider of this ResourceProviderResponse.

        云服务名称

        :return: The provider of this ResourceProviderResponse.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ResourceProviderResponse.

        云服务名称

        :param provider: The provider of this ResourceProviderResponse.
        :type provider: str
        """
        self._provider = provider

    @property
    def display_name(self):
        r"""Gets the display_name of this ResourceProviderResponse.

        云服务显示名称，可以通过请求Header中的'X-Language'设置语言

        :return: The display_name of this ResourceProviderResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ResourceProviderResponse.

        云服务显示名称，可以通过请求Header中的'X-Language'设置语言

        :param display_name: The display_name of this ResourceProviderResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def category_display_name(self):
        r"""Gets the category_display_name of this ResourceProviderResponse.

        云服务类别显示名称，可以通过请求Header中的'X-Language'设置语言

        :return: The category_display_name of this ResourceProviderResponse.
        :rtype: str
        """
        return self._category_display_name

    @category_display_name.setter
    def category_display_name(self, category_display_name):
        r"""Sets the category_display_name of this ResourceProviderResponse.

        云服务类别显示名称，可以通过请求Header中的'X-Language'设置语言

        :param category_display_name: The category_display_name of this ResourceProviderResponse.
        :type category_display_name: str
        """
        self._category_display_name = category_display_name

    @property
    def resource_types(self):
        r"""Gets the resource_types of this ResourceProviderResponse.

        资源类型列表

        :return: The resource_types of this ResourceProviderResponse.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.ResourceTypeResponse`]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        r"""Sets the resource_types of this ResourceProviderResponse.

        资源类型列表

        :param resource_types: The resource_types of this ResourceProviderResponse.
        :type resource_types: list[:class:`huaweicloudsdkconfig.v1.ResourceTypeResponse`]
        """
        self._resource_types = resource_types

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceProviderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
