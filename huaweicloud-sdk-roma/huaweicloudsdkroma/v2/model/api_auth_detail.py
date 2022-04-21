# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiAuthDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'auth_method': 'str',
        'app_auth_type': 'str',
        'user_name': 'str',
        'password': 'str',
        'app_key': 'str',
        'app_secret': 'str',
        'secret': 'str',
        'alt_ip': 'str',
        'access_token_url': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'scope': 'str',
        'authorization': 'str',
        'grant_type': 'str'
    }

    attribute_map = {
        'auth_method': 'auth_method',
        'app_auth_type': 'app_auth_type',
        'user_name': 'user_name',
        'password': 'password',
        'app_key': 'app_key',
        'app_secret': 'app_secret',
        'secret': 'secret',
        'alt_ip': 'alt_ip',
        'access_token_url': 'access_token_url',
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'scope': 'scope',
        'authorization': 'authorization',
        'grant_type': 'grant_type'
    }

    def __init__(self, auth_method=None, app_auth_type=None, user_name=None, password=None, app_key=None, app_secret=None, secret=None, alt_ip=None, access_token_url=None, client_id=None, client_secret=None, scope=None, authorization=None, grant_type=None):
        """ApiAuthDetail

        The model defined in huaweicloud sdk

        :param auth_method: 访问API服务的认证方式 - none - basicauth - oauth2.0 - hmac - secret - md5 - apiGateway - keyTop - hikVision - huaweiNetworkManagement - liHe
        :type auth_method: str
        :param app_auth_type: 访问API服务的APP认证方式，认证方式为（apiGateway）时填写 - default - secret - jwt
        :type app_auth_type: str
        :param user_name: 访问API服务的用户名 - 认证方式为（lihe、huaweiNetworkManagement、basicauth）时填写
        :type user_name: str
        :param password: 访问API服务的密码 - 认证方式为（lihe、huaweiNetworkManagement、basicauth、secret、md5、hmac）时填写
        :type password: str
        :param app_key: 访问API服务的AppKey - 认证方式为（apiGateway、oauth2.0）时填写
        :type app_key: str
        :param app_secret: 访问API服务的AppSecret - 认证方式为（apiGateway、oauth2.0）时填写
        :type app_secret: str
        :param secret: 访问API服务的Secret - 认证方式为（KeyTop、HikVision、Secret、HMAC、MD5）时填写
        :type secret: str
        :param alt_ip: 访问API服务的备用IP - 认证方式为（HuaweiNetworkManagement）时填写
        :type alt_ip: str
        :param access_token_url: 访问API服务的AccessTokenUrl - 认证方式为（liHe、oauth2.0 huaweiNetworkManagement）时填写
        :type access_token_url: str
        :param client_id: 访问API服务的客户端标识 - 认证方式为Oauth2时填写
        :type client_id: str
        :param client_secret: 访问API服务的客户端密钥 - 认证方式为Oauth2时填写
        :type client_secret: str
        :param scope: 访问API服务的Scope - 认证方式为（LiHe、Oauth2）时填写
        :type scope: str
        :param authorization: 访问API服务的Authorization - 认证方式为（LiHe）时填写
        :type authorization: str
        :param grant_type: 访问API服务的授权类型 - 认证方式为（LiHe、Oauth2）时填写 - client_credentials （oauth2.0使用）
        :type grant_type: str
        """
        
        

        self._auth_method = None
        self._app_auth_type = None
        self._user_name = None
        self._password = None
        self._app_key = None
        self._app_secret = None
        self._secret = None
        self._alt_ip = None
        self._access_token_url = None
        self._client_id = None
        self._client_secret = None
        self._scope = None
        self._authorization = None
        self._grant_type = None
        self.discriminator = None

        if auth_method is not None:
            self.auth_method = auth_method
        if app_auth_type is not None:
            self.app_auth_type = app_auth_type
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password
        if app_key is not None:
            self.app_key = app_key
        if app_secret is not None:
            self.app_secret = app_secret
        if secret is not None:
            self.secret = secret
        if alt_ip is not None:
            self.alt_ip = alt_ip
        if access_token_url is not None:
            self.access_token_url = access_token_url
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if scope is not None:
            self.scope = scope
        if authorization is not None:
            self.authorization = authorization
        if grant_type is not None:
            self.grant_type = grant_type

    @property
    def auth_method(self):
        """Gets the auth_method of this ApiAuthDetail.

        访问API服务的认证方式 - none - basicauth - oauth2.0 - hmac - secret - md5 - apiGateway - keyTop - hikVision - huaweiNetworkManagement - liHe

        :return: The auth_method of this ApiAuthDetail.
        :rtype: str
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Sets the auth_method of this ApiAuthDetail.

        访问API服务的认证方式 - none - basicauth - oauth2.0 - hmac - secret - md5 - apiGateway - keyTop - hikVision - huaweiNetworkManagement - liHe

        :param auth_method: The auth_method of this ApiAuthDetail.
        :type auth_method: str
        """
        self._auth_method = auth_method

    @property
    def app_auth_type(self):
        """Gets the app_auth_type of this ApiAuthDetail.

        访问API服务的APP认证方式，认证方式为（apiGateway）时填写 - default - secret - jwt

        :return: The app_auth_type of this ApiAuthDetail.
        :rtype: str
        """
        return self._app_auth_type

    @app_auth_type.setter
    def app_auth_type(self, app_auth_type):
        """Sets the app_auth_type of this ApiAuthDetail.

        访问API服务的APP认证方式，认证方式为（apiGateway）时填写 - default - secret - jwt

        :param app_auth_type: The app_auth_type of this ApiAuthDetail.
        :type app_auth_type: str
        """
        self._app_auth_type = app_auth_type

    @property
    def user_name(self):
        """Gets the user_name of this ApiAuthDetail.

        访问API服务的用户名 - 认证方式为（lihe、huaweiNetworkManagement、basicauth）时填写

        :return: The user_name of this ApiAuthDetail.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ApiAuthDetail.

        访问API服务的用户名 - 认证方式为（lihe、huaweiNetworkManagement、basicauth）时填写

        :param user_name: The user_name of this ApiAuthDetail.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this ApiAuthDetail.

        访问API服务的密码 - 认证方式为（lihe、huaweiNetworkManagement、basicauth、secret、md5、hmac）时填写

        :return: The password of this ApiAuthDetail.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ApiAuthDetail.

        访问API服务的密码 - 认证方式为（lihe、huaweiNetworkManagement、basicauth、secret、md5、hmac）时填写

        :param password: The password of this ApiAuthDetail.
        :type password: str
        """
        self._password = password

    @property
    def app_key(self):
        """Gets the app_key of this ApiAuthDetail.

        访问API服务的AppKey - 认证方式为（apiGateway、oauth2.0）时填写

        :return: The app_key of this ApiAuthDetail.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this ApiAuthDetail.

        访问API服务的AppKey - 认证方式为（apiGateway、oauth2.0）时填写

        :param app_key: The app_key of this ApiAuthDetail.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def app_secret(self):
        """Gets the app_secret of this ApiAuthDetail.

        访问API服务的AppSecret - 认证方式为（apiGateway、oauth2.0）时填写

        :return: The app_secret of this ApiAuthDetail.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this ApiAuthDetail.

        访问API服务的AppSecret - 认证方式为（apiGateway、oauth2.0）时填写

        :param app_secret: The app_secret of this ApiAuthDetail.
        :type app_secret: str
        """
        self._app_secret = app_secret

    @property
    def secret(self):
        """Gets the secret of this ApiAuthDetail.

        访问API服务的Secret - 认证方式为（KeyTop、HikVision、Secret、HMAC、MD5）时填写

        :return: The secret of this ApiAuthDetail.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this ApiAuthDetail.

        访问API服务的Secret - 认证方式为（KeyTop、HikVision、Secret、HMAC、MD5）时填写

        :param secret: The secret of this ApiAuthDetail.
        :type secret: str
        """
        self._secret = secret

    @property
    def alt_ip(self):
        """Gets the alt_ip of this ApiAuthDetail.

        访问API服务的备用IP - 认证方式为（HuaweiNetworkManagement）时填写

        :return: The alt_ip of this ApiAuthDetail.
        :rtype: str
        """
        return self._alt_ip

    @alt_ip.setter
    def alt_ip(self, alt_ip):
        """Sets the alt_ip of this ApiAuthDetail.

        访问API服务的备用IP - 认证方式为（HuaweiNetworkManagement）时填写

        :param alt_ip: The alt_ip of this ApiAuthDetail.
        :type alt_ip: str
        """
        self._alt_ip = alt_ip

    @property
    def access_token_url(self):
        """Gets the access_token_url of this ApiAuthDetail.

        访问API服务的AccessTokenUrl - 认证方式为（liHe、oauth2.0 huaweiNetworkManagement）时填写

        :return: The access_token_url of this ApiAuthDetail.
        :rtype: str
        """
        return self._access_token_url

    @access_token_url.setter
    def access_token_url(self, access_token_url):
        """Sets the access_token_url of this ApiAuthDetail.

        访问API服务的AccessTokenUrl - 认证方式为（liHe、oauth2.0 huaweiNetworkManagement）时填写

        :param access_token_url: The access_token_url of this ApiAuthDetail.
        :type access_token_url: str
        """
        self._access_token_url = access_token_url

    @property
    def client_id(self):
        """Gets the client_id of this ApiAuthDetail.

        访问API服务的客户端标识 - 认证方式为Oauth2时填写

        :return: The client_id of this ApiAuthDetail.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ApiAuthDetail.

        访问API服务的客户端标识 - 认证方式为Oauth2时填写

        :param client_id: The client_id of this ApiAuthDetail.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this ApiAuthDetail.

        访问API服务的客户端密钥 - 认证方式为Oauth2时填写

        :return: The client_secret of this ApiAuthDetail.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this ApiAuthDetail.

        访问API服务的客户端密钥 - 认证方式为Oauth2时填写

        :param client_secret: The client_secret of this ApiAuthDetail.
        :type client_secret: str
        """
        self._client_secret = client_secret

    @property
    def scope(self):
        """Gets the scope of this ApiAuthDetail.

        访问API服务的Scope - 认证方式为（LiHe、Oauth2）时填写

        :return: The scope of this ApiAuthDetail.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ApiAuthDetail.

        访问API服务的Scope - 认证方式为（LiHe、Oauth2）时填写

        :param scope: The scope of this ApiAuthDetail.
        :type scope: str
        """
        self._scope = scope

    @property
    def authorization(self):
        """Gets the authorization of this ApiAuthDetail.

        访问API服务的Authorization - 认证方式为（LiHe）时填写

        :return: The authorization of this ApiAuthDetail.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ApiAuthDetail.

        访问API服务的Authorization - 认证方式为（LiHe）时填写

        :param authorization: The authorization of this ApiAuthDetail.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def grant_type(self):
        """Gets the grant_type of this ApiAuthDetail.

        访问API服务的授权类型 - 认证方式为（LiHe、Oauth2）时填写 - client_credentials （oauth2.0使用）

        :return: The grant_type of this ApiAuthDetail.
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """Sets the grant_type of this ApiAuthDetail.

        访问API服务的授权类型 - 认证方式为（LiHe、Oauth2）时填写 - client_credentials （oauth2.0使用）

        :param grant_type: The grant_type of this ApiAuthDetail.
        :type grant_type: str
        """
        self._grant_type = grant_type

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
        if not isinstance(other, ApiAuthDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
