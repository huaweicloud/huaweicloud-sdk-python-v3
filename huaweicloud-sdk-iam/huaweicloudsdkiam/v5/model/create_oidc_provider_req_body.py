# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOIDCProviderReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'name': 'str',
        'client_ids': 'list[str]',
        'thumbprints': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'url': 'url',
        'name': 'name',
        'client_ids': 'client_ids',
        'thumbprints': 'thumbprints',
        'description': 'description'
    }

    def __init__(self, url=None, name=None, client_ids=None, thumbprints=None, description=None):
        r"""CreateOIDCProviderReqBody

        The model defined in huaweicloud sdk

        :param url: **参数解释**： 身份提供商的 URL。该 URL 必须以 https:// 开头，并且应与提供商的 OpenID Connect ID 令牌中的 iss (issuer) 声明相对应。根据 OIDC 标准，URL 允许包含路径组件，但不允许包含查询参数。通常，该 URL 仅由一个主机名组成，不包含端口号，例如 https://www.oidc.com 或 https://oidc.com。  **约束限制**： 长度范围为[1,255]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。
        :type url: str
        :param name: **参数解释**： OIDC 提供商的名称。  **约束限制**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、下划线（_）、中划线（-）。  **取值范围**： 不涉及。  **默认取值**： 不涉及。
        :type name: str
        :param client_ids: **参数解释**： 客户端 ID 列表，客户端 ID 也称为受众 (Audiences)。您可以使用同一个提供商注册多个客户端 ID。  **约束限制**： 列表元素数量取值范围为[1,100]个，每个元素字符串长度取值范围为[1,255]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。
        :type client_ids: list[str]
        :param thumbprints: **参数解释**： OIDC 身份提供商的服务器证书指纹列表，列表中的指纹是 X.509 证书的十六进制编码的 SHA-1 哈希值，它始终是一个 64 个字符的字符串。通常，此列表只包含一个指纹，然而 IAM 允许您为一个 OIDC 提供商设置最多五个指纹，这使得您可以对身份提供商的证书进行安全轮转。此参数是可选的，如果未包含此参数，IAM 将检索并使用 OIDC 身份提供商服务器证书的顶层中间证书颁发机构 (CA) 指纹。有关获取 OIDC 提供商指纹的更多信息，请参阅 IAM 用户指南中的**获取 OIDC 提供商的指纹**。  **约束限制**： 列表元素数量取值范围为[0,5]个，每个元素字符串长度为64。  **取值范围**： 不涉及。  **默认取值**： 不涉及。
        :type thumbprints: list[str]
        :param description: **参数解释**： 身份提供商描述。  **约束限制**： 长度范围为[0,255]。  **取值范围**： 不能包含特定字符\&quot;@\&quot;、\&quot;#\&quot;、\&quot;%\&quot;、\&quot;&amp;\&quot;、\&quot;&lt;\&quot;、\&quot;&gt;\&quot;、\&quot;\\\&quot;、\&quot;$\&quot;、\&quot;^\&quot;和\&quot;*\&quot;的字符串。  **默认取值**： 不涉及。
        :type description: str
        """
        
        

        self._url = None
        self._name = None
        self._client_ids = None
        self._thumbprints = None
        self._description = None
        self.discriminator = None

        self.url = url
        self.name = name
        self.client_ids = client_ids
        if thumbprints is not None:
            self.thumbprints = thumbprints
        if description is not None:
            self.description = description

    @property
    def url(self):
        r"""Gets the url of this CreateOIDCProviderReqBody.

        **参数解释**： 身份提供商的 URL。该 URL 必须以 https:// 开头，并且应与提供商的 OpenID Connect ID 令牌中的 iss (issuer) 声明相对应。根据 OIDC 标准，URL 允许包含路径组件，但不允许包含查询参数。通常，该 URL 仅由一个主机名组成，不包含端口号，例如 https://www.oidc.com 或 https://oidc.com。  **约束限制**： 长度范围为[1,255]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :return: The url of this CreateOIDCProviderReqBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateOIDCProviderReqBody.

        **参数解释**： 身份提供商的 URL。该 URL 必须以 https:// 开头，并且应与提供商的 OpenID Connect ID 令牌中的 iss (issuer) 声明相对应。根据 OIDC 标准，URL 允许包含路径组件，但不允许包含查询参数。通常，该 URL 仅由一个主机名组成，不包含端口号，例如 https://www.oidc.com 或 https://oidc.com。  **约束限制**： 长度范围为[1,255]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :param url: The url of this CreateOIDCProviderReqBody.
        :type url: str
        """
        self._url = url

    @property
    def name(self):
        r"""Gets the name of this CreateOIDCProviderReqBody.

        **参数解释**： OIDC 提供商的名称。  **约束限制**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、下划线（_）、中划线（-）。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :return: The name of this CreateOIDCProviderReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateOIDCProviderReqBody.

        **参数解释**： OIDC 提供商的名称。  **约束限制**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、下划线（_）、中划线（-）。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :param name: The name of this CreateOIDCProviderReqBody.
        :type name: str
        """
        self._name = name

    @property
    def client_ids(self):
        r"""Gets the client_ids of this CreateOIDCProviderReqBody.

        **参数解释**： 客户端 ID 列表，客户端 ID 也称为受众 (Audiences)。您可以使用同一个提供商注册多个客户端 ID。  **约束限制**： 列表元素数量取值范围为[1,100]个，每个元素字符串长度取值范围为[1,255]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :return: The client_ids of this CreateOIDCProviderReqBody.
        :rtype: list[str]
        """
        return self._client_ids

    @client_ids.setter
    def client_ids(self, client_ids):
        r"""Sets the client_ids of this CreateOIDCProviderReqBody.

        **参数解释**： 客户端 ID 列表，客户端 ID 也称为受众 (Audiences)。您可以使用同一个提供商注册多个客户端 ID。  **约束限制**： 列表元素数量取值范围为[1,100]个，每个元素字符串长度取值范围为[1,255]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :param client_ids: The client_ids of this CreateOIDCProviderReqBody.
        :type client_ids: list[str]
        """
        self._client_ids = client_ids

    @property
    def thumbprints(self):
        r"""Gets the thumbprints of this CreateOIDCProviderReqBody.

        **参数解释**： OIDC 身份提供商的服务器证书指纹列表，列表中的指纹是 X.509 证书的十六进制编码的 SHA-1 哈希值，它始终是一个 64 个字符的字符串。通常，此列表只包含一个指纹，然而 IAM 允许您为一个 OIDC 提供商设置最多五个指纹，这使得您可以对身份提供商的证书进行安全轮转。此参数是可选的，如果未包含此参数，IAM 将检索并使用 OIDC 身份提供商服务器证书的顶层中间证书颁发机构 (CA) 指纹。有关获取 OIDC 提供商指纹的更多信息，请参阅 IAM 用户指南中的**获取 OIDC 提供商的指纹**。  **约束限制**： 列表元素数量取值范围为[0,5]个，每个元素字符串长度为64。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :return: The thumbprints of this CreateOIDCProviderReqBody.
        :rtype: list[str]
        """
        return self._thumbprints

    @thumbprints.setter
    def thumbprints(self, thumbprints):
        r"""Sets the thumbprints of this CreateOIDCProviderReqBody.

        **参数解释**： OIDC 身份提供商的服务器证书指纹列表，列表中的指纹是 X.509 证书的十六进制编码的 SHA-1 哈希值，它始终是一个 64 个字符的字符串。通常，此列表只包含一个指纹，然而 IAM 允许您为一个 OIDC 提供商设置最多五个指纹，这使得您可以对身份提供商的证书进行安全轮转。此参数是可选的，如果未包含此参数，IAM 将检索并使用 OIDC 身份提供商服务器证书的顶层中间证书颁发机构 (CA) 指纹。有关获取 OIDC 提供商指纹的更多信息，请参阅 IAM 用户指南中的**获取 OIDC 提供商的指纹**。  **约束限制**： 列表元素数量取值范围为[0,5]个，每个元素字符串长度为64。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :param thumbprints: The thumbprints of this CreateOIDCProviderReqBody.
        :type thumbprints: list[str]
        """
        self._thumbprints = thumbprints

    @property
    def description(self):
        r"""Gets the description of this CreateOIDCProviderReqBody.

        **参数解释**： 身份提供商描述。  **约束限制**： 长度范围为[0,255]。  **取值范围**： 不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\"、\"$\"、\"^\"和\"*\"的字符串。  **默认取值**： 不涉及。

        :return: The description of this CreateOIDCProviderReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateOIDCProviderReqBody.

        **参数解释**： 身份提供商描述。  **约束限制**： 长度范围为[0,255]。  **取值范围**： 不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\"、\"$\"、\"^\"和\"*\"的字符串。  **默认取值**： 不涉及。

        :param description: The description of this CreateOIDCProviderReqBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateOIDCProviderReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
