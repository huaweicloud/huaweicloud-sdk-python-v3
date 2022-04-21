# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCertificateAuthorityRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'distinguished_name': 'DistinguishedName',
        'key_algorithm': 'str',
        'validity': 'Validity',
        'issuer_id': 'str',
        'path_length': 'int',
        'signature_algorithm': 'str',
        'key_usages': 'list[str]',
        'crl_configuration': 'CrlConfiguration'
    }

    attribute_map = {
        'type': 'type',
        'distinguished_name': 'distinguished_name',
        'key_algorithm': 'key_algorithm',
        'validity': 'validity',
        'issuer_id': 'issuer_id',
        'path_length': 'path_length',
        'signature_algorithm': 'signature_algorithm',
        'key_usages': 'key_usages',
        'crl_configuration': 'crl_configuration'
    }

    def __init__(self, type=None, distinguished_name=None, key_algorithm=None, validity=None, issuer_id=None, path_length=None, signature_algorithm=None, key_usages=None, crl_configuration=None):
        """CreateCertificateAuthorityRequestBody

        The model defined in huaweicloud sdk

        :param type: 创建的CA类型。 - **ROOT** : 根CA - **SUBORDINATE** : 从属CA
        :type type: str
        :param distinguished_name: 
        :type distinguished_name: :class:`huaweicloudsdkccm.v1.DistinguishedName`
        :param key_algorithm: 密钥算法，可选值如下：   - **RSA2048** : RSA算法，密钥长度2048位；   - **RSA4096** : RSA算法，密钥长度4096位；   - **EC256** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度256位；   - **EC384** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度384位。
        :type key_algorithm: str
        :param validity: 
        :type validity: :class:`huaweicloudsdkccm.v1.Validity`
        :param issuer_id: 父CA证书ID，分以下三种情况：   - 创建根CA，根CA为自签名证书，无父CA，将忽略该参数；   - 创建从属CA，并需要直接激活该证书，为必填值；   - 创建从属CA，不需要直接激活该证书，本参数值将被忽略，激活证书时需要再次传入。
        :type issuer_id: str
        :param path_length: CA证书路径长度，分以下三种情况：   - 创建根CA，为便于后期对证书层级的扩展，根CA默认不对路径长度做限制，故将忽略该参数。证书层级规划可由从属CA做限制；   - 创建从属CA，并需要直接激活该证书，用户可自定义。缺省值为0；   - 创建从属CA，不需要直接激活该证书，本参数值将被忽略。激活证书时若要自定义，需要再次传入；
        :type path_length: int
        :param signature_algorithm: 签名哈希算法。 - 分以下三种情况：   - 创建根CA，为必填值；   - 创建从属CA，并需要直接激活该证书，为必填值；   - 创建从属CA，不需要直接激活该证书，本参数值将被忽略，激活证书时需要再次传入。 - 可选值如下：   - **SHA256**   - **SHA384**   - **SHA512**
        :type signature_algorithm: str
        :param key_usages: 密钥用法，具体标准参见RFC 5280中:[4.2.1.3节](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3)。   - **digitalSignature** : 数字签名；   - **nonRepudiation** : 不可抵赖；   - **keyEncipherment** : 密钥用于加密密钥数据；   - **dataEncipherment** : 用于加密数据；   - **keyAgreement** : 密钥协商；   - **keyCertSign** : 签发证书；   - **cRLSign** : 签发吊销列表；   - **encipherOnly** : 仅用于加密；   - **decipherOnly** : 仅用于解密。 &gt; 缺省值如下： &gt; - 根CA证书：默认为**[digitalSignature,keyCertSign,cRLSign]**，忽略用户传入值； &gt; - 从属CA证书：默认为**[digitalSignature,keyCertSign,cRLSign]**，支持用户自定义。
        :type key_usages: list[str]
        :param crl_configuration: 
        :type crl_configuration: :class:`huaweicloudsdkccm.v1.CrlConfiguration`
        """
        
        

        self._type = None
        self._distinguished_name = None
        self._key_algorithm = None
        self._validity = None
        self._issuer_id = None
        self._path_length = None
        self._signature_algorithm = None
        self._key_usages = None
        self._crl_configuration = None
        self.discriminator = None

        self.type = type
        self.distinguished_name = distinguished_name
        self.key_algorithm = key_algorithm
        if validity is not None:
            self.validity = validity
        if issuer_id is not None:
            self.issuer_id = issuer_id
        if path_length is not None:
            self.path_length = path_length
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if key_usages is not None:
            self.key_usages = key_usages
        if crl_configuration is not None:
            self.crl_configuration = crl_configuration

    @property
    def type(self):
        """Gets the type of this CreateCertificateAuthorityRequestBody.

        创建的CA类型。 - **ROOT** : 根CA - **SUBORDINATE** : 从属CA

        :return: The type of this CreateCertificateAuthorityRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateCertificateAuthorityRequestBody.

        创建的CA类型。 - **ROOT** : 根CA - **SUBORDINATE** : 从属CA

        :param type: The type of this CreateCertificateAuthorityRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def distinguished_name(self):
        """Gets the distinguished_name of this CreateCertificateAuthorityRequestBody.


        :return: The distinguished_name of this CreateCertificateAuthorityRequestBody.
        :rtype: :class:`huaweicloudsdkccm.v1.DistinguishedName`
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        """Sets the distinguished_name of this CreateCertificateAuthorityRequestBody.


        :param distinguished_name: The distinguished_name of this CreateCertificateAuthorityRequestBody.
        :type distinguished_name: :class:`huaweicloudsdkccm.v1.DistinguishedName`
        """
        self._distinguished_name = distinguished_name

    @property
    def key_algorithm(self):
        """Gets the key_algorithm of this CreateCertificateAuthorityRequestBody.

        密钥算法，可选值如下：   - **RSA2048** : RSA算法，密钥长度2048位；   - **RSA4096** : RSA算法，密钥长度4096位；   - **EC256** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度256位；   - **EC384** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度384位。

        :return: The key_algorithm of this CreateCertificateAuthorityRequestBody.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """Sets the key_algorithm of this CreateCertificateAuthorityRequestBody.

        密钥算法，可选值如下：   - **RSA2048** : RSA算法，密钥长度2048位；   - **RSA4096** : RSA算法，密钥长度4096位；   - **EC256** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度256位；   - **EC384** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度384位。

        :param key_algorithm: The key_algorithm of this CreateCertificateAuthorityRequestBody.
        :type key_algorithm: str
        """
        self._key_algorithm = key_algorithm

    @property
    def validity(self):
        """Gets the validity of this CreateCertificateAuthorityRequestBody.


        :return: The validity of this CreateCertificateAuthorityRequestBody.
        :rtype: :class:`huaweicloudsdkccm.v1.Validity`
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this CreateCertificateAuthorityRequestBody.


        :param validity: The validity of this CreateCertificateAuthorityRequestBody.
        :type validity: :class:`huaweicloudsdkccm.v1.Validity`
        """
        self._validity = validity

    @property
    def issuer_id(self):
        """Gets the issuer_id of this CreateCertificateAuthorityRequestBody.

        父CA证书ID，分以下三种情况：   - 创建根CA，根CA为自签名证书，无父CA，将忽略该参数；   - 创建从属CA，并需要直接激活该证书，为必填值；   - 创建从属CA，不需要直接激活该证书，本参数值将被忽略，激活证书时需要再次传入。

        :return: The issuer_id of this CreateCertificateAuthorityRequestBody.
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this CreateCertificateAuthorityRequestBody.

        父CA证书ID，分以下三种情况：   - 创建根CA，根CA为自签名证书，无父CA，将忽略该参数；   - 创建从属CA，并需要直接激活该证书，为必填值；   - 创建从属CA，不需要直接激活该证书，本参数值将被忽略，激活证书时需要再次传入。

        :param issuer_id: The issuer_id of this CreateCertificateAuthorityRequestBody.
        :type issuer_id: str
        """
        self._issuer_id = issuer_id

    @property
    def path_length(self):
        """Gets the path_length of this CreateCertificateAuthorityRequestBody.

        CA证书路径长度，分以下三种情况：   - 创建根CA，为便于后期对证书层级的扩展，根CA默认不对路径长度做限制，故将忽略该参数。证书层级规划可由从属CA做限制；   - 创建从属CA，并需要直接激活该证书，用户可自定义。缺省值为0；   - 创建从属CA，不需要直接激活该证书，本参数值将被忽略。激活证书时若要自定义，需要再次传入；

        :return: The path_length of this CreateCertificateAuthorityRequestBody.
        :rtype: int
        """
        return self._path_length

    @path_length.setter
    def path_length(self, path_length):
        """Sets the path_length of this CreateCertificateAuthorityRequestBody.

        CA证书路径长度，分以下三种情况：   - 创建根CA，为便于后期对证书层级的扩展，根CA默认不对路径长度做限制，故将忽略该参数。证书层级规划可由从属CA做限制；   - 创建从属CA，并需要直接激活该证书，用户可自定义。缺省值为0；   - 创建从属CA，不需要直接激活该证书，本参数值将被忽略。激活证书时若要自定义，需要再次传入；

        :param path_length: The path_length of this CreateCertificateAuthorityRequestBody.
        :type path_length: int
        """
        self._path_length = path_length

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this CreateCertificateAuthorityRequestBody.

        签名哈希算法。 - 分以下三种情况：   - 创建根CA，为必填值；   - 创建从属CA，并需要直接激活该证书，为必填值；   - 创建从属CA，不需要直接激活该证书，本参数值将被忽略，激活证书时需要再次传入。 - 可选值如下：   - **SHA256**   - **SHA384**   - **SHA512**

        :return: The signature_algorithm of this CreateCertificateAuthorityRequestBody.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this CreateCertificateAuthorityRequestBody.

        签名哈希算法。 - 分以下三种情况：   - 创建根CA，为必填值；   - 创建从属CA，并需要直接激活该证书，为必填值；   - 创建从属CA，不需要直接激活该证书，本参数值将被忽略，激活证书时需要再次传入。 - 可选值如下：   - **SHA256**   - **SHA384**   - **SHA512**

        :param signature_algorithm: The signature_algorithm of this CreateCertificateAuthorityRequestBody.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def key_usages(self):
        """Gets the key_usages of this CreateCertificateAuthorityRequestBody.

        密钥用法，具体标准参见RFC 5280中:[4.2.1.3节](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3)。   - **digitalSignature** : 数字签名；   - **nonRepudiation** : 不可抵赖；   - **keyEncipherment** : 密钥用于加密密钥数据；   - **dataEncipherment** : 用于加密数据；   - **keyAgreement** : 密钥协商；   - **keyCertSign** : 签发证书；   - **cRLSign** : 签发吊销列表；   - **encipherOnly** : 仅用于加密；   - **decipherOnly** : 仅用于解密。 > 缺省值如下： > - 根CA证书：默认为**[digitalSignature,keyCertSign,cRLSign]**，忽略用户传入值； > - 从属CA证书：默认为**[digitalSignature,keyCertSign,cRLSign]**，支持用户自定义。

        :return: The key_usages of this CreateCertificateAuthorityRequestBody.
        :rtype: list[str]
        """
        return self._key_usages

    @key_usages.setter
    def key_usages(self, key_usages):
        """Sets the key_usages of this CreateCertificateAuthorityRequestBody.

        密钥用法，具体标准参见RFC 5280中:[4.2.1.3节](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3)。   - **digitalSignature** : 数字签名；   - **nonRepudiation** : 不可抵赖；   - **keyEncipherment** : 密钥用于加密密钥数据；   - **dataEncipherment** : 用于加密数据；   - **keyAgreement** : 密钥协商；   - **keyCertSign** : 签发证书；   - **cRLSign** : 签发吊销列表；   - **encipherOnly** : 仅用于加密；   - **decipherOnly** : 仅用于解密。 > 缺省值如下： > - 根CA证书：默认为**[digitalSignature,keyCertSign,cRLSign]**，忽略用户传入值； > - 从属CA证书：默认为**[digitalSignature,keyCertSign,cRLSign]**，支持用户自定义。

        :param key_usages: The key_usages of this CreateCertificateAuthorityRequestBody.
        :type key_usages: list[str]
        """
        self._key_usages = key_usages

    @property
    def crl_configuration(self):
        """Gets the crl_configuration of this CreateCertificateAuthorityRequestBody.


        :return: The crl_configuration of this CreateCertificateAuthorityRequestBody.
        :rtype: :class:`huaweicloudsdkccm.v1.CrlConfiguration`
        """
        return self._crl_configuration

    @crl_configuration.setter
    def crl_configuration(self, crl_configuration):
        """Sets the crl_configuration of this CreateCertificateAuthorityRequestBody.


        :param crl_configuration: The crl_configuration of this CreateCertificateAuthorityRequestBody.
        :type crl_configuration: :class:`huaweicloudsdkccm.v1.CrlConfiguration`
        """
        self._crl_configuration = crl_configuration

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
        if not isinstance(other, CreateCertificateAuthorityRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
