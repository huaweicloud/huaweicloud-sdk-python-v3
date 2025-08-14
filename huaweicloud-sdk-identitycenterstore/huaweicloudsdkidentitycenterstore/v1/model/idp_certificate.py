# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdpCertificate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_id': 'str',
        'issuer_name': 'str',
        'not_after': 'float',
        'not_before': 'float',
        'public_key': 'str',
        'serial_number': 'float',
        'serial_number_string': 'str',
        'signature_algorithm_name': 'str',
        'subject_name': 'str',
        'version': 'float',
        'x509_certificate_in_pem': 'str'
    }

    attribute_map = {
        'certificate_id': 'certificate_id',
        'issuer_name': 'issuer_name',
        'not_after': 'not_after',
        'not_before': 'not_before',
        'public_key': 'public_key',
        'serial_number': 'serial_number',
        'serial_number_string': 'serial_number_string',
        'signature_algorithm_name': 'signature_algorithm_name',
        'subject_name': 'subject_name',
        'version': 'version',
        'x509_certificate_in_pem': 'x509_Certificate_in_pem'
    }

    def __init__(self, certificate_id=None, issuer_name=None, not_after=None, not_before=None, public_key=None, serial_number=None, serial_number_string=None, signature_algorithm_name=None, subject_name=None, version=None, x509_certificate_in_pem=None):
        r"""IdpCertificate

        The model defined in huaweicloud sdk

        :param certificate_id: 证书全局唯一标识符（ID）
        :type certificate_id: str
        :param issuer_name: 身份提供商签发者
        :type issuer_name: str
        :param not_after: 证书有效期
        :type not_after: float
        :param not_before: 证书有效期
        :type not_before: float
        :param public_key: 证书公钥
        :type public_key: str
        :param serial_number: 证书序列号
        :type serial_number: float
        :param serial_number_string: 证书序列号文本
        :type serial_number_string: str
        :param signature_algorithm_name: 签名算法
        :type signature_algorithm_name: str
        :param subject_name: Subject
        :type subject_name: str
        :param version: 版本
        :type version: float
        :param x509_certificate_in_pem: x509格式证书
        :type x509_certificate_in_pem: str
        """
        
        

        self._certificate_id = None
        self._issuer_name = None
        self._not_after = None
        self._not_before = None
        self._public_key = None
        self._serial_number = None
        self._serial_number_string = None
        self._signature_algorithm_name = None
        self._subject_name = None
        self._version = None
        self._x509_certificate_in_pem = None
        self.discriminator = None

        self.certificate_id = certificate_id
        self.issuer_name = issuer_name
        self.not_after = not_after
        self.not_before = not_before
        self.public_key = public_key
        self.serial_number = serial_number
        self.serial_number_string = serial_number_string
        self.signature_algorithm_name = signature_algorithm_name
        self.subject_name = subject_name
        self.version = version
        self.x509_certificate_in_pem = x509_certificate_in_pem

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this IdpCertificate.

        证书全局唯一标识符（ID）

        :return: The certificate_id of this IdpCertificate.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this IdpCertificate.

        证书全局唯一标识符（ID）

        :param certificate_id: The certificate_id of this IdpCertificate.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def issuer_name(self):
        r"""Gets the issuer_name of this IdpCertificate.

        身份提供商签发者

        :return: The issuer_name of this IdpCertificate.
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        r"""Sets the issuer_name of this IdpCertificate.

        身份提供商签发者

        :param issuer_name: The issuer_name of this IdpCertificate.
        :type issuer_name: str
        """
        self._issuer_name = issuer_name

    @property
    def not_after(self):
        r"""Gets the not_after of this IdpCertificate.

        证书有效期

        :return: The not_after of this IdpCertificate.
        :rtype: float
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        r"""Sets the not_after of this IdpCertificate.

        证书有效期

        :param not_after: The not_after of this IdpCertificate.
        :type not_after: float
        """
        self._not_after = not_after

    @property
    def not_before(self):
        r"""Gets the not_before of this IdpCertificate.

        证书有效期

        :return: The not_before of this IdpCertificate.
        :rtype: float
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        r"""Sets the not_before of this IdpCertificate.

        证书有效期

        :param not_before: The not_before of this IdpCertificate.
        :type not_before: float
        """
        self._not_before = not_before

    @property
    def public_key(self):
        r"""Gets the public_key of this IdpCertificate.

        证书公钥

        :return: The public_key of this IdpCertificate.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        r"""Sets the public_key of this IdpCertificate.

        证书公钥

        :param public_key: The public_key of this IdpCertificate.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def serial_number(self):
        r"""Gets the serial_number of this IdpCertificate.

        证书序列号

        :return: The serial_number of this IdpCertificate.
        :rtype: float
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this IdpCertificate.

        证书序列号

        :param serial_number: The serial_number of this IdpCertificate.
        :type serial_number: float
        """
        self._serial_number = serial_number

    @property
    def serial_number_string(self):
        r"""Gets the serial_number_string of this IdpCertificate.

        证书序列号文本

        :return: The serial_number_string of this IdpCertificate.
        :rtype: str
        """
        return self._serial_number_string

    @serial_number_string.setter
    def serial_number_string(self, serial_number_string):
        r"""Sets the serial_number_string of this IdpCertificate.

        证书序列号文本

        :param serial_number_string: The serial_number_string of this IdpCertificate.
        :type serial_number_string: str
        """
        self._serial_number_string = serial_number_string

    @property
    def signature_algorithm_name(self):
        r"""Gets the signature_algorithm_name of this IdpCertificate.

        签名算法

        :return: The signature_algorithm_name of this IdpCertificate.
        :rtype: str
        """
        return self._signature_algorithm_name

    @signature_algorithm_name.setter
    def signature_algorithm_name(self, signature_algorithm_name):
        r"""Sets the signature_algorithm_name of this IdpCertificate.

        签名算法

        :param signature_algorithm_name: The signature_algorithm_name of this IdpCertificate.
        :type signature_algorithm_name: str
        """
        self._signature_algorithm_name = signature_algorithm_name

    @property
    def subject_name(self):
        r"""Gets the subject_name of this IdpCertificate.

        Subject

        :return: The subject_name of this IdpCertificate.
        :rtype: str
        """
        return self._subject_name

    @subject_name.setter
    def subject_name(self, subject_name):
        r"""Sets the subject_name of this IdpCertificate.

        Subject

        :param subject_name: The subject_name of this IdpCertificate.
        :type subject_name: str
        """
        self._subject_name = subject_name

    @property
    def version(self):
        r"""Gets the version of this IdpCertificate.

        版本

        :return: The version of this IdpCertificate.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this IdpCertificate.

        版本

        :param version: The version of this IdpCertificate.
        :type version: float
        """
        self._version = version

    @property
    def x509_certificate_in_pem(self):
        r"""Gets the x509_certificate_in_pem of this IdpCertificate.

        x509格式证书

        :return: The x509_certificate_in_pem of this IdpCertificate.
        :rtype: str
        """
        return self._x509_certificate_in_pem

    @x509_certificate_in_pem.setter
    def x509_certificate_in_pem(self, x509_certificate_in_pem):
        r"""Sets the x509_certificate_in_pem of this IdpCertificate.

        x509格式证书

        :param x509_certificate_in_pem: The x509_certificate_in_pem of this IdpCertificate.
        :type x509_certificate_in_pem: str
        """
        self._x509_certificate_in_pem = x509_certificate_in_pem

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
        if not isinstance(other, IdpCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
