# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainHttpsCertInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_format': 'str',
        'certificate': 'str',
        'certificate_key': 'str',
        'force_redirect': 'bool',
        'gm_certificate': 'GmCertificateInfo',
        'tls_certificate': 'TlsCertificateInfo'
    }

    attribute_map = {
        'certificate_format': 'certificate_format',
        'certificate': 'certificate',
        'certificate_key': 'certificate_key',
        'force_redirect': 'force_redirect',
        'gm_certificate': 'gm_certificate',
        'tls_certificate': 'tls_certificate'
    }

    def __init__(self, certificate_format=None, certificate=None, certificate_key=None, force_redirect=None, gm_certificate=None, tls_certificate=None):
        r"""DomainHttpsCertInfo

        The model defined in huaweicloud sdk

        :param certificate_format: 证书格式，默认为PEM，当前只支持PEM格式
        :type certificate_format: str
        :param certificate: 证书内容
        :type certificate: str
        :param certificate_key: 私钥内容
        :type certificate_key: str
        :param force_redirect: 是否开启重定向，默认false
        :type force_redirect: bool
        :param gm_certificate: 
        :type gm_certificate: :class:`huaweicloudsdklive.v1.GmCertificateInfo`
        :param tls_certificate: 
        :type tls_certificate: :class:`huaweicloudsdklive.v1.TlsCertificateInfo`
        """
        
        

        self._certificate_format = None
        self._certificate = None
        self._certificate_key = None
        self._force_redirect = None
        self._gm_certificate = None
        self._tls_certificate = None
        self.discriminator = None

        if certificate_format is not None:
            self.certificate_format = certificate_format
        if certificate is not None:
            self.certificate = certificate
        if certificate_key is not None:
            self.certificate_key = certificate_key
        if force_redirect is not None:
            self.force_redirect = force_redirect
        if gm_certificate is not None:
            self.gm_certificate = gm_certificate
        if tls_certificate is not None:
            self.tls_certificate = tls_certificate

    @property
    def certificate_format(self):
        r"""Gets the certificate_format of this DomainHttpsCertInfo.

        证书格式，默认为PEM，当前只支持PEM格式

        :return: The certificate_format of this DomainHttpsCertInfo.
        :rtype: str
        """
        return self._certificate_format

    @certificate_format.setter
    def certificate_format(self, certificate_format):
        r"""Sets the certificate_format of this DomainHttpsCertInfo.

        证书格式，默认为PEM，当前只支持PEM格式

        :param certificate_format: The certificate_format of this DomainHttpsCertInfo.
        :type certificate_format: str
        """
        self._certificate_format = certificate_format

    @property
    def certificate(self):
        r"""Gets the certificate of this DomainHttpsCertInfo.

        证书内容

        :return: The certificate of this DomainHttpsCertInfo.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this DomainHttpsCertInfo.

        证书内容

        :param certificate: The certificate of this DomainHttpsCertInfo.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def certificate_key(self):
        r"""Gets the certificate_key of this DomainHttpsCertInfo.

        私钥内容

        :return: The certificate_key of this DomainHttpsCertInfo.
        :rtype: str
        """
        return self._certificate_key

    @certificate_key.setter
    def certificate_key(self, certificate_key):
        r"""Sets the certificate_key of this DomainHttpsCertInfo.

        私钥内容

        :param certificate_key: The certificate_key of this DomainHttpsCertInfo.
        :type certificate_key: str
        """
        self._certificate_key = certificate_key

    @property
    def force_redirect(self):
        r"""Gets the force_redirect of this DomainHttpsCertInfo.

        是否开启重定向，默认false

        :return: The force_redirect of this DomainHttpsCertInfo.
        :rtype: bool
        """
        return self._force_redirect

    @force_redirect.setter
    def force_redirect(self, force_redirect):
        r"""Sets the force_redirect of this DomainHttpsCertInfo.

        是否开启重定向，默认false

        :param force_redirect: The force_redirect of this DomainHttpsCertInfo.
        :type force_redirect: bool
        """
        self._force_redirect = force_redirect

    @property
    def gm_certificate(self):
        r"""Gets the gm_certificate of this DomainHttpsCertInfo.

        :return: The gm_certificate of this DomainHttpsCertInfo.
        :rtype: :class:`huaweicloudsdklive.v1.GmCertificateInfo`
        """
        return self._gm_certificate

    @gm_certificate.setter
    def gm_certificate(self, gm_certificate):
        r"""Sets the gm_certificate of this DomainHttpsCertInfo.

        :param gm_certificate: The gm_certificate of this DomainHttpsCertInfo.
        :type gm_certificate: :class:`huaweicloudsdklive.v1.GmCertificateInfo`
        """
        self._gm_certificate = gm_certificate

    @property
    def tls_certificate(self):
        r"""Gets the tls_certificate of this DomainHttpsCertInfo.

        :return: The tls_certificate of this DomainHttpsCertInfo.
        :rtype: :class:`huaweicloudsdklive.v1.TlsCertificateInfo`
        """
        return self._tls_certificate

    @tls_certificate.setter
    def tls_certificate(self, tls_certificate):
        r"""Sets the tls_certificate of this DomainHttpsCertInfo.

        :param tls_certificate: The tls_certificate of this DomainHttpsCertInfo.
        :type tls_certificate: :class:`huaweicloudsdklive.v1.TlsCertificateInfo`
        """
        self._tls_certificate = tls_certificate

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
        if not isinstance(other, DomainHttpsCertInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
