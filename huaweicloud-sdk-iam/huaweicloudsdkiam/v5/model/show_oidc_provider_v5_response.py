# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOIDCProviderV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'oidc_provider': 'InlineResponse2003OidcProvider'
    }

    attribute_map = {
        'oidc_provider': 'oidc_provider'
    }

    def __init__(self, oidc_provider=None):
        r"""ShowOIDCProviderV5Response

        The model defined in huaweicloud sdk

        :param oidc_provider: 
        :type oidc_provider: :class:`huaweicloudsdkiam.v5.InlineResponse2003OidcProvider`
        """
        
        super().__init__()

        self._oidc_provider = None
        self.discriminator = None

        if oidc_provider is not None:
            self.oidc_provider = oidc_provider

    @property
    def oidc_provider(self):
        r"""Gets the oidc_provider of this ShowOIDCProviderV5Response.

        :return: The oidc_provider of this ShowOIDCProviderV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.InlineResponse2003OidcProvider`
        """
        return self._oidc_provider

    @oidc_provider.setter
    def oidc_provider(self, oidc_provider):
        r"""Sets the oidc_provider of this ShowOIDCProviderV5Response.

        :param oidc_provider: The oidc_provider of this ShowOIDCProviderV5Response.
        :type oidc_provider: :class:`huaweicloudsdkiam.v5.InlineResponse2003OidcProvider`
        """
        self._oidc_provider = oidc_provider

    def to_dict(self):
        import warnings
        warnings.warn("ShowOIDCProviderV5Response.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOIDCProviderV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
