# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InlineResponse2002OidcProviders:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_id': 'str',
        'name': 'str',
        'description': 'str',
        'url': 'str',
        'urn': 'str',
        'client_ids': 'list[str]',
        'thumbprints': 'list[str]',
        'created_at': 'datetime'
    }

    attribute_map = {
        'provider_id': 'provider_id',
        'name': 'name',
        'description': 'description',
        'url': 'url',
        'urn': 'urn',
        'client_ids': 'client_ids',
        'thumbprints': 'thumbprints',
        'created_at': 'created_at'
    }

    def __init__(self, provider_id=None, name=None, description=None, url=None, urn=None, client_ids=None, thumbprints=None, created_at=None):
        r"""InlineResponse2002OidcProviders

        The model defined in huaweicloud sdk

        :param provider_id: **参数解释**： OIDC 身份提供商的 ID。  **取值范围**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、中划线（-）。
        :type provider_id: str
        :param name: **参数解释**： OIDC 身份提供商的名称。  **取值范围**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、下划线（_）、中划线（-）。
        :type name: str
        :param description: **参数解释**： 身份提供商描述。  **取值范围**： 字符串长度不超过 255，并且不能包含特定字符\&quot;@\&quot;、\&quot;#\&quot;、\&quot;%\&quot;、\&quot;&amp;\&quot;、\&quot;&lt;\&quot;、\&quot;&gt;\&quot;、\&quot;\\\&quot;、\&quot;$\&quot;、\&quot;^\&quot;和\&quot;*\&quot;。
        :type description: str
        :param url: **参数解释**： OIDC 身份提供商的 URL。  **取值范围**： 字符串长度在 1 到 255 之间。
        :type url: str
        :param urn: **参数解释**： 统一资源名称。  **取值范围**： 字符串长度在 16 到 1500 之间，并且只能包含：字母、数字、字符\&quot;/\&quot;、\&quot;&#x3D;\&quot;、\&quot;_\&quot;、\&quot;:\&quot;、\&quot;-\&quot;。
        :type urn: str
        :param client_ids: **参数解释**： 客户端 ID 列表。  **取值范围**： 数组长度在 1 到 100 之间；数组元素为字符串，长度在 1 到 255 之间。
        :type client_ids: list[str]
        :param thumbprints: **参数解释**： OIDC 身份提供商的服务器证书指纹列表。  **取值范围**： 数组长度在 1 到 5 之间；数组元素为长度为 64 的字符串，并且只能包含字母、数字。
        :type thumbprints: list[str]
        :param created_at: **参数解释**： 提供商创建时间。  **取值范围**： 不涉及。
        :type created_at: datetime
        """
        
        

        self._provider_id = None
        self._name = None
        self._description = None
        self._url = None
        self._urn = None
        self._client_ids = None
        self._thumbprints = None
        self._created_at = None
        self.discriminator = None

        self.provider_id = provider_id
        self.name = name
        self.description = description
        self.url = url
        self.urn = urn
        self.client_ids = client_ids
        self.thumbprints = thumbprints
        self.created_at = created_at

    @property
    def provider_id(self):
        r"""Gets the provider_id of this InlineResponse2002OidcProviders.

        **参数解释**： OIDC 身份提供商的 ID。  **取值范围**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、中划线（-）。

        :return: The provider_id of this InlineResponse2002OidcProviders.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this InlineResponse2002OidcProviders.

        **参数解释**： OIDC 身份提供商的 ID。  **取值范围**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、中划线（-）。

        :param provider_id: The provider_id of this InlineResponse2002OidcProviders.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def name(self):
        r"""Gets the name of this InlineResponse2002OidcProviders.

        **参数解释**： OIDC 身份提供商的名称。  **取值范围**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、下划线（_）、中划线（-）。

        :return: The name of this InlineResponse2002OidcProviders.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InlineResponse2002OidcProviders.

        **参数解释**： OIDC 身份提供商的名称。  **取值范围**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、下划线（_）、中划线（-）。

        :param name: The name of this InlineResponse2002OidcProviders.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this InlineResponse2002OidcProviders.

        **参数解释**： 身份提供商描述。  **取值范围**： 字符串长度不超过 255，并且不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\"、\"$\"、\"^\"和\"*\"。

        :return: The description of this InlineResponse2002OidcProviders.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InlineResponse2002OidcProviders.

        **参数解释**： 身份提供商描述。  **取值范围**： 字符串长度不超过 255，并且不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\"、\"$\"、\"^\"和\"*\"。

        :param description: The description of this InlineResponse2002OidcProviders.
        :type description: str
        """
        self._description = description

    @property
    def url(self):
        r"""Gets the url of this InlineResponse2002OidcProviders.

        **参数解释**： OIDC 身份提供商的 URL。  **取值范围**： 字符串长度在 1 到 255 之间。

        :return: The url of this InlineResponse2002OidcProviders.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this InlineResponse2002OidcProviders.

        **参数解释**： OIDC 身份提供商的 URL。  **取值范围**： 字符串长度在 1 到 255 之间。

        :param url: The url of this InlineResponse2002OidcProviders.
        :type url: str
        """
        self._url = url

    @property
    def urn(self):
        r"""Gets the urn of this InlineResponse2002OidcProviders.

        **参数解释**： 统一资源名称。  **取值范围**： 字符串长度在 16 到 1500 之间，并且只能包含：字母、数字、字符\"/\"、\"=\"、\"_\"、\":\"、\"-\"。

        :return: The urn of this InlineResponse2002OidcProviders.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this InlineResponse2002OidcProviders.

        **参数解释**： 统一资源名称。  **取值范围**： 字符串长度在 16 到 1500 之间，并且只能包含：字母、数字、字符\"/\"、\"=\"、\"_\"、\":\"、\"-\"。

        :param urn: The urn of this InlineResponse2002OidcProviders.
        :type urn: str
        """
        self._urn = urn

    @property
    def client_ids(self):
        r"""Gets the client_ids of this InlineResponse2002OidcProviders.

        **参数解释**： 客户端 ID 列表。  **取值范围**： 数组长度在 1 到 100 之间；数组元素为字符串，长度在 1 到 255 之间。

        :return: The client_ids of this InlineResponse2002OidcProviders.
        :rtype: list[str]
        """
        return self._client_ids

    @client_ids.setter
    def client_ids(self, client_ids):
        r"""Sets the client_ids of this InlineResponse2002OidcProviders.

        **参数解释**： 客户端 ID 列表。  **取值范围**： 数组长度在 1 到 100 之间；数组元素为字符串，长度在 1 到 255 之间。

        :param client_ids: The client_ids of this InlineResponse2002OidcProviders.
        :type client_ids: list[str]
        """
        self._client_ids = client_ids

    @property
    def thumbprints(self):
        r"""Gets the thumbprints of this InlineResponse2002OidcProviders.

        **参数解释**： OIDC 身份提供商的服务器证书指纹列表。  **取值范围**： 数组长度在 1 到 5 之间；数组元素为长度为 64 的字符串，并且只能包含字母、数字。

        :return: The thumbprints of this InlineResponse2002OidcProviders.
        :rtype: list[str]
        """
        return self._thumbprints

    @thumbprints.setter
    def thumbprints(self, thumbprints):
        r"""Sets the thumbprints of this InlineResponse2002OidcProviders.

        **参数解释**： OIDC 身份提供商的服务器证书指纹列表。  **取值范围**： 数组长度在 1 到 5 之间；数组元素为长度为 64 的字符串，并且只能包含字母、数字。

        :param thumbprints: The thumbprints of this InlineResponse2002OidcProviders.
        :type thumbprints: list[str]
        """
        self._thumbprints = thumbprints

    @property
    def created_at(self):
        r"""Gets the created_at of this InlineResponse2002OidcProviders.

        **参数解释**： 提供商创建时间。  **取值范围**： 不涉及。

        :return: The created_at of this InlineResponse2002OidcProviders.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this InlineResponse2002OidcProviders.

        **参数解释**： 提供商创建时间。  **取值范围**： 不涉及。

        :param created_at: The created_at of this InlineResponse2002OidcProviders.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, InlineResponse2002OidcProviders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
