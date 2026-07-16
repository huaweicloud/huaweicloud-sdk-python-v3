# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunCustomJWTAuthorizerConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'discovery_url': 'str',
        'allowed_audience': 'list[str]',
        'allowed_clients': 'list[str]',
        'allowed_scopes': 'list[str]',
        'custom_claims': 'list[CoreRunCustomClaimValidation]'
    }

    attribute_map = {
        'discovery_url': 'discovery_url',
        'allowed_audience': 'allowed_audience',
        'allowed_clients': 'allowed_clients',
        'allowed_scopes': 'allowed_scopes',
        'custom_claims': 'custom_claims'
    }

    def __init__(self, discovery_url=None, allowed_audience=None, allowed_clients=None, allowed_scopes=None, custom_claims=None):
        r"""CoreRunCustomJWTAuthorizerConfiguration

        The model defined in huaweicloud sdk

        :param discovery_url: **参数解释**：  此 URL 用于获取 OpenID Connect 配置或授权服务器元数据，以验证传入的令牌。 **约束限制**: 不涉及。 **取值范围**： 长度为 1 - 2048 个字符。 **默认取值**: 不涉及。
        :type discovery_url: str
        :param allowed_audience: **参数解释**：  允许对入站 JWT 进行验证的受众值列表。 **约束限制**: 不涉及。 **取值范围**： 元素个数0 - 10，每个受众值元素的长度为1-512个字符。 **默认取值**: 不涉及。
        :type allowed_audience: list[str]
        :param allowed_clients: **参数解释**：  允许用于入站 JWT 验证的客户端标识符值列表。 **约束限制**: 不涉及。 **取值范围**： 元素个数0 - 50，每个客户端值的长度为 1 - 256 个字符。 **默认取值**: 不涉及。
        :type allowed_clients: list[str]
        :param allowed_scopes: **参数解释**：  允许对入站 JWT 进行验证的范围值列表。 **约束限制**: 不涉及。 **取值范围**： 元素个数0 - 50，每个范围值的长度为 1 - 256 个字符。 **默认取值**: 不涉及。
        :type allowed_scopes: list[str]
        :param custom_claims: **参数解释**：  对入站 JWT 应用自定义声明验证规则。 **约束限制**: 不涉及。 **取值范围**： 最小数量 1，最大数量 20。 **默认取值**: 不涉及。
        :type custom_claims: list[:class:`huaweicloudsdkagentarts.v1.CoreRunCustomClaimValidation`]
        """
        
        

        self._discovery_url = None
        self._allowed_audience = None
        self._allowed_clients = None
        self._allowed_scopes = None
        self._custom_claims = None
        self.discriminator = None

        self.discovery_url = discovery_url
        if allowed_audience is not None:
            self.allowed_audience = allowed_audience
        if allowed_clients is not None:
            self.allowed_clients = allowed_clients
        if allowed_scopes is not None:
            self.allowed_scopes = allowed_scopes
        if custom_claims is not None:
            self.custom_claims = custom_claims

    @property
    def discovery_url(self):
        r"""Gets the discovery_url of this CoreRunCustomJWTAuthorizerConfiguration.

        **参数解释**：  此 URL 用于获取 OpenID Connect 配置或授权服务器元数据，以验证传入的令牌。 **约束限制**: 不涉及。 **取值范围**： 长度为 1 - 2048 个字符。 **默认取值**: 不涉及。

        :return: The discovery_url of this CoreRunCustomJWTAuthorizerConfiguration.
        :rtype: str
        """
        return self._discovery_url

    @discovery_url.setter
    def discovery_url(self, discovery_url):
        r"""Sets the discovery_url of this CoreRunCustomJWTAuthorizerConfiguration.

        **参数解释**：  此 URL 用于获取 OpenID Connect 配置或授权服务器元数据，以验证传入的令牌。 **约束限制**: 不涉及。 **取值范围**： 长度为 1 - 2048 个字符。 **默认取值**: 不涉及。

        :param discovery_url: The discovery_url of this CoreRunCustomJWTAuthorizerConfiguration.
        :type discovery_url: str
        """
        self._discovery_url = discovery_url

    @property
    def allowed_audience(self):
        r"""Gets the allowed_audience of this CoreRunCustomJWTAuthorizerConfiguration.

        **参数解释**：  允许对入站 JWT 进行验证的受众值列表。 **约束限制**: 不涉及。 **取值范围**： 元素个数0 - 10，每个受众值元素的长度为1-512个字符。 **默认取值**: 不涉及。

        :return: The allowed_audience of this CoreRunCustomJWTAuthorizerConfiguration.
        :rtype: list[str]
        """
        return self._allowed_audience

    @allowed_audience.setter
    def allowed_audience(self, allowed_audience):
        r"""Sets the allowed_audience of this CoreRunCustomJWTAuthorizerConfiguration.

        **参数解释**：  允许对入站 JWT 进行验证的受众值列表。 **约束限制**: 不涉及。 **取值范围**： 元素个数0 - 10，每个受众值元素的长度为1-512个字符。 **默认取值**: 不涉及。

        :param allowed_audience: The allowed_audience of this CoreRunCustomJWTAuthorizerConfiguration.
        :type allowed_audience: list[str]
        """
        self._allowed_audience = allowed_audience

    @property
    def allowed_clients(self):
        r"""Gets the allowed_clients of this CoreRunCustomJWTAuthorizerConfiguration.

        **参数解释**：  允许用于入站 JWT 验证的客户端标识符值列表。 **约束限制**: 不涉及。 **取值范围**： 元素个数0 - 50，每个客户端值的长度为 1 - 256 个字符。 **默认取值**: 不涉及。

        :return: The allowed_clients of this CoreRunCustomJWTAuthorizerConfiguration.
        :rtype: list[str]
        """
        return self._allowed_clients

    @allowed_clients.setter
    def allowed_clients(self, allowed_clients):
        r"""Sets the allowed_clients of this CoreRunCustomJWTAuthorizerConfiguration.

        **参数解释**：  允许用于入站 JWT 验证的客户端标识符值列表。 **约束限制**: 不涉及。 **取值范围**： 元素个数0 - 50，每个客户端值的长度为 1 - 256 个字符。 **默认取值**: 不涉及。

        :param allowed_clients: The allowed_clients of this CoreRunCustomJWTAuthorizerConfiguration.
        :type allowed_clients: list[str]
        """
        self._allowed_clients = allowed_clients

    @property
    def allowed_scopes(self):
        r"""Gets the allowed_scopes of this CoreRunCustomJWTAuthorizerConfiguration.

        **参数解释**：  允许对入站 JWT 进行验证的范围值列表。 **约束限制**: 不涉及。 **取值范围**： 元素个数0 - 50，每个范围值的长度为 1 - 256 个字符。 **默认取值**: 不涉及。

        :return: The allowed_scopes of this CoreRunCustomJWTAuthorizerConfiguration.
        :rtype: list[str]
        """
        return self._allowed_scopes

    @allowed_scopes.setter
    def allowed_scopes(self, allowed_scopes):
        r"""Sets the allowed_scopes of this CoreRunCustomJWTAuthorizerConfiguration.

        **参数解释**：  允许对入站 JWT 进行验证的范围值列表。 **约束限制**: 不涉及。 **取值范围**： 元素个数0 - 50，每个范围值的长度为 1 - 256 个字符。 **默认取值**: 不涉及。

        :param allowed_scopes: The allowed_scopes of this CoreRunCustomJWTAuthorizerConfiguration.
        :type allowed_scopes: list[str]
        """
        self._allowed_scopes = allowed_scopes

    @property
    def custom_claims(self):
        r"""Gets the custom_claims of this CoreRunCustomJWTAuthorizerConfiguration.

        **参数解释**：  对入站 JWT 应用自定义声明验证规则。 **约束限制**: 不涉及。 **取值范围**： 最小数量 1，最大数量 20。 **默认取值**: 不涉及。

        :return: The custom_claims of this CoreRunCustomJWTAuthorizerConfiguration.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreRunCustomClaimValidation`]
        """
        return self._custom_claims

    @custom_claims.setter
    def custom_claims(self, custom_claims):
        r"""Sets the custom_claims of this CoreRunCustomJWTAuthorizerConfiguration.

        **参数解释**：  对入站 JWT 应用自定义声明验证规则。 **约束限制**: 不涉及。 **取值范围**： 最小数量 1，最大数量 20。 **默认取值**: 不涉及。

        :param custom_claims: The custom_claims of this CoreRunCustomJWTAuthorizerConfiguration.
        :type custom_claims: list[:class:`huaweicloudsdkagentarts.v1.CoreRunCustomClaimValidation`]
        """
        self._custom_claims = custom_claims

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
        if not isinstance(other, CoreRunCustomJWTAuthorizerConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
