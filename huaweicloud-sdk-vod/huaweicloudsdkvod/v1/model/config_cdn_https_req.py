# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigCdnHttpsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'domain': 'str',
        'cert_name': 'str',
        'cert_id': 'str',
        'https_status': 'int',
        'certificate': 'str',
        'private_key': 'str',
        'force_redirect_https': 'int',
        'http2': 'int'
    }

    attribute_map = {
        'source': 'source',
        'domain': 'domain',
        'cert_name': 'cert_name',
        'cert_id': 'cert_id',
        'https_status': 'https_status',
        'certificate': 'certificate',
        'private_key': 'private_key',
        'force_redirect_https': 'force_redirect_https',
        'http2': 'http2'
    }

    def __init__(self, source=None, domain=None, cert_name=None, cert_id=None, https_status=None, certificate=None, private_key=None, force_redirect_https=None, http2=None):
        r"""ConfigCdnHttpsReq

        The model defined in huaweicloud sdk

        :param source: 来源，user表示用户自己上传，scm表示scm证书，默认user 
        :type source: str
        :param domain: 加速域名 
        :type domain: str
        :param cert_name: 证书名称，若来源是scm则非必填，不填默认取scm上的证书名称 
        :type cert_name: str
        :param cert_id: scm证书ID，若来源是scm则必填 
        :type cert_id: str
        :param https_status: https配置，0为关闭https配置，1为开启https配置，默认0 
        :type https_status: int
        :param certificate: 证书内容，若来源是user则需填写，来源是scm则非必填 
        :type certificate: str
        :param private_key: 私钥，若来源是user则需填写，来源是scm则非必填 
        :type private_key: str
        :param force_redirect_https: 客户端请求是否强制重定向，0表示不重定向，1表示重定向，默认0 
        :type force_redirect_https: int
        :param http2: 是否使用HTTP2.0，0表示不使用HTTP2.0，1表示使用，默认0 
        :type http2: int
        """
        
        

        self._source = None
        self._domain = None
        self._cert_name = None
        self._cert_id = None
        self._https_status = None
        self._certificate = None
        self._private_key = None
        self._force_redirect_https = None
        self._http2 = None
        self.discriminator = None

        if source is not None:
            self.source = source
        self.domain = domain
        if cert_name is not None:
            self.cert_name = cert_name
        if cert_id is not None:
            self.cert_id = cert_id
        if https_status is not None:
            self.https_status = https_status
        if certificate is not None:
            self.certificate = certificate
        if private_key is not None:
            self.private_key = private_key
        if force_redirect_https is not None:
            self.force_redirect_https = force_redirect_https
        if http2 is not None:
            self.http2 = http2

    @property
    def source(self):
        r"""Gets the source of this ConfigCdnHttpsReq.

        来源，user表示用户自己上传，scm表示scm证书，默认user 

        :return: The source of this ConfigCdnHttpsReq.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ConfigCdnHttpsReq.

        来源，user表示用户自己上传，scm表示scm证书，默认user 

        :param source: The source of this ConfigCdnHttpsReq.
        :type source: str
        """
        self._source = source

    @property
    def domain(self):
        r"""Gets the domain of this ConfigCdnHttpsReq.

        加速域名 

        :return: The domain of this ConfigCdnHttpsReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ConfigCdnHttpsReq.

        加速域名 

        :param domain: The domain of this ConfigCdnHttpsReq.
        :type domain: str
        """
        self._domain = domain

    @property
    def cert_name(self):
        r"""Gets the cert_name of this ConfigCdnHttpsReq.

        证书名称，若来源是scm则非必填，不填默认取scm上的证书名称 

        :return: The cert_name of this ConfigCdnHttpsReq.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this ConfigCdnHttpsReq.

        证书名称，若来源是scm则非必填，不填默认取scm上的证书名称 

        :param cert_name: The cert_name of this ConfigCdnHttpsReq.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def cert_id(self):
        r"""Gets the cert_id of this ConfigCdnHttpsReq.

        scm证书ID，若来源是scm则必填 

        :return: The cert_id of this ConfigCdnHttpsReq.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        r"""Sets the cert_id of this ConfigCdnHttpsReq.

        scm证书ID，若来源是scm则必填 

        :param cert_id: The cert_id of this ConfigCdnHttpsReq.
        :type cert_id: str
        """
        self._cert_id = cert_id

    @property
    def https_status(self):
        r"""Gets the https_status of this ConfigCdnHttpsReq.

        https配置，0为关闭https配置，1为开启https配置，默认0 

        :return: The https_status of this ConfigCdnHttpsReq.
        :rtype: int
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        r"""Sets the https_status of this ConfigCdnHttpsReq.

        https配置，0为关闭https配置，1为开启https配置，默认0 

        :param https_status: The https_status of this ConfigCdnHttpsReq.
        :type https_status: int
        """
        self._https_status = https_status

    @property
    def certificate(self):
        r"""Gets the certificate of this ConfigCdnHttpsReq.

        证书内容，若来源是user则需填写，来源是scm则非必填 

        :return: The certificate of this ConfigCdnHttpsReq.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this ConfigCdnHttpsReq.

        证书内容，若来源是user则需填写，来源是scm则非必填 

        :param certificate: The certificate of this ConfigCdnHttpsReq.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        r"""Gets the private_key of this ConfigCdnHttpsReq.

        私钥，若来源是user则需填写，来源是scm则非必填 

        :return: The private_key of this ConfigCdnHttpsReq.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this ConfigCdnHttpsReq.

        私钥，若来源是user则需填写，来源是scm则非必填 

        :param private_key: The private_key of this ConfigCdnHttpsReq.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def force_redirect_https(self):
        r"""Gets the force_redirect_https of this ConfigCdnHttpsReq.

        客户端请求是否强制重定向，0表示不重定向，1表示重定向，默认0 

        :return: The force_redirect_https of this ConfigCdnHttpsReq.
        :rtype: int
        """
        return self._force_redirect_https

    @force_redirect_https.setter
    def force_redirect_https(self, force_redirect_https):
        r"""Sets the force_redirect_https of this ConfigCdnHttpsReq.

        客户端请求是否强制重定向，0表示不重定向，1表示重定向，默认0 

        :param force_redirect_https: The force_redirect_https of this ConfigCdnHttpsReq.
        :type force_redirect_https: int
        """
        self._force_redirect_https = force_redirect_https

    @property
    def http2(self):
        r"""Gets the http2 of this ConfigCdnHttpsReq.

        是否使用HTTP2.0，0表示不使用HTTP2.0，1表示使用，默认0 

        :return: The http2 of this ConfigCdnHttpsReq.
        :rtype: int
        """
        return self._http2

    @http2.setter
    def http2(self, http2):
        r"""Sets the http2 of this ConfigCdnHttpsReq.

        是否使用HTTP2.0，0表示不使用HTTP2.0，1表示使用，默认0 

        :param http2: The http2 of this ConfigCdnHttpsReq.
        :type http2: int
        """
        self._http2 = http2

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigCdnHttpsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
