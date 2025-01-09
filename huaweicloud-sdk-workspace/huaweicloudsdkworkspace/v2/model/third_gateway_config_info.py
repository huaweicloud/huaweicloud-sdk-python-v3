# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThirdGatewayConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'login_url': 'str',
        'logout_url': 'str',
        'token_url': 'str',
        'verification_cipher_url': 'str',
        'cert_content': 'str'
    }

    attribute_map = {
        'login_url': 'login_url',
        'logout_url': 'logout_url',
        'token_url': 'token_url',
        'verification_cipher_url': 'verification_cipher_url',
        'cert_content': 'cert_content'
    }

    def __init__(self, login_url=None, logout_url=None, token_url=None, verification_cipher_url=None, cert_content=None):
        """ThirdGatewayConfigInfo

        The model defined in huaweicloud sdk

        :param login_url: 第三方登录url
        :type login_url: str
        :param logout_url: 第三方登出url
        :type logout_url: str
        :param token_url: 第三方网关token校验地址
        :type token_url: str
        :param verification_cipher_url: 校验证书url
        :type verification_cipher_url: str
        :param cert_content: 第三方证书
        :type cert_content: str
        """
        
        

        self._login_url = None
        self._logout_url = None
        self._token_url = None
        self._verification_cipher_url = None
        self._cert_content = None
        self.discriminator = None

        self.login_url = login_url
        self.logout_url = logout_url
        self.token_url = token_url
        self.verification_cipher_url = verification_cipher_url
        self.cert_content = cert_content

    @property
    def login_url(self):
        """Gets the login_url of this ThirdGatewayConfigInfo.

        第三方登录url

        :return: The login_url of this ThirdGatewayConfigInfo.
        :rtype: str
        """
        return self._login_url

    @login_url.setter
    def login_url(self, login_url):
        """Sets the login_url of this ThirdGatewayConfigInfo.

        第三方登录url

        :param login_url: The login_url of this ThirdGatewayConfigInfo.
        :type login_url: str
        """
        self._login_url = login_url

    @property
    def logout_url(self):
        """Gets the logout_url of this ThirdGatewayConfigInfo.

        第三方登出url

        :return: The logout_url of this ThirdGatewayConfigInfo.
        :rtype: str
        """
        return self._logout_url

    @logout_url.setter
    def logout_url(self, logout_url):
        """Sets the logout_url of this ThirdGatewayConfigInfo.

        第三方登出url

        :param logout_url: The logout_url of this ThirdGatewayConfigInfo.
        :type logout_url: str
        """
        self._logout_url = logout_url

    @property
    def token_url(self):
        """Gets the token_url of this ThirdGatewayConfigInfo.

        第三方网关token校验地址

        :return: The token_url of this ThirdGatewayConfigInfo.
        :rtype: str
        """
        return self._token_url

    @token_url.setter
    def token_url(self, token_url):
        """Sets the token_url of this ThirdGatewayConfigInfo.

        第三方网关token校验地址

        :param token_url: The token_url of this ThirdGatewayConfigInfo.
        :type token_url: str
        """
        self._token_url = token_url

    @property
    def verification_cipher_url(self):
        """Gets the verification_cipher_url of this ThirdGatewayConfigInfo.

        校验证书url

        :return: The verification_cipher_url of this ThirdGatewayConfigInfo.
        :rtype: str
        """
        return self._verification_cipher_url

    @verification_cipher_url.setter
    def verification_cipher_url(self, verification_cipher_url):
        """Sets the verification_cipher_url of this ThirdGatewayConfigInfo.

        校验证书url

        :param verification_cipher_url: The verification_cipher_url of this ThirdGatewayConfigInfo.
        :type verification_cipher_url: str
        """
        self._verification_cipher_url = verification_cipher_url

    @property
    def cert_content(self):
        """Gets the cert_content of this ThirdGatewayConfigInfo.

        第三方证书

        :return: The cert_content of this ThirdGatewayConfigInfo.
        :rtype: str
        """
        return self._cert_content

    @cert_content.setter
    def cert_content(self, cert_content):
        """Sets the cert_content of this ThirdGatewayConfigInfo.

        第三方证书

        :param cert_content: The cert_content of this ThirdGatewayConfigInfo.
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
        if not isinstance(other, ThirdGatewayConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
