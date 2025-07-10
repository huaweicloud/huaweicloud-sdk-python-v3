# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RadiusGatewayConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'app_id': 'str',
        'cert_domain_name': 'str',
        'token_url': 'str',
        'verification_cipher_url': 'str',
        'auth_type': 'str',
        'assist_auth_type': 'str',
        'expiration': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'app_id': 'app_id',
        'cert_domain_name': 'cert_domain_name',
        'token_url': 'token_url',
        'verification_cipher_url': 'verification_cipher_url',
        'auth_type': 'auth_type',
        'assist_auth_type': 'assist_auth_type',
        'expiration': 'expiration'
    }

    def __init__(self, enable=None, app_id=None, cert_domain_name=None, token_url=None, verification_cipher_url=None, auth_type=None, assist_auth_type=None, expiration=None):
        r"""RadiusGatewayConfigInfo

        The model defined in huaweicloud sdk

        :param enable: 是否启用。
        :type enable: bool
        :param app_id: 用户名。
        :type app_id: str
        :param cert_domain_name: 证书域名。
        :type cert_domain_name: str
        :param token_url: 获取token地址。
        :type token_url: str
        :param verification_cipher_url: 获取验证码地址。
        :type verification_cipher_url: str
        :param auth_type: 认证类型。
        :type auth_type: str
        :param assist_auth_type: 辅助认证类型。
        :type assist_auth_type: str
        :param expiration: 过期时间。
        :type expiration: str
        """
        
        

        self._enable = None
        self._app_id = None
        self._cert_domain_name = None
        self._token_url = None
        self._verification_cipher_url = None
        self._auth_type = None
        self._assist_auth_type = None
        self._expiration = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if app_id is not None:
            self.app_id = app_id
        if cert_domain_name is not None:
            self.cert_domain_name = cert_domain_name
        if token_url is not None:
            self.token_url = token_url
        if verification_cipher_url is not None:
            self.verification_cipher_url = verification_cipher_url
        if auth_type is not None:
            self.auth_type = auth_type
        if assist_auth_type is not None:
            self.assist_auth_type = assist_auth_type
        if expiration is not None:
            self.expiration = expiration

    @property
    def enable(self):
        r"""Gets the enable of this RadiusGatewayConfigInfo.

        是否启用。

        :return: The enable of this RadiusGatewayConfigInfo.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this RadiusGatewayConfigInfo.

        是否启用。

        :param enable: The enable of this RadiusGatewayConfigInfo.
        :type enable: bool
        """
        self._enable = enable

    @property
    def app_id(self):
        r"""Gets the app_id of this RadiusGatewayConfigInfo.

        用户名。

        :return: The app_id of this RadiusGatewayConfigInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this RadiusGatewayConfigInfo.

        用户名。

        :param app_id: The app_id of this RadiusGatewayConfigInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def cert_domain_name(self):
        r"""Gets the cert_domain_name of this RadiusGatewayConfigInfo.

        证书域名。

        :return: The cert_domain_name of this RadiusGatewayConfigInfo.
        :rtype: str
        """
        return self._cert_domain_name

    @cert_domain_name.setter
    def cert_domain_name(self, cert_domain_name):
        r"""Sets the cert_domain_name of this RadiusGatewayConfigInfo.

        证书域名。

        :param cert_domain_name: The cert_domain_name of this RadiusGatewayConfigInfo.
        :type cert_domain_name: str
        """
        self._cert_domain_name = cert_domain_name

    @property
    def token_url(self):
        r"""Gets the token_url of this RadiusGatewayConfigInfo.

        获取token地址。

        :return: The token_url of this RadiusGatewayConfigInfo.
        :rtype: str
        """
        return self._token_url

    @token_url.setter
    def token_url(self, token_url):
        r"""Sets the token_url of this RadiusGatewayConfigInfo.

        获取token地址。

        :param token_url: The token_url of this RadiusGatewayConfigInfo.
        :type token_url: str
        """
        self._token_url = token_url

    @property
    def verification_cipher_url(self):
        r"""Gets the verification_cipher_url of this RadiusGatewayConfigInfo.

        获取验证码地址。

        :return: The verification_cipher_url of this RadiusGatewayConfigInfo.
        :rtype: str
        """
        return self._verification_cipher_url

    @verification_cipher_url.setter
    def verification_cipher_url(self, verification_cipher_url):
        r"""Sets the verification_cipher_url of this RadiusGatewayConfigInfo.

        获取验证码地址。

        :param verification_cipher_url: The verification_cipher_url of this RadiusGatewayConfigInfo.
        :type verification_cipher_url: str
        """
        self._verification_cipher_url = verification_cipher_url

    @property
    def auth_type(self):
        r"""Gets the auth_type of this RadiusGatewayConfigInfo.

        认证类型。

        :return: The auth_type of this RadiusGatewayConfigInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this RadiusGatewayConfigInfo.

        认证类型。

        :param auth_type: The auth_type of this RadiusGatewayConfigInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def assist_auth_type(self):
        r"""Gets the assist_auth_type of this RadiusGatewayConfigInfo.

        辅助认证类型。

        :return: The assist_auth_type of this RadiusGatewayConfigInfo.
        :rtype: str
        """
        return self._assist_auth_type

    @assist_auth_type.setter
    def assist_auth_type(self, assist_auth_type):
        r"""Sets the assist_auth_type of this RadiusGatewayConfigInfo.

        辅助认证类型。

        :param assist_auth_type: The assist_auth_type of this RadiusGatewayConfigInfo.
        :type assist_auth_type: str
        """
        self._assist_auth_type = assist_auth_type

    @property
    def expiration(self):
        r"""Gets the expiration of this RadiusGatewayConfigInfo.

        过期时间。

        :return: The expiration of this RadiusGatewayConfigInfo.
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        r"""Sets the expiration of this RadiusGatewayConfigInfo.

        过期时间。

        :param expiration: The expiration of this RadiusGatewayConfigInfo.
        :type expiration: str
        """
        self._expiration = expiration

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
        if not isinstance(other, RadiusGatewayConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
