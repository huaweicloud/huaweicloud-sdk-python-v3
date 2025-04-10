# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TlsCertificateInfo:

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
        'certificate': 'str',
        'certificate_key': 'str'
    }

    attribute_map = {
        'source': 'source',
        'cert_name': 'cert_name',
        'cert_id': 'cert_id',
        'certificate': 'certificate',
        'certificate_key': 'certificate_key'
    }

    def __init__(self, source=None, cert_name=None, cert_id=None, certificate=None, certificate_key=None):
        r"""TlsCertificateInfo

        The model defined in huaweicloud sdk

        :param source: 证书来源， 可选,  scm: 云证书管理服务，user：默认，用户自有
        :type source: str
        :param cert_name: SCM证书名， 证书来源为scm时可选
        :type cert_name: str
        :param cert_id: SCM证书ID, 证书来源为scm时必选
        :type cert_id: str
        :param certificate: 证书内容，证书来源为user时必选
        :type certificate: str
        :param certificate_key: 私钥内容，证书来源为user时必选
        :type certificate_key: str
        """
        
        

        self._source = None
        self._cert_name = None
        self._cert_id = None
        self._certificate = None
        self._certificate_key = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if cert_name is not None:
            self.cert_name = cert_name
        if cert_id is not None:
            self.cert_id = cert_id
        if certificate is not None:
            self.certificate = certificate
        if certificate_key is not None:
            self.certificate_key = certificate_key

    @property
    def source(self):
        r"""Gets the source of this TlsCertificateInfo.

        证书来源， 可选,  scm: 云证书管理服务，user：默认，用户自有

        :return: The source of this TlsCertificateInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this TlsCertificateInfo.

        证书来源， 可选,  scm: 云证书管理服务，user：默认，用户自有

        :param source: The source of this TlsCertificateInfo.
        :type source: str
        """
        self._source = source

    @property
    def cert_name(self):
        r"""Gets the cert_name of this TlsCertificateInfo.

        SCM证书名， 证书来源为scm时可选

        :return: The cert_name of this TlsCertificateInfo.
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        r"""Sets the cert_name of this TlsCertificateInfo.

        SCM证书名， 证书来源为scm时可选

        :param cert_name: The cert_name of this TlsCertificateInfo.
        :type cert_name: str
        """
        self._cert_name = cert_name

    @property
    def cert_id(self):
        r"""Gets the cert_id of this TlsCertificateInfo.

        SCM证书ID, 证书来源为scm时必选

        :return: The cert_id of this TlsCertificateInfo.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        r"""Sets the cert_id of this TlsCertificateInfo.

        SCM证书ID, 证书来源为scm时必选

        :param cert_id: The cert_id of this TlsCertificateInfo.
        :type cert_id: str
        """
        self._cert_id = cert_id

    @property
    def certificate(self):
        r"""Gets the certificate of this TlsCertificateInfo.

        证书内容，证书来源为user时必选

        :return: The certificate of this TlsCertificateInfo.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this TlsCertificateInfo.

        证书内容，证书来源为user时必选

        :param certificate: The certificate of this TlsCertificateInfo.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def certificate_key(self):
        r"""Gets the certificate_key of this TlsCertificateInfo.

        私钥内容，证书来源为user时必选

        :return: The certificate_key of this TlsCertificateInfo.
        :rtype: str
        """
        return self._certificate_key

    @certificate_key.setter
    def certificate_key(self, certificate_key):
        r"""Sets the certificate_key of this TlsCertificateInfo.

        私钥内容，证书来源为user时必选

        :param certificate_key: The certificate_key of this TlsCertificateInfo.
        :type certificate_key: str
        """
        self._certificate_key = certificate_key

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
        if not isinstance(other, TlsCertificateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
