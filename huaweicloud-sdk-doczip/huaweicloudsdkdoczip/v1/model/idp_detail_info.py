# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IDPDetailInfo:

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
        'public_keys': 'list[PublicInfo]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'idp_type': 'idp_type',
        'idp_issuer': 'idp_issuer',
        'idp_signing_alg': 'idp_signing_alg',
        'idp_audience': 'idp_audience',
        'public_keys': 'public_keys',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, idp_type=None, idp_issuer=None, idp_signing_alg=None, idp_audience=None, public_keys=None, created_at=None, updated_at=None):
        r"""IDPDetailInfo

        The model defined in huaweicloud sdk

        :param idp_type: **参数解释**： 身份提供方类型。 **约束限制**： 不涉及。 **取值范围**： - oidc：OIDC签名。 - self_signed_jwt：自签。 **默认取值**： 不涉及。
        :type idp_type: str
        :param idp_issuer: **参数解释**： 身份提供方的 Issuer URL。 **约束限制**： 格式如：https://idp.example.com。 **取值范围**： [1-512]个字符。 **默认取值**： 不涉及。
        :type idp_issuer: str
        :param idp_signing_alg: **参数解释**： 签名算法。 **约束限制**： 不涉及。 **取值范围**： - RS256：RS256算法。 - ES256：ES256算法。 **默认取值**： 不涉及。
        :type idp_signing_alg: str
        :param idp_audience: **参数解释**： 预期的 Audience。 **约束限制**： 不涉及。 **取值范围**： [1-512]个字符。 **默认取值**： 不涉及。
        :type idp_audience: str
        :param public_keys: **参数解释**： 身份提供方公钥。 **取值范围**： 不涉及。
        :type public_keys: list[:class:`huaweicloudsdkdoczip.v1.PublicInfo`]
        :param created_at: **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。
        :type created_at: datetime
        :param updated_at: **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。
        :type updated_at: datetime
        """
        
        

        self._idp_type = None
        self._idp_issuer = None
        self._idp_signing_alg = None
        self._idp_audience = None
        self._public_keys = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if idp_type is not None:
            self.idp_type = idp_type
        if idp_issuer is not None:
            self.idp_issuer = idp_issuer
        if idp_signing_alg is not None:
            self.idp_signing_alg = idp_signing_alg
        if idp_audience is not None:
            self.idp_audience = idp_audience
        if public_keys is not None:
            self.public_keys = public_keys
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def idp_type(self):
        r"""Gets the idp_type of this IDPDetailInfo.

        **参数解释**： 身份提供方类型。 **约束限制**： 不涉及。 **取值范围**： - oidc：OIDC签名。 - self_signed_jwt：自签。 **默认取值**： 不涉及。

        :return: The idp_type of this IDPDetailInfo.
        :rtype: str
        """
        return self._idp_type

    @idp_type.setter
    def idp_type(self, idp_type):
        r"""Sets the idp_type of this IDPDetailInfo.

        **参数解释**： 身份提供方类型。 **约束限制**： 不涉及。 **取值范围**： - oidc：OIDC签名。 - self_signed_jwt：自签。 **默认取值**： 不涉及。

        :param idp_type: The idp_type of this IDPDetailInfo.
        :type idp_type: str
        """
        self._idp_type = idp_type

    @property
    def idp_issuer(self):
        r"""Gets the idp_issuer of this IDPDetailInfo.

        **参数解释**： 身份提供方的 Issuer URL。 **约束限制**： 格式如：https://idp.example.com。 **取值范围**： [1-512]个字符。 **默认取值**： 不涉及。

        :return: The idp_issuer of this IDPDetailInfo.
        :rtype: str
        """
        return self._idp_issuer

    @idp_issuer.setter
    def idp_issuer(self, idp_issuer):
        r"""Sets the idp_issuer of this IDPDetailInfo.

        **参数解释**： 身份提供方的 Issuer URL。 **约束限制**： 格式如：https://idp.example.com。 **取值范围**： [1-512]个字符。 **默认取值**： 不涉及。

        :param idp_issuer: The idp_issuer of this IDPDetailInfo.
        :type idp_issuer: str
        """
        self._idp_issuer = idp_issuer

    @property
    def idp_signing_alg(self):
        r"""Gets the idp_signing_alg of this IDPDetailInfo.

        **参数解释**： 签名算法。 **约束限制**： 不涉及。 **取值范围**： - RS256：RS256算法。 - ES256：ES256算法。 **默认取值**： 不涉及。

        :return: The idp_signing_alg of this IDPDetailInfo.
        :rtype: str
        """
        return self._idp_signing_alg

    @idp_signing_alg.setter
    def idp_signing_alg(self, idp_signing_alg):
        r"""Sets the idp_signing_alg of this IDPDetailInfo.

        **参数解释**： 签名算法。 **约束限制**： 不涉及。 **取值范围**： - RS256：RS256算法。 - ES256：ES256算法。 **默认取值**： 不涉及。

        :param idp_signing_alg: The idp_signing_alg of this IDPDetailInfo.
        :type idp_signing_alg: str
        """
        self._idp_signing_alg = idp_signing_alg

    @property
    def idp_audience(self):
        r"""Gets the idp_audience of this IDPDetailInfo.

        **参数解释**： 预期的 Audience。 **约束限制**： 不涉及。 **取值范围**： [1-512]个字符。 **默认取值**： 不涉及。

        :return: The idp_audience of this IDPDetailInfo.
        :rtype: str
        """
        return self._idp_audience

    @idp_audience.setter
    def idp_audience(self, idp_audience):
        r"""Sets the idp_audience of this IDPDetailInfo.

        **参数解释**： 预期的 Audience。 **约束限制**： 不涉及。 **取值范围**： [1-512]个字符。 **默认取值**： 不涉及。

        :param idp_audience: The idp_audience of this IDPDetailInfo.
        :type idp_audience: str
        """
        self._idp_audience = idp_audience

    @property
    def public_keys(self):
        r"""Gets the public_keys of this IDPDetailInfo.

        **参数解释**： 身份提供方公钥。 **取值范围**： 不涉及。

        :return: The public_keys of this IDPDetailInfo.
        :rtype: list[:class:`huaweicloudsdkdoczip.v1.PublicInfo`]
        """
        return self._public_keys

    @public_keys.setter
    def public_keys(self, public_keys):
        r"""Sets the public_keys of this IDPDetailInfo.

        **参数解释**： 身份提供方公钥。 **取值范围**： 不涉及。

        :param public_keys: The public_keys of this IDPDetailInfo.
        :type public_keys: list[:class:`huaweicloudsdkdoczip.v1.PublicInfo`]
        """
        self._public_keys = public_keys

    @property
    def created_at(self):
        r"""Gets the created_at of this IDPDetailInfo.

        **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。

        :return: The created_at of this IDPDetailInfo.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this IDPDetailInfo.

        **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。

        :param created_at: The created_at of this IDPDetailInfo.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this IDPDetailInfo.

        **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。

        :return: The updated_at of this IDPDetailInfo.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this IDPDetailInfo.

        **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。

        :param updated_at: The updated_at of this IDPDetailInfo.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, IDPDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
