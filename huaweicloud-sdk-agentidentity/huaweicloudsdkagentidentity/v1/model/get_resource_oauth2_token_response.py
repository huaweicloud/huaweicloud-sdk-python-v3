# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetResourceOauth2TokenResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('access_token')

    openapi_types = {
        'access_token': 'str',
        'authorization_url': 'str',
        'session_status': 'str',
        'session_uri': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'authorization_url': 'authorization_url',
        'session_status': 'session_status',
        'session_uri': 'session_uri'
    }

    def __init__(self, access_token=None, authorization_url=None, session_status=None, session_uri=None):
        r"""GetResourceOauth2TokenResponse

        The model defined in huaweicloud sdk

        :param access_token: OAuth2.0 access token to use (embedded with RAR authorization details claims if rich_authorization_details were requested)
        :type access_token: str
        :param authorization_url: URL to initiate authorization (provided when user authorization is required, includes encoded RAR details for user consent)
        :type authorization_url: str
        :param session_status: Status of the user&#39;s authorization session (determines next steps in OAuth2 flow)
        :type session_status: str
        :param session_uri: Unique identifier for the user&#39;s authentication session (matches request session_uri)
        :type session_uri: str
        """
        
        super().__init__()

        self._access_token = None
        self._authorization_url = None
        self._session_status = None
        self._session_uri = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if authorization_url is not None:
            self.authorization_url = authorization_url
        if session_status is not None:
            self.session_status = session_status
        if session_uri is not None:
            self.session_uri = session_uri

    @property
    def access_token(self):
        r"""Gets the access_token of this GetResourceOauth2TokenResponse.

        OAuth2.0 access token to use (embedded with RAR authorization details claims if rich_authorization_details were requested)

        :return: The access_token of this GetResourceOauth2TokenResponse.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        r"""Sets the access_token of this GetResourceOauth2TokenResponse.

        OAuth2.0 access token to use (embedded with RAR authorization details claims if rich_authorization_details were requested)

        :param access_token: The access_token of this GetResourceOauth2TokenResponse.
        :type access_token: str
        """
        self._access_token = access_token

    @property
    def authorization_url(self):
        r"""Gets the authorization_url of this GetResourceOauth2TokenResponse.

        URL to initiate authorization (provided when user authorization is required, includes encoded RAR details for user consent)

        :return: The authorization_url of this GetResourceOauth2TokenResponse.
        :rtype: str
        """
        return self._authorization_url

    @authorization_url.setter
    def authorization_url(self, authorization_url):
        r"""Sets the authorization_url of this GetResourceOauth2TokenResponse.

        URL to initiate authorization (provided when user authorization is required, includes encoded RAR details for user consent)

        :param authorization_url: The authorization_url of this GetResourceOauth2TokenResponse.
        :type authorization_url: str
        """
        self._authorization_url = authorization_url

    @property
    def session_status(self):
        r"""Gets the session_status of this GetResourceOauth2TokenResponse.

        Status of the user's authorization session (determines next steps in OAuth2 flow)

        :return: The session_status of this GetResourceOauth2TokenResponse.
        :rtype: str
        """
        return self._session_status

    @session_status.setter
    def session_status(self, session_status):
        r"""Sets the session_status of this GetResourceOauth2TokenResponse.

        Status of the user's authorization session (determines next steps in OAuth2 flow)

        :param session_status: The session_status of this GetResourceOauth2TokenResponse.
        :type session_status: str
        """
        self._session_status = session_status

    @property
    def session_uri(self):
        r"""Gets the session_uri of this GetResourceOauth2TokenResponse.

        Unique identifier for the user's authentication session (matches request session_uri)

        :return: The session_uri of this GetResourceOauth2TokenResponse.
        :rtype: str
        """
        return self._session_uri

    @session_uri.setter
    def session_uri(self, session_uri):
        r"""Sets the session_uri of this GetResourceOauth2TokenResponse.

        Unique identifier for the user's authentication session (matches request session_uri)

        :param session_uri: The session_uri of this GetResourceOauth2TokenResponse.
        :type session_uri: str
        """
        self._session_uri = session_uri

    def to_dict(self):
        import warnings
        warnings.warn("GetResourceOauth2TokenResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, GetResourceOauth2TokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
