# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTokenReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('client_secret')
    sensitive_list.append('code')
    sensitive_list.append('refresh_token')

    openapi_types = {
        'client_id': 'str',
        'client_secret': 'str',
        'code': 'str',
        'device_code': 'str',
        'grant_type': 'str',
        'redirect_uri': 'str',
        'refresh_token': 'str',
        'scopes': 'list[str]'
    }

    attribute_map = {
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'code': 'code',
        'device_code': 'device_code',
        'grant_type': 'grant_type',
        'redirect_uri': 'redirect_uri',
        'refresh_token': 'refresh_token',
        'scopes': 'scopes'
    }

    def __init__(self, client_id=None, client_secret=None, code=None, device_code=None, grant_type=None, redirect_uri=None, refresh_token=None, scopes=None):
        r"""CreateTokenReqBody

        The model defined in huaweicloud sdk

        :param client_id: 客户端的唯一标识
        :type client_id: str
        :param client_secret: 为客户端生成的秘密字符串。客户端将使用此字符串在后续调用中获得服务的身份验证
        :type client_secret: str
        :param code: 从授权服务接收的授权代码。执行授权授予请求以获取对令牌的访问权限时需要此参数
        :type code: str
        :param device_code: 仅在为设备代码授权类型调用此API时使用
        :type device_code: str
        :param grant_type: 请求的授权类型。支持授权码、设备代码、客户端凭证和刷新令牌等授权类型
        :type grant_type: str
        :param redirect_uri: 将接收授权代码的应用程序的位置。用户授权服务将请求发送到此位置
        :type redirect_uri: str
        :param refresh_token: 刷新令牌，此令牌可在访问令牌过期后获取新的访问令牌
        :type refresh_token: str
        :param scopes: 客户端定义的作用域列表，表示客户端想要获取的权限。授权后，此列表用于在授予访问令牌时限制权限
        :type scopes: list[str]
        """
        
        

        self._client_id = None
        self._client_secret = None
        self._code = None
        self._device_code = None
        self._grant_type = None
        self._redirect_uri = None
        self._refresh_token = None
        self._scopes = None
        self.discriminator = None

        self.client_id = client_id
        self.client_secret = client_secret
        if code is not None:
            self.code = code
        if device_code is not None:
            self.device_code = device_code
        self.grant_type = grant_type
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if scopes is not None:
            self.scopes = scopes

    @property
    def client_id(self):
        r"""Gets the client_id of this CreateTokenReqBody.

        客户端的唯一标识

        :return: The client_id of this CreateTokenReqBody.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this CreateTokenReqBody.

        客户端的唯一标识

        :param client_id: The client_id of this CreateTokenReqBody.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        r"""Gets the client_secret of this CreateTokenReqBody.

        为客户端生成的秘密字符串。客户端将使用此字符串在后续调用中获得服务的身份验证

        :return: The client_secret of this CreateTokenReqBody.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        r"""Sets the client_secret of this CreateTokenReqBody.

        为客户端生成的秘密字符串。客户端将使用此字符串在后续调用中获得服务的身份验证

        :param client_secret: The client_secret of this CreateTokenReqBody.
        :type client_secret: str
        """
        self._client_secret = client_secret

    @property
    def code(self):
        r"""Gets the code of this CreateTokenReqBody.

        从授权服务接收的授权代码。执行授权授予请求以获取对令牌的访问权限时需要此参数

        :return: The code of this CreateTokenReqBody.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this CreateTokenReqBody.

        从授权服务接收的授权代码。执行授权授予请求以获取对令牌的访问权限时需要此参数

        :param code: The code of this CreateTokenReqBody.
        :type code: str
        """
        self._code = code

    @property
    def device_code(self):
        r"""Gets the device_code of this CreateTokenReqBody.

        仅在为设备代码授权类型调用此API时使用

        :return: The device_code of this CreateTokenReqBody.
        :rtype: str
        """
        return self._device_code

    @device_code.setter
    def device_code(self, device_code):
        r"""Sets the device_code of this CreateTokenReqBody.

        仅在为设备代码授权类型调用此API时使用

        :param device_code: The device_code of this CreateTokenReqBody.
        :type device_code: str
        """
        self._device_code = device_code

    @property
    def grant_type(self):
        r"""Gets the grant_type of this CreateTokenReqBody.

        请求的授权类型。支持授权码、设备代码、客户端凭证和刷新令牌等授权类型

        :return: The grant_type of this CreateTokenReqBody.
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        r"""Sets the grant_type of this CreateTokenReqBody.

        请求的授权类型。支持授权码、设备代码、客户端凭证和刷新令牌等授权类型

        :param grant_type: The grant_type of this CreateTokenReqBody.
        :type grant_type: str
        """
        self._grant_type = grant_type

    @property
    def redirect_uri(self):
        r"""Gets the redirect_uri of this CreateTokenReqBody.

        将接收授权代码的应用程序的位置。用户授权服务将请求发送到此位置

        :return: The redirect_uri of this CreateTokenReqBody.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        r"""Sets the redirect_uri of this CreateTokenReqBody.

        将接收授权代码的应用程序的位置。用户授权服务将请求发送到此位置

        :param redirect_uri: The redirect_uri of this CreateTokenReqBody.
        :type redirect_uri: str
        """
        self._redirect_uri = redirect_uri

    @property
    def refresh_token(self):
        r"""Gets the refresh_token of this CreateTokenReqBody.

        刷新令牌，此令牌可在访问令牌过期后获取新的访问令牌

        :return: The refresh_token of this CreateTokenReqBody.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        r"""Sets the refresh_token of this CreateTokenReqBody.

        刷新令牌，此令牌可在访问令牌过期后获取新的访问令牌

        :param refresh_token: The refresh_token of this CreateTokenReqBody.
        :type refresh_token: str
        """
        self._refresh_token = refresh_token

    @property
    def scopes(self):
        r"""Gets the scopes of this CreateTokenReqBody.

        客户端定义的作用域列表，表示客户端想要获取的权限。授权后，此列表用于在授予访问令牌时限制权限

        :return: The scopes of this CreateTokenReqBody.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        r"""Sets the scopes of this CreateTokenReqBody.

        客户端定义的作用域列表，表示客户端想要获取的权限。授权后，此列表用于在授予访问令牌时限制权限

        :param scopes: The scopes of this CreateTokenReqBody.
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
        if not isinstance(other, CreateTokenReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
