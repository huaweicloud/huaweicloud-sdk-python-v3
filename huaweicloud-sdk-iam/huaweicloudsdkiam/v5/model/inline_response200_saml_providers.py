# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InlineResponse200SamlProviders:

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
        'urn': 'str',
        'saml_metadata_document': 'str',
        'assertion_encryption_mode': 'str',
        'private_keys': 'list[InlineResponse200PrivateKeys]',
        'created_at': 'datetime',
        'expires_at': 'datetime'
    }

    attribute_map = {
        'provider_id': 'provider_id',
        'name': 'name',
        'description': 'description',
        'urn': 'urn',
        'saml_metadata_document': 'saml_metadata_document',
        'assertion_encryption_mode': 'assertion_encryption_mode',
        'private_keys': 'private_keys',
        'created_at': 'created_at',
        'expires_at': 'expires_at'
    }

    def __init__(self, provider_id=None, name=None, description=None, urn=None, saml_metadata_document=None, assertion_encryption_mode=None, private_keys=None, created_at=None, expires_at=None):
        r"""InlineResponse200SamlProviders

        The model defined in huaweicloud sdk

        :param provider_id: **参数解释**： SAML 身份提供商的ID。  **取值范围**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、中划线（-）。
        :type provider_id: str
        :param name: **参数解释**： SAML 身份提供商的名称。  **取值范围**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、下划线（_）、中划线（-）。
        :type name: str
        :param description: **参数解释**： 身份提供商描述。  **取值范围**： 不能包含特定字符\&quot;@\&quot;、\&quot;#\&quot;、\&quot;%\&quot;、\&quot;&amp;\&quot;、\&quot;&lt;\&quot;、\&quot;&gt;\&quot;、\&quot;\\\&quot;、\&quot;$\&quot;、\&quot;^\&quot;和\&quot;*\&quot;的字符串。
        :type description: str
        :param urn: **参数解释**： 统一资源名称。  **取值范围**： 字符串长度在 16 到 1500 之间，可以包含：字母、数字、斜杠（/）、等号（&#x3D;）、下划线（_）、冒号（:）、中划线（-）
        :type urn: str
        :param saml_metadata_document: **参数解释**： 支持 SAML 2.0 的身份提供商 (IdP) 的 XML 文档。  **取值范围**： 长度范围为[1000,512000]。
        :type saml_metadata_document: str
        :param assertion_encryption_mode: **参数解释**： 指定 SAML 身份提供商的加密设置。  **取值范围**： 取值范围为[Required,Allowed]。
        :type assertion_encryption_mode: str
        :param private_keys: **参数解释**： 解密 SAML 断言的私钥。  **取值范围**： 不涉及。
        :type private_keys: list[:class:`huaweicloudsdkiam.v5.InlineResponse200PrivateKeys`]
        :param created_at: **参数解释**： SAML 身份提供商创建时间。  **取值范围**： 不涉及。
        :type created_at: datetime
        :param expires_at: **参数解释**： SAML 身份提供商过期时间。  **取值范围**： 不涉及。
        :type expires_at: datetime
        """
        
        

        self._provider_id = None
        self._name = None
        self._description = None
        self._urn = None
        self._saml_metadata_document = None
        self._assertion_encryption_mode = None
        self._private_keys = None
        self._created_at = None
        self._expires_at = None
        self.discriminator = None

        self.provider_id = provider_id
        self.name = name
        self.description = description
        self.urn = urn
        self.saml_metadata_document = saml_metadata_document
        self.assertion_encryption_mode = assertion_encryption_mode
        self.private_keys = private_keys
        self.created_at = created_at
        self.expires_at = expires_at

    @property
    def provider_id(self):
        r"""Gets the provider_id of this InlineResponse200SamlProviders.

        **参数解释**： SAML 身份提供商的ID。  **取值范围**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、中划线（-）。

        :return: The provider_id of this InlineResponse200SamlProviders.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this InlineResponse200SamlProviders.

        **参数解释**： SAML 身份提供商的ID。  **取值范围**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、中划线（-）。

        :param provider_id: The provider_id of this InlineResponse200SamlProviders.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def name(self):
        r"""Gets the name of this InlineResponse200SamlProviders.

        **参数解释**： SAML 身份提供商的名称。  **取值范围**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、下划线（_）、中划线（-）。

        :return: The name of this InlineResponse200SamlProviders.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InlineResponse200SamlProviders.

        **参数解释**： SAML 身份提供商的名称。  **取值范围**： 字符串长度在 1 到 64 之间，并且只能包含：字母、数字、下划线（_）、中划线（-）。

        :param name: The name of this InlineResponse200SamlProviders.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this InlineResponse200SamlProviders.

        **参数解释**： 身份提供商描述。  **取值范围**： 不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :return: The description of this InlineResponse200SamlProviders.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InlineResponse200SamlProviders.

        **参数解释**： 身份提供商描述。  **取值范围**： 不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :param description: The description of this InlineResponse200SamlProviders.
        :type description: str
        """
        self._description = description

    @property
    def urn(self):
        r"""Gets the urn of this InlineResponse200SamlProviders.

        **参数解释**： 统一资源名称。  **取值范围**： 字符串长度在 16 到 1500 之间，可以包含：字母、数字、斜杠（/）、等号（=）、下划线（_）、冒号（:）、中划线（-）

        :return: The urn of this InlineResponse200SamlProviders.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this InlineResponse200SamlProviders.

        **参数解释**： 统一资源名称。  **取值范围**： 字符串长度在 16 到 1500 之间，可以包含：字母、数字、斜杠（/）、等号（=）、下划线（_）、冒号（:）、中划线（-）

        :param urn: The urn of this InlineResponse200SamlProviders.
        :type urn: str
        """
        self._urn = urn

    @property
    def saml_metadata_document(self):
        r"""Gets the saml_metadata_document of this InlineResponse200SamlProviders.

        **参数解释**： 支持 SAML 2.0 的身份提供商 (IdP) 的 XML 文档。  **取值范围**： 长度范围为[1000,512000]。

        :return: The saml_metadata_document of this InlineResponse200SamlProviders.
        :rtype: str
        """
        return self._saml_metadata_document

    @saml_metadata_document.setter
    def saml_metadata_document(self, saml_metadata_document):
        r"""Sets the saml_metadata_document of this InlineResponse200SamlProviders.

        **参数解释**： 支持 SAML 2.0 的身份提供商 (IdP) 的 XML 文档。  **取值范围**： 长度范围为[1000,512000]。

        :param saml_metadata_document: The saml_metadata_document of this InlineResponse200SamlProviders.
        :type saml_metadata_document: str
        """
        self._saml_metadata_document = saml_metadata_document

    @property
    def assertion_encryption_mode(self):
        r"""Gets the assertion_encryption_mode of this InlineResponse200SamlProviders.

        **参数解释**： 指定 SAML 身份提供商的加密设置。  **取值范围**： 取值范围为[Required,Allowed]。

        :return: The assertion_encryption_mode of this InlineResponse200SamlProviders.
        :rtype: str
        """
        return self._assertion_encryption_mode

    @assertion_encryption_mode.setter
    def assertion_encryption_mode(self, assertion_encryption_mode):
        r"""Sets the assertion_encryption_mode of this InlineResponse200SamlProviders.

        **参数解释**： 指定 SAML 身份提供商的加密设置。  **取值范围**： 取值范围为[Required,Allowed]。

        :param assertion_encryption_mode: The assertion_encryption_mode of this InlineResponse200SamlProviders.
        :type assertion_encryption_mode: str
        """
        self._assertion_encryption_mode = assertion_encryption_mode

    @property
    def private_keys(self):
        r"""Gets the private_keys of this InlineResponse200SamlProviders.

        **参数解释**： 解密 SAML 断言的私钥。  **取值范围**： 不涉及。

        :return: The private_keys of this InlineResponse200SamlProviders.
        :rtype: list[:class:`huaweicloudsdkiam.v5.InlineResponse200PrivateKeys`]
        """
        return self._private_keys

    @private_keys.setter
    def private_keys(self, private_keys):
        r"""Sets the private_keys of this InlineResponse200SamlProviders.

        **参数解释**： 解密 SAML 断言的私钥。  **取值范围**： 不涉及。

        :param private_keys: The private_keys of this InlineResponse200SamlProviders.
        :type private_keys: list[:class:`huaweicloudsdkiam.v5.InlineResponse200PrivateKeys`]
        """
        self._private_keys = private_keys

    @property
    def created_at(self):
        r"""Gets the created_at of this InlineResponse200SamlProviders.

        **参数解释**： SAML 身份提供商创建时间。  **取值范围**： 不涉及。

        :return: The created_at of this InlineResponse200SamlProviders.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this InlineResponse200SamlProviders.

        **参数解释**： SAML 身份提供商创建时间。  **取值范围**： 不涉及。

        :param created_at: The created_at of this InlineResponse200SamlProviders.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def expires_at(self):
        r"""Gets the expires_at of this InlineResponse200SamlProviders.

        **参数解释**： SAML 身份提供商过期时间。  **取值范围**： 不涉及。

        :return: The expires_at of this InlineResponse200SamlProviders.
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this InlineResponse200SamlProviders.

        **参数解释**： SAML 身份提供商过期时间。  **取值范围**： 不涉及。

        :param expires_at: The expires_at of this InlineResponse200SamlProviders.
        :type expires_at: datetime
        """
        self._expires_at = expires_at

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
        if not isinstance(other, InlineResponse200SamlProviders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
