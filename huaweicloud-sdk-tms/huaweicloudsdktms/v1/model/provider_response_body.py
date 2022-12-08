# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProviderResponseBody:

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
        'provider_i18n_display_name': 'str',
        'resource_types': 'list[ResourceTypeBody]'
    }

    attribute_map = {
        'provider': 'provider',
        'provider_i18n_display_name': 'provider_i18n_display_name',
        'resource_types': 'resource_types'
    }

    def __init__(self, provider=None, provider_i18n_display_name=None, resource_types=None):
        """ProviderResponseBody

        The model defined in huaweicloud sdk

        :param provider: 云服务名称
        :type provider: str
        :param provider_i18n_display_name: 服务显示名称，可以通过参数中“locale”设置语言。
        :type provider_i18n_display_name: str
        :param resource_types: 资源类型列表
        :type resource_types: list[:class:`huaweicloudsdktms.v1.ResourceTypeBody`]
        """
        
        

        self._provider = None
        self._provider_i18n_display_name = None
        self._resource_types = None
        self.discriminator = None

        self.provider = provider
        self.provider_i18n_display_name = provider_i18n_display_name
        self.resource_types = resource_types

    @property
    def provider(self):
        """Gets the provider of this ProviderResponseBody.

        云服务名称

        :return: The provider of this ProviderResponseBody.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ProviderResponseBody.

        云服务名称

        :param provider: The provider of this ProviderResponseBody.
        :type provider: str
        """
        self._provider = provider

    @property
    def provider_i18n_display_name(self):
        """Gets the provider_i18n_display_name of this ProviderResponseBody.

        服务显示名称，可以通过参数中“locale”设置语言。

        :return: The provider_i18n_display_name of this ProviderResponseBody.
        :rtype: str
        """
        return self._provider_i18n_display_name

    @provider_i18n_display_name.setter
    def provider_i18n_display_name(self, provider_i18n_display_name):
        """Sets the provider_i18n_display_name of this ProviderResponseBody.

        服务显示名称，可以通过参数中“locale”设置语言。

        :param provider_i18n_display_name: The provider_i18n_display_name of this ProviderResponseBody.
        :type provider_i18n_display_name: str
        """
        self._provider_i18n_display_name = provider_i18n_display_name

    @property
    def resource_types(self):
        """Gets the resource_types of this ProviderResponseBody.

        资源类型列表

        :return: The resource_types of this ProviderResponseBody.
        :rtype: list[:class:`huaweicloudsdktms.v1.ResourceTypeBody`]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """Sets the resource_types of this ProviderResponseBody.

        资源类型列表

        :param resource_types: The resource_types of this ProviderResponseBody.
        :type resource_types: list[:class:`huaweicloudsdktms.v1.ResourceTypeBody`]
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
        if not isinstance(other, ProviderResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
