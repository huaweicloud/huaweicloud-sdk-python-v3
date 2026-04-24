# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOauth2CredentialProviderReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'oauth2_provider_config_input': 'Oauth2ProviderConfigInput',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'oauth2_provider_config_input': 'oauth2_provider_config_input',
        'tags': 'tags'
    }

    def __init__(self, oauth2_provider_config_input=None, tags=None):
        r"""UpdateOauth2CredentialProviderReqBody

        The model defined in huaweicloud sdk

        :param oauth2_provider_config_input: 
        :type oauth2_provider_config_input: :class:`huaweicloudsdkagentidentity.v1.Oauth2ProviderConfigInput`
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        
        

        self._oauth2_provider_config_input = None
        self._tags = None
        self.discriminator = None

        if oauth2_provider_config_input is not None:
            self.oauth2_provider_config_input = oauth2_provider_config_input
        if tags is not None:
            self.tags = tags

    @property
    def oauth2_provider_config_input(self):
        r"""Gets the oauth2_provider_config_input of this UpdateOauth2CredentialProviderReqBody.

        :return: The oauth2_provider_config_input of this UpdateOauth2CredentialProviderReqBody.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.Oauth2ProviderConfigInput`
        """
        return self._oauth2_provider_config_input

    @oauth2_provider_config_input.setter
    def oauth2_provider_config_input(self, oauth2_provider_config_input):
        r"""Sets the oauth2_provider_config_input of this UpdateOauth2CredentialProviderReqBody.

        :param oauth2_provider_config_input: The oauth2_provider_config_input of this UpdateOauth2CredentialProviderReqBody.
        :type oauth2_provider_config_input: :class:`huaweicloudsdkagentidentity.v1.Oauth2ProviderConfigInput`
        """
        self._oauth2_provider_config_input = oauth2_provider_config_input

    @property
    def tags(self):
        r"""Gets the tags of this UpdateOauth2CredentialProviderReqBody.

        自定义标签列表。

        :return: The tags of this UpdateOauth2CredentialProviderReqBody.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateOauth2CredentialProviderReqBody.

        自定义标签列表。

        :param tags: The tags of this UpdateOauth2CredentialProviderReqBody.
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, UpdateOauth2CredentialProviderReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
