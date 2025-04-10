# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertificatesPutBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_source': 'int',
        'scm_certificate_id': 'str',
        'certificate_type': 'str',
        'certificate_name': 'str',
        'certificate_value': 'str',
        'private_key': 'str',
        'enc_certificate_value': 'str',
        'enc_private_key': 'str'
    }

    attribute_map = {
        'certificate_source': 'certificate_source',
        'scm_certificate_id': 'scm_certificate_id',
        'certificate_type': 'certificate_type',
        'certificate_name': 'certificate_name',
        'certificate_value': 'certificate_value',
        'private_key': 'private_key',
        'enc_certificate_value': 'enc_certificate_value',
        'enc_private_key': 'enc_private_key'
    }

    def __init__(self, certificate_source=None, scm_certificate_id=None, certificate_type=None, certificate_name=None, certificate_value=None, private_key=None, enc_certificate_value=None, enc_private_key=None):
        r"""CertificatesPutBody

        The model defined in huaweicloud sdk

        :param certificate_source: 证书来源，0：自有证书。2：SCM证书。
        :type certificate_source: int
        :param scm_certificate_id: SCM证书id
        :type scm_certificate_id: str
        :param certificate_type: 证书类型，server：国际证书；server_sm：国密证书。
        :type certificate_type: str
        :param certificate_name: 证书名字，长度限制为3-64字符。
        :type certificate_name: str
        :param certificate_value: HTTPS协议使用的证书内容。  &gt; PEM编码格式。
        :type certificate_value: str
        :param private_key: HTTPS协议使用的私钥。  &gt; PEM编码格式。
        :type private_key: str
        :param enc_certificate_value: 加密证书内容，证书类型为国密证书时必传。  &gt; PEM编码格式。
        :type enc_certificate_value: str
        :param enc_private_key: 加密私钥内容，证书类型为国密证书时必传。  &gt; PEM编码格式。
        :type enc_private_key: str
        """
        
        

        self._certificate_source = None
        self._scm_certificate_id = None
        self._certificate_type = None
        self._certificate_name = None
        self._certificate_value = None
        self._private_key = None
        self._enc_certificate_value = None
        self._enc_private_key = None
        self.discriminator = None

        if certificate_source is not None:
            self.certificate_source = certificate_source
        if scm_certificate_id is not None:
            self.scm_certificate_id = scm_certificate_id
        self.certificate_type = certificate_type
        self.certificate_name = certificate_name
        self.certificate_value = certificate_value
        self.private_key = private_key
        if enc_certificate_value is not None:
            self.enc_certificate_value = enc_certificate_value
        if enc_private_key is not None:
            self.enc_private_key = enc_private_key

    @property
    def certificate_source(self):
        r"""Gets the certificate_source of this CertificatesPutBody.

        证书来源，0：自有证书。2：SCM证书。

        :return: The certificate_source of this CertificatesPutBody.
        :rtype: int
        """
        return self._certificate_source

    @certificate_source.setter
    def certificate_source(self, certificate_source):
        r"""Sets the certificate_source of this CertificatesPutBody.

        证书来源，0：自有证书。2：SCM证书。

        :param certificate_source: The certificate_source of this CertificatesPutBody.
        :type certificate_source: int
        """
        self._certificate_source = certificate_source

    @property
    def scm_certificate_id(self):
        r"""Gets the scm_certificate_id of this CertificatesPutBody.

        SCM证书id

        :return: The scm_certificate_id of this CertificatesPutBody.
        :rtype: str
        """
        return self._scm_certificate_id

    @scm_certificate_id.setter
    def scm_certificate_id(self, scm_certificate_id):
        r"""Sets the scm_certificate_id of this CertificatesPutBody.

        SCM证书id

        :param scm_certificate_id: The scm_certificate_id of this CertificatesPutBody.
        :type scm_certificate_id: str
        """
        self._scm_certificate_id = scm_certificate_id

    @property
    def certificate_type(self):
        r"""Gets the certificate_type of this CertificatesPutBody.

        证书类型，server：国际证书；server_sm：国密证书。

        :return: The certificate_type of this CertificatesPutBody.
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        r"""Sets the certificate_type of this CertificatesPutBody.

        证书类型，server：国际证书；server_sm：国密证书。

        :param certificate_type: The certificate_type of this CertificatesPutBody.
        :type certificate_type: str
        """
        self._certificate_type = certificate_type

    @property
    def certificate_name(self):
        r"""Gets the certificate_name of this CertificatesPutBody.

        证书名字，长度限制为3-64字符。

        :return: The certificate_name of this CertificatesPutBody.
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        r"""Sets the certificate_name of this CertificatesPutBody.

        证书名字，长度限制为3-64字符。

        :param certificate_name: The certificate_name of this CertificatesPutBody.
        :type certificate_name: str
        """
        self._certificate_name = certificate_name

    @property
    def certificate_value(self):
        r"""Gets the certificate_value of this CertificatesPutBody.

        HTTPS协议使用的证书内容。  > PEM编码格式。

        :return: The certificate_value of this CertificatesPutBody.
        :rtype: str
        """
        return self._certificate_value

    @certificate_value.setter
    def certificate_value(self, certificate_value):
        r"""Sets the certificate_value of this CertificatesPutBody.

        HTTPS协议使用的证书内容。  > PEM编码格式。

        :param certificate_value: The certificate_value of this CertificatesPutBody.
        :type certificate_value: str
        """
        self._certificate_value = certificate_value

    @property
    def private_key(self):
        r"""Gets the private_key of this CertificatesPutBody.

        HTTPS协议使用的私钥。  > PEM编码格式。

        :return: The private_key of this CertificatesPutBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this CertificatesPutBody.

        HTTPS协议使用的私钥。  > PEM编码格式。

        :param private_key: The private_key of this CertificatesPutBody.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def enc_certificate_value(self):
        r"""Gets the enc_certificate_value of this CertificatesPutBody.

        加密证书内容，证书类型为国密证书时必传。  > PEM编码格式。

        :return: The enc_certificate_value of this CertificatesPutBody.
        :rtype: str
        """
        return self._enc_certificate_value

    @enc_certificate_value.setter
    def enc_certificate_value(self, enc_certificate_value):
        r"""Sets the enc_certificate_value of this CertificatesPutBody.

        加密证书内容，证书类型为国密证书时必传。  > PEM编码格式。

        :param enc_certificate_value: The enc_certificate_value of this CertificatesPutBody.
        :type enc_certificate_value: str
        """
        self._enc_certificate_value = enc_certificate_value

    @property
    def enc_private_key(self):
        r"""Gets the enc_private_key of this CertificatesPutBody.

        加密私钥内容，证书类型为国密证书时必传。  > PEM编码格式。

        :return: The enc_private_key of this CertificatesPutBody.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        r"""Sets the enc_private_key of this CertificatesPutBody.

        加密私钥内容，证书类型为国密证书时必传。  > PEM编码格式。

        :param enc_private_key: The enc_private_key of this CertificatesPutBody.
        :type enc_private_key: str
        """
        self._enc_private_key = enc_private_key

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
        if not isinstance(other, CertificatesPutBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
