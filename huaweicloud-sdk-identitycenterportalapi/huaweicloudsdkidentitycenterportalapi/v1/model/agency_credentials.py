# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyCredentials:

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
        'expiration': 'int',
        'secret_access_key': 'str',
        'session_token': 'str'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'expiration': 'expiration',
        'secret_access_key': 'secret_access_key',
        'session_token': 'session_token'
    }

    def __init__(self, access_key_id=None, expiration=None, secret_access_key=None, session_token=None):
        r"""AgencyCredentials

        The model defined in huaweicloud sdk

        :param access_key_id: 用于临时安全凭证的标识符
        :type access_key_id: str
        :param expiration: 临时安全凭证到期的日期
        :type expiration: int
        :param secret_access_key: 用于对请求进行签名的密钥
        :type secret_access_key: str
        :param session_token: 用于临时凭证的令牌
        :type session_token: str
        """
        
        

        self._access_key_id = None
        self._expiration = None
        self._secret_access_key = None
        self._session_token = None
        self.discriminator = None

        if access_key_id is not None:
            self.access_key_id = access_key_id
        if expiration is not None:
            self.expiration = expiration
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key
        if session_token is not None:
            self.session_token = session_token

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this AgencyCredentials.

        用于临时安全凭证的标识符

        :return: The access_key_id of this AgencyCredentials.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this AgencyCredentials.

        用于临时安全凭证的标识符

        :param access_key_id: The access_key_id of this AgencyCredentials.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

    @property
    def expiration(self):
        r"""Gets the expiration of this AgencyCredentials.

        临时安全凭证到期的日期

        :return: The expiration of this AgencyCredentials.
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        r"""Sets the expiration of this AgencyCredentials.

        临时安全凭证到期的日期

        :param expiration: The expiration of this AgencyCredentials.
        :type expiration: int
        """
        self._expiration = expiration

    @property
    def secret_access_key(self):
        r"""Gets the secret_access_key of this AgencyCredentials.

        用于对请求进行签名的密钥

        :return: The secret_access_key of this AgencyCredentials.
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        r"""Sets the secret_access_key of this AgencyCredentials.

        用于对请求进行签名的密钥

        :param secret_access_key: The secret_access_key of this AgencyCredentials.
        :type secret_access_key: str
        """
        self._secret_access_key = secret_access_key

    @property
    def session_token(self):
        r"""Gets the session_token of this AgencyCredentials.

        用于临时凭证的令牌

        :return: The session_token of this AgencyCredentials.
        :rtype: str
        """
        return self._session_token

    @session_token.setter
    def session_token(self, session_token):
        r"""Sets the session_token of this AgencyCredentials.

        用于临时凭证的令牌

        :param session_token: The session_token of this AgencyCredentials.
        :type session_token: str
        """
        self._session_token = session_token

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
        if not isinstance(other, AgencyCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
