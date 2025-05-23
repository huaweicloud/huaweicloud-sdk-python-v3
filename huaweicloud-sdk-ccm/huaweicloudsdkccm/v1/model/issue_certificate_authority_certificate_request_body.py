# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueCertificateAuthorityCertificateRequestBody:

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
        'path_length': 'int',
        'signature_algorithm': 'str',
        'validity': 'Validity',
        'type': 'str',
        'distinguished_name': 'DistinguishedName',
        'key_algorithm': 'str',
        'key_usages': 'list[str]',
        'crl_configuration': 'CrlConfiguration',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'issuer_id': 'issuer_id',
        'path_length': 'path_length',
        'signature_algorithm': 'signature_algorithm',
        'validity': 'validity',
        'type': 'type',
        'distinguished_name': 'distinguished_name',
        'key_algorithm': 'key_algorithm',
        'key_usages': 'key_usages',
        'crl_configuration': 'crl_configuration',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, issuer_id=None, path_length=None, signature_algorithm=None, validity=None, type=None, distinguished_name=None, key_algorithm=None, key_usages=None, crl_configuration=None, enterprise_project_id=None):
        r"""IssueCertificateAuthorityCertificateRequestBody

        The model defined in huaweicloud sdk

        :param issuer_id: 父CA证书ID。
        :type issuer_id: str
        :param path_length: 路径长度。
        :type path_length: int
        :param signature_algorithm: 签名哈希算法，可选值如下：   - **SHA256**   - **SHA384**   - **SHA512**   - **SM3**（中国站）
        :type signature_algorithm: str
        :param validity: 
        :type validity: :class:`huaweicloudsdkccm.v1.Validity`
        :param type: 创建的CA类型。（如果激活包周期CA，为必填值） - **ROOT** : 根CA - **SUBORDINATE** : 从属CA
        :type type: str
        :param distinguished_name: 
        :type distinguished_name: :class:`huaweicloudsdkccm.v1.DistinguishedName`
        :param key_algorithm: 密钥算法（如果激活包周期CA，为必填值），可选值如下：   - **RSA2048** : RSA算法，密钥长度2048位；   - **RSA4096** : RSA算法，密钥长度4096位；   - **EC256** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度256位；   - **EC384** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度384位；   - **SM2** : 国家密码管理局颁发的椭圆曲线算法（签名哈希算法SM3），密钥长度256位。（中国站）
        :type key_algorithm: str
        :param key_usages: 密钥用法，具体标准参见RFC 5280中:[4.2.1.3节](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3)。   - **digitalSignature** : 数字签名；   - **nonRepudiation** : 不可抵赖；   - **keyEncipherment** : 密钥用于加密密钥数据；   - **dataEncipherment** : 用于加密数据；   - **keyAgreement** : 密钥协商；   - **keyCertSign** : 签发证书；   - **cRLSign** : 签发吊销列表；   - **encipherOnly** : 仅用于加密；   - **decipherOnly** : 仅用于解密。 &gt; 缺省值如下： &gt; - 根CA证书：默认为**[digitalSignature,keyCertSign,cRLSign]**，忽略用户传入值； &gt; - 从属CA证书：默认为**[digitalSignature,keyCertSign,cRLSign]**，支持用户自定义。
        :type key_usages: list[str]
        :param crl_configuration: 
        :type crl_configuration: :class:`huaweicloudsdkccm.v1.CrlConfiguration`
        :param enterprise_project_id: 企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.   取值为“all”   取值为“0”   满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”
        :type enterprise_project_id: str
        """
        
        

        self._issuer_id = None
        self._path_length = None
        self._signature_algorithm = None
        self._validity = None
        self._type = None
        self._distinguished_name = None
        self._key_algorithm = None
        self._key_usages = None
        self._crl_configuration = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.issuer_id = issuer_id
        self.path_length = path_length
        self.signature_algorithm = signature_algorithm
        self.validity = validity
        if type is not None:
            self.type = type
        if distinguished_name is not None:
            self.distinguished_name = distinguished_name
        if key_algorithm is not None:
            self.key_algorithm = key_algorithm
        if key_usages is not None:
            self.key_usages = key_usages
        if crl_configuration is not None:
            self.crl_configuration = crl_configuration
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def issuer_id(self):
        r"""Gets the issuer_id of this IssueCertificateAuthorityCertificateRequestBody.

        父CA证书ID。

        :return: The issuer_id of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        r"""Sets the issuer_id of this IssueCertificateAuthorityCertificateRequestBody.

        父CA证书ID。

        :param issuer_id: The issuer_id of this IssueCertificateAuthorityCertificateRequestBody.
        :type issuer_id: str
        """
        self._issuer_id = issuer_id

    @property
    def path_length(self):
        r"""Gets the path_length of this IssueCertificateAuthorityCertificateRequestBody.

        路径长度。

        :return: The path_length of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: int
        """
        return self._path_length

    @path_length.setter
    def path_length(self, path_length):
        r"""Sets the path_length of this IssueCertificateAuthorityCertificateRequestBody.

        路径长度。

        :param path_length: The path_length of this IssueCertificateAuthorityCertificateRequestBody.
        :type path_length: int
        """
        self._path_length = path_length

    @property
    def signature_algorithm(self):
        r"""Gets the signature_algorithm of this IssueCertificateAuthorityCertificateRequestBody.

        签名哈希算法，可选值如下：   - **SHA256**   - **SHA384**   - **SHA512**   - **SM3**（中国站）

        :return: The signature_algorithm of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        r"""Sets the signature_algorithm of this IssueCertificateAuthorityCertificateRequestBody.

        签名哈希算法，可选值如下：   - **SHA256**   - **SHA384**   - **SHA512**   - **SM3**（中国站）

        :param signature_algorithm: The signature_algorithm of this IssueCertificateAuthorityCertificateRequestBody.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def validity(self):
        r"""Gets the validity of this IssueCertificateAuthorityCertificateRequestBody.

        :return: The validity of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: :class:`huaweicloudsdkccm.v1.Validity`
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        r"""Sets the validity of this IssueCertificateAuthorityCertificateRequestBody.

        :param validity: The validity of this IssueCertificateAuthorityCertificateRequestBody.
        :type validity: :class:`huaweicloudsdkccm.v1.Validity`
        """
        self._validity = validity

    @property
    def type(self):
        r"""Gets the type of this IssueCertificateAuthorityCertificateRequestBody.

        创建的CA类型。（如果激活包周期CA，为必填值） - **ROOT** : 根CA - **SUBORDINATE** : 从属CA

        :return: The type of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IssueCertificateAuthorityCertificateRequestBody.

        创建的CA类型。（如果激活包周期CA，为必填值） - **ROOT** : 根CA - **SUBORDINATE** : 从属CA

        :param type: The type of this IssueCertificateAuthorityCertificateRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def distinguished_name(self):
        r"""Gets the distinguished_name of this IssueCertificateAuthorityCertificateRequestBody.

        :return: The distinguished_name of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: :class:`huaweicloudsdkccm.v1.DistinguishedName`
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        r"""Sets the distinguished_name of this IssueCertificateAuthorityCertificateRequestBody.

        :param distinguished_name: The distinguished_name of this IssueCertificateAuthorityCertificateRequestBody.
        :type distinguished_name: :class:`huaweicloudsdkccm.v1.DistinguishedName`
        """
        self._distinguished_name = distinguished_name

    @property
    def key_algorithm(self):
        r"""Gets the key_algorithm of this IssueCertificateAuthorityCertificateRequestBody.

        密钥算法（如果激活包周期CA，为必填值），可选值如下：   - **RSA2048** : RSA算法，密钥长度2048位；   - **RSA4096** : RSA算法，密钥长度4096位；   - **EC256** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度256位；   - **EC384** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度384位；   - **SM2** : 国家密码管理局颁发的椭圆曲线算法（签名哈希算法SM3），密钥长度256位。（中国站）

        :return: The key_algorithm of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        r"""Sets the key_algorithm of this IssueCertificateAuthorityCertificateRequestBody.

        密钥算法（如果激活包周期CA，为必填值），可选值如下：   - **RSA2048** : RSA算法，密钥长度2048位；   - **RSA4096** : RSA算法，密钥长度4096位；   - **EC256** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度256位；   - **EC384** : 椭圆曲线算法（Elliptic Curve Digital Signature Algorithm (ECDSA)），密钥长度384位；   - **SM2** : 国家密码管理局颁发的椭圆曲线算法（签名哈希算法SM3），密钥长度256位。（中国站）

        :param key_algorithm: The key_algorithm of this IssueCertificateAuthorityCertificateRequestBody.
        :type key_algorithm: str
        """
        self._key_algorithm = key_algorithm

    @property
    def key_usages(self):
        r"""Gets the key_usages of this IssueCertificateAuthorityCertificateRequestBody.

        密钥用法，具体标准参见RFC 5280中:[4.2.1.3节](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3)。   - **digitalSignature** : 数字签名；   - **nonRepudiation** : 不可抵赖；   - **keyEncipherment** : 密钥用于加密密钥数据；   - **dataEncipherment** : 用于加密数据；   - **keyAgreement** : 密钥协商；   - **keyCertSign** : 签发证书；   - **cRLSign** : 签发吊销列表；   - **encipherOnly** : 仅用于加密；   - **decipherOnly** : 仅用于解密。 > 缺省值如下： > - 根CA证书：默认为**[digitalSignature,keyCertSign,cRLSign]**，忽略用户传入值； > - 从属CA证书：默认为**[digitalSignature,keyCertSign,cRLSign]**，支持用户自定义。

        :return: The key_usages of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: list[str]
        """
        return self._key_usages

    @key_usages.setter
    def key_usages(self, key_usages):
        r"""Sets the key_usages of this IssueCertificateAuthorityCertificateRequestBody.

        密钥用法，具体标准参见RFC 5280中:[4.2.1.3节](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3)。   - **digitalSignature** : 数字签名；   - **nonRepudiation** : 不可抵赖；   - **keyEncipherment** : 密钥用于加密密钥数据；   - **dataEncipherment** : 用于加密数据；   - **keyAgreement** : 密钥协商；   - **keyCertSign** : 签发证书；   - **cRLSign** : 签发吊销列表；   - **encipherOnly** : 仅用于加密；   - **decipherOnly** : 仅用于解密。 > 缺省值如下： > - 根CA证书：默认为**[digitalSignature,keyCertSign,cRLSign]**，忽略用户传入值； > - 从属CA证书：默认为**[digitalSignature,keyCertSign,cRLSign]**，支持用户自定义。

        :param key_usages: The key_usages of this IssueCertificateAuthorityCertificateRequestBody.
        :type key_usages: list[str]
        """
        self._key_usages = key_usages

    @property
    def crl_configuration(self):
        r"""Gets the crl_configuration of this IssueCertificateAuthorityCertificateRequestBody.

        :return: The crl_configuration of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: :class:`huaweicloudsdkccm.v1.CrlConfiguration`
        """
        return self._crl_configuration

    @crl_configuration.setter
    def crl_configuration(self, crl_configuration):
        r"""Sets the crl_configuration of this IssueCertificateAuthorityCertificateRequestBody.

        :param crl_configuration: The crl_configuration of this IssueCertificateAuthorityCertificateRequestBody.
        :type crl_configuration: :class:`huaweicloudsdkccm.v1.CrlConfiguration`
        """
        self._crl_configuration = crl_configuration

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this IssueCertificateAuthorityCertificateRequestBody.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.   取值为“all”   取值为“0”   满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :return: The enterprise_project_id of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this IssueCertificateAuthorityCertificateRequestBody.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.   取值为“all”   取值为“0”   满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :param enterprise_project_id: The enterprise_project_id of this IssueCertificateAuthorityCertificateRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, IssueCertificateAuthorityCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
