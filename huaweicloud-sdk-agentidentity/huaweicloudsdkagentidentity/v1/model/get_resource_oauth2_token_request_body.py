# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetResourceOauth2TokenRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('workload_access_token')

    openapi_types = {
        'custom_parameters': 'dict(str, str)',
        'custom_state': 'str',
        'force_authentication': 'bool',
        'oauth2_flow': 'str',
        'resource_credential_provider_name': 'str',
        'resource_oauth2_return_url': 'str',
        'scopes': 'list[str]',
        'session_uri': 'str',
        'workload_access_token': 'str'
    }

    attribute_map = {
        'custom_parameters': 'custom_parameters',
        'custom_state': 'custom_state',
        'force_authentication': 'force_authentication',
        'oauth2_flow': 'oauth2_flow',
        'resource_credential_provider_name': 'resource_credential_provider_name',
        'resource_oauth2_return_url': 'resource_oauth2_return_url',
        'scopes': 'scopes',
        'session_uri': 'session_uri',
        'workload_access_token': 'workload_access_token'
    }

    def __init__(self, custom_parameters=None, custom_state=None, force_authentication=None, oauth2_flow=None, resource_credential_provider_name=None, resource_oauth2_return_url=None, scopes=None, session_uri=None, workload_access_token=None):
        r"""GetResourceOauth2TokenRequestBody

        The model defined in huaweicloud sdk

        :param custom_parameters: Additional custom parameters for the authorization request (does not override standard OAuth2 parameters)
        :type custom_parameters: dict(str, str)
        :param custom_state: Opaque string for CSRF protection (returned in callback URL response as standard state parameter)
        :type custom_state: str
        :param force_authentication: Whether to initiate a new 3LO flow regardless of existing sessions
        :type force_authentication: bool
        :param oauth2_flow: Type of OAuth2 flow to perform
        :type oauth2_flow: str
        :param resource_credential_provider_name: Name of the resource&#39;s credential provider
        :type resource_credential_provider_name: str
        :param resource_oauth2_return_url: Callback URL to redirect after token retrieval (must be configured for workload identity)
        :type resource_oauth2_return_url: str
        :param scopes: OAuth scopes being requested (coarse-grained permissions, supplemented by rich_authorization_details for fine-grained control)
        :type scopes: list[str]
        :param session_uri: Unique identifier for the user&#39;s authentication session (tracks OAuth2 flow state)
        :type session_uri: str
        :param workload_access_token: Identity token of the workload requesting the OAuth2 token
        :type workload_access_token: str
        """
        
        

        self._custom_parameters = None
        self._custom_state = None
        self._force_authentication = None
        self._oauth2_flow = None
        self._resource_credential_provider_name = None
        self._resource_oauth2_return_url = None
        self._scopes = None
        self._session_uri = None
        self._workload_access_token = None
        self.discriminator = None

        if custom_parameters is not None:
            self.custom_parameters = custom_parameters
        if custom_state is not None:
            self.custom_state = custom_state
        if force_authentication is not None:
            self.force_authentication = force_authentication
        self.oauth2_flow = oauth2_flow
        self.resource_credential_provider_name = resource_credential_provider_name
        if resource_oauth2_return_url is not None:
            self.resource_oauth2_return_url = resource_oauth2_return_url
        if scopes is not None:
            self.scopes = scopes
        if session_uri is not None:
            self.session_uri = session_uri
        if workload_access_token is not None:
            self.workload_access_token = workload_access_token

    @property
    def custom_parameters(self):
        r"""Gets the custom_parameters of this GetResourceOauth2TokenRequestBody.

        Additional custom parameters for the authorization request (does not override standard OAuth2 parameters)

        :return: The custom_parameters of this GetResourceOauth2TokenRequestBody.
        :rtype: dict(str, str)
        """
        return self._custom_parameters

    @custom_parameters.setter
    def custom_parameters(self, custom_parameters):
        r"""Sets the custom_parameters of this GetResourceOauth2TokenRequestBody.

        Additional custom parameters for the authorization request (does not override standard OAuth2 parameters)

        :param custom_parameters: The custom_parameters of this GetResourceOauth2TokenRequestBody.
        :type custom_parameters: dict(str, str)
        """
        self._custom_parameters = custom_parameters

    @property
    def custom_state(self):
        r"""Gets the custom_state of this GetResourceOauth2TokenRequestBody.

        Opaque string for CSRF protection (returned in callback URL response as standard state parameter)

        :return: The custom_state of this GetResourceOauth2TokenRequestBody.
        :rtype: str
        """
        return self._custom_state

    @custom_state.setter
    def custom_state(self, custom_state):
        r"""Sets the custom_state of this GetResourceOauth2TokenRequestBody.

        Opaque string for CSRF protection (returned in callback URL response as standard state parameter)

        :param custom_state: The custom_state of this GetResourceOauth2TokenRequestBody.
        :type custom_state: str
        """
        self._custom_state = custom_state

    @property
    def force_authentication(self):
        r"""Gets the force_authentication of this GetResourceOauth2TokenRequestBody.

        Whether to initiate a new 3LO flow regardless of existing sessions

        :return: The force_authentication of this GetResourceOauth2TokenRequestBody.
        :rtype: bool
        """
        return self._force_authentication

    @force_authentication.setter
    def force_authentication(self, force_authentication):
        r"""Sets the force_authentication of this GetResourceOauth2TokenRequestBody.

        Whether to initiate a new 3LO flow regardless of existing sessions

        :param force_authentication: The force_authentication of this GetResourceOauth2TokenRequestBody.
        :type force_authentication: bool
        """
        self._force_authentication = force_authentication

    @property
    def oauth2_flow(self):
        r"""Gets the oauth2_flow of this GetResourceOauth2TokenRequestBody.

        Type of OAuth2 flow to perform

        :return: The oauth2_flow of this GetResourceOauth2TokenRequestBody.
        :rtype: str
        """
        return self._oauth2_flow

    @oauth2_flow.setter
    def oauth2_flow(self, oauth2_flow):
        r"""Sets the oauth2_flow of this GetResourceOauth2TokenRequestBody.

        Type of OAuth2 flow to perform

        :param oauth2_flow: The oauth2_flow of this GetResourceOauth2TokenRequestBody.
        :type oauth2_flow: str
        """
        self._oauth2_flow = oauth2_flow

    @property
    def resource_credential_provider_name(self):
        r"""Gets the resource_credential_provider_name of this GetResourceOauth2TokenRequestBody.

        Name of the resource's credential provider

        :return: The resource_credential_provider_name of this GetResourceOauth2TokenRequestBody.
        :rtype: str
        """
        return self._resource_credential_provider_name

    @resource_credential_provider_name.setter
    def resource_credential_provider_name(self, resource_credential_provider_name):
        r"""Sets the resource_credential_provider_name of this GetResourceOauth2TokenRequestBody.

        Name of the resource's credential provider

        :param resource_credential_provider_name: The resource_credential_provider_name of this GetResourceOauth2TokenRequestBody.
        :type resource_credential_provider_name: str
        """
        self._resource_credential_provider_name = resource_credential_provider_name

    @property
    def resource_oauth2_return_url(self):
        r"""Gets the resource_oauth2_return_url of this GetResourceOauth2TokenRequestBody.

        Callback URL to redirect after token retrieval (must be configured for workload identity)

        :return: The resource_oauth2_return_url of this GetResourceOauth2TokenRequestBody.
        :rtype: str
        """
        return self._resource_oauth2_return_url

    @resource_oauth2_return_url.setter
    def resource_oauth2_return_url(self, resource_oauth2_return_url):
        r"""Sets the resource_oauth2_return_url of this GetResourceOauth2TokenRequestBody.

        Callback URL to redirect after token retrieval (must be configured for workload identity)

        :param resource_oauth2_return_url: The resource_oauth2_return_url of this GetResourceOauth2TokenRequestBody.
        :type resource_oauth2_return_url: str
        """
        self._resource_oauth2_return_url = resource_oauth2_return_url

    @property
    def scopes(self):
        r"""Gets the scopes of this GetResourceOauth2TokenRequestBody.

        OAuth scopes being requested (coarse-grained permissions, supplemented by rich_authorization_details for fine-grained control)

        :return: The scopes of this GetResourceOauth2TokenRequestBody.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        r"""Sets the scopes of this GetResourceOauth2TokenRequestBody.

        OAuth scopes being requested (coarse-grained permissions, supplemented by rich_authorization_details for fine-grained control)

        :param scopes: The scopes of this GetResourceOauth2TokenRequestBody.
        :type scopes: list[str]
        """
        self._scopes = scopes

    @property
    def session_uri(self):
        r"""Gets the session_uri of this GetResourceOauth2TokenRequestBody.

        Unique identifier for the user's authentication session (tracks OAuth2 flow state)

        :return: The session_uri of this GetResourceOauth2TokenRequestBody.
        :rtype: str
        """
        return self._session_uri

    @session_uri.setter
    def session_uri(self, session_uri):
        r"""Sets the session_uri of this GetResourceOauth2TokenRequestBody.

        Unique identifier for the user's authentication session (tracks OAuth2 flow state)

        :param session_uri: The session_uri of this GetResourceOauth2TokenRequestBody.
        :type session_uri: str
        """
        self._session_uri = session_uri

    @property
    def workload_access_token(self):
        r"""Gets the workload_access_token of this GetResourceOauth2TokenRequestBody.

        Identity token of the workload requesting the OAuth2 token

        :return: The workload_access_token of this GetResourceOauth2TokenRequestBody.
        :rtype: str
        """
        return self._workload_access_token

    @workload_access_token.setter
    def workload_access_token(self, workload_access_token):
        r"""Sets the workload_access_token of this GetResourceOauth2TokenRequestBody.

        Identity token of the workload requesting the OAuth2 token

        :param workload_access_token: The workload_access_token of this GetResourceOauth2TokenRequestBody.
        :type workload_access_token: str
        """
        self._workload_access_token = workload_access_token

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
        if not isinstance(other, GetResourceOauth2TokenRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
