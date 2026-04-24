# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Oauth2ProviderConfigOutput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'microsoft_oauth2_provider_config': 'MicrosoftOauth2ProviderConfigOutput',
        'google_oauth2_provider_config': 'GoogleOauth2ProviderConfigOutput',
        'github_oauth2_provider_config': 'GithubOauth2ProviderConfigOutput',
        'custom_oauth2_provider_config': 'CustomOauth2ProviderConfigOutput'
    }

    attribute_map = {
        'microsoft_oauth2_provider_config': 'microsoft_oauth2_provider_config',
        'google_oauth2_provider_config': 'google_oauth2_provider_config',
        'github_oauth2_provider_config': 'github_oauth2_provider_config',
        'custom_oauth2_provider_config': 'custom_oauth2_provider_config'
    }

    def __init__(self, microsoft_oauth2_provider_config=None, google_oauth2_provider_config=None, github_oauth2_provider_config=None, custom_oauth2_provider_config=None):
        r"""Oauth2ProviderConfigOutput

        The model defined in huaweicloud sdk

        :param microsoft_oauth2_provider_config: 
        :type microsoft_oauth2_provider_config: :class:`huaweicloudsdkagentidentity.v1.MicrosoftOauth2ProviderConfigOutput`
        :param google_oauth2_provider_config: 
        :type google_oauth2_provider_config: :class:`huaweicloudsdkagentidentity.v1.GoogleOauth2ProviderConfigOutput`
        :param github_oauth2_provider_config: 
        :type github_oauth2_provider_config: :class:`huaweicloudsdkagentidentity.v1.GithubOauth2ProviderConfigOutput`
        :param custom_oauth2_provider_config: 
        :type custom_oauth2_provider_config: :class:`huaweicloudsdkagentidentity.v1.CustomOauth2ProviderConfigOutput`
        """
        
        

        self._microsoft_oauth2_provider_config = None
        self._google_oauth2_provider_config = None
        self._github_oauth2_provider_config = None
        self._custom_oauth2_provider_config = None
        self.discriminator = None

        if microsoft_oauth2_provider_config is not None:
            self.microsoft_oauth2_provider_config = microsoft_oauth2_provider_config
        if google_oauth2_provider_config is not None:
            self.google_oauth2_provider_config = google_oauth2_provider_config
        if github_oauth2_provider_config is not None:
            self.github_oauth2_provider_config = github_oauth2_provider_config
        if custom_oauth2_provider_config is not None:
            self.custom_oauth2_provider_config = custom_oauth2_provider_config

    @property
    def microsoft_oauth2_provider_config(self):
        r"""Gets the microsoft_oauth2_provider_config of this Oauth2ProviderConfigOutput.

        :return: The microsoft_oauth2_provider_config of this Oauth2ProviderConfigOutput.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.MicrosoftOauth2ProviderConfigOutput`
        """
        return self._microsoft_oauth2_provider_config

    @microsoft_oauth2_provider_config.setter
    def microsoft_oauth2_provider_config(self, microsoft_oauth2_provider_config):
        r"""Sets the microsoft_oauth2_provider_config of this Oauth2ProviderConfigOutput.

        :param microsoft_oauth2_provider_config: The microsoft_oauth2_provider_config of this Oauth2ProviderConfigOutput.
        :type microsoft_oauth2_provider_config: :class:`huaweicloudsdkagentidentity.v1.MicrosoftOauth2ProviderConfigOutput`
        """
        self._microsoft_oauth2_provider_config = microsoft_oauth2_provider_config

    @property
    def google_oauth2_provider_config(self):
        r"""Gets the google_oauth2_provider_config of this Oauth2ProviderConfigOutput.

        :return: The google_oauth2_provider_config of this Oauth2ProviderConfigOutput.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.GoogleOauth2ProviderConfigOutput`
        """
        return self._google_oauth2_provider_config

    @google_oauth2_provider_config.setter
    def google_oauth2_provider_config(self, google_oauth2_provider_config):
        r"""Sets the google_oauth2_provider_config of this Oauth2ProviderConfigOutput.

        :param google_oauth2_provider_config: The google_oauth2_provider_config of this Oauth2ProviderConfigOutput.
        :type google_oauth2_provider_config: :class:`huaweicloudsdkagentidentity.v1.GoogleOauth2ProviderConfigOutput`
        """
        self._google_oauth2_provider_config = google_oauth2_provider_config

    @property
    def github_oauth2_provider_config(self):
        r"""Gets the github_oauth2_provider_config of this Oauth2ProviderConfigOutput.

        :return: The github_oauth2_provider_config of this Oauth2ProviderConfigOutput.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.GithubOauth2ProviderConfigOutput`
        """
        return self._github_oauth2_provider_config

    @github_oauth2_provider_config.setter
    def github_oauth2_provider_config(self, github_oauth2_provider_config):
        r"""Sets the github_oauth2_provider_config of this Oauth2ProviderConfigOutput.

        :param github_oauth2_provider_config: The github_oauth2_provider_config of this Oauth2ProviderConfigOutput.
        :type github_oauth2_provider_config: :class:`huaweicloudsdkagentidentity.v1.GithubOauth2ProviderConfigOutput`
        """
        self._github_oauth2_provider_config = github_oauth2_provider_config

    @property
    def custom_oauth2_provider_config(self):
        r"""Gets the custom_oauth2_provider_config of this Oauth2ProviderConfigOutput.

        :return: The custom_oauth2_provider_config of this Oauth2ProviderConfigOutput.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.CustomOauth2ProviderConfigOutput`
        """
        return self._custom_oauth2_provider_config

    @custom_oauth2_provider_config.setter
    def custom_oauth2_provider_config(self, custom_oauth2_provider_config):
        r"""Sets the custom_oauth2_provider_config of this Oauth2ProviderConfigOutput.

        :param custom_oauth2_provider_config: The custom_oauth2_provider_config of this Oauth2ProviderConfigOutput.
        :type custom_oauth2_provider_config: :class:`huaweicloudsdkagentidentity.v1.CustomOauth2ProviderConfigOutput`
        """
        self._custom_oauth2_provider_config = custom_oauth2_provider_config

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
        if not isinstance(other, Oauth2ProviderConfigOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
