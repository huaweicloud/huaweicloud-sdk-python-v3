# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOauth2CredentialProviderReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'credential_provider_vendor': 'CredentialProviderVendor',
        'oauth2_provider_config_input': 'Oauth2ProviderConfigInput',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'credential_provider_vendor': 'credential_provider_vendor',
        'oauth2_provider_config_input': 'oauth2_provider_config_input',
        'tags': 'tags'
    }

    def __init__(self, name=None, credential_provider_vendor=None, oauth2_provider_config_input=None, tags=None):
        r"""CreateOauth2CredentialProviderReqBody

        The model defined in huaweicloud sdk

        :param name: The name of the credential provider.
        :type name: str
        :param credential_provider_vendor: 
        :type credential_provider_vendor: :class:`huaweicloudsdkagentidentity.v1.CredentialProviderVendor`
        :param oauth2_provider_config_input: 
        :type oauth2_provider_config_input: :class:`huaweicloudsdkagentidentity.v1.Oauth2ProviderConfigInput`
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        
        

        self._name = None
        self._credential_provider_vendor = None
        self._oauth2_provider_config_input = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.credential_provider_vendor = credential_provider_vendor
        self.oauth2_provider_config_input = oauth2_provider_config_input
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateOauth2CredentialProviderReqBody.

        The name of the credential provider.

        :return: The name of this CreateOauth2CredentialProviderReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateOauth2CredentialProviderReqBody.

        The name of the credential provider.

        :param name: The name of this CreateOauth2CredentialProviderReqBody.
        :type name: str
        """
        self._name = name

    @property
    def credential_provider_vendor(self):
        r"""Gets the credential_provider_vendor of this CreateOauth2CredentialProviderReqBody.

        :return: The credential_provider_vendor of this CreateOauth2CredentialProviderReqBody.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.CredentialProviderVendor`
        """
        return self._credential_provider_vendor

    @credential_provider_vendor.setter
    def credential_provider_vendor(self, credential_provider_vendor):
        r"""Sets the credential_provider_vendor of this CreateOauth2CredentialProviderReqBody.

        :param credential_provider_vendor: The credential_provider_vendor of this CreateOauth2CredentialProviderReqBody.
        :type credential_provider_vendor: :class:`huaweicloudsdkagentidentity.v1.CredentialProviderVendor`
        """
        self._credential_provider_vendor = credential_provider_vendor

    @property
    def oauth2_provider_config_input(self):
        r"""Gets the oauth2_provider_config_input of this CreateOauth2CredentialProviderReqBody.

        :return: The oauth2_provider_config_input of this CreateOauth2CredentialProviderReqBody.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.Oauth2ProviderConfigInput`
        """
        return self._oauth2_provider_config_input

    @oauth2_provider_config_input.setter
    def oauth2_provider_config_input(self, oauth2_provider_config_input):
        r"""Sets the oauth2_provider_config_input of this CreateOauth2CredentialProviderReqBody.

        :param oauth2_provider_config_input: The oauth2_provider_config_input of this CreateOauth2CredentialProviderReqBody.
        :type oauth2_provider_config_input: :class:`huaweicloudsdkagentidentity.v1.Oauth2ProviderConfigInput`
        """
        self._oauth2_provider_config_input = oauth2_provider_config_input

    @property
    def tags(self):
        r"""Gets the tags of this CreateOauth2CredentialProviderReqBody.

        自定义标签列表。

        :return: The tags of this CreateOauth2CredentialProviderReqBody.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateOauth2CredentialProviderReqBody.

        自定义标签列表。

        :param tags: The tags of this CreateOauth2CredentialProviderReqBody.
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
        if not isinstance(other, CreateOauth2CredentialProviderReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
