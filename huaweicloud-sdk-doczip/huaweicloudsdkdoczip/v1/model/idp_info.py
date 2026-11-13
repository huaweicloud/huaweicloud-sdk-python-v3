# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IDPInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'idp_type': 'str',
        'idp_issuer': 'str',
        'idp_signing_alg': 'str',
        'idp_audience': 'str',
        'public_keys': 'PublicUpdateInfo'
    }

    attribute_map = {
        'idp_type': 'idp_type',
        'idp_issuer': 'idp_issuer',
        'idp_signing_alg': 'idp_signing_alg',
        'idp_audience': 'idp_audience',
        'public_keys': 'public_keys'
    }

    def __init__(self, idp_type=None, idp_issuer=None, idp_signing_alg=None, idp_audience=None, public_keys=None):
        r"""IDPInfo

        The model defined in huaweicloud sdk

        :param idp_type: **参数解释**： 身份提供方类型。 **约束限制**： 不涉及。 **取值范围**： - oidc：OIDC签名。 - self_signed_jwt：自签。 **默认取值**： 不涉及。
        :type idp_type: str
        :param idp_issuer: **参数解释**： 身份提供方的 Issuer URL。 **约束限制**： 格式如：https://idp.example.com。 **取值范围**： [1-512]个字符。 **默认取值**： 不涉及。
        :type idp_issuer: str
        :param idp_signing_alg: **参数解释**： 签名算法。 **约束限制**： 不涉及。 **取值范围**： - RS256：RS256算法。 - ES256：ES256算法。 **默认取值**： 不涉及。
        :type idp_signing_alg: str
        :param idp_audience: **参数解释**： 预期的 Audience。 **约束限制**： 不涉及。 **取值范围**： [1-512]个字符。 **默认取值**： 不涉及。
        :type idp_audience: str
        :param public_keys: 
        :type public_keys: :class:`huaweicloudsdkdoczip.v1.PublicUpdateInfo`
        """
        
        

        self._idp_type = None
        self._idp_issuer = None
        self._idp_signing_alg = None
        self._idp_audience = None
        self._public_keys = None
        self.discriminator = None

        self.idp_type = idp_type
        if idp_issuer is not None:
            self.idp_issuer = idp_issuer
        if idp_signing_alg is not None:
            self.idp_signing_alg = idp_signing_alg
        if idp_audience is not None:
            self.idp_audience = idp_audience
        if public_keys is not None:
            self.public_keys = public_keys

    @property
    def idp_type(self):
        r"""Gets the idp_type of this IDPInfo.

        **参数解释**： 身份提供方类型。 **约束限制**： 不涉及。 **取值范围**： - oidc：OIDC签名。 - self_signed_jwt：自签。 **默认取值**： 不涉及。

        :return: The idp_type of this IDPInfo.
        :rtype: str
        """
        return self._idp_type

    @idp_type.setter
    def idp_type(self, idp_type):
        r"""Sets the idp_type of this IDPInfo.

        **参数解释**： 身份提供方类型。 **约束限制**： 不涉及。 **取值范围**： - oidc：OIDC签名。 - self_signed_jwt：自签。 **默认取值**： 不涉及。

        :param idp_type: The idp_type of this IDPInfo.
        :type idp_type: str
        """
        self._idp_type = idp_type

    @property
    def idp_issuer(self):
        r"""Gets the idp_issuer of this IDPInfo.

        **参数解释**： 身份提供方的 Issuer URL。 **约束限制**： 格式如：https://idp.example.com。 **取值范围**： [1-512]个字符。 **默认取值**： 不涉及。

        :return: The idp_issuer of this IDPInfo.
        :rtype: str
        """
        return self._idp_issuer

    @idp_issuer.setter
    def idp_issuer(self, idp_issuer):
        r"""Sets the idp_issuer of this IDPInfo.

        **参数解释**： 身份提供方的 Issuer URL。 **约束限制**： 格式如：https://idp.example.com。 **取值范围**： [1-512]个字符。 **默认取值**： 不涉及。

        :param idp_issuer: The idp_issuer of this IDPInfo.
        :type idp_issuer: str
        """
        self._idp_issuer = idp_issuer

    @property
    def idp_signing_alg(self):
        r"""Gets the idp_signing_alg of this IDPInfo.

        **参数解释**： 签名算法。 **约束限制**： 不涉及。 **取值范围**： - RS256：RS256算法。 - ES256：ES256算法。 **默认取值**： 不涉及。

        :return: The idp_signing_alg of this IDPInfo.
        :rtype: str
        """
        return self._idp_signing_alg

    @idp_signing_alg.setter
    def idp_signing_alg(self, idp_signing_alg):
        r"""Sets the idp_signing_alg of this IDPInfo.

        **参数解释**： 签名算法。 **约束限制**： 不涉及。 **取值范围**： - RS256：RS256算法。 - ES256：ES256算法。 **默认取值**： 不涉及。

        :param idp_signing_alg: The idp_signing_alg of this IDPInfo.
        :type idp_signing_alg: str
        """
        self._idp_signing_alg = idp_signing_alg

    @property
    def idp_audience(self):
        r"""Gets the idp_audience of this IDPInfo.

        **参数解释**： 预期的 Audience。 **约束限制**： 不涉及。 **取值范围**： [1-512]个字符。 **默认取值**： 不涉及。

        :return: The idp_audience of this IDPInfo.
        :rtype: str
        """
        return self._idp_audience

    @idp_audience.setter
    def idp_audience(self, idp_audience):
        r"""Sets the idp_audience of this IDPInfo.

        **参数解释**： 预期的 Audience。 **约束限制**： 不涉及。 **取值范围**： [1-512]个字符。 **默认取值**： 不涉及。

        :param idp_audience: The idp_audience of this IDPInfo.
        :type idp_audience: str
        """
        self._idp_audience = idp_audience

    @property
    def public_keys(self):
        r"""Gets the public_keys of this IDPInfo.

        :return: The public_keys of this IDPInfo.
        :rtype: :class:`huaweicloudsdkdoczip.v1.PublicUpdateInfo`
        """
        return self._public_keys

    @public_keys.setter
    def public_keys(self, public_keys):
        r"""Sets the public_keys of this IDPInfo.

        :param public_keys: The public_keys of this IDPInfo.
        :type public_keys: :class:`huaweicloudsdkdoczip.v1.PublicUpdateInfo`
        """
        self._public_keys = public_keys

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
        if not isinstance(other, IDPInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
