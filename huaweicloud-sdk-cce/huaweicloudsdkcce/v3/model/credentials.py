# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Credentials:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key_id': 'str',
        'secret_access_key': 'str',
        'security_token': 'str',
        'expiration': 'str'
    }

    attribute_map = {
        'access_key_id': 'accessKeyId',
        'secret_access_key': 'secretAccessKey',
        'security_token': 'securityToken',
        'expiration': 'expiration'
    }

    def __init__(self, access_key_id=None, secret_access_key=None, security_token=None, expiration=None):
        r"""Credentials

        The model defined in huaweicloud sdk

        :param access_key_id: **参数解释**： 临时安全凭证的AK **约束限制**： 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type access_key_id: str
        :param secret_access_key: **参数解释：** 临时安全凭证的SK **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type secret_access_key: str
        :param security_token: **参数解释**： 临时安全凭证的security_token **约束限制**： 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type security_token: str
        :param expiration: **参数解释：** 临时安全凭证的失效时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type expiration: str
        """
        
        

        self._access_key_id = None
        self._secret_access_key = None
        self._security_token = None
        self._expiration = None
        self.discriminator = None

        if access_key_id is not None:
            self.access_key_id = access_key_id
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key
        if security_token is not None:
            self.security_token = security_token
        if expiration is not None:
            self.expiration = expiration

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this Credentials.

        **参数解释**： 临时安全凭证的AK **约束限制**： 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The access_key_id of this Credentials.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this Credentials.

        **参数解释**： 临时安全凭证的AK **约束限制**： 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param access_key_id: The access_key_id of this Credentials.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

    @property
    def secret_access_key(self):
        r"""Gets the secret_access_key of this Credentials.

        **参数解释：** 临时安全凭证的SK **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The secret_access_key of this Credentials.
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        r"""Sets the secret_access_key of this Credentials.

        **参数解释：** 临时安全凭证的SK **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param secret_access_key: The secret_access_key of this Credentials.
        :type secret_access_key: str
        """
        self._secret_access_key = secret_access_key

    @property
    def security_token(self):
        r"""Gets the security_token of this Credentials.

        **参数解释**： 临时安全凭证的security_token **约束限制**： 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The security_token of this Credentials.
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        r"""Sets the security_token of this Credentials.

        **参数解释**： 临时安全凭证的security_token **约束限制**： 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param security_token: The security_token of this Credentials.
        :type security_token: str
        """
        self._security_token = security_token

    @property
    def expiration(self):
        r"""Gets the expiration of this Credentials.

        **参数解释：** 临时安全凭证的失效时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The expiration of this Credentials.
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        r"""Sets the expiration of this Credentials.

        **参数解释：** 临时安全凭证的失效时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param expiration: The expiration of this Credentials.
        :type expiration: str
        """
        self._expiration = expiration

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
        if not isinstance(other, Credentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
