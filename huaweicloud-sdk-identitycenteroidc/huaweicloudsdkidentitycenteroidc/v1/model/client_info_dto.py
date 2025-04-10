# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClientInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorization_endpoint': 'str',
        'client_id': 'str',
        'client_id_issued_at': 'int',
        'client_secret': 'str',
        'client_secret_expires_at': 'int',
        'token_endpoint': 'str',
        'scopes': 'list[str]'
    }

    attribute_map = {
        'authorization_endpoint': 'authorization_endpoint',
        'client_id': 'client_id',
        'client_id_issued_at': 'client_id_issued_at',
        'client_secret': 'client_secret',
        'client_secret_expires_at': 'client_secret_expires_at',
        'token_endpoint': 'token_endpoint',
        'scopes': 'scopes'
    }

    def __init__(self, authorization_endpoint=None, client_id=None, client_id_issued_at=None, client_secret=None, client_secret_expires_at=None, token_endpoint=None, scopes=None):
        r"""ClientInfoDto

        The model defined in huaweicloud sdk

        :param authorization_endpoint: 客户端可以请求授权的端点
        :type authorization_endpoint: str
        :param client_id: 客户端应用唯一标识
        :type client_id: str
        :param client_id_issued_at: 客户端标识符和客户端密钥的注册时间
        :type client_id_issued_at: int
        :param client_secret: 为客户端生成的秘密字符串。客户端将使用此字符串在后续调用中获得服务的身份验证
        :type client_secret: str
        :param client_secret_expires_at: 客户端标识符和客户端密钥失效的时间
        :type client_secret_expires_at: int
        :param token_endpoint: 客户端可以在其中获取访问令牌的端点
        :type token_endpoint: str
        :param scopes: 服务器为客户端注册的作用域列表。后续授权访问令牌时，权限都应该限制在此作用域列表的子集范围内
        :type scopes: list[str]
        """
        
        

        self._authorization_endpoint = None
        self._client_id = None
        self._client_id_issued_at = None
        self._client_secret = None
        self._client_secret_expires_at = None
        self._token_endpoint = None
        self._scopes = None
        self.discriminator = None

        self.authorization_endpoint = authorization_endpoint
        self.client_id = client_id
        self.client_id_issued_at = client_id_issued_at
        self.client_secret = client_secret
        self.client_secret_expires_at = client_secret_expires_at
        self.token_endpoint = token_endpoint
        if scopes is not None:
            self.scopes = scopes

    @property
    def authorization_endpoint(self):
        r"""Gets the authorization_endpoint of this ClientInfoDto.

        客户端可以请求授权的端点

        :return: The authorization_endpoint of this ClientInfoDto.
        :rtype: str
        """
        return self._authorization_endpoint

    @authorization_endpoint.setter
    def authorization_endpoint(self, authorization_endpoint):
        r"""Sets the authorization_endpoint of this ClientInfoDto.

        客户端可以请求授权的端点

        :param authorization_endpoint: The authorization_endpoint of this ClientInfoDto.
        :type authorization_endpoint: str
        """
        self._authorization_endpoint = authorization_endpoint

    @property
    def client_id(self):
        r"""Gets the client_id of this ClientInfoDto.

        客户端应用唯一标识

        :return: The client_id of this ClientInfoDto.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this ClientInfoDto.

        客户端应用唯一标识

        :param client_id: The client_id of this ClientInfoDto.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def client_id_issued_at(self):
        r"""Gets the client_id_issued_at of this ClientInfoDto.

        客户端标识符和客户端密钥的注册时间

        :return: The client_id_issued_at of this ClientInfoDto.
        :rtype: int
        """
        return self._client_id_issued_at

    @client_id_issued_at.setter
    def client_id_issued_at(self, client_id_issued_at):
        r"""Sets the client_id_issued_at of this ClientInfoDto.

        客户端标识符和客户端密钥的注册时间

        :param client_id_issued_at: The client_id_issued_at of this ClientInfoDto.
        :type client_id_issued_at: int
        """
        self._client_id_issued_at = client_id_issued_at

    @property
    def client_secret(self):
        r"""Gets the client_secret of this ClientInfoDto.

        为客户端生成的秘密字符串。客户端将使用此字符串在后续调用中获得服务的身份验证

        :return: The client_secret of this ClientInfoDto.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        r"""Sets the client_secret of this ClientInfoDto.

        为客户端生成的秘密字符串。客户端将使用此字符串在后续调用中获得服务的身份验证

        :param client_secret: The client_secret of this ClientInfoDto.
        :type client_secret: str
        """
        self._client_secret = client_secret

    @property
    def client_secret_expires_at(self):
        r"""Gets the client_secret_expires_at of this ClientInfoDto.

        客户端标识符和客户端密钥失效的时间

        :return: The client_secret_expires_at of this ClientInfoDto.
        :rtype: int
        """
        return self._client_secret_expires_at

    @client_secret_expires_at.setter
    def client_secret_expires_at(self, client_secret_expires_at):
        r"""Sets the client_secret_expires_at of this ClientInfoDto.

        客户端标识符和客户端密钥失效的时间

        :param client_secret_expires_at: The client_secret_expires_at of this ClientInfoDto.
        :type client_secret_expires_at: int
        """
        self._client_secret_expires_at = client_secret_expires_at

    @property
    def token_endpoint(self):
        r"""Gets the token_endpoint of this ClientInfoDto.

        客户端可以在其中获取访问令牌的端点

        :return: The token_endpoint of this ClientInfoDto.
        :rtype: str
        """
        return self._token_endpoint

    @token_endpoint.setter
    def token_endpoint(self, token_endpoint):
        r"""Sets the token_endpoint of this ClientInfoDto.

        客户端可以在其中获取访问令牌的端点

        :param token_endpoint: The token_endpoint of this ClientInfoDto.
        :type token_endpoint: str
        """
        self._token_endpoint = token_endpoint

    @property
    def scopes(self):
        r"""Gets the scopes of this ClientInfoDto.

        服务器为客户端注册的作用域列表。后续授权访问令牌时，权限都应该限制在此作用域列表的子集范围内

        :return: The scopes of this ClientInfoDto.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        r"""Sets the scopes of this ClientInfoDto.

        服务器为客户端注册的作用域列表。后续授权访问令牌时，权限都应该限制在此作用域列表的子集范围内

        :param scopes: The scopes of this ClientInfoDto.
        :type scopes: list[str]
        """
        self._scopes = scopes

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
        if not isinstance(other, ClientInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
