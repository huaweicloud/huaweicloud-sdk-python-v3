# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreModelProviderCredentialProviderConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'credential_provider_type': 'str',
        'credential_provider': 'CoreModelProviderCredentialProvider'
    }

    attribute_map = {
        'credential_provider_type': 'credential_provider_type',
        'credential_provider': 'credential_provider'
    }

    def __init__(self, credential_provider_type=None, credential_provider=None):
        r"""CoreModelProviderCredentialProviderConfiguration

        The model defined in huaweicloud sdk

        :param credential_provider_type: **参数解释：** 凭证提供者类型。 **约束限制：** 不涉及。 **取值范围：** - &#x60;iam&#x60;: 使用网关 IAM 角色。 - &#x60;api_key&#x60;: 使用 API 密钥。 **默认取值：** 不涉及。 
        :type credential_provider_type: str
        :param credential_provider: 
        :type credential_provider: :class:`huaweicloudsdkagentarts.v1.CoreModelProviderCredentialProvider`
        """
        
        

        self._credential_provider_type = None
        self._credential_provider = None
        self.discriminator = None

        self.credential_provider_type = credential_provider_type
        if credential_provider is not None:
            self.credential_provider = credential_provider

    @property
    def credential_provider_type(self):
        r"""Gets the credential_provider_type of this CoreModelProviderCredentialProviderConfiguration.

        **参数解释：** 凭证提供者类型。 **约束限制：** 不涉及。 **取值范围：** - `iam`: 使用网关 IAM 角色。 - `api_key`: 使用 API 密钥。 **默认取值：** 不涉及。 

        :return: The credential_provider_type of this CoreModelProviderCredentialProviderConfiguration.
        :rtype: str
        """
        return self._credential_provider_type

    @credential_provider_type.setter
    def credential_provider_type(self, credential_provider_type):
        r"""Sets the credential_provider_type of this CoreModelProviderCredentialProviderConfiguration.

        **参数解释：** 凭证提供者类型。 **约束限制：** 不涉及。 **取值范围：** - `iam`: 使用网关 IAM 角色。 - `api_key`: 使用 API 密钥。 **默认取值：** 不涉及。 

        :param credential_provider_type: The credential_provider_type of this CoreModelProviderCredentialProviderConfiguration.
        :type credential_provider_type: str
        """
        self._credential_provider_type = credential_provider_type

    @property
    def credential_provider(self):
        r"""Gets the credential_provider of this CoreModelProviderCredentialProviderConfiguration.

        :return: The credential_provider of this CoreModelProviderCredentialProviderConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreModelProviderCredentialProvider`
        """
        return self._credential_provider

    @credential_provider.setter
    def credential_provider(self, credential_provider):
        r"""Sets the credential_provider of this CoreModelProviderCredentialProviderConfiguration.

        :param credential_provider: The credential_provider of this CoreModelProviderCredentialProviderConfiguration.
        :type credential_provider: :class:`huaweicloudsdkagentarts.v1.CoreModelProviderCredentialProvider`
        """
        self._credential_provider = credential_provider

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
        if not isinstance(other, CoreModelProviderCredentialProviderConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
