# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceLtCredentialResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_token': 'str',
        'created_at': 'str',
        'expire_date': 'str',
        'token_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'auth_token': 'auth_token',
        'created_at': 'created_at',
        'expire_date': 'expire_date',
        'token_id': 'token_id',
        'user_id': 'user_id'
    }

    def __init__(self, auth_token=None, created_at=None, expire_date=None, token_id=None, user_id=None):
        r"""CreateInstanceLtCredentialResponse

        The model defined in huaweicloud sdk

        :param auth_token: 访问凭证密码
        :type auth_token: str
        :param created_at: 创建时间
        :type created_at: str
        :param expire_date: 过期时间
        :type expire_date: str
        :param token_id: 访问凭证ID
        :type token_id: str
        :param user_id: 访问凭证用户名
        :type user_id: str
        """
        
        super(CreateInstanceLtCredentialResponse, self).__init__()

        self._auth_token = None
        self._created_at = None
        self._expire_date = None
        self._token_id = None
        self._user_id = None
        self.discriminator = None

        if auth_token is not None:
            self.auth_token = auth_token
        if created_at is not None:
            self.created_at = created_at
        if expire_date is not None:
            self.expire_date = expire_date
        if token_id is not None:
            self.token_id = token_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def auth_token(self):
        r"""Gets the auth_token of this CreateInstanceLtCredentialResponse.

        访问凭证密码

        :return: The auth_token of this CreateInstanceLtCredentialResponse.
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        r"""Sets the auth_token of this CreateInstanceLtCredentialResponse.

        访问凭证密码

        :param auth_token: The auth_token of this CreateInstanceLtCredentialResponse.
        :type auth_token: str
        """
        self._auth_token = auth_token

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateInstanceLtCredentialResponse.

        创建时间

        :return: The created_at of this CreateInstanceLtCredentialResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateInstanceLtCredentialResponse.

        创建时间

        :param created_at: The created_at of this CreateInstanceLtCredentialResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def expire_date(self):
        r"""Gets the expire_date of this CreateInstanceLtCredentialResponse.

        过期时间

        :return: The expire_date of this CreateInstanceLtCredentialResponse.
        :rtype: str
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        r"""Sets the expire_date of this CreateInstanceLtCredentialResponse.

        过期时间

        :param expire_date: The expire_date of this CreateInstanceLtCredentialResponse.
        :type expire_date: str
        """
        self._expire_date = expire_date

    @property
    def token_id(self):
        r"""Gets the token_id of this CreateInstanceLtCredentialResponse.

        访问凭证ID

        :return: The token_id of this CreateInstanceLtCredentialResponse.
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        r"""Sets the token_id of this CreateInstanceLtCredentialResponse.

        访问凭证ID

        :param token_id: The token_id of this CreateInstanceLtCredentialResponse.
        :type token_id: str
        """
        self._token_id = token_id

    @property
    def user_id(self):
        r"""Gets the user_id of this CreateInstanceLtCredentialResponse.

        访问凭证用户名

        :return: The user_id of this CreateInstanceLtCredentialResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this CreateInstanceLtCredentialResponse.

        访问凭证用户名

        :param user_id: The user_id of this CreateInstanceLtCredentialResponse.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, CreateInstanceLtCredentialResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
