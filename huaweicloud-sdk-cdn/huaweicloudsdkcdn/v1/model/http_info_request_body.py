# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_name': 'str',
        'https_status': 'int',
        'certificate': 'str',
        'private_key': 'str',
        'http2': 'int',
        'certificate_type': 'int',
        'force_redirect_https': 'int',
        'force_redirect_config': 'ForceRedirect'
    }

    attribute_map = {
        'cert_name': 'cert_name',
        'https_status': 'https_status',
        'certificate': 'certificate',
        'private_key': 'private_key',
        'http2': 'http2',
        'certificate_type': 'certificate_type',
        'force_redirect_https': 'force_redirect_https',
        'force_redirect_config': 'force_redirect_config'
    }

    def __init__(self, cert_name=None, https_status=None, certificate=None, private_key=None, http2=None, certificate_type=None, force_redirect_https=None, force_redirect_config=None):
        """HttpInfoRequestBody

        The model defined in huaweicloud sdk

        :param cert_name: 证书名字。（长度限制为3-64字符）。
        :type cert_name: str
        :param https_status: HTTPS证书是否启用。0：不启用，此时无需填写证书及私钥参数；1：启用HTTPS加速并协议跟随回源；2：启用HTTPS加速并HTTP回源；3：启用HTTPS加速并HTTPS回源，首次配置证书需要传递证书及私钥，如已有证书可不用传证书及私钥。
        :type https_status: int
        :param certificate: HTTPS协议使用的SSL证书内容，仅支持PEM编码格式。不启用证书则无需输入。初次配置证书时必传。
        :type certificate: str
        :param private_key: HTTPS协议使用的SSL证书私钥内容，仅支持PEM编码格式。不启用证书则无需输入。初次配置证书时必传。
        :type private_key: str
        :param http2: 是否使用HTTP2.0。（1：是，0：否。）
        :type http2: int
        :param certificate_type: 证书类型。1：代表华为云托管证书；0：表示自有证书。 默认值0。
        :type certificate_type: int
        :param force_redirect_https: 强制跳转HTTPS（0：不强制；1：强制） 为空值时默认设置为关闭。（此参数即将下线,建议使用force_redirect_config修改配置）
        :type force_redirect_https: int
        :param force_redirect_config: 
        :type force_redirect_config: :class:`huaweicloudsdkcdn.v1.ForceRedirect`
        """
        
        

        self._cert_name = None
        self._https_status = None
        self._certificate = None
        self._private_key = None
        self._http2 = None
        self._certificate_type = None
        self._force_redirect_https = None
        self._force_redirect_config = None
        self.discriminator = None

        self.cert_name = cert_name
        self.https_status = https_status
        if certificate is not None:
            self.certificate = certificate
        if private_key is not None:
            self.private_key = private_key
        if http2 is not None:
            self.http2 = http2
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if force_redirect_https is not None:
            self.force_redirect_https = force_redirect_https
        if force_redirect_config is not None:
            self.force_redirect_config = force_redirect_config

    @property
    def cert_name(self):
        """Gets the cert_name of this HttpInfoRequestBody.

        证书名字。（长度限制为3-64字符）。

        :return: The cert_name of this HttpInfoRequestBody.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        """Sets the cert_name of this HttpInfoRequestBody.

        证书名字。（长度限制为3-64字符）。

        :param cert_name: The cert_name of this HttpInfoRequestBody.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def https_status(self):
        """Gets the https_status of this HttpInfoRequestBody.

        HTTPS证书是否启用。0：不启用，此时无需填写证书及私钥参数；1：启用HTTPS加速并协议跟随回源；2：启用HTTPS加速并HTTP回源；3：启用HTTPS加速并HTTPS回源，首次配置证书需要传递证书及私钥，如已有证书可不用传证书及私钥。

        :return: The https_status of this HttpInfoRequestBody.
        :rtype: int
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        """Sets the https_status of this HttpInfoRequestBody.

        HTTPS证书是否启用。0：不启用，此时无需填写证书及私钥参数；1：启用HTTPS加速并协议跟随回源；2：启用HTTPS加速并HTTP回源；3：启用HTTPS加速并HTTPS回源，首次配置证书需要传递证书及私钥，如已有证书可不用传证书及私钥。

        :param https_status: The https_status of this HttpInfoRequestBody.
        :type https_status: int
        """
        self._https_status = https_status

    @property
    def certificate(self):
        """Gets the certificate of this HttpInfoRequestBody.

        HTTPS协议使用的SSL证书内容，仅支持PEM编码格式。不启用证书则无需输入。初次配置证书时必传。

        :return: The certificate of this HttpInfoRequestBody.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this HttpInfoRequestBody.

        HTTPS协议使用的SSL证书内容，仅支持PEM编码格式。不启用证书则无需输入。初次配置证书时必传。

        :param certificate: The certificate of this HttpInfoRequestBody.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        """Gets the private_key of this HttpInfoRequestBody.

        HTTPS协议使用的SSL证书私钥内容，仅支持PEM编码格式。不启用证书则无需输入。初次配置证书时必传。

        :return: The private_key of this HttpInfoRequestBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this HttpInfoRequestBody.

        HTTPS协议使用的SSL证书私钥内容，仅支持PEM编码格式。不启用证书则无需输入。初次配置证书时必传。

        :param private_key: The private_key of this HttpInfoRequestBody.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def http2(self):
        """Gets the http2 of this HttpInfoRequestBody.

        是否使用HTTP2.0。（1：是，0：否。）

        :return: The http2 of this HttpInfoRequestBody.
        :rtype: int
        """
        return self._http2

    @http2.setter
    def http2(self, http2):
        """Sets the http2 of this HttpInfoRequestBody.

        是否使用HTTP2.0。（1：是，0：否。）

        :param http2: The http2 of this HttpInfoRequestBody.
        :type http2: int
        """
        self._http2 = http2

    @property
    def certificate_type(self):
        """Gets the certificate_type of this HttpInfoRequestBody.

        证书类型。1：代表华为云托管证书；0：表示自有证书。 默认值0。

        :return: The certificate_type of this HttpInfoRequestBody.
        :rtype: int
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this HttpInfoRequestBody.

        证书类型。1：代表华为云托管证书；0：表示自有证书。 默认值0。

        :param certificate_type: The certificate_type of this HttpInfoRequestBody.
        :type certificate_type: int
        """
        self._certificate_type = certificate_type

    @property
    def force_redirect_https(self):
        """Gets the force_redirect_https of this HttpInfoRequestBody.

        强制跳转HTTPS（0：不强制；1：强制） 为空值时默认设置为关闭。（此参数即将下线,建议使用force_redirect_config修改配置）

        :return: The force_redirect_https of this HttpInfoRequestBody.
        :rtype: int
        """
        return self._force_redirect_https

    @force_redirect_https.setter
    def force_redirect_https(self, force_redirect_https):
        """Sets the force_redirect_https of this HttpInfoRequestBody.

        强制跳转HTTPS（0：不强制；1：强制） 为空值时默认设置为关闭。（此参数即将下线,建议使用force_redirect_config修改配置）

        :param force_redirect_https: The force_redirect_https of this HttpInfoRequestBody.
        :type force_redirect_https: int
        """
        self._force_redirect_https = force_redirect_https

    @property
    def force_redirect_config(self):
        """Gets the force_redirect_config of this HttpInfoRequestBody.

        :return: The force_redirect_config of this HttpInfoRequestBody.
        :rtype: :class:`huaweicloudsdkcdn.v1.ForceRedirect`
        """
        return self._force_redirect_config

    @force_redirect_config.setter
    def force_redirect_config(self, force_redirect_config):
        """Sets the force_redirect_config of this HttpInfoRequestBody.

        :param force_redirect_config: The force_redirect_config of this HttpInfoRequestBody.
        :type force_redirect_config: :class:`huaweicloudsdkcdn.v1.ForceRedirect`
        """
        self._force_redirect_config = force_redirect_config

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
        if not isinstance(other, HttpInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
