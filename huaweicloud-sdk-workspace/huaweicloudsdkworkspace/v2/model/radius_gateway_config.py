# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RadiusGatewayConfig:

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
        'password': 'str',
        'token_url': 'str',
        'verification_cipher_url': 'str',
        'cert_content': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'app_id': 'app_id',
        'password': 'password',
        'token_url': 'token_url',
        'verification_cipher_url': 'verification_cipher_url',
        'cert_content': 'cert_content'
    }

    def __init__(self, enable=None, app_id=None, password=None, token_url=None, verification_cipher_url=None, cert_content=None):
        r"""RadiusGatewayConfig

        The model defined in huaweicloud sdk

        :param enable: 是否启用。
        :type enable: bool
        :param app_id: 用户名。
        :type app_id: str
        :param password: 密码。
        :type password: str
        :param token_url: 获取token地址。
        :type token_url: str
        :param verification_cipher_url: 获取验证码地址。
        :type verification_cipher_url: str
        :param cert_content: 证书内容（PEM）。
        :type cert_content: str
        """
        
        

        self._enable = None
        self._app_id = None
        self._password = None
        self._token_url = None
        self._verification_cipher_url = None
        self._cert_content = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if app_id is not None:
            self.app_id = app_id
        if password is not None:
            self.password = password
        if token_url is not None:
            self.token_url = token_url
        if verification_cipher_url is not None:
            self.verification_cipher_url = verification_cipher_url
        if cert_content is not None:
            self.cert_content = cert_content

    @property
    def enable(self):
        r"""Gets the enable of this RadiusGatewayConfig.

        是否启用。

        :return: The enable of this RadiusGatewayConfig.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this RadiusGatewayConfig.

        是否启用。

        :param enable: The enable of this RadiusGatewayConfig.
        :type enable: bool
        """
        self._enable = enable

    @property
    def app_id(self):
        r"""Gets the app_id of this RadiusGatewayConfig.

        用户名。

        :return: The app_id of this RadiusGatewayConfig.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this RadiusGatewayConfig.

        用户名。

        :param app_id: The app_id of this RadiusGatewayConfig.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def password(self):
        r"""Gets the password of this RadiusGatewayConfig.

        密码。

        :return: The password of this RadiusGatewayConfig.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this RadiusGatewayConfig.

        密码。

        :param password: The password of this RadiusGatewayConfig.
        :type password: str
        """
        self._password = password

    @property
    def token_url(self):
        r"""Gets the token_url of this RadiusGatewayConfig.

        获取token地址。

        :return: The token_url of this RadiusGatewayConfig.
        :rtype: str
        """
        return self._token_url

    @token_url.setter
    def token_url(self, token_url):
        r"""Sets the token_url of this RadiusGatewayConfig.

        获取token地址。

        :param token_url: The token_url of this RadiusGatewayConfig.
        :type token_url: str
        """
        self._token_url = token_url

    @property
    def verification_cipher_url(self):
        r"""Gets the verification_cipher_url of this RadiusGatewayConfig.

        获取验证码地址。

        :return: The verification_cipher_url of this RadiusGatewayConfig.
        :rtype: str
        """
        return self._verification_cipher_url

    @verification_cipher_url.setter
    def verification_cipher_url(self, verification_cipher_url):
        r"""Sets the verification_cipher_url of this RadiusGatewayConfig.

        获取验证码地址。

        :param verification_cipher_url: The verification_cipher_url of this RadiusGatewayConfig.
        :type verification_cipher_url: str
        """
        self._verification_cipher_url = verification_cipher_url

    @property
    def cert_content(self):
        r"""Gets the cert_content of this RadiusGatewayConfig.

        证书内容（PEM）。

        :return: The cert_content of this RadiusGatewayConfig.
        :rtype: str
        """
        return self._cert_content

    @cert_content.setter
    def cert_content(self, cert_content):
        r"""Sets the cert_content of this RadiusGatewayConfig.

        证书内容（PEM）。

        :param cert_content: The cert_content of this RadiusGatewayConfig.
        :type cert_content: str
        """
        self._cert_content = cert_content

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
        if not isinstance(other, RadiusGatewayConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
