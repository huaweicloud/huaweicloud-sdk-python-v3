# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpsDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'domain_name': 'str',
        'cert_name': 'str',
        'certificate': 'str',
        'private_key': 'str',
        'certificate_type': 'int',
        'expiration_time': 'int',
        'https_status': 'int',
        'force_redirect_https': 'int',
        'force_redirect_config': 'ForceRedirect',
        'http2': 'int',
        'certificates': 'list[HttpsDetailCertificates]'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'cert_name': 'cert_name',
        'certificate': 'certificate',
        'private_key': 'private_key',
        'certificate_type': 'certificate_type',
        'expiration_time': 'expiration_time',
        'https_status': 'https_status',
        'force_redirect_https': 'force_redirect_https',
        'force_redirect_config': 'force_redirect_config',
        'http2': 'http2',
        'certificates': 'certificates'
    }

    def __init__(self, domain_id=None, domain_name=None, cert_name=None, certificate=None, private_key=None, certificate_type=None, expiration_time=None, https_status=None, force_redirect_https=None, force_redirect_config=None, http2=None, certificates=None):
        r"""HttpsDetail

        The model defined in huaweicloud sdk

        :param domain_id: **参数解释：** 域名id。 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type domain_id: str
        :param domain_name: **参数解释：** 绑定该证书的域名。 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type domain_name: str
        :param cert_name: **参数解释：** 证书名字。 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type cert_name: str
        :param certificate: **参数解释：** 证书内容。 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type certificate: str
        :param private_key: **参数解释：** 私钥内容。 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type private_key: str
        :param certificate_type: 证书类型，0：自有证书，1：云托管证书，2：SCM证书。
        :type certificate_type: int
        :param expiration_time: **参数解释：** 证书过期时间，Unix时间戳格式，单位为毫秒。 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type expiration_time: int
        :param https_status: HTTPS证书是否启用，取值0：不启用；1：启用HTTPS加速并协议跟随回源；2：启用HTTPS加速并HTTP回源。
        :type https_status: int
        :param force_redirect_https: 客户端请求是否强制重定向。1是，0否。（如果为2，表示强制跳转HTTP）
        :type force_redirect_https: int
        :param force_redirect_config: 
        :type force_redirect_config: :class:`huaweicloudsdkcdn.v2.ForceRedirect`
        :param http2: 是否使用HTTP2.0。（1是，0否。）
        :type http2: int
        :param certificates: **参数解释：** 证书列表，配置双证书场景下包含国际证书和国密证书两项 **约束限制：** 不涉及
        :type certificates: list[:class:`huaweicloudsdkcdn.v2.HttpsDetailCertificates`]
        """
        
        

        self._domain_id = None
        self._domain_name = None
        self._cert_name = None
        self._certificate = None
        self._private_key = None
        self._certificate_type = None
        self._expiration_time = None
        self._https_status = None
        self._force_redirect_https = None
        self._force_redirect_config = None
        self._http2 = None
        self._certificates = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if cert_name is not None:
            self.cert_name = cert_name
        if certificate is not None:
            self.certificate = certificate
        if private_key is not None:
            self.private_key = private_key
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if https_status is not None:
            self.https_status = https_status
        if force_redirect_https is not None:
            self.force_redirect_https = force_redirect_https
        if force_redirect_config is not None:
            self.force_redirect_config = force_redirect_config
        if http2 is not None:
            self.http2 = http2
        if certificates is not None:
            self.certificates = certificates

    @property
    def domain_id(self):
        r"""Gets the domain_id of this HttpsDetail.

        **参数解释：** 域名id。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The domain_id of this HttpsDetail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this HttpsDetail.

        **参数解释：** 域名id。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param domain_id: The domain_id of this HttpsDetail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this HttpsDetail.

        **参数解释：** 绑定该证书的域名。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The domain_name of this HttpsDetail.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this HttpsDetail.

        **参数解释：** 绑定该证书的域名。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param domain_name: The domain_name of this HttpsDetail.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def cert_name(self):
        r"""Gets the cert_name of this HttpsDetail.

        **参数解释：** 证书名字。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The cert_name of this HttpsDetail.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this HttpsDetail.

        **参数解释：** 证书名字。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param cert_name: The cert_name of this HttpsDetail.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def certificate(self):
        r"""Gets the certificate of this HttpsDetail.

        **参数解释：** 证书内容。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The certificate of this HttpsDetail.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this HttpsDetail.

        **参数解释：** 证书内容。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param certificate: The certificate of this HttpsDetail.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        r"""Gets the private_key of this HttpsDetail.

        **参数解释：** 私钥内容。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The private_key of this HttpsDetail.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this HttpsDetail.

        **参数解释：** 私钥内容。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param private_key: The private_key of this HttpsDetail.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate_type(self):
        r"""Gets the certificate_type of this HttpsDetail.

        证书类型，0：自有证书，1：云托管证书，2：SCM证书。

        :return: The certificate_type of this HttpsDetail.
        :rtype: int
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        r"""Sets the certificate_type of this HttpsDetail.

        证书类型，0：自有证书，1：云托管证书，2：SCM证书。

        :param certificate_type: The certificate_type of this HttpsDetail.
        :type certificate_type: int
        """
        self._certificate_type = certificate_type

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this HttpsDetail.

        **参数解释：** 证书过期时间，Unix时间戳格式，单位为毫秒。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The expiration_time of this HttpsDetail.
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this HttpsDetail.

        **参数解释：** 证书过期时间，Unix时间戳格式，单位为毫秒。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param expiration_time: The expiration_time of this HttpsDetail.
        :type expiration_time: int
        """
        self._expiration_time = expiration_time

    @property
    def https_status(self):
        r"""Gets the https_status of this HttpsDetail.

        HTTPS证书是否启用，取值0：不启用；1：启用HTTPS加速并协议跟随回源；2：启用HTTPS加速并HTTP回源。

        :return: The https_status of this HttpsDetail.
        :rtype: int
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        r"""Sets the https_status of this HttpsDetail.

        HTTPS证书是否启用，取值0：不启用；1：启用HTTPS加速并协议跟随回源；2：启用HTTPS加速并HTTP回源。

        :param https_status: The https_status of this HttpsDetail.
        :type https_status: int
        """
        self._https_status = https_status

    @property
    def force_redirect_https(self):
        r"""Gets the force_redirect_https of this HttpsDetail.

        客户端请求是否强制重定向。1是，0否。（如果为2，表示强制跳转HTTP）

        :return: The force_redirect_https of this HttpsDetail.
        :rtype: int
        """
        return self._force_redirect_https

    @force_redirect_https.setter
    def force_redirect_https(self, force_redirect_https):
        r"""Sets the force_redirect_https of this HttpsDetail.

        客户端请求是否强制重定向。1是，0否。（如果为2，表示强制跳转HTTP）

        :param force_redirect_https: The force_redirect_https of this HttpsDetail.
        :type force_redirect_https: int
        """
        self._force_redirect_https = force_redirect_https

    @property
    def force_redirect_config(self):
        r"""Gets the force_redirect_config of this HttpsDetail.

        :return: The force_redirect_config of this HttpsDetail.
        :rtype: :class:`huaweicloudsdkcdn.v2.ForceRedirect`
        """
        return self._force_redirect_config

    @force_redirect_config.setter
    def force_redirect_config(self, force_redirect_config):
        r"""Sets the force_redirect_config of this HttpsDetail.

        :param force_redirect_config: The force_redirect_config of this HttpsDetail.
        :type force_redirect_config: :class:`huaweicloudsdkcdn.v2.ForceRedirect`
        """
        self._force_redirect_config = force_redirect_config

    @property
    def http2(self):
        r"""Gets the http2 of this HttpsDetail.

        是否使用HTTP2.0。（1是，0否。）

        :return: The http2 of this HttpsDetail.
        :rtype: int
        """
        return self._http2

    @http2.setter
    def http2(self, http2):
        r"""Sets the http2 of this HttpsDetail.

        是否使用HTTP2.0。（1是，0否。）

        :param http2: The http2 of this HttpsDetail.
        :type http2: int
        """
        self._http2 = http2

    @property
    def certificates(self):
        r"""Gets the certificates of this HttpsDetail.

        **参数解释：** 证书列表，配置双证书场景下包含国际证书和国密证书两项 **约束限制：** 不涉及

        :return: The certificates of this HttpsDetail.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.HttpsDetailCertificates`]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        r"""Sets the certificates of this HttpsDetail.

        **参数解释：** 证书列表，配置双证书场景下包含国际证书和国密证书两项 **约束限制：** 不涉及

        :param certificates: The certificates of this HttpsDetail.
        :type certificates: list[:class:`huaweicloudsdkcdn.v2.HttpsDetailCertificates`]
        """
        self._certificates = certificates

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
        if not isinstance(other, HttpsDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
