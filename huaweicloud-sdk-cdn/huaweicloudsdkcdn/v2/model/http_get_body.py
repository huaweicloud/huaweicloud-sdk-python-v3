# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpGetBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'https_status': 'str',
        'certificate_type': 'str',
        'certificate_source': 'int',
        'certificate_name': 'str',
        'certificate_value': 'str',
        'expire_time': 'int',
        'enc_certificate_value': 'str',
        'certificates': 'list[CertificatesGetBody]',
        'http2_status': 'str',
        'tls_version': 'str',
        'ocsp_stapling_status': 'str'
    }

    attribute_map = {
        'https_status': 'https_status',
        'certificate_type': 'certificate_type',
        'certificate_source': 'certificate_source',
        'certificate_name': 'certificate_name',
        'certificate_value': 'certificate_value',
        'expire_time': 'expire_time',
        'enc_certificate_value': 'enc_certificate_value',
        'certificates': 'certificates',
        'http2_status': 'http2_status',
        'tls_version': 'tls_version',
        'ocsp_stapling_status': 'ocsp_stapling_status'
    }

    def __init__(self, https_status=None, certificate_type=None, certificate_source=None, certificate_name=None, certificate_value=None, expire_time=None, enc_certificate_value=None, certificates=None, http2_status=None, tls_version=None, ocsp_stapling_status=None):
        """HttpGetBody

        The model defined in huaweicloud sdk

        :param https_status: HTTPS证书是否启用，on：开启，off：关闭。
        :type https_status: str
        :param certificate_type: 证书类型。server：国际证书；server_sm：国密证书。
        :type certificate_type: str
        :param certificate_source: 证书来源，1：华为云托管证书，0：自有证书。
        :type certificate_source: int
        :param certificate_name: 证书名字。
        :type certificate_name: str
        :param certificate_value: HTTPS协议使用的证书内容，PEM编码格式。
        :type certificate_value: str
        :param expire_time: 证书过期时间。  &gt; UTC时间。
        :type expire_time: int
        :param enc_certificate_value: 国密证书加密证书内容，PEM编码格式。
        :type enc_certificate_value: str
        :param certificates: 
        :type certificates: list[:class:`huaweicloudsdkcdn.v2.CertificatesGetBody`]
        :param http2_status: 是否使用HTTP2.0，on：是，off：否。
        :type http2_status: str
        :param tls_version: 传输层安全性协议。
        :type tls_version: str
        :param ocsp_stapling_status: 是否开启ocsp stapling,on：是，off：否。
        :type ocsp_stapling_status: str
        """
        
        

        self._https_status = None
        self._certificate_type = None
        self._certificate_source = None
        self._certificate_name = None
        self._certificate_value = None
        self._expire_time = None
        self._enc_certificate_value = None
        self._certificates = None
        self._http2_status = None
        self._tls_version = None
        self._ocsp_stapling_status = None
        self.discriminator = None

        if https_status is not None:
            self.https_status = https_status
        if certificate_type is not None:
            self.certificate_type = certificate_type
        if certificate_source is not None:
            self.certificate_source = certificate_source
        if certificate_name is not None:
            self.certificate_name = certificate_name
        if certificate_value is not None:
            self.certificate_value = certificate_value
        if expire_time is not None:
            self.expire_time = expire_time
        if enc_certificate_value is not None:
            self.enc_certificate_value = enc_certificate_value
        if certificates is not None:
            self.certificates = certificates
        if http2_status is not None:
            self.http2_status = http2_status
        if tls_version is not None:
            self.tls_version = tls_version
        if ocsp_stapling_status is not None:
            self.ocsp_stapling_status = ocsp_stapling_status

    @property
    def https_status(self):
        """Gets the https_status of this HttpGetBody.

        HTTPS证书是否启用，on：开启，off：关闭。

        :return: The https_status of this HttpGetBody.
        :rtype: str
        """
        return self._https_status

    @https_status.setter
    def https_status(self, https_status):
        """Sets the https_status of this HttpGetBody.

        HTTPS证书是否启用，on：开启，off：关闭。

        :param https_status: The https_status of this HttpGetBody.
        :type https_status: str
        """
        self._https_status = https_status

    @property
    def certificate_type(self):
        """Gets the certificate_type of this HttpGetBody.

        证书类型。server：国际证书；server_sm：国密证书。

        :return: The certificate_type of this HttpGetBody.
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this HttpGetBody.

        证书类型。server：国际证书；server_sm：国密证书。

        :param certificate_type: The certificate_type of this HttpGetBody.
        :type certificate_type: str
        """
        self._certificate_type = certificate_type

    @property
    def certificate_source(self):
        """Gets the certificate_source of this HttpGetBody.

        证书来源，1：华为云托管证书，0：自有证书。

        :return: The certificate_source of this HttpGetBody.
        :rtype: int
        """
        return self._certificate_source

    @certificate_source.setter
    def certificate_source(self, certificate_source):
        """Sets the certificate_source of this HttpGetBody.

        证书来源，1：华为云托管证书，0：自有证书。

        :param certificate_source: The certificate_source of this HttpGetBody.
        :type certificate_source: int
        """
        self._certificate_source = certificate_source

    @property
    def certificate_name(self):
        """Gets the certificate_name of this HttpGetBody.

        证书名字。

        :return: The certificate_name of this HttpGetBody.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """Sets the certificate_name of this HttpGetBody.

        证书名字。

        :param certificate_name: The certificate_name of this HttpGetBody.
        :type certificate_name: str
        """
        self._certificate_name = certificate_name

    @property
    def certificate_value(self):
        """Gets the certificate_value of this HttpGetBody.

        HTTPS协议使用的证书内容，PEM编码格式。

        :return: The certificate_value of this HttpGetBody.
        :rtype: str
        """
        return self._certificate_value

    @certificate_value.setter
    def certificate_value(self, certificate_value):
        """Sets the certificate_value of this HttpGetBody.

        HTTPS协议使用的证书内容，PEM编码格式。

        :param certificate_value: The certificate_value of this HttpGetBody.
        :type certificate_value: str
        """
        self._certificate_value = certificate_value

    @property
    def expire_time(self):
        """Gets the expire_time of this HttpGetBody.

        证书过期时间。  > UTC时间。

        :return: The expire_time of this HttpGetBody.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this HttpGetBody.

        证书过期时间。  > UTC时间。

        :param expire_time: The expire_time of this HttpGetBody.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def enc_certificate_value(self):
        """Gets the enc_certificate_value of this HttpGetBody.

        国密证书加密证书内容，PEM编码格式。

        :return: The enc_certificate_value of this HttpGetBody.
        :rtype: str
        """
        return self._enc_certificate_value

    @enc_certificate_value.setter
    def enc_certificate_value(self, enc_certificate_value):
        """Sets the enc_certificate_value of this HttpGetBody.

        国密证书加密证书内容，PEM编码格式。

        :param enc_certificate_value: The enc_certificate_value of this HttpGetBody.
        :type enc_certificate_value: str
        """
        self._enc_certificate_value = enc_certificate_value

    @property
    def certificates(self):
        """Gets the certificates of this HttpGetBody.

        :return: The certificates of this HttpGetBody.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.CertificatesGetBody`]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        """Sets the certificates of this HttpGetBody.

        :param certificates: The certificates of this HttpGetBody.
        :type certificates: list[:class:`huaweicloudsdkcdn.v2.CertificatesGetBody`]
        """
        self._certificates = certificates

    @property
    def http2_status(self):
        """Gets the http2_status of this HttpGetBody.

        是否使用HTTP2.0，on：是，off：否。

        :return: The http2_status of this HttpGetBody.
        :rtype: str
        """
        return self._http2_status

    @http2_status.setter
    def http2_status(self, http2_status):
        """Sets the http2_status of this HttpGetBody.

        是否使用HTTP2.0，on：是，off：否。

        :param http2_status: The http2_status of this HttpGetBody.
        :type http2_status: str
        """
        self._http2_status = http2_status

    @property
    def tls_version(self):
        """Gets the tls_version of this HttpGetBody.

        传输层安全性协议。

        :return: The tls_version of this HttpGetBody.
        :rtype: str
        """
        return self._tls_version

    @tls_version.setter
    def tls_version(self, tls_version):
        """Sets the tls_version of this HttpGetBody.

        传输层安全性协议。

        :param tls_version: The tls_version of this HttpGetBody.
        :type tls_version: str
        """
        self._tls_version = tls_version

    @property
    def ocsp_stapling_status(self):
        """Gets the ocsp_stapling_status of this HttpGetBody.

        是否开启ocsp stapling,on：是，off：否。

        :return: The ocsp_stapling_status of this HttpGetBody.
        :rtype: str
        """
        return self._ocsp_stapling_status

    @ocsp_stapling_status.setter
    def ocsp_stapling_status(self, ocsp_stapling_status):
        """Sets the ocsp_stapling_status of this HttpGetBody.

        是否开启ocsp stapling,on：是，off：否。

        :param ocsp_stapling_status: The ocsp_stapling_status of this HttpGetBody.
        :type ocsp_stapling_status: str
        """
        self._ocsp_stapling_status = ocsp_stapling_status

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
        if not isinstance(other, HttpGetBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
