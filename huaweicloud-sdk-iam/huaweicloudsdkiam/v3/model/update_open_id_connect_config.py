# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOpenIdConnectConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'access_mode': 'str',
        'idp_url': 'str',
        'client_id': 'str',
        'authorization_endpoint': 'str',
        'scope': 'str',
        'response_type': 'str',
        'response_mode': 'str',
        'signing_key': 'str'
    }

    attribute_map = {
        'access_mode': 'access_mode',
        'idp_url': 'idp_url',
        'client_id': 'client_id',
        'authorization_endpoint': 'authorization_endpoint',
        'scope': 'scope',
        'response_type': 'response_type',
        'response_mode': 'response_mode',
        'signing_key': 'signing_key'
    }

    def __init__(self, access_mode=None, idp_url=None, client_id=None, authorization_endpoint=None, scope=None, response_type=None, response_mode=None, signing_key=None):
        """UpdateOpenIdConnectConfig

        The model defined in huaweicloud sdk

        :param access_mode: 访问方式: program_console: 支持编程访问和管理控制台访问方式; program: 支持编程访问方式
        :type access_mode: str
        :param idp_url: OpenID Connect身份提供商标识，对应ID token 中 iss
        :type idp_url: str
        :param client_id: 在OpenID Connect身份提供商注册的客户端ID
        :type client_id: str
        :param authorization_endpoint: OpenID Connect身份提供商授权地址；编程访问和管理控制台访问方式值不可为空，编程访问方式值可为空
        :type authorization_endpoint: str
        :param scope: 授权请求信息范围，编程访问和管理控制台访问方式必选，编程访问方式不可选，可选值：openid 、email、profile，IDP自定义scope，字符集a-zA-Z_0-9 ，1-10个可选值组合空格分割，至少包括openid，顺序无关，总长度最长255字符，例如：\&quot;openid\&quot;、\&quot;openid email\&quot;、\&quot;openid profile\&quot; 、\&quot;openid email profile\&quot;
        :type scope: str
        :param response_type: 授权请求返回的类型；值为id_token ；编程访问和管理控制台访问方式值不可为空，编程访问方式值可为空 
        :type response_type: str
        :param response_mode: 授权请求返回方式，可选值 form_post 或 fragment ；编程访问和管理控制台访问方式值为可选值，编程访问方式值可为空
        :type response_mode: str
        :param signing_key: OpenID Connect身份提供商ID Token签名的公钥
        :type signing_key: str
        """
        
        

        self._access_mode = None
        self._idp_url = None
        self._client_id = None
        self._authorization_endpoint = None
        self._scope = None
        self._response_type = None
        self._response_mode = None
        self._signing_key = None
        self.discriminator = None

        if access_mode is not None:
            self.access_mode = access_mode
        if idp_url is not None:
            self.idp_url = idp_url
        if client_id is not None:
            self.client_id = client_id
        if authorization_endpoint is not None:
            self.authorization_endpoint = authorization_endpoint
        if scope is not None:
            self.scope = scope
        if response_type is not None:
            self.response_type = response_type
        if response_mode is not None:
            self.response_mode = response_mode
        if signing_key is not None:
            self.signing_key = signing_key

    @property
    def access_mode(self):
        """Gets the access_mode of this UpdateOpenIdConnectConfig.

        访问方式: program_console: 支持编程访问和管理控制台访问方式; program: 支持编程访问方式

        :return: The access_mode of this UpdateOpenIdConnectConfig.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this UpdateOpenIdConnectConfig.

        访问方式: program_console: 支持编程访问和管理控制台访问方式; program: 支持编程访问方式

        :param access_mode: The access_mode of this UpdateOpenIdConnectConfig.
        :type access_mode: str
        """
        self._access_mode = access_mode

    @property
    def idp_url(self):
        """Gets the idp_url of this UpdateOpenIdConnectConfig.

        OpenID Connect身份提供商标识，对应ID token 中 iss

        :return: The idp_url of this UpdateOpenIdConnectConfig.
        :rtype: str
        """
        return self._idp_url

    @idp_url.setter
    def idp_url(self, idp_url):
        """Sets the idp_url of this UpdateOpenIdConnectConfig.

        OpenID Connect身份提供商标识，对应ID token 中 iss

        :param idp_url: The idp_url of this UpdateOpenIdConnectConfig.
        :type idp_url: str
        """
        self._idp_url = idp_url

    @property
    def client_id(self):
        """Gets the client_id of this UpdateOpenIdConnectConfig.

        在OpenID Connect身份提供商注册的客户端ID

        :return: The client_id of this UpdateOpenIdConnectConfig.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this UpdateOpenIdConnectConfig.

        在OpenID Connect身份提供商注册的客户端ID

        :param client_id: The client_id of this UpdateOpenIdConnectConfig.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def authorization_endpoint(self):
        """Gets the authorization_endpoint of this UpdateOpenIdConnectConfig.

        OpenID Connect身份提供商授权地址；编程访问和管理控制台访问方式值不可为空，编程访问方式值可为空

        :return: The authorization_endpoint of this UpdateOpenIdConnectConfig.
        :rtype: str
        """
        return self._authorization_endpoint

    @authorization_endpoint.setter
    def authorization_endpoint(self, authorization_endpoint):
        """Sets the authorization_endpoint of this UpdateOpenIdConnectConfig.

        OpenID Connect身份提供商授权地址；编程访问和管理控制台访问方式值不可为空，编程访问方式值可为空

        :param authorization_endpoint: The authorization_endpoint of this UpdateOpenIdConnectConfig.
        :type authorization_endpoint: str
        """
        self._authorization_endpoint = authorization_endpoint

    @property
    def scope(self):
        """Gets the scope of this UpdateOpenIdConnectConfig.

        授权请求信息范围，编程访问和管理控制台访问方式必选，编程访问方式不可选，可选值：openid 、email、profile，IDP自定义scope，字符集a-zA-Z_0-9 ，1-10个可选值组合空格分割，至少包括openid，顺序无关，总长度最长255字符，例如：\"openid\"、\"openid email\"、\"openid profile\" 、\"openid email profile\"

        :return: The scope of this UpdateOpenIdConnectConfig.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this UpdateOpenIdConnectConfig.

        授权请求信息范围，编程访问和管理控制台访问方式必选，编程访问方式不可选，可选值：openid 、email、profile，IDP自定义scope，字符集a-zA-Z_0-9 ，1-10个可选值组合空格分割，至少包括openid，顺序无关，总长度最长255字符，例如：\"openid\"、\"openid email\"、\"openid profile\" 、\"openid email profile\"

        :param scope: The scope of this UpdateOpenIdConnectConfig.
        :type scope: str
        """
        self._scope = scope

    @property
    def response_type(self):
        """Gets the response_type of this UpdateOpenIdConnectConfig.

        授权请求返回的类型；值为id_token ；编程访问和管理控制台访问方式值不可为空，编程访问方式值可为空 

        :return: The response_type of this UpdateOpenIdConnectConfig.
        :rtype: str
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this UpdateOpenIdConnectConfig.

        授权请求返回的类型；值为id_token ；编程访问和管理控制台访问方式值不可为空，编程访问方式值可为空 

        :param response_type: The response_type of this UpdateOpenIdConnectConfig.
        :type response_type: str
        """
        self._response_type = response_type

    @property
    def response_mode(self):
        """Gets the response_mode of this UpdateOpenIdConnectConfig.

        授权请求返回方式，可选值 form_post 或 fragment ；编程访问和管理控制台访问方式值为可选值，编程访问方式值可为空

        :return: The response_mode of this UpdateOpenIdConnectConfig.
        :rtype: str
        """
        return self._response_mode

    @response_mode.setter
    def response_mode(self, response_mode):
        """Sets the response_mode of this UpdateOpenIdConnectConfig.

        授权请求返回方式，可选值 form_post 或 fragment ；编程访问和管理控制台访问方式值为可选值，编程访问方式值可为空

        :param response_mode: The response_mode of this UpdateOpenIdConnectConfig.
        :type response_mode: str
        """
        self._response_mode = response_mode

    @property
    def signing_key(self):
        """Gets the signing_key of this UpdateOpenIdConnectConfig.

        OpenID Connect身份提供商ID Token签名的公钥

        :return: The signing_key of this UpdateOpenIdConnectConfig.
        :rtype: str
        """
        return self._signing_key

    @signing_key.setter
    def signing_key(self, signing_key):
        """Sets the signing_key of this UpdateOpenIdConnectConfig.

        OpenID Connect身份提供商ID Token签名的公钥

        :param signing_key: The signing_key of this UpdateOpenIdConnectConfig.
        :type signing_key: str
        """
        self._signing_key = signing_key

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
        if not isinstance(other, UpdateOpenIdConnectConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
