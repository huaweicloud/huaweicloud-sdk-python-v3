# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOIDCProvidersV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'oidc_providers': 'list[InlineResponse2002OidcProviders]',
        'page_info': 'InlineResponse200PageInfo'
    }

    attribute_map = {
        'oidc_providers': 'oidc_providers',
        'page_info': 'page_info'
    }

    def __init__(self, oidc_providers=None, page_info=None):
        r"""ListOIDCProvidersV5Response

        The model defined in huaweicloud sdk

        :param oidc_providers: **参数解释**： OIDC 提供商列表。  **取值范围**： 不涉及。
        :type oidc_providers: list[:class:`huaweicloudsdkiam.v5.InlineResponse2002OidcProviders`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiam.v5.InlineResponse200PageInfo`
        """
        
        super().__init__()

        self._oidc_providers = None
        self._page_info = None
        self.discriminator = None

        if oidc_providers is not None:
            self.oidc_providers = oidc_providers
        if page_info is not None:
            self.page_info = page_info

    @property
    def oidc_providers(self):
        r"""Gets the oidc_providers of this ListOIDCProvidersV5Response.

        **参数解释**： OIDC 提供商列表。  **取值范围**： 不涉及。

        :return: The oidc_providers of this ListOIDCProvidersV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.InlineResponse2002OidcProviders`]
        """
        return self._oidc_providers

    @oidc_providers.setter
    def oidc_providers(self, oidc_providers):
        r"""Sets the oidc_providers of this ListOIDCProvidersV5Response.

        **参数解释**： OIDC 提供商列表。  **取值范围**： 不涉及。

        :param oidc_providers: The oidc_providers of this ListOIDCProvidersV5Response.
        :type oidc_providers: list[:class:`huaweicloudsdkiam.v5.InlineResponse2002OidcProviders`]
        """
        self._oidc_providers = oidc_providers

    @property
    def page_info(self):
        r"""Gets the page_info of this ListOIDCProvidersV5Response.

        :return: The page_info of this ListOIDCProvidersV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.InlineResponse200PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListOIDCProvidersV5Response.

        :param page_info: The page_info of this ListOIDCProvidersV5Response.
        :type page_info: :class:`huaweicloudsdkiam.v5.InlineResponse200PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListOIDCProvidersV5Response.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOIDCProvidersV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
