# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainConfigurationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_configurations': 'list[DomainConfigurationDTO]',
        'page': 'Page'
    }

    attribute_map = {
        'domain_configurations': 'domain_configurations',
        'page': 'page'
    }

    def __init__(self, domain_configurations=None, page=None):
        r"""ListDomainConfigurationsResponse

        The model defined in huaweicloud sdk

        :param domain_configurations: **参数说明**：域配置列表。
        :type domain_configurations: list[:class:`huaweicloudsdkiotda.v5.DomainConfigurationDTO`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super().__init__()

        self._domain_configurations = None
        self._page = None
        self.discriminator = None

        if domain_configurations is not None:
            self.domain_configurations = domain_configurations
        if page is not None:
            self.page = page

    @property
    def domain_configurations(self):
        r"""Gets the domain_configurations of this ListDomainConfigurationsResponse.

        **参数说明**：域配置列表。

        :return: The domain_configurations of this ListDomainConfigurationsResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.DomainConfigurationDTO`]
        """
        return self._domain_configurations

    @domain_configurations.setter
    def domain_configurations(self, domain_configurations):
        r"""Sets the domain_configurations of this ListDomainConfigurationsResponse.

        **参数说明**：域配置列表。

        :param domain_configurations: The domain_configurations of this ListDomainConfigurationsResponse.
        :type domain_configurations: list[:class:`huaweicloudsdkiotda.v5.DomainConfigurationDTO`]
        """
        self._domain_configurations = domain_configurations

    @property
    def page(self):
        r"""Gets the page of this ListDomainConfigurationsResponse.

        :return: The page of this ListDomainConfigurationsResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListDomainConfigurationsResponse.

        :param page: The page of this ListDomainConfigurationsResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        self._page = page

    def to_dict(self):
        import warnings
        warnings.warn("ListDomainConfigurationsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListDomainConfigurationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
