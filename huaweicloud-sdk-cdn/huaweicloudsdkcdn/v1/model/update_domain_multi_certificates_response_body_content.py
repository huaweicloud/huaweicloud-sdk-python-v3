# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainMultiCertificatesResponseBodyContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'https_switch': 'int',
        'access_origin_way': 'int',
        'force_redirect_https': 'int',
        'force_redirect_config': 'ForceRedirect',
        'http2': 'int',
        'cert_name': 'str',
        'certificate': 'str',
        'certificate_type': 'int',
        'expiration_time': 'int'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'https_switch': 'https_switch',
        'access_origin_way': 'access_origin_way',
        'force_redirect_https': 'force_redirect_https',
        'force_redirect_config': 'force_redirect_config',
        'http2': 'http2',
        'cert_name': 'cert_name',
        'certificate': 'certificate',
        'certificate_type': 'certificate_type',
        'expiration_time': 'expiration_time'
    }

    def __init__(self, domain_name=None, https_switch=None, access_origin_way=None, force_redirect_https=None, force_redirect_config=None, http2=None, cert_name=None, certificate=None, certificate_type=None, expiration_time=None):
        r"""UpdateDomainMultiCertificatesResponseBodyContent

        The model defined in huaweicloud sdk

        :param domain_name: 域名列表。
        :type domain_name: str
        :param https_switch: https开关(0：\&quot;关闭\&quot;；1：\&quot;设置证书\&quot;)。
        :type https_switch: int
        :param access_origin_way: 回源方式:1：\&quot;回源跟随\&quot;；2：\&quot;HTTP\&quot;(默认)，3：https（自建）。
        :type access_origin_way: int
        :param force_redirect_https: 强制跳转HTTPS（0：不强制；1：强制） 。
        :type force_redirect_https: int
        :param force_redirect_config: 
        :type force_redirect_config: :class:`huaweicloudsdkcdn.v1.ForceRedirect`
        :param http2: http2.0（0：关闭；1：开启）。
        :type http2: int
        :param cert_name: 证书名称。
        :type cert_name: str
        :param certificate: 证书内容。
        :type certificate: str
        :param certificate_type: 证书类型（0为自有证书 ， 1为托管证书）。
        :type certificate_type: int
        :param expiration_time: 证书过期时间。
        :type expiration_time: int
        """
        
        

        self._domain_name = None
        self._https_switch = None
        self._access_origin_way = None
        self._force_redirect_https = None
        self._force_redirect_config = None
        self._http2 = None
        self._cert_name = None
        self._certificate = None
        self._certificate_type = None
        self._expiration_time = None
        self.discriminator = None

        self.domain_name = domain_name
        if https_switch is not None:
            self.https_switch = https_switch
        if access_origin_way is not None:
            self.access_origin_way = access_origin_way
        if force_redirect_https is not None:
            self.force_redirect_https = force_redirect_https
        if force_redirect_config is not None:
            self.force_redirect_config = force_redirect_config
        if http2 is not None:
            self.http2 = http2
        if cert_name is not None:
            self.cert_name = cert_name
        if certificate is not None:
            self.certificate = certificate
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if expiration_time is not None:
            self.expiration_time = expiration_time

    @property
    def domain_name(self):
        r"""Gets the domain_name of this UpdateDomainMultiCertificatesResponseBodyContent.

        域名列表。

        :return: The domain_name of this UpdateDomainMultiCertificatesResponseBodyContent.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this UpdateDomainMultiCertificatesResponseBodyContent.

        域名列表。

        :param domain_name: The domain_name of this UpdateDomainMultiCertificatesResponseBodyContent.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def https_switch(self):
        r"""Gets the https_switch of this UpdateDomainMultiCertificatesResponseBodyContent.

        https开关(0：\"关闭\"；1：\"设置证书\")。

        :return: The https_switch of this UpdateDomainMultiCertificatesResponseBodyContent.
        :rtype: int
        """
        return self._https_switch

    @https_switch.setter
    def https_switch(self, https_switch):
        r"""Sets the https_switch of this UpdateDomainMultiCertificatesResponseBodyContent.

        https开关(0：\"关闭\"；1：\"设置证书\")。

        :param https_switch: The https_switch of this UpdateDomainMultiCertificatesResponseBodyContent.
        :type https_switch: int
        """
        self._https_switch = https_switch

    @property
    def access_origin_way(self):
        r"""Gets the access_origin_way of this UpdateDomainMultiCertificatesResponseBodyContent.

        回源方式:1：\"回源跟随\"；2：\"HTTP\"(默认)，3：https（自建）。

        :return: The access_origin_way of this UpdateDomainMultiCertificatesResponseBodyContent.
        :rtype: int
        """
        return self._access_origin_way

    @access_origin_way.setter
    def access_origin_way(self, access_origin_way):
        r"""Sets the access_origin_way of this UpdateDomainMultiCertificatesResponseBodyContent.

        回源方式:1：\"回源跟随\"；2：\"HTTP\"(默认)，3：https（自建）。

        :param access_origin_way: The access_origin_way of this UpdateDomainMultiCertificatesResponseBodyContent.
        :type access_origin_way: int
        """
        self._access_origin_way = access_origin_way

    @property
    def force_redirect_https(self):
        r"""Gets the force_redirect_https of this UpdateDomainMultiCertificatesResponseBodyContent.

        强制跳转HTTPS（0：不强制；1：强制） 。

        :return: The force_redirect_https of this UpdateDomainMultiCertificatesResponseBodyContent.
        :rtype: int
        """
        return self._force_redirect_https

    @force_redirect_https.setter
    def force_redirect_https(self, force_redirect_https):
        r"""Sets the force_redirect_https of this UpdateDomainMultiCertificatesResponseBodyContent.

        强制跳转HTTPS（0：不强制；1：强制） 。

        :param force_redirect_https: The force_redirect_https of this UpdateDomainMultiCertificatesResponseBodyContent.
        :type force_redirect_https: int
        """
        self._force_redirect_https = force_redirect_https

    @property
    def force_redirect_config(self):
        r"""Gets the force_redirect_config of this UpdateDomainMultiCertificatesResponseBodyContent.

        :return: The force_redirect_config of this UpdateDomainMultiCertificatesResponseBodyContent.
        :rtype: :class:`huaweicloudsdkcdn.v1.ForceRedirect`
        """
        return self._force_redirect_config

    @force_redirect_config.setter
    def force_redirect_config(self, force_redirect_config):
        r"""Sets the force_redirect_config of this UpdateDomainMultiCertificatesResponseBodyContent.

        :param force_redirect_config: The force_redirect_config of this UpdateDomainMultiCertificatesResponseBodyContent.
        :type force_redirect_config: :class:`huaweicloudsdkcdn.v1.ForceRedirect`
        """
        self._force_redirect_config = force_redirect_config

    @property
    def http2(self):
        r"""Gets the http2 of this UpdateDomainMultiCertificatesResponseBodyContent.

        http2.0（0：关闭；1：开启）。

        :return: The http2 of this UpdateDomainMultiCertificatesResponseBodyContent.
        :rtype: int
        """
        return self._http2

    @http2.setter
    def http2(self, http2):
        r"""Sets the http2 of this UpdateDomainMultiCertificatesResponseBodyContent.

        http2.0（0：关闭；1：开启）。

        :param http2: The http2 of this UpdateDomainMultiCertificatesResponseBodyContent.
        :type http2: int
        """
        self._http2 = http2

    @property
    def cert_name(self):
        r"""Gets the cert_name of this UpdateDomainMultiCertificatesResponseBodyContent.

        证书名称。

        :return: The cert_name of this UpdateDomainMultiCertificatesResponseBodyContent.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this UpdateDomainMultiCertificatesResponseBodyContent.

        证书名称。

        :param cert_name: The cert_name of this UpdateDomainMultiCertificatesResponseBodyContent.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def certificate(self):
        r"""Gets the certificate of this UpdateDomainMultiCertificatesResponseBodyContent.

        证书内容。

        :return: The certificate of this UpdateDomainMultiCertificatesResponseBodyContent.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this UpdateDomainMultiCertificatesResponseBodyContent.

        证书内容。

        :param certificate: The certificate of this UpdateDomainMultiCertificatesResponseBodyContent.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def certificate_type(self):
        r"""Gets the certificate_type of this UpdateDomainMultiCertificatesResponseBodyContent.

        证书类型（0为自有证书 ， 1为托管证书）。

        :return: The certificate_type of this UpdateDomainMultiCertificatesResponseBodyContent.
        :rtype: int
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        r"""Sets the certificate_type of this UpdateDomainMultiCertificatesResponseBodyContent.

        证书类型（0为自有证书 ， 1为托管证书）。

        :param certificate_type: The certificate_type of this UpdateDomainMultiCertificatesResponseBodyContent.
        :type certificate_type: int
        """
        self._certificate_type = certificate_type

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this UpdateDomainMultiCertificatesResponseBodyContent.

        证书过期时间。

        :return: The expiration_time of this UpdateDomainMultiCertificatesResponseBodyContent.
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this UpdateDomainMultiCertificatesResponseBodyContent.

        证书过期时间。

        :param expiration_time: The expiration_time of this UpdateDomainMultiCertificatesResponseBodyContent.
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
        if not isinstance(other, UpdateDomainMultiCertificatesResponseBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
