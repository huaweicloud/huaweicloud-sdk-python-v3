# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GoogleOauth2ProviderConfigInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('client_secret')

    openapi_types = {
        'client_id': 'str',
        'client_secret': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'client_secret': 'client_secret'
    }

    def __init__(self, client_id=None, client_secret=None):
        r"""GoogleOauth2ProviderConfigInput

        The model defined in huaweicloud sdk

        :param client_id: Client ID for OAuth2 application.
        :type client_id: str
        :param client_secret: Client secret for OAuth2 application.
        :type client_secret: str
        """
        
        

        self._client_id = None
        self._client_secret = None
        self.discriminator = None

        self.client_id = client_id
        self.client_secret = client_secret

    @property
    def client_id(self):
        r"""Gets the client_id of this GoogleOauth2ProviderConfigInput.

        Client ID for OAuth2 application.

        :return: The client_id of this GoogleOauth2ProviderConfigInput.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this GoogleOauth2ProviderConfigInput.

        Client ID for OAuth2 application.

        :param client_id: The client_id of this GoogleOauth2ProviderConfigInput.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        r"""Gets the client_secret of this GoogleOauth2ProviderConfigInput.

        Client secret for OAuth2 application.

        :return: The client_secret of this GoogleOauth2ProviderConfigInput.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        r"""Sets the client_secret of this GoogleOauth2ProviderConfigInput.

        Client secret for OAuth2 application.

        :param client_secret: The client_secret of this GoogleOauth2ProviderConfigInput.
        :type client_secret: str
        """
        self._client_secret = client_secret

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
        if not isinstance(other, GoogleOauth2ProviderConfigInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
