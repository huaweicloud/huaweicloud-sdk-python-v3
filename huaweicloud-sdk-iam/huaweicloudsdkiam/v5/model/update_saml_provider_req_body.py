# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSAMLProviderReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'saml_metadata_document': 'str',
        'assertion_encryption_mode': 'str',
        'add_private_key': 'str',
        'remove_private_key': 'str',
        'description': 'str'
    }

    attribute_map = {
        'saml_metadata_document': 'saml_metadata_document',
        'assertion_encryption_mode': 'assertion_encryption_mode',
        'add_private_key': 'add_private_key',
        'remove_private_key': 'remove_private_key',
        'description': 'description'
    }

    def __init__(self, saml_metadata_document=None, assertion_encryption_mode=None, add_private_key=None, remove_private_key=None, description=None):
        r"""UpdateSAMLProviderReqBody

        The model defined in huaweicloud sdk

        :param saml_metadata_document: **参数解释**： 由支持 SAML 2.0 的身份提供商 (IdP) 生成的 XML 文档。该文档包含颁发者的名称、过期信息，以及可用于验证从 IdP 接收到的 SAML 身份验证响应（断言）的密钥。  **约束限制**： 长度范围为[1000,512000]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。
        :type saml_metadata_document: str
        :param assertion_encryption_mode: **参数解释**： 指定 SAML 提供商的加密设置。  **约束限制**： 不涉及。  **取值范围**： 取值范围为[Required,Allowed]。  **默认取值**： 不涉及。
        :type assertion_encryption_mode: str
        :param add_private_key: **参数解释**： 添加解密 SAML 断言的私钥，必须是一个 PEM 格式的 RSA 私钥。在接收到加密的 SAML 断言时，IAM 会基于 RSA-OAEP 算法使用该私钥解密得到用于加密 SAML 断言的对称密钥，然后再基于 AES-GCM 或 AES-CBC 加密算法使用对称密钥解密出 SAML 断言明文。  **约束限制**： 长度范围为[1,16384]。  **取值范围**： 字符串必须由 1 个或多个字符组成，这些字符可以是：空格、可见 ASCII 字符、Latin-1 扩展字符、Tab、换行、回车。  **默认取值**： 不涉及。
        :type add_private_key: str
        :param remove_private_key: **参数解释**： 解密 SAML 断言私钥的 ID。  **约束限制**： 长度范围为[22,64]。  **取值范围**： 字符串只能包含大写字母和数字。  **默认取值**： 不涉及。
        :type remove_private_key: str
        :param description: **参数解释**： 身份提供商描述。  **约束限制**： 长度范围为[0,255]。  **取值范围**： 不能包含特定字符\&quot;@\&quot;、\&quot;#\&quot;、\&quot;%\&quot;、\&quot;&amp;\&quot;、\&quot;&lt;\&quot;、\&quot;&gt;\&quot;、\&quot;\\\&quot;、\&quot;$\&quot;、\&quot;^\&quot;和\&quot;*\&quot;的字符串。  **默认取值**： 不涉及。
        :type description: str
        """
        
        

        self._saml_metadata_document = None
        self._assertion_encryption_mode = None
        self._add_private_key = None
        self._remove_private_key = None
        self._description = None
        self.discriminator = None

        if saml_metadata_document is not None:
            self.saml_metadata_document = saml_metadata_document
        if assertion_encryption_mode is not None:
            self.assertion_encryption_mode = assertion_encryption_mode
        if add_private_key is not None:
            self.add_private_key = add_private_key
        if remove_private_key is not None:
            self.remove_private_key = remove_private_key
        if description is not None:
            self.description = description

    @property
    def saml_metadata_document(self):
        r"""Gets the saml_metadata_document of this UpdateSAMLProviderReqBody.

        **参数解释**： 由支持 SAML 2.0 的身份提供商 (IdP) 生成的 XML 文档。该文档包含颁发者的名称、过期信息，以及可用于验证从 IdP 接收到的 SAML 身份验证响应（断言）的密钥。  **约束限制**： 长度范围为[1000,512000]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :return: The saml_metadata_document of this UpdateSAMLProviderReqBody.
        :rtype: str
        """
        return self._saml_metadata_document

    @saml_metadata_document.setter
    def saml_metadata_document(self, saml_metadata_document):
        r"""Sets the saml_metadata_document of this UpdateSAMLProviderReqBody.

        **参数解释**： 由支持 SAML 2.0 的身份提供商 (IdP) 生成的 XML 文档。该文档包含颁发者的名称、过期信息，以及可用于验证从 IdP 接收到的 SAML 身份验证响应（断言）的密钥。  **约束限制**： 长度范围为[1000,512000]。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :param saml_metadata_document: The saml_metadata_document of this UpdateSAMLProviderReqBody.
        :type saml_metadata_document: str
        """
        self._saml_metadata_document = saml_metadata_document

    @property
    def assertion_encryption_mode(self):
        r"""Gets the assertion_encryption_mode of this UpdateSAMLProviderReqBody.

        **参数解释**： 指定 SAML 提供商的加密设置。  **约束限制**： 不涉及。  **取值范围**： 取值范围为[Required,Allowed]。  **默认取值**： 不涉及。

        :return: The assertion_encryption_mode of this UpdateSAMLProviderReqBody.
        :rtype: str
        """
        return self._assertion_encryption_mode

    @assertion_encryption_mode.setter
    def assertion_encryption_mode(self, assertion_encryption_mode):
        r"""Sets the assertion_encryption_mode of this UpdateSAMLProviderReqBody.

        **参数解释**： 指定 SAML 提供商的加密设置。  **约束限制**： 不涉及。  **取值范围**： 取值范围为[Required,Allowed]。  **默认取值**： 不涉及。

        :param assertion_encryption_mode: The assertion_encryption_mode of this UpdateSAMLProviderReqBody.
        :type assertion_encryption_mode: str
        """
        self._assertion_encryption_mode = assertion_encryption_mode

    @property
    def add_private_key(self):
        r"""Gets the add_private_key of this UpdateSAMLProviderReqBody.

        **参数解释**： 添加解密 SAML 断言的私钥，必须是一个 PEM 格式的 RSA 私钥。在接收到加密的 SAML 断言时，IAM 会基于 RSA-OAEP 算法使用该私钥解密得到用于加密 SAML 断言的对称密钥，然后再基于 AES-GCM 或 AES-CBC 加密算法使用对称密钥解密出 SAML 断言明文。  **约束限制**： 长度范围为[1,16384]。  **取值范围**： 字符串必须由 1 个或多个字符组成，这些字符可以是：空格、可见 ASCII 字符、Latin-1 扩展字符、Tab、换行、回车。  **默认取值**： 不涉及。

        :return: The add_private_key of this UpdateSAMLProviderReqBody.
        :rtype: str
        """
        return self._add_private_key

    @add_private_key.setter
    def add_private_key(self, add_private_key):
        r"""Sets the add_private_key of this UpdateSAMLProviderReqBody.

        **参数解释**： 添加解密 SAML 断言的私钥，必须是一个 PEM 格式的 RSA 私钥。在接收到加密的 SAML 断言时，IAM 会基于 RSA-OAEP 算法使用该私钥解密得到用于加密 SAML 断言的对称密钥，然后再基于 AES-GCM 或 AES-CBC 加密算法使用对称密钥解密出 SAML 断言明文。  **约束限制**： 长度范围为[1,16384]。  **取值范围**： 字符串必须由 1 个或多个字符组成，这些字符可以是：空格、可见 ASCII 字符、Latin-1 扩展字符、Tab、换行、回车。  **默认取值**： 不涉及。

        :param add_private_key: The add_private_key of this UpdateSAMLProviderReqBody.
        :type add_private_key: str
        """
        self._add_private_key = add_private_key

    @property
    def remove_private_key(self):
        r"""Gets the remove_private_key of this UpdateSAMLProviderReqBody.

        **参数解释**： 解密 SAML 断言私钥的 ID。  **约束限制**： 长度范围为[22,64]。  **取值范围**： 字符串只能包含大写字母和数字。  **默认取值**： 不涉及。

        :return: The remove_private_key of this UpdateSAMLProviderReqBody.
        :rtype: str
        """
        return self._remove_private_key

    @remove_private_key.setter
    def remove_private_key(self, remove_private_key):
        r"""Sets the remove_private_key of this UpdateSAMLProviderReqBody.

        **参数解释**： 解密 SAML 断言私钥的 ID。  **约束限制**： 长度范围为[22,64]。  **取值范围**： 字符串只能包含大写字母和数字。  **默认取值**： 不涉及。

        :param remove_private_key: The remove_private_key of this UpdateSAMLProviderReqBody.
        :type remove_private_key: str
        """
        self._remove_private_key = remove_private_key

    @property
    def description(self):
        r"""Gets the description of this UpdateSAMLProviderReqBody.

        **参数解释**： 身份提供商描述。  **约束限制**： 长度范围为[0,255]。  **取值范围**： 不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\"、\"$\"、\"^\"和\"*\"的字符串。  **默认取值**： 不涉及。

        :return: The description of this UpdateSAMLProviderReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateSAMLProviderReqBody.

        **参数解释**： 身份提供商描述。  **约束限制**： 长度范围为[0,255]。  **取值范围**： 不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\"、\"$\"、\"^\"和\"*\"的字符串。  **默认取值**： 不涉及。

        :param description: The description of this UpdateSAMLProviderReqBody.
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
        if not isinstance(other, UpdateSAMLProviderReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
