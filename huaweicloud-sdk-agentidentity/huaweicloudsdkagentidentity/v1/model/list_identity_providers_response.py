# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIdentityProvidersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity_providers': 'list[IdentityProviderListSummary]'
    }

    attribute_map = {
        'identity_providers': 'identity_providers'
    }

    def __init__(self, identity_providers=None):
        r"""ListIdentityProvidersResponse

        The model defined in huaweicloud sdk

        :param identity_providers: List of identity providers.
        :type identity_providers: list[:class:`huaweicloudsdkagentidentity.v1.IdentityProviderListSummary`]
        """
        
        super().__init__()

        self._identity_providers = None
        self.discriminator = None

        if identity_providers is not None:
            self.identity_providers = identity_providers

    @property
    def identity_providers(self):
        r"""Gets the identity_providers of this ListIdentityProvidersResponse.

        List of identity providers.

        :return: The identity_providers of this ListIdentityProvidersResponse.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.IdentityProviderListSummary`]
        """
        return self._identity_providers

    @identity_providers.setter
    def identity_providers(self, identity_providers):
        r"""Sets the identity_providers of this ListIdentityProvidersResponse.

        List of identity providers.

        :param identity_providers: The identity_providers of this ListIdentityProvidersResponse.
        :type identity_providers: list[:class:`huaweicloudsdkagentidentity.v1.IdentityProviderListSummary`]
        """
        self._identity_providers = identity_providers

    def to_dict(self):
        import warnings
        warnings.warn("ListIdentityProvidersResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListIdentityProvidersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
