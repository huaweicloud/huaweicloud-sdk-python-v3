# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Oauth2AuthorizationServerMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorization_endpoint': 'str',
        'issuer': 'str',
        'token_endpoint': 'str',
        'response_types': 'list[str]',
        'token_endpoint_auth_methods': 'list[str]'
    }

    attribute_map = {
        'authorization_endpoint': 'authorization_endpoint',
        'issuer': 'issuer',
        'token_endpoint': 'token_endpoint',
        'response_types': 'response_types',
        'token_endpoint_auth_methods': 'token_endpoint_auth_methods'
    }

    def __init__(self, authorization_endpoint=None, issuer=None, token_endpoint=None, response_types=None, token_endpoint_auth_methods=None):
        r"""Oauth2AuthorizationServerMetadata

        The model defined in huaweicloud sdk

        :param authorization_endpoint: Authorization endpoint of the authorization server.
        :type authorization_endpoint: str
        :param issuer: Issuer identifier of the authorization server.
        :type issuer: str
        :param token_endpoint: Token endpoint of the authorization server.
        :type token_endpoint: str
        :param response_types: Supported response types.
        :type response_types: list[str]
        :param token_endpoint_auth_methods: Client authentication methods supported by the token endpoint.
        :type token_endpoint_auth_methods: list[str]
        """
        
        

        self._authorization_endpoint = None
        self._issuer = None
        self._token_endpoint = None
        self._response_types = None
        self._token_endpoint_auth_methods = None
        self.discriminator = None

        self.authorization_endpoint = authorization_endpoint
        self.issuer = issuer
        self.token_endpoint = token_endpoint
        if response_types is not None:
            self.response_types = response_types
        if token_endpoint_auth_methods is not None:
            self.token_endpoint_auth_methods = token_endpoint_auth_methods

    @property
    def authorization_endpoint(self):
        r"""Gets the authorization_endpoint of this Oauth2AuthorizationServerMetadata.

        Authorization endpoint of the authorization server.

        :return: The authorization_endpoint of this Oauth2AuthorizationServerMetadata.
        :rtype: str
        """
        return self._authorization_endpoint

    @authorization_endpoint.setter
    def authorization_endpoint(self, authorization_endpoint):
        r"""Sets the authorization_endpoint of this Oauth2AuthorizationServerMetadata.

        Authorization endpoint of the authorization server.

        :param authorization_endpoint: The authorization_endpoint of this Oauth2AuthorizationServerMetadata.
        :type authorization_endpoint: str
        """
        self._authorization_endpoint = authorization_endpoint

    @property
    def issuer(self):
        r"""Gets the issuer of this Oauth2AuthorizationServerMetadata.

        Issuer identifier of the authorization server.

        :return: The issuer of this Oauth2AuthorizationServerMetadata.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        r"""Sets the issuer of this Oauth2AuthorizationServerMetadata.

        Issuer identifier of the authorization server.

        :param issuer: The issuer of this Oauth2AuthorizationServerMetadata.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def token_endpoint(self):
        r"""Gets the token_endpoint of this Oauth2AuthorizationServerMetadata.

        Token endpoint of the authorization server.

        :return: The token_endpoint of this Oauth2AuthorizationServerMetadata.
        :rtype: str
        """
        return self._token_endpoint

    @token_endpoint.setter
    def token_endpoint(self, token_endpoint):
        r"""Sets the token_endpoint of this Oauth2AuthorizationServerMetadata.

        Token endpoint of the authorization server.

        :param token_endpoint: The token_endpoint of this Oauth2AuthorizationServerMetadata.
        :type token_endpoint: str
        """
        self._token_endpoint = token_endpoint

    @property
    def response_types(self):
        r"""Gets the response_types of this Oauth2AuthorizationServerMetadata.

        Supported response types.

        :return: The response_types of this Oauth2AuthorizationServerMetadata.
        :rtype: list[str]
        """
        return self._response_types

    @response_types.setter
    def response_types(self, response_types):
        r"""Sets the response_types of this Oauth2AuthorizationServerMetadata.

        Supported response types.

        :param response_types: The response_types of this Oauth2AuthorizationServerMetadata.
        :type response_types: list[str]
        """
        self._response_types = response_types

    @property
    def token_endpoint_auth_methods(self):
        r"""Gets the token_endpoint_auth_methods of this Oauth2AuthorizationServerMetadata.

        Client authentication methods supported by the token endpoint.

        :return: The token_endpoint_auth_methods of this Oauth2AuthorizationServerMetadata.
        :rtype: list[str]
        """
        return self._token_endpoint_auth_methods

    @token_endpoint_auth_methods.setter
    def token_endpoint_auth_methods(self, token_endpoint_auth_methods):
        r"""Sets the token_endpoint_auth_methods of this Oauth2AuthorizationServerMetadata.

        Client authentication methods supported by the token endpoint.

        :param token_endpoint_auth_methods: The token_endpoint_auth_methods of this Oauth2AuthorizationServerMetadata.
        :type token_endpoint_auth_methods: list[str]
        """
        self._token_endpoint_auth_methods = token_endpoint_auth_methods

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
        if not isinstance(other, Oauth2AuthorizationServerMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
