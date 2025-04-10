# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlDomainCreate:

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
        'ingress_http_port': 'int',
        'ingress_https_port': 'int',
        'url_domain': 'str'
    }

    attribute_map = {
        'min_ssl_version': 'min_ssl_version',
        'is_http_redirect_to_https': 'is_http_redirect_to_https',
        'ingress_http_port': 'ingress_http_port',
        'ingress_https_port': 'ingress_https_port',
        'url_domain': 'url_domain'
    }

    def __init__(self, min_ssl_version=None, is_http_redirect_to_https=None, ingress_http_port=None, ingress_https_port=None, url_domain=None):
        r"""UrlDomainCreate

        The model defined in huaweicloud sdk

        :param min_ssl_version: 最小ssl协议版本号。支持TLSv1.1或TLSv1.2
        :type min_ssl_version: str
        :param is_http_redirect_to_https: 是否开启http到https的重定向，false为关闭，true为开启，默认为false
        :type is_http_redirect_to_https: bool
        :param ingress_http_port: 访问该域名绑定的http协议入方向端口，-1表示无端口且协议不支持，可使用80默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTP协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认80端口；如果填写该参数，则必须同时填写https_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 
        :type ingress_http_port: int
        :param ingress_https_port: 访问该域名绑定的https协议入方向端口，-1表示无端口且协议不支持，可使用443默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTPS协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认443端口；如果填写该参数，则必须同时填写http_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 
        :type ingress_https_port: int
        :param url_domain: 自定义域名。长度为0-255位的字符串，需要符合域名规范（即符合正则&#39;^(\\[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\\\\.){1,7}[a-zA-Z]{2,64}\\\\.?$&#39;或者符合正则&#39;^\\[*](\\\\.\\[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?){1,6}\\\\.[a-zA-Z]{2,64}\\\\.?$&#39;）。
        :type url_domain: str
        """
        
        

        self._min_ssl_version = None
        self._is_http_redirect_to_https = None
        self._ingress_http_port = None
        self._ingress_https_port = None
        self._url_domain = None
        self.discriminator = None

        if min_ssl_version is not None:
            self.min_ssl_version = min_ssl_version
        if is_http_redirect_to_https is not None:
            self.is_http_redirect_to_https = is_http_redirect_to_https
        if ingress_http_port is not None:
            self.ingress_http_port = ingress_http_port
        if ingress_https_port is not None:
            self.ingress_https_port = ingress_https_port
        if url_domain is not None:
            self.url_domain = url_domain

    @property
    def min_ssl_version(self):
        r"""Gets the min_ssl_version of this UrlDomainCreate.

        最小ssl协议版本号。支持TLSv1.1或TLSv1.2

        :return: The min_ssl_version of this UrlDomainCreate.
        :rtype: str
        """
        return self._min_ssl_version

    @min_ssl_version.setter
    def min_ssl_version(self, min_ssl_version):
        r"""Sets the min_ssl_version of this UrlDomainCreate.

        最小ssl协议版本号。支持TLSv1.1或TLSv1.2

        :param min_ssl_version: The min_ssl_version of this UrlDomainCreate.
        :type min_ssl_version: str
        """
        self._min_ssl_version = min_ssl_version

    @property
    def is_http_redirect_to_https(self):
        r"""Gets the is_http_redirect_to_https of this UrlDomainCreate.

        是否开启http到https的重定向，false为关闭，true为开启，默认为false

        :return: The is_http_redirect_to_https of this UrlDomainCreate.
        :rtype: bool
        """
        return self._is_http_redirect_to_https

    @is_http_redirect_to_https.setter
    def is_http_redirect_to_https(self, is_http_redirect_to_https):
        r"""Sets the is_http_redirect_to_https of this UrlDomainCreate.

        是否开启http到https的重定向，false为关闭，true为开启，默认为false

        :param is_http_redirect_to_https: The is_http_redirect_to_https of this UrlDomainCreate.
        :type is_http_redirect_to_https: bool
        """
        self._is_http_redirect_to_https = is_http_redirect_to_https

    @property
    def ingress_http_port(self):
        r"""Gets the ingress_http_port of this UrlDomainCreate.

        访问该域名绑定的http协议入方向端口，-1表示无端口且协议不支持，可使用80默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTP协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认80端口；如果填写该参数，则必须同时填写https_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 

        :return: The ingress_http_port of this UrlDomainCreate.
        :rtype: int
        """
        return self._ingress_http_port

    @ingress_http_port.setter
    def ingress_http_port(self, ingress_http_port):
        r"""Sets the ingress_http_port of this UrlDomainCreate.

        访问该域名绑定的http协议入方向端口，-1表示无端口且协议不支持，可使用80默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTP协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认80端口；如果填写该参数，则必须同时填写https_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 

        :param ingress_http_port: The ingress_http_port of this UrlDomainCreate.
        :type ingress_http_port: int
        """
        self._ingress_http_port = ingress_http_port

    @property
    def ingress_https_port(self):
        r"""Gets the ingress_https_port of this UrlDomainCreate.

        访问该域名绑定的https协议入方向端口，-1表示无端口且协议不支持，可使用443默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTPS协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认443端口；如果填写该参数，则必须同时填写http_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 

        :return: The ingress_https_port of this UrlDomainCreate.
        :rtype: int
        """
        return self._ingress_https_port

    @ingress_https_port.setter
    def ingress_https_port(self, ingress_https_port):
        r"""Sets the ingress_https_port of this UrlDomainCreate.

        访问该域名绑定的https协议入方向端口，-1表示无端口且协议不支持，可使用443默认端口，其他有效端口允许的取值范围为1024~49151，需为实例已开放的HTTPS协议的自定义入方向端口。  当创建域名时，该参数未填表示用默认443端口；如果填写该参数，则必须同时填写http_port；如果要http_port和https_port同时使用默认端口，则两个参数都不填。  当修改域名时，该参数未填表示不修改该端口。 

        :param ingress_https_port: The ingress_https_port of this UrlDomainCreate.
        :type ingress_https_port: int
        """
        self._ingress_https_port = ingress_https_port

    @property
    def url_domain(self):
        r"""Gets the url_domain of this UrlDomainCreate.

        自定义域名。长度为0-255位的字符串，需要符合域名规范（即符合正则'^(\\[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\\\\.){1,7}[a-zA-Z]{2,64}\\\\.?$'或者符合正则'^\\[*](\\\\.\\[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?){1,6}\\\\.[a-zA-Z]{2,64}\\\\.?$'）。

        :return: The url_domain of this UrlDomainCreate.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        r"""Sets the url_domain of this UrlDomainCreate.

        自定义域名。长度为0-255位的字符串，需要符合域名规范（即符合正则'^(\\[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\\\\.){1,7}[a-zA-Z]{2,64}\\\\.?$'或者符合正则'^\\[*](\\\\.\\[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?){1,6}\\\\.[a-zA-Z]{2,64}\\\\.?$'）。

        :param url_domain: The url_domain of this UrlDomainCreate.
        :type url_domain: str
        """
        self._url_domain = url_domain

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
        if not isinstance(other, UrlDomainCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
