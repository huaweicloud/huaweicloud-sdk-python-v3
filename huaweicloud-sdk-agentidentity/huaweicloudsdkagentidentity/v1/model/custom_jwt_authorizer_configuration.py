# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomJWTAuthorizerConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'discovery_url': 'str',
        'allowed_audience': 'list[str]',
        'allowed_clients': 'list[str]',
        'allowed_scopes': 'list[str]',
        'custom_claims': 'list[CustomClaimValidation]'
    }

    attribute_map = {
        'discovery_url': 'discovery_url',
        'allowed_audience': 'allowed_audience',
        'allowed_clients': 'allowed_clients',
        'allowed_scopes': 'allowed_scopes',
        'custom_claims': 'custom_claims'
    }

    def __init__(self, discovery_url=None, allowed_audience=None, allowed_clients=None, allowed_scopes=None, custom_claims=None):
        r"""CustomJWTAuthorizerConfiguration

        The model defined in huaweicloud sdk

        :param discovery_url: This URL is used to fetch OpenID Connect configuration.
        :type discovery_url: str
        :param allowed_audience: 
        :type allowed_audience: list[str]
        :param allowed_clients: 
        :type allowed_clients: list[str]
        :param allowed_scopes: 
        :type allowed_scopes: list[str]
        :param custom_claims: Custom claim validation rules applied to inbound JWTs.
        :type custom_claims: list[:class:`huaweicloudsdkagentidentity.v1.CustomClaimValidation`]
        """
        
        

        self._discovery_url = None
        self._allowed_audience = None
        self._allowed_clients = None
        self._allowed_scopes = None
        self._custom_claims = None
        self.discriminator = None

        self.discovery_url = discovery_url
        if allowed_audience is not None:
            self.allowed_audience = allowed_audience
        if allowed_clients is not None:
            self.allowed_clients = allowed_clients
        if allowed_scopes is not None:
            self.allowed_scopes = allowed_scopes
        if custom_claims is not None:
            self.custom_claims = custom_claims

    @property
    def discovery_url(self):
        r"""Gets the discovery_url of this CustomJWTAuthorizerConfiguration.

        This URL is used to fetch OpenID Connect configuration.

        :return: The discovery_url of this CustomJWTAuthorizerConfiguration.
        :rtype: str
        """
        return self._discovery_url

    @discovery_url.setter
    def discovery_url(self, discovery_url):
        r"""Sets the discovery_url of this CustomJWTAuthorizerConfiguration.

        This URL is used to fetch OpenID Connect configuration.

        :param discovery_url: The discovery_url of this CustomJWTAuthorizerConfiguration.
        :type discovery_url: str
        """
        self._discovery_url = discovery_url

    @property
    def allowed_audience(self):
        r"""Gets the allowed_audience of this CustomJWTAuthorizerConfiguration.

        :return: The allowed_audience of this CustomJWTAuthorizerConfiguration.
        :rtype: list[str]
        """
        return self._allowed_audience

    @allowed_audience.setter
    def allowed_audience(self, allowed_audience):
        r"""Sets the allowed_audience of this CustomJWTAuthorizerConfiguration.

        :param allowed_audience: The allowed_audience of this CustomJWTAuthorizerConfiguration.
        :type allowed_audience: list[str]
        """
        self._allowed_audience = allowed_audience

    @property
    def allowed_clients(self):
        r"""Gets the allowed_clients of this CustomJWTAuthorizerConfiguration.

        :return: The allowed_clients of this CustomJWTAuthorizerConfiguration.
        :rtype: list[str]
        """
        return self._allowed_clients

    @allowed_clients.setter
    def allowed_clients(self, allowed_clients):
        r"""Sets the allowed_clients of this CustomJWTAuthorizerConfiguration.

        :param allowed_clients: The allowed_clients of this CustomJWTAuthorizerConfiguration.
        :type allowed_clients: list[str]
        """
        self._allowed_clients = allowed_clients

    @property
    def allowed_scopes(self):
        r"""Gets the allowed_scopes of this CustomJWTAuthorizerConfiguration.

        :return: The allowed_scopes of this CustomJWTAuthorizerConfiguration.
        :rtype: list[str]
        """
        return self._allowed_scopes

    @allowed_scopes.setter
    def allowed_scopes(self, allowed_scopes):
        r"""Sets the allowed_scopes of this CustomJWTAuthorizerConfiguration.

        :param allowed_scopes: The allowed_scopes of this CustomJWTAuthorizerConfiguration.
        :type allowed_scopes: list[str]
        """
        self._allowed_scopes = allowed_scopes

    @property
    def custom_claims(self):
        r"""Gets the custom_claims of this CustomJWTAuthorizerConfiguration.

        Custom claim validation rules applied to inbound JWTs.

        :return: The custom_claims of this CustomJWTAuthorizerConfiguration.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.CustomClaimValidation`]
        """
        return self._custom_claims

    @custom_claims.setter
    def custom_claims(self, custom_claims):
        r"""Sets the custom_claims of this CustomJWTAuthorizerConfiguration.

        Custom claim validation rules applied to inbound JWTs.

        :param custom_claims: The custom_claims of this CustomJWTAuthorizerConfiguration.
        :type custom_claims: list[:class:`huaweicloudsdkagentidentity.v1.CustomClaimValidation`]
        """
        self._custom_claims = custom_claims

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
        if not isinstance(other, CustomJWTAuthorizerConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
