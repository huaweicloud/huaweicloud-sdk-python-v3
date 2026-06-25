# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSAMLProvidersV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'saml_providers': 'list[InlineResponse200SamlProviders]',
        'page_info': 'InlineResponse200PageInfo'
    }

    attribute_map = {
        'saml_providers': 'saml_providers',
        'page_info': 'page_info'
    }

    def __init__(self, saml_providers=None, page_info=None):
        r"""ListSAMLProvidersV5Response

        The model defined in huaweicloud sdk

        :param saml_providers: **参数解释**： SAML 提供商。  **取值范围**： 不涉及。
        :type saml_providers: list[:class:`huaweicloudsdkiam.v5.InlineResponse200SamlProviders`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiam.v5.InlineResponse200PageInfo`
        """
        
        super().__init__()

        self._saml_providers = None
        self._page_info = None
        self.discriminator = None

        if saml_providers is not None:
            self.saml_providers = saml_providers
        if page_info is not None:
            self.page_info = page_info

    @property
    def saml_providers(self):
        r"""Gets the saml_providers of this ListSAMLProvidersV5Response.

        **参数解释**： SAML 提供商。  **取值范围**： 不涉及。

        :return: The saml_providers of this ListSAMLProvidersV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.InlineResponse200SamlProviders`]
        """
        return self._saml_providers

    @saml_providers.setter
    def saml_providers(self, saml_providers):
        r"""Sets the saml_providers of this ListSAMLProvidersV5Response.

        **参数解释**： SAML 提供商。  **取值范围**： 不涉及。

        :param saml_providers: The saml_providers of this ListSAMLProvidersV5Response.
        :type saml_providers: list[:class:`huaweicloudsdkiam.v5.InlineResponse200SamlProviders`]
        """
        self._saml_providers = saml_providers

    @property
    def page_info(self):
        r"""Gets the page_info of this ListSAMLProvidersV5Response.

        :return: The page_info of this ListSAMLProvidersV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.InlineResponse200PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListSAMLProvidersV5Response.

        :param page_info: The page_info of this ListSAMLProvidersV5Response.
        :type page_info: :class:`huaweicloudsdkiam.v5.InlineResponse200PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListSAMLProvidersV5Response.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSAMLProvidersV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
