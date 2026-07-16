# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayApiKeyCredentialProvider:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_name': 'str',
        'credential_location': 'str',
        'credential_parameter_name': 'str',
        'credential_prefix': 'str'
    }

    attribute_map = {
        'provider_name': 'provider_name',
        'credential_location': 'credential_location',
        'credential_parameter_name': 'credential_parameter_name',
        'credential_prefix': 'credential_prefix'
    }

    def __init__(self, provider_name=None, credential_location=None, credential_parameter_name=None, credential_prefix=None):
        r"""CoreGatewayApiKeyCredentialProvider

        The model defined in huaweicloud sdk

        :param provider_name: **参数解释：** 凭证提供者名称。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-56 个字符，由字母、数字、下划线或短横线组成的、长度为1到56个字符的字符串，符合正则条件^[a-zA-Z0-9_-]{1,56}$。 **默认取值：** 不涉及。 
        :type provider_name: str
        :param credential_location: **参数解释：** 凭证传递位置。 **约束限制：** 不涉及。 **取值范围：** - &#x60;header&#x60;: 通过 HTTP 请求头传递 API 密钥 - &#x60;query&#x60;: 通过 URL 查询参数传递 API 密钥 **默认取值：** 不涉及。 
        :type credential_location: str
        :param credential_parameter_name: **参数解释：** 凭证参数名称。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-64 个字符。 **默认取值：** Authorization。 
        :type credential_parameter_name: str
        :param credential_prefix: **参数解释：** 凭证前缀（如 \&quot;Bearer \&quot;）。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-64 个字符。 **默认取值：** 不涉及。 
        :type credential_prefix: str
        """
        
        

        self._provider_name = None
        self._credential_location = None
        self._credential_parameter_name = None
        self._credential_prefix = None
        self.discriminator = None

        self.provider_name = provider_name
        self.credential_location = credential_location
        if credential_parameter_name is not None:
            self.credential_parameter_name = credential_parameter_name
        if credential_prefix is not None:
            self.credential_prefix = credential_prefix

    @property
    def provider_name(self):
        r"""Gets the provider_name of this CoreGatewayApiKeyCredentialProvider.

        **参数解释：** 凭证提供者名称。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-56 个字符，由字母、数字、下划线或短横线组成的、长度为1到56个字符的字符串，符合正则条件^[a-zA-Z0-9_-]{1,56}$。 **默认取值：** 不涉及。 

        :return: The provider_name of this CoreGatewayApiKeyCredentialProvider.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        r"""Sets the provider_name of this CoreGatewayApiKeyCredentialProvider.

        **参数解释：** 凭证提供者名称。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-56 个字符，由字母、数字、下划线或短横线组成的、长度为1到56个字符的字符串，符合正则条件^[a-zA-Z0-9_-]{1,56}$。 **默认取值：** 不涉及。 

        :param provider_name: The provider_name of this CoreGatewayApiKeyCredentialProvider.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def credential_location(self):
        r"""Gets the credential_location of this CoreGatewayApiKeyCredentialProvider.

        **参数解释：** 凭证传递位置。 **约束限制：** 不涉及。 **取值范围：** - `header`: 通过 HTTP 请求头传递 API 密钥 - `query`: 通过 URL 查询参数传递 API 密钥 **默认取值：** 不涉及。 

        :return: The credential_location of this CoreGatewayApiKeyCredentialProvider.
        :rtype: str
        """
        return self._credential_location

    @credential_location.setter
    def credential_location(self, credential_location):
        r"""Sets the credential_location of this CoreGatewayApiKeyCredentialProvider.

        **参数解释：** 凭证传递位置。 **约束限制：** 不涉及。 **取值范围：** - `header`: 通过 HTTP 请求头传递 API 密钥 - `query`: 通过 URL 查询参数传递 API 密钥 **默认取值：** 不涉及。 

        :param credential_location: The credential_location of this CoreGatewayApiKeyCredentialProvider.
        :type credential_location: str
        """
        self._credential_location = credential_location

    @property
    def credential_parameter_name(self):
        r"""Gets the credential_parameter_name of this CoreGatewayApiKeyCredentialProvider.

        **参数解释：** 凭证参数名称。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-64 个字符。 **默认取值：** Authorization。 

        :return: The credential_parameter_name of this CoreGatewayApiKeyCredentialProvider.
        :rtype: str
        """
        return self._credential_parameter_name

    @credential_parameter_name.setter
    def credential_parameter_name(self, credential_parameter_name):
        r"""Sets the credential_parameter_name of this CoreGatewayApiKeyCredentialProvider.

        **参数解释：** 凭证参数名称。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-64 个字符。 **默认取值：** Authorization。 

        :param credential_parameter_name: The credential_parameter_name of this CoreGatewayApiKeyCredentialProvider.
        :type credential_parameter_name: str
        """
        self._credential_parameter_name = credential_parameter_name

    @property
    def credential_prefix(self):
        r"""Gets the credential_prefix of this CoreGatewayApiKeyCredentialProvider.

        **参数解释：** 凭证前缀（如 \"Bearer \"）。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-64 个字符。 **默认取值：** 不涉及。 

        :return: The credential_prefix of this CoreGatewayApiKeyCredentialProvider.
        :rtype: str
        """
        return self._credential_prefix

    @credential_prefix.setter
    def credential_prefix(self, credential_prefix):
        r"""Sets the credential_prefix of this CoreGatewayApiKeyCredentialProvider.

        **参数解释：** 凭证前缀（如 \"Bearer \"）。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-64 个字符。 **默认取值：** 不涉及。 

        :param credential_prefix: The credential_prefix of this CoreGatewayApiKeyCredentialProvider.
        :type credential_prefix: str
        """
        self._credential_prefix = credential_prefix

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
        if not isinstance(other, CoreGatewayApiKeyCredentialProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
