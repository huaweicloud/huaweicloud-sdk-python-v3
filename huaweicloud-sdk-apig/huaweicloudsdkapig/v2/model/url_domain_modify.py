# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlDomainModify:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_ssl_version': 'str',
        'is_http_redirect_to_https': 'bool',
        'verified_client_certificate_enabled': 'bool',
        'ingress_http_port': 'int',
        'ingress_https_port': 'int'
    }

    attribute_map = {
        'min_ssl_version': 'min_ssl_version',
        'is_http_redirect_to_https': 'is_http_redirect_to_https',
        'verified_client_certificate_enabled': 'verified_client_certificate_enabled',
        'ingress_http_port': 'ingress_http_port',
        'ingress_https_port': 'ingress_https_port'
    }

    def __init__(self, min_ssl_version=None, is_http_redirect_to_https=None, verified_client_certificate_enabled=None, ingress_http_port=None, ingress_https_port=None):
        r"""UrlDomainModify

        The model defined in huaweicloud sdk

        :param min_ssl_version: 最小ssl协议版本号。支持TLSv1.1或TLSv1.2
        :type min_ssl_version: str
        :param is_http_redirect_to_https: 是否开启http到https的重定向，false为关闭，true为开启，默认为false
        :type is_http_redirect_to_https: bool
        :param verified_client_certificate_enabled: 是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。
        :type verified_client_certificate_enabled: bool
        :param ingress_http_port: 访问该域名绑定的http协议入方向端口，-1表示无端口且协议不支持，可使用80默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTP协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认80端口；如果填写该参数，则必须同时填写https_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 
        :type ingress_http_port: int
        :param ingress_https_port: 访问该域名绑定的https协议入方向端口，-1表示无端口且协议不支持，可使用443默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTPS协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认443端口；如果填写该参数，则必须同时填写http_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 
        :type ingress_https_port: int
        """
        
        

        self._min_ssl_version = None
        self._is_http_redirect_to_https = None
        self._verified_client_certificate_enabled = None
        self._ingress_http_port = None
        self._ingress_https_port = None
        self.discriminator = None

        self.min_ssl_version = min_ssl_version
        if is_http_redirect_to_https is not None:
            self.is_http_redirect_to_https = is_http_redirect_to_https
        if verified_client_certificate_enabled is not None:
            self.verified_client_certificate_enabled = verified_client_certificate_enabled
        if ingress_http_port is not None:
            self.ingress_http_port = ingress_http_port
        if ingress_https_port is not None:
            self.ingress_https_port = ingress_https_port

    @property
    def min_ssl_version(self):
        r"""Gets the min_ssl_version of this UrlDomainModify.

        最小ssl协议版本号。支持TLSv1.1或TLSv1.2

        :return: The min_ssl_version of this UrlDomainModify.
        :rtype: str
        """
        return self._min_ssl_version

    @min_ssl_version.setter
    def min_ssl_version(self, min_ssl_version):
        r"""Sets the min_ssl_version of this UrlDomainModify.

        最小ssl协议版本号。支持TLSv1.1或TLSv1.2

        :param min_ssl_version: The min_ssl_version of this UrlDomainModify.
        :type min_ssl_version: str
        """
        self._min_ssl_version = min_ssl_version

    @property
    def is_http_redirect_to_https(self):
        r"""Gets the is_http_redirect_to_https of this UrlDomainModify.

        是否开启http到https的重定向，false为关闭，true为开启，默认为false

        :return: The is_http_redirect_to_https of this UrlDomainModify.
        :rtype: bool
        """
        return self._is_http_redirect_to_https

    @is_http_redirect_to_https.setter
    def is_http_redirect_to_https(self, is_http_redirect_to_https):
        r"""Sets the is_http_redirect_to_https of this UrlDomainModify.

        是否开启http到https的重定向，false为关闭，true为开启，默认为false

        :param is_http_redirect_to_https: The is_http_redirect_to_https of this UrlDomainModify.
        :type is_http_redirect_to_https: bool
        """
        self._is_http_redirect_to_https = is_http_redirect_to_https

    @property
    def verified_client_certificate_enabled(self):
        r"""Gets the verified_client_certificate_enabled of this UrlDomainModify.

        是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :return: The verified_client_certificate_enabled of this UrlDomainModify.
        :rtype: bool
        """
        return self._verified_client_certificate_enabled

    @verified_client_certificate_enabled.setter
    def verified_client_certificate_enabled(self, verified_client_certificate_enabled):
        r"""Sets the verified_client_certificate_enabled of this UrlDomainModify.

        是否开启客户端证书校验。只有绑定证书时，该参数才生效。当绑定证书存在trusted_root_ca时，默认开启；当绑定证书不存在trusted_root_ca时，默认关闭。

        :param verified_client_certificate_enabled: The verified_client_certificate_enabled of this UrlDomainModify.
        :type verified_client_certificate_enabled: bool
        """
        self._verified_client_certificate_enabled = verified_client_certificate_enabled

    @property
    def ingress_http_port(self):
        r"""Gets the ingress_http_port of this UrlDomainModify.

        访问该域名绑定的http协议入方向端口，-1表示无端口且协议不支持，可使用80默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTP协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认80端口；如果填写该参数，则必须同时填写https_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 

        :return: The ingress_http_port of this UrlDomainModify.
        :rtype: int
        """
        return self._ingress_http_port

    @ingress_http_port.setter
    def ingress_http_port(self, ingress_http_port):
        r"""Sets the ingress_http_port of this UrlDomainModify.

        访问该域名绑定的http协议入方向端口，-1表示无端口且协议不支持，可使用80默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTP协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认80端口；如果填写该参数，则必须同时填写https_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 

        :param ingress_http_port: The ingress_http_port of this UrlDomainModify.
        :type ingress_http_port: int
        """
        self._ingress_http_port = ingress_http_port

    @property
    def ingress_https_port(self):
        r"""Gets the ingress_https_port of this UrlDomainModify.

        访问该域名绑定的https协议入方向端口，-1表示无端口且协议不支持，可使用443默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTPS协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认443端口；如果填写该参数，则必须同时填写http_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 

        :return: The ingress_https_port of this UrlDomainModify.
        :rtype: int
        """
        return self._ingress_https_port

    @ingress_https_port.setter
    def ingress_https_port(self, ingress_https_port):
        r"""Sets the ingress_https_port of this UrlDomainModify.

        访问该域名绑定的https协议入方向端口，-1表示无端口且协议不支持，可使用443默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTPS协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认443端口；如果填写该参数，则必须同时填写http_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 

        :param ingress_https_port: The ingress_https_port of this UrlDomainModify.
        :type ingress_https_port: int
        """
        self._ingress_https_port = ingress_https_port

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
        if not isinstance(other, UrlDomainModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
