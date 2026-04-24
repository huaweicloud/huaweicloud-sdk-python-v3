# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MicrosoftOauth2ProviderConfigOutput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'oauth2_discovery': 'Oauth2Discovery',
        'client_id': 'str'
    }

    attribute_map = {
        'oauth2_discovery': 'oauth2_discovery',
        'client_id': 'client_id'
    }

    def __init__(self, oauth2_discovery=None, client_id=None):
        r"""MicrosoftOauth2ProviderConfigOutput

        The model defined in huaweicloud sdk

        :param oauth2_discovery: 
        :type oauth2_discovery: :class:`huaweicloudsdkagentidentity.v1.Oauth2Discovery`
        :param client_id: Client ID for OAuth2 application.
        :type client_id: str
        """
        
        

        self._oauth2_discovery = None
        self._client_id = None
        self.discriminator = None

        self.oauth2_discovery = oauth2_discovery
        if client_id is not None:
            self.client_id = client_id

    @property
    def oauth2_discovery(self):
        r"""Gets the oauth2_discovery of this MicrosoftOauth2ProviderConfigOutput.

        :return: The oauth2_discovery of this MicrosoftOauth2ProviderConfigOutput.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.Oauth2Discovery`
        """
        return self._oauth2_discovery

    @oauth2_discovery.setter
    def oauth2_discovery(self, oauth2_discovery):
        r"""Sets the oauth2_discovery of this MicrosoftOauth2ProviderConfigOutput.

        :param oauth2_discovery: The oauth2_discovery of this MicrosoftOauth2ProviderConfigOutput.
        :type oauth2_discovery: :class:`huaweicloudsdkagentidentity.v1.Oauth2Discovery`
        """
        self._oauth2_discovery = oauth2_discovery

    @property
    def client_id(self):
        r"""Gets the client_id of this MicrosoftOauth2ProviderConfigOutput.

        Client ID for OAuth2 application.

        :return: The client_id of this MicrosoftOauth2ProviderConfigOutput.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this MicrosoftOauth2ProviderConfigOutput.

        Client ID for OAuth2 application.

        :param client_id: The client_id of this MicrosoftOauth2ProviderConfigOutput.
        :type client_id: str
        """
        self._client_id = client_id

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
        if not isinstance(other, MicrosoftOauth2ProviderConfigOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
