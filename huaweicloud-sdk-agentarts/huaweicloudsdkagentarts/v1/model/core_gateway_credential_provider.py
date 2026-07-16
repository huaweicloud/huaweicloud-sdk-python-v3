# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayCredentialProvider:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_key_credential_provider': 'CoreGatewayApiKeyCredentialProvider',
        'oauth_credential_provider': 'CoreGatewayOAuthCredentialProvider',
        'iam_credential_provider': 'CoreGatewayIamCredentialProvider'
    }

    attribute_map = {
        'api_key_credential_provider': 'api_key_credential_provider',
        'oauth_credential_provider': 'oauth_credential_provider',
        'iam_credential_provider': 'iam_credential_provider'
    }

    def __init__(self, api_key_credential_provider=None, oauth_credential_provider=None, iam_credential_provider=None):
        r"""CoreGatewayCredentialProvider

        The model defined in huaweicloud sdk

        :param api_key_credential_provider: 
        :type api_key_credential_provider: :class:`huaweicloudsdkagentarts.v1.CoreGatewayApiKeyCredentialProvider`
        :param oauth_credential_provider: 
        :type oauth_credential_provider: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOAuthCredentialProvider`
        :param iam_credential_provider: 
        :type iam_credential_provider: :class:`huaweicloudsdkagentarts.v1.CoreGatewayIamCredentialProvider`
        """
        
        

        self._api_key_credential_provider = None
        self._oauth_credential_provider = None
        self._iam_credential_provider = None
        self.discriminator = None

        if api_key_credential_provider is not None:
            self.api_key_credential_provider = api_key_credential_provider
        if oauth_credential_provider is not None:
            self.oauth_credential_provider = oauth_credential_provider
        if iam_credential_provider is not None:
            self.iam_credential_provider = iam_credential_provider

    @property
    def api_key_credential_provider(self):
        r"""Gets the api_key_credential_provider of this CoreGatewayCredentialProvider.

        :return: The api_key_credential_provider of this CoreGatewayCredentialProvider.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayApiKeyCredentialProvider`
        """
        return self._api_key_credential_provider

    @api_key_credential_provider.setter
    def api_key_credential_provider(self, api_key_credential_provider):
        r"""Sets the api_key_credential_provider of this CoreGatewayCredentialProvider.

        :param api_key_credential_provider: The api_key_credential_provider of this CoreGatewayCredentialProvider.
        :type api_key_credential_provider: :class:`huaweicloudsdkagentarts.v1.CoreGatewayApiKeyCredentialProvider`
        """
        self._api_key_credential_provider = api_key_credential_provider

    @property
    def oauth_credential_provider(self):
        r"""Gets the oauth_credential_provider of this CoreGatewayCredentialProvider.

        :return: The oauth_credential_provider of this CoreGatewayCredentialProvider.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOAuthCredentialProvider`
        """
        return self._oauth_credential_provider

    @oauth_credential_provider.setter
    def oauth_credential_provider(self, oauth_credential_provider):
        r"""Sets the oauth_credential_provider of this CoreGatewayCredentialProvider.

        :param oauth_credential_provider: The oauth_credential_provider of this CoreGatewayCredentialProvider.
        :type oauth_credential_provider: :class:`huaweicloudsdkagentarts.v1.CoreGatewayOAuthCredentialProvider`
        """
        self._oauth_credential_provider = oauth_credential_provider

    @property
    def iam_credential_provider(self):
        r"""Gets the iam_credential_provider of this CoreGatewayCredentialProvider.

        :return: The iam_credential_provider of this CoreGatewayCredentialProvider.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayIamCredentialProvider`
        """
        return self._iam_credential_provider

    @iam_credential_provider.setter
    def iam_credential_provider(self, iam_credential_provider):
        r"""Sets the iam_credential_provider of this CoreGatewayCredentialProvider.

        :param iam_credential_provider: The iam_credential_provider of this CoreGatewayCredentialProvider.
        :type iam_credential_provider: :class:`huaweicloudsdkagentarts.v1.CoreGatewayIamCredentialProvider`
        """
        self._iam_credential_provider = iam_credential_provider

    def to_dict(self):
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
        if not isinstance(other, CoreGatewayCredentialProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
