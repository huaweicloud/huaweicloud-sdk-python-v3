# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSupabaseApplicationAuthConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'updated_time': 'int',
        'enable_account_sign_up': 'bool',
        'enable_anonymous_users': 'bool',
        'api_external_url': 'str',
        'site_url': 'str',
        'allow_redirect_urls': 'str',
        'github_oauth_provider': 'SupabaseApiGitHubOAuthProvider',
        'email_oauth_provider': 'SupabaseApiEmailOAuthProvider',
        'email_template_config': 'SupabaseApiEmailTemplate'
    }

    attribute_map = {
        'updated_time': 'updated_time',
        'enable_account_sign_up': 'enable_account_sign_up',
        'enable_anonymous_users': 'enable_anonymous_users',
        'api_external_url': 'api_external_url',
        'site_url': 'site_url',
        'allow_redirect_urls': 'allow_redirect_urls',
        'github_oauth_provider': 'github_oauth_provider',
        'email_oauth_provider': 'email_oauth_provider',
        'email_template_config': 'email_template_config'
    }

    def __init__(self, updated_time=None, enable_account_sign_up=None, enable_anonymous_users=None, api_external_url=None, site_url=None, allow_redirect_urls=None, github_oauth_provider=None, email_oauth_provider=None, email_template_config=None):
        r"""ShowSupabaseApplicationAuthConfigResponse

        The model defined in huaweicloud sdk

        :param updated_time: 
        :type updated_time: int
        :param enable_account_sign_up: 
        :type enable_account_sign_up: bool
        :param enable_anonymous_users: 
        :type enable_anonymous_users: bool
        :param api_external_url: 
        :type api_external_url: str
        :param site_url: 
        :type site_url: str
        :param allow_redirect_urls: 
        :type allow_redirect_urls: str
        :param github_oauth_provider: 
        :type github_oauth_provider: :class:`huaweicloudsdkrds.v3.SupabaseApiGitHubOAuthProvider`
        :param email_oauth_provider: 
        :type email_oauth_provider: :class:`huaweicloudsdkrds.v3.SupabaseApiEmailOAuthProvider`
        :param email_template_config: 
        :type email_template_config: :class:`huaweicloudsdkrds.v3.SupabaseApiEmailTemplate`
        """
        
        super().__init__()

        self._updated_time = None
        self._enable_account_sign_up = None
        self._enable_anonymous_users = None
        self._api_external_url = None
        self._site_url = None
        self._allow_redirect_urls = None
        self._github_oauth_provider = None
        self._email_oauth_provider = None
        self._email_template_config = None
        self.discriminator = None

        if updated_time is not None:
            self.updated_time = updated_time
        if enable_account_sign_up is not None:
            self.enable_account_sign_up = enable_account_sign_up
        if enable_anonymous_users is not None:
            self.enable_anonymous_users = enable_anonymous_users
        if api_external_url is not None:
            self.api_external_url = api_external_url
        if site_url is not None:
            self.site_url = site_url
        if allow_redirect_urls is not None:
            self.allow_redirect_urls = allow_redirect_urls
        if github_oauth_provider is not None:
            self.github_oauth_provider = github_oauth_provider
        if email_oauth_provider is not None:
            self.email_oauth_provider = email_oauth_provider
        if email_template_config is not None:
            self.email_template_config = email_template_config

    @property
    def updated_time(self):
        r"""Gets the updated_time of this ShowSupabaseApplicationAuthConfigResponse.

        :return: The updated_time of this ShowSupabaseApplicationAuthConfigResponse.
        :rtype: int
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this ShowSupabaseApplicationAuthConfigResponse.

        :param updated_time: The updated_time of this ShowSupabaseApplicationAuthConfigResponse.
        :type updated_time: int
        """
        self._updated_time = updated_time

    @property
    def enable_account_sign_up(self):
        r"""Gets the enable_account_sign_up of this ShowSupabaseApplicationAuthConfigResponse.

        :return: The enable_account_sign_up of this ShowSupabaseApplicationAuthConfigResponse.
        :rtype: bool
        """
        return self._enable_account_sign_up

    @enable_account_sign_up.setter
    def enable_account_sign_up(self, enable_account_sign_up):
        r"""Sets the enable_account_sign_up of this ShowSupabaseApplicationAuthConfigResponse.

        :param enable_account_sign_up: The enable_account_sign_up of this ShowSupabaseApplicationAuthConfigResponse.
        :type enable_account_sign_up: bool
        """
        self._enable_account_sign_up = enable_account_sign_up

    @property
    def enable_anonymous_users(self):
        r"""Gets the enable_anonymous_users of this ShowSupabaseApplicationAuthConfigResponse.

        :return: The enable_anonymous_users of this ShowSupabaseApplicationAuthConfigResponse.
        :rtype: bool
        """
        return self._enable_anonymous_users

    @enable_anonymous_users.setter
    def enable_anonymous_users(self, enable_anonymous_users):
        r"""Sets the enable_anonymous_users of this ShowSupabaseApplicationAuthConfigResponse.

        :param enable_anonymous_users: The enable_anonymous_users of this ShowSupabaseApplicationAuthConfigResponse.
        :type enable_anonymous_users: bool
        """
        self._enable_anonymous_users = enable_anonymous_users

    @property
    def api_external_url(self):
        r"""Gets the api_external_url of this ShowSupabaseApplicationAuthConfigResponse.

        :return: The api_external_url of this ShowSupabaseApplicationAuthConfigResponse.
        :rtype: str
        """
        return self._api_external_url

    @api_external_url.setter
    def api_external_url(self, api_external_url):
        r"""Sets the api_external_url of this ShowSupabaseApplicationAuthConfigResponse.

        :param api_external_url: The api_external_url of this ShowSupabaseApplicationAuthConfigResponse.
        :type api_external_url: str
        """
        self._api_external_url = api_external_url

    @property
    def site_url(self):
        r"""Gets the site_url of this ShowSupabaseApplicationAuthConfigResponse.

        :return: The site_url of this ShowSupabaseApplicationAuthConfigResponse.
        :rtype: str
        """
        return self._site_url

    @site_url.setter
    def site_url(self, site_url):
        r"""Sets the site_url of this ShowSupabaseApplicationAuthConfigResponse.

        :param site_url: The site_url of this ShowSupabaseApplicationAuthConfigResponse.
        :type site_url: str
        """
        self._site_url = site_url

    @property
    def allow_redirect_urls(self):
        r"""Gets the allow_redirect_urls of this ShowSupabaseApplicationAuthConfigResponse.

        :return: The allow_redirect_urls of this ShowSupabaseApplicationAuthConfigResponse.
        :rtype: str
        """
        return self._allow_redirect_urls

    @allow_redirect_urls.setter
    def allow_redirect_urls(self, allow_redirect_urls):
        r"""Sets the allow_redirect_urls of this ShowSupabaseApplicationAuthConfigResponse.

        :param allow_redirect_urls: The allow_redirect_urls of this ShowSupabaseApplicationAuthConfigResponse.
        :type allow_redirect_urls: str
        """
        self._allow_redirect_urls = allow_redirect_urls

    @property
    def github_oauth_provider(self):
        r"""Gets the github_oauth_provider of this ShowSupabaseApplicationAuthConfigResponse.

        :return: The github_oauth_provider of this ShowSupabaseApplicationAuthConfigResponse.
        :rtype: :class:`huaweicloudsdkrds.v3.SupabaseApiGitHubOAuthProvider`
        """
        return self._github_oauth_provider

    @github_oauth_provider.setter
    def github_oauth_provider(self, github_oauth_provider):
        r"""Sets the github_oauth_provider of this ShowSupabaseApplicationAuthConfigResponse.

        :param github_oauth_provider: The github_oauth_provider of this ShowSupabaseApplicationAuthConfigResponse.
        :type github_oauth_provider: :class:`huaweicloudsdkrds.v3.SupabaseApiGitHubOAuthProvider`
        """
        self._github_oauth_provider = github_oauth_provider

    @property
    def email_oauth_provider(self):
        r"""Gets the email_oauth_provider of this ShowSupabaseApplicationAuthConfigResponse.

        :return: The email_oauth_provider of this ShowSupabaseApplicationAuthConfigResponse.
        :rtype: :class:`huaweicloudsdkrds.v3.SupabaseApiEmailOAuthProvider`
        """
        return self._email_oauth_provider

    @email_oauth_provider.setter
    def email_oauth_provider(self, email_oauth_provider):
        r"""Sets the email_oauth_provider of this ShowSupabaseApplicationAuthConfigResponse.

        :param email_oauth_provider: The email_oauth_provider of this ShowSupabaseApplicationAuthConfigResponse.
        :type email_oauth_provider: :class:`huaweicloudsdkrds.v3.SupabaseApiEmailOAuthProvider`
        """
        self._email_oauth_provider = email_oauth_provider

    @property
    def email_template_config(self):
        r"""Gets the email_template_config of this ShowSupabaseApplicationAuthConfigResponse.

        :return: The email_template_config of this ShowSupabaseApplicationAuthConfigResponse.
        :rtype: :class:`huaweicloudsdkrds.v3.SupabaseApiEmailTemplate`
        """
        return self._email_template_config

    @email_template_config.setter
    def email_template_config(self, email_template_config):
        r"""Sets the email_template_config of this ShowSupabaseApplicationAuthConfigResponse.

        :param email_template_config: The email_template_config of this ShowSupabaseApplicationAuthConfigResponse.
        :type email_template_config: :class:`huaweicloudsdkrds.v3.SupabaseApiEmailTemplate`
        """
        self._email_template_config = email_template_config

    def to_dict(self):
        import warnings
        warnings.warn("ShowSupabaseApplicationAuthConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSupabaseApplicationAuthConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
