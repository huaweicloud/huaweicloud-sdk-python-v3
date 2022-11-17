# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCertificateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issuer_id': 'str',
        'key_algorithm': 'str',
        'signature_algorithm': 'str',
        'distinguished_name': 'CertDistinguishedName',
        'validity': 'Validity',
        'key_usages': 'list[str]',
        'subject_alternative_names': 'list[SubjectAlternativeName]',
        'extended_key_usage': 'ExtendedKeyUsage',
        'customized_extension': 'CustomizedExtension'
    }

    attribute_map = {
        'issuer_id': 'issuer_id',
        'key_algorithm': 'key_algorithm',
        'signature_algorithm': 'signature_algorithm',
        'distinguished_name': 'distinguished_name',
        'validity': 'validity',
        'key_usages': 'key_usages',
        'subject_alternative_names': 'subject_alternative_names',
        'extended_key_usage': 'extended_key_usage',
        'customized_extension': 'customized_extension'
    }

    def __init__(self, issuer_id=None, key_algorithm=None, signature_algorithm=None, distinguished_name=None, validity=None, key_usages=None, subject_alternative_names=None, extended_key_usage=None, customized_extension=None):
        """CreateCertificateRequestBody

        The model defined in huaweicloud sdk

        :param issuer_id: 父CA证书ID。
        :type issuer_id: str
        :param key_algorithm: 密钥算法，可选值如下：   - **RSA2048** : RSA算法，密钥长度2048位；   - **RSA4096** : RSA算法，密钥长度4096位；   - **EC256** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度256位；   - **EC384** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度384位。
        :type key_algorithm: str
        :param signature_algorithm: 签名哈希算法，可选值如下：   - **SHA256**   - **SHA384**   - **SHA512**
        :type signature_algorithm: str
        :param distinguished_name: 
        :type distinguished_name: :class:`huaweicloudsdkccm.v1.CertDistinguishedName`
        :param validity: 
        :type validity: :class:`huaweicloudsdkccm.v1.Validity`
        :param key_usages: 密钥用法，具体标准参见RFC 5280中:[4.2.1.3节](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3)。   - **digitalSignature** : 数字签名；   - **nonRepudiation** : 不可抵赖；   - **keyEncipherment** : 密钥用于加密密钥数据；   - **dataEncipherment** : 用于加密数据；   - **keyAgreement** : 密钥协商；   - **keyCertSign** : 签发证书；   - **cRLSign** : 签发吊销列表；   - **encipherOnly** : 仅用于加密；   - **decipherOnly** : 仅用于解密。
        :type key_usages: list[str]
        :param subject_alternative_names: 主体备用名称，详情请参见**SubjectAlternativeName**字段数据结构说明。   - array大小：[0,20]。
        :type subject_alternative_names: list[:class:`huaweicloudsdkccm.v1.SubjectAlternativeName`]
        :param extended_key_usage: 
        :type extended_key_usage: :class:`huaweicloudsdkccm.v1.ExtendedKeyUsage`
        :param customized_extension: 
        :type customized_extension: :class:`huaweicloudsdkccm.v1.CustomizedExtension`
        """
        
        

        self._issuer_id = None
        self._key_algorithm = None
        self._signature_algorithm = None
        self._distinguished_name = None
        self._validity = None
        self._key_usages = None
        self._subject_alternative_names = None
        self._extended_key_usage = None
        self._customized_extension = None
        self.discriminator = None

        self.issuer_id = issuer_id
        self.key_algorithm = key_algorithm
        self.signature_algorithm = signature_algorithm
        self.distinguished_name = distinguished_name
        self.validity = validity
        if key_usages is not None:
            self.key_usages = key_usages
        if subject_alternative_names is not None:
            self.subject_alternative_names = subject_alternative_names
        if extended_key_usage is not None:
            self.extended_key_usage = extended_key_usage
        if customized_extension is not None:
            self.customized_extension = customized_extension

    @property
    def issuer_id(self):
        """Gets the issuer_id of this CreateCertificateRequestBody.

        父CA证书ID。

        :return: The issuer_id of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this CreateCertificateRequestBody.

        父CA证书ID。

        :param issuer_id: The issuer_id of this CreateCertificateRequestBody.
        :type issuer_id: str
        """
        self._issuer_id = issuer_id

    @property
    def key_algorithm(self):
        """Gets the key_algorithm of this CreateCertificateRequestBody.

        密钥算法，可选值如下：   - **RSA2048** : RSA算法，密钥长度2048位；   - **RSA4096** : RSA算法，密钥长度4096位；   - **EC256** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度256位；   - **EC384** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度384位。

        :return: The key_algorithm of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """Sets the key_algorithm of this CreateCertificateRequestBody.

        密钥算法，可选值如下：   - **RSA2048** : RSA算法，密钥长度2048位；   - **RSA4096** : RSA算法，密钥长度4096位；   - **EC256** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度256位；   - **EC384** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度384位。

        :param key_algorithm: The key_algorithm of this CreateCertificateRequestBody.
        :type key_algorithm: str
        """
        self._key_algorithm = key_algorithm

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this CreateCertificateRequestBody.

        签名哈希算法，可选值如下：   - **SHA256**   - **SHA384**   - **SHA512**

        :return: The signature_algorithm of this CreateCertificateRequestBody.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this CreateCertificateRequestBody.

        签名哈希算法，可选值如下：   - **SHA256**   - **SHA384**   - **SHA512**

        :param signature_algorithm: The signature_algorithm of this CreateCertificateRequestBody.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def distinguished_name(self):
        """Gets the distinguished_name of this CreateCertificateRequestBody.

        :return: The distinguished_name of this CreateCertificateRequestBody.
        :rtype: :class:`huaweicloudsdkccm.v1.CertDistinguishedName`
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        """Sets the distinguished_name of this CreateCertificateRequestBody.

        :param distinguished_name: The distinguished_name of this CreateCertificateRequestBody.
        :type distinguished_name: :class:`huaweicloudsdkccm.v1.CertDistinguishedName`
        """
        self._distinguished_name = distinguished_name

    @property
    def validity(self):
        """Gets the validity of this CreateCertificateRequestBody.

        :return: The validity of this CreateCertificateRequestBody.
        :rtype: :class:`huaweicloudsdkccm.v1.Validity`
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this CreateCertificateRequestBody.

        :param validity: The validity of this CreateCertificateRequestBody.
        :type validity: :class:`huaweicloudsdkccm.v1.Validity`
        """
        self._validity = validity

    @property
    def key_usages(self):
        """Gets the key_usages of this CreateCertificateRequestBody.

        密钥用法，具体标准参见RFC 5280中:[4.2.1.3节](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3)。   - **digitalSignature** : 数字签名；   - **nonRepudiation** : 不可抵赖；   - **keyEncipherment** : 密钥用于加密密钥数据；   - **dataEncipherment** : 用于加密数据；   - **keyAgreement** : 密钥协商；   - **keyCertSign** : 签发证书；   - **cRLSign** : 签发吊销列表；   - **encipherOnly** : 仅用于加密；   - **decipherOnly** : 仅用于解密。

        :return: The key_usages of this CreateCertificateRequestBody.
        :rtype: list[str]
        """
        return self._key_usages

    @key_usages.setter
    def key_usages(self, key_usages):
        """Sets the key_usages of this CreateCertificateRequestBody.

        密钥用法，具体标准参见RFC 5280中:[4.2.1.3节](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3)。   - **digitalSignature** : 数字签名；   - **nonRepudiation** : 不可抵赖；   - **keyEncipherment** : 密钥用于加密密钥数据；   - **dataEncipherment** : 用于加密数据；   - **keyAgreement** : 密钥协商；   - **keyCertSign** : 签发证书；   - **cRLSign** : 签发吊销列表；   - **encipherOnly** : 仅用于加密；   - **decipherOnly** : 仅用于解密。

        :param key_usages: The key_usages of this CreateCertificateRequestBody.
        :type key_usages: list[str]
        """
        self._key_usages = key_usages

    @property
    def subject_alternative_names(self):
        """Gets the subject_alternative_names of this CreateCertificateRequestBody.

        主体备用名称，详情请参见**SubjectAlternativeName**字段数据结构说明。   - array大小：[0,20]。

        :return: The subject_alternative_names of this CreateCertificateRequestBody.
        :rtype: list[:class:`huaweicloudsdkccm.v1.SubjectAlternativeName`]
        """
        return self._subject_alternative_names

    @subject_alternative_names.setter
    def subject_alternative_names(self, subject_alternative_names):
        """Sets the subject_alternative_names of this CreateCertificateRequestBody.

        主体备用名称，详情请参见**SubjectAlternativeName**字段数据结构说明。   - array大小：[0,20]。

        :param subject_alternative_names: The subject_alternative_names of this CreateCertificateRequestBody.
        :type subject_alternative_names: list[:class:`huaweicloudsdkccm.v1.SubjectAlternativeName`]
        """
        self._subject_alternative_names = subject_alternative_names

    @property
    def extended_key_usage(self):
        """Gets the extended_key_usage of this CreateCertificateRequestBody.

        :return: The extended_key_usage of this CreateCertificateRequestBody.
        :rtype: :class:`huaweicloudsdkccm.v1.ExtendedKeyUsage`
        """
        return self._extended_key_usage

    @extended_key_usage.setter
    def extended_key_usage(self, extended_key_usage):
        """Sets the extended_key_usage of this CreateCertificateRequestBody.

        :param extended_key_usage: The extended_key_usage of this CreateCertificateRequestBody.
        :type extended_key_usage: :class:`huaweicloudsdkccm.v1.ExtendedKeyUsage`
        """
        self._extended_key_usage = extended_key_usage

    @property
    def customized_extension(self):
        """Gets the customized_extension of this CreateCertificateRequestBody.

        :return: The customized_extension of this CreateCertificateRequestBody.
        :rtype: :class:`huaweicloudsdkccm.v1.CustomizedExtension`
        """
        return self._customized_extension

    @customized_extension.setter
    def customized_extension(self, customized_extension):
        """Sets the customized_extension of this CreateCertificateRequestBody.

        :param customized_extension: The customized_extension of this CreateCertificateRequestBody.
        :type customized_extension: :class:`huaweicloudsdkccm.v1.CustomizedExtension`
        """
        self._customized_extension = customized_extension

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
        if not isinstance(other, CreateCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
