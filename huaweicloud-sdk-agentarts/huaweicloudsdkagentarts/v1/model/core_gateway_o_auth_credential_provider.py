# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayOAuthCredentialProvider:

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
        'grant_type': 'str',
        'scopes': 'list[str]',
        'default_return_url': 'str',
        'custom_parameters': 'dict(str, str)'
    }

    attribute_map = {
        'provider_name': 'provider_name',
        'grant_type': 'grant_type',
        'scopes': 'scopes',
        'default_return_url': 'default_return_url',
        'custom_parameters': 'custom_parameters'
    }

    def __init__(self, provider_name=None, grant_type=None, scopes=None, default_return_url=None, custom_parameters=None):
        r"""CoreGatewayOAuthCredentialProvider

        The model defined in huaweicloud sdk

        :param provider_name: **参数解释：** 凭证提供者名称。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-56 个字符，由字母、数字、下划线或短横线组成的、长度为1到56个字符的字符串，符合正则条件^[a-zA-Z0-9_-]{1,56}$。 **默认取值：** 不涉及。 
        :type provider_name: str
        :param grant_type: **参数解释：** OAuth 授权类型。 **约束限制：** 不涉及。 **取值范围：** - &#x60;client_credentials&#x60;: 适用于服务器到服务器通信 - &#x60;authorization_code&#x60;: 适用于需要用户授权的应用 **默认取值：** 不涉及。 
        :type grant_type: str
        :param scopes: **参数解释：** OAuth 作用域列表。 **约束限制：** 不涉及。 **取值范围：** 数组长度为 0-100。 **默认取值：** 不涉及。 
        :type scopes: list[str]
        :param default_return_url: **参数解释：** 默认返回 URL。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-2048，匹配由单词字符组成的协议名、冒号、零到两个斜杠，以及后续非空白字符序列的字符串，符合正则条件\\w+:(/?/?)[^\\s]+。 **默认取值：** 不涉及。 
        :type default_return_url: str
        :param custom_parameters: **参数解释：** 自定义参数，键值对形式。 **约束限制：** 不涉及。 **取值范围：** - 键：遵循 RFC 3986 URL 查询参数规范，最大长度 64，不允许为空 - 值：支持任意可打印 ASCII 字符，最大长度 255，可以为空 **默认取值：** 不涉及。 
        :type custom_parameters: dict(str, str)
        """
        
        

        self._provider_name = None
        self._grant_type = None
        self._scopes = None
        self._default_return_url = None
        self._custom_parameters = None
        self.discriminator = None

        self.provider_name = provider_name
        self.grant_type = grant_type
        if scopes is not None:
            self.scopes = scopes
        if default_return_url is not None:
            self.default_return_url = default_return_url
        if custom_parameters is not None:
            self.custom_parameters = custom_parameters

    @property
    def provider_name(self):
        r"""Gets the provider_name of this CoreGatewayOAuthCredentialProvider.

        **参数解释：** 凭证提供者名称。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-56 个字符，由字母、数字、下划线或短横线组成的、长度为1到56个字符的字符串，符合正则条件^[a-zA-Z0-9_-]{1,56}$。 **默认取值：** 不涉及。 

        :return: The provider_name of this CoreGatewayOAuthCredentialProvider.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        r"""Sets the provider_name of this CoreGatewayOAuthCredentialProvider.

        **参数解释：** 凭证提供者名称。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-56 个字符，由字母、数字、下划线或短横线组成的、长度为1到56个字符的字符串，符合正则条件^[a-zA-Z0-9_-]{1,56}$。 **默认取值：** 不涉及。 

        :param provider_name: The provider_name of this CoreGatewayOAuthCredentialProvider.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def grant_type(self):
        r"""Gets the grant_type of this CoreGatewayOAuthCredentialProvider.

        **参数解释：** OAuth 授权类型。 **约束限制：** 不涉及。 **取值范围：** - `client_credentials`: 适用于服务器到服务器通信 - `authorization_code`: 适用于需要用户授权的应用 **默认取值：** 不涉及。 

        :return: The grant_type of this CoreGatewayOAuthCredentialProvider.
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        r"""Sets the grant_type of this CoreGatewayOAuthCredentialProvider.

        **参数解释：** OAuth 授权类型。 **约束限制：** 不涉及。 **取值范围：** - `client_credentials`: 适用于服务器到服务器通信 - `authorization_code`: 适用于需要用户授权的应用 **默认取值：** 不涉及。 

        :param grant_type: The grant_type of this CoreGatewayOAuthCredentialProvider.
        :type grant_type: str
        """
        self._grant_type = grant_type

    @property
    def scopes(self):
        r"""Gets the scopes of this CoreGatewayOAuthCredentialProvider.

        **参数解释：** OAuth 作用域列表。 **约束限制：** 不涉及。 **取值范围：** 数组长度为 0-100。 **默认取值：** 不涉及。 

        :return: The scopes of this CoreGatewayOAuthCredentialProvider.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        r"""Sets the scopes of this CoreGatewayOAuthCredentialProvider.

        **参数解释：** OAuth 作用域列表。 **约束限制：** 不涉及。 **取值范围：** 数组长度为 0-100。 **默认取值：** 不涉及。 

        :param scopes: The scopes of this CoreGatewayOAuthCredentialProvider.
        :type scopes: list[str]
        """
        self._scopes = scopes

    @property
    def default_return_url(self):
        r"""Gets the default_return_url of this CoreGatewayOAuthCredentialProvider.

        **参数解释：** 默认返回 URL。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-2048，匹配由单词字符组成的协议名、冒号、零到两个斜杠，以及后续非空白字符序列的字符串，符合正则条件\\w+:(/?/?)[^\\s]+。 **默认取值：** 不涉及。 

        :return: The default_return_url of this CoreGatewayOAuthCredentialProvider.
        :rtype: str
        """
        return self._default_return_url

    @default_return_url.setter
    def default_return_url(self, default_return_url):
        r"""Sets the default_return_url of this CoreGatewayOAuthCredentialProvider.

        **参数解释：** 默认返回 URL。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-2048，匹配由单词字符组成的协议名、冒号、零到两个斜杠，以及后续非空白字符序列的字符串，符合正则条件\\w+:(/?/?)[^\\s]+。 **默认取值：** 不涉及。 

        :param default_return_url: The default_return_url of this CoreGatewayOAuthCredentialProvider.
        :type default_return_url: str
        """
        self._default_return_url = default_return_url

    @property
    def custom_parameters(self):
        r"""Gets the custom_parameters of this CoreGatewayOAuthCredentialProvider.

        **参数解释：** 自定义参数，键值对形式。 **约束限制：** 不涉及。 **取值范围：** - 键：遵循 RFC 3986 URL 查询参数规范，最大长度 64，不允许为空 - 值：支持任意可打印 ASCII 字符，最大长度 255，可以为空 **默认取值：** 不涉及。 

        :return: The custom_parameters of this CoreGatewayOAuthCredentialProvider.
        :rtype: dict(str, str)
        """
        return self._custom_parameters

    @custom_parameters.setter
    def custom_parameters(self, custom_parameters):
        r"""Sets the custom_parameters of this CoreGatewayOAuthCredentialProvider.

        **参数解释：** 自定义参数，键值对形式。 **约束限制：** 不涉及。 **取值范围：** - 键：遵循 RFC 3986 URL 查询参数规范，最大长度 64，不允许为空 - 值：支持任意可打印 ASCII 字符，最大长度 255，可以为空 **默认取值：** 不涉及。 

        :param custom_parameters: The custom_parameters of this CoreGatewayOAuthCredentialProvider.
        :type custom_parameters: dict(str, str)
        """
        self._custom_parameters = custom_parameters

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
        if not isinstance(other, CoreGatewayOAuthCredentialProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
