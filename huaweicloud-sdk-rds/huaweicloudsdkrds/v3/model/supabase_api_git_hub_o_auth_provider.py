# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupabaseApiGitHubOAuthProvider:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_github': 'bool',
        'oauth_client_id': 'str',
        'redirect_uri': 'str'
    }

    attribute_map = {
        'enable_github': 'enable_github',
        'oauth_client_id': 'oauth_client_id',
        'redirect_uri': 'redirect_uri'
    }

    def __init__(self, enable_github=None, oauth_client_id=None, redirect_uri=None):
        r"""SupabaseApiGitHubOAuthProvider

        The model defined in huaweicloud sdk

        :param enable_github: 
        :type enable_github: bool
        :param oauth_client_id: 
        :type oauth_client_id: str
        :param redirect_uri: 
        :type redirect_uri: str
        """
        
        

        self._enable_github = None
        self._oauth_client_id = None
        self._redirect_uri = None
        self.discriminator = None

        if enable_github is not None:
            self.enable_github = enable_github
        if oauth_client_id is not None:
            self.oauth_client_id = oauth_client_id
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri

    @property
    def enable_github(self):
        r"""Gets the enable_github of this SupabaseApiGitHubOAuthProvider.

        :return: The enable_github of this SupabaseApiGitHubOAuthProvider.
        :rtype: bool
        """
        return self._enable_github

    @enable_github.setter
    def enable_github(self, enable_github):
        r"""Sets the enable_github of this SupabaseApiGitHubOAuthProvider.

        :param enable_github: The enable_github of this SupabaseApiGitHubOAuthProvider.
        :type enable_github: bool
        """
        self._enable_github = enable_github

    @property
    def oauth_client_id(self):
        r"""Gets the oauth_client_id of this SupabaseApiGitHubOAuthProvider.

        :return: The oauth_client_id of this SupabaseApiGitHubOAuthProvider.
        :rtype: str
        """
        return self._oauth_client_id

    @oauth_client_id.setter
    def oauth_client_id(self, oauth_client_id):
        r"""Sets the oauth_client_id of this SupabaseApiGitHubOAuthProvider.

        :param oauth_client_id: The oauth_client_id of this SupabaseApiGitHubOAuthProvider.
        :type oauth_client_id: str
        """
        self._oauth_client_id = oauth_client_id

    @property
    def redirect_uri(self):
        r"""Gets the redirect_uri of this SupabaseApiGitHubOAuthProvider.

        :return: The redirect_uri of this SupabaseApiGitHubOAuthProvider.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        r"""Sets the redirect_uri of this SupabaseApiGitHubOAuthProvider.

        :param redirect_uri: The redirect_uri of this SupabaseApiGitHubOAuthProvider.
        :type redirect_uri: str
        """
        self._redirect_uri = redirect_uri

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
        if not isinstance(other, SupabaseApiGitHubOAuthProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
