# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpInfoResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'https_status': 'int',
        'cert_name': 'str',
        'certificate': 'str',
        'private_key': 'str',
        'certificate_type': 'int',
        'force_redirect_https': 'int',
        'force_redirect_config': 'ForceRedirect',
        'http2': 'int',
        'expiration_time': 'int'
    }

    attribute_map = {
        'https_status': 'https_status',
        'cert_name': 'cert_name',
        'certificate': 'certificate',
        'private_key': 'private_key',
        'certificate_type': 'certificate_type',
        'force_redirect_https': 'force_redirect_https',
        'force_redirect_config': 'force_redirect_config',
        'http2': 'http2',
        'expiration_time': 'expiration_time'
    }

    def __init__(self, https_status=None, cert_name=None, certificate=None, private_key=None, certificate_type=None, force_redirect_https=None, force_redirect_config=None, http2=None, expiration_time=None):
        """HttpInfoResponseBody

        The model defined in huaweicloud sdk

        :param https_status: HTTPS证书是否启用。0：不启用，此时无需填写证书及私钥参数；1：启用HTTPS加速并协议跟随回源；2：启用HTTPS加速并HTTP回源；3：启用HTTPS加速并HTTPS回源，开启时需要传递证书及私钥
        :type https_status: int
        :param cert_name: 证书名称。（长度限制为3-32字符）。
        :type cert_name: str
        :param certificate: 证书内容。
        :type certificate: str
        :param private_key: 功能说明： HTTPS协议使用的私钥，不启用证书则无需输入。（为了客户信息安全，接口返回私钥为空）
        :type private_key: str
        :param certificate_type: 证书类型。1：代表华为云托管证书；0：表示自有证书。
        :type certificate_type: int
        :param force_redirect_https: 客户端请求是否强制重定向。1是，0否。（如果为2，表示强制跳转HTTP）
        :type force_redirect_https: int
        :param force_redirect_config: 
        :type force_redirect_config: :class:`huaweicloudsdkcdn.v1.ForceRedirect`
        :param http2: 是否使用HTTP2.0。（1是，0否。）
        :type http2: int
        :param expiration_time: 证书过期时间
        :type expiration_time: int
        """
        
        

        self._https_status = None
        self._cert_name = None
        self._certificate = None
        self._private_key = None
        self._certificate_type = None
        self._force_redirect_https = None
        self._force_redirect_config = None
        self._http2 = None
        self._expiration_time = None
        self.discriminator = None

        if https_status is not None:
            self.https_status = https_status
        if cert_name is not None:
            self.cert_name = cert_name
        if certificate is not None:
            self.certificate = certificate
        if private_key is not None:
            self.private_key = private_key
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if force_redirect_https is not None:
            self.force_redirect_https = force_redirect_https
        if force_redirect_config is not None:
            self.force_redirect_config = force_redirect_config
        if http2 is not None:
            self.http2 = http2
        if expiration_time is not None:
            self.expiration_time = expiration_time

    @property
    def https_status(self):
        """Gets the https_status of this HttpInfoResponseBody.

        HTTPS证书是否启用。0：不启用，此时无需填写证书及私钥参数；1：启用HTTPS加速并协议跟随回源；2：启用HTTPS加速并HTTP回源；3：启用HTTPS加速并HTTPS回源，开启时需要传递证书及私钥

        :return: The https_status of this HttpInfoResponseBody.
        :rtype: int
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        """Sets the https_status of this HttpInfoResponseBody.

        HTTPS证书是否启用。0：不启用，此时无需填写证书及私钥参数；1：启用HTTPS加速并协议跟随回源；2：启用HTTPS加速并HTTP回源；3：启用HTTPS加速并HTTPS回源，开启时需要传递证书及私钥

        :param https_status: The https_status of this HttpInfoResponseBody.
        :type https_status: int
        """
        self._https_status = https_status

    @property
    def cert_name(self):
        """Gets the cert_name of this HttpInfoResponseBody.

        证书名称。（长度限制为3-32字符）。

        :return: The cert_name of this HttpInfoResponseBody.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        """Sets the cert_name of this HttpInfoResponseBody.

        证书名称。（长度限制为3-32字符）。

        :param cert_name: The cert_name of this HttpInfoResponseBody.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def certificate(self):
        """Gets the certificate of this HttpInfoResponseBody.

        证书内容。

        :return: The certificate of this HttpInfoResponseBody.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this HttpInfoResponseBody.

        证书内容。

        :param certificate: The certificate of this HttpInfoResponseBody.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        """Gets the private_key of this HttpInfoResponseBody.

        功能说明： HTTPS协议使用的私钥，不启用证书则无需输入。（为了客户信息安全，接口返回私钥为空）

        :return: The private_key of this HttpInfoResponseBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this HttpInfoResponseBody.

        功能说明： HTTPS协议使用的私钥，不启用证书则无需输入。（为了客户信息安全，接口返回私钥为空）

        :param private_key: The private_key of this HttpInfoResponseBody.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate_type(self):
        """Gets the certificate_type of this HttpInfoResponseBody.

        证书类型。1：代表华为云托管证书；0：表示自有证书。

        :return: The certificate_type of this HttpInfoResponseBody.
        :rtype: int
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this HttpInfoResponseBody.

        证书类型。1：代表华为云托管证书；0：表示自有证书。

        :param certificate_type: The certificate_type of this HttpInfoResponseBody.
        :type certificate_type: int
        """
        self._certificate_type = certificate_type

    @property
    def force_redirect_https(self):
        """Gets the force_redirect_https of this HttpInfoResponseBody.

        客户端请求是否强制重定向。1是，0否。（如果为2，表示强制跳转HTTP）

        :return: The force_redirect_https of this HttpInfoResponseBody.
        :rtype: int
        """
        return self._force_redirect_https

    @force_redirect_https.setter
    def force_redirect_https(self, force_redirect_https):
        """Sets the force_redirect_https of this HttpInfoResponseBody.

        客户端请求是否强制重定向。1是，0否。（如果为2，表示强制跳转HTTP）

        :param force_redirect_https: The force_redirect_https of this HttpInfoResponseBody.
        :type force_redirect_https: int
        """
        self._force_redirect_https = force_redirect_https

    @property
    def force_redirect_config(self):
        """Gets the force_redirect_config of this HttpInfoResponseBody.

        :return: The force_redirect_config of this HttpInfoResponseBody.
        :rtype: :class:`huaweicloudsdkcdn.v1.ForceRedirect`
        """
        return self._force_redirect_config

    @force_redirect_config.setter
    def force_redirect_config(self, force_redirect_config):
        """Sets the force_redirect_config of this HttpInfoResponseBody.

        :param force_redirect_config: The force_redirect_config of this HttpInfoResponseBody.
        :type force_redirect_config: :class:`huaweicloudsdkcdn.v1.ForceRedirect`
        """
        self._force_redirect_config = force_redirect_config

    @property
    def http2(self):
        """Gets the http2 of this HttpInfoResponseBody.

        是否使用HTTP2.0。（1是，0否。）

        :return: The http2 of this HttpInfoResponseBody.
        :rtype: int
        """
        return self._http2

    @http2.setter
    def http2(self, http2):
        """Sets the http2 of this HttpInfoResponseBody.

        是否使用HTTP2.0。（1是，0否。）

        :param http2: The http2 of this HttpInfoResponseBody.
        :type http2: int
        """
        self._http2 = http2

    @property
    def expiration_time(self):
        """Gets the expiration_time of this HttpInfoResponseBody.

        证书过期时间

        :return: The expiration_time of this HttpInfoResponseBody.
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this HttpInfoResponseBody.

        证书过期时间

        :param expiration_time: The expiration_time of this HttpInfoResponseBody.
        :type expiration_time: int
        """
        self._expiration_time = expiration_time

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
        if not isinstance(other, HttpInfoResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
