# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GmCertificateInfo:

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
        'cert_name': 'str',
        'cert_id': 'str',
        'sign_certificate': 'str',
        'sign_certificate_key': 'str',
        'enc_certificate': 'str',
        'enc_certificate_key': 'str'
    }

    attribute_map = {
        'source': 'source',
        'cert_name': 'cert_name',
        'cert_id': 'cert_id',
        'sign_certificate': 'sign_certificate',
        'sign_certificate_key': 'sign_certificate_key',
        'enc_certificate': 'enc_certificate',
        'enc_certificate_key': 'enc_certificate_key'
    }

    def __init__(self, source=None, cert_name=None, cert_id=None, sign_certificate=None, sign_certificate_key=None, enc_certificate=None, enc_certificate_key=None):
        r"""GmCertificateInfo

        The model defined in huaweicloud sdk

        :param source: 证书来源， 可选,  scm: 云证书管理服务，user：默认，用户自有
        :type source: str
        :param cert_name: SCM证书名， 可选
        :type cert_name: str
        :param cert_id: SCM证书ID, 证书来源为scm时必选
        :type cert_id: str
        :param sign_certificate: 国密签名证书内容
        :type sign_certificate: str
        :param sign_certificate_key: 国密签名私钥内容
        :type sign_certificate_key: str
        :param enc_certificate: 国密加密证书内容
        :type enc_certificate: str
        :param enc_certificate_key: 国密加密私钥内容
        :type enc_certificate_key: str
        """
        
        

        self._source = None
        self._cert_name = None
        self._cert_id = None
        self._sign_certificate = None
        self._sign_certificate_key = None
        self._enc_certificate = None
        self._enc_certificate_key = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if cert_name is not None:
            self.cert_name = cert_name
        if cert_id is not None:
            self.cert_id = cert_id
        if sign_certificate is not None:
            self.sign_certificate = sign_certificate
        if sign_certificate_key is not None:
            self.sign_certificate_key = sign_certificate_key
        if enc_certificate is not None:
            self.enc_certificate = enc_certificate
        if enc_certificate_key is not None:
            self.enc_certificate_key = enc_certificate_key

    @property
    def source(self):
        r"""Gets the source of this GmCertificateInfo.

        证书来源， 可选,  scm: 云证书管理服务，user：默认，用户自有

        :return: The source of this GmCertificateInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this GmCertificateInfo.

        证书来源， 可选,  scm: 云证书管理服务，user：默认，用户自有

        :param source: The source of this GmCertificateInfo.
        :type source: str
        """
        self._source = source

    @property
    def cert_name(self):
        r"""Gets the cert_name of this GmCertificateInfo.

        SCM证书名， 可选

        :return: The cert_name of this GmCertificateInfo.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this GmCertificateInfo.

        SCM证书名， 可选

        :param cert_name: The cert_name of this GmCertificateInfo.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def cert_id(self):
        r"""Gets the cert_id of this GmCertificateInfo.

        SCM证书ID, 证书来源为scm时必选

        :return: The cert_id of this GmCertificateInfo.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        r"""Sets the cert_id of this GmCertificateInfo.

        SCM证书ID, 证书来源为scm时必选

        :param cert_id: The cert_id of this GmCertificateInfo.
        :type cert_id: str
        """
        self._cert_id = cert_id

    @property
    def sign_certificate(self):
        r"""Gets the sign_certificate of this GmCertificateInfo.

        国密签名证书内容

        :return: The sign_certificate of this GmCertificateInfo.
        :rtype: str
        """
        return self._sign_certificate

    @sign_certificate.setter
    def sign_certificate(self, sign_certificate):
        r"""Sets the sign_certificate of this GmCertificateInfo.

        国密签名证书内容

        :param sign_certificate: The sign_certificate of this GmCertificateInfo.
        :type sign_certificate: str
        """
        self._sign_certificate = sign_certificate

    @property
    def sign_certificate_key(self):
        r"""Gets the sign_certificate_key of this GmCertificateInfo.

        国密签名私钥内容

        :return: The sign_certificate_key of this GmCertificateInfo.
        :rtype: str
        """
        return self._sign_certificate_key

    @sign_certificate_key.setter
    def sign_certificate_key(self, sign_certificate_key):
        r"""Sets the sign_certificate_key of this GmCertificateInfo.

        国密签名私钥内容

        :param sign_certificate_key: The sign_certificate_key of this GmCertificateInfo.
        :type sign_certificate_key: str
        """
        self._sign_certificate_key = sign_certificate_key

    @property
    def enc_certificate(self):
        r"""Gets the enc_certificate of this GmCertificateInfo.

        国密加密证书内容

        :return: The enc_certificate of this GmCertificateInfo.
        :rtype: str
        """
        return self._enc_certificate

    @enc_certificate.setter
    def enc_certificate(self, enc_certificate):
        r"""Sets the enc_certificate of this GmCertificateInfo.

        国密加密证书内容

        :param enc_certificate: The enc_certificate of this GmCertificateInfo.
        :type enc_certificate: str
        """
        self._enc_certificate = enc_certificate

    @property
    def enc_certificate_key(self):
        r"""Gets the enc_certificate_key of this GmCertificateInfo.

        国密加密私钥内容

        :return: The enc_certificate_key of this GmCertificateInfo.
        :rtype: str
        """
        return self._enc_certificate_key

    @enc_certificate_key.setter
    def enc_certificate_key(self, enc_certificate_key):
        r"""Sets the enc_certificate_key of this GmCertificateInfo.

        国密加密私钥内容

        :param enc_certificate_key: The enc_certificate_key of this GmCertificateInfo.
        :type enc_certificate_key: str
        """
        self._enc_certificate_key = enc_certificate_key

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
        if not isinstance(other, GmCertificateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
