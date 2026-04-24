# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOauth2CredentialProvidersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'credential_providers': 'list[Oauth2CredentialProviderSummary]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'credential_providers': 'credential_providers',
        'page_info': 'page_info'
    }

    def __init__(self, credential_providers=None, page_info=None):
        r"""ListOauth2CredentialProvidersResponse

        The model defined in huaweicloud sdk

        :param credential_providers: 
        :type credential_providers: list[:class:`huaweicloudsdkagentidentity.v1.Oauth2CredentialProviderSummary`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkagentidentity.v1.PageInfo`
        """
        
        super().__init__()

        self._credential_providers = None
        self._page_info = None
        self.discriminator = None

        if credential_providers is not None:
            self.credential_providers = credential_providers
        if page_info is not None:
            self.page_info = page_info

    @property
    def credential_providers(self):
        r"""Gets the credential_providers of this ListOauth2CredentialProvidersResponse.

        :return: The credential_providers of this ListOauth2CredentialProvidersResponse.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.Oauth2CredentialProviderSummary`]
        """
        return self._credential_providers

    @credential_providers.setter
    def credential_providers(self, credential_providers):
        r"""Sets the credential_providers of this ListOauth2CredentialProvidersResponse.

        :param credential_providers: The credential_providers of this ListOauth2CredentialProvidersResponse.
        :type credential_providers: list[:class:`huaweicloudsdkagentidentity.v1.Oauth2CredentialProviderSummary`]
        """
        self._credential_providers = credential_providers

    @property
    def page_info(self):
        r"""Gets the page_info of this ListOauth2CredentialProvidersResponse.

        :return: The page_info of this ListOauth2CredentialProvidersResponse.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListOauth2CredentialProvidersResponse.

        :param page_info: The page_info of this ListOauth2CredentialProvidersResponse.
        :type page_info: :class:`huaweicloudsdkagentidentity.v1.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListOauth2CredentialProvidersResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOauth2CredentialProvidersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
