# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CredentialsDto:

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
        'expiration': 'datetime',
        'secret_access_key': 'str',
        'security_token': 'str'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'expiration': 'expiration',
        'secret_access_key': 'secret_access_key',
        'security_token': 'security_token'
    }

    def __init__(self, access_key_id=None, expiration=None, secret_access_key=None, security_token=None):
        r"""CredentialsDto

        The model defined in huaweicloud sdk

        :param access_key_id: 临时安全凭证的AK。
        :type access_key_id: str
        :param expiration: 临时安全凭证的失效时间。
        :type expiration: datetime
        :param secret_access_key: 临时安全凭证的SK。
        :type secret_access_key: str
        :param security_token: 临时安全凭证的security_token。
        :type security_token: str
        """
        
        

        self._access_key_id = None
        self._expiration = None
        self._secret_access_key = None
        self._security_token = None
        self.discriminator = None

        self.access_key_id = access_key_id
        self.expiration = expiration
        self.secret_access_key = secret_access_key
        self.security_token = security_token

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this CredentialsDto.

        临时安全凭证的AK。

        :return: The access_key_id of this CredentialsDto.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this CredentialsDto.

        临时安全凭证的AK。

        :param access_key_id: The access_key_id of this CredentialsDto.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

    @property
    def expiration(self):
        r"""Gets the expiration of this CredentialsDto.

        临时安全凭证的失效时间。

        :return: The expiration of this CredentialsDto.
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        r"""Sets the expiration of this CredentialsDto.

        临时安全凭证的失效时间。

        :param expiration: The expiration of this CredentialsDto.
        :type expiration: datetime
        """
        self._expiration = expiration

    @property
    def secret_access_key(self):
        r"""Gets the secret_access_key of this CredentialsDto.

        临时安全凭证的SK。

        :return: The secret_access_key of this CredentialsDto.
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        r"""Sets the secret_access_key of this CredentialsDto.

        临时安全凭证的SK。

        :param secret_access_key: The secret_access_key of this CredentialsDto.
        :type secret_access_key: str
        """
        self._secret_access_key = secret_access_key

    @property
    def security_token(self):
        r"""Gets the security_token of this CredentialsDto.

        临时安全凭证的security_token。

        :return: The security_token of this CredentialsDto.
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        r"""Sets the security_token of this CredentialsDto.

        临时安全凭证的security_token。

        :param security_token: The security_token of this CredentialsDto.
        :type security_token: str
        """
        self._security_token = security_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CredentialsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
